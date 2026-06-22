#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import html.parser
import json
import re
from pathlib import Path
from typing import Any

try:
    from scripts.translated_pdf_common import source_manifest
except ModuleNotFoundError:  # direct script execution
    from translated_pdf_common import source_manifest


class HtmlTextExtractor(html.parser.HTMLParser):
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


def html_to_text(value: str | None) -> str:
    parser = HtmlTextExtractor()
    parser.feed(value or "")
    return parser.text()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_pdforder(path: Path) -> list[str]:
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def build_page_rows(args: argparse.Namespace) -> list[dict[str, Any]]:
    images = read_pdforder(args.pdforder)
    rows: list[dict[str, Any]] = []
    for index, image in enumerate(images, 1):
        text_path = args.page_text_dir / f"{index:03d}.txt"
        if not text_path.exists():
            raise FileNotFoundError(text_path)
        text = text_path.read_text(encoding="utf-8").strip()
        rows.append(
            {
                "record_type": "page",
                "ocr_engine": args.ocr_engine,
                "page": index,
                "page_label": f"{index:03d}",
                "source_image": image,
                "source_text": text,
                "source_sha256": sha256_text(text),
            }
        )
    return rows


def result_key_for(index: int, image: str, results: dict[str, Any]) -> str:
    prefix = f"{index:03d}__"
    matches = [key for key in results if key.startswith(prefix)]
    if matches:
        return matches[0]
    stem = Path(image).stem
    matches = [key for key in results if key.endswith(stem) or stem in key]
    if len(matches) == 1:
        return matches[0]
    raise KeyError(f"No Surya result for page {index:03d} / {image}")


def build_block_rows(args: argparse.Namespace) -> list[dict[str, Any]]:
    images = read_pdforder(args.pdforder)
    results = json.loads(args.surya_json.read_text(encoding="utf-8"))
    rows: list[dict[str, Any]] = []
    for page_index, image in enumerate(images, 1):
        key = result_key_for(page_index, image, results)
        block_counter = 0
        for page in results[key]:
            blocks = sorted(page.get("blocks", []), key=lambda b: b.get("reading_order", 0))
            for block in blocks:
                if block.get("skipped") or block.get("error"):
                    continue
                text = html_to_text(block.get("html"))
                if not text:
                    continue
                rows.append(
                    {
                        "record_type": "block",
                        "ocr_engine": args.ocr_engine,
                        "page": page_index,
                        "page_label": f"{page_index:03d}",
                        "source_image": image,
                        "source_key": key,
                        "block_id": f"{page_index:03d}-{block_counter:03d}",
                        "reading_order": block.get("reading_order", block_counter),
                        "label": block.get("label"),
                        "bbox": block.get("bbox"),
                        "polygon": block.get("polygon"),
                        "source_text": text,
                        "source_sha256": sha256_text(text),
                    }
                )
                block_counter += 1
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare page/block JSONL sources for local translation runs.")
    parser.add_argument("--pdforder", type=Path, default=Path("dist/pdforder.txt"))
    parser.add_argument("--page-text-dir", type=Path, default=Path("dist/text/surya/pages"))
    parser.add_argument("--surya-json", type=Path, default=Path("dist/metadata/ocr-bakeoff/surya-full/results.json"))
    parser.add_argument("--ocr-engine", default="surya-ocr-2")
    parser.add_argument("--images-dir", type=Path, default=Path("dist/crops/refined"))
    parser.add_argument("--pages-out", type=Path, default=Path("work/translation/source/pages-surya.jsonl"))
    parser.add_argument("--blocks-out", type=Path, default=Path("work/translation/source/blocks-surya.jsonl"))
    parser.add_argument("--manifest-out", type=Path, default=None, help="Optional JSON manifest for the generated block source contract")
    parser.add_argument("--pages", action="store_true", help="Build page-level records")
    parser.add_argument("--blocks", action="store_true", help="Build block-level records")
    args = parser.parse_args()

    if not args.pages and not args.blocks:
        args.pages = args.blocks = True

    if args.pages:
        page_rows = build_page_rows(args)
        write_jsonl(args.pages_out, page_rows)
        print(f"wrote {len(page_rows)} page records to {args.pages_out}")
    if args.blocks:
        block_rows = build_block_rows(args)
        write_jsonl(args.blocks_out, block_rows)
        print(f"wrote {len(block_rows)} block records to {args.blocks_out}")
        if args.manifest_out:
            args.manifest_out.parent.mkdir(parents=True, exist_ok=True)
            manifest = source_manifest(source_jsonl=args.blocks_out, pdforder=args.pdforder, images_dir=args.images_dir)
            args.manifest_out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print(f"wrote block source manifest to {args.manifest_out}")


if __name__ == "__main__":
    main()
