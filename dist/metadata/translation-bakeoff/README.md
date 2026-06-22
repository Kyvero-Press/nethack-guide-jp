# Local translation bakeoff

This directory records local Japanese-to-English translation experiments for the Japanese NetHack guidebook.

Source OCR: Surya (`dist/text/surya/`).

## Results

- `model-research.md` — model candidates and selection rationale.
- `results.md` — 10-page local model bakeoff summary.
- `samples/` — sample JSONL translations for tested local models:
  - `qwen2_5_3b_instruct.jsonl`
  - `qwen2_5_7b_instruct.jsonl`
  - `qwen3_4b_instruct_2507.jsonl`

Selected full-book model: `Qwen/Qwen2.5-7B-Instruct`.

Full-book translation output:

- `dist/text/translation-local/qwen2_5_7b_instruct/`

PDF review/prototype outputs:

- `dist/pdf/nethack-guide-qwen2_5_7b-translation-review.pdf`
- `dist/pdf/nethack-guide-qwen2_5_7b-block-hybrid.pdf`
- `dist/pdf/nethack-guide-qwen2_5_7b-translated-prototype.pdf` (older page-level smoke test)

## Block-level hybrid update

The layout-preserving translated facsimile was rerun with validated block-level translations keyed to Surya `block_id` + `source_sha256`, cleaned derived backgrounds, fit reports, and manual overrides for cover/artistic text. See:

- `dist/metadata/translation-block-hybrid/`
- `dist/text/translation-local/qwen2_5_7b_instruct/blocks/`
