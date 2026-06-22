# OCR bakeoff for refined NetHack guide scans

Date: 2026-06-21

Input sample pages came from `dist/crops/refined/` using canonical `dist/pdforder.txt` order:

- 001 cover
- 002 opening/copyright
- 005 table of contents
- 011 license prose
- 016 command/instructions
- 050 command + prose
- 100 prose
- 150 item list with English + Japanese terms
- 160 item/list page
- 200 item list with English + Japanese terms
- 240 monster prose/list
- 274 colophon

## Engines tried

### Tesseract `jpn+eng`

Output: `work/ocr-bakeoff/tesseract/`

Result: rejected. It recognized some body text but produced many spurious spaces, circled-number confusions, broken Japanese, and very noisy front matter/table-of-contents output.

### YomiToku

Output: `work/ocr-bakeoff/yomitoku/`

Result: selected at the time of the initial full-book run. It was the strongest successfully-run engine before the later Surya-via-Podman test: good Japanese prose fidelity, good layout/reading order, decent mixed English/Japanese item headings, fast GPU throughput, and low hallucination compared with VLM OCR systems.

Notable strengths observed:

- Page 011 license page is clean and coherent.
- Page 050 prose is much cleaner than Tesseract, with paragraph-level output.
- Page 100/150/160/240 mixed prose/list pages preserve most content and terminology.
- Much faster than CPU NDLOCR-Lite and much less normalization than Chandra/Qwen.

Known weaknesses:

- Some tiny key glyphs are missed, e.g. page 050 loses the exact pickup key glyph where Qwen/Chandra guessed `[y]`/`[n]` better.
- TOC/front matter can still have decorative/noisy text.
- Some headings/footers are included in text output.

### YomiToku `yomitoku_extract_with_llm`

Output:

- `work/ocr-bakeoff/yomitoku-llm/`
- `dist/metadata/ocr-bakeoff/yomitoku-llm-sample/`
- `dist/metadata/ocr-bakeoff/yomitoku-llm-vs-yomitoku-surya.md`

Result: rejected for full-page/book OCR. This path is structured extraction over
YomiToku OCR/layout/table-semantic text using a local vLLM text model; it is not
image-native OCR. Tested with local GPU vLLM
`Qwen/Qwen2.5-3B-Instruct`. It produced valid JSON for 11/12 sample pages but
failed repeatedly on the cover and generally degraded literal OCR fidelity by
collapsing layout, losing line/list structure, and introducing substitutions or
front-matter junk. It may be useful for form/table field extraction, but not for
this book's final OCR layer.

### NDLOCR-Lite

Output: `work/ocr-bakeoff/ndlocr-lite/`

Result: good Japanese library-scan baseline but not selected. It preserved line breaks nicely and handled TOC page 005 well, but was slower on CPU and had more errors in English item names and some repeated/corrupted phrase artifacts, e.g. page 100.

### Qwen3.5-OCR-JP-2B

Output: `work/ocr-bakeoff/qwen-jp/`

Result: promising but not selected. It was good on layout blocks and sometimes better on tiny command/key glyphs. However, it showed small hallucination/normalization behavior that is risky for a book OCR deliverable: substitutions like `人に`/`人を`, omitted particles, and `メイル` normalized to `メール`.

### Chandra OCR 2 local HF mode

Output: `work/ocr-bakeoff/chandra/`

Result: not selected. It produced fluent Markdown but normalized/hallucinated Japanese terms more than desired for literal OCR, e.g. `チェインメイル` -> `チェーンメール`, `イェンダー` corruption, and some simplified/changed phrasing.

### Surya OCR 2

Initial Docker run failed because Docker daemon was not running. It was rerun
successfully through rootless Podman using `scripts/surya_podman_docker_shim.sh`,
a small `docker` shim that translated Surya's vLLM Docker command to
Podman-compatible GPU arguments.

Output:

- `work/ocr-bakeoff/surya-podman-full/pages/results.json`
- `dist/metadata/ocr-bakeoff/surya-podman-sample/results.json`
- `dist/metadata/ocr-bakeoff/surya-podman-sample/text/*.txt`
- `dist/metadata/ocr-bakeoff/surya-vs-yomitoku.md`

Result: very strong. On the 12-page bakeoff set, Surya is often cleaner than
YomiToku, especially for the table of contents/front matter and mixed
English/Japanese item-list pages. It still makes some confident substitutions
on tiny glyphs or terms, but after this Podman run it should be considered a
leading candidate for highest-quality OCR.

## Decision

Initial full-book engine: **YomiToku**.

Reason at the time: quality for this specific Japanese printed book was best
overall among the engines that had successfully run, with better literal
fidelity than Chandra/Qwen and far less noise than Tesseract.

After the later successful Surya-via-Podman bakeoff, the recommendation changed:
for **highest OCR text quality**, run a full-book Surya pass and compare it
against the already-published YomiToku artifacts. That full-book Surya text pass
has now been run and published. Surya is now published as text/Markdown, raw
JSON OCR results, and compressed/lossless searchable PDFs. The YomiToku
searchable PDFs remain available as the earlier baseline. A later YomiToku-LLM
extractor test was rejected for full-page OCR.

## Full-book outputs

Final YomiToku OCR outputs were generated under `work/ocr-final/` and published
under `dist/`:

- `work/ocr-final/nethack-guide-yomitoku.md` — combined Markdown, 274 pages, canonical order.
- `work/ocr-final/nethack-guide-yomitoku.txt` — combined plain text, 274 pages, canonical order.
- `dist/pdf/nethack-guide-yomitoku-searchable-uncompressed.pdf` — lossless/uncompressed-style searchable image PDF, 274 pages, 300 DPI coordinate scaling, ~1.6GB. It embeds page images without JPEG quantization.
- `dist/pdf/nethack-guide-yomitoku-searchable-compressed.pdf` — smaller searchable image PDF, 274 pages, 300 DPI coordinate scaling, ~265MB. It uses a JPEG-compressed image layer.
- `dist/text/yomitoku/nethack-guide-yomitoku-searchable-uncompressed-pdftotext.txt` — `pdftotext` extraction from the uncompressed/lossless searchable PDF for smoke-checking.
- `dist/text/yomitoku/nethack-guide-yomitoku-searchable-compressed-pdftotext.txt` — `pdftotext` extraction from the compressed searchable PDF for smoke-checking.
- `work/ocr-final/yomitoku/md-pages/` — per-page Markdown files.
- `work/ocr-final/yomitoku/page-map.tsv` — mapping from canonical page number to source refined crop.

Final Surya OCR outputs:

- `dist/text/surya/nethack-guide-surya.md` — combined Markdown, 274 pages, canonical order.
- `dist/text/surya/nethack-guide-surya.txt` — combined plain text, 274 pages, canonical order.
- `dist/text/surya/pages/` — per-page Markdown and plain text.
- `dist/text/surya/page-map.tsv` — mapping from canonical page number to source refined crop.
- `dist/pdf/nethack-guide-surya-searchable-uncompressed.pdf` — lossless/uncompressed-style searchable image PDF, 274 pages, 300 DPI coordinate scaling, ~1.6GB. It embeds page images without JPEG quantization.
- `dist/pdf/nethack-guide-surya-searchable-compressed.pdf` — smaller searchable image PDF, 274 pages, 300 DPI coordinate scaling, ~258MB. It uses a JPEG-compressed image layer.
- `dist/text/surya/nethack-guide-surya-searchable-uncompressed-pdftotext.txt` — `pdftotext` extraction from the Surya uncompressed/lossless searchable PDF for smoke-checking.
- `dist/text/surya/nethack-guide-surya-searchable-compressed-pdftotext.txt` — `pdftotext` extraction from the Surya compressed searchable PDF for smoke-checking.
- `dist/metadata/ocr-bakeoff/surya-full/results.json` — raw full-book Surya OCR JSON.
- `dist/metadata/ocr-bakeoff/surya-full/run.log` — full-book Surya run log.
- `scripts/make_surya_searchable_pdf.py` — builder for searchable PDFs from Surya block boxes.

YomiToku-LLM sample outputs:

- `dist/metadata/ocr-bakeoff/sample-pages.tsv` — shared 12-page bakeoff sample manifest.
- `dist/metadata/ocr-bakeoff/yomitoku-llm-vs-yomitoku-surya.md` — comparison report.
- `dist/metadata/ocr-bakeoff/yomitoku-llm-sample/` — successful sample JSON/text plus summary tables.

Validation performed:

- YomiToku Markdown per-page count: 274/274.
- Surya per-page text count: 274/274 plain text and 274/274 Markdown.
- YomiToku searchable PDF page count: 274.
- Surya searchable PDF page count: 274 for both compressed and lossless PDFs.
- Body page size check: page 7 is `408 x 585.6 pt`, matching `1700 x 2440 px` at 300 DPI for both YomiToku and Surya PDFs.
- `pdfimages` smoke test: Surya compressed PDF image layer reports `jpeg`; Surya lossless/uncompressed PDF image layer reports non-JPEG `image`.
- `pdftotext` smoke test found expected strings in both YomiToku searchable PDFs:
  - `ネットハック・ジェネラルパブリックライセンス`
  - `ピックアップ`
  - `hawaiian shirt`
  - `NetHack the R. P. G.`
- Surya combined text and both Surya searchable PDF `pdftotext` outputs found the same expected strings:
  - `ネットハック・ジェネラルパブリックライセンス`
  - `ピックアップ`
  - `hawaiian shirt`
  - `NetHack the R. P. G.`

## Downstream local translation outputs

After Surya was selected as the OCR source, local Japanese-to-English translation
bakeoffs were run under `dist/metadata/translation-bakeoff/`. The selected
full-book local model was `Qwen/Qwen2.5-7B-Instruct` served by vLLM. Published
translation/review artifacts include:

- `dist/text/translation-local/qwen2_5_7b_instruct/`
- `dist/pdf/nethack-guide-qwen2_5_7b-translation-review.pdf`
- `dist/pdf/nethack-guide-qwen2_5_7b-translated-prototype.pdf`

The translated facsimile PDF is a prototype only; Oracle and local tests both
recommend block-level translation plus cleaned derived backgrounds for a higher
quality next iteration.
