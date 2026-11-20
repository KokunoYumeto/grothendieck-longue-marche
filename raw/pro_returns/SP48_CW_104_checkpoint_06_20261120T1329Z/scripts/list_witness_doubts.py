"""Index uncertainty macros in the current text packet, without reading images.

This is a clerical coverage aid. It does not decide or align any manuscript
reading, and it is run only for the page currently being read.
"""
from pathlib import Path
import argparse
import json
import re

p = argparse.ArgumentParser()
p.add_argument('scan', type=int)
args = p.parse_args()
out = Path(__file__).resolve().parents[1]
packet = out.parent / f'reader_inputs/scan{args.scan:03d}'
result = {'scan': args.scan, 'C': [], 'H': []}
for witness, names in [('C', 'unsure|illegible'), ('H', 'uncertain|ill')]:
    text = (packet / f'{witness}.tex').read_text()
    for match in re.finditer(r'\\(' + names + r')\{', text):
        start = match.end()
        end = start
        depth = 1
        while end < len(text) and depth:
            if text[end] == '\\':
                end += 2
                continue
            if text[end] == '{':
                depth += 1
            elif text[end] == '}':
                depth -= 1
            end += 1
        if depth:
            raise ValueError(f'Unbalanced witness macro at {witness}:{start}')
        line_start = text.rfind('\n', 0, match.start()) + 1
        line_end = text.find('\n', end)
        if line_end < 0:
            line_end = len(text)
        result[witness].append({
            'id': f'{witness}{len(result[witness]) + 1:02d}',
            'line': text.count('\n', 0, match.start()) + 1,
            'macro': match.group(1),
            'reading': text[start:end-1],
            'line_context': text[line_start:line_end],
        })
target = out / f'records/scan{args.scan:03d}/witness_doubts.json'
target.parent.mkdir(parents=True, exist_ok=True)
target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'scan': args.scan, 'C': len(result['C']), 'H': len(result['H'])}))
