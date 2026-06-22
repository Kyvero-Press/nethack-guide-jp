# Block-level translated hybrid PDF

This directory documents the block-level translated facsimile pass for the Japanese NetHack guidebook.

## Output PDF

- `dist/pdf/nethack-guide-qwen2_5_7b-block-hybrid.pdf`

This supersedes the older page-level facsimile prototype for layout review.

## Strategy

- Source page order: `dist/pdforder.txt`.
- Source images: `dist/crops/refined/`.
- Source OCR/layout blocks: `work/translation/source/blocks-surya.jsonl`, generated from `dist/metadata/ocr-bakeoff/surya-full/results.json`.
- Translation model: local `Qwen/Qwen2.5-7B-Instruct` served through vLLM/OpenAI-compatible API.
- Join key: `block_id` + `source_sha256` from the Surya block source.
- Cleaned page backgrounds are derived under `work/translation-pdf-hybrid/backgrounds/cleaned/`; original refined crops are not modified.
- Manual render overrides are in `config/translation-render-overrides.yaml`.
- Manual translation patches are in `config/block-translation-patches.yaml`.

## Important files

- `generation-writeup.md` — end-to-end writeup of how the block-hybrid translated PDF was generated from the original scans.
- `source-manifest.json` — reproducibility manifest for block source, pdforder, and block counts.
- `cleaned-backgrounds-summary.json` — full cleaned-background generation summary.
- `full-fit-report.jsonl` — machine-readable per-block render fit/status report.
- `fit-report.md` — human-readable fit summary.
- `previews/` — sample block-hybrid previews.
- `previews-full/` — selected previews rendered from the full PDF.

Block translation artifacts:

- `dist/text/translation-local/qwen2_5_7b_instruct/blocks/translation-records.raw.jsonl`
- `dist/text/translation-local/qwen2_5_7b_instruct/blocks/translation-records.retry.jsonl`
- `dist/text/translation-local/qwen2_5_7b_instruct/blocks/translation-records.jsonl`
- `dist/text/translation-local/qwen2_5_7b_instruct/blocks/validation-report.json`
- `dist/text/translation-local/qwen2_5_7b_instruct/blocks/patch-report.json`
- `dist/text/translation-local/qwen2_5_7b_instruct/blocks/nethack-guide-qwen2_5_7b-block-hybrid-pdftotext.txt`

## Validation summary

- Block source records: 3,809 text/layout blocks across 273 pages; page 272 has no text block.
- Final block translations: 3,809/3,809 records.
- Final translation validation: zero hard issues, zero soft issues.
- Final English-only/glyph validation: zero CJK leakage and zero unsupported characters for the embedded DejaVu Sans Condensed font.
- Manual translation patches: 142 guarded block patches, including English-only cleanup for CJK leakage, placeholder artifacts, unsupported punctuation, and post-font-change fit fixes.
- Full block-hybrid PDF: 274 pages.
- Final fit report: zero missing translations and zero overflow rows.
- Render statuses: `preserve_original=21`, `fitted=2619`, `shrunk=1169`.

## Known limitations

- This is still a machine-translated facsimile prototype, not a hand-typeset English edition.
- The cover/title-art pages are conservatively preserved rather than fully redesigned in English.
- Some blocks use very small text to fit English into Japanese-sized OCR boxes.
- Dense tables, item labels, and OCR-garbled prose should receive human review using `full-fit-report.jsonl` and preview PNGs.
