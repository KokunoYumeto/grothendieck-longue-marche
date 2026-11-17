import sys, json, csv, re
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'MPL_64_002-039'

def now():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

data = json.load(sys.stdin)
n = data['scan']
name = f'{PREFIX}_64_scan{n:03d}.tex'
page = ROOT / 'pages' / name
if page.exists():
    raise SystemExit('Refusing to silently replace an already saved page')
page.write_text(data['tex'].rstrip()+'\n', encoding='utf-8')
(ROOT/'records'/f'scan{n:03d}.json').write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')
with (ROOT/f'{PREFIX}_inventory.csv').open('a', newline='') as f:
    w=csv.writer(f)
    for i, e in enumerate(data['elements'],1):
        kind,position,first = e
        w.writerow([64,n,data.get('sheet_kind','text'),f'{n:03d}-{i:02d}',kind,position,first,'yes'])
with (ROOT/'progress.log').open('a') as f:
    f.write(f'64 scan {n:03d} done {now()}\n')
with (ROOT/f'{PREFIX}_transcription.tex').open('w') as f:
    for p in sorted((ROOT/'pages').glob('*.tex')):
        f.write(p.read_text()+'\n')
print(f'Saved scan {n:03d}: {len(data["tex"])} characters; {len(data["elements"])} inventory rows')
