from __future__ import annotations

import json
from pathlib import Path

import cv2
import numpy as np

from scripts.process_scans import prepare_output_dir
from scripts.scan_pipeline_common import (
    PageTask,
    apply_trim_insets,
    build_page_tasks,
    choose_fixed_window,
    crop_with_padding,
    detect_scanner_tail,
    estimate_skew_line_segments,
    estimate_skew_projection,
    infer_page_side,
    load_overrides,
    paper_bed_likelihood,
    parse_manifest,
    remove_bad_components_with_stats,
    parse_page_range,
    resolve_page_overrides,
    rotate_mask,
    trim_insets_for_page,
)


ROOT = Path(__file__).resolve().parents[1]


def test_build_page_tasks_expands_pdforder_and_split_mapping() -> None:
    tasks = build_page_tasks(
        ROOT / "dist/pdforder.txt",
        ROOT / "scan/pdforder-rename-manifest.tsv",
        scan_dir=ROOT / "scan",
        target_size=(1788, 2512),
    )

    assert len(tasks) == 274
    assert [task.page_number for task in tasks[:4]] == [1, 2, 3, 4]
    assert tasks[0].output_name == "cropped_nethack_uncropped_cover.png"
    assert tasks[1].source_filename == "pdf002-003__nethack_uncropped_openpages_1_2_3-1.png"
    assert tasks[2].source_filename == tasks[1].source_filename
    assert tasks[1].split == "left"
    assert tasks[2].split == "right"
    assert tasks[1].output_name.endswith("_left.png")
    assert tasks[2].output_name.endswith("_right.png")
    assert tasks[-1].page_number == 274


def test_parse_manifest_reports_missing_required_columns_even_with_extra_columns(tmp_path: Path) -> None:
    manifest = tmp_path / "manifest.tsv"
    manifest.write_text(
        "pdf_page_range\told_filename\textra\tpdforder_entries\n"
        "001\traw.png\tignored\tcropped_raw.png\n",
        encoding="utf-8",
    )

    try:
        parse_manifest(manifest)
    except ValueError as exc:
        assert "new_filename" in str(exc)
    else:  # pragma: no cover - defensive
        raise AssertionError("manifest missing required columns must fail")


def test_prepare_output_dir_refuses_force_delete_outside_generated_work_dirs(tmp_path: Path) -> None:
    out_dir = tmp_path / "important"
    out_dir.mkdir()
    (out_dir / "keep.txt").write_text("do not delete", encoding="utf-8")

    try:
        prepare_output_dir(out_dir, tmp_path / "scan", force=True)
    except SystemExit as exc:
        assert "refusing --force deletion" in str(exc)
    else:  # pragma: no cover - defensive
        raise AssertionError("--force must not delete arbitrary directories")

    assert (out_dir / "keep.txt").exists()


def test_parse_page_range_preserves_order_and_rejects_bad_ranges() -> None:
    assert parse_page_range("001-003,003,050,100,274") == [1, 2, 3, 50, 100, 274]
    assert parse_page_range(None) is None
    assert parse_page_range("") is None

    try:
        parse_page_range("011-001")
    except ValueError as exc:
        assert "descending" in str(exc)
    else:  # pragma: no cover - defensive
        raise AssertionError("descending ranges must fail")


def test_choose_fixed_window_keeps_expanded_content_inside() -> None:
    window = choose_fixed_window((100, 150, 350, 550), target_w=400, target_h=600)
    x0, y0, x1, y1 = window

    assert (x1 - x0, y1 - y0) == (400, 600)
    assert x0 <= 100
    assert y0 <= 150
    assert x1 >= 350
    assert y1 >= 550


def test_choose_fixed_window_centers_bbox_that_is_too_large() -> None:
    window = choose_fixed_window((100, 50, 300, 850), target_w=120, target_h=400)

    assert (window[2] - window[0], window[3] - window[1]) == (120, 400)
    # The bbox is too tall to contain.  Keep a centered vertical crop rather
    # than snapping to the bottom edge and losing the top of the page.
    assert abs(((window[1] + window[3]) / 2) - 450) <= 1


def test_remove_bad_components_rejects_tall_narrow_scan_slivers() -> None:
    mask = np.zeros((800, 500), dtype=np.uint8)
    cv2.line(mask, (450, 250), (450, 799), 255, 3)
    cv2.rectangle(mask, (120, 120), (300, 180), 255, -1)

    result = remove_bad_components_with_stats(mask)

    assert result.stats.rejected_component_count >= 1
    assert result.mask[:, 448:453].sum() == 0
    assert result.mask[130:170, 130:290].sum() > 0


def test_crop_with_padding_returns_fixed_size_and_white_border() -> None:
    img = np.zeros((4, 5, 3), dtype=np.uint8)
    img[:, :] = (10, 20, 30)

    cropped = crop_with_padding(img, (-2, -1, 5, 5), pad_color=(255, 255, 255))

    assert cropped.shape == (6, 7, 3)
    assert cropped[0, 0].tolist() == [255, 255, 255]
    assert cropped[1, 2].tolist() == [10, 20, 30]


def test_projection_deskew_estimates_correction_angle_on_synthetic_lines() -> None:
    mask = np.zeros((700, 900), dtype=np.uint8)
    for y in range(120, 600, 48):
        cv2.line(mask, (120, y), (780, y), 255, 3)

    skewed = rotate_mask(mask, 1.2)
    angle, peak_z, _scores = estimate_skew_projection(skewed, max_angle=2.0, coarse_step=0.2, fine_step=0.05)

    assert abs(angle + 1.2) <= 0.2
    assert peak_z > 1.0


def test_line_segment_deskew_uses_rotate_image_sign_convention() -> None:
    img = np.full((700, 900), 255, dtype=np.uint8)
    for y in range(120, 600, 48):
        cv2.line(img, (120, y), (780, y), 0, 3)
    matrix = cv2.getRotationMatrix2D((450, 350), 1.0, 1.0)
    skewed = cv2.warpAffine(img, matrix, (900, 700), borderMode=cv2.BORDER_CONSTANT, borderValue=255)

    angle, confidence, count = estimate_skew_line_segments(skewed, max_angle=2.0, min_segments=3)

    assert angle is not None
    assert abs(angle + 1.0) <= 0.2
    assert confidence > 0
    assert count >= 3


def test_body_page_side_and_trim_insets_are_inner_outer_aware() -> None:
    even_task = PageTask(160, "cropped_nethack_uncropped_both_sides_ordered-154.png", "raw.png", Path("raw.png"), None, "body", (1788, 2512))
    odd_task = PageTask(159, "cropped_nethack_uncropped_both_sides_ordered-153.png", "raw.png", Path("raw.png"), None, "body", (1788, 2512))
    config = load_overrides(None)["defaults"]

    even_side = infer_page_side(even_task, config)
    odd_side = infer_page_side(odd_task, config)

    assert even_side is not None
    assert odd_side is not None
    assert even_side.page_side == "left"
    assert even_side.inner_edge == "right"
    assert odd_side.page_side == "right"
    assert odd_side.inner_edge == "left"
    assert trim_insets_for_page(even_task, config, even_side) == (36, 0, 52, 72)
    assert trim_insets_for_page(odd_task, config, odd_side) == (52, 0, 36, 72)
    assert apply_trim_insets((378, 0, 2166, 2512), (36, 0, 52, 72)) == (414, 0, 2114, 2440)


def test_paper_bed_likelihood_prefers_supplied_paper_samples() -> None:
    img = np.array([[[0xF4, 0xF4, 0xF2], [0xFB, 0xF8, 0xF1]]], dtype=np.uint8)
    # OpenCV images are BGR.
    img = img[:, :, ::-1].copy()
    likelihood = paper_bed_likelihood(img, load_overrides(None)["defaults"])

    assert likelihood[0, 0] < 0
    assert likelihood[0, 1] > 0


def test_scanner_tail_detector_flags_repeated_dark_corner_shadow() -> None:
    img = np.full((260, 300, 3), 246, dtype=np.uint8)
    for row in range(230, 260):
        cv2.line(img, (10, row), (110, row), (160, 160, 160), 2)

    info = detect_scanner_tail(img, load_overrides(None)["defaults"])

    assert info.detected
    assert info.confidence > 1.0


def test_override_precedence_defaults_page_then_output_name(tmp_path: Path) -> None:
    override_path = tmp_path / "overrides.json"
    override_path.write_text(
        json.dumps(
            {
                "defaults": {"deskew": True, "body_margin_x": 90, "note": "default"},
                "pages": {"007": {"deskew": False, "body_margin_x": 100}},
                "outputs": {"page-007.png": {"body_margin_x": 120, "note": "output"}},
            }
        ),
        encoding="utf-8",
    )
    task = PageTask(
        page_number=7,
        output_name="page-007.png",
        source_filename="raw.png",
        source_path=Path("raw.png"),
        split=None,
        mode="body",
        target_size=(1788, 2512),
    )

    overrides = load_overrides(override_path)
    resolved = resolve_page_overrides(task, overrides)

    assert resolved["deskew"] is False
    assert resolved["body_margin_x"] == 120
    assert resolved["note"] == "output"
