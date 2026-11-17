"""Save one manually read page, its manually supplied inventory and doubts."""
from pathlib import Path
from datetime import datetime, timezone
import csv, json, sys
ROOT=Path(__file__).resolve().parents[1]
def now(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def record(scan,tex,elements,doubts=(),sheet_kind='text',notation=()):
    path=ROOT/'pages'/f'MPL_137_002-044_137_scan{scan:03}.tex'
    if path.exists(): raise RuntimeError('Page exists; review explicitly, do not duplicate completion.')
    path.write_text(tex.rstrip()+'\n',encoding='utf-8')
    with (ROOT/'MPL_137_002-044_inventory.csv').open('a',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        for n,e in enumerate(elements,1):
            kind,position,words=e
            w.writerow([137,scan,sheet_kind,f'{scan:03}-{n:02}',kind,position,words,'yes'])
    rec={'scan':scan,'sheet_kind':sheet_kind,'elements':elements,'doubts':doubts,'notation':notation}
    (ROOT/'records'/f'{scan:03}.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
    with (ROOT/'progress.log').open('a') as f:
        f.write(f'137 scan {scan:03} done {now()}\n')
    combine()
    print(f'Saved scan {scan:03}: {len(elements)} inventory elements, {len(doubts)} doubt entries.')
def combine():
    pages=sorted((ROOT/'pages').glob('*.tex'))
    (ROOT/'MPL_137_002-044_transcription.tex').write_text('\n'.join(p.read_text() for p in pages),encoding='utf-8')
    recs=[json.loads(p.read_text()) for p in sorted((ROOT/'records').glob('*.json'))]
    lines=['# Notation table and doubts','', '## Notation table','', '| Visible sign / convention | LaTeX | Evidence / cautions |','|---|---|---|']
    for r in recs:
        for n in r.get('notation',[]): lines.append('| '+' | '.join(str(v).replace('|',' / ') for v in n)+' |')
    lines+=['','## Doubts','', '| File | Scan | Approximate line / place | Reading | Alternatives | Confidence |','|---|---|---|---|---|---|']
    for r in recs:
        for d in r.get('doubts',[]): lines.append('| 137 | '+str(r['scan'])+' | '+' | '.join(str(v).replace('|',' / ') for v in d)+' |')
    lines+=['','The page files retain in-place uncertainty markers. These tables do not resolve them.']
    (ROOT/'MPL_137_002-044_doubts.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
if __name__=='__main__': combine()
