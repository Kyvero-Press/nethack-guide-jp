from __future__ import annotations

import json
from pathlib import Path

from scripts.translated_pdf_common import load_block_sources, source_manifest

ROOT = Path(__file__).resolve().parents[1]


def test_current_block_source_contract_is_stable_enough() -> None:
    blocks = load_block_sources(ROOT / "work/translation/source/blocks-surya.jsonl")
    assert len(blocks) > 3000
    assert len({block.key for block in blocks}) == len(blocks)
    assert all(block.width_px > 0 and block.height_px > 0 for block in blocks)
    assert blocks[0].block_id == "001-000"


def test_source_manifest_reports_pdforder_and_empty_pages() -> None:
    manifest = source_manifest(
        source_jsonl=ROOT / "work/translation/source/blocks-surya.jsonl",
        pdforder=ROOT / "dist/pdforder.txt",
        images_dir=ROOT / "dist/crops/refined",
    )
    assert manifest["pdforder_pages"] == 274
    assert manifest["block_count"] > 3000
    assert "272" in manifest["pages_without_blocks"]
    assert manifest["missing_images"] == []
