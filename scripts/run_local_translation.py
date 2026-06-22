#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows=[]
    with path.open(encoding='utf-8') as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a', encoding='utf-8') as f:
        f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + '\n')


def load_done(path: Path) -> set[str]:
    if not path.exists():
        return set()
    done=set()
    for row in read_jsonl(path):
        done.add(row['record_id'])
    return done


def record_id(row: dict[str, Any]) -> str:
    if row.get('record_type') == 'block':
        return f"block:{row['page_label']}:{row['block_id']}:{row['source_sha256']}"
    return f"page:{row['page_label']}:{row['source_sha256']}"


def load_text(path: Path | None) -> str:
    return path.read_text(encoding='utf-8') if path else ''


def make_prompt(template: str, glossary: str, row: dict[str, Any]) -> str:
    metadata = [
        f"page={row.get('page_label')}",
        f"image={row.get('source_image')}",
        f"record_type={row.get('record_type')}",
    ]
    if row.get('record_type') == 'block':
        metadata.extend([
            f"block_id={row.get('block_id')}",
            f"reading_order={row.get('reading_order')}",
            f"label={row.get('label')}",
            f"bbox={row.get('bbox')}",
        ])
    return (
        template.rstrip()
        + '\n\nGlossary / style notes:\n'
        + glossary.strip()
        + '\n\nSource metadata:\n'
        + ' '.join(metadata)
        + '\n\nJapanese OCR source text:\n<<<SOURCE\n'
        + row['source_text'].strip()
        + '\nSOURCE\n>>>\n\nEnglish translation:'
    )


_CJK_RE = __import__('re').compile(r'[\u3040-\u30ff\u3400-\u9fff]')


def should_passthrough(row: dict[str, Any], enabled: bool) -> bool:
    if not enabled:
        return False
    text = (row.get('source_text') or '').strip()
    if not text:
        return True
    # For block-level rendering, English item names, ISBNs, page numbers, and
    # model numbers should remain unchanged and do not need an LLM call.
    return not _CJK_RE.search(text)


def chat(base_url: str, model: str, prompt: str, temperature: float, max_tokens: int, timeout: int) -> str:
    url = base_url.rstrip('/') + '/chat/completions'
    body = {
        'model': model,
        'messages': [
            {'role': 'system', 'content': 'You are a faithful Japanese-to-English translator. Return only the English translation. Do not output Chinese or Japanese prose; avoid CJK characters unless the source is an untranslated proper noun that must remain as-is.'},
            {'role': 'user', 'content': prompt},
        ],
        'temperature': temperature,
        'max_tokens': max_tokens,
    }
    data = json.dumps(body).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer EMPTY'})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        payload = json.loads(resp.read().decode('utf-8'))
    return payload['choices'][0]['message']['content'].strip()


def main() -> None:
    p=argparse.ArgumentParser(description='Translate OCR JSONL records with a local OpenAI-compatible LLM endpoint.')
    p.add_argument('--input-jsonl', type=Path, required=True)
    p.add_argument('--output-jsonl', type=Path, required=True)
    p.add_argument('--model', required=True)
    p.add_argument('--base-url', default='http://127.0.0.1:8001/v1')
    p.add_argument('--prompt', type=Path, default=Path('config/translation-prompts/ja-en-guide-v1.md'))
    p.add_argument('--glossary', type=Path, default=Path('config/translation-glossary.yaml'))
    p.add_argument('--pages', default='', help='Comma/range page filter, e.g. 1,5,11-20')
    p.add_argument('--limit', type=int, default=0)
    p.add_argument('--temperature', type=float, default=0.0)
    p.add_argument('--max-tokens', type=int, default=2048)
    p.add_argument('--timeout', type=int, default=300)
    p.add_argument('--passthrough-non-cjk', action='store_true', help='Copy block/page source text directly when it contains no Japanese/CJK characters')
    p.add_argument('--resume', action='store_true')
    args=p.parse_args()

    rows=read_jsonl(args.input_jsonl)
    if args.pages:
        wanted=set()
        for part in args.pages.split(','):
            part=part.strip()
            if not part: continue
            if '-' in part:
                a,b=map(int, part.split('-',1)); wanted.update(range(a,b+1))
            else:
                wanted.add(int(part))
        rows=[r for r in rows if int(r['page']) in wanted]
    if args.limit:
        rows=rows[:args.limit]

    template=load_text(args.prompt)
    glossary=load_text(args.glossary)
    done=load_done(args.output_jsonl) if args.resume else set()

    print(f'translating {len(rows)} records with {args.model}; resume done={len(done)}')
    for index,row in enumerate(rows,1):
        rid=record_id(row)
        if rid in done:
            print(f'[{index}/{len(rows)}] skip {rid}')
            continue
        start=time.time()
        if should_passthrough(row, args.passthrough_non_cjk):
            text=(row.get('source_text') or '').strip()
            status='ok'; error=''; prompt=''
        else:
            prompt=make_prompt(template, glossary, row)
            try:
                text=chat(args.base_url, args.model, prompt, args.temperature, args.max_tokens, args.timeout)
                status='ok'; error=''
            except Exception as exc:
                text=''; status='error'; error=repr(exc)
        elapsed=time.time()-start
        out={
            'record_id': rid,
            'status': status,
            'error': error,
            'model': args.model,
            'base_url': args.base_url,
            'temperature': args.temperature,
            'max_tokens': args.max_tokens,
            'elapsed_sec': round(elapsed,3),
            'passthrough_non_cjk': should_passthrough(row, args.passthrough_non_cjk),
            'record_type': row.get('record_type'),
            'page': row.get('page'),
            'page_label': row.get('page_label'),
            'source_image': row.get('source_image'),
            'source_sha256': row.get('source_sha256'),
            'source_text': row.get('source_text'),
            'translation': text,
        }
        if row.get('record_type') == 'block':
            for k in ['block_id','bbox','reading_order','label']:
                out[k]=row.get(k)
        append_jsonl(args.output_jsonl, out)
        print(f"[{index}/{len(rows)}] {rid} {status} {elapsed:.1f}s src={len(row.get('source_text',''))} out={len(text)}")
        if status != 'ok':
            print(error)


if __name__ == '__main__':
    main()
