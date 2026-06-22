#!/usr/bin/env bash
# Docker-compatible shim for Surya's vLLM backend on a rootless Podman host.
#
# Usage:
#   mkdir -p work/surya-bin
#   ln -sf ../../scripts/surya_podman_docker_shim.sh work/surya-bin/docker
#   PATH="$PWD/work/surya-bin:$PATH" \
#   DOCKER_HF_CACHE_PATH="$PWD/work/surya-hf" \
#   SURYA_INFERENCE_BACKEND=vllm \
#   uvx --from surya-ocr surya_ocr INPUT_DIR --output_dir OUTPUT_DIR
#
# Tunables:
#   SURYA_PODMAN_ROOT     default: $PWD/work/surya-podman-root
#   SURYA_PODMAN_RUNROOT  default: $PWD/work/surya-podman-run
#   SURYA_PODMAN_TMP      default: $PWD/work/surya-podman-tmp

set -euo pipefail

ROOT="${SURYA_PODMAN_ROOT:-$PWD/work/surya-podman-root}"
RUNROOT="${SURYA_PODMAN_RUNROOT:-$PWD/work/surya-podman-run}"
TMPROOT="${SURYA_PODMAN_TMP:-$PWD/work/surya-podman-tmp}"
mkdir -p "$ROOT" "$RUNROOT" "$TMPROOT"
export TMPDIR="$TMPROOT" TMP="$TMPROOT" TEMP="$TMPROOT"

cmd=${1:-}
shift || true
args=()

case "$cmd" in
  run)
    while (($#)); do
      case "$1" in
        --runtime)
          shift 2 || true
          ;;
        --runtime=*)
          shift
          ;;
        --gpus)
          shift
          if (($#)); then shift; fi
          args+=(--gpus all)
          ;;
        --gpus=*)
          args+=(--gpus all)
          shift
          ;;
        vllm/vllm-openai:*)
          args+=("docker.io/$1")
          shift
          ;;
        *)
          args+=("$1")
          shift
          ;;
      esac
    done
    exec podman --root "$ROOT" --runroot "$RUNROOT" run "${args[@]}"
    ;;
  logs|stop|rm|ps|inspect|images|pull|system)
    exec podman --root "$ROOT" --runroot "$RUNROOT" "$cmd" "$@"
    ;;
  *)
    exec podman --root "$ROOT" --runroot "$RUNROOT" "$cmd" "$@"
    ;;
esac
