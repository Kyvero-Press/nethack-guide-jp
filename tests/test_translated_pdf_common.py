from __future__ import annotations

from scripts.translated_pdf_common import choose_fitting_font_size, px_bbox_to_pt_box, register_font


def test_px_bbox_to_pt_box_uses_top_left_pixel_origin() -> None:
    x, y, w, h = px_bbox_to_pt_box((10, 20, 110, 220), page_height_pt=500, scale=0.5)
    assert (x, y, w, h) == (5, 390, 50, 100)


def test_choose_fitting_font_size_reports_overflow_for_tiny_box() -> None:
    font = register_font(None, name="TestTranslatedPdfFont")
    size, remaining = choose_fitting_font_size("one two three four five six seven", 20, 5, font, 4, 8)
    assert size >= 4
    assert remaining > 0
