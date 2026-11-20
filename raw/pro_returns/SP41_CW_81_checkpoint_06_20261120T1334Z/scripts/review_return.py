"""Print bounded portions of a reader return for actual main-reader review.

This is a display helper only: no reading, alignment or decision is inferred.
"""
from pathlib import Path
import argparse, json

p = argparse.ArgumentParser()
p.add_argument('scan', type=int)
p.add_argument('reader', type=int)
p.add_argument('part', choices=['text', 'findings', 'inventory', 'rest'])
p.add_argument('--start', type=int, default=1)
p.add_argument('--count', type=int, default=12)
a = p.parse_args()
w = Path(__file__).resolve().parents[1]
base = w / f'readers/scan{a.scan:03d}/R{a.reader}'
if a.part == 'text':
    print((base / 'reading.tex').read_text())
else:
    d = json.loads((base / 'return.json').read_text())
    if a.part in ('findings', 'inventory'):
        values = d[a.part]
        end = min(a.start - 1 + a.count, len(values))
        print(f'{a.part}: entries {a.start}–{end} of {len(values)}')
        for i in range(a.start - 1, end):
            print(i + 1, json.dumps(values[i], ensure_ascii=False))
    else:
        for k, v in d.items():
            if k not in ('findings', 'inventory'):
                print(k, json.dumps(v, ensure_ascii=False))
