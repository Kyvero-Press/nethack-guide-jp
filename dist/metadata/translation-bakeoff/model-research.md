# Local Japanese-to-English translation model candidates

Date: 2026-06-21

## Hardware/runtime constraints

- GPU: RTX 4090, 24GB VRAM.
- Disk at start of translation work: about 37GB free under `/home`.
- Local serving path: rootless Podman running `docker.io/vllm/vllm-openai:v0.20.1` with OpenAI-compatible API on `http://127.0.0.1:8001/v1`.
- Requirement: local models only; no CPU LLM inference. One vLLM model is loaded at a time.

## Models tested

### Qwen/Qwen2.5-3B-Instruct

- Status: cached locally from the YomiToku-LLM test.
- Pros: fast, low download cost, fits easily.
- Cons: weaker translation quality; echoed `<<<SOURCE` delimiters on some pages; more terminology mistakes.

### Qwen/Qwen2.5-7B-Instruct

- Status: cached locally.
- Pros: best sample quality among tested local candidates; more stable formatting; fewer source-marker echoes; strong enough for prose and item lists.
- Cons: slower and higher VRAM than 3B/4B; still needs human review for OCR-driven terms and sensitive game terminology.

### Qwen/Qwen3-4B-Instruct-2507

- Status: downloaded and tested locally.
- Pros: fast and modern; fluent prose.
- Cons: echoed `<<<SOURCE` delimiters on several sample pages; made notable terminology errors such as `orc` -> `oak` and changed license wording; not selected.

## Candidate not run in this first pass

- NLLB/Marian-style translation-specific models: local and useful as baselines, but not LLMs and would require additional downloads. Given disk constraints and the user's explicit interest in LLMs, the first full-book run uses the best tested local LLM.
- Larger Japanese-focused models: likely better in some cases but risk exceeding local disk/VRAM/time budget without quantization setup.

## Selection

Selected full-book model: **Qwen/Qwen2.5-7B-Instruct**.

Reason: best balance of local availability, quality, and operational stability on the sample bakeoff.
