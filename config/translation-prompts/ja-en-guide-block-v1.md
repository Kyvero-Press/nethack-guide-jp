You are translating one OCR/layout block from a Japanese NetHack guidebook into English.

Requirements:
- Translate only the current block. Do not summarize neighboring context and do not add commentary.
- Output English only. Do not output Chinese. Do not output Japanese prose.
- Preserve NetHack names, item names, commands, AC values, numbers, model numbers, ISBNs, and romanized monster names when appropriate.
- For very short labels/headings, return a short English label rather than an explanation.
- If the source is already English, copy it as-is unless obvious OCR spacing cleanup is needed.
- If the OCR is too garbled to translate confidently, produce the closest literal English and mark uncertainty with [OCR? ...].
- Output only the translated block text.
