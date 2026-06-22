#!/usr/bin/env python3
"""Shared helpers for block-level translated PDF reconstruction."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

import yaml
from PIL import Image
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

CJK_RE = re.compile(r"[\u3040-\u30ff\u3400-\u9fff]")
JP_RE = re.compile(r"[\u3040-\u30ff]")

RENDER_ACTIONS = {
    "auto",
    "preserve_original",
    "skip_mask",
    "manual_text",
    "caption_only",
    "omit",
}

TEXT_LABELS = {
    "Text",
    "SectionHeader",
    "Title",
    "Caption",
    "ListGroup",
    "List",
    "Table",
    "TableOfContents",
    "Footnote",
}


@dataclass(frozen=True)
class BlockKey:
    block_id: str
    source_sha256: str

    @classmethod
    def from_row(cls, row: Mapping[str, Any]) -> "BlockKey":
        return cls(str(row["block_id"]), str(row["source_sha256"]))

    def record_id(self, page_label: str) -> str:
        return f"block:{page_label}:{self.block_id}:{self.source_sha256}"


@dataclass(frozen=True)
class BlockSource:
    page: int
    page_label: str
    source_image: str
    source_key: str
    block_id: str
    reading_order: int
    label: str
    bbox: tuple[float, float, float, float]
    source_text: str
    source_sha256: str

    @classmethod
    def from_row(cls, row: Mapping[str, Any]) -> "BlockSource":
        bbox_raw = row.get("bbox")
        if not isinstance(bbox_raw, list) or len(bbox_raw) != 4:
            raise ValueError(f"invalid bbox for {row.get('block_id')}: {bbox_raw!r}")
        bbox = tuple(float(v) for v in bbox_raw)
        x0, y0, x1, y1 = bbox
        if x1 <= x0 or y1 <= y0:
            raise ValueError(f"non-positive bbox for {row.get('block_id')}: {bbox!r}")
        return cls(
            page=int(row["page"]),
            page_label=str(row["page_label"]),
            source_image=str(row["source_image"]),
            source_key=str(row.get("source_key") or ""),
            block_id=str(row["block_id"]),
            reading_order=int(row.get("reading_order") or 0),
            label=str(row.get("label") or "Text"),
            bbox=bbox,
            source_text=str(row.get("source_text") or ""),
            source_sha256=str(row["source_sha256"]),
        )

    @property
    def key(self) -> BlockKey:
        return BlockKey(self.block_id, self.source_sha256)

    @property
    def width_px(self) -> float:
        return self.bbox[2] - self.bbox[0]

    @property
    def height_px(self) -> float:
        return self.bbox[3] - self.bbox[1]

    @property
    def is_tall_narrow(self) -> bool:
        return self.height_px > self.width_px * 2.5 and self.height_px > 120

    def to_row(self) -> dict[str, Any]:
        return {
            "record_type": "block",
            "page": self.page,
            "page_label": self.page_label,
            "source_image": self.source_image,
            "source_key": self.source_key,
            "block_id": self.block_id,
            "reading_order": self.reading_order,
            "label": self.label,
            "bbox": list(self.bbox),
            "source_text": self.source_text,
            "source_sha256": self.source_sha256,
        }


@dataclass(frozen=True)
class RenderOverride:
    action: str = "auto"
    manual_text: str | None = None
    bbox: tuple[float, float, float, float] | None = None
    source_sha256: str | None = None
    mask_padding_px: int | None = None
    rotation_deg: float = 0.0
    min_font_size: float | None = None
    max_font_size: float | None = None
    font_family: str | None = None
    fill_color: str | None = None
    note: str = ""


@dataclass(frozen=True)
class RenderDecision:
    block: BlockSource
    override: RenderOverride

    @property
    def action(self) -> str:
        return self.override.action

    @property
    def bbox(self) -> tuple[float, float, float, float]:
        return self.override.bbox or self.block.bbox

    @property
    def mask_padding_px(self) -> int:
        if self.override.mask_padding_px is not None:
            return int(self.override.mask_padding_px)
        if self.block.is_tall_narrow:
            return 2
        return 5


@dataclass(frozen=True)
class TranslationRecord:
    block_id: str
    source_sha256: str
    translation: str
    status: str
    row: dict[str, Any]


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not path.exists():
        return rows
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: Iterable[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(dict(row), ensure_ascii=False, sort_keys=True) + "\n")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_pdforder(path: Path) -> list[str]:
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def parse_page_selection(value: str | None, total_pages: int) -> list[int]:
    if not value:
        return list(range(1, total_pages + 1))
    pages: set[int] = set()
    for part in value.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start_s, end_s = part.split("-", 1)
            start, end = int(start_s), int(end_s)
            pages.update(range(start, end + 1))
        else:
            pages.add(int(part))
    return sorted(p for p in pages if 1 <= p <= total_pages)


def load_block_sources(path: Path) -> list[BlockSource]:
    blocks = [BlockSource.from_row(row) for row in read_jsonl(path)]
    seen: set[BlockKey] = set()
    for block in blocks:
        if block.key in seen:
            raise ValueError(f"duplicate block/source key: {block.block_id} {block.source_sha256}")
        seen.add(block.key)
    return blocks


def group_blocks_by_page(blocks: Iterable[BlockSource]) -> dict[int, list[BlockSource]]:
    by_page: dict[int, list[BlockSource]] = {}
    for block in blocks:
        by_page.setdefault(block.page, []).append(block)
    for page_blocks in by_page.values():
        page_blocks.sort(key=lambda b: (b.reading_order, b.bbox[1], b.bbox[0], b.block_id))
    return by_page


def load_translation_records(path: Path) -> dict[BlockKey, TranslationRecord]:
    records: dict[BlockKey, TranslationRecord] = {}
    for row in read_jsonl(path):
        if row.get("record_type") != "block" and "block_id" not in row:
            continue
        block_id = str(row.get("block_id") or "")
        source_sha256 = str(row.get("source_sha256") or "")
        if not block_id or not source_sha256:
            continue
        key = BlockKey(block_id, source_sha256)
        records[key] = TranslationRecord(
            block_id=block_id,
            source_sha256=source_sha256,
            translation=str(row.get("translation") or ""),
            status=str(row.get("status") or ""),
            row=dict(row),
        )
    return records


def normalize_override(raw: Mapping[str, Any], block_id: str) -> RenderOverride:
    action = str(raw.get("action") or raw.get("mode") or "auto")
    if action not in RENDER_ACTIONS:
        raise ValueError(f"unknown render override action for {block_id}: {action}")
    bbox = raw.get("bbox") or raw.get("bbox_override")
    bbox_tuple = None
    if bbox is not None:
        if not isinstance(bbox, list) or len(bbox) != 4:
            raise ValueError(f"override bbox for {block_id} must be a 4-number list")
        bbox_tuple = tuple(float(v) for v in bbox)
        if bbox_tuple[2] <= bbox_tuple[0] or bbox_tuple[3] <= bbox_tuple[1]:
            raise ValueError(f"override bbox for {block_id} has non-positive size")
    return RenderOverride(
        action=action,
        manual_text=raw.get("manual_text") if raw.get("manual_text") is not None else raw.get("text"),
        bbox=bbox_tuple,
        source_sha256=str(raw["source_sha256"]) if raw.get("source_sha256") else None,
        mask_padding_px=int(raw["mask_padding_px"]) if raw.get("mask_padding_px") is not None else None,
        rotation_deg=float(raw.get("rotation_deg") or 0.0),
        min_font_size=float(raw["min_font_size"]) if raw.get("min_font_size") is not None else None,
        max_font_size=float(raw["max_font_size"]) if raw.get("max_font_size") is not None else None,
        font_family=str(raw["font_family"]) if raw.get("font_family") else None,
        fill_color=str(raw["fill_color"]) if raw.get("fill_color") else None,
        note=str(raw.get("note") or raw.get("reason") or ""),
    )


def load_render_overrides(path: Path | None, sources: Sequence[BlockSource] | None = None) -> dict[str, RenderOverride]:
    if not path or not path.exists():
        return {}
    payload = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    raw_blocks: dict[str, Any] = {}
    if isinstance(payload.get("blocks"), dict):
        raw_blocks.update(payload["blocks"])
    if isinstance(payload.get("pages"), dict):
        for _page, page_payload in payload["pages"].items():
            if isinstance(page_payload, dict) and isinstance(page_payload.get("blocks"), dict):
                raw_blocks.update(page_payload["blocks"])
    overrides = {str(block_id): normalize_override(raw or {}, str(block_id)) for block_id, raw in raw_blocks.items()}
    if sources is not None:
        by_id = {block.block_id: block for block in sources}
        for block_id, override in overrides.items():
            if block_id not in by_id:
                raise ValueError(f"override references unknown block_id {block_id}")
            if override.source_sha256 and override.source_sha256 != by_id[block_id].source_sha256:
                raise ValueError(f"override source_sha256 mismatch for {block_id}")
    return overrides


def decision_for_block(block: BlockSource, overrides: Mapping[str, RenderOverride]) -> RenderDecision:
    return RenderDecision(block=block, override=overrides.get(block.block_id, RenderOverride()))


def cjk_ratio(text: str) -> float:
    return len(CJK_RE.findall(text)) / max(1, len(text))


def contains_cjk(text: str) -> bool:
    return bool(CJK_RE.search(text))


def repeated_loop(text: str) -> bool:
    if len(text) < 160:
        return False
    candidates = [text[:20], text[:30], text[:40], text[:60]]
    return any(chunk.strip() and chunk * 4 in text for chunk in candidates)


def source_record_id(row: Mapping[str, Any]) -> str:
    if row.get("record_type") == "block" or row.get("block_id"):
        return f"block:{row['page_label']}:{row['block_id']}:{row['source_sha256']}"
    return f"page:{row['page_label']}:{row['source_sha256']}"


def image_size(path: Path) -> tuple[int, int]:
    with Image.open(path) as image:
        return image.size


def px_bbox_to_pt_box(
    bbox: tuple[float, float, float, float],
    page_height_pt: float,
    scale: float,
    pad_pt: float = 0.0,
) -> tuple[float, float, float, float]:
    x0, y0, x1, y1 = bbox
    x = x0 * scale - pad_pt
    y = page_height_pt - y1 * scale - pad_pt
    w = (x1 - x0) * scale + 2 * pad_pt
    h = (y1 - y0) * scale + 2 * pad_pt
    return x, y, w, h


def register_font(font_path: Path | None = None, name: str = "TranslatedPdfFont") -> str:
    candidates = [
        font_path,
        # Debian/Ubuntu-style paths.
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"),
        Path("/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf"),
        Path("/usr/share/fonts/truetype/liberation2/LiberationSerif-Regular.ttf"),
        # Arch/GNU Guix-style paths seen on the restoration workstation.
        Path("/usr/share/fonts/TTF/DejaVuSansCondensed.ttf"),
        Path("/usr/share/fonts/TTF/DejaVuSans.ttf"),
        Path("/usr/share/fonts/TTF/DejaVuSerif.ttf"),
        Path("/usr/share/fonts/liberation/LiberationSans-Regular.ttf"),
        Path("/usr/share/fonts/liberation/LiberationSerif-Regular.ttf"),
        # Broad fallback, if present.
        Path("/usr/share/fonts/noto/NotoSans-Regular.ttf"),
    ]
    for candidate in candidates:
        if candidate and candidate.exists():
            if name not in pdfmetrics.getRegisteredFontNames():
                pdfmetrics.registerFont(TTFont(name, str(candidate)))
            return name
    return "Times-Roman"


def font_size_bounds(label: str, override: RenderOverride | None = None) -> tuple[float, float]:
    label = label or "Text"
    if label in {"SectionHeader", "Title"}:
        default_min, default_max = 5.5, 12.0
    elif label in {"Caption", "Footnote"}:
        default_min, default_max = 4.5, 7.0
    elif label in {"Table", "ListGroup", "List"}:
        default_min, default_max = 4.5, 8.0
    else:
        default_min, default_max = 4.8, 8.8
    if override:
        if override.min_font_size is not None:
            default_min = override.min_font_size
        if override.max_font_size is not None:
            default_max = override.max_font_size
    if default_max < default_min:
        default_max = default_min
    return default_min, default_max


def tokenize_for_wrap(text: str) -> list[str]:
    tokens: list[str] = []
    for paragraph in re.split(r"\n\s*\n", text.strip()):
        paragraph = paragraph.strip()
        if not paragraph:
            continue
        # Keep slash-heavy item names intact while wrapping mostly on spaces.
        tokens.extend(paragraph.split())
        tokens.append("\n")
    return tokens


def wrap_line(font_name: str, font_size: float, words: Sequence[str], width: float) -> tuple[str, int]:
    line_words: list[str] = []
    used = 0
    for word in words:
        candidate = " ".join([*line_words, word]) if line_words else word
        if pdfmetrics.stringWidth(candidate, font_name, font_size) <= width or not line_words:
            line_words.append(word)
            used += 1
        else:
            break
    return " ".join(line_words), used


def count_fit_tokens(
    text: str,
    box_w: float,
    box_h: float,
    font_name: str,
    font_size: float,
    leading_factor: float = 1.14,
) -> tuple[int, int]:
    tokens = tokenize_for_wrap(text)
    remaining = list(tokens)
    line_height = font_size * leading_factor
    lines = max(0, int((box_h - 1.5) // line_height))
    drawn = 0
    for _ in range(lines):
        while remaining and remaining[0] == "\n":
            remaining.pop(0)
            drawn += 1
            # paragraph gap consumes part of a line; approximate as a line for fitting.
            break
        if not remaining:
            break
        segment: list[str] = []
        for token in remaining:
            if token == "\n":
                break
            segment.append(token)
        if not segment:
            continue
        _line, used = wrap_line(font_name, font_size, segment, max(1.0, box_w - 2.0))
        if used <= 0:
            break
        del remaining[:used]
        drawn += used
    return drawn, len([t for t in remaining if t != "\n"])


def choose_fitting_font_size(
    text: str,
    box_w: float,
    box_h: float,
    font_name: str,
    min_size: float,
    max_size: float,
) -> tuple[float, int]:
    best = min_size
    best_remaining = len([t for t in tokenize_for_wrap(text) if t != "\n"])
    steps = [max_size - i * 0.5 for i in range(int(math.ceil((max_size - min_size) / 0.5)) + 1)]
    if min_size not in steps:
        steps.append(min_size)
    for size in steps:
        if size < min_size:
            continue
        _drawn, remaining = count_fit_tokens(text, box_w, box_h, font_name, size)
        if remaining == 0:
            return size, 0
        if remaining < best_remaining:
            best = size
            best_remaining = remaining
    return best, best_remaining


def draw_wrapped_text(
    c: Any,
    text: str,
    x: float,
    y: float,
    w: float,
    h: float,
    font_name: str,
    font_size: float,
    leading_factor: float = 1.14,
) -> int:
    tokens = tokenize_for_wrap(text)
    remaining = list(tokens)
    line_height = font_size * leading_factor
    current_y = y + h - line_height
    c.setFont(font_name, font_size)
    while current_y >= y and remaining:
        while remaining and remaining[0] == "\n":
            remaining.pop(0)
            current_y -= line_height * 0.45
            if current_y < y:
                return len([t for t in remaining if t != "\n"])
        if not remaining:
            break
        segment: list[str] = []
        for token in remaining:
            if token == "\n":
                break
            segment.append(token)
        if not segment:
            continue
        line, used = wrap_line(font_name, font_size, segment, max(1.0, w - 2.0))
        if used <= 0 or not line:
            break
        c.drawString(x + 1.0, current_y, line)
        del remaining[:used]
        current_y -= line_height
    return len([t for t in remaining if t != "\n"])


def source_manifest(
    *,
    source_jsonl: Path,
    pdforder: Path,
    images_dir: Path,
    blocks: Sequence[BlockSource] | None = None,
) -> dict[str, Any]:
    order = read_pdforder(pdforder)
    block_list = list(blocks) if blocks is not None else load_block_sources(source_jsonl)
    by_page = group_blocks_by_page(block_list)
    missing_images = [name for name in order if not (images_dir / name).exists()]
    missing_pages = [page for page in range(1, len(order) + 1) if page not in by_page]
    page_counts = {f"{page:03d}": len(by_page.get(page, [])) for page in range(1, len(order) + 1)}
    return {
        "source_jsonl": str(source_jsonl),
        "source_jsonl_sha256": sha256_file(source_jsonl) if source_jsonl.exists() else None,
        "pdforder": str(pdforder),
        "pdforder_sha256": sha256_file(pdforder) if pdforder.exists() else None,
        "images_dir": str(images_dir),
        "pdforder_pages": len(order),
        "block_count": len(block_list),
        "pages_with_blocks": len(by_page),
        "pages_without_blocks": [f"{p:03d}" for p in missing_pages],
        "per_page_block_counts": page_counts,
        "missing_images": missing_images,
    }


def add_common_page_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--pdforder", type=Path, default=Path("dist/pdforder.txt"))
    parser.add_argument("--pages", help="Comma/range page selection such as 1,5,10-12")
