"""Count explicit C uncertainty marks against committed decision records.

This bookkeeping aid does not decide any reading. A count difference may be
legitimate if one inseparable locus contains several marks; it requires review.
Only committed pages are read. No image processing or TeX compilation occurs.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,re
O=Path(__file__).resolve().parents[1];W=O.parent
rows=[]
for p in sorted((O/'decisions').glob('scan*.json')):
 d=json.loads(p.read_text());n=d['scan']
 source=W/f'packets/scan{n:03}/C.tex'
 if not source.exists():
  meta=next(x for x in json.loads((O/'page_order.json').read_text()) if int(x['our_scan'])==n)
  source=W/'source/SP46_CW_37_witnesses'/meta['codex_file']
 t=source.read_text();marks=[]
 for m in re.finditer(r'\\(unsure|illegible)\{',t):
  start=m.end();depth=1;i=start
  while i<len(t) and depth:
   if t[i]=='{' and (i==0 or t[i-1]!='\\'):depth+=1
   if t[i]=='}' and (i==0 or t[i-1]!='\\'):depth-=1
   i+=1
  marks.append(dict(command=m.group(1),contents=t[start:i-1]))
 decisions=[dict(place=x['place'],c_reading=x['c_reading'],reading=x['reading'],unresolved=x.get('unresolved',False)) for x in d['decisions'] if x.get('c_doubt')]
 rows.append(dict(scan=n,c_marks=marks,c_mark_count=len(marks),c_doubt_decision_count=len(decisions),counts_agree=len(marks)==len(decisions),decisions=decisions))
result=dict(checked_utc=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),scope='Explicit unsure/illegible macros in C; contextual doubts and confirmed inspection targets are handled separately in page decisions. Count agreement is a bookkeeping check, not proof of individual coverage or correctness.',pages=rows)
(O/'doubt_coverage.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('Explicit C-mark/decision counts:',', '.join(f"{r['scan']:03} {r['c_mark_count']}/{r['c_doubt_decision_count']}" for r in rows))
print('Count discrepancies requiring review:',[r['scan'] for r in rows if not r['counts_agree']])
