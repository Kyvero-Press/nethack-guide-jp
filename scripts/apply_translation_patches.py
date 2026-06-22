#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml

try:
    from scripts.translated_pdf_common import BlockSource, cjk_ratio, load_block_sources, read_jsonl, source_record_id, write_jsonl
except ModuleNotFoundError:  # direct script execution
    from translated_pdf_common import BlockSource, cjk_ratio, load_block_sources, read_jsonl, source_record_id, write_jsonl


def load_patch_rows(path: Path | None) -> list[dict[str, Any]]:
    if not path or not path.exists():
        return []
    payload = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    patches = payload.get("patches") or []
    if not isinstance(patches, list):
        raise ValueError("patches must be a list")
    out: list[dict[str, Any]] = []
    for item in patches:
        if not isinstance(item, dict):
            raise ValueError(f"invalid patch item: {item!r}")
        if not item.get("block_id") or item.get("translation") is None:
            raise ValueError(f"patch requires block_id and translation: {item!r}")
        out.append(dict(item))
    return out


def rank_record(row: dict[str, Any]) -> tuple[int, float]:
    if row.get("status") != "ok" or not str(row.get("translation") or "").strip():
        return (0, 0.0)
    text = str(row.get("translation") or "")
    # Prefer lower CJK leakage and non-passthrough translated rows when both exist.
    score = 10.0 - cjk_ratio(text) * 10.0
    if row.get("passthrough_non_cjk"):
        score -= 0.1
    return (1, score)


def merge_records(source_rows: list[BlockSource], inputs: list[Path], patches: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    source_by_key = {source_record_id(block.to_row()): block for block in source_rows}
    best: dict[str, dict[str, Any]] = {}
    candidates: dict[str, list[dict[str, Any]]] = {key: [] for key in source_by_key}
    for path in inputs:
        if not path or not path.exists():
            continue
        for row in read_jsonl(path):
            if row.get("record_type") != "block" and not row.get("block_id"):
                continue
            key = source_record_id(row)
            candidates.setdefault(key, []).append(row)
            if key not in source_by_key:
                continue
            if key not in best or rank_record(row) >= rank_record(best[key]):
                best[key] = dict(row)

    patches_by_block: dict[str, dict[str, Any]] = {}
    for patch in patches:
        block_id = str(patch["block_id"])
        if block_id in patches_by_block:
            raise ValueError(f"duplicate patch for {block_id}")
        patches_by_block[block_id] = patch

    final_rows: list[dict[str, Any]] = []
    patch_count = 0
    missing_count = 0
    for source in source_rows:
        source_row = source.to_row()
        key = source_record_id(source_row)
        row = dict(best.get(key) or {})
        if not row:
            missing_count += 1
            row = {
                **source_row,
                "record_id": key,
                "status": "missing",
                "error": "no raw/retry translation record found",
                "translation": "",
                "model": None,
            }
        patch = patches_by_block.get(source.block_id)
        if patch:
            guard = patch.get("source_sha256")
            if guard and str(guard) != source.source_sha256:
                raise ValueError(f"source_sha256 guard mismatch for patch {source.block_id}")
            row.update(source_row)
            row["record_id"] = key
            row["status"] = "ok"
            row["error"] = ""
            row["translation"] = str(patch["translation"]).strip()
            row["patched"] = True
            row["patch_reason"] = str(patch.get("reason") or "manual patch")
            row["patch_source"] = str(patch.get("source") or "config/block-translation-patches.yaml")
            patch_count += 1
        else:
            # Ensure final rows always carry source metadata exactly from the current source contract.
            row.update(source_row)
            row.setdefault("record_id", key)
            row.setdefault("patched", False)
        final_rows.append(row)

    report = {
        "source_records": len(source_rows),
        "final_records": len(final_rows),
        "input_files": [str(path) for path in inputs if path and path.exists()],
        "candidate_records": sum(len(v) for v in candidates.values()),
        "manual_patches": patch_count,
        "missing_records": missing_count,
        "patched_block_ids": sorted(patches_by_block),
    }
    return final_rows, report


def main() -> None:
    parser = argparse.ArgumentParser(description="Merge raw/retry/manual block translations into a final JSONL.")
    parser.add_argument("--source-jsonl", type=Path, required=True)
    parser.add_argument("--input", type=Path, required=True, help="Raw translation JSONL")
    parser.add_argument("--retry", type=Path, action="append", default=[])
    parser.add_argument("--patches", type=Path, default=Path("config/block-translation-patches.yaml"))
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()

    sources = load_block_sources(args.source_jsonl)
    patches = load_patch_rows(args.patches)
    inputs = [args.input, *args.retry]
    final_rows, report = merge_records(sources, inputs, patches)
    write_jsonl(args.output, final_rows)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {len(final_rows)} final records to {args.output}")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()
