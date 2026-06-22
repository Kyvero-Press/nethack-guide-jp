#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import tempfile
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

try:
    from scripts.translated_pdf_common import (
        BlockKey,
        choose_fitting_font_size,
        decision_for_block,
        draw_wrapped_text,
        font_size_bounds,
        group_blocks_by_page,
        load_block_sources,
        load_render_overrides,
        load_translation_records,
        parse_page_selection,
        px_bbox_to_pt_box,
        read_pdforder,
        register_font,
        write_jsonl,
    )
except ModuleNotFoundError:  # direct script execution
    from translated_pdf_common import (
        BlockKey,
        choose_fitting_font_size,
        decision_for_block,
        draw_wrapped_text,
        font_size_bounds,
        group_blocks_by_page,
        load_block_sources,
        load_render_overrides,
        load_translation_records,
        parse_page_selection,
        px_bbox_to_pt_box,
        read_pdforder,
        register_font,
        write_jsonl,
    )

DRAW_ACTIONS = {"auto", "manual_text", "caption_only", "skip_mask"}
NO_DRAW_ACTIONS = {"preserve_original", "omit"}


def make_background_reader(image_path: Path, quality: int) -> tuple[ImageReader, Path | None, int, int]:
    image = Image.open(image_path).convert("RGB")
    width, height = image.size
    if quality >= 100:
        return ImageReader(image), None, width, height
    tmp = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
    image.save(tmp.name, format="JPEG", quality=quality, optimize=True)
    tmp.close()
    return ImageReader(tmp.name), Path(tmp.name), width, height


def debug_color(status: str) -> tuple[int, int, int]:
    if status in {"fitted", "shrunk"}:
        return (0, 180, 0)
    if status in {"preserve_original", "caption_only", "manual_text"}:
        return (0, 100, 220)
    if status in {"overflow", "missing_translation"}:
        return (230, 0, 0)
    if status == "omitted":
        return (120, 120, 120)
    return (220, 140, 0)


def draw_debug_overlay(base_image: Path, out_path: Path, rows: list[dict[str, Any]]) -> None:
    image = Image.open(base_image).convert("RGB")
    draw = ImageDraw.Draw(image)
    for row in rows:
        bbox = row.get("bbox")
        if not bbox:
            continue
        x0, y0, x1, y1 = [int(round(float(v))) for v in bbox]
        color = debug_color(str(row.get("status") or ""))
        draw.rectangle((x0, y0, x1, y1), outline=color, width=3)
        draw.text((x0 + 2, y0 + 2), f"{row.get('block_id')} {row.get('status')}", fill=color)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(out_path)


def render_caption_box(c: canvas.Canvas, text: str, page_w: float, page_h: float, font_name: str) -> None:
    # Conservative caption placement for preserved art: a small unobtrusive footer.
    if not text.strip():
        return
    x = page_w * 0.08
    y = page_h * 0.035
    w = page_w * 0.84
    h = page_h * 0.055
    c.setFillColor(colors.Color(1, 1, 1, alpha=0.82))
    c.rect(x, y, w, h, stroke=0, fill=1)
    c.setStrokeColor(colors.Color(0.75, 0.75, 0.75))
    c.rect(x, y, w, h, stroke=1, fill=0)
    c.setFillColor(colors.black)
    draw_wrapped_text(c, text, x + 3, y + 3, w - 6, h - 6, font_name, 6.0)


def render_pdf(args: argparse.Namespace) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    order = read_pdforder(args.pdforder)
    blocks = load_block_sources(args.source_jsonl)
    by_page = group_blocks_by_page(blocks)
    overrides = load_render_overrides(args.overrides, blocks)
    translations = load_translation_records(args.translations)
    pages = parse_page_selection(args.pages, len(order))
    font_name = register_font(args.font)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(args.output))
    all_fit_rows: list[dict[str, Any]] = []
    debug_rows_by_page: dict[int, list[dict[str, Any]]] = defaultdict(list)

    for page in pages:
        image_name = order[page - 1]
        bg_path = args.background_dir / image_name
        if not bg_path.exists():
            raise FileNotFoundError(bg_path)
        reader, tmp_path, width_px, height_px = make_background_reader(bg_path, args.image_quality)
        scale = 72.0 / args.dpi
        page_w, page_h = width_px * scale, height_px * scale
        c.setPageSize((page_w, page_h))
        c.drawImage(reader, 0, 0, page_w, page_h, preserveAspectRatio=False, mask="auto")
        c.setFillColor(colors.black)

        page_caption_texts: list[str] = []
        for block in by_page.get(page, []):
            decision = decision_for_block(block, overrides)
            action = decision.action
            key = BlockKey(block.block_id, block.source_sha256)
            translation = translations.get(key)
            text = ""
            if action == "manual_text" and decision.override.manual_text is not None:
                text = decision.override.manual_text
            elif action == "caption_only" and decision.override.manual_text is not None:
                text = decision.override.manual_text
            elif translation and translation.status == "ok":
                text = translation.translation.strip()

            x, y, w, h = px_bbox_to_pt_box(decision.bbox, page_h, scale, pad_pt=0.8)
            status = "unhandled"
            font_size = None
            remaining = 0
            if action in NO_DRAW_ACTIONS:
                status = "preserve_original" if action == "preserve_original" else "omitted"
            elif action == "caption_only":
                page_caption_texts.append(text)
                status = "caption_only"
            elif not text:
                status = "missing_translation"
                remaining = 1
            else:
                min_size, max_size = font_size_bounds(block.label, decision.override)
                font_size, remaining = choose_fitting_font_size(text, w, h, font_name, min_size, max_size)
                if remaining:
                    status = "overflow"
                elif font_size < max_size - 0.05:
                    status = "shrunk"
                else:
                    status = "fitted"
                c.setFillColor(colors.black)
                remaining_after_draw = draw_wrapped_text(c, text, x, y, w, h, font_name, font_size)
                remaining = max(remaining, remaining_after_draw)
                if remaining:
                    status = "overflow"

            fit_row = {
                "page": page,
                "page_label": f"{page:03d}",
                "source_image": image_name,
                "block_id": block.block_id,
                "source_sha256": block.source_sha256,
                "label": block.label,
                "reading_order": block.reading_order,
                "action": action,
                "status": status,
                "bbox": list(decision.bbox),
                "bbox_pt": [round(v, 3) for v in (x, y, w, h)],
                "source_chars": len(block.source_text),
                "translation_chars": len(text),
                "font_size": round(font_size, 3) if font_size is not None else None,
                "remaining_tokens": remaining,
                "override_note": decision.override.note,
            }
            all_fit_rows.append(fit_row)
            debug_rows_by_page[page].append(fit_row)

        if page_caption_texts:
            render_caption_box(c, " / ".join(t for t in page_caption_texts if t), page_w, page_h, font_name)

        c.setFillColor(colors.Color(0.28, 0.28, 0.28))
        c.setFont(font_name, 4.0)
        c.drawRightString(page_w - 4, 4, f"block-level machine translation prototype · page {page:03d}")
        c.showPage()
        if tmp_path:
            tmp_path.unlink(missing_ok=True)

    c.save()

    if args.debug_dir:
        for page, rows in debug_rows_by_page.items():
            image_name = order[page - 1]
            draw_debug_overlay(args.background_dir / image_name, args.debug_dir / f"{page:03d}.png", rows)

    status_counts = Counter(str(row["status"]) for row in all_fit_rows)
    action_counts = Counter(str(row["action"]) for row in all_fit_rows)
    summary = {
        "output": str(args.output),
        "pages": len(pages),
        "blocks": len(all_fit_rows),
        "status_counts": dict(status_counts),
        "action_counts": dict(action_counts),
        "missing_translation_blocks": [row["block_id"] for row in all_fit_rows if row["status"] == "missing_translation"],
        "overflow_blocks": [row["block_id"] for row in all_fit_rows if row["status"] == "overflow"],
        "preserved_blocks": [row["block_id"] for row in all_fit_rows if row["status"] == "preserve_original"],
    }
    return all_fit_rows, summary


def write_fit_markdown(path: Path, summary: dict[str, Any], rows: list[dict[str, Any]]) -> None:
    lines = ["# Block-level hybrid PDF fit report\n", "\n## Summary\n\n"]
    for key in ["output", "pages", "blocks"]:
        lines.append(f"- `{key}`: {summary[key]}\n")
    lines.append(f"- status counts: `{summary['status_counts']}`\n")
    lines.append(f"- action counts: `{summary['action_counts']}`\n")
    lines.append("\n## Blocks needing review\n\n")
    review = [row for row in rows if row["status"] in {"overflow", "missing_translation"}]
    if not review:
        lines.append("No hard overflow or missing-translation rows.\n")
    else:
        for row in review[:200]:
            lines.append(
                f"- page `{row['page_label']}` block `{row['block_id']}` status `{row['status']}` "
                f"remaining `{row['remaining_tokens']}` chars `{row['translation_chars']}`\n"
            )
        if len(review) > 200:
            lines.append(f"- ... {len(review) - 200} more\n")
    lines.append("\n## Manual/preserved blocks\n\n")
    for row in rows:
        if row["action"] != "auto" or row["status"] == "preserve_original":
            lines.append(f"- page `{row['page_label']}` block `{row['block_id']}` action `{row['action']}` status `{row['status']}` — {row.get('override_note','')}\n")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a block-level translated hybrid facsimile PDF.")
    parser.add_argument("--background-dir", type=Path, required=True)
    parser.add_argument("--source-jsonl", type=Path, default=Path("work/translation/source/blocks-surya.jsonl"))
    parser.add_argument("--translations", type=Path, required=True)
    parser.add_argument("--overrides", type=Path, default=Path("config/translation-render-overrides.yaml"))
    parser.add_argument("--pdforder", type=Path, default=Path("dist/pdforder.txt"))
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--fit-report", type=Path, required=True)
    parser.add_argument("--fit-report-md", type=Path)
    parser.add_argument("--debug-dir", type=Path)
    parser.add_argument("--pages")
    parser.add_argument("--dpi", type=int, default=300)
    parser.add_argument("--image-quality", type=int, default=76)
    parser.add_argument("--font", type=Path)
    args = parser.parse_args()

    fit_rows, summary = render_pdf(args)
    write_jsonl(args.fit_report, fit_rows)
    if args.fit_report_md:
        write_fit_markdown(args.fit_report_md, summary, fit_rows)
    print(f"wrote {args.output} pages={summary['pages']} blocks={summary['blocks']}")
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
