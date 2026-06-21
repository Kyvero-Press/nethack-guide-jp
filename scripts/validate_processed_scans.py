#!/usr/bin/env python3
"""Validate processed scan outputs against pdforder, metrics, and sidecars."""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

from PIL import Image

try:
    from scripts.scan_pipeline_common import parse_page_range, parse_pdforder, parse_target_size, read_metrics_jsonl
except ModuleNotFoundError:  # pragma: no cover
    from scan_pipeline_common import parse_page_range, parse_pdforder, parse_target_size, read_metrics_jsonl  # type: ignore[no-redef]


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdforder", type=Path, required=True)
    parser.add_argument("--processed-dir", type=Path, required=True)
    parser.add_argument("--metrics", type=Path, required=True)
    parser.add_argument("--target", required=True, help="expected WIDTHxHEIGHT, or auto to use each metric target_size")
    parser.add_argument("--expected-pages", type=int, default=None)
    parser.add_argument("--pages", default=None)
    parser.add_argument(
        "--fail-on-flags",
        default="",
        help="comma-separated metric flags that should make validation fail, e.g. content_overflow,crop_near_content",
    )
    return parser.parse_args(argv)


def expected_names(pdforder: Path, pages_spec: str | None) -> list[str]:
    order = parse_pdforder(pdforder)
    pages = parse_page_range(pages_spec)
    if pages is None:
        return order
    for page_number in pages:
        if page_number < 1 or page_number > len(order):
            raise ValueError(f"requested page {page_number:03d} outside pdforder length {len(order)}")
    wanted = set(pages)
    return [name for page_number, name in enumerate(order, start=1) if page_number in wanted]


def metadata_dir_for(metrics_path: Path) -> Path:
    return metrics_path.parent / "metadata"


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    target_size_auto = args.target.strip().lower() == "auto"
    target_w = target_h = 0
    if not target_size_auto:
        target_w, target_h = parse_target_size(args.target)
    names = expected_names(args.pdforder, args.pages)
    errors: list[str] = []

    if args.expected_pages is not None and len(names) != args.expected_pages:
        errors.append(f"expected page selection count {args.expected_pages}, got {len(names)}")

    if not args.metrics.exists():
        errors.append(f"missing metrics file: {args.metrics}")
        metrics = []
    else:
        metrics = read_metrics_jsonl(args.metrics)

    metrics_by_name = {str(record.get("output_name")): record for record in metrics}
    metric_order = [str(record.get("output_name")) for record in metrics]
    if metric_order != names:
        errors.append("metrics order does not match requested pdforder pages")
        missing_metrics = [name for name in names if name not in metrics_by_name]
        extra_metrics = [name for name in metric_order if name not in set(names)]
        if missing_metrics:
            errors.append(f"metrics missing pages: {missing_metrics[:5]}")
        if extra_metrics:
            errors.append(f"metrics has unexpected pages: {extra_metrics[:5]}")

    sidecar_dir = metadata_dir_for(args.metrics)
    fail_flags = {flag.strip() for flag in args.fail_on_flags.split(",") if flag.strip()}
    flag_counts: Counter[str] = Counter()
    failed_flag_pages: dict[str, list[str]] = {flag: [] for flag in fail_flags}
    for name in names:
        path = args.processed_dir / name
        if not path.exists():
            errors.append(f"missing processed page: {path}")
            continue
        record = metrics_by_name.get(name)
        try:
            with Image.open(path) as img:
                expected_size = (target_w, target_h)
                if target_size_auto:
                    if record is None:
                        errors.append(f"cannot auto-validate dimensions without metrics for {name}")
                        expected_size = img.size
                    else:
                        metric_size = record.get("target_size") or record.get("output_size")
                        if not isinstance(metric_size, list) or len(metric_size) != 2:
                            errors.append(f"metrics missing target_size for {name}")
                            expected_size = img.size
                        else:
                            expected_size = (int(metric_size[0]), int(metric_size[1]))
                if img.size != expected_size:
                    errors.append(f"wrong dimensions for {name}: {img.size[0]}x{img.size[1]} expected {expected_size[0]}x{expected_size[1]}")
        except Exception as exc:
            errors.append(f"cannot read processed page {path}: {exc}")

        sidecar = sidecar_dir / f"{Path(name).stem}.json"
        if not sidecar.exists():
            errors.append(f"missing metadata sidecar: {sidecar}")

        if record is not None:
            flags = record.get("flags", [])
            if isinstance(flags, list):
                flag_strings = [str(flag) for flag in flags]
                flag_counts.update(flag_strings)
                for flag in fail_flags.intersection(flag_strings):
                    failed_flag_pages.setdefault(flag, []).append(name)

    print(f"validated requested pages: {len(names)}")
    print(f"processed directory: {args.processed_dir}")
    print(f"metrics records: {len(metrics)}")
    if flag_counts:
        print("flags:")
        for flag, count in sorted(flag_counts.items()):
            print(f"  {flag}: {count}")
    else:
        print("flags: none")

    for flag, pages in sorted(failed_flag_pages.items()):
        if pages:
            errors.append(f"flag {flag!r} present on {len(pages)} page(s), e.g. {pages[:5]}")

    if errors:
        print("validation FAILED:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1
    if flag_counts and not fail_flags:
        print("structural validation PASS (QA flags are present; review contact sheets/metrics before publishing)")
    else:
        print("validation PASS")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
