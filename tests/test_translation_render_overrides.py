from __future__ import annotations

from pathlib import Path

import pytest

from scripts.translated_pdf_common import BlockSource, load_render_overrides


def block() -> BlockSource:
    return BlockSource(
        page=1,
        page_label="001",
        source_image="p.png",
        source_key="001__p",
        block_id="001-000",
        reading_order=0,
        label="Text",
        bbox=(1, 2, 30, 40),
        source_text="こんにちは",
        source_sha256="abc",
    )


def test_override_loader_validates_known_block_and_guard(tmp_path: Path) -> None:
    path = tmp_path / "overrides.yaml"
    path.write_text('blocks:\n  "001-000": { action: manual_text, source_sha256: "abc", manual_text: "Hello" }\n', encoding="utf-8")
    overrides = load_render_overrides(path, [block()])
    assert overrides["001-000"].action == "manual_text"
    assert overrides["001-000"].manual_text == "Hello"


def test_override_loader_rejects_unknown_action(tmp_path: Path) -> None:
    path = tmp_path / "overrides.yaml"
    path.write_text('blocks:\n  "001-000": { action: explode }\n', encoding="utf-8")
    with pytest.raises(ValueError):
        load_render_overrides(path, [block()])
