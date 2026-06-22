# Translated PDF prototype metadata

This directory documents the first full-book translated facsimile prototype.

## Output PDF

- `dist/pdf/nethack-guide-qwen2_5_7b-translated-prototype.pdf`

## Rendering strategy

`make_translated_pdf_prototype.py` uses a smoke-test hybrid approach:

1. draw each refined crop as the page background;
2. cover Surya-detected text regions with white rectangles;
3. flow page-level English translation through those text boxes;
4. leave picture/image regions untouched.

This preserves original page appearance and images, but it is **not final typography**. Page-level text is not the right granularity for a professional layout-preserving translation.

## Files

- `sample-summary.json` — 12-page sample fit/overflow summary.
- `full-summary.json` — full-book fit/overflow summary.
- `oracle-recommendations.md` — Oracle/GPT Pro recommendations for the next reconstruction iteration.
- `previews/` — sample rendered page previews and local UI analyzer artifacts.
- `previews-full/` — selected previews from the full prototype PDF.

## Validation summary

The full prototype rendered all 274 pages with no script-detected token overflow or fallback boxes. Human visual review is still required.

Next recommended step: validated block-level translation plus cleaned derived backgrounds, then a true hybrid renderer using block text rather than page-level text.
