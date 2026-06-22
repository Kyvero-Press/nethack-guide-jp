# Surya via Podman vs YomiToku sample comparison

Date: 2026-06-21

Surya was rerun successfully using Podman as a Docker-compatible wrapper for Surya's vLLM backend. Docker itself was not running, but rootless Podman GPU passthrough worked with `--gpus all`; a shim translated Surya's Docker command (`--runtime nvidia --gpus device=0`) into Podman-compatible arguments.

## Setup notes

- Surya command: `surya_ocr work/ocr-bakeoff/pages --output_dir work/ocr-bakeoff/surya-podman-full`
- Container backend: `vllm/vllm-openai:v0.20.1` via rootless Podman
- Model: `datalab-to/surya-ocr-2`
- GPU: RTX 4090
- Published sample output:
  - `dist/metadata/ocr-bakeoff/surya-podman-sample/results.json`
  - `dist/metadata/ocr-bakeoff/surya-podman-sample/text/*.txt`

## Qualitative comparison

Surya is stronger than the earlier skipped/untested state suggested. On this book's 12-page sample, it appears **at least competitive with YomiToku and probably better overall** for plain text quality.

Where Surya looks better:

- **Front matter / cover / TOC**: Surya preserves more meaningful text and layout. Page 005 TOC is much cleaner than YomiToku's noisy output.
- **Mixed English + Japanese item lists**: Surya is clearly better on pages like 200, preserving item names and Japanese descriptions in correct order.
- **Prose pages**: Surya is very close to YomiToku and often has cleaner punctuation/paragraph flow.
- **Noise suppression**: Surya avoids some stray symbols YomiToku emitted on page 160.

Where YomiToku still has advantages:

- **Speed and setup**: YomiToku is much easier and faster to run locally. Surya required a large vLLM container image and several minutes of startup.
- **Some literal glyphs/terms**: Surya made a few confident substitutions, e.g. page 150 has `エルブ造り` where YomiToku read `エルフ造り`; page 050 command/key glyphs become circled-number placeholders.
- **Full-book artifacts already exist**: the currently published searchable PDFs/text are YomiToku-based.

## Sample-specific notes

- `pdf005` TOC: Surya wins strongly.
- `pdf011` license prose: tie; both are good.
- `pdf050` command/prose: Surya is cleaner prose, but command key glyphs are questionable (`①/②/③`).
- `pdf100` prose: Surya slightly cleaner punctuation/wording.
- `pdf150` armor/item list: mostly Surya, but YomiToku gets `エルフ造り` correct where Surya reads `エルブ造り`.
- `pdf160` food/armor page: Surya wins; fewer stray symbols.
- `pdf200` weapons list: Surya wins strongly.
- `pdf240` monster prose/list: Surya is very good, but section label/list merging still needs review.
- `pdf274` colophon: Surya preserves author/furigana structure better than YomiToku, though still not perfect.

## Recommendation

If the deliverable is **highest OCR text quality**, Surya should be considered the new leading candidate. A full-book Surya pass has now been run and published alongside the YomiToku outputs:

- `dist/text/surya/nethack-guide-surya.md`
- `dist/text/surya/nethack-guide-surya.txt`
- `dist/pdf/nethack-guide-surya-searchable-compressed.pdf`
- `dist/pdf/nethack-guide-surya-searchable-uncompressed.pdf`

If the deliverable prioritizes **stable, lightweight, reproducible local processing**, YomiToku remains the easier engine to reproduce. For the public OCR artifacts, however, Surya is now the recommended text layer pending manual review of any remaining questionable glyphs.
