#!/usr/bin/env python3
"""Build a side-by-side original scan + English translation review PDF.

Unlike the facsimile prototype, this PDF prioritizes human translation review:
left side shows the refined original page image; right side shows the local
English machine translation. Long translations spill onto continuation pages
instead of being truncated.
"""

from __future__ import annotations

import argparse
import json
import re
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from PIL import Image
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


@dataclass
class ReviewStats:
    source_page: int
    pdf_pages: int
    source_image: str
    translation_chars: int
    overflow: bool


def load_pdf_order(path: Path) -> list[str]:
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def load_translations(path: Path) -> dict[int, dict]:
    rows: dict[int, dict] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            row = json.loads(line)
            rows[int(row["page"])] = row
    return rows


def parse_pages(value: str | None, total: int) -> list[int]:
    if not value:
        return list(range(1, total + 1))
    out: set[int] = set()
    for part in value.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = [int(x) for x in part.split("-", 1)]
            out.update(range(a, b + 1))
        else:
            out.add(int(part))
    return sorted(p for p in out if 1 <= p <= total)


def register_font(font: Path | None) -> str:
    candidates = [
        font,
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
        Path("/usr/share/fonts/truetype/liberation2/LiberationSerif-Regular.ttf"),
    ]
    for candidate in candidates:
        if candidate and candidate.exists():
            pdfmetrics.registerFont(TTFont("ReviewFont", str(candidate)))
            return "ReviewFont"
    return "Times-Roman"


def make_review_image(image_path: Path, max_px: int, quality: int) -> tempfile.NamedTemporaryFile:
    image = Image.open(image_path).convert("RGB")
    image.thumbnail((max_px, max_px), Image.Resampling.LANCZOS)
    tmp = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
    image.save(tmp.name, format="JPEG", quality=quality, optimize=True)
    tmp.close()
    return tmp


def words_from_text(text: str) -> list[str]:
    tokens: list[str] = []
    for paragraph in re.split(r"\n\s*\n", text.strip()):
        paragraph = paragraph.strip()
        if not paragraph:
            continue
        tokens.extend(paragraph.split())
        tokens.append("\n")
    return tokens


def wrap_line(font_name: str, font_size: float, words: Sequence[str], width: float) -> tuple[str, int]:
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


def draw_text_box(
    c: canvas.Canvas,
    tokens: list[str],
    x: float,
    y: float,
    width: float,
    height: float,
    font_name: str,
    font_size: float,
) -> list[str]:
    remaining = list(tokens)
    line_height = font_size * 1.25
    current_y = y + height - line_height
    c.setFont(font_name, font_size)
    c.setFillColor(colors.black)
    while current_y >= y and remaining:
        while remaining and remaining[0] == "\n":
            remaining.pop(0)
            current_y -= line_height * 0.55
            if current_y < y:
                return remaining
        if not remaining:
            break
        segment: list[str] = []
        for token in remaining:
            if token == "\n":
                break
            segment.append(token)
        if not segment:
            continue
        line, used = wrap_line(font_name, font_size, segment, width)
        if not line or used <= 0:
            break
        c.drawString(x, current_y, line)
        del remaining[:used]
        current_y -= line_height
    return remaining


def draw_review_page(
    c: canvas.Canvas,
    page_size: tuple[float, float],
    font_name: str,
    source_page: int,
    image_name: str,
    image_tmp: tempfile.NamedTemporaryFile | None,
    tokens: list[str],
    title_suffix: str,
    first: bool,
) -> list[str]:
    page_w, page_h = page_size
    margin = 24.0
    gap = 18.0
    left_w = 365.0
    right_x = margin + left_w + gap
    right_w = page_w - right_x - margin
    body_y = margin + 22
    body_h = page_h - body_y - 48

    c.setPageSize(page_size)
    c.setFillColor(colors.white)
    c.rect(0, 0, page_w, page_h, stroke=0, fill=1)
    c.setFont(font_name, 11)
    c.setFillColor(colors.black)
    c.drawString(margin, page_h - 28, f"Original page {source_page:03d}{title_suffix}")
    c.drawString(right_x, page_h - 28, "Local English translation (Qwen2.5-7B-Instruct)")
    c.setStrokeColor(colors.lightgrey)
    c.line(margin, page_h - 36, page_w - margin, page_h - 36)

    if first and image_tmp is not None:
        reader = ImageReader(image_tmp.name)
        iw, ih = reader.getSize()
        max_h = body_h
        scale = min(left_w / iw, max_h / ih)
        draw_w = iw * scale
        draw_h = ih * scale
        x = margin + (left_w - draw_w) / 2
        y = body_y + (max_h - draw_h) / 2
        c.drawImage(reader, x, y, draw_w, draw_h, preserveAspectRatio=True, mask="auto")
    else:
        c.setFillColor(colors.whitesmoke)
        c.rect(margin, body_y, left_w, body_h, stroke=0, fill=1)
        c.setFillColor(colors.grey)
        c.setFont(font_name, 9)
        c.drawCentredString(margin + left_w / 2, body_y + body_h / 2, f"Page {source_page:03d} continued")

    c.setStrokeColor(colors.lightgrey)
    c.rect(right_x - 8, body_y - 8, right_w + 16, body_h + 16, stroke=1, fill=0)
    c.setFont(font_name, 7.8)
    remaining = draw_text_box(c, tokens, right_x, body_y, right_w, body_h, font_name, 7.8)

    c.setFont(font_name, 6)
    c.setFillColor(colors.grey)
    c.drawRightString(page_w - margin, 12, f"review artifact · source page {source_page:03d} · {image_name}")
    c.showPage()
    return remaining


def write_summary(path: Path, stats: Sequence[ReviewStats], output: Path) -> None:
    payload = {
        "renderer": "make_translation_review_pdf.py",
        "strategy": "side-by-side-original-scan-plus-page-level-translation",
        "output_pdf": str(output),
        "source_pages": len(stats),
        "pdf_pages": sum(s.pdf_pages for s in stats),
        "continuation_source_pages": [s.source_page for s in stats if s.overflow],
        "pages": [s.__dict__ for s in stats],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--images-dir", type=Path, default=Path("dist/crops/refined"))
    parser.add_argument("--pdf-order", type=Path, default=Path("dist/pdforder.txt"))
    parser.add_argument("--translations", type=Path, default=Path("dist/text/translation-local/qwen2_5_7b_instruct/translation-records.jsonl"))
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--summary-json", type=Path)
    parser.add_argument("--pages")
    parser.add_argument("--font", type=Path)
    parser.add_argument("--image-max-px", type=int, default=1200)
    parser.add_argument("--image-quality", type=int, default=78)
    args = parser.parse_args()

    order = load_pdf_order(args.pdf_order)
    translations = load_translations(args.translations)
    pages = parse_pages(args.pages, len(order))
    font_name = register_font(args.font)
    args.output.parent.mkdir(parents=True, exist_ok=True)

    c = canvas.Canvas(str(args.output))
    page_size = landscape(A4)
    stats: list[ReviewStats] = []
    for page in pages:
        image_name = order[page - 1]
        image_path = args.images_dir / image_name
        translation = (translations.get(page) or {}).get("translation", "[No translation available]")
        image_tmp = make_review_image(image_path, args.image_max_px, args.image_quality)
        tokens = words_from_text(translation)
        pdf_pages = 0
        remaining = tokens
        first = True
        try:
            while remaining:
                suffix = "" if first else " (continued)"
                before = len(remaining)
                remaining = draw_review_page(c, page_size, font_name, page, image_name, image_tmp, remaining, suffix, first)
                pdf_pages += 1
                first = False
                if len(remaining) >= before:
                    # Safety: force progress if an unbreakable token is pathological.
                    remaining = remaining[1:]
            stats.append(ReviewStats(page, pdf_pages, image_name, len(translation), pdf_pages > 1))
        finally:
            Path(image_tmp.name).unlink(missing_ok=True)
    c.save()
    if args.summary_json:
        write_summary(args.summary_json, stats, args.output)
    print(f"wrote {args.output} source_pages={len(stats)} pdf_pages={sum(s.pdf_pages for s in stats)}")
    continuations = [s.source_page for s in stats if s.overflow]
    if continuations:
        print("continuation source pages:", ",".join(f"{p:03d}" for p in continuations))


if __name__ == "__main__":
    main()
