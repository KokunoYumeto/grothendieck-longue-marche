from pathlib import Path
from datetime import datetime, timezone
import csv, json
ROOT=Path(__file__).resolve().parents[1]
PREFIX='MPL_91_059-098'
def utc(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def save(scan, body, elements, doubts=(), remarks='', sheet='text'):
    path=ROOT/'pages'/f'{PREFIX}_91_scan{scan:03d}.tex'
    if path.exists(): raise RuntimeError('Page already exists; edit explicitly')
    text=('\\cotefile{91}\n' if scan==59 else '')+f'\\scanpage{{{scan}}}\n'+body.strip()+'\n'
    path.write_text(text,encoding='utf-8')
    inv=ROOT/f'{PREFIX}_inventory.csv'
    exists=inv.exists()
    with inv.open('a',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        if not exists:w.writerow(['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'])
        for i,(kind,pos,first) in enumerate(elements,1):w.writerow([91,scan,sheet,i,kind,pos,first,'yes'])
    with (ROOT/'records/doubts.jsonl').open('a',encoding='utf-8') as f:
        for line,reading,alt,confidence in doubts:f.write(json.dumps(dict(cote=91,scan=scan,line=line,reading=reading,alternatives=alt,confidence=confidence),ensure_ascii=False)+'\n')
    if remarks:
        with (ROOT/'records/precontext_observations.md').open('a',encoding='utf-8') as f:f.write(f'\n## Scan {scan}\n\n{remarks}\n')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:f.write(f'91 scan {scan:03d} done {utc()}\n')
    print(f'Wrote scan {scan:03d}: {len(elements)} inventory elements.')
