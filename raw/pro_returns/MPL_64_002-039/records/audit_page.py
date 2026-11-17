import sys,json,csv,hashlib
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
PREFIX='MPL_64_002-039'
def now(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
x=json.load(sys.stdin); n=x['scan']; p=ROOT/'pages'/f'{PREFIX}_64_scan{n:03d}.tex'
r=ROOT/'records'/f'scan{n:03d}.json'; d=json.loads(r.read_text()); old=p.read_text(); s=x.get('tex',old)
for a,b in x.get('replace',[]):
    if a not in s: raise SystemExit('Missing replacement target: '+a)
    s=s.replace(a,b)
s=s.rstrip()+'\n'; d['tex']=s
for key in ('elements','doubts','notation','abbreviations'):
    d.setdefault(key,[]).extend(x.get('add_'+key,[]))
d.setdefault('audit_notes',[]).append(x.get('note','Visual comparison completed'))
p.write_text(s);r.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
with (ROOT/f'{PREFIX}_inventory.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'])
    for q in sorted((ROOT/'records').glob('scan[0-9][0-9][0-9].json')):
        z=json.loads(q.read_text()); k=z['scan']
        for i,(kind,pos,first) in enumerate(z['elements'],1):
            w.writerow([64,k,z.get('sheet_kind','text'),f'{k:03d}-{i:02d}',kind,pos,first,'yes'])
with (ROOT/f'{PREFIX}_transcription.tex').open('w') as f:
    for q in sorted((ROOT/'pages').glob('*.tex')): f.write(q.read_text()+'\n')
t=now()
with (ROOT/'records'/'audit_changes.jsonl').open('a') as f:
    f.write(json.dumps({'scan':n,'utc':t,'before_sha256':hashlib.sha256(old.encode()).hexdigest(),'after_sha256':hashlib.sha256(s.encode()).hexdigest(),'changes':x},ensure_ascii=False)+'\n')
if x.get('audited',True):
    with (ROOT/'progress.log').open('a') as f:f.write(f'scan {n:03d} audited {t}\n')
print(f'Audited {n:03d}; changed={old!=s}')
