"""Save a manually read page and its contemporaneous inventory (no OCR)."""
import sys, json, csv, re
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'MPL_33_002-049'
d = json.load(sys.stdin)
n = int(d['scan'])
page = ROOT / 'pages' / f'{PREFIX}_33_scan{n:03d}.tex'
if page.exists():
    raise SystemExit(f'Refusing to overwrite completed page {n}')
page.write_text(d['tex'].rstrip()+'\n', encoding='utf-8')
inventory = ROOT / f'{PREFIX}_inventory.csv'
new = not inventory.exists()
with inventory.open('a', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    if new:
        w.writerow(['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'])
    for i, row in enumerate(d['elements'], 1):
        w.writerow(['33',n,d.get('sheet_kind','text'),f'{n:03d}-{i:02d}',*row,'yes'])
(ROOT/'records'/f'scan{n:03d}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
    f.write(f'33 scan {n:03d} done '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+'\n')
pages = sorted((ROOT/'pages').glob('*.tex'))
(ROOT/f'{PREFIX}_transcription.tex').write_text('\\cotefile{33}\n'+ '\n'.join(p.read_text(encoding='utf-8') for p in pages),encoding='utf-8')
print(f'Saved scan {n:03d}: {len(d["elements"])} inventory elements; {len(pages)}/48 pages.')
