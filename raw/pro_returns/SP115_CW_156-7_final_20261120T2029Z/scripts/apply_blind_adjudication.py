#!/usr/bin/env python3
"""Apply explicit root decisions after direct inspection of every differing blind crop.
This program never decides a reading; all decisions and evidence are supplied in JSON.
"""
from pathlib import Path
import csv,json,hashlib,datetime,sys
R=Path(__file__).resolve().parents[1]
n=int(sys.argv[1]);stem=f'H156-01_156-7_scan{n:03d}'
cfg=json.loads((R/'second'/f'{stem}_decisions.json').read_text())
cmp=json.loads((R/'second'/f'{stem}_comparison.json').read_text())
fp=R/'second'/f'{stem}_adjudication.tsv'
if fp.exists():raise SystemExit('Refusing to overwrite completed blind adjudication')
need={x['box'] for x in cmp['rows'] if x['different']}
if set(cfg['boxes'])!=need:raise SystemExit('Decision coverage mismatch: '+str(need-set(cfg['boxes']))+' extra '+str(set(cfg['boxes'])-need))
page=R/'pages'/f'{stem}.tex';text=page.read_text();before=hashlib.sha256(page.read_bytes()).hexdigest()
for p in cfg.get('patches',[]):
 hits=text.count(p['old'])
 if hits!=p.get('count',1):raise SystemExit(f"Patch count {hits}, expected {p.get('count',1)}: {p['old']!r}")
 text=text.replace(p['old'],p['new'])
dp=R/'review'/f'scan{n:03d}_final.json';d=json.loads(dp.read_text())
for id,updates in cfg.get('change_updates',{}).items():
 hits=[x for x in d['changes'] if x['id']==id]
 if len(hits)!=1:raise SystemExit('Missing/duplicate change id '+id)
 hits[0].update(updates)
d['changes'].extend(cfg.get('new_changes',[]))
d['doubts']=[x for x in d['doubts'] if x['place'] not in cfg.get('remove_doubt_places',[])]
d['doubts'].extend(cfg.get('new_doubts',[]))
rows=[];audit_changes=[];changed=set()
for x in cmp['rows']:
 if not x['different']:continue
 b=cfg['boxes'][x['box']];crop=R/b['crop']
 if not crop.exists():raise SystemExit('Missing inspected crop '+str(crop))
 final=x['first']
 for p in cfg.get('patches',[]):final=final.replace(p['old'],p['new'])
 final=b.get('final',final)
 ids=b.get('changed_place_ids',[]);changed.update(ids)
 evidence=b['evidence']+' Crop: '+b['crop']+'; original box '+str(b['box_coords'])+'.'
 rows.append(dict(box=x['box'],first=x['first'],second=x['second'],final=final,decision=b['decision'],changed_place_ids=';'.join(ids),crop=b['crop'],scan_shows=evidence))
 if ids:audit_changes.append(dict(box=x['box'],first=x['first'],second=x['second'],final=final,evidence=evidence+' Change-place IDs: '+', '.join(ids)+'.'))
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
d['audit_changes']=audit_changes
d['blind_audit']={'completed_utc':now,'boxes_read':cmp['boxes'],'different_boxes':cmp['different_boxes'],'changed_places':len(changed),'changed_place_ids':sorted(changed),'reader':cfg['reader'],'root_checked_every_difference_on_new_blind_crop':True,'initial_page_sha256':before,'second_tsv_sha256':hashlib.sha256((R/'second'/f'{stem}_second.tsv').read_bytes()).hexdigest()}
page.write_text(text)
dp.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
with fp.open('x',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['box','first','second','final','decision','changed_place_ids','crop','scan_shows'],delimiter='\t');w.writeheader();w.writerows(rows)
with (R/'progress.log').open('a') as f:f.write(f'scan {n:03d} audited {now}: {cmp["boxes"]} boxes read, {cmp["different_boxes"]} differences, {len(changed)} changed\n')
print(d['blind_audit'])
