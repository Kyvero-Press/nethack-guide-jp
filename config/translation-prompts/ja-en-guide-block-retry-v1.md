You are fixing a failed block translation from a Japanese NetHack guidebook.

Return a clean English-only translation of the current OCR/layout block.

Hard rules:
- Use English only.
- Do NOT output Chinese.
- Do NOT output Japanese prose.
- Do NOT output Han, Hiragana, or Katakana characters.
- Do NOT include commentary such as "untranslatable", "OCR result", or explanations about the source.
- If the block is a command label like "Kick 蹴る", output a concise English label like "Kick — kick".
- If the block is already English or romanized NetHack terms, copy or lightly clean it.
- Preserve numbers, ISBNs, AC values, commands, romanized monster names, and item names.
- If OCR is garbled, give the closest literal English phrase and mark uncertainty with [OCR? ...] using English letters only.

Output only the corrected English block translation.
