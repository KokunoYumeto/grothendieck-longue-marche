from pathlib import Path
from datetime import datetime, timezone
import csv

ROOT=Path(__file__).resolve().parents[1]
PREFIX='MPL_108+112+113+114+115'

def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def save_page(cote,scan,tex,elements,sheet_kind='text',doubts=(),notes=''):
    p=ROOT/'pages'/f'{PREFIX}_{cote}_scan{scan:03}.tex'
    if p.exists():
        raise RuntimeError(f'Page already recorded: {p}')
    p.write_text(tex.strip()+'\n',encoding='utf-8')
    inv=ROOT/f'{PREFIX}_inventory.csv'
    new=not inv.exists()
    with inv.open('a',encoding='utf-8',newline='') as f:
        w=csv.writer(f)
        if new:
            w.writerow(['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'])
        for i,(kind,pos,words) in enumerate(elements,1):
            w.writerow([cote,scan,sheet_kind,i,kind,pos,words,'yes'])
    with (ROOT/'work_records/doubts_rows.md').open('a',encoding='utf-8') as f:
        for line,reading,alternatives,confidence in doubts:
            vals=[str(cote),f'{scan:03}',line,reading,alternatives,confidence]
            f.write('| '+' | '.join(v.replace('|',' / ') for v in vals)+' |\n')
    if notes:
        with (ROOT/'work_records/precontext_observations.md').open('a',encoding='utf-8') as f:
            f.write(f'\n## {cote} scan {scan:03}\n\n{notes.strip()}\n')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'{cote} scan {scan:03} done {utc()}\n')
    print(f'Saved {cote} scan {scan:03}: {len(elements)} inventory elements.')
