"""Normalize type labels only, preserving each explicit refinement id in outcome."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json,re
O=Path(__file__).resolve().parents[1];p=O/'CHECK_EVENTS.tsv'
with p.open() as f:reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
canonical="refuted, with the refined statement's id"
changed=[]
for i,r in enumerate(rows):
 if r['type'].startswith('refuted') and r['type']!=canonical:
  m=re.search(r'(\d{2,3}-\d{3}-[A-Za-z0-9-]+)$',r['type']);assert m,r
  old=r['type'];r['type']=canonical;r['outcome']='Refined statement '+m[1]+': '+r['outcome']
  changed.append(dict(row=i+2,statement_id=r['statement_id'],date=r['date'],old_type=old,new_type=canonical,refined_statement_id=m[1]))
if changed:
 with p.open('w') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
 history=O/'decisions/check_event_type_normalization.json'
 data=json.loads(history.read_text()) if history.exists() else []
 now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
 data.append(dict(date=now,changes=changed));history.write_text(json.dumps(data,indent=2)+'\n')
 with (O/'progress.log').open('a') as f:f.write('check-event type-label normalization '+now+'; '+str(len(changed))+' refuted rows use the exact requested type label; original refinement ids retained in outcome; no event or mathematical claim changed.\n')
print(json.dumps({'normalized_type_labels':len(changed),'events':len(rows)}))
