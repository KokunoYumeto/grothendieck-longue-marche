#!/usr/bin/env python3
"""Read-only checks of note coverage and basic Markdown hygiene; no semantic claims."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parent.parent
p = root / "MPL_46_002-048_notes.md"
s = p.read_text(encoding="utf-8")
errors = []
heads = list(re.finditer(r"^### N(\d{2}) — .+$", s, re.M))
ids = [int(m.group(1)) for m in heads]
if ids != list(range(1, 72)):
    errors.append("Research-note IDs do not form N01–N71 in order.")
for i, m in enumerate(heads):
    end = heads[i + 1].start() if i + 1 < len(heads) else s.find("\n| Hua's", m.end())
    block = s[m.end():end if end >= 0 else len(s)]
    meta = block.split("\n\n", 2)[1] if "\n\n" in block else block
    for field in ("**Kind:**", "**File/scan:**", "**State:**"):
        if field not in meta:
            errors.append(f"N{m.group(1)} missing {field}")
    if "own" in meta.lower() and "Confidence:" not in block:
        errors.append(f"N{m.group(1)} labelled own work without explicit confidence.")
for number, line in enumerate(s.splitlines(), 1):
    if any(ord(c) < 32 and c != "\t" for c in line):
        errors.append(f"Control character on line {number}.")
    if len(re.findall(r"(?<!\\)\$", line)) % 2:
        errors.append(f"Unpaired inline math dollar on line {number}.")
for number in re.findall(r"\bN(\d{2})\b", s):
    if int(number) not in ids:
        errors.append(f"Reference to absent note N{number}.")
print(json.dumps({
    "notes": len(ids),
    "words": len(s.split()),
    "errors": errors,
    "scope": "Coverage and basic Markdown hygiene only; no assertion of mathematical or paleographic correctness."
}, ensure_ascii=False, indent=2))
raise SystemExit(bool(errors))
