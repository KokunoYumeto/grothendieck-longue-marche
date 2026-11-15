from pathlib import Path
import csv
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]
NAME='MPL_14_002-044'
COLS=['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed']
def now(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def save_page(scan,tex,elements,sheet_kind='text',observations=''):
    path=ROOT/'pages'/f'{NAME}_14_scan{scan:03}.tex'
    if path.exists(): raise RuntimeError('Page already exists: '+str(path))
    prefix=('\\cotefile{14}\n' if scan==2 else '')+f'\\scanpage{{{scan}}}\n'
    path.write_text(prefix+tex.strip()+'\n',encoding='utf-8')
    inventory=ROOT/f'{NAME}_inventory.csv'
    new=not inventory.exists()
    with inventory.open('a',encoding='utf-8',newline='') as f:
        w=csv.writer(f)
        if new: w.writerow(COLS)
        for i,(kind,pos,first) in enumerate(elements,1):
            w.writerow([14,scan,sheet_kind,f'{scan:03}-{i:02}',kind,pos,first,'yes'])
    if observations:
        with (ROOT/'records/manuscript_observations.md').open('a',encoding='utf-8') as f:
            f.write(f'\n## Scan {scan:03}\n\n'+observations.strip()+'\n')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'14 scan {scan:03} done {now()}\n')
    print(f'Saved scan {scan:03}; {len(elements)} inventory elements; {len(tex)} characters. UTC {now()}')
