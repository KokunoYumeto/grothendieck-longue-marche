#!/usr/bin/env python3
"""Merge check events using the prompt's exact event categories.

The source TSVs preserve their original wording.  When a descriptive source
activity is categorized, that wording is retained verbatim in the outcome.
Coverage and compilation events do not certify a mathematical assertion.
"""
from pathlib import Path
import csv
p=Path(__file__).resolve().parents[1]
h=['statement_id','date','who','type','outcome'];a=[]
allowed={
 'targeted proof check', 'independent re-proof',
 'computation or formal certificate', 'used and rechecked in this run',
 'carried as background without fault found',
}
def categorize(r):
 original=r.get('type','')
 if original in allowed:
  return r
 if original.startswith('refuted,'):
  if original=="refuted, with the refined statement's id":
   r['type']='refuted, with the refined statement P.3'
  return r
 low=original.lower()
 if low in {'scope record','historical audit boundary'}:
  category='carried as background without fault found'
 elif low in {'syntax verification','format check','program executed',
              'computation','executable certificate','exact executable verification',
              'independent certificate rerun'} or (
              ('computation' in low or 'finite computation' in low)
              and not any(w in low for w in ['proof','review','audit'])):
  category='computation or formal certificate'
 elif low in {'source opened','external sources opened','source verification',
              'primary source verification','primary-source verification',
              'primary-source check','independent primary-source check',
              'source audit','historical closure'}:
  category='used and rechecked in this run'
 elif ('re-proof' in low or 'second re-proof' in low
       or low in {'independent proof','new independent proof',
                  'independent elementary proof'}):
  category='independent re-proof'
 else:
  # A review, scope/parameter audit, or construction check is not promoted
  # to an independent reconstruction merely because its author says full.
  category='targeted proof check'
 r['type']=category
 r['outcome']='Original recorded activity: '+original+'. '+r.get('outcome','')
 if original in {'syntax verification','format check'}:
  r['outcome']+=' This event certifies document processing only, not the mathematical claim.'
 return r
for f in sorted((p/'notes').glob('*[Cc][Hh][Ee][Cc][Kk]_[Ee][Vv][Ee][Nn][Tt][Ss].tsv')):
 with f.open() as t:
  a.extend(categorize(dict(r)) for r in csv.DictReader(t,delimiter='\t'))
with (p/'CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=h,delimiter='\t');w.writeheader();w.writerows({k:r.get(k,'') for k in h} for r in a)
known={r['statement_id'] for r in a}
missing=[r['id'] for r in csv.DictReader((p/'SECTION_GHOSTS_results.csv').open()) if r['id'] not in known]
print('Recorded check events:',len(a));print('Results without events:',missing)
assert not missing
assert all(r['type'] in allowed or r['type'].startswith('refuted,') for r in a)
print('PASS: event coverage, not proof certification.')
