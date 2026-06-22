#!/usr/bin/env python3
"""Build a translated-PDF prototype from page images, Surya layout, and translations.

This is intentionally a prototype renderer, not a final book-designer.  It uses a
hybrid strategy:

1. draw the refined crop as the page background;
2. cover OCR text/layout blocks with white rectangles;
3. flow the page-level English translation through those block rectangles in
   reading order;
4. leave picture/image regions untouched.

The result is useful for reviewing whether the translated-book reconstruction
approach is viable while preserving original illustrations and page structure.
"""

from __future__ import annotations

import argparse
import json
import re
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

from PIL import Image
from reportlab.lib.colors import Color, black, white
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


TEXT_LABELS = {
    "Text",
    "SectionHeader",
    "Title",
    "Caption",
    "List",
    "Table",
    "TableOfContents",
    "Footnote",
    "Formula",
}


@dataclass(frozen=True)
class Box:
    label: str
    reading_order: int
    bbox_px: tuple[float, float, float, float]


@dataclass
class PageRenderStats:
    page: int
    source_image: str
    text_boxes: int
    font_size: float
    remaining_tokens: int
    used_fallback_box: bool
    translation_chars: int


def parse_pages(value: str | None, total: int) -> list[int]:
    if not value:
        return list(range(1, total + 1))
    pages: set[int] = set()
    for part in value.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start_s, end_s = part.split("-", 1)
            start, end = int(start_s), int(end_s)
            pages.update(range(start, end + 1))
        else:
            pages.add(int(part))
    return sorted(p for p in pages if 1 <= p <= total)


def load_translation_records(path: Path) -> dict[int, dict]:
    rows: dict[int, dict] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        rows[int(record["page"])] = record
    return rows


def load_pdf_order(path: Path) -> list[str]:
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def load_layout(path: Path) -> dict[int, list[Box]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    pages: dict[int, list[Box]] = {}
    for key, value in data.items():
        page = int(key.split("__", 1)[0])
        if not value:
            pages[page] = []
            continue
        blocks = value[0].get("blocks", [])
        boxes: list[Box] = []
        for block in blocks:
            label = block.get("label") or block.get("raw_label") or "Text"
            if block.get("skipped") and label == "Picture":
                continue
            if label == "Picture" or block.get("raw_label") == "Image":
                continue
            bbox = block.get("bbox")
            if not bbox or len(bbox) != 4:
                continue
            x0, y0, x1, y1 = [float(v) for v in bbox]
            if x1 <= x0 or y1 <= y0:
                continue
            # Ignore tiny specks, but keep small page numbers/headings.
            if (x1 - x0) < 8 or (y1 - y0) < 8:
                continue
            boxes.append(
                Box(
                    label=label,
                    reading_order=int(block.get("reading_order") or 0),
                    bbox_px=(x0, y0, x1, y1),
                )
            )
        pages[page] = sorted(boxes, key=lambda b: (b.reading_order, b.bbox_px[1], b.bbox_px[0]))
    return pages


def register_font(font_path: Path | None) -> str:
    candidates = [
        font_path,
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
        Path("/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf"),
    ]
    for candidate in candidates:
        if candidate and candidate.exists():
            pdfmetrics.registerFont(TTFont("PrototypeSans", str(candidate)))
            return "PrototypeSans"
    return "Helvetica"


def make_background_reader(image_path: Path, quality: int) -> tuple[ImageReader, tempfile.NamedTemporaryFile | None, int, int]:
    image = Image.open(image_path).convert("RGB")
    width, height = image.size
    if quality >= 100:
        return ImageReader(image), None, width, height
    tmp = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
    image.save(tmp.name, format="JPEG", quality=quality, optimize=True)
    tmp.close()
    return ImageReader(tmp.name), tmp, width, height


def tokenize(text: str) -> list[str]:
    tokens: list[str] = []
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text.strip())]
    for paragraph in paragraphs:
        if not paragraph:
            continue
        tokens.extend(paragraph.split())
        tokens.append("\n")
    return tokens


def pt_box_from_px(
    bbox: tuple[float, float, float, float],
    page_height_pt: float,
    scale: float,
    pad_pt: float,
) -> tuple[float, float, float, float]:
    x0, y0, x1, y1 = bbox
    x = x0 * scale - pad_pt
    y = page_height_pt - y1 * scale - pad_pt
    w = (x1 - x0) * scale + 2 * pad_pt
    h = (y1 - y0) * scale + 2 * pad_pt
    return x, y, w, h


def wrap_line(font_name: str, font_size: float, words: list[str], width: float) -> tuple[str, int]:
    if not words:
        return "", 0
    line_words: list[str] = []
    used = 0
    for word in words:
        candidate = " ".join([*line_words, word]) if line_words else word
        if pdfmetrics.stringWidth(candidate, font_name, font_size) <= width or not line_words:
            line_words.append(word)
            used += 1
        else:
            break
    return " ".join(line_words), used


def draw_tokens_in_box(
    c: canvas.Canvas,
    tokens: list[str],
    x: float,
    y: float,
    w: float,
    h: float,
    font_name: str,
    font_size: float,
    draw: bool,
) -> list[str]:
    if w <= 4 or h <= 4:
        return tokens
    line_height = font_size * 1.18
    max_lines = max(0, int((h - 2) // line_height))
    if max_lines <= 0:
        return tokens

    remaining = list(tokens)
    current_y = y + h - line_height
    if draw:
        c.setFont(font_name, font_size)
        c.setFillColor(black)

    for _ in range(max_lines):
        # Paragraph break.
        while remaining and remaining[0] == "\n":
            remaining.pop(0)
            current_y -= line_height * 0.45
            if current_y < y:
                return remaining
        if not remaining:
            return remaining
        words: list[str] = []
        for token in remaining:
            if token == "\n":
                break
            words.append(token)
        if not words:
            continue
        line, used = wrap_line(font_name, font_size, words, w - 3)
        if not line or used <= 0:
            return remaining
        if draw:
            c.drawString(x + 1.5, current_y, line)
        del remaining[:used]
        current_y -= line_height
        if current_y < y:
            break
    return remaining


def simulate_fit(tokens: list[str], boxes: Sequence[tuple[float, float, float, float]], font_name: str, font_size: float) -> int:
    remaining = list(tokens)
    for x, y, w, h in boxes:
        remaining = draw_tokens_in_box(canvas.Canvas(tempfile.TemporaryFile()), remaining, x, y, w, h, font_name, font_size, False)
        if not remaining:
            return 0
    return len([t for t in remaining if t != "\n"])


def choose_font_size(tokens: list[str], boxes: Sequence[tuple[float, float, float, float]], font_name: str) -> float:
    for size in (8.0, 7.5, 7.0, 6.5, 6.0, 5.5, 5.0, 4.5, 4.0):
        if simulate_fit(tokens, boxes, font_name, size) == 0:
            return size
    return 4.0


def make_fallback_box(page_width_pt: float, page_height_pt: float) -> tuple[float, float, float, float]:
    margin_x = page_width_pt * 0.09
    margin_y = page_height_pt * 0.08
    return margin_x, margin_y, page_width_pt - 2 * margin_x, page_height_pt * 0.26


def render_page(
    c: canvas.Canvas,
    page: int,
    image_name: str,
    image_path: Path,
    boxes: list[Box],
    translation: str,
    font_name: str,
    dpi: int,
    image_quality: int,
    debug: bool,
) -> PageRenderStats:
    bg_reader, tmp, width_px, height_px = make_background_reader(image_path, image_quality)
    scale = 72.0 / dpi
    page_width_pt = width_px * scale
    page_height_pt = height_px * scale
    c.setPageSize((page_width_pt, page_height_pt))
    c.drawImage(bg_reader, 0, 0, page_width_pt, page_height_pt, preserveAspectRatio=False, mask="auto")

    pt_boxes = [pt_box_from_px(box.bbox_px, page_height_pt, scale, pad_pt=1.25) for box in boxes]
    # If Surya found no text blocks, use one readable page-level box.
    if not pt_boxes:
        pt_boxes = [make_fallback_box(page_width_pt, page_height_pt)]

    tokens = tokenize(translation)
    font_size = choose_font_size(tokens, pt_boxes, font_name)

    # White-out text regions.  Keep image/picture regions intact by never
    # covering blocks labelled Picture/Image.
    c.setFillColor(white)
    for x, y, w, h in pt_boxes:
        c.rect(x, y, w, h, stroke=0, fill=1)
        if debug:
            c.setStrokeColor(Color(1, 0, 0, alpha=0.65))
            c.rect(x, y, w, h, stroke=1, fill=0)
            c.setFillColor(white)

    remaining = list(tokens)
    for x, y, w, h in pt_boxes:
        remaining = draw_tokens_in_box(c, remaining, x, y, w, h, font_name, font_size, True)
        if not remaining:
            break

    used_fallback = False
    remaining_words = len([t for t in remaining if t != "\n"])
    if remaining_words:
        used_fallback = True
        x, y, w, h = make_fallback_box(page_width_pt, page_height_pt)
        c.setFillColor(Color(1, 1, 0.86))
        c.rect(x, y, w, h, stroke=0, fill=1)
        c.setStrokeColor(Color(0.7, 0.55, 0.0))
        c.rect(x, y, w, h, stroke=1, fill=0)
        remaining = draw_tokens_in_box(c, remaining, x + 2, y + 2, w - 4, h - 4, font_name, 5.0, True)
        remaining_words = len([t for t in remaining if t != "\n"])

    # Small provenance footer in non-image margin if possible.
    c.setFillColor(Color(0.25, 0.25, 0.25))
    c.setFont(font_name, 4.0)
    c.drawRightString(page_width_pt - 4, 4, f"machine translation prototype · page {page:03d}")
    c.showPage()
    if tmp is not None:
        Path(tmp.name).unlink(missing_ok=True)
    return PageRenderStats(
        page=page,
        source_image=image_name,
        text_boxes=len(boxes),
        font_size=font_size,
        remaining_tokens=remaining_words,
        used_fallback_box=used_fallback,
        translation_chars=len(translation),
    )


def write_summary(path: Path, stats: Sequence[PageRenderStats], args: argparse.Namespace) -> None:
    payload = {
        "renderer": "make_translated_pdf_prototype.py",
        "strategy": "hybrid-image-background-surya-text-block-whiteout-page-translation-flow",
        "output_pdf": str(args.output),
        "pages": [s.__dict__ for s in stats],
        "page_count": len(stats),
        "fallback_pages": [s.page for s in stats if s.used_fallback_box],
        "overflow_pages": [s.page for s in stats if s.remaining_tokens > 0],
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--images-dir", type=Path, default=Path("dist/crops/refined"))
    parser.add_argument("--pdf-order", type=Path, default=Path("dist/pdforder.txt"))
    parser.add_argument("--layout-json", type=Path, default=Path("dist/metadata/ocr-bakeoff/surya-full/results.json"))
    parser.add_argument("--translations", type=Path, default=Path("dist/text/translation-local/qwen2_5_7b_instruct/translation-records.jsonl"))
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--summary-json", type=Path, default=None)
    parser.add_argument("--pages", help="Comma/range page selection, e.g. 1-5,50,100")
    parser.add_argument("--dpi", type=int, default=300)
    parser.add_argument("--image-quality", type=int, default=82, help="JPEG quality for embedded background; 100 embeds RGB image directly")
    parser.add_argument("--font", type=Path, default=None)
    parser.add_argument("--debug", action="store_true", help="Draw red outlines around text regions")
    args = parser.parse_args()

    order = load_pdf_order(args.pdf_order)
    translations = load_translation_records(args.translations)
    layout = load_layout(args.layout_json)
    font_name = register_font(args.font)
    pages = parse_pages(args.pages, len(order))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(args.output))
    stats: list[PageRenderStats] = []
    for page in pages:
        image_name = order[page - 1]
        image_path = args.images_dir / image_name
        if not image_path.exists():
            raise FileNotFoundError(image_path)
        translation = (translations.get(page) or {}).get("translation", "")
        if not translation:
            translation = "[No translation text available.]"
        stats.append(
            render_page(
                c=c,
                page=page,
                image_name=image_name,
                image_path=image_path,
                boxes=layout.get(page, []),
                translation=translation,
                font_name=font_name,
                dpi=args.dpi,
                image_quality=args.image_quality,
                debug=args.debug,
            )
        )
    c.save()

    if args.summary_json:
        args.summary_json.parent.mkdir(parents=True, exist_ok=True)
        write_summary(args.summary_json, stats, args)
    print(f"wrote {args.output} pages={len(stats)}")
    fallback = [s.page for s in stats if s.used_fallback_box]
    overflow = [s.page for s in stats if s.remaining_tokens > 0]
    if fallback:
        print("fallback pages:", ",".join(f"{p:03d}" for p in fallback))
    if overflow:
        print("overflow pages:", ",".join(f"{p:03d}" for p in overflow))


if __name__ == "__main__":
    main()
