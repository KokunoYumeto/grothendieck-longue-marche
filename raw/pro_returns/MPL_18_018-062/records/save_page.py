from pathlib import Path
from datetime import datetime,timezone
import csv,json,re
BASE=Path(__file__).resolve().parents[1]
def save_page(n,text,items,doubts=(),observations=''):
    p=BASE/'pages'/f'MPL_18_018-062_18_scan{n:03d}.tex'
    if p.exists(): raise RuntimeError('Page already saved')
    prefix=('\\cotefile{18}\n' if n==18 else '')+f'\\scanpage{{{n}}}\n'
    p.write_text(prefix+text.strip()+'\n',encoding='utf-8')
    with (BASE/'MPL_18_018-062_inventory.csv').open('a',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        for i,(sheet,kind,pos,words) in enumerate(items,1):
            w.writerow([18,n,sheet,i,kind,pos,words,'yes'])
    with (BASE/'records/doubts.jsonl').open('a',encoding='utf-8') as f:
        for d in doubts:f.write(json.dumps({'cote':18,'scan':n,'position':d[0],'reading':d[1],'alternatives':d[2],'confidence':d[3]},ensure_ascii=False)+'\n')
    if observations:
        with (BASE/'records/reading_observations.md').open('a',encoding='utf-8') as f:f.write(f'\n## Scan {n}\n\n'+observations+'\n')
    now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    with (BASE/'progress.log').open('a',encoding='utf-8') as f:f.write(f'18 scan {n:03d} done {now}\n')
    print(f'Saved scan {n:03d}: {len(text)} characters, {len(items)} inventory elements; {now}')
