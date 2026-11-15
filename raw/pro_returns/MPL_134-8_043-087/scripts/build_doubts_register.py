#!/usr/bin/env python3
"""Build the principal reader's register from exact extracted macro arguments.

The header and confidence policy are editorial decisions by the principal
reader. This script does not read images or context, infer text, or edit TeX.
"""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent.parent
data = json.loads((ROOT / 'records/doubts_extracted.json').read_text())
assert not data['errors']
for source in data['sources']:
    assert hashlib.sha256(Path(source['file']).read_bytes()).hexdigest() == source['sha256'], source['file']


def split_alternative(raw):
    depth = 0
    i = 0
    while i < len(raw):
        char = raw[i]
        if char == '\\':
            i += 1
            if i < len(raw) and raw[i].isalpha():
                while i < len(raw) and raw[i].isalpha():
                    i += 1
                continue
            i += 1
            continue
        if char == '{':
            depth += 1
        elif char == '}':
            depth -= 1
        elif char == '|' and depth == 0:
            return raw[:i], raw[i + 1:]
        i += 1
    return raw, None


def cell(raw):
    raw = raw.replace('\r\n', '\\n').replace('\r', '\\n').replace('\n', '\\n').replace('|', '&#124;')
    runs = [len(x) for x in re.findall(r'`+', raw)]
    fence = '`' * (max(runs, default=0) + 1)
    return fence + ' ' + raw + ' ' + fence


out = [(ROOT / 'records/doubts_editorial_header.md').read_text()]
out.append('| File | Scan | Approximate line / exact TeX column | Preferred reading | Alternative | Confidence |\n')
out.append('|---|---:|---|---|---|---|\n')
counts = {'medium': 0, 'low': 0}
for record in data['records']:
    raw = record['raw_argument']
    reading, alternative = split_alternative(raw)
    confidence = 'low' if alternative is not None else 'medium'
    # The principal reader flags these residual single readings as especially
    # insecure after the page audits. Their raw reading is never changed here.
    if record['scan'] in (57, 59, 73, 74) or record['macro'] == 'illegible':
        confidence = 'low'
    if record['scan'] == 85 and reading in ('u', '-', 'simples'):
        confidence = 'low'
    if '*' in reading and len(reading) > 30:
        confidence = 'low'
    if record['scan'] in (61, 63, 65, 67, 74, 75, 77, 79, 81, 86) and any(s in raw for s in ('\\flat', '\\sharp')):
        confidence = 'low'
    counts[confidence] += 1
    loc = record['location']
    alt = cell(alternative) if alternative is not None else 'No secure second reading'
    if record['macro'] == 'illegible':
        reading = '\\illegible{' + raw + '}'
    out.append(f"| 134-8 | {record['scan']:03d} | TeX line {loc['line']}, column {loc['column']} | {cell(reading)} | {alt} | {confidence} |\n")
out.append(f"\nRegister: {len(data['records'])} occurrences across {len(data['sources'])} page files; {counts['medium']} medium, {counts['low']} low. Raw source arguments and exact byte spans are preserved separately.\n")
target = ROOT / 'MPL_134-8_043-087_doubts.md'
target.write_text(''.join(out))
print(f'Wrote {target}: {len(data["records"])} exact doubt occurrences.')
