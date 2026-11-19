#!/usr/bin/env python3
"""Append reproducible crop totals and the complete first/last briefs."""
from pathlib import Path
import json,re
p=Path(__file__).resolve().parents[1]
records=[json.loads(x.read_text()) for x in sorted((p/'decisions').glob('scan*.json'))]
last=records[-1]['scan']
briefs=[]
for f in sorted((p/'briefs').glob('brief_v*.md')):
 t=f.read_text();m=re.search(r'first used scan\s+(\d+)',t)
 if m and int(m.group(1))<=last:briefs.append((int(m.group(1)),f,t))
first=briefs[0];final=briefs[-1]
rows=[]
for r in records:
 n=r['scan'];counts=[]
 for k in ['R1','R2','R3']:
  rr=p/f'readers/scan{n:03d}/{k}'
  counts.append(sum(x.suffix.lower() in {'.jpg','.jpeg','.png'} for x in rr.rglob('*') if x.is_file()))
 new=sum(x.suffix.lower() in {'.jpg','.jpeg','.png'} for x in (p/f'crops/scan{n:03d}').rglob('*') if x.is_file())
 a=r.get('main_crop_audit',[])
 if isinstance(a,dict):viewed=sum(len(v) for v in a.values() if isinstance(v,list))
 else:viewed=len(a)
 rows.append([n,*counts,new,viewed,sum(counts)+new])
marker='\n## Final workflow totals and briefs\n'
f=p/'SP37_CW_71_workflow.md';t=f.read_text().split(marker)[0]
add=marker+'\nCrop files count distinct tight crops, not whole pages or halves. Main views include reusing reader crops; they do not add another crop file. Rotation mistakes are disclosed in each affected page record.\n\n'
add+='| Scan | R1 crops | R2 crops | R3 crops | New main crops | Main crop views | Total distinct crops |\n| --- | --- | --- | --- | --- | --- | --- |\n'
for row in rows:add+='| '+' | '.join(map(str,row))+' |\n'
add+='\n### Brief versions actually used\n\n'
for n,b,_ in briefs:add+=f'- {b.name}: first used scan {n:03d}.\n'
add+='\n### First brief — complete text\n\n```markdown\n'+first[2].rstrip()+'\n```\n'
add+='\n### Last brief actually used — complete text\n\n```markdown\n'+final[2].rstrip()+'\n```\n'
f.write_text(t+add)
print(json.dumps({'pages':len(records),'last_brief':final[1].name,'distinct_crops':sum(row[-1] for row in rows)}))
