from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image

from scripts.make_block_translated_pdf_hybrid import render_pdf


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")


def test_render_pdf_writes_fit_rows(tmp_path: Path) -> None:
    bg = tmp_path / "bg"
    bg.mkdir()
    Image.new("RGB", (200, 300), (255, 255, 250)).save(bg / "page.png")
    pdforder = tmp_path / "pdforder.txt"
    pdforder.write_text("page.png\n", encoding="utf-8")
    source = tmp_path / "source.jsonl"
    row = {
        "record_type": "block",
        "page": 1,
        "page_label": "001",
        "source_image": "page.png",
        "source_key": "001__page",
        "block_id": "001-000",
        "reading_order": 0,
        "label": "Text",
        "bbox": [20, 20, 180, 80],
        "source_text": "こんにちは",
        "source_sha256": "abc",
    }
    write_jsonl(source, [row])
    translations = tmp_path / "translations.jsonl"
    write_jsonl(translations, [{**row, "record_id": "block:001:001-000:abc", "status": "ok", "translation": "Hello world."}])
    args = argparse.Namespace(
        background_dir=bg,
        source_jsonl=source,
        translations=translations,
        overrides=tmp_path / "missing.yaml",
        pdforder=pdforder,
        output=tmp_path / "out.pdf",
        fit_report=tmp_path / "fit.jsonl",
        fit_report_md=None,
        debug_dir=None,
        pages="1",
        dpi=100,
        image_quality=100,
        font=None,
    )
    rows, summary = render_pdf(args)
    assert args.output.exists()
    assert summary["pages"] == 1
    assert rows[0]["block_id"] == "001-000"
    assert rows[0]["status"] in {"fitted", "shrunk"}
