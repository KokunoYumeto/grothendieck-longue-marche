from pathlib import Path
from datetime import datetime, timezone
import json, csv

ROOT=Path('/workspace/scratch/b8e2c31cadf4/work')
BASE='MPL_36_053-085+39'
def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def log(s):
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f: f.write(s+'\n')
def save(cote,scan,tex,elements,sheet_kind='text',leads='',doubts=None):
    name=f'{BASE}_{cote}_scan{scan:03d}.tex'
    path=ROOT/'pages'/name
    if path.exists(): raise RuntimeError('Page already saved; revise explicitly before freeze')
    path.write_text(tex.strip()+'\n',encoding='utf-8')
    record={'cote':cote,'scan':scan,'sheet_kind':sheet_kind,'elements':elements,'doubts':doubts or [],'leads':leads}
    (ROOT/'records'/f'{cote}_{scan:03d}.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    with (ROOT/(BASE+'_inventory.csv')).open('a',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        for n,(kind,pos,words) in enumerate(elements,1): w.writerow([cote,scan,sheet_kind,n,kind,pos,words,'yes'])
    if leads:
        with (ROOT/'research_leads.md').open('a',encoding='utf-8') as f: f.write(f'\n## {cote}, scan {scan:03d}\n\n{leads}\n')
    combined='\n'.join(p.read_text(encoding='utf-8').rstrip()+'\n' for p in sorted((ROOT/'pages').glob('*.tex')))
    (ROOT/(BASE+'_transcription.tex')).write_text(combined,encoding='utf-8')
    log(f'{cote} scan {scan:03d} done {utc()}')
    import runpy
    runpy.run_path(str(ROOT/'scripts'/'build_doubts.py'),run_name='__main__')
    start=datetime.strptime((ROOT/'progress.log').read_text().splitlines()[0],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
    print(f'Saved {name}; {len(list((ROOT/"pages").glob("*.tex")))} pages; elapsed {(datetime.now(timezone.utc)-start).total_seconds()/60:.1f} minutes')
