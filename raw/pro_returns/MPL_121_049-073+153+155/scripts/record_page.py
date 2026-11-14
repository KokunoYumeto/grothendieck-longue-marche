#!/usr/bin/env python3
"""Record a visually transcribed page; no OCR or image processing is performed."""
import csv, json, re, sys
from pathlib import Path
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]
PREFIX='MPL_121_049-073+153+155'
def utc(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def record(data):
    c,n=str(data['cote']),int(data['scan'])
    path=ROOT/'pages'/f'{PREFIX}_{c}_scan{n:03d}.tex'
    if path.exists(): raise RuntimeError(f'Already recorded: {path.name}')
    path.write_text(data['tex'].rstrip()+'\n',encoding='utf-8')
    inv=ROOT/f'{PREFIX}_inventory.csv'
    new=not inv.exists()
    with inv.open('a',encoding='utf-8',newline='') as f:
        w=csv.writer(f)
        if new: w.writerow(['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'])
        for i,row in enumerate(data['inventory'],1):
            w.writerow([c,n,data.get('sheet_kind','text'),f'{c}-{n:03d}-{i:02d}',*row,'yes'])
    with (ROOT/'doubt_records.jsonl').open('a',encoding='utf-8') as f:
        for item in data.get('doubts',[]):
            f.write(json.dumps(dict(cote=c,scan=n,**item),ensure_ascii=False)+'\n')
    with (ROOT/'research_seeds.md').open('a',encoding='utf-8') as f:
        if data.get('seeds'): f.write(f'\n## {c} scan {n:03d}\n'+data['seeds']+'\n')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'{c} scan {n:03d} done {utc()}\n')
    combine()
    print(f'{c} scan {n:03d} recorded; {len(list((ROOT/"pages").glob("*.tex")))} pages total.')
def combine():
    paths=sorted((ROOT/'pages').glob('*.tex'),key=lambda p:tuple(map(int,re.search(r'_(\d+)_scan(\d+)',p.name).groups())))
    (ROOT/f'{PREFIX}_transcription.tex').write_text('\n'.join(p.read_text(encoding='utf-8') for p in paths),encoding='utf-8')
if __name__=='__main__': record(json.load(sys.stdin))
