#!/usr/bin/env python3
"""Shared helpers for the non-destructive scan post-processing pipeline."""

from __future__ import annotations

import csv
import copy
import json
import math
import re
from dataclasses import asdict, dataclass, field, is_dataclass
from pathlib import Path
from typing import Any, Iterable, Sequence

import cv2
import numpy as np

BBox = tuple[int, int, int, int]
Size = tuple[int, int]


DEFAULT_PROCESSING_OPTIONS: dict[str, Any] = {
    "analysis_max_dim": 1600,
    "deskew": True,
    "body_angle_range": 3.0,
    "front_angle_range": 1.5,
    "coarse_step": 0.10,
    "fine_step": 0.02,
    "body_margin_x": 95,
    "body_margin_top": 95,
    "body_margin_bottom": 135,
    "front_margin_x": 80,
    "front_margin_top": 80,
    "front_margin_bottom": 110,
    "hough_disagreement_threshold": 0.35,
    "low_projection_peak_z": 5.0,
    "suspicious_angle_degrees": 2.0,
    "reference_crop_strategy": "trim",
    "reference_rotate_margin": 180,
    "body_outer_trim_px": 36,
    "body_inner_trim_px": 52,
    "body_top_trim_px": 0,
    "body_bottom_trim_px": 72,
    "front_trim_px": 0,
    "line_projection_agreement_threshold": 0.25,
    "line_confidence_threshold": 2.0,
    "line_min_segments": 3,
    "scanner_tail_probe_px": 200,
    "scanner_tail_std_threshold": 8.0,
    "scanner_tail_dark_mean_threshold": 242.0,
    "scanner_bed_rgb_samples": ["#f6f6f4", "#f5f5f3", "#f4f4f2"],
    "paper_rgb_samples": ["#fbf8f1", "#faf9f5"],
}


@dataclass(frozen=True)
class PageSideInfo:
    book_page_number: int
    page_side: str
    inner_edge: str
    outer_edge: str


@dataclass(frozen=True)
class ScannerTailInfo:
    detected: bool
    confidence: float
    probe_rows: int
    bottom_row_std: float
    bottom_row_mean: float


@dataclass(frozen=True)
class PageTask:
    """One final output page to render from a raw scan."""

    page_number: int
    output_name: str
    source_filename: str
    source_path: Path
    split: str | None
    mode: str
    target_size: Size


@dataclass(frozen=True)
class MaskCleanupStats:
    kept_component_count: int
    rejected_component_count: int
    rejected_boxes: list[BBox] = field(default_factory=list)


@dataclass(frozen=True)
class MaskResult:
    mask: np.ndarray
    stats: MaskCleanupStats


@dataclass(frozen=True)
class PageMetrics:
    page_number: int
    output_name: str
    source_filename: str
    split: str | None
    mode: str
    target_size: Size
    source_size: Size
    output_size: Size
    angle_projection: float | None
    angle_hough: float | None
    angle_line: float | None
    angle_used: float
    projection_peak_z: float
    projection_second_gap: float
    projection_hough_delta: float | None
    hough_confidence: float
    line_confidence: float
    line_segment_count: int
    foreground_component_count: int
    content_bbox: BBox
    expanded_bbox: BBox
    crop_window: BBox
    trim_insets: BBox
    page_side: str | None
    inner_edge: str | None
    outer_edge: str | None
    book_page_number: int | None
    reference_match_score: float | None
    scanner_tail_detected: bool
    scanner_tail_confidence: float
    content_area_ratio: float
    min_crop_margin: int
    padding_px: int
    flags: list[str]


# ---------------------------------------------------------------------------
# Inventory and override parsing


def parse_pdforder(path: str | Path) -> list[str]:
    """Return canonical output filenames in dist/pdforder.txt order."""

    lines = Path(path).read_text(encoding="utf-8").splitlines()
    return [line.strip() for line in lines if line.strip()]


def _parse_pdf_page_numbers(page_range: str) -> list[int]:
    if "-" not in page_range:
        return [int(page_range)]
    start_s, end_s = page_range.split("-", 1)
    start = int(start_s)
    end = int(end_s)
    if end < start:
        raise ValueError(f"descending manifest page range: {page_range}")
    return list(range(start, end + 1))


def parse_manifest(path: str | Path) -> list[dict[str, Any]]:
    """Parse scan/pdforder-rename-manifest.tsv rows."""

    rows: list[dict[str, Any]] = []
    with Path(path).open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        required = {"pdf_page_range", "old_filename", "new_filename", "pdforder_entries"}
        fieldnames = set(reader.fieldnames or [])
        if not required <= fieldnames:
            missing = sorted(required - fieldnames)
            raise ValueError(f"manifest {path} is missing required columns: {missing}")
        for row in reader:
            entries = [entry.strip() for entry in row["pdforder_entries"].split(",") if entry.strip()]
            page_numbers = _parse_pdf_page_numbers(row["pdf_page_range"].strip())
            if len(entries) != len(page_numbers):
                raise ValueError(
                    "manifest row page count does not match pdforder_entries: "
                    f"{row['pdf_page_range']} -> {entries}"
                )
            rows.append(
                {
                    "pdf_page_range": row["pdf_page_range"].strip(),
                    "page_numbers": page_numbers,
                    "old_filename": row["old_filename"].strip(),
                    "new_filename": row["new_filename"].strip(),
                    "pdforder_entries": entries,
                }
            )
    return rows


def classify_page(page_number: int, output_name: str) -> str:
    """Return the default processing mode for a final page."""

    lowered = output_name.lower()
    if page_number == 1 or "cover" in lowered:
        return "cover"
    if page_number <= 6 or "tocpage" in lowered or "openpages" in lowered:
        return "front"
    return "body"


def _split_side_for_entry(entries: Sequence[str], index: int) -> str | None:
    if len(entries) == 1:
        return None
    name = entries[index].lower()
    if name.endswith("_left.png"):
        return "left"
    if name.endswith("_right.png"):
        return "right"
    if len(entries) == 2:
        return "left" if index == 0 else "right"
    raise ValueError(f"cannot infer split side for manifest entries: {entries}")


def build_page_tasks(
    pdforder: str | Path,
    manifest: str | Path,
    *,
    scan_dir: str | Path = "scan",
    target_size: Size = (1788, 2512),
    require_count: int | None = 274,
) -> list[PageTask]:
    """Expand pdforder/manifest into one PageTask per final PDF page."""

    order = parse_pdforder(pdforder)
    if require_count is not None and len(order) != require_count:
        raise ValueError(f"expected {require_count} pdforder entries, got {len(order)}")

    rows = parse_manifest(manifest)
    by_entry: dict[str, tuple[dict[str, Any], int]] = {}
    for row in rows:
        for index, entry in enumerate(row["pdforder_entries"]):
            if entry in by_entry:
                raise ValueError(f"duplicate pdforder entry in manifest: {entry}")
            by_entry[entry] = (row, index)

    scan_path = Path(scan_dir)
    tasks: list[PageTask] = []
    for page_number, output_name in enumerate(order, start=1):
        try:
            row, index = by_entry[output_name]
        except KeyError as exc:
            raise ValueError(f"pdforder entry missing from manifest: {output_name}") from exc

        row_page_number = row["page_numbers"][index]
        if row_page_number != page_number:
            raise ValueError(
                f"manifest/pdforder page mismatch for {output_name}: "
                f"manifest page {row_page_number:03d}, pdforder position {page_number:03d}"
            )

        split = _split_side_for_entry(row["pdforder_entries"], index)
        source_filename = row["new_filename"]
        tasks.append(
            PageTask(
                page_number=page_number,
                output_name=output_name,
                source_filename=source_filename,
                source_path=scan_path / source_filename,
                split=split,
                mode=classify_page(page_number, output_name),
                target_size=target_size,
            )
        )

    unused = set(by_entry) - set(order)
    if unused:
        raise ValueError(f"manifest contains entries not present in pdforder: {sorted(unused)[:5]}")
    return tasks


def parse_page_range(spec: str | None) -> list[int] | None:
    """Parse a comma separated page/range spec, preserving order and de-duplicating."""

    if spec is None or not spec.strip() or spec.strip().lower() == "all":
        return None
    pages: list[int] = []
    seen: set[int] = set()
    for part in spec.split(","):
        token = part.strip()
        if not token:
            continue
        if "-" in token:
            start_s, end_s = token.split("-", 1)
            start = int(start_s)
            end = int(end_s)
            if start <= 0 or end <= 0:
                raise ValueError(f"page numbers must be positive: {token}")
            if end < start:
                raise ValueError(f"descending page range is not allowed: {token}")
            values = range(start, end + 1)
        else:
            value = int(token)
            if value <= 0:
                raise ValueError(f"page numbers must be positive: {token}")
            values = [value]
        for value in values:
            if value not in seen:
                seen.add(value)
                pages.append(value)
    return pages or None


def parse_target_size(spec: str) -> Size:
    """Parse WIDTHxHEIGHT target canvas strings."""

    token = spec.lower().replace("×", "x")
    if "x" not in token:
        raise ValueError(f"target size must be WIDTHxHEIGHT, got {spec!r}")
    width_s, height_s = token.split("x", 1)
    width = int(width_s)
    height = int(height_s)
    if width <= 0 or height <= 0:
        raise ValueError(f"target dimensions must be positive, got {spec!r}")
    return (width, height)


def deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    """Recursively merge two JSON-like dictionaries."""

    result = copy.deepcopy(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = copy.deepcopy(value)
    return result


def load_overrides(path: str | Path | None) -> dict[str, Any]:
    """Load override JSON, returning defaults even when no file is supplied."""

    overrides: dict[str, Any] = {
        "defaults": copy.deepcopy(DEFAULT_PROCESSING_OPTIONS),
        "pages": {},
        "outputs": {},
    }
    if path is None:
        return overrides

    override_path = Path(path)
    with override_path.open("r", encoding="utf-8") as handle:
        loaded = json.load(handle)
    if not isinstance(loaded, dict):
        raise ValueError(f"override file must contain a JSON object: {override_path}")

    loaded = copy.deepcopy(loaded)
    if "defaults" in loaded:
        overrides["defaults"] = deep_merge(overrides["defaults"], loaded.pop("defaults"))
    if "pages" in loaded:
        pages = loaded.pop("pages")
        if not isinstance(pages, dict):
            raise ValueError("override 'pages' must be an object")
        overrides["pages"] = pages
    outputs: dict[str, Any] = {}
    for output_key in ("outputs", "output_names", "by_output"):
        if output_key in loaded:
            value = loaded.pop(output_key)
            if not isinstance(value, dict):
                raise ValueError(f"override '{output_key}' must be an object")
            outputs = deep_merge(outputs, value)
    overrides["outputs"] = outputs
    # Preserve any future top-level metadata keys without letting them affect processing.
    overrides["meta"] = loaded
    return overrides


def _page_override_candidates(page_number: int) -> list[str]:
    return [f"{page_number:03d}", str(page_number)]


def resolve_page_overrides(task: PageTask, overrides: dict[str, Any] | None) -> dict[str, Any]:
    """Resolve defaults, page overrides, then output-name overrides for a task."""

    if overrides is None:
        overrides = load_overrides(None)
    resolved = copy.deepcopy(overrides.get("defaults", {}))
    resolved.setdefault("mode", task.mode)
    resolved.setdefault("target_size", list(task.target_size))

    pages = overrides.get("pages", {}) or {}
    for key in _page_override_candidates(task.page_number):
        value = pages.get(key)
        if isinstance(value, dict):
            resolved = deep_merge(resolved, value)

    outputs = overrides.get("outputs", {}) or {}
    value = outputs.get(task.output_name)
    if isinstance(value, dict):
        resolved = deep_merge(resolved, value)
    return resolved


def selected_tasks(tasks: Sequence[PageTask], page_numbers: Sequence[int] | None) -> list[PageTask]:
    if page_numbers is None:
        return list(tasks)
    wanted = set(page_numbers)
    return [task for task in tasks if task.page_number in wanted]


_ORDERED_PAGE_RE = re.compile(r"both_sides_ordered-(\d+)\.png$")


def infer_page_side(task: PageTask, config: dict[str, Any] | None = None) -> PageSideInfo | None:
    """Infer left/right-hand page side and inner edge for body pages.

    For this book's final PDF order, even-numbered body pages are left-hand
    pages, so the inner/ragged binding edge is on the right.  Odd pages are
    right-hand pages, with their inner edge on the left.  Per-page overrides can
    force any of the returned values.
    """

    cfg = config or {}
    if str(cfg.get("mode", task.mode)) != "body":
        return None

    book_page_number = int(cfg.get("book_page_number", task.page_number))
    page_side = str(cfg.get("page_side", "left" if book_page_number % 2 == 0 else "right"))
    if page_side not in {"left", "right"}:
        raise ValueError(f"page_side must be 'left' or 'right', got {page_side!r}")

    inner_edge = str(cfg.get("inner_edge", "right" if page_side == "left" else "left"))
    if inner_edge not in {"left", "right"}:
        raise ValueError(f"inner_edge must be 'left' or 'right', got {inner_edge!r}")
    outer_edge = "left" if inner_edge == "right" else "right"
    outer_edge = str(cfg.get("outer_edge", outer_edge))
    if outer_edge not in {"left", "right"}:
        raise ValueError(f"outer_edge must be 'left' or 'right', got {outer_edge!r}")

    return PageSideInfo(
        book_page_number=book_page_number,
        page_side=page_side,
        inner_edge=inner_edge,
        outer_edge=outer_edge,
    )


def trim_insets_for_page(task: PageTask, config: dict[str, Any], side_info: PageSideInfo | None = None) -> BBox:
    """Return left/top/right/bottom trim insets for the final crop.

    Body pages are trimmed asymmetrically in inner/outer terms: the debound
    inner edge gets a slightly larger trim to hide ragged paper and shadows, but
    the left+right sum stays constant so all body pages share one output size.
    """

    if "trim_insets" in config:
        return tuple(int(v) for v in config["trim_insets"])  # type: ignore[return-value]

    mode = str(config.get("mode", task.mode))
    if mode != "body":
        front_trim = int(config.get("front_trim_px", 0))
        return (front_trim, front_trim, front_trim, front_trim)

    side = side_info or infer_page_side(task, config)
    outer = int(config.get("body_outer_trim_px", 36))
    inner = int(config.get("body_inner_trim_px", 52))
    top = int(config.get("body_top_trim_px", 0))
    bottom = int(config.get("body_bottom_trim_px", 72))
    if side is not None and side.inner_edge == "right":
        left, right = outer, inner
    else:
        left, right = inner, outer
    return (left, top, right, bottom)


def apply_trim_insets(window: BBox, insets: BBox) -> BBox:
    left, top, right, bottom = insets
    x0, y0, x1, y1 = window
    trimmed = (x0 + left, y0 + top, x1 - right, y1 - bottom)
    if trimmed[2] <= trimmed[0] or trimmed[3] <= trimmed[1]:
        raise ValueError(f"trim insets {insets} collapse crop window {window}")
    return trimmed


def _parse_rgb_sample(value: str | Sequence[int]) -> tuple[int, int, int]:
    if isinstance(value, str):
        token = value.strip().lstrip("#")
        if len(token) != 6:
            raise ValueError(f"RGB sample must be #rrggbb, got {value!r}")
        return (int(token[0:2], 16), int(token[2:4], 16), int(token[4:6], 16))
    if len(value) != 3:
        raise ValueError(f"RGB sample must have three channels, got {value!r}")
    return (int(value[0]), int(value[1]), int(value[2]))


def paper_bed_likelihood(img: np.ndarray, config: dict[str, Any]) -> np.ndarray:
    """Return positive values for paper-like pixels and negative for bed-like.

    The provided scanner-bed and paper samples are extremely close in RGB, so
    this is used as weak evidence for edge/tail diagnostics rather than a hard
    crop boundary by itself.
    """

    if img.ndim == 2:
        rgb = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    else:
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    bed = np.array([_parse_rgb_sample(v) for v in config.get("scanner_bed_rgb_samples", [])], dtype=np.uint8)
    paper = np.array([_parse_rgb_sample(v) for v in config.get("paper_rgb_samples", [])], dtype=np.uint8)
    if len(bed) == 0 or len(paper) == 0:
        return np.zeros(rgb.shape[:2], dtype=np.float32)

    lab_img = cv2.cvtColor(rgb, cv2.COLOR_RGB2LAB).astype(np.float32)
    bed_lab = cv2.cvtColor(bed.reshape(-1, 1, 3), cv2.COLOR_RGB2LAB).reshape(-1, 3).astype(np.float32)
    paper_lab = cv2.cvtColor(paper.reshape(-1, 1, 3), cv2.COLOR_RGB2LAB).reshape(-1, 3).astype(np.float32)
    bed_dist = np.min(np.linalg.norm(lab_img[:, :, None, :] - bed_lab[None, None, :, :], axis=3), axis=2)
    paper_dist = np.min(np.linalg.norm(lab_img[:, :, None, :] - paper_lab[None, None, :, :], axis=3), axis=2)
    return (bed_dist - paper_dist).astype(np.float32)


# ---------------------------------------------------------------------------
# OpenCV image helpers


def odd(n: int) -> int:
    return n if n % 2 else n + 1


def to_gray(img: np.ndarray) -> np.ndarray:
    if img.ndim == 2:
        return img
    if img.shape[2] == 4:
        return cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def resize_for_analysis(img: np.ndarray, max_dim: int = 1600) -> tuple[np.ndarray, float]:
    h, w = img.shape[:2]
    if max_dim <= 0:
        raise ValueError("analysis max dimension must be positive")
    scale = min(1.0, max_dim / float(max(h, w)))
    if scale >= 0.999:
        return img.copy(), 1.0
    out = cv2.resize(img, (round(w * scale), round(h * scale)), interpolation=cv2.INTER_AREA)
    return out, scale


def normalize_background(gray: np.ndarray) -> np.ndarray:
    gray = to_gray(gray)
    h, w = gray.shape[:2]
    max_kernel = min(h, w)
    if max_kernel < 3:
        return gray.copy()
    if max_kernel % 2 == 0:
        max_kernel -= 1
    kernel = odd(max(51, round(min(h, w) * 0.035)))
    kernel = min(kernel, max_kernel)
    if kernel < 3:
        return gray.copy()
    bg = cv2.medianBlur(gray, kernel)
    bg = np.maximum(bg, 1)
    norm = cv2.divide(gray, bg, scale=235)
    return np.clip(norm, 0, 255).astype(np.uint8)


def remove_bad_components_with_stats(mask: np.ndarray) -> MaskResult:
    """Remove tiny specks and large edge-touching scanner artifacts."""

    binary = ((mask > 0).astype(np.uint8)) * 255
    h, w = binary.shape[:2]
    count, labels, stats, _centroids = cv2.connectedComponentsWithStats(binary, connectivity=8)
    keep = np.zeros_like(binary)
    img_area = h * w
    kept = 0
    rejected = 0
    rejected_boxes: list[BBox] = []

    for label in range(1, count):
        x, y, bw, bh, area = [int(v) for v in stats[label]]
        if area < 6:
            rejected += 1
            rejected_boxes.append((x, y, x + bw, y + bh))
            continue

        touches_edge = x == 0 or y == 0 or x + bw >= w - 1 or y + bh >= h - 1
        huge = area > 0.08 * img_area
        very_wide = bw > 0.90 * w and bh > 0.04 * h
        very_tall = bh > 0.75 * h and bw > 0.04 * w
        density = area / float(max(1, bw * bh))
        low_density = density < 0.08
        border_artifact = touches_edge and (huge or very_wide or very_tall or low_density)

        # Many raw pages contain dark scanner/book-edge slivers that do not
        # quite touch the image border after cropping/rotation.  If kept, these
        # one-digit-pixel vertical components stretch the content bbox to the
        # bottom of the scan and cause the fixed crop window to select the wrong
        # half of the page.  Reject only extreme tall+narrow components; normal
        # tables still have surrounding text/horizontal rules and survive in the
        # aggregate mask.
        narrow = bw <= max(8, int(w * 0.015))
        tall = bh >= max(120, int(h * 0.18))
        tall_narrow_sliver = narrow and tall and density > 0.20
        edge_margin = max(6, int(min(w, h) * 0.01))
        near_outer_edge = x <= edge_margin or y <= edge_margin or x + bw >= w - edge_margin or y + bh >= h - edge_margin
        near_edge_small_artifact = near_outer_edge and area < max(100, int(img_area * 0.001))

        if border_artifact or tall_narrow_sliver or near_edge_small_artifact:
            rejected += 1
            rejected_boxes.append((x, y, x + bw, y + bh))
            continue

        keep[labels == label] = 255
        kept += 1

    return MaskResult(
        mask=keep,
        stats=MaskCleanupStats(
            kept_component_count=kept,
            rejected_component_count=rejected,
            rejected_boxes=rejected_boxes,
        ),
    )


def remove_bad_components(mask: np.ndarray) -> np.ndarray:
    return remove_bad_components_with_stats(mask).mask


def make_ink_mask_with_stats(img: np.ndarray) -> MaskResult:
    gray = to_gray(img)
    norm = normalize_background(gray)
    norm = cv2.GaussianBlur(norm, (3, 3), 0)

    _threshold, otsu = cv2.threshold(norm, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    block_size = min(51, min(norm.shape[:2]) // 2 * 2 - 1)
    mask = otsu
    # Adaptive thresholding is a fallback for very sparse/faint pages only.  On
    # these book scans it otherwise turns paper texture in blank lower scan
    # regions into foreground, which is much worse than missing a few faint
    # glyph pixels for geometry estimation.
    if block_size >= 3 and int((mask > 0).sum()) < max(100, int(mask.size * 0.001)):
        adaptive = cv2.adaptiveThreshold(
            norm,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY_INV,
            block_size,
            13,
        )
        adaptive = cv2.bitwise_and(adaptive, ((norm < 205).astype(np.uint8)) * 255)
        mask = cv2.bitwise_or(mask, adaptive)

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((2, 2), np.uint8))
    return remove_bad_components_with_stats(mask)


def make_ink_mask(img: np.ndarray) -> np.ndarray:
    return make_ink_mask_with_stats(img).mask


def rotate_mask(mask: np.ndarray, angle_deg: float) -> np.ndarray:
    h, w = mask.shape[:2]
    center = (w / 2.0, h / 2.0)
    matrix = cv2.getRotationMatrix2D(center, angle_deg, 1.0)
    return cv2.warpAffine(
        mask,
        matrix,
        (w, h),
        flags=cv2.INTER_NEAREST,
        borderMode=cv2.BORDER_CONSTANT,
        borderValue=0,
    )


def rotate_image(img: np.ndarray, angle_deg: float, pad_color: int | tuple[int, int, int] = (255, 255, 255)) -> np.ndarray:
    h, w = img.shape[:2]
    center = (w / 2.0, h / 2.0)
    matrix = cv2.getRotationMatrix2D(center, angle_deg, 1.0)
    if img.ndim == 2 and isinstance(pad_color, tuple):
        border_value: int | tuple[int, int, int] = int(pad_color[0])
    else:
        border_value = pad_color
    return cv2.warpAffine(
        img,
        matrix,
        (w, h),
        flags=cv2.INTER_CUBIC,
        borderMode=cv2.BORDER_CONSTANT,
        borderValue=border_value,
    )


def projection_score(mask: np.ndarray) -> float:
    proj = (mask > 0).sum(axis=1).astype(np.float32)
    ink = float(proj.sum())
    if ink < 100:
        return 0.0
    return float(np.var(proj) / (np.mean(proj) + 1.0))


def scan_angles(lo: float, hi: float, step: float) -> list[float]:
    if step <= 0:
        raise ValueError("angle step must be positive")
    count = int(round((hi - lo) / step)) + 1
    return [round(lo + i * step, 10) for i in range(max(0, count))]


def _peak_stats(scores: Sequence[tuple[float, float]]) -> tuple[float, float]:
    if not scores:
        return 0.0, 0.0
    values = np.array([score for _angle, score in scores], dtype=np.float64)
    best = float(values.max())
    median = float(np.median(values))
    mad = float(np.median(np.abs(values - median)))
    if mad > 1e-9:
        peak_z = (best - median) / (1.4826 * mad)
    else:
        std = float(values.std())
        peak_z = (best - median) / std if std > 1e-9 else 0.0
    sorted_values = np.sort(values)
    second_gap = float(best - sorted_values[-2]) if len(sorted_values) >= 2 else best
    return float(peak_z), second_gap


def estimate_skew_projection(
    mask: np.ndarray,
    max_angle: float = 3.0,
    *,
    coarse_step: float = 0.10,
    fine_step: float = 0.02,
) -> tuple[float, float, list[tuple[float, float]]]:
    """Estimate the correction angle that maximizes horizontal row projections."""

    if int((mask > 0).sum()) < 100:
        return 0.0, 0.0, []

    coarse_angles = scan_angles(-max_angle, max_angle, coarse_step)
    coarse_scores = [(angle, projection_score(rotate_mask(mask, angle))) for angle in coarse_angles]
    best_angle, _best_score = max(coarse_scores, key=lambda item: item[1])

    fine_lo = max(-max_angle, best_angle - max(0.20, coarse_step))
    fine_hi = min(max_angle, best_angle + max(0.20, coarse_step))
    fine_angles = scan_angles(fine_lo, fine_hi, fine_step)
    fine_scores = [(angle, projection_score(rotate_mask(mask, angle))) for angle in fine_angles]
    best_angle, _best_score = max(fine_scores, key=lambda item: item[1])
    peak_z, _second_gap = _peak_stats(fine_scores)
    return float(best_angle), float(peak_z), fine_scores


def weighted_median(values: np.ndarray, weights: np.ndarray) -> float:
    if len(values) == 0:
        raise ValueError("cannot compute weighted median of empty values")
    order = np.argsort(values)
    sorted_values = values[order]
    sorted_weights = weights[order]
    midpoint = float(sorted_weights.sum()) / 2.0
    cumulative = np.cumsum(sorted_weights)
    index = int(np.searchsorted(cumulative, midpoint, side="left"))
    return float(sorted_values[min(index, len(sorted_values) - 1)])


def estimate_skew_hough(mask: np.ndarray) -> tuple[float | None, float]:
    """Estimate correction angle via near-horizontal Hough line samples."""

    h, w = mask.shape[:2]
    if int((mask > 0).sum()) < 100:
        return None, 0.0

    kernel_width = max(25, w // 60)
    line_mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_CLOSE,
        cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_width, 3)),
    )
    edges = cv2.Canny(line_mask, 50, 150)
    lines = cv2.HoughLinesP(
        edges,
        rho=1,
        theta=np.pi / 180,
        threshold=max(40, w // 35),
        minLineLength=max(80, w // 8),
        maxLineGap=max(10, w // 100),
    )
    if lines is None:
        return None, 0.0

    angles: list[float] = []
    weights: list[float] = []
    for [[x1, y1, x2, y2]] in lines:
        dx = int(x2) - int(x1)
        dy = int(y2) - int(y1)
        length = math.hypot(dx, dy)
        if length < w * 0.08:
            continue
        observed_angle = math.degrees(math.atan2(dy, dx))
        if abs(observed_angle) <= 8.0:
            angles.append(observed_angle)
            weights.append(length)

    if len(angles) < 5:
        return None, 0.0

    angle_values = np.array(angles, dtype=np.float64)
    weight_values = np.array(weights, dtype=np.float64)
    observed = weighted_median(angle_values, weight_values)
    spread = float(np.percentile(angle_values, 75) - np.percentile(angle_values, 25))
    confidence = max(0.0, min(10.0, len(angles) / 5.0 - spread))
    # In image coordinates (y increasing downward), this observed angle is the
    # same signed correction accepted by rotate_image/rotate_mask.
    return float(observed), float(confidence)


def estimate_skew_line_segments(
    img: np.ndarray,
    max_angle: float = 3.0,
    *,
    min_segments: int = 3,
) -> tuple[float | None, float, int]:
    """Estimate deskew from long horizontal text/rule segments.

    Projection profiles are still useful for dense text, but Hough line segments
    are a better reader-facing signal when a page has long rules, table borders,
    or crisp text baselines.  The returned angle uses the same sign convention as
    rotate_image: pass it directly as the correction angle.
    """

    analysis = img
    gray = to_gray(analysis)
    mask_result = make_ink_mask_with_stats(gray)
    mask = mask_result.mask
    h, w = mask.shape[:2]
    if int((mask > 0).sum()) < 100:
        return None, 0.0, 0

    # Ignore the very top/bottom and extreme side strips.  These are where the
    # scan commonly has cut-off top margins, ragged debinding edges, and tail
    # stretch artifacts; text/rules in the central body carry the desired angle.
    roi = mask.copy()
    roi[: int(h * 0.03), :] = 0
    roi[int(h * 0.92) :, :] = 0
    roi[:, : int(w * 0.03)] = 0
    roi[:, int(w * 0.97) :] = 0

    close_width = max(25, w // 45)
    line_mask = cv2.morphologyEx(
        roi,
        cv2.MORPH_CLOSE,
        cv2.getStructuringElement(cv2.MORPH_RECT, (close_width, 2)),
    )
    line_mask = cv2.morphologyEx(
        line_mask,
        cv2.MORPH_OPEN,
        cv2.getStructuringElement(cv2.MORPH_RECT, (max(11, w // 100), 1)),
    )
    edges = cv2.Canny(line_mask, 50, 150)
    lines = cv2.HoughLinesP(
        edges,
        rho=1,
        theta=np.pi / 720,
        threshold=max(24, w // 55),
        minLineLength=max(60, w // 9),
        maxLineGap=max(8, w // 80),
    )
    if lines is None:
        return None, 0.0, 0

    angles: list[float] = []
    weights: list[float] = []
    for [[x1, y1, x2, y2]] in lines:
        dx = int(x2) - int(x1)
        dy = int(y2) - int(y1)
        length = math.hypot(dx, dy)
        if length < max(60, w * 0.08):
            continue
        observed_angle = math.degrees(math.atan2(dy, dx))
        if observed_angle > 90:
            observed_angle -= 180
        elif observed_angle < -90:
            observed_angle += 180
        if abs(observed_angle) <= max_angle:
            angles.append(observed_angle)
            weights.append(length)

    if len(angles) < min_segments:
        return None, 0.0, len(angles)

    angle_values = np.array(angles, dtype=np.float64)
    weight_values = np.array(weights, dtype=np.float64)
    observed = weighted_median(angle_values, weight_values)
    spread = float(np.percentile(angle_values, 75) - np.percentile(angle_values, 25))
    confidence = max(0.0, min(10.0, len(angles) / float(min_segments) - spread))
    return float(observed), float(confidence), len(angles)


def detect_scanner_tail(img: np.ndarray, config: dict[str, Any]) -> ScannerTailInfo:
    """Detect likely bottom scanner-tail stretch in an already-cropped page.

    The scanner artifact appears as repeated/stretched lower rows, often carrying
    a dark corner shadow.  We keep detection conservative and use trimming as the
    hard mitigation; this flag is for QA and for avoiding use of tail rows in
    geometry decisions.
    """

    gray = to_gray(img)
    h = gray.shape[0]
    probe_rows = min(h, int(config.get("scanner_tail_probe_px", 200)))
    if probe_rows < 10:
        return ScannerTailInfo(False, 0.0, probe_rows, 0.0, 255.0)
    probe = gray[h - probe_rows :, :]
    bottom = probe[-min(24, probe_rows) :, :]
    bottom_std = float(np.mean(np.std(bottom, axis=1)))
    bottom_mean = float(np.mean(bottom))
    std_threshold = float(config.get("scanner_tail_std_threshold", 8.0))
    dark_threshold = float(config.get("scanner_tail_dark_mean_threshold", 242.0))
    confidence = max(0.0, bottom_std / max(1e-6, std_threshold))
    if bottom_mean < dark_threshold:
        confidence += min(2.0, (dark_threshold - bottom_mean) / 20.0)
    detected = bottom_std >= std_threshold and bottom_mean < dark_threshold
    return ScannerTailInfo(detected, float(confidence), probe_rows, bottom_std, bottom_mean)


def content_bbox(mask: np.ndarray) -> BBox:
    h, w = mask.shape[:2]
    if int((mask > 0).sum()) == 0:
        return (0, 0, w, h)
    block = cv2.dilate(
        mask,
        cv2.getStructuringElement(cv2.MORPH_RECT, (max(21, w // 90), max(7, h // 350))),
        iterations=1,
    )
    ys, xs = np.where(block > 0)
    if len(xs) == 0:
        return (0, 0, w, h)

    # A few sparse specks or faint page-edge pixels can otherwise stretch the
    # union bbox to the full scan. Trim by row/column projection density while
    # keeping page numbers/captions, then fall back to the raw union if the page
    # is genuinely too sparse for projection trimming.
    row_counts = (block > 0).sum(axis=1)
    col_counts = (block > 0).sum(axis=0)
    row_threshold = max(5, int(w * 0.01))
    col_threshold = max(5, int(h * 0.005))
    dense_rows = np.where(row_counts >= row_threshold)[0]
    dense_cols = np.where(col_counts >= col_threshold)[0]
    if len(dense_rows) > 0 and len(dense_cols) > 0:
        return (
            int(dense_cols.min()),
            int(dense_rows.min()),
            int(dense_cols.max()) + 1,
            int(dense_rows.max()) + 1,
        )

    return (int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1)


def scale_bbox(bbox: BBox, scale: float) -> BBox:
    x0, y0, x1, y1 = bbox
    return (round(x0 * scale), round(y0 * scale), round(x1 * scale), round(y1 * scale))


def expand_bbox(bbox: BBox, margin_x: int, margin_y_top: int, margin_y_bottom: int) -> BBox:
    x0, y0, x1, y1 = bbox
    return (x0 - margin_x, y0 - margin_y_top, x1 + margin_x, y1 + margin_y_bottom)


def choose_fixed_window(expanded_bbox: BBox, target_w: int, target_h: int) -> BBox:
    """Choose a fixed-size crop window that contains the bbox when possible.

    If the desired bbox is larger than the target in one axis, no fixed window
    can contain it.  In that case keep the centered window for that axis instead
    of applying contradictory left/top then right/bottom shifts; otherwise a
    single long artifact can force the crop to the bottom/right of the scan.
    """

    x0, y0, x1, y1 = expanded_bbox
    cx = (x0 + x1) / 2.0
    cy = (y0 + y1) / 2.0

    left = round(cx - target_w / 2.0)
    top = round(cy - target_h / 2.0)

    if (x1 - x0) <= target_w:
        if left > x0:
            left = x0
        if left + target_w < x1:
            left = x1 - target_w

    if (y1 - y0) <= target_h:
        if top > y0:
            top = y0
        if top + target_h < y1:
            top = y1 - target_h

    return (int(left), int(top), int(left + target_w), int(top + target_h))


def crop_with_padding(
    img: np.ndarray,
    window: BBox,
    pad_color: int | tuple[int, int, int] = (255, 255, 255),
) -> np.ndarray:
    h, w = img.shape[:2]
    x0, y0, x1, y1 = [int(v) for v in window]
    out_w = x1 - x0
    out_h = y1 - y0
    if out_w <= 0 or out_h <= 0:
        raise ValueError(f"crop window must have positive size: {window}")

    if img.ndim == 2:
        fill = int(pad_color[0] if isinstance(pad_color, tuple) else pad_color)
        out = np.full((out_h, out_w), fill, dtype=img.dtype)
    else:
        fill_tuple = pad_color if isinstance(pad_color, tuple) else (pad_color,) * img.shape[2]
        out = np.full((out_h, out_w, img.shape[2]), fill_tuple, dtype=img.dtype)

    sx0 = max(0, x0)
    sy0 = max(0, y0)
    sx1 = min(w, x1)
    sy1 = min(h, y1)
    if sx1 <= sx0 or sy1 <= sy0:
        return out

    dx0 = sx0 - x0
    dy0 = sy0 - y0
    out[dy0 : dy0 + (sy1 - sy0), dx0 : dx0 + (sx1 - sx0)] = img[sy0:sy1, sx0:sx1]
    return out


def apply_split(img: np.ndarray, split: str | None, options: dict[str, Any] | None = None) -> np.ndarray:
    """Split a landscape scan into left/right page images."""

    if split is None:
        return img.copy()
    if split not in {"left", "right"}:
        raise ValueError(f"split must be 'left', 'right', or null, got {split!r}")
    opts = options or {}
    h, w = img.shape[:2]
    split_x = int(opts.get("split_x", w // 2))
    overlap = int(opts.get("overlap", 0))
    gutter = int(opts.get("gutter", 0))
    left_end = max(1, min(w, split_x - gutter // 2 + overlap))
    right_start = max(0, min(w - 1, split_x + gutter // 2 - overlap))
    if split == "left":
        return img[:, :left_end].copy()
    return img[:, right_start:].copy()


def bbox_area(bbox: BBox) -> int:
    x0, y0, x1, y1 = bbox
    return max(0, x1 - x0) * max(0, y1 - y0)


def min_margin(inner: BBox, outer: BBox) -> int:
    ix0, iy0, ix1, iy1 = inner
    ox0, oy0, ox1, oy1 = outer
    return int(min(ix0 - ox0, iy0 - oy0, ox1 - ix1, oy1 - iy1))


def window_padding_px(window: BBox, image_shape: Sequence[int]) -> int:
    h, w = int(image_shape[0]), int(image_shape[1])
    x0, y0, x1, y1 = window
    return int(max(0, -x0) + max(0, -y0) + max(0, x1 - w) + max(0, y1 - h))


def bbox_overflows(bbox: BBox, target_size: Size) -> bool:
    target_w, target_h = target_size
    x0, y0, x1, y1 = bbox
    return (x1 - x0) > target_w or (y1 - y0) > target_h


def _scaled_rect(bbox: BBox, scale: float) -> tuple[int, int, int, int]:
    x0, y0, x1, y1 = bbox
    return (round(x0 * scale), round(y0 * scale), round(x1 * scale), round(y1 * scale))


def make_debug_overlay(
    img: np.ndarray,
    *,
    content_box: BBox,
    crop_window: BBox,
    rejected_boxes: Sequence[BBox] = (),
    label: str = "",
    max_dim: int = 1600,
) -> np.ndarray:
    """Draw content/crop boxes on a downscaled copy for QA."""

    if img.ndim == 2:
        canvas = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    else:
        canvas = img.copy()
    h, w = canvas.shape[:2]
    scale = min(1.0, max_dim / float(max(h, w)))
    if scale < 0.999:
        canvas = cv2.resize(canvas, (round(w * scale), round(h * scale)), interpolation=cv2.INTER_AREA)
    for rejected in rejected_boxes[:50]:
        cv2.rectangle(canvas, _scaled_rect(rejected, scale)[:2], _scaled_rect(rejected, scale)[2:], (0, 0, 255), 1)
    cv2.rectangle(canvas, _scaled_rect(content_box, scale)[:2], _scaled_rect(content_box, scale)[2:], (0, 180, 0), 3)
    cv2.rectangle(canvas, _scaled_rect(crop_window, scale)[:2], _scaled_rect(crop_window, scale)[2:], (255, 0, 0), 3)
    if label:
        text = label[:180]
        cv2.rectangle(canvas, (0, 0), (canvas.shape[1], 36), (255, 255, 255), -1)
        cv2.putText(canvas, text, (8, 24), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2, cv2.LINE_AA)
    return canvas


# ---------------------------------------------------------------------------
# Serialization helpers


def jsonable(value: Any) -> Any:
    if is_dataclass(value):
        return jsonable(asdict(value))
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, dict):
        return {str(key): jsonable(item) for key, item in value.items()}
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        return float(value)
    if isinstance(value, np.ndarray):
        return value.tolist()
    return value


def metrics_to_json(metrics: PageMetrics) -> dict[str, Any]:
    return jsonable(metrics)


def write_json(path: str | Path, value: Any) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(jsonable(value), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_metrics_jsonl(path: str | Path, metrics: Iterable[PageMetrics | dict[str, Any]]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for item in metrics:
            handle.write(json.dumps(jsonable(item), ensure_ascii=False, sort_keys=True) + "\n")


def read_metrics_jsonl(path: str | Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with Path(path).open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                record = json.loads(stripped)
            except json.JSONDecodeError as exc:
                raise ValueError(f"invalid metrics JSON on line {line_number}: {exc}") from exc
            if not isinstance(record, dict):
                raise ValueError(f"metrics line {line_number} is not an object")
            records.append(record)
    return records


def imread_color(path: str | Path) -> np.ndarray:
    img = cv2.imread(str(path), cv2.IMREAD_COLOR)
    if img is None:
        raise FileNotFoundError(f"cannot read image: {path}")
    return img


def locate_reference_crop_window(
    source_img: np.ndarray,
    reference_img: np.ndarray,
    *,
    max_dim: int = 1200,
) -> tuple[BBox, float]:
    """Locate an existing cropped reference image inside a source scan.

    The repository already contains legacy cropped pages in `dist/`.  They are a
    strong prior for page size and approximate placement, even when we later
    deskew.  Template matching on a downscaled grayscale copy recovers that crop
    rectangle for special front-matter pages whose dimensions differ from the
    body-page crop.
    """

    src_h, src_w = source_img.shape[:2]
    ref_h, ref_w = reference_img.shape[:2]
    if ref_w <= 0 or ref_h <= 0:
        raise ValueError("reference image has invalid dimensions")
    if ref_w == src_w and ref_h == src_h:
        return (0, 0, src_w, src_h), 1.0
    if ref_w > src_w or ref_h > src_h:
        # A split or prior mismatch can make direct matching impossible.  Keep a
        # centered best-effort crop and flag via the low score.
        left = round((src_w - ref_w) / 2)
        top = round((src_h - ref_h) / 2)
        return (left, top, left + ref_w, top + ref_h), 0.0

    scale = min(1.0, max_dim / float(max(src_h, src_w)))
    src_gray = to_gray(source_img)
    ref_gray = to_gray(reference_img)
    if scale < 0.999:
        src_small = cv2.resize(src_gray, (round(src_w * scale), round(src_h * scale)), interpolation=cv2.INTER_AREA)
        ref_small = cv2.resize(ref_gray, (round(ref_w * scale), round(ref_h * scale)), interpolation=cv2.INTER_AREA)
    else:
        src_small = src_gray
        ref_small = ref_gray

    if ref_small.shape[0] > src_small.shape[0] or ref_small.shape[1] > src_small.shape[1]:
        left = round((src_w - ref_w) / 2)
        top = round((src_h - ref_h) / 2)
        return (left, top, left + ref_w, top + ref_h), 0.0

    result = cv2.matchTemplate(src_small, ref_small, cv2.TM_CCOEFF_NORMED)
    _min_val, max_val, _min_loc, max_loc = cv2.minMaxLoc(result)
    left = round(max_loc[0] / scale)
    top = round(max_loc[1] / scale)
    return (left, top, left + ref_w, top + ref_h), float(max_val)


def imwrite_checked(path: str | Path, img: np.ndarray) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not cv2.imwrite(str(path), img):
        raise OSError(f"failed to write image: {path}")
