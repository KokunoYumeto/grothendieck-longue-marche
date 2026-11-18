from pathlib import Path
from datetime import datetime,timezone
import csv,json,re
ROOT=Path(__file__).resolve().parents[1]
def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def save(scan,tex,elements,doubts=(),notations=(),abbreviations=(),leads=(),sheet_kind='text'):
    path=ROOT/'pages'/f'MPL_67_053-101_67_scan{scan:03d}.tex'
    if path.exists(): raise FileExistsError(path)
    path.write_text(tex.strip()+'\n',encoding='utf-8')
    with (ROOT/'MPL_67_053-101_inventory.csv').open('a',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        for i,(kind,pos,words) in enumerate(elements,1):
            w.writerow([67,scan,sheet_kind,f'{scan:03d}-{i:02d}',kind,pos,words,'yes'])
    rec={'scan':scan,'doubts':doubts,'notations':notations,'abbreviations':abbreviations}
    with (ROOT/'records/readings.jsonl').open('a',encoding='utf-8') as f: f.write(json.dumps(rec,ensure_ascii=False)+'\n')
    with (ROOT/'records/research_leads.md').open('a',encoding='utf-8') as f:
        for x in leads: f.write(f'\n- Scan {scan}: {x}\n')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f: f.write(f'67 scan {scan:03d} done {utc()}\n')
    print(f'Saved scan {scan:03d}: {len(tex)} characters, {len(elements)} inventory elements at {utc()}')
