"""Write the primary reader's explicit records; no recognition or inferred readings."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv

OUT=Path(__file__).resolve().parents[1]
PREFIX='SP58_CW_156-5'
FIELDS=['id','scan','place','C','H','final','scan_shows','kind','confidence','against_C','against_H','marked_in_H','consequential','pass']

def now(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def append_table(path,fields,rows,delimiter='\t'):
    fresh=not path.exists()
    with path.open('a',newline='') as f:
        w=csv.writer(f,delimiter=delimiter)
        if fresh:w.writerow(fields)
        w.writerows(rows)

def esc(s): return str(s).replace('|','&#124;').replace('\n','<br>')

def refresh():
    p=OUT/'CHANGE_REGISTER.tsv'
    rows=list(csv.DictReader(p.open(),delimiter='\t')) if p.exists() else []
    coll=[]
    for r in rows:
        if r['against_H']=='yes':
            n=int(r['scan']);folder='J156-5-05' if n<42 else 'J156-5-06'
            coll.append([folder,n-1,n,r['place'],r['H'],r['C'],r['final'],r['scan_shows'],r['kind'],r['marked_in_H'],r['confidence']])
    with (OUT/f'{PREFIX}_collation.tsv').open('w',newline='') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence']);w.writerows(coll)
    text=['# Changes decided from the ink','', 'Counts are places, not individual characters. A place differing from both witnesses counts once in each witness column. Pure macro changes and certainty-only changes are excluded. A retained uncertain alternative is counted when the chosen first reading or source state differs. Coordinates are in the original whole JPEG; inspection crops are excluded from the package.','', '| Scan | Against C | Against H | High | Medium | Low |','|---:|---:|---:|---:|---:|---:|']
    for n in range(34,50):
        rs=[r for r in rows if int(r['scan'])==n]
        text.append(f'| {n:03d} | '+ ' | '.join(str(v) for v in [sum(r['against_C']=='yes' for r in rs),sum(r['against_H']=='yes' for r in rs),*[sum(r['confidence']==c for r in rs) for c in ('high','medium','low')]])+' |')
    text.append('| **Total** | '+' | '.join(str(v) for v in [sum(r['against_C']=='yes' for r in rows),sum(r['against_H']=='yes' for r in rows),*[sum(r['confidence']==c for r in rows) for c in ('high','medium','low')]])+' |')
    text += ['', '## Consequential readings', '']
    text += ['- '+r['id']+': '+r['consequential'] for r in rows if r['consequential']]
    for n in range(34,50):
        rs=[r for r in rows if int(r['scan'])==n]
        if not rs and not list((OUT/'pages').glob(f'*scan{n:03d}.tex')):continue
        text += ['',f'## Scan {n:03d} (H page {n-1})','', '| ID / place | C | H | Final | What the scan shows | Confidence |','|---|---|---|---|---|---|']
        for r in rs:text.append('| '+' | '.join(esc(x) for x in [r['id']+' / '+r['place'],r['C'],r['H'],r['final'],r['scan_shows'],r['confidence']])+' |')
        text += ['','Unresolved places: see this scan’s entries in the remaining-doubts table. Certainty-only decisions on C’s marks are recorded in the doubts file.']
    (OUT/f'{PREFIX}_changes.md').write_text('\n'.join(text)+'\n')
    files=sorted((OUT/'pages').glob('*.tex'))
    (OUT/f'{PREFIX}_transcription.tex').write_text(''.join(p.read_text().rstrip()+'\n\n' for p in files))

def commit(scan,tex,changes,inventory,notes,doubts='',hand='',notation='',abbr='',checks=(),pass_name='first'):
    folder='J156-5-05' if scan<42 else 'J156-5-06'
    (OUT/'pages'/f'{folder}_156-5_scan{scan:03d}.tex').write_text(tex.strip()+'\n')
    existing=[]
    reg=OUT/'CHANGE_REGISTER.tsv'
    if reg.exists():existing=list(csv.DictReader(reg.open(),delimiter='\t'))
    offset=sum(int(r['scan'])==scan for r in existing)
    rows=[]
    for i,c in enumerate(changes,offset+1):
        place,C,H,final,shows,kind,confidence,ac,ah,hm,*consequence=c
        rows.append([f'{scan:03d}-{i:02d}',scan,place,C,H,final,shows,kind,confidence,'yes' if ac else 'no','yes' if ah else 'no','yes' if hm else 'no',consequence[0] if consequence else '',pass_name])
    append_table(reg,FIELDS,rows)
    append_table(OUT/f'{PREFIX}_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],[[scan,'text','his hand',f'{scan:03d}-{i:02d}',kind,pos,words,'yes'] for i,(kind,pos,words) in enumerate(inventory,1)],',')
    for suffix,heading,body in [('notes','# Notes from the pages',notes),('doubts','# Notation and doubts',doubts),('hand_log','# Hand log',hand)]:
        p=OUT/f'{PREFIX}_{suffix}.md'
        if not p.exists():p.write_text(heading+'\n')
        with p.open('a') as f:
            f.write(f'\n## Scan {scan:03d}\n\n'+body.strip()+'\n')
            if suffix=='doubts' and notation:f.write('\nNotation observations: '+notation+'\n')
            if suffix=='doubts' and abbr:f.write('\nAbbreviations: '+abbr+'\n')
    if checks:append_table(OUT/'CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],[[a,now(),'GPT-6 Astra Pro; effort not exposed; SP58 second pass',b,c] for a,b,c in checks])
    refresh()
    with (OUT/'progress.log').open('a') as f:f.write(f'scan {scan:03d} done {now()}\n')
    print(f'Scan {scan:03d}: saved page, {len(changes)} substantive difference records, inventory and notes.')
