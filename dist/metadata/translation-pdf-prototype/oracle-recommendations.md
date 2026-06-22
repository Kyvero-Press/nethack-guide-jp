# Oracle recommendations: translated PDF reconstruction

Date: 2026-06-21

Oracle session: `nethack-translated-pdf-reconstruc` (`gpt-5.5-pro`, browser Pro Extended).

## Summary

Oracle recommended a **hybrid translated facsimile** as the primary path, plus a **side-by-side/interleaved review PDF** as a mandatory QA companion.

Practical ranking:

1. Hybrid: preserve page art/images, mask text, redraw English text — best primary path.
2. Side-by-side original + translation — mandatory review artifact.
3. Image background + white text overlays — acceptable smoke test/prototype, but not final.
4. Full vector/layout reconstruction — defer until layout and block-level translation are stable.

## Key warnings

- Do not treat page-level translation poured into Surya bboxes as final; it is only a smoke test because it loses block/paragraph alignment.
- Better facsimile output needs block-level translations keyed to stable Surya block IDs.
- Do not silently truncate overflow; every overflow or fallback needs metadata.
- Do not attempt professional cover/artistic/vertical typography automatically; preserve original art and add captions/overlays or manual overrides.
- Do not overwrite original scans or refined crops; build derived backgrounds separately.

## Implementation guidance adopted here

Implemented in this pass:

- A smoke-test hybrid prototype script:
  - `scripts/make_translated_pdf_prototype.py`
- A side-by-side review PDF script:
  - `scripts/make_translation_review_pdf.py`
- Full page-level translated text artifacts:
  - `dist/text/translation-local/qwen2_5_7b_instruct/`
- Full prototype translated facsimile PDF:
  - `dist/pdf/nethack-guide-qwen2_5_7b-translated-prototype.pdf`
- Full side-by-side review PDF:
  - `dist/pdf/nethack-guide-qwen2_5_7b-translation-review.pdf`

Deferred to next iteration:

- Stable normalized layout JSONL under `dist/metadata/translated-layout/`.
- Full block-level translation with JSON/block-id validation.
- Cleaned derived page backgrounds instead of only drawing white rectangles in PDF.
- Manual overrides for cover, vertical/artistic labels, and problematic dense item-list pages.

## Notes from local block-level sample

A 12-page block-level Qwen2.5-7B sample was attempted using existing block records. It improves granularity but still produced CJK/Chinese leakage in several short/ambiguous blocks. This confirms Oracle's recommendation that block-level translation should be done with stricter validation and retry/patch machinery before it replaces the page-level review translation.
