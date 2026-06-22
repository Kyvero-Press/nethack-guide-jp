# Block-level hybrid PDF fit report

## Summary

- `output`: dist/pdf/nethack-guide-qwen2_5_7b-block-hybrid-sample.pdf
- `pages`: 13
- `blocks`: 180
- status counts: `{'preserve_original': 20, 'fitted': 108, 'shrunk': 52}`
- action counts: `{'preserve_original': 20, 'auto': 158, 'manual_text': 2}`

## Blocks needing review

No hard overflow or missing-translation rows.

## Manual/preserved blocks

- page `001` block `001-000` action `preserve_original` status `preserve_original` — Cover media label.
- page `001` block `001-001` action `preserve_original` status `preserve_original` — Cover library label.
- page `001` block `001-002` action `preserve_original` status `preserve_original` — Vertical/artistic cover series text.
- page `001` block `001-003` action `preserve_original` status `preserve_original` — Main title art already English.
- page `001` block `001-004` action `preserve_original` status `preserve_original` — Cover platform label.
- page `001` block `001-005` action `preserve_original` status `preserve_original` — Main cover title block; preserve original art.
- page `001` block `001-006` action `preserve_original` status `preserve_original` — Cover subtitle already English-like.
- page `001` block `001-007` action `preserve_original` status `preserve_original` — Cover credit text; preserve original.
- page `001` block `001-008` action `preserve_original` status `preserve_original` — Cover publisher/price line; preserve original.
- page `001` block `001-009` action `preserve_original` status `preserve_original` — Cover ISBN line; preserve original.
- page `003` block `003-000` action `preserve_original` status `preserve_original` — Title page platform label.
- page `003` block `003-001` action `preserve_original` status `preserve_original` — Title page library label.
- page `003` block `003-002` action `preserve_original` status `preserve_original` — Title page collection label.
- page `003` block `003-003` action `preserve_original` status `preserve_original` — Main NetHack title art.
- page `003` block `003-004` action `preserve_original` status `preserve_original` — The RPG title-page label.
- page `003` block `003-005` action `preserve_original` status `preserve_original` — Title-page credit label.
- page `003` block `003-006` action `preserve_original` status `preserve_original` — Title-page credit name.
- page `003` block `003-007` action `preserve_original` status `preserve_original` — Publisher logo/art.
- page `273` block `273-000` action `preserve_original` status `preserve_original` — Artistic farewell caption in image area.
- page `273` block `273-001` action `preserve_original` status `preserve_original` — Mixed English title artwork already readable.
- page `274` block `274-002` action `manual_text` status `fitted` — Title block contains Japanese reading plus English; render concise English title.
- page `274` block `274-003` action `manual_text` status `fitted` — Avoid retaining Japanese date markers.
