# Translation review PDF metadata

This directory documents the side-by-side review PDFs for the local English machine translation.

## Output PDFs

- `dist/pdf/nethack-guide-qwen2_5_7b-translation-review-sample.pdf`
- `dist/pdf/nethack-guide-qwen2_5_7b-translation-review.pdf`

## Rendering strategy

`make_translation_review_pdf.py` creates an A4-landscape review artifact:

- left side: refined original page image;
- right side: page-level local English translation;
- continuation pages are added instead of truncating long translations.

This is the preferred artifact for human evaluation of translation quality because it keeps the original page visible next to the generated English.

## Files

- `sample-summary.json` — sample review PDF summary.
- `full-summary.json` — full review PDF summary.
- `previews/` — selected rendered sample pages.

## Validation summary

The full review PDF covers 274 source pages and renders to 276 PDF pages. Source pages 181 and 188 required continuation pages.
