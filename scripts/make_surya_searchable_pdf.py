#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from html.parser import HTMLParser
from io import BytesIO
from pathlib import Path
from typing import Any

from PIL import Image
from reportlab.lib.colors import Color
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFError, TTFont
from reportlab.pdfgen import canvas


class HtmlTextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"br", "p", "div", "li", "tr", "h1", "h2", "h3", "h4"}:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"p", "div", "li", "tr", "h1", "h2", "h3", "h4"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if data.strip():
            self.parts.append(data)

    def text(self) -> str:
        text = "".join(self.parts)
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()


def html_to_text(html: str | None) -> str:
    parser = HtmlTextExtractor()
    parser.feed(html or "")
    return parser.text()


def ordered_images(pdforder: Path, image_dir: Path) -> list[Path]:
    names = [line.strip() for line in pdforder.read_text(encoding="utf-8").splitlines() if line.strip()]
    paths = [image_dir / name for name in names]
    missing = [str(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("Missing images:\n" + "\n".join(missing[:20]))
    return paths


def key_for_page(index: int, image_name: str, results: dict[str, Any]) -> str:
    prefix = f"{index:03d}__"
    matches = [key for key in results if key.startswith(prefix)]
    if matches:
        return matches[0]
    stem = Path(image_name).stem
    matches = [key for key in results if key.endswith(stem) or stem in key]
    if len(matches) == 1:
        return matches[0]
    raise KeyError(f"Could not find Surya results for page {index:03d} / {image_name}")


def fit_font_size(lines: list[str], box_w: float, box_h: float, font_name: str, max_size: float = 18.0) -> float:
    if not lines:
        return 1.0
    line_count = max(1, len(lines))
    by_height = max(1.0, (box_h / line_count) * 0.72)
    by_width = max_size
    for line in lines:
        width_at_1 = pdfmetrics.stringWidth(line, font_name, 1.0)
        if width_at_1 > 0:
            by_width = min(by_width, box_w / width_at_1)
    return max(1.0, min(max_size, by_height, by_width * 0.95))


def draw_text_block(
    c: canvas.Canvas,
    *,
    text: str,
    bbox: list[float],
    page_h: float,
    scale: float,
    font_name: str,
) -> None:
    x1, y1, x2, y2 = bbox
    x = x1 * scale
    top = page_h - y1 * scale
    box_w = max(1.0, (x2 - x1) * scale)
    box_h = max(1.0, (y2 - y1) * scale)
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return
    font_size = fit_font_size(lines, box_w, box_h, font_name)
    line_height = max(font_size * 1.15, box_h / max(1, len(lines)))
    c.setFont(font_name, font_size)
    y = top - line_height + (line_height - font_size) * 0.5
    for line in lines:
        c.drawString(x, y, line)
        y -= line_height


def draw_page(
    c: canvas.Canvas,
    *,
    image_path: Path,
    page_result: list[dict[str, Any]],
    dpi: int,
    image_encoding: str,
    jpeg_quality: int,
    font_name: str,
) -> None:
    image = Image.open(image_path).convert("RGB")
    w_px, h_px = image.size
    scale = 72.0 / dpi
    page_w = w_px * scale
    page_h = h_px * scale
    c.setPageSize((page_w, page_h))

    buf = BytesIO()
    if image_encoding == "png":
        image.save(buf, format="PNG")
    else:
        image.save(buf, format="JPEG", quality=jpeg_quality, optimize=True)
    buf.seek(0)
    c.drawImage(ImageReader(buf), 0, 0, width=page_w, height=page_h)

    blocks: list[dict[str, Any]] = []
    for page in page_result:
        for block in page.get("blocks", []):
            html = block.get("html")
            bbox = block.get("bbox")
            if not html or not bbox or block.get("skipped") or block.get("error"):
                continue
            text = html_to_text(html)
            if text:
                blocks.append({"order": block.get("reading_order", 0), "bbox": bbox, "text": text})
    blocks.sort(key=lambda block: block["order"])

    # Invisible text layer. It is not meant for visual rendering; it gives PDF
    # search/copy tools a text layer while the scanned page remains authoritative.
    c.setFillColor(Color(0, 0, 0, alpha=0))
    for block in blocks:
        draw_text_block(c, text=block["text"], bbox=block["bbox"], page_h=page_h, scale=scale, font_name=font_name)
    c.showPage()


def register_font(font_name: str, requested_font: Path | None) -> None:
    candidates: list[Path] = []
    if requested_font is not None:
        candidates.append(requested_font)
    candidates.extend(
        [
            Path("/home/tay/.local/share/Steam/clientui/fonts/GoNotoKurrent-Regular.ttf"),
            Path("/usr/share/fonts/TTF/GoNotoKurrent-Regular.ttf"),
            Path("/usr/share/fonts/truetype/fonts-japanese-gothic.ttf"),
            Path("/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf"),
            Path("/usr/share/fonts/noto-cjk/NotoSansCJK-Regular.ttc"),
        ]
    )
    errors: list[str] = []
    seen: set[Path] = set()
    for candidate in candidates:
        if candidate in seen:
            continue
        seen.add(candidate)
        if not candidate.exists():
            continue
        try:
            pdfmetrics.registerFont(TTFont(font_name, str(candidate)))
            print(f"using PDF text font: {candidate}")
            return
        except (TTFError, Exception) as exc:  # report all unusable local CJK fonts.
            errors.append(f"{candidate}: {exc}")
    detail = "\n".join(errors[-5:]) if errors else "no candidate font files found"
    raise RuntimeError("Could not register a ReportLab-compatible CJK TrueType font:\n" + detail)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a searchable scan PDF from Surya OCR JSON block boxes.")
    parser.add_argument("--pdforder", type=Path, default=Path("dist/pdforder.txt"))
    parser.add_argument("--image-dir", type=Path, default=Path("dist/crops/refined"))
    parser.add_argument("--surya-json", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--dpi", type=int, default=300)
    parser.add_argument("--image-encoding", choices=["jpeg", "png"], default="jpeg")
    parser.add_argument("--jpeg-quality", type=int, default=85)
    parser.add_argument("--font", type=Path, default=None, help="ReportLab-compatible TrueType/OpenType CJK font. If omitted, common local fonts are tried.")
    parser.add_argument("--font-name", default="NotoSansCJKJP")
    parser.add_argument("--limit", type=int, default=0, help="Only render the first N pages, for testing.")
    args = parser.parse_args()

    register_font(args.font_name, args.font)

    results = json.loads(args.surya_json.read_text(encoding="utf-8"))
    images = ordered_images(args.pdforder, args.image_dir)
    if args.limit:
        images = images[: args.limit]
    args.output.parent.mkdir(parents=True, exist_ok=True)

    c = canvas.Canvas(str(args.output), pageCompression=0 if args.image_encoding == "png" else 1)
    for index, image_path in enumerate(images, 1):
        print(f"[{index:03d}/{len(images):03d}] {image_path.name}", flush=True)
        key = key_for_page(index, image_path.name, results)
        draw_page(
            c,
            image_path=image_path,
            page_result=results[key],
            dpi=args.dpi,
            image_encoding=args.image_encoding,
            jpeg_quality=args.jpeg_quality,
            font_name=args.font_name,
        )
    c.save()
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
