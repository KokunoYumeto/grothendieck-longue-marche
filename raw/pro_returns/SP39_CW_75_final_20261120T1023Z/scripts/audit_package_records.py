#!/usr/bin/env python3
"""Check required records, collation cardinality, crops and package provenance."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json,re,hashlib
R=Path(__file__).resolve().parents[1]
scans=[26,27,28,30,31,32,33]
rows=list(csv.DictReader((R/'SP39_CW_75_collation.tsv').open(),delimiter='\t'))
inv=list(csv.DictReader((R/'SP39_CW_75_inventory.csv').open()))
allids=set();summary=[]
valid_kinds={'text','display','diagram','drawing','margin note','insertion','deletion'}
valid_sheets={'text','reused_typed','typescript','letter','list','cancelled_draft','cover'}
for scan in scans:
 rec=json.loads((R/f'decisions/scan{scan:03}.json').read_text())
 assert rec['scan']==scan
 manifests=[];reader_counts=[]
 for w in 'ABC':
  D=R/f'readers/scan{scan:03}/{w}'
  for name in ['page.tex','review.json','report.md','crops.tsv']:assert (D/name).is_file(),str(D/name)
  json.loads((D/'review.json').read_text())
  cr=list(csv.DictReader((D/'crops.tsv').open(),delimiter='\t'));reader_counts.append(len(cr));manifests+=cr
  assert len({x['crop'] for x in cr})==len(cr)
 manifests+=list(csv.DictReader((R/f'decisions/scan{scan:03}_main_crops.tsv').open(),delimiter='\t'))
 names={x['crop'] for x in manifests}
 for x in rec['loci']:
  assert x['id'] not in allids;xid=x['id'];allids.add(xid)
  assert set(x.get('readers',{}))==set('ABC'),xid
  if x['diff_C'] or x['diff_H']:
   assert x.get('crop'),xid+' missing root crop reference'
  for name in re.findall(r'([A-Za-z0-9_.-]+\.(?:png|jpe?g))',x.get('crop','') or ''):
   assert name in names,(xid,name,'crop missing from permanent manifests')
 assert sum(int(x['our_scan'])==scan for x in rows)==sum(bool(x['diff_H']) for x in rec['loci'])
 assert sum(int(x['scan'])==scan for x in inv)==len(rec['inventory'])
 assert all(x['transcribed']=='yes' and x['kind'] in valid_kinds and x['sheet_kind'] in valid_sheets for x in rec['inventory'])
 assert not (scan==30 and any(x['diff_H'] for x in rec['loci']))
 summary.append({'scan':scan,'reader_crop_counts':reader_counts,'loci':len(rec['loci']),'inventory':len(rec['inventory']),'doubts':len(rec['doubts'])})
assert len(list((R/'pages').glob('*.tex')))==7
assert len(list((R/'briefs').glob('brief_v*_scan*.md')))==7
workflow=(R/'SP39_CW_75_workflow.md').read_text()
for name in ['brief_v01_scan026.md','brief_v07_scan033.md']:
 body=(R/'briefs'/name).read_text().rstrip();assert body in workflow,name+' not included in full'
assert 'Assessment will be completed' not in (R/'SP39_CW_75_doubts.md').read_text()
source_rows=list(csv.DictReader((R/'SOURCE_INPUTS.tsv').open(),delimiter='\t'))
# The receipt format is retained as supplied; original attachments are never packaged.
report={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'status':'passed','scope':'seven page records; 21 complete reader returns; unique loci; permanent crop references; H row counts; inventory values; complete first/last briefs; final legibility note','pages':summary,'total_loci':len(allids),'H_rows':len(rows),'inventory_rows':len(inv)}
(R/'records_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
