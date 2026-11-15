"""Apply explicitly supplied visual-audit edits; never reads or recognises images."""
import csv, json, sys
from datetime import datetime, timezone
from pathlib import Path
root=Path(__file__).resolve().parents[1]
d=json.load(sys.stdin); n=int(d['scan'])
record=root/'records'/f'scan{n:03d}.json'
r=json.loads(record.read_text())
p=root/'pages'/f'MPL_33_002-049_33_scan{n:03d}.tex'
s=p.read_text()
for old,new in d.get('replacements',[]):
    if old not in s: raise SystemExit(f'Absent exact old text on scan {n}: {old!r}')
    s=s.replace(old,new)
if 'tex' in d: s=d['tex'].rstrip()+'\n'
p.write_text(s)
r['tex']=s
r.setdefault('audit_observations',[]).extend(d.get('observations',[]))
if 'elements' in d: r['elements']=d['elements']
r['elements'].extend(d.get('add_elements',[]))
for item in d.get('insert_elements',[]): r['elements'].insert(item['index'],item['element'])
for old,new in d.get('element_replacements',[]):
    r['elements']=[[value.replace(old,new) for value in row] for row in r['elements']]
if 'sheet_kind' in d:r['sheet_kind']=d['sheet_kind']
r['audit_time']=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
record.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
with (root/'MPL_33_002-049_inventory.csv').open('w',newline='') as out:
    w=csv.writer(out);w.writerow(['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'])
    for rp in sorted((root/'records').glob('scan[0-9][0-9][0-9].json')):
        q=json.loads(rp.read_text()); m=q['scan']
        for i,row in enumerate(q['elements'],1): w.writerow(['33',m,q.get('sheet_kind','text'),f'{m:03d}-{i:02d}',*row,'yes'])
pages=sorted((root/'pages').glob('*.tex'))
(root/'MPL_33_002-049_transcription.tex').write_text('\\cotefile{33}\n'+'\n'.join(q.read_text() for q in pages))
with (root/'progress.log').open('a') as log:
    log.write(f'scan {n:03d} audited '+r['audit_time']+'\n')
print(f'Visual audit recorded for scan {n:03d}; {len(d.get("replacements",[]))} edit(s).')
