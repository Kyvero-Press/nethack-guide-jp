# Qwen2.5-7B local English translation

Machine translation generated locally from Surya OCR using `Qwen/Qwen2.5-7B-Instruct` served by vLLM.

This is for human evaluation, not a polished publication. OCR errors and translation errors remain possible.

Files:

- `translation-records.jsonl` — raw per-page translation records and metadata.
- `nethack-guide-qwen2_5_7b-instruct-en.md` — combined Markdown.
- `nethack-guide-qwen2_5_7b-instruct-en.txt` — combined plain text.
- `pages/` — per-page Markdown.
- `pages-txt/` — per-page plain text.
- `page-map.tsv` — page/status/patch map.
- `run.log` and `validation.log` — generation and validation evidence.

Manual patches:

- Page 196: removed Japanese item-label echoes and one Chinese leakage token from the model output.
- Page 233: replaced a full-page output that switched to Chinese mid-page, using shorter local-vLLM chunk/sentence retries plus glossary correction.
