# Local translation bakeoff results

Date: 2026-06-21

Source OCR: Surya full-book text (`work/translation/source/pages-surya.jsonl`).

Sample pages translated: 002, 005, 011, 050, 100, 150, 160, 200, 240, 274.

Published sample JSONL outputs:

- `dist/metadata/translation-bakeoff/samples/qwen2_5_3b_instruct.jsonl`
- `dist/metadata/translation-bakeoff/samples/qwen2_5_7b_instruct.jsonl`
- `dist/metadata/translation-bakeoff/samples/qwen3_4b_instruct_2507.jsonl`

## Automated validation

All three sample outputs completed 10/10 records with no empty translations and no high Japanese leakage according to `scripts/validate_translation_outputs.py`.

## Qualitative ranking

1. **Qwen/Qwen2.5-7B-Instruct** — selected.
2. Qwen/Qwen3-4B-Instruct-2507 — fluent but less faithful/less well-behaved.
3. Qwen/Qwen2.5-3B-Instruct — fast baseline but weaker.

## Notes by model

### Qwen2.5 7B

Pros:

- Best overall sample quality.
- Did not echo the source delimiters in tested samples.
- Item lists are readable and preserve terms better than 3B/Qwen3.
- Handles prose pages smoothly.

Cons:

- Still needs human review; OCR errors and ambiguous game terms propagate.
- Occasionally softens or rephrases source wording.
- Higher VRAM and slower than 3B/4B.

Representative page 200 excerpt:

> orcish arrow — Orcish Arrow — A black arrow made by orc craftsmen. Compared to other arrows, it can be said to be of rather poor quality. ... crossbow bolt — Crossbow Bolt — An arrow for a crossbow. Also known as a quarrel.

### Qwen2.5 3B

Pros:

- Very fast and small.
- Coherent on straightforward prose.

Cons:

- Echoed `<<<SOURCE` delimiters on some pages.
- More terminology mistakes: e.g. `orc` became `oak` on page 200.
- Less polished and more literal/awkward.

### Qwen3 4B 2507

Pros:

- Fast and fluent.
- Strong enough for many prose paragraphs.

Cons:

- Echoed `<<<SOURCE` delimiters on multiple pages.
- Made serious terminology mistakes: e.g. `orcish chain mail` became chain mail favored by `oak warriors`; page 240 made Baluchitherium a tapir-family animal instead of rhinoceros-family.
- Changed license wording on page 011 by introducing Free Software Foundation phrasing not present in the OCR source.

## Decision

Run the full book with **Qwen/Qwen2.5-7B-Instruct** for human evaluation.

A second full-book model is not recommended in this first autonomous pass because both alternates showed clear sample regressions. If a second full-book candidate is needed later, rerun the bakeoff with a different local Japanese-focused model rather than the tested 3B/Qwen3 outputs.
