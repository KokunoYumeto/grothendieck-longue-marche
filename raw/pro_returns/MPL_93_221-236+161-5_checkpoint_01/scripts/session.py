from pathlib import Path
from datetime import datetime, timezone
import csv, json
BASE=Path(__file__).resolve().parents[1]
STEM='MPL_93_221-236+161-5'

def utc(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def commit(cote, scan, tex, elements, doubts=(), observations='', sheet_kind='text'):
    cote=str(cote)
    p=BASE/'pages'/f'{STEM}_{cote}_scan{scan:03d}.tex'
    if p.exists(): raise RuntimeError(f'Page already exists: {p}')
    expected=(r'\cotefile{'+cote+'}\n' if (cote,scan) in [('93',221),('161-5',3)] else '')+r'\scanpage{'+str(scan)+'}\n'
    p.write_text(expected+tex.strip()+'\n',encoding='utf-8')
    inv=BASE/f'{STEM}_inventory.csv'
    with inv.open('a',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        if f.tell()==0:w.writerow(['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'])
        for i,(kind,position,first) in enumerate(elements,1):w.writerow([cote,scan,sheet_kind,f'{cote}-{scan:03d}-{i:02d}',kind,position,first,'yes'])
    with (BASE/'records/doubts.jsonl').open('a',encoding='utf-8') as f:
        for d in doubts:
            f.write(json.dumps({'cote':cote,'scan':scan,'line':d[0],'reading':d[1],'alternatives':d[2],'confidence':d[3]},ensure_ascii=False)+'\n')
    if observations:
        with (BASE/'records/reading_observations.md').open('a',encoding='utf-8') as f:f.write(f'\n## {cote} scan {scan:03d}\n\n'+observations.strip()+'\n')
    with (BASE/'progress.log').open('a',encoding='utf-8') as f:f.write(f'{cote} scan {scan:03d} done {utc()}\n')
    refresh_doubts()
    print(f'Saved {cote} scan {scan:03d}; {len(elements)} inventory elements; {len(doubts)} doubt entries. {utc()}')

def refresh_doubts():
    out=['# Notation table\n', (BASE/'records/notation.md').read_text(encoding='utf-8'), '\n# Doubts\n\n| File | Scan | Approximate line / position | Reading | Alternatives / issue | Confidence |\n|---|---:|---|---|---|---|\n']
    p=BASE/'records/doubts.jsonl'
    if p.exists():
        for line in p.read_text(encoding='utf-8').splitlines():
            d=json.loads(line)
            vals=[str(d[k]).replace('|',' / ').replace('\n',' ') for k in ['cote','scan','line','reading','alternatives','confidence']]
            out.append('| '+' | '.join(vals)+' |\n')
    for name,title in [('abbreviations.md','Abbreviations'),('legibility.md','Legibility and limitations')]:
        p=BASE/'records'/name
        if p.exists():out.append('\n# '+title+'\n\n'+p.read_text(encoding='utf-8'))
    (BASE/f'{STEM}_doubts.md').write_text(''.join(out),encoding='utf-8')
