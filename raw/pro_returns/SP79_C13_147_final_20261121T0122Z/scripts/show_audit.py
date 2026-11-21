"""Print committed and blind readings with numbered token operations for review.

This script makes no reading decisions and changes no source files.
"""
from pathlib import Path
import csv
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
n = int(sys.argv[1])
stem = f'147_scan{n:03d}'
comparison = json.loads((ROOT / 'second' / f'{stem}_comparison.json').read_text())
requested = set(sys.argv[2:])
with (ROOT / 'second' / f'{stem}_boxes.tsv').open() as f:
    boxes = {r['box']: r for r in csv.DictReader(f, delimiter='\t')}
print(json.dumps({k: comparison[k] for k in ('scan', 'boxes', 'differences')}))
for item in comparison['items']:
    if requested and item['box'] not in requested:
        continue
    print('\nBOX', json.dumps(boxes[item['box']], ensure_ascii=False))
    print('FIRST', item['first'])
    print('SECOND', item['second'])
    for i, op in enumerate(item['token_differences']):
        print('OP', i, op['operation'],
              json.dumps(op['first_tokens'], ensure_ascii=False), '=>',
              json.dumps(op['second_tokens'], ensure_ascii=False))
