from __future__ import annotations

from pathlib import Path

from PIL import Image

from scripts.make_cleaned_page_backgrounds import clean_page
from scripts.translated_pdf_common import BlockSource, RenderOverride


def test_clean_page_masks_auto_and_preserves_override(tmp_path: Path) -> None:
    image_path = tmp_path / "page.png"
    image = Image.new("RGB", (80, 80), (250, 250, 240))
    image.putpixel((20, 20), (0, 0, 0))
    image.save(image_path)
    blocks = [
        BlockSource(1, "001", "page.png", "001__page", "001-000", 0, "Text", (10, 10, 40, 40), "こんにちは", "a"),
        BlockSource(1, "001", "page.png", "001__page", "001-001", 1, "Text", (45, 10, 70, 40), "NetHack", "b"),
    ]
    out = tmp_path / "out.png"
    summary = clean_page(image_path, out, None, blocks, {"001-001": RenderOverride(action="preserve_original")})
    assert out.exists()
    assert summary["masked_blocks"] == ["001-000"]
    assert summary["preserved_blocks"] == ["001-001"]
