#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image, ImageDraw

try:
    from scripts.translated_pdf_common import (
        decision_for_block,
        group_blocks_by_page,
        load_block_sources,
        load_render_overrides,
        parse_page_selection,
        read_pdforder,
    )
except ModuleNotFoundError:  # direct script execution
    from translated_pdf_common import (
        decision_for_block,
        group_blocks_by_page,
        load_block_sources,
        load_render_overrides,
        parse_page_selection,
        read_pdforder,
    )

MASK_ACTIONS = {"auto", "manual_text", "omit"}
PRESERVE_ACTIONS = {"preserve_original", "skip_mask", "caption_only"}


def clamp_bbox(bbox: tuple[float, float, float, float], width: int, height: int, padding: int = 0) -> tuple[int, int, int, int]:
    x0, y0, x1, y1 = bbox
    return (
        max(0, int(round(x0)) - padding),
        max(0, int(round(y0)) - padding),
        min(width, int(round(x1)) + padding),
        min(height, int(round(y1)) + padding),
    )


def sample_fill(image: Image.Image, bbox: tuple[int, int, int, int], margin: int = 16) -> tuple[int, int, int]:
    width, height = image.size
    x0, y0, x1, y1 = bbox
    sx0, sy0 = max(0, x0 - margin), max(0, y0 - margin)
    sx1, sy1 = min(width, x1 + margin), min(height, y1 + margin)
    arr = np.asarray(image.crop((sx0, sy0, sx1, sy1)).convert("RGB"))
    if arr.size == 0:
        return (255, 255, 255)
    # Use light pixels from the local neighborhood; this avoids sampling black text.
    flat = arr.reshape(-1, 3)
    brightness = flat.mean(axis=1)
    light = flat[brightness > np.percentile(brightness, 55)]
    if len(light) < 10:
        light = flat
    rgb = np.median(light, axis=0)
    return tuple(int(max(0, min(255, v))) for v in rgb)


def clean_page(
    image_path: Path,
    out_path: Path,
    debug_path: Path | None,
    page_blocks: list[Any],
    overrides: dict[str, Any],
) -> dict[str, Any]:
    image = Image.open(image_path).convert("RGB")
    width, height = image.size
    cleaned = image.copy()
    debug = image.copy() if debug_path else None
    cleaned_draw = ImageDraw.Draw(cleaned)
    debug_draw = ImageDraw.Draw(debug) if debug else None
    masked: list[str] = []
    preserved: list[str] = []
    warnings: list[str] = []

    for block in page_blocks:
        decision = decision_for_block(block, overrides)
        action = decision.action
        bbox = clamp_bbox(decision.bbox, width, height, decision.mask_padding_px)
        if bbox[2] <= bbox[0] or bbox[3] <= bbox[1]:
            warnings.append(f"empty bbox {block.block_id}")
            continue
        if action in MASK_ACTIONS:
            fill = sample_fill(image, bbox)
            cleaned_draw.rectangle(bbox, fill=fill)
            masked.append(block.block_id)
            if debug_draw:
                debug_draw.rectangle(bbox, outline=(220, 0, 0), width=4)
        elif action in PRESERVE_ACTIONS:
            preserved.append(block.block_id)
            if debug_draw:
                debug_draw.rectangle(bbox, outline=(0, 160, 0), width=4)
        else:
            warnings.append(f"unknown action {action} for {block.block_id}")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    cleaned.save(out_path)
    if debug and debug_path:
        debug_path.parent.mkdir(parents=True, exist_ok=True)
        debug.save(debug_path)
    return {
        "source_image": str(image_path),
        "output_image": str(out_path),
        "debug_image": str(debug_path) if debug_path else None,
        "width": width,
        "height": height,
        "blocks": len(page_blocks),
        "masked_blocks": masked,
        "preserved_blocks": preserved,
        "warnings": warnings,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate cleaned translated-PDF page backgrounds from refined crops and Surya text bboxes.")
    parser.add_argument("--source-jsonl", type=Path, default=Path("work/translation/source/blocks-surya.jsonl"))
    parser.add_argument("--overrides", type=Path, default=Path("config/translation-render-overrides.yaml"))
    parser.add_argument("--images-dir", type=Path, default=Path("dist/crops/refined"))
    parser.add_argument("--pdforder", type=Path, default=Path("dist/pdforder.txt"))
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--debug-dir", type=Path)
    parser.add_argument("--summary-json", type=Path, required=True)
    parser.add_argument("--pages")
    parser.add_argument("--force", action="store_true", help="Remove the output directory before writing")
    args = parser.parse_args()

    order = read_pdforder(args.pdforder)
    blocks = load_block_sources(args.source_jsonl)
    overrides = load_render_overrides(args.overrides, blocks)
    by_page = group_blocks_by_page(blocks)
    pages = parse_page_selection(args.pages, len(order))

    if args.force and args.out_dir.exists():
        shutil.rmtree(args.out_dir)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    if args.debug_dir:
        args.debug_dir.mkdir(parents=True, exist_ok=True)

    page_summaries: list[dict[str, Any]] = []
    for page in pages:
        image_name = order[page - 1]
        image_path = args.images_dir / image_name
        if not image_path.exists():
            raise FileNotFoundError(image_path)
        out_path = args.out_dir / image_name
        debug_path = args.debug_dir / f"{page:03d}.png" if args.debug_dir else None
        page_summaries.append(clean_page(image_path, out_path, debug_path, by_page.get(page, []), overrides))

    summary = {
        "source_jsonl": str(args.source_jsonl),
        "overrides": str(args.overrides),
        "images_dir": str(args.images_dir),
        "out_dir": str(args.out_dir),
        "pages_requested": len(pages),
        "pages_written": len(page_summaries),
        "total_masked_blocks": sum(len(p["masked_blocks"]) for p in page_summaries),
        "total_preserved_blocks": sum(len(p["preserved_blocks"]) for p in page_summaries),
        "pages": page_summaries,
    }
    args.summary_json.parent.mkdir(parents=True, exist_ok=True)
    args.summary_json.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {len(page_summaries)} cleaned backgrounds to {args.out_dir}")
    print(f"masked_blocks={summary['total_masked_blocks']} preserved_blocks={summary['total_preserved_blocks']}")


if __name__ == "__main__":
    main()
