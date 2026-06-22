# YomiToku LLM extractor vs standard YomiToku vs Surya

Date: 2026-06-21

## Question

The original YomiToku OCR pass used the standard YomiToku OCR/layout pipeline, not
`yomitoku_extract_with_llm`. This follow-up tests whether YomiToku's LLM
extractor improves full-page OCR for this Japanese NetHack guide.

## Setup

Input sample: `dist/metadata/ocr-bakeoff/sample-pages.tsv` / `work/ocr-bakeoff/pages/`.

YomiToku LLM schema:

- `work/ocr-bakeoff/yomitoku-llm-schema.yaml`
- later JSON-safe retry schema: `work/ocr-bakeoff/yomitoku-llm-schema-jsonsafe.yaml`

LLM endpoint:

- OpenAI-compatible vLLM container via rootless Podman
- model: `Qwen/Qwen2.5-3B-Instruct`
- final successful server config: `--max-model-len 16384 --gpu-memory-utilization 0.55`
- endpoint: `http://127.0.0.1:8001/v1`

Extractor command shape:

```bash
uvx --from yomitoku --with openai yomitoku_extract_with_llm \
  work/ocr-bakeoff/pages \
  -s work/ocr-bakeoff/yomitoku-llm-schema.yaml \
  -m Qwen/Qwen2.5-3B-Instruct \
  --api-base http://127.0.0.1:8001/v1 \
  --api-key EMPTY \
  --outdir work/ocr-bakeoff/yomitoku-llm \
  --device cuda \
  --temperature 0 \
  --max-tokens 2048 \
  --no-normalize \
  --simple
```

Important: this is **not image-native OCR**. `yomitoku_extract_with_llm` first
runs YomiToku's OCR/layout/table semantic parser, then sends the recognized text
and cell/paragraph metadata to a text LLM for structured extraction. The LLM can
only reorganize or alter YomiToku's OCR data; it cannot recover visual details
that YomiToku did not recognize.

## Published artifacts

- `dist/metadata/ocr-bakeoff/yomitoku-llm-sample/json/` — successful extraction JSON files.
- `dist/metadata/ocr-bakeoff/yomitoku-llm-sample/text/` — extracted `full_page_text` values.
- `dist/metadata/ocr-bakeoff/yomitoku-llm-sample/summary.tsv`
- `dist/metadata/ocr-bakeoff/yomitoku-llm-sample/summary.json`

Run logs remain in ignored `work/ocr-bakeoff/`:

- `work/ocr-bakeoff/yomitoku-llm-run.log`
- `work/ocr-bakeoff/yomitoku-llm-retry*.log`
- `work/ocr-bakeoff/yomitoku-llm-jsonsafe-run.log`
- `work/ocr-bakeoff/yomitoku-llm-cover-last-run.log`

## Result summary

YomiToku-LLM produced valid JSON for **11/12** sample pages. The cover page
failed repeatedly with invalid JSON (`Unterminated string ...`) even after a
JSON-safe schema retry and lower output cap.

The successful pages are not better OCR. The LLM extractor is generally worse
for literal text fidelity:

- It collapses page layout into a single long line/string.
- It loses useful line/paragraph/list structure.
- It sometimes changes characters or wording.
- It hallucinates or preserves semantic-parser noise in front matter and TOC.
- It can fail operationally because YomiToku's semantic prompt is very large for
  dense pages, requiring 12k-16k context even on a 12-page sample.

## Page observations

| Page | Status | Notes |
|---:|---|---|
| 001 | failed | Cover repeatedly returned invalid JSON. This page includes quoted disk-size text and decorative layout; the local 3B model did not produce parseable JSON. |
| 002 | poor | Injects/keeps front-matter noise such as `1/15BARBARLAN`; loses bullet/line structure; contains OCR wording errors. |
| 005 | poor | TOC output contains junk names/phrases (`福永弘飛路家公家安`, etc.) and loses table/list alignment. Surya is much cleaner. |
| 011 | acceptable but not better | License prose is mostly coherent, but LLM collapses paragraphs and punctuation. Standard YomiToku/Surya are preferable. |
| 016 | mixed | Collapses formatting and changes key glyphs/notation (`2)キー`); not better than standard OCR. |
| 050 | worse | Loses command glyph fidelity and collapses prose. Some key text becomes vague or substituted. |
| 100 | worse | Substitution observed: `鎧` becomes `鎖` in `最強の鎧`; punctuation and paragraphing changed. |
| 150 | mixed/worse | Item list mostly present, and it corrects one `エルフ造り` case, but loses list line breaks and is shorter than Surya/YomiToku. |
| 160 | worse | Content mostly present but line/list structure is collapsed; standard Surya is clearer. |
| 200 | worse | Mixed item list collapses; observed `弩` rendered as `努`. Surya is stronger. |
| 240 | worse | Required JSON-safe retry; ordering of monster romanized names changed (`titanothere, baluchitherium` moved before the full list). |
| 274 | mixed/worse | Captures much colophon text but collapses structure and is shorter than Surya. |

## Recommendation

Do **not** use `yomitoku_extract_with_llm` for the final OCR text layer or
searchable PDFs.

For this book, the LLM extractor is useful only as evidence that structured
extraction is the wrong tool for literal OCR. It may be useful for forms/tables
where a small schema asks for specific fields, but it is a poor fit for full-page
book transcription.

Current OCR recommendation remains:

1. **Surya OCR 2** for highest-quality text/Markdown/searchable PDF layer.
2. **Standard YomiToku** as the lightweight, reproducible baseline and fallback.
3. **YomiToku LLM extractor** rejected for full-book OCR.

## Validation

- CUDA YomiToku prepass was used (`--device cuda`).
- LLM inference used local vLLM on GPU; no CPU LLM inference was used.
- Successful extraction JSON count: 11/12 sample pages.
- Failed page: 001 cover.
