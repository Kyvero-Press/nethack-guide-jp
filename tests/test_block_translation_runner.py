from __future__ import annotations

from scripts.run_local_translation import make_prompt, should_passthrough


def test_block_prompt_includes_block_metadata() -> None:
    row = {
        "record_type": "block",
        "page_label": "050",
        "source_image": "page.png",
        "block_id": "050-001",
        "reading_order": 1,
        "label": "Text",
        "bbox": [1, 2, 3, 4],
        "source_text": "読む",
    }
    prompt = make_prompt("Translate.", "glossary", row)
    assert "block_id=050-001" in prompt
    assert "bbox=[1, 2, 3, 4]" in prompt
    assert "読む" in prompt


def test_passthrough_non_cjk_only_when_enabled() -> None:
    assert should_passthrough({"source_text": "NetHack"}, True)
    assert not should_passthrough({"source_text": "読む"}, True)
    assert not should_passthrough({"source_text": "NetHack"}, False)
