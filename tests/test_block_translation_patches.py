from __future__ import annotations

from scripts.apply_translation_patches import merge_records
from scripts.translated_pdf_common import BlockSource


def block() -> BlockSource:
    return BlockSource(
        page=1,
        page_label="001",
        source_image="p.png",
        source_key="001__p",
        block_id="001-000",
        reading_order=0,
        label="Text",
        bbox=(1, 2, 30, 40),
        source_text="こんにちは",
        source_sha256="abc",
    )


def test_merge_records_applies_guarded_patch(tmp_path) -> None:
    raw = tmp_path / "raw.jsonl"
    raw.write_text(
        '{"record_type":"block","page":1,"page_label":"001","block_id":"001-000","source_sha256":"abc","status":"ok","translation":"bad 世界"}\n',
        encoding="utf-8",
    )
    rows, report = merge_records(
        [block()],
        [raw],
        [{"block_id": "001-000", "source_sha256": "abc", "translation": "Hello.", "reason": "test"}],
    )
    assert report["manual_patches"] == 1
    assert rows[0]["translation"] == "Hello."
    assert rows[0]["patched"] is True
