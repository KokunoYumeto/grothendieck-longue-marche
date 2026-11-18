#!/usr/bin/env python3
"""Save one manually read scan and its manually enumerated inventory rows."""
from pathlib import Path
import sys,json,csv,datetime,re
ROOT=Path(__file__).resolve().parents[1]
PREFIX='MPL_29_049-094'
def now(): return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def save(scan, tex, elements, sheet_kind='text', doubts=(), notes=()):
    p=ROOT/'pages'/f'{PREFIX}_29_scan{scan:03}.tex'
    if p.exists(): raise RuntimeError(f'{p.name} exists; use explicit audit edit')
    p.write_text(tex.strip()+'\n',encoding='utf-8')
    inv=ROOT/f'{PREFIX}_inventory.csv'
    fresh=not inv.exists()
    with inv.open('a',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        if fresh: w.writerow(['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'])
        for i,(kind,position,words) in enumerate(elements,1):
            w.writerow([29,scan,sheet_kind,f'{scan:03}-{i:02}',kind,position,words,'yes'])
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'29 scan {scan:03} done {now()}\n')
    for name,items in [('doubts_records.jsonl',doubts),('research_leads.jsonl',notes)]:
        with (ROOT/'work'/name).open('a',encoding='utf-8') as f:
            for item in items: f.write(json.dumps({'scan':scan,**item},ensure_ascii=False)+'\n')
    allpages=sorted((ROOT/'pages').glob('*.tex'))
    (ROOT/f'{PREFIX}_transcription.tex').write_text('\n'.join(x.read_text(encoding='utf-8').rstrip()+'\n' for x in allpages),encoding='utf-8')
    print(f'Saved scan {scan:03}: {len(elements)} inventory elements; {len(allpages)}/42 page files')
if __name__=='__main__':
    request=json.load(sys.stdin)
    save(**request)
