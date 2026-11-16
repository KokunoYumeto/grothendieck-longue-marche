from pathlib import Path
from datetime import datetime, timezone
import csv,json,re,sys
ROOT=Path(__file__).resolve().parents[1]
def utc():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def save(scan,tex,elements,doubts=None,observations='',sheet_kind='text'):
    p=ROOT/'pages'/f'MPL_36_002-052_36_scan{scan:03}.tex'
    if p.exists():raise RuntimeError('Page already saved: use explicit revision')
    p.write_text(tex.strip()+'\n',encoding='utf-8')
    with (ROOT/'MPL_36_002-052_inventory.csv').open('a',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        for i,(kind,position,incipit) in enumerate(elements,1):w.writerow([36,scan,sheet_kind,f'{scan:03}.{i:02}',kind,position,incipit,'yes'])
    if doubts:
        with (ROOT/'records/doubts_rows.jsonl').open('a',encoding='utf-8') as f:
            for row in doubts:f.write(json.dumps({'cote':36,'scan':scan,**row},ensure_ascii=False)+'\n')
    if observations:
        with (ROOT/'records/precontext_observations.md').open('a',encoding='utf-8') as f:f.write(f'\n## Scan {scan:03}\n\n'+observations+'\n')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:f.write(f'36 scan {scan:03} done {utc()}\n')
    print(f'Saved scan {scan:03}: {len(tex)} characters; {len(elements)} inventory elements.')
    state=json.loads((ROOT/'records/run_state.json').read_text())
    last=datetime.strptime(state['last_checkpoint_utc'],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
    print('Minutes since last scheduled checkpoint baseline:',round((datetime.now(timezone.utc)-last).total_seconds()/60,1))
