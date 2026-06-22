#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

try:
    from scripts.translated_pdf_common import CJK_RE, cjk_ratio, read_jsonl, repeated_loop, source_record_id, write_jsonl
except ModuleNotFoundError:  # direct script execution
    from translated_pdf_common import CJK_RE, cjk_ratio, read_jsonl, repeated_loop, source_record_id, write_jsonl


def output_key(row: dict[str, Any], record_type: str) -> str:
    if record_type == "block":
        return f"block:{row.get('page_label')}:{row.get('block_id')}:{row.get('source_sha256')}"
    return f"page:{row.get('page_label')}:{row.get('source_sha256')}"


def make_issue(kind: str, severity: str, row: dict[str, Any] | None = None, **extra: Any) -> dict[str, Any]:
    item = {"kind": kind, "severity": severity}
    if row:
        item.update(
            {
                "record_id": row.get("record_id") or output_key(row, "block" if row.get("block_id") else "page"),
                "page": row.get("page"),
                "page_label": row.get("page_label"),
                "block_id": row.get("block_id"),
                "source_sha256": row.get("source_sha256"),
            }
        )
    item.update(extra)
    return item


def source_index(rows: list[dict[str, Any]], record_type: str) -> dict[str, dict[str, Any]]:
    if not rows:
        return {}
    idx: dict[str, dict[str, Any]] = {}
    for row in rows:
        if record_type != "auto" and row.get("record_type") != record_type:
            continue
        key = source_record_id(row)
        idx[key] = row
    return idx


def validate(args: argparse.Namespace) -> tuple[dict[str, Any], list[dict[str, Any]], list[dict[str, Any]]]:
    rows = read_jsonl(args.input)
    record_type = args.record_type
    if record_type == "auto":
        record_type = "block" if any("block_id" in row for row in rows) else "page"

    sources = source_index(read_jsonl(args.source_jsonl), record_type) if args.source_jsonl else {}
    ok_rows = [row for row in rows if row.get("status") == "ok" and str(row.get("translation") or "").strip()]
    error_rows = [row for row in rows if row.get("status") != "ok" or not str(row.get("translation") or "").strip()]
    pages = {int(row["page"]) for row in ok_rows if row.get("page") is not None}

    issues: list[dict[str, Any]] = []
    retry_keys: set[str] = set()

    key_counts = Counter(output_key(row, record_type) for row in rows)
    for key, count in key_counts.items():
        if count > 1:
            issues.append(make_issue("duplicate_record", "hard", record_id=key, count=count))
            retry_keys.add(key)

    by_key: dict[str, dict[str, Any]] = {}
    for row in rows:
        by_key[output_key(row, record_type)] = row

    if sources:
        for key, source in sources.items():
            if key not in by_key:
                issues.append(make_issue("missing_record", "hard", source, record_id=key))
                retry_keys.add(key)
        for key, row in by_key.items():
            if key not in sources:
                issues.append(make_issue("unexpected_record", "soft", row, record_id=key))

    for row in error_rows:
        key = output_key(row, record_type)
        issues.append(make_issue("error_or_empty", "hard", row, status=row.get("status"), error=row.get("error")))
        retry_keys.add(key)

    for row in ok_rows:
        text = str(row.get("translation") or "")
        source_text = str(row.get("source_text") or "")
        key = output_key(row, record_type)
        ratio = cjk_ratio(text)
        repeated = repeated_loop(text)
        if ratio > args.max_ja_ratio:
            issues.append(make_issue("cjk_leakage", "hard", row, cjk_ratio=ratio, preview=text[:160]))
            retry_keys.add(key)
        if repeated:
            issues.append(make_issue("repeated_output", "hard", row, preview=text[:160]))
            retry_keys.add(key)
        if source_text.strip() and text.strip() == source_text.strip() and CJK_RE.search(source_text):
            issues.append(make_issue("unchanged_cjk_source", "hard", row, preview=text[:160]))
            retry_keys.add(key)
        if len(source_text) >= 80 and len(text) < max(12, len(source_text) * args.min_length_ratio):
            issues.append(
                make_issue(
                    "suspiciously_short",
                    "soft",
                    row,
                    source_chars=len(source_text),
                    translation_chars=len(text),
                    preview=text[:160],
                )
            )
        if len(source_text) >= 20 and len(text) > len(source_text) * args.max_length_ratio + 120:
            issues.append(
                make_issue(
                    "suspiciously_long",
                    "soft",
                    row,
                    source_chars=len(source_text),
                    translation_chars=len(text),
                    preview=text[:160],
                )
            )

    hard = [issue for issue in issues if issue.get("severity") == "hard"]
    soft = [issue for issue in issues if issue.get("severity") != "hard"]
    summary = {
        "input": str(args.input),
        "source_jsonl": str(args.source_jsonl) if args.source_jsonl else None,
        "record_type": record_type,
        "rows": len(rows),
        "ok": len(ok_rows),
        "errors": len(error_rows),
        "pages": len(pages),
        "expected_records": args.expected_records,
        "expected_pages": args.expected_pages,
        "source_records": len(sources) if sources else None,
        "hard_issues": len(hard),
        "soft_issues": len(soft),
        "retry_records": len(retry_keys),
    }

    if args.expected_records and len(ok_rows) != args.expected_records:
        issues.append(make_issue("expected_record_count_mismatch", "hard", expected=args.expected_records, actual=len(ok_rows)))
    if args.expected_pages and len(pages) != args.expected_pages:
        issues.append(make_issue("expected_page_count_mismatch", "hard", expected=args.expected_pages, actual=len(pages)))
    if sources and len(ok_rows) < len(sources):
        # Already represented by missing/error issues, but useful in summary.
        summary["missing_or_non_ok"] = len(sources) - len(ok_rows)

    retry_rows: list[dict[str, Any]] = []
    if sources:
        for key in sorted(retry_keys):
            if key in sources:
                retry_rows.append(sources[key])

    return summary, issues, retry_rows


def write_markdown(path: Path, summary: dict[str, Any], issues: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# Translation validation report\n", "\n## Summary\n\n"]
    for key in sorted(summary):
        lines.append(f"- `{key}`: {summary[key]}\n")
    lines.append("\n## Issues\n\n")
    if not issues:
        lines.append("No issues.\n")
    else:
        by_kind: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for issue in issues:
            by_kind[str(issue.get("kind"))].append(issue)
        for kind, kind_issues in sorted(by_kind.items()):
            lines.append(f"### {kind} ({len(kind_issues)})\n\n")
            for issue in kind_issues[:100]:
                loc = issue.get("block_id") or issue.get("page_label") or issue.get("record_id")
                preview = str(issue.get("preview") or "").replace("\n", " ")[:180]
                lines.append(f"- `{issue.get('severity')}` `{loc}` {preview}\n")
            if len(kind_issues) > 100:
                lines.append(f"- ... {len(kind_issues) - 100} more\n")
            lines.append("\n")
    path.write_text("".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate local translation JSONL outputs.")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--source-jsonl", type=Path)
    parser.add_argument("--record-type", choices=["auto", "page", "block"], default="auto")
    parser.add_argument("--expected-records", type=int, default=0)
    parser.add_argument("--expected-pages", type=int, default=0)
    parser.add_argument("--max-ja-ratio", type=float, default=0.25)
    parser.add_argument("--min-length-ratio", type=float, default=0.18)
    parser.add_argument("--max-length-ratio", type=float, default=5.0)
    parser.add_argument("--write-report", type=Path)
    parser.add_argument("--write-report-md", type=Path)
    parser.add_argument("--write-retry-jsonl", type=Path)
    parser.add_argument("--allow-issues", action="store_true", help="Exit zero even when hard validation issues are present")
    args = parser.parse_args()

    summary, issues, retry_rows = validate(args)
    print(f"rows={summary['rows']} ok={summary['ok']} errors={summary['errors']} pages={summary['pages']}")
    print(f"hard_issues={summary['hard_issues']} soft_issues={summary['soft_issues']} retry_records={len(retry_rows)}")
    for issue in issues[:30]:
        print(json.dumps(issue, ensure_ascii=False))

    if args.write_report:
        args.write_report.parent.mkdir(parents=True, exist_ok=True)
        args.write_report.write_text(json.dumps({"summary": summary, "issues": issues}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.write_report_md:
        write_markdown(args.write_report_md, summary, issues)
    if args.write_retry_jsonl:
        write_jsonl(args.write_retry_jsonl, retry_rows)
        print(f"wrote retry source records: {args.write_retry_jsonl} ({len(retry_rows)})")

    hard_count = sum(1 for issue in issues if issue.get("severity") == "hard")
    if hard_count and not args.allow_issues:
        raise SystemExit(1)
    if summary.get("expected_records") and summary["ok"] != summary["expected_records"] and not args.allow_issues:
        raise SystemExit(1)
    if summary.get("expected_pages") and summary["pages"] != summary["expected_pages"] and not args.allow_issues:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
