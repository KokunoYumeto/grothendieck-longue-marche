#!/usr/bin/env python3
import sys,json,csv
from pathlib import Path
from datetime import datetime,timezone
root=Path(__file__).resolve().parents[1]
p=json.load(sys.stdin)
n=int(p['scan'])
path=root/'pages'/f'MPL_62_002-050_62_scan{n:03d}.tex'
if path.exists(): raise SystemExit(f'Refusing duplicate initial commit: {path}')
path.write_text(p['tex'].strip()+'\n',encoding='utf-8')
with (root/'MPL_62_002-050_inventory.csv').open('a',encoding='utf-8',newline='') as f:
 w=csv.writer(f)
 for i,e in enumerate(p['elements'],1): w.writerow([62,f'{n:03d}',p.get('sheet_kind','text'),f'{n:03d}.{i:02d}',e[0],e[1],e[2],'yes'])
with (root/'records'/'doubts.jsonl').open('a',encoding='utf-8') as f:
 for d in p.get('doubts',[]): f.write(json.dumps({'cote':62,'scan':n,**d},ensure_ascii=False)+'\n')
if p.get('leads'):
 with (root/'records'/'research_leads.md').open('a',encoding='utf-8') as f: f.write(f'\n## Scan {n:03d}\n\n'+p['leads'].strip()+'\n')
if p.get('notation'):
 with (root/'records'/'notation.md').open('a',encoding='utf-8') as f: f.write(f'\n## Scan {n:03d}\n\n'+p['notation'].strip()+'\n')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root/'progress.log').open('a',encoding='utf-8') as f:
 f.write(f'62 scan {n:03d} whole and both supplied halves visually read; transcription rechecked; element inventory reconciled\n62 scan {n:03d} done {now}\n')
print(f'{path.name}: {len(p["elements"])} inventory elements; saved {now}')
