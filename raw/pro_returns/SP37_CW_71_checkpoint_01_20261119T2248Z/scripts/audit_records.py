#!/usr/bin/env python3
"""Validate documentary completeness, without recognizing images or judging readings."""
from pathlib import Path
import json,csv,re
root=Path(__file__).resolve().parents[1]
records=[json.loads(x.read_text()) for x in sorted((root/'decisions').glob('scan*.json'))]
errors=[];rows=[]
allowed={'misread word','misread symbol or index','omission','text not on the page','deletion state','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
htext={36,37,38,47,48}
for r in records:
 n=r['scan']; f=root/'pages'/r['page_file'];t=f.read_text()
 if t.count('\\scanpage{'+str(n)+'}')!=1:errors.append(f'{n}: scan marker')
 ids=[x['id'] for x in r['issues']]
 if len(ids)!=len(set(ids)):errors.append(f'{n}: duplicate issue IDs')
 for x in r['issues']:
  if x.get('against_H'):
   if n not in htext:errors.append(f'{n}: H row on desc/nothing page')
   if x.get('kind') not in allowed:errors.append(f'{n}: invalid H kind {x.get("kind")}')
  if x.get('confidence') not in {'high','medium','low'}:errors.append(f'{n}: confidence')
  if not x.get('evidence'):errors.append(f'{n}: empty stroke evidence')
 for k in ['R1','R2','R3']:
  rr=root/f'readers/scan{n:03d}/{k}'
  if not (rr/'report.json').is_file():errors.append(f'{n}: missing {k} report')
 for x in r['inventory']:
  if x['transcribed']!='yes':errors.append(f'{n}: inventory incomplete')
 if not r.get('notes'):errors.append(f'{n}: missing notes')
 rows.append({'scan':n,'issues':len(ids),'inventory':len(r['inventory']),'remaining_doubts':len(r['doubts']),'C_changes':sum(bool(x.get('against_C')) for x in r['issues']),'H_changes':sum(bool(x.get('against_H')) for x in r['issues'])})
report={'scans':[r['scan'] for r in records],'complete_13_pages':len(records)==13 and [r['scan'] for r in records]==list(range(36,49)),'pages':rows,'errors':errors,'scope':'Documentary and syntax consistency only; no OCR, compilation, or mathematical verification.'}
(root/'document_audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
