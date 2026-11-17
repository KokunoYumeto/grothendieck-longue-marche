from pathlib import Path
from datetime import datetime, timezone
import csv
ROOT=Path(__file__).resolve().parents[1]
def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def record(scan, tex, elements, doubts=(), kind='text'):
    p=ROOT/'pages'/f'MPL_136_002-046_136_scan{scan:03}.tex'
    if p.exists(): raise RuntimeError(f'Page already exists: {p}')
    p.write_text(tex.strip()+'\n',encoding='utf-8')
    with (ROOT/'MPL_136_002-046_inventory.csv').open('a',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        for i,(k,pos,words) in enumerate(elements,1):
            w.writerow(['136',f'{scan:03}',kind,f'{scan:03}-{i:02}',k,pos,words,'yes'])
    with (ROOT/'MPL_136_002-046_doubts.md').open('a',encoding='utf-8') as f:
        for line,reading,alternatives,confidence in doubts:
            values=['136',f'{scan:03}',line,reading,alternatives,confidence]
            f.write('| '+' | '.join(str(v).replace('|',' / ').replace('\n',' ') for v in values)+' |\n')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'136 scan {scan:03} done {utc()}\n')
    print(f'Saved scan {scan:03}: {len(tex)} characters, {len(elements)} inventory elements, {len(doubts)} doubt records.')
