#!/usr/bin/env python3
"""Generate contact sheets and an HTML review page from scan metrics."""

from __future__ import annotations

import argparse
import html
import math
import os
from collections import Counter
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageFont

try:
    from scripts.scan_pipeline_common import read_metrics_jsonl
except ModuleNotFoundError:  # pragma: no cover
    from scan_pipeline_common import read_metrics_jsonl  # type: ignore[no-redef]


Record = dict[str, object]


FLAG_GLOSSARY: dict[str, tuple[str, str, str]] = {
    "content_overflow": (
        "high",
        "Detected content is larger than the fixed target canvas.",
        "Inspect for clipping; use a page-specific crop/window override or larger target if needed.",
    ),
    "crop_near_content": (
        "high",
        "Detected content lies very close to the chosen crop window.",
        "Inspect page edges/page numbers and adjust crop_window if anything is tight.",
    ),
    "expanded_margin_overflow": (
        "medium",
        "Content fits, but requested safety margins do not fully fit in the target canvas.",
        "Usually acceptable; inspect if page feels cramped.",
    ),
    "projection_hough_disagree": (
        "medium",
        "Projection-profile skew and Hough-line skew estimates differ.",
        "Inspect baseline angle; override angle_deg if one estimator chose a table/border.",
    ),
    "low_projection_confidence": (
        "medium",
        "Projection-profile skew peak was weak or ambiguous.",
        "Inspect baseline angle; often expected for sparse/table/illustration pages.",
    ),
    "suspicious_angle": (
        "medium",
        "Chosen deskew angle is larger than the normal body-page threshold.",
        "Inspect baseline angle and set angle_deg if the page was over-rotated.",
    ),
    "padding_needed": (
        "low",
        "Crop window extends beyond source pixels and was padded white.",
        "Usually acceptable near scan edges; inspect if content placement looks odd.",
    ),
    "angle_override": ("info", "Angle came from override JSON.", "Confirm override is intentional."),
    "deskew_disabled": ("info", "Deskew was disabled by override/config.", "Expected for conservative cover/front matter."),
    "used_hough_angle": ("info", "Hough fallback angle was used.", "Inspect if tables/rules dominate the page."),
}

FLAG_SHORT_NAMES = {
    "content_overflow": "overflow",
    "crop_near_content": "near crop",
    "expanded_margin_overflow": "margin",
    "projection_hough_disagree": "hough≠proj",
    "low_projection_confidence": "low skew",
    "suspicious_angle": "angle",
    "padding_needed": "padding",
    "angle_override": "override",
    "deskew_disabled": "no deskew",
    "used_hough_angle": "hough used",
}

SEVERITY_ORDER = {"high": 0, "medium": 1, "low": 2, "info": 3}


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--metrics", type=Path, required=True)
    parser.add_argument("--processed-dir", type=Path, required=True)
    parser.add_argument("--debug-dir", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--thumb-width", type=int, default=240)
    parser.add_argument("--per-sheet", type=int, default=50)
    return parser.parse_args(argv)


def chunks(items: list[Record], size: int) -> Iterable[list[Record]]:
    for index in range(0, len(items), size):
        yield items[index : index + size]


def image_path_for(record: Record, processed_dir: Path, debug_dir: Path) -> Path:
    name = str(record["output_name"])
    debug_path = debug_dir / name
    if debug_path.exists():
        return debug_path
    return processed_dir / name


def load_image(path: Path, *, width: int) -> Image.Image:
    if path.exists():
        img = Image.open(path).convert("RGB")
    else:
        img = Image.new("RGB", (width, int(width * 1.4)), "white")
        draw = ImageDraw.Draw(img)
        draw.text((10, 10), f"missing\n{path.name}", fill=(180, 0, 0))
        return img

    scale = width / float(img.width)
    height = max(1, round(img.height * scale))
    return img.resize((width, height), Image.Resampling.LANCZOS)


def flags_for(record: Record) -> list[str]:
    flags = record.get("flags", [])
    if not isinstance(flags, list):
        return [str(flags)] if flags else []
    return [str(flag) for flag in flags]


def label_for(record: Record) -> str:
    page = int(record.get("page_number", 0))
    angle = float(record.get("angle_used", 0.0))
    flags = flags_for(record)
    short_flags = [FLAG_SHORT_NAMES.get(flag, flag) for flag in flags]
    flag_text = ", ".join(short_flags[:3]) if short_flags else "ok"
    if len(short_flags) > 3:
        flag_text += f" +{len(short_flags) - 3}"
    return f"{page:03d} {angle:+.2f}°\n{flag_text}"


def flag_counts(records: list[Record]) -> Counter[str]:
    counts: Counter[str] = Counter()
    for record in records:
        counts.update(flags_for(record))
    return counts


def flag_severity(flag: str) -> str:
    return FLAG_GLOSSARY.get(flag, ("info", "", ""))[0]


def priority_score(record: Record) -> tuple[int, int, int]:
    flags = flags_for(record)
    if not flags:
        return (99, 0, int(record.get("page_number", 0)))
    severity = min(SEVERITY_ORDER.get(flag_severity(flag), 3) for flag in flags)
    return (severity, -len(flags), int(record.get("page_number", 0)))


def make_sheet(
    records: list[Record],
    *,
    processed_dir: Path,
    debug_dir: Path,
    out_path: Path,
    thumb_width: int,
    title: str,
) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if not records:
        img = Image.new("RGB", (thumb_width * 2, 120), "white")
        draw = ImageDraw.Draw(img)
        draw.text((12, 12), f"{title}: no pages", fill=(0, 0, 0))
        img.save(out_path, quality=90)
        return

    columns = max(1, min(5, math.ceil(math.sqrt(len(records)))))
    label_h = 58
    gap = 8
    thumbs: list[tuple[Image.Image, str]] = []
    max_thumb_h = 0
    for record in records:
        thumb = load_image(image_path_for(record, processed_dir, debug_dir), width=thumb_width)
        max_thumb_h = max(max_thumb_h, thumb.height)
        thumbs.append((thumb, label_for(record)))

    rows = math.ceil(len(thumbs) / columns)
    title_h = 34
    sheet_w = columns * thumb_width + (columns + 1) * gap
    sheet_h = title_h + rows * (max_thumb_h + label_h + gap) + gap
    sheet = Image.new("RGB", (sheet_w, sheet_h), "white")
    draw = ImageDraw.Draw(sheet)
    draw.text((gap, 8), title, fill=(0, 0, 0))

    for index, (thumb, label) in enumerate(thumbs):
        row, col = divmod(index, columns)
        x = gap + col * (thumb_width + gap)
        y = title_h + row * (max_thumb_h + label_h + gap)
        sheet.paste(thumb, (x, y))
        draw.rectangle((x, y, x + thumb_width - 1, y + thumb.height - 1), outline=(160, 160, 160))
        draw.multiline_text((x + 2, y + max_thumb_h + 4), label[:84], fill=(0, 0, 0), spacing=2)

    sheet.save(out_path, quality=90)


def records_with_flags(records: list[Record], *flag_names: str) -> list[Record]:
    wanted = set(flag_names)
    selected: list[Record] = []
    for record in records:
        flags = record.get("flags", [])
        if isinstance(flags, list) and wanted.intersection(str(flag) for flag in flags):
            selected.append(record)
    return selected


def high_angle_records(records: list[Record]) -> list[Record]:
    return [record for record in records if abs(float(record.get("angle_used", 0.0))) > 1.5]


def low_projection_records(records: list[Record]) -> list[Record]:
    selected: list[Record] = []
    for record in records:
        peak = float(record.get("projection_peak_z", 0.0))
        flags = record.get("flags", [])
        if peak < 5.0 or (isinstance(flags, list) and "low_projection_confidence" in flags):
            selected.append(record)
    return selected


def relative_link(from_dir: Path, target: Path) -> str:
    return html.escape(os.path.relpath(target, start=from_dir))


def build_review_html(
    records: list[Record],
    image_links: list[Path],
    out_dir: Path,
    *,
    processed_dir: Path,
    debug_dir: Path,
    metadata_dir: Path,
) -> None:
    counts = flag_counts(records)
    count_rows = "\n".join(
        "<tr>"
        f"<td><code>{html.escape(flag)}</code></td>"
        f"<td>{count}</td>"
        f"<td>{html.escape(flag_severity(flag))}</td>"
        f"<td>{html.escape(FLAG_GLOSSARY.get(flag, ('info', 'Unrecognized flag.', 'Inspect manually.'))[1])}</td>"
        f"<td>{html.escape(FLAG_GLOSSARY.get(flag, ('info', 'Unrecognized flag.', 'Inspect manually.'))[2])}</td>"
        "</tr>"
        for flag, count in sorted(counts.items(), key=lambda item: (SEVERITY_ORDER.get(flag_severity(item[0]), 3), item[0]))
    )
    if not count_rows:
        count_rows = '<tr><td colspan="5">No flags.</td></tr>'

    priority_records = sorted([record for record in records if flags_for(record)], key=priority_score)[:30]
    priority_items = "\n".join(
        f'<li><a href="#page-{int(record.get("page_number", 0)):03d}">'
        f'{int(record.get("page_number", 0)):03d} — {html.escape(str(record.get("output_name", "")))}'
        f'</a>: {html.escape(", ".join(flags_for(record)))}</li>'
        for record in priority_records
    ) or "<li>No flagged pages.</li>"

    rows: list[str] = []
    for record in records:
        flags = flags_for(record)
        flag_text = ", ".join(f"<code>{html.escape(flag)}</code>" for flag in flags)
        output_name_raw = str(record.get("output_name", ""))
        output_name = html.escape(output_name_raw)
        source_name = html.escape(str(record.get("source_filename", "")))
        page = int(record.get("page_number", 0))
        processed_path = processed_dir / output_name_raw
        debug_path = debug_dir / output_name_raw
        metadata_path = metadata_dir / f"{Path(output_name_raw).stem}.json"
        rows.append(
            f'<tr id="page-{page:03d}">'
            f'<th scope="row">{page:03d}</th>'
            f"<td>{output_name}</td>"
            f"<td>{source_name}</td>"
            f'<td><a href="{relative_link(out_dir, processed_path)}">image</a></td>'
            f'<td><a href="{relative_link(out_dir, debug_path)}">debug</a></td>'
            f'<td><a href="{relative_link(out_dir, metadata_path)}">json</a></td>'
            f"<td>{float(record.get('angle_used', 0.0)):+.2f}</td>"
            f"<td>{float(record.get('projection_peak_z', 0.0)):.2f}</td>"
            f"<td>{html.escape(str(record.get('min_crop_margin', '')))}</td>"
            f"<td>{html.escape(str(record.get('padding_px', '')))}</td>"
            f"<td>{flag_text or 'ok'}</td>"
            "</tr>"
        )

    links = "\n".join(
        f'<li><a href="{relative_link(out_dir, path)}">{html.escape(path.name)}</a></li>' for path in image_links
    )
    document = f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\">
<title>Scan QA Review</title>
<style>
body {{ font-family: sans-serif; margin: 2rem; line-height: 1.35; }}
.table-wrap {{ overflow-x: auto; }}
table {{ border-collapse: collapse; width: 100%; margin: 1rem 0; }}
caption {{ text-align: left; font-weight: bold; margin: 0.5rem 0; }}
th, td {{ border: 1px solid #ccc; padding: 0.25rem 0.4rem; font-size: 0.9rem; vertical-align: top; }}
th {{ background: #f3f3f3; }}
thead th {{ position: sticky; top: 0; z-index: 1; }}
code {{ white-space: nowrap; }}
.note {{ background: #fff8d8; border: 1px solid #e6d27a; padding: 0.75rem; }}
</style>
</head>
<body>
<h1>Scan QA Review</h1>
<p class="note">Structural validation can pass while QA flags are present. Flags are review prompts: inspect high-priority pages, apply overrides when needed, then regenerate QA.</p>
<p>Pages: {len(records)}. Contact sheets use debug overlays when available and processed images otherwise.</p>
<h2>Sheets</h2>
<ul>
{links}
</ul>
<h2>Flag summary and glossary</h2>
<div class="table-wrap">
<table>
<caption>Flag counts, severity, and recommended action</caption>
<thead><tr><th scope="col">Flag</th><th scope="col">Count</th><th scope="col">Severity</th><th scope="col">Meaning</th><th scope="col">Suggested action</th></tr></thead>
<tbody>
{count_rows}
</tbody>
</table>
</div>
<h2>Highest priority pages to inspect</h2>
<ol>
{priority_items}
</ol>
<h2>Metrics</h2>
<div class="table-wrap">
<table>
<caption>Per-page outputs, links, crop metrics, and flags</caption>
<thead><tr><th scope="col">Page</th><th scope="col">Output</th><th scope="col">Source</th><th scope="col">Processed</th><th scope="col">Debug</th><th scope="col">Metadata</th><th scope="col">Angle</th><th scope="col">Projection z</th><th scope="col">Min margin</th><th scope="col">Padding</th><th scope="col">Flags</th></tr></thead>
<tbody>
{''.join(rows)}
</tbody>
</table>
</div>
</body>
</html>
"""
    (out_dir / "review.html").write_text(document, encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.thumb_width <= 0:
        raise SystemExit("--thumb-width must be positive")
    if args.per_sheet <= 0:
        raise SystemExit("--per-sheet must be positive")

    records = read_metrics_jsonl(args.metrics)
    records.sort(key=lambda record: int(record.get("page_number", 0)))
    contact_dir = args.out / "contact-all"
    outlier_dir = args.out / "contact-outliers"
    image_links: list[Path] = []

    for group in chunks(records, args.per_sheet):
        first = int(group[0].get("page_number", 0))
        last = int(group[-1].get("page_number", 0))
        out_path = contact_dir / f"contact-{first:03d}-{last:03d}.jpg"
        make_sheet(
            group,
            processed_dir=args.processed_dir,
            debug_dir=args.debug_dir,
            out_path=out_path,
            thumb_width=args.thumb_width,
            title=f"All pages {first:03d}-{last:03d}",
        )
        image_links.append(out_path)

    outlier_groups: list[tuple[str, list[Record]]] = [
        ("all-flagged", [record for record in records if record.get("flags")]),
        ("low-skew-confidence", low_projection_records(records)),
        ("crop-near-edge", records_with_flags(records, "crop_near_content", "content_overflow")),
        ("large-padding", records_with_flags(records, "padding_needed")),
        ("large-angle", high_angle_records(records)),
    ]
    for name, group in outlier_groups:
        out_path = outlier_dir / f"{name}.jpg"
        make_sheet(
            group,
            processed_dir=args.processed_dir,
            debug_dir=args.debug_dir,
            out_path=out_path,
            thumb_width=args.thumb_width,
            title=name.replace("-", " "),
        )
        image_links.append(out_path)

    build_review_html(
        records,
        image_links,
        args.out,
        processed_dir=args.processed_dir,
        debug_dir=args.debug_dir,
        metadata_dir=args.metrics.parent / "metadata",
    )
    print(f"wrote QA review: {args.out / 'review.html'}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
