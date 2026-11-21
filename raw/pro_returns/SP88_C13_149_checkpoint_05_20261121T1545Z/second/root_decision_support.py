"""Write explicit, already visually adjudicated root decisions; decide nothing.

Each supplied evidence entry is a root decision to retain the first reading,
unless an explicit final_readings override is supplied. The required set of
boxes must match exactly. Frozen first/second data are never modified.
"""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
def write_decisions(scan,evidence,medium=(),low=(),final_readings=None,extra=None,crop_overrides=None):
 final_readings=final_readings or {};extra=extra or {};crop_overrides=crop_overrides or {}
 stem=f'149_scan{scan:03d}';s=ROOT/'second';comp=json.loads((s/f'{stem}_comparison.json').read_text());data=json.loads((ROOT/'review/accepted'/f'{stem}.json').read_text());boxes={x['box']:x for x in data['audit_boxes']}
 required=[x['box'] for x in comp if x['different']]
 assert set(evidence)==set(required),(set(evidence)^set(required))
 rows=[]
 for c in comp:
  if not c['different']:continue
  b=c['box'];final=final_readings.get(b,c['first']);row={'box':b,'root_visually_inspected':True,'final':final,'evidence':evidence[b],'crop':crop_overrides.get(b,f'crops/{stem}_second_{b}.png'),'bbox':boxes[b]['bbox'],'confidence':'low' if b in low else ('medium' if b in medium else 'high'),'changed':final!=c['first']};row.update(extra.get(b,{}));rows.append(row)
 p=s/f'{stem}_adjudications.json'
 if p.exists():raise ValueError('Do not overwrite completed adjudications')
 p.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
def sync_tracking(scan):
 p=ROOT/'review/audit_assignments.json';d=json.loads(p.read_text());a=next(x for x in d['assignments'] if x['scan']==scan);a['status']='audited';a['audit_counts']=json.loads((ROOT/f'review/accepted/149_scan{scan:03d}.json').read_text())['audited'];p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
