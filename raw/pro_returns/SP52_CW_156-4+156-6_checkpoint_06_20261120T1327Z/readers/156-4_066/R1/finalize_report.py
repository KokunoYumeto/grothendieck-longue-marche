from pathlib import Path
import json
from datetime import datetime,timezone
r=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_066/R1')
d=json.loads((r/'report.json').read_text())
t=(r/'reading.tex').read_text()
h=(Path('/workspace/scratch/6644f30583f9/page_packets/156-4_066/H.tex')).read_text()
hnote=next(line for line in h.splitlines() if line.startswith('\\note{'))
d['differences'][14]['h']=hnote
d['differences'][30]['h']=hnote
d['differences'][31]['h']=hnote
d['differences'][24]['c']=r"``en tenant compte \unsure{du|des} \unsure{Sup}''"
d['differences'][24]['reading']=r"``en tenant compte \unsure{du|des} Sup''"
figures=[]
p=0
while True:
 p=t.find('\\figure{',p)
 if p<0:break
 q=p+len('\\figure{'); depth=1
 while depth:
  if t[q]=='{':depth+=1
  elif t[q]=='}':depth-=1
  q+=1
 figures.append(t[p:q]);p=q
assert len(figures)==2
d['differences'][34]['reading']=figures[0]
d['differences'][52]['reading']=figures[1]
d['started_utc']='2026-11-20T09:24:01Z'
d['finished_utc']=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
(r/'report.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
log=(r/'inspection_log.md').read_text()
log=log.replace('Started: 2026-11-20T09:23:41Z (assignment and packet reading).','Started timestamp: 2026-11-20T09:24:01Z (first recorded clock value, after packet reading and before the first image view).')
log=log.rsplit('Finished: ',1)[0]+'Finished: '+d['finished_utc']+'\n'
log+='\nStructural/report checks only: balanced braces; two matched TikZ environments; all referenced source and crop files exist; no mathematical illegibility macro; 58 unique difference IDs; 24 C-doubt entries; inventory kinds restricted to the requested vocabulary. No LaTeX compiler was invoked.\n'
(r/'inspection_log.md').write_text(log)
allowed={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised','readable ink left as \\ill{}','drawing or diagram','other'}
assert all(x['kind'] in allowed for x in d['differences'])
assert len({x['id'] for x in d['differences']})==58
assert all(x['kind'] in {'text','display','diagram','drawing','margin note','insertion','deletion'} for x in d['inventory'])
assert all(x['sheet_kind']=='text' and x['hand']=='his hand' and x['transcribed']=='yes' for x in d['inventory'])
assert all(x['status'] in {'resolved','retained','revised'} for x in d['c_doubts'])
assert all(Path(x['path']).is_file() for x in d['crops'])
assert t.count('{')==t.count('}')
print(json.dumps({'status':'complete','differences':len(d['differences']),'c_doubts':len(d['c_doubts']),'remaining_doubts':len(d['remaining_doubts']),'crops':len(d['crops']),'finished_utc':d['finished_utc']}))
