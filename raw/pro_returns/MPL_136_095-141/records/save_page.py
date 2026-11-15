from pathlib import Path
from datetime import datetime, timezone
import csv, json, sys
ROOT=Path(__file__).resolve().parents[1]
def save(scan, tex, elements, kind='text', observation=''):
    page=ROOT/'pages'/f'MPL_136_095-141_136_scan{scan:03}.tex'
    if page.exists(): raise ValueError('Page already exists; revise explicitly')
    page.write_text(tex.strip()+'\n')
    with (ROOT/'MPL_136_095-141_inventory.csv').open('a',newline='') as f:
        w=csv.writer(f)
        for i,(k,pos,words) in enumerate(elements,1):w.writerow([136,scan,kind,f'{scan:03}-{i:02}',k,pos,words,'yes'])
    if observation:
        with (ROOT/'records/precontext_observations.md').open('a') as f:f.write(f'\n## Scan {scan}\n\n{observation}\n')
    now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    with (ROOT/'progress.log').open('a') as f:f.write(f'136 scan {scan:03} done {now}\n')
    print(f'scan {scan:03} saved; {len(elements)} inventory elements; {now}')
