#!/usr/bin/env python3
"""Process renamed raw scans into fixed-size page images plus QA metadata."""

from __future__ import annotations

import argparse
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

import cv2

try:  # Allow both `python scripts/process_scans.py` and package imports in tests.
    from scripts.scan_pipeline_common import (
        PageMetrics,
        PageTask,
        apply_split,
        apply_trim_insets,
        bbox_area,
        bbox_overflows,
        build_page_tasks,
        choose_fixed_window,
        content_bbox,
        crop_with_padding,
        detect_scanner_tail,
        estimate_skew_hough,
        estimate_skew_line_segments,
        estimate_skew_projection,
        expand_bbox,
        imread_color,
        imwrite_checked,
        infer_page_side,
        load_overrides,
        locate_reference_crop_window,
        make_debug_overlay,
        make_ink_mask_with_stats,
        metrics_to_json,
        min_margin,
        normalize_background,
        parse_page_range,
        parse_target_size,
        read_metrics_jsonl,
        resize_for_analysis,
        resolve_page_overrides,
        rotate_image,
        scale_bbox,
        selected_tasks,
        to_gray,
        trim_insets_for_page,
        window_padding_px,
        write_json,
        write_metrics_jsonl,
    )
except ModuleNotFoundError:  # pragma: no cover - exercised by direct CLI use.
    from scan_pipeline_common import (  # type: ignore[no-redef]
        PageMetrics,
        PageTask,
        apply_split,
        apply_trim_insets,
        bbox_area,
        bbox_overflows,
        build_page_tasks,
        choose_fixed_window,
        content_bbox,
        crop_with_padding,
        detect_scanner_tail,
        estimate_skew_hough,
        estimate_skew_line_segments,
        estimate_skew_projection,
        expand_bbox,
        imread_color,
        imwrite_checked,
        infer_page_side,
        load_overrides,
        locate_reference_crop_window,
        make_debug_overlay,
        make_ink_mask_with_stats,
        metrics_to_json,
        min_margin,
        normalize_background,
        parse_page_range,
        parse_target_size,
        read_metrics_jsonl,
        resize_for_analysis,
        resolve_page_overrides,
        rotate_image,
        scale_bbox,
        selected_tasks,
        to_gray,
        trim_insets_for_page,
        window_padding_px,
        write_json,
        write_metrics_jsonl,
    )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scan-dir", type=Path, default=Path("scan"))
    parser.add_argument("--manifest", type=Path, default=Path("scan/pdforder-rename-manifest.tsv"))
    parser.add_argument("--pdforder", type=Path, default=Path("dist/pdforder.txt"))
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--target", default="1788x2512", help="fixed output canvas, WIDTHxHEIGHT")
    parser.add_argument("--overrides", type=Path, default=None)
    parser.add_argument(
        "--reference-crops",
        type=Path,
        default=None,
        help="directory of existing cropped pages to use as page-size/crop priors (for this repo, dist/crops/reference/)",
    )
    parser.add_argument("--pages", default=None, help="comma page/range spec, e.g. 001-011,050")
    parser.add_argument("--jobs", type=int, default=1)
    parser.add_argument("--force", action="store_true", help="allow replacing a non-empty output directory")
    parser.add_argument("--debug", action="store_true", help="write debug overlays")
    return parser.parse_args(argv)


def is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
    except ValueError:
        return False
    return True


def is_safe_force_delete_target(out_dir: Path) -> bool:
    """Return true only for generated processing directories we own.

    `--force` uses recursive deletion, so keep it narrowly scoped to the
    documented generated output locations.  Users may still write to a new empty
    directory elsewhere, but replacing non-empty arbitrary directories such as
    the repository root, `dist/`, or `scan/` is never allowed.
    """

    out_resolved = out_dir.resolve()
    work_root = (Path.cwd() / "work").resolve()
    return is_relative_to(out_resolved, work_root) and out_resolved.name.startswith("processed")


def prepare_output_dir(out_dir: Path, scan_dir: Path, *, force: bool) -> None:
    out_resolved = out_dir.resolve()
    cwd_resolved = Path.cwd().resolve()
    scan_resolved = scan_dir.resolve()
    dist_resolved = (Path.cwd() / "dist").resolve()
    if out_resolved in {cwd_resolved, scan_resolved, dist_resolved}:
        raise SystemExit(f"refusing to use protected directory as output: {out_dir}")
    if is_relative_to(out_resolved, scan_resolved):
        raise SystemExit(f"refusing to write output inside scan directory: {out_dir}")
    if is_relative_to(out_resolved, dist_resolved):
        raise SystemExit(f"refusing to write output inside dist directory: {out_dir}")

    if out_dir.exists() and not out_dir.is_dir():
        raise SystemExit(f"output path exists and is not a directory: {out_dir}")

    if out_dir.exists() and any(out_dir.iterdir()):
        if not force:
            raise SystemExit(f"refusing to use non-empty output directory without --force: {out_dir}")
        if not is_safe_force_delete_target(out_dir):
            raise SystemExit(
                "refusing --force deletion outside generated work/processed* directories: "
                f"{out_dir}"
            )
        shutil.rmtree(out_dir)

    for name in ("color", "gray_for_ocr", "debug", "metadata"):
        (out_dir / name).mkdir(parents=True, exist_ok=True)


def _as_bbox(value: Any, field_name: str) -> tuple[int, int, int, int]:
    if not isinstance(value, (list, tuple)) or len(value) != 4:
        raise ValueError(f"{field_name} must be a four-element list")
    return tuple(int(v) for v in value)  # type: ignore[return-value]


def _target_from_config(task: PageTask, config: dict[str, Any]) -> tuple[int, int]:
    value = config.get("target_size", task.target_size)
    if not isinstance(value, (list, tuple)) or len(value) != 2:
        raise ValueError("target_size override must be [width, height]")
    return (int(value[0]), int(value[1]))


def _margins_for_mode(mode: str, config: dict[str, Any]) -> tuple[int, int, int]:
    prefix = "front" if mode in {"cover", "front"} else "body"
    margin_x = int(config.get("margin_x", config.get(f"{prefix}_margin_x", config.get("body_margin_x", 95))))
    margin_top = int(config.get("margin_top", config.get(f"{prefix}_margin_top", config.get("body_margin_top", 95))))
    margin_bottom = int(
        config.get("margin_bottom", config.get(f"{prefix}_margin_bottom", config.get("body_margin_bottom", 135)))
    )
    return margin_x, margin_top, margin_bottom


def _projection_second_gap(scores: list[tuple[float, float]]) -> float:
    if len(scores) < 2:
        return 0.0
    values = sorted(score for _angle, score in scores)
    return float(values[-1] - values[-2])


def process_task(
    task: PageTask,
    out_dir: Path,
    overrides: dict[str, Any],
    *,
    debug: bool,
    reference_dir: Path | None = None,
) -> PageMetrics:
    config = resolve_page_overrides(task, overrides)
    mode = str(config.get("mode", task.mode))
    target_size = _target_from_config(task, config)
    target_w, target_h = target_size
    flags: list[str] = []

    raw = imread_color(task.source_path)
    split_side = config.get("split", task.split)
    split_options = config.get("split_options") or config.get("split_config") or None
    page_img = apply_split(raw, split_side, split_options)
    source_h, source_w = page_img.shape[:2]

    side_info = infer_page_side(task, config)
    trim_insets: tuple[int, int, int, int] = (0, 0, 0, 0)
    reference_img = None
    reference_crop_window: tuple[int, int, int, int] | None = None
    reference_render_window: tuple[int, int, int, int] | None = None
    reference_match_score: float | None = None
    tail_info = detect_scanner_tail(page_img, config)
    if reference_dir is not None:
        reference_path = reference_dir / task.output_name
        if reference_path.exists():
            reference_img = imread_color(reference_path)
            ref_h, ref_w = reference_img.shape[:2]
            target_size = (ref_w, ref_h)
            target_w, target_h = target_size
            reference_crop_window, reference_match_score = locate_reference_crop_window(page_img, reference_img)
            flags.append("reference_crop")
            if reference_match_score < float(config.get("reference_match_threshold", 0.55)):
                flags.append("low_reference_match")
            tail_info = detect_scanner_tail(reference_img, config)
            if tail_info.detected:
                flags.append("scanner_tail_detected")

            if str(config.get("reference_crop_strategy", "trim")) == "trim":
                trim_insets = trim_insets_for_page(task, config, side_info)
                reference_render_window = apply_trim_insets(reference_crop_window, trim_insets)
                target_w = reference_render_window[2] - reference_render_window[0]
                target_h = reference_render_window[3] - reference_render_window[1]
                target_size = (target_w, target_h)
                if any(trim_insets):
                    flags.append("reference_trim")
            else:
                reference_render_window = reference_crop_window

    analysis_max_dim = int(config.get("analysis_max_dim", 1600))
    if reference_render_window is not None:
        angle_source_img = crop_with_padding(page_img, reference_render_window, pad_color=(255, 255, 255))
    else:
        angle_source_img = page_img
    analysis, _scale = resize_for_analysis(angle_source_img, analysis_max_dim)
    mask_result = make_ink_mask_with_stats(analysis)
    mask = mask_result.mask

    angle_projection: float | None = None
    projection_peak_z = 0.0
    projection_second_gap = 0.0
    angle_hough: float | None = None
    hough_confidence = 0.0
    angle_line: float | None = None
    line_confidence = 0.0
    line_segment_count = 0

    if "angle_deg" in config:
        angle_used = float(config["angle_deg"])
        flags.append("angle_override")
    elif config.get("deskew", True) is False:
        angle_used = 0.0
        angle_projection = 0.0
        projection_peak_z = 999.0
        flags.append("deskew_disabled")
    else:
        max_angle = float(config.get("front_angle_range" if mode in {"cover", "front"} else "body_angle_range", 3.0))
        coarse_step = float(config.get("coarse_step", 0.10))
        fine_step = float(config.get("fine_step", 0.02))
        angle_projection, projection_peak_z, scores = estimate_skew_projection(
            mask,
            max_angle=max_angle,
            coarse_step=coarse_step,
            fine_step=fine_step,
        )
        projection_second_gap = _projection_second_gap(scores)
        angle_used = angle_projection
        if projection_peak_z < float(config.get("low_projection_peak_z", 5.0)):
            flags.append("low_projection_confidence")

        angle_line, line_confidence, line_segment_count = estimate_skew_line_segments(
            analysis,
            max_angle=max_angle,
            min_segments=int(config.get("line_min_segments", 3)),
        )
        if angle_line is not None:
            line_delta = abs(angle_projection - angle_line)
            line_threshold = float(config.get("line_projection_agreement_threshold", 0.25))
            line_conf_threshold = float(config.get("line_confidence_threshold", 2.0))
            if line_confidence >= line_conf_threshold and (
                projection_peak_z < float(config.get("low_projection_peak_z", 5.0)) or line_delta <= line_threshold
            ):
                angle_used = angle_line
                flags.append("used_line_angle")
            elif line_delta > line_threshold:
                flags.append("line_projection_disagree")

        angle_hough, hough_confidence = estimate_skew_hough(mask)
        if angle_hough is not None:
            delta = abs(angle_projection - angle_hough)
            if delta > float(config.get("hough_disagreement_threshold", 0.35)):
                flags.append("projection_hough_disagree")
                if hough_confidence >= 6.0 and projection_peak_z < float(config.get("low_projection_peak_z", 5.0)):
                    angle_used = angle_hough
                    flags.append("used_hough_angle")

    if "used_line_angle" in flags and "low_projection_confidence" in flags:
        flags.remove("low_projection_confidence")
    if abs(angle_used) > float(config.get("suspicious_angle_degrees", 2.0)):
        flags.append("suspicious_angle")

    margin_x, margin_top, margin_bottom = _margins_for_mode(mode, config)

    if reference_render_window is not None and "crop_window" not in config and "content_bbox" not in config:
        # The existing cropped pages define a reliable raw-scan placement prior.
        # Refined mode trims inside that prior (especially the ragged inner edge
        # and stretched bottom rows) instead of exposing the physical page edge.
        rotate_margin = int(config.get("reference_rotate_margin", 180))
        expanded_reference_window = expand_bbox(reference_render_window, rotate_margin, rotate_margin, rotate_margin)
        roi = crop_with_padding(page_img, expanded_reference_window, pad_color=(255, 255, 255))
        rotated_roi = rotate_image(roi, angle_used)
        crop_window = reference_render_window
        cropped = crop_with_padding(
            rotated_roi,
            (rotate_margin, rotate_margin, rotate_margin + target_w, rotate_margin + target_h),
            pad_color=(255, 255, 255),
        )

        cropped_analysis, cropped_scale = resize_for_analysis(cropped, analysis_max_dim)
        rotated_mask_result = make_ink_mask_with_stats(cropped_analysis)
        bbox_in_output = scale_bbox(content_bbox(rotated_mask_result.mask), 1.0 / cropped_scale)
        detected_bbox = (
            crop_window[0] + bbox_in_output[0],
            crop_window[1] + bbox_in_output[1],
            crop_window[0] + bbox_in_output[2],
            crop_window[1] + bbox_in_output[3],
        )
        expanded = expand_bbox(detected_bbox, margin_x, margin_top, margin_bottom)
        if bbox_overflows(bbox_in_output, target_size):
            flags.append("content_overflow")
        elif bbox_overflows(expand_bbox(bbox_in_output, margin_x, margin_top, margin_bottom), target_size):
            flags.append("expanded_margin_overflow")
        padding = window_padding_px(crop_window, page_img.shape)
        debug_base = page_img
        debug_rejected_boxes = ()
    else:
        rotated = rotate_image(page_img, angle_used)
        rotated_analysis, rotated_scale = resize_for_analysis(rotated, analysis_max_dim)
        rotated_mask_result = make_ink_mask_with_stats(rotated_analysis)
        rotated_bbox_small = content_bbox(rotated_mask_result.mask)
        detected_bbox = scale_bbox(rotated_bbox_small, 1.0 / rotated_scale)
        if "content_bbox" in config:
            detected_bbox = _as_bbox(config["content_bbox"], "content_bbox")
            flags.append("content_bbox_override")

        expanded = expand_bbox(detected_bbox, margin_x, margin_top, margin_bottom)
        if "crop_window" in config:
            crop_window = _as_bbox(config["crop_window"], "crop_window")
            flags.append("crop_window_override")
        else:
            crop_window = choose_fixed_window(expanded, target_w, target_h)

        if bbox_overflows(detected_bbox, target_size):
            flags.append("content_overflow")
        elif bbox_overflows(expanded, target_size):
            flags.append("expanded_margin_overflow")

        cropped = crop_with_padding(rotated, crop_window, pad_color=(255, 255, 255))
        padding = window_padding_px(crop_window, rotated.shape)
        debug_base = rotated
        debug_rejected_boxes = rotated_mask_result.stats.rejected_boxes

    out_h, out_w = cropped.shape[:2]
    if (out_w, out_h) != target_size:
        flags.append("non_target_output_size")

    color_path = out_dir / "color" / task.output_name
    gray_path = out_dir / "gray_for_ocr" / task.output_name
    sidecar_path = out_dir / "metadata" / f"{Path(task.output_name).stem}.json"
    debug_path = out_dir / "debug" / task.output_name

    imwrite_checked(color_path, cropped)
    gray_for_ocr = normalize_background(to_gray(cropped))
    imwrite_checked(gray_path, gray_for_ocr)

    hough_delta = None if angle_hough is None or angle_projection is None else abs(angle_projection - angle_hough)
    content_ratio = bbox_area(detected_bbox) / float(max(1, source_w * source_h))
    crop_margin = min_margin(detected_bbox, crop_window)
    if crop_margin < 20:
        flags.append("crop_near_content")
    if padding > 0:
        flags.append("padding_needed")

    metrics = PageMetrics(
        page_number=task.page_number,
        output_name=task.output_name,
        source_filename=task.source_filename,
        split=split_side,
        mode=mode,
        target_size=target_size,
        source_size=(source_w, source_h),
        output_size=(out_w, out_h),
        angle_projection=angle_projection,
        angle_hough=angle_hough,
        angle_line=angle_line,
        angle_used=angle_used,
        projection_peak_z=projection_peak_z,
        projection_second_gap=projection_second_gap,
        projection_hough_delta=hough_delta,
        hough_confidence=hough_confidence,
        line_confidence=line_confidence,
        line_segment_count=line_segment_count,
        foreground_component_count=rotated_mask_result.stats.kept_component_count,
        content_bbox=detected_bbox,
        expanded_bbox=expanded,
        crop_window=crop_window,
        trim_insets=trim_insets,
        page_side=None if side_info is None else side_info.page_side,
        inner_edge=None if side_info is None else side_info.inner_edge,
        outer_edge=None if side_info is None else side_info.outer_edge,
        book_page_number=None if side_info is None else side_info.book_page_number,
        reference_match_score=reference_match_score,
        scanner_tail_detected=tail_info.detected,
        scanner_tail_confidence=tail_info.confidence,
        content_area_ratio=content_ratio,
        min_crop_margin=crop_margin,
        padding_px=padding,
        flags=sorted(set(flags)),
    )

    sidecar = metrics_to_json(metrics)
    sidecar["paths"] = {
        "color": str(color_path),
        "gray_for_ocr": str(gray_path),
        "debug": str(debug_path) if debug else None,
    }
    write_json(sidecar_path, sidecar)

    if debug:
        label = (
            f"{task.page_number:03d} angle={angle_used:+.2f} "
            f"line={angle_line if angle_line is not None else 'n/a'} "
            f"flags={','.join(metrics.flags) or 'ok'}"
        )
        overlay = make_debug_overlay(
            debug_base,
            content_box=detected_bbox,
            crop_window=crop_window,
            rejected_boxes=debug_rejected_boxes,
            label=label,
        )
        imwrite_checked(debug_path, overlay)

    return metrics


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.jobs < 1:
        raise SystemExit("--jobs must be >= 1")

    target_size = parse_target_size(args.target)
    tasks = build_page_tasks(args.pdforder, args.manifest, scan_dir=args.scan_dir, target_size=target_size)
    requested_pages = parse_page_range(args.pages)
    tasks = selected_tasks(tasks, requested_pages)
    if not tasks:
        raise SystemExit("no pages selected")

    overrides = load_overrides(args.overrides)
    prepare_output_dir(args.out, args.scan_dir, force=args.force)
    metrics: list[PageMetrics] = []

    print(f"processing {len(tasks)} page(s) into {args.out}", file=sys.stderr)
    if args.jobs == 1:
        for task in tasks:
            print(f"  {task.page_number:03d} {task.output_name}", file=sys.stderr)
            metrics.append(process_task(task, args.out, overrides, debug=args.debug, reference_dir=args.reference_crops))
    else:
        with ThreadPoolExecutor(max_workers=args.jobs) as executor:
            future_to_task = {
                executor.submit(
                    process_task,
                    task,
                    args.out,
                    overrides,
                    debug=args.debug,
                    reference_dir=args.reference_crops,
                ): task
                for task in tasks
            }
            for future in as_completed(future_to_task):
                task = future_to_task[future]
                try:
                    metric = future.result()
                except Exception as exc:  # pragma: no cover - CLI error reporting.
                    raise RuntimeError(f"failed processing page {task.page_number:03d} {task.output_name}: {exc}") from exc
                print(f"  done {task.page_number:03d} {task.output_name}", file=sys.stderr)
                metrics.append(metric)

    metrics.sort(key=lambda item: item.page_number)
    write_metrics_jsonl(args.out / "metrics.jsonl", metrics)

    # Read back once to catch serialization mistakes before the caller validates.
    _ = read_metrics_jsonl(args.out / "metrics.jsonl")
    flagged = sum(1 for item in metrics if item.flags)
    print(f"wrote {len(metrics)} page(s); flagged {flagged}; metrics={args.out / 'metrics.jsonl'}", file=sys.stderr)
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
