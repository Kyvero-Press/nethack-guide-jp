#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: scripts/build_processed_pdf.sh \
  --processed-dir DIR \
  --pdforder dist/pdforder.txt \
  --out-pdf work/nethack-guide-processed.pdf \
  [--out-ocr-pdf work/nethack-guide-processed-ocr.pdf] \
  [--dpi 300] [--lang jpn+eng]

Builds an image PDF in pdforder.txt order using img2pdf. If --out-ocr-pdf is
provided, runs ocrmypdf without deskew/cleaning on the image PDF.
EOF
}

processed_dir=""
pdforder=""
out_pdf=""
out_ocr_pdf=""
dpi="300"
lang="jpn+eng"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --processed-dir)
      processed_dir="${2:?--processed-dir requires a value}"
      shift 2
      ;;
    --pdforder)
      pdforder="${2:?--pdforder requires a value}"
      shift 2
      ;;
    --out-pdf)
      out_pdf="${2:?--out-pdf requires a value}"
      shift 2
      ;;
    --out-ocr-pdf)
      out_ocr_pdf="${2:?--out-ocr-pdf requires a value}"
      shift 2
      ;;
    --dpi)
      dpi="${2:?--dpi requires a value}"
      shift 2
      ;;
    --lang)
      lang="${2:?--lang requires a value}"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if [[ -z "$processed_dir" || -z "$pdforder" || -z "$out_pdf" ]]; then
  usage >&2
  exit 2
fi

if ! command -v img2pdf >/dev/null 2>&1; then
  echo "img2pdf is required; install requirements-scan.txt or your distro package" >&2
  exit 127
fi

if [[ ! -f "$pdforder" ]]; then
  echo "Missing pdforder file: $pdforder" >&2
  exit 1
fi

image_dir="$processed_dir"
if [[ -d "$processed_dir/color" ]]; then
  image_dir="$processed_dir/color"
fi

if [[ ! -d "$image_dir" ]]; then
  echo "Missing processed image directory: $image_dir" >&2
  exit 1
fi

mapfile -t image_names < <(sed '/^[[:space:]]*$/d' "$pdforder")
if [[ ${#image_names[@]} -eq 0 ]]; then
  echo "No entries in pdforder file: $pdforder" >&2
  exit 1
fi

images=()
for name in "${image_names[@]}"; do
  path="$image_dir/$name"
  if [[ ! -f "$path" ]]; then
    echo "Missing processed image in pdforder: $path" >&2
    exit 1
  fi
  images+=("$path")
done

mkdir -p "$(dirname "$out_pdf")"
img2pdf --imgsize "${dpi}dpi" --output "$out_pdf" "${images[@]}"
echo "wrote $out_pdf"

if [[ -n "$out_ocr_pdf" ]]; then
  if ! command -v ocrmypdf >/dev/null 2>&1; then
    echo "ocrmypdf is required for --out-ocr-pdf" >&2
    exit 127
  fi
  mkdir -p "$(dirname "$out_ocr_pdf")"
  ocrmypdf -l "$lang" --skip-text --output-type pdf "$out_pdf" "$out_ocr_pdf"
  echo "wrote $out_ocr_pdf"
fi
