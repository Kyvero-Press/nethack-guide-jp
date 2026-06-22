from __future__ import annotations

import argparse
import json
from pathlib import Path

from scripts.validate_translation_outputs import validate


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")


def source_row() -> dict:
    return {
        "record_type": "block",
        "page": 1,
        "page_label": "001",
        "source_image": "p.png",
        "source_key": "001__p",
        "block_id": "001-000",
        "reading_order": 0,
        "label": "Text",
        "bbox": [1, 2, 30, 40],
        "source_text": "こんにちは",
        "source_sha256": "abc",
    }


def args(tmp_path: Path, input_path: Path, source_path: Path) -> argparse.Namespace:
    return argparse.Namespace(
        input=input_path,
        source_jsonl=source_path,
        record_type="block",
        expected_records=0,
        expected_pages=0,
        max_ja_ratio=0.05,
        min_length_ratio=0.18,
        max_length_ratio=5.0,
        write_report=None,
        write_report_md=None,
        write_retry_jsonl=None,
        allow_issues=False,
    )


def test_validate_detects_missing_and_builds_retry_rows(tmp_path: Path) -> None:
    source = tmp_path / "source.jsonl"
    output = tmp_path / "out.jsonl"
    write_jsonl(source, [source_row()])
    write_jsonl(output, [])
    summary, issues, retry = validate(args(tmp_path, output, source))
    assert summary["source_records"] == 1
    assert any(issue["kind"] == "missing_record" for issue in issues)
    assert retry == [source_row()]


def test_validate_flags_cjk_leakage(tmp_path: Path) -> None:
    source = tmp_path / "source.jsonl"
    output = tmp_path / "out.jsonl"
    row = source_row()
    write_jsonl(source, [row])
    write_jsonl(output, [{**row, "record_id": "block:001:001-000:abc", "status": "ok", "translation": "hello 世界"}])
    _summary, issues, retry = validate(args(tmp_path, output, source))
    assert any(issue["kind"] == "cjk_leakage" for issue in issues)
    assert retry == [row]
