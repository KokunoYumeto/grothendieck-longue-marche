#!/usr/bin/env python3
"""Mechanical delivery gate, separate from visual reading and mathematics."""
from pathlib import Path
import csv,json,re,sys
root=Path(__file__).resolve().parents[1]
state=json.loads((root/'run_state.json').read_text())
final='--partial' not in sys.argv
errors=[];warnings=[]
if final and state['completed_scans']!=state['scan_order']: errors.append('Not all 30 scans decided')
expected=[];reader_count=0;crop_count=0
for n in state['completed_scans']:
 d=json.loads((root/f'decisions/scan{n:03d}.json').read_text());expected.append(d['filename'])
 p=root/'pages'/d['filename'];s=p.read_text()
 if 'c_mark_count' in d or int(d['brief_version'].lstrip('v'))>=7:
  marks={f'C{i:03d}' for i in range(1,d.get('c_mark_count',0)+1)}
  if set(d.get('c_mark_coverage',[]))!=marks:errors.append(f'C-mark outcome coverage {n}')
  actual={m for q in d.get('c_doubts',[]) for m in q.get('c_mark_ids',[])}
  if actual!=marks:errors.append(f'C-mark IDs on outcomes {n}')
 if s.count(r'\scanpage{'+str(n)+'}')!=1:errors.append(f'Scan marker {n}')
 if (n==3 and s.count(r'\cotefile{37}')!=1) or (n!=3 and r'\cotefile' in s):errors.append(f'Cote scope {n}')
 for macro in ['ill','struck','add','note','uncertain','supplied']:
  if re.search(r'\\'+macro+r'\{',s):errors.append(f'Foreign witness macro {macro}, scan {n}')
 for k in ['r1','r2','r3']:
  base=root/f'readers/scan{n:03d}/{k}'
  if not (base/'reading.tex').is_file(): errors.append(f'Missing reading {n}/{k}')
  r=json.loads((base/'report.json').read_text());reader_count+=1
  vv=r.get('views',[])
  if len(vv)!=3 or not all(v.get('viewed_once') for v in vv):warnings.append(f'Inspect source-view audit schema {n}/{k}')
  for c in r.get('crops',[]):
   crop_count+=1
   if not (root/c['path']).is_file():errors.append(f'Missing reader crop {n}/{k}: '+c['path'])
 for c in d.get('changes',[]):
  if c.get('diff_h') and d['hua_has']!='text':errors.append(f'H row on description page {n}')
  if set(c.get('readers',{}))!={'r1','r2','r3'}:errors.append(f'Missing three readings {n}: '+c['locus'])
  if not c.get('crop'):warnings.append(f'No crop citation on change {n}: '+c['locus'])
  for q in re.findall(r'(?:readers|crops)/[^\s;]+\.(?:jpg|png)',c.get('crop','')):
   if not (root/q).is_file():errors.append(f'Missing main-cited crop {q}')
 for x in d.get('inventory',[]):
  if x['transcribed']!='yes':errors.append(f'Incomplete inventory scan {n}')
 for x in d.get('notes',[]):
  if x['id'] not in {e['statement_id'] for e in d.get('check_events',[])}:errors.append(f'Note lacks epistemic event {x["id"]}')
actual=sorted(p.name for p in (root/'pages').glob('*.tex'))
if actual!=sorted(expected):errors.append('Page file set differs from decisions')
expected_combined='\n'.join((root/'pages'/name).read_text().rstrip()+'\n' for name in expected)
if (root/'SP45_CW_37_transcription.tex').read_text()!=expected_combined:errors.append('Combined text differs from ordered page files')
with (root/'SP45_CW_37_collation.tsv').open() as f:
 rows=list(csv.DictReader(f,delimiter='\t'))
 if any(int(x['our_scan']) in [9,10,11,12,27,34,35,42,66,67,68] for x in rows):errors.append('Forbidden H description-only collation row')
for name in ['SP45_CW_37_changes.md','SP45_CW_37_collation.tsv','SP45_CW_37_doubts.md','SP45_CW_37_inventory.csv','SP45_CW_37_notes.md','CHECK_EVENTS.tsv','progress.log','SP45_CW_37_workflow.md','PREAMBLE.tex']:
 if not (root/name).is_file():errors.append('Missing deliverable '+name)
if list(root.rglob('*.zip')):errors.append('ZIP nested inside deliverable root')
result={'mode':'final' if final else 'partial','pages':len(expected),'reader_returns':reader_count,'reader_crops':crop_count,'errors':errors,'warnings':warnings,'scope':'Structure and record consistency only; no claim of visual or mathematical verification.'}
(root/'package_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
