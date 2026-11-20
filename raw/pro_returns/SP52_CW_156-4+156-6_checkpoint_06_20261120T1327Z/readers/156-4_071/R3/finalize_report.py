from pathlib import Path
import json,re
from datetime import datetime,timezone
p=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_071/R3')
packet=Path('/workspace/scratch/6644f30583f9/page_packets/156-4_071')
r=json.loads((p/'report.json').read_text()); C=(packet/'C.tex').read_text(); H=(packet/'H.tex').read_text(); T=(p/'reading.tex').read_text()
d={x['id']:x for x in r['differences']}
fig2=T[T.index('% Figure L2:'):T.index('\nde $\\mathcal F$ est fermé')]
d['D07']['reading']=fig2
d['D07']['scan_shows']+=' This row concerns the de state only.'
for k in ['D09','D40','D41']:
 d[k]['c']='';d[k]['h']=''
d['D25']['c']=''
hnote=H[H.rindex('\\note{'):].strip()
d['D25']['h']=hnote
d['D26']['h']=hnote
d['D26']['scan_shows']+=' H gives 55 only in its editorial note.'
d['D24'].update(location='Paragraph boundary before Donc',c='.\n\nDonc ',h='. Donc ',reading='.\n\nDonc ',scan_shows='Donc begins a fresh left-aligned block below the corollary.')
new=dict(d['D24']);new.update(id='D45',location='Paragraph boundary before En d’autres termes',c='.\n\nEn d\'autres termes,',h='. En d\'autres termes,',reading='.\n\nEn d\'autres termes,',scan_shows='En d’autres termes begins another fresh left-aligned block.')
r['differences'].append(new)
# Quote complete corresponding blocks for the inverted-paragraph placement row.
cstart=C.index('\\deleted{un ensemble,')
hstart=H.index('\\struck{un ensemble,')
hend=H.index('\n\\note{',hstart)
tstart=T.index('\\deleted{un ensemble,')
d['D44']['c']=C[cstart:].strip();d['D44']['h']=H[hstart:hend].strip();d['D44']['reading']=T[tstart:].strip()
d['D44']['scan_shows']='The inverted text has successive first-line starts un ensemble, Alors and Dém. This row concerns paragraph placement only.'
d['D27']['math_consequential']=False
r['finished_utc']=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
(p/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
with (p/'inspection_log.md').open('a') as f:
 f.write('\nFinal report collation: 45 difference loci, 29 C-doubt/context dispositions, 15 remaining doubts, 28 inventory entries, 16 own crops. Witness snippets and figure scopes were aligned in finalize_report.py. No further image views or mathematical checks.\n')
print(json.dumps({'reading_file':str(p/'reading.tex'),'report_file':str(p/'report.json'),'differences':len(r['differences']),'remaining_doubts':len(r['remaining_doubts']),'crops':len(r['crops']),'finished_utc':r['finished_utc']},indent=2))
