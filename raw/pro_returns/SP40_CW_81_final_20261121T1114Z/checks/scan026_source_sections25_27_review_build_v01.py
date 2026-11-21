"""Bounded byte-exact review chunks; no content compression or normalization."""
from pathlib import Path
import hashlib,json
B=Path('/workspace/scratch/94548b74fbe0');O=B/'out/checks'
sha=lambda x:hashlib.sha256(x).hexdigest()
def save(path,raw):
 if path.exists():assert path.read_bytes()==raw
 else:path.write_bytes(raw)
 return {'path':str(path.relative_to(B)),'sha256':sha(raw),'bytes':len(raw)}
manifest=[]
for kind,suffix in [('delta','diff'),('selected_states','json')]:
 p=O/f'scan026_source_sections25_27_{kind}_v01.{suffix}';raw=p.read_bytes();chunks=[];current=[];size=0;start=1;number=0
 def flush():
  data=b''.join(current);out=O/f'scan026_source_sections25_27_{kind}_review_v01_{len(chunks)+1:02d}.txt'
  row=save(out,data);row.update({'source_line_start':start,'source_line_end_inclusive':number});chunks.append(row)
 for line in raw.splitlines(keepends=True):
  if current and size+len(line)>8500:flush();current=[];size=0;start=number+1
  current.append(line);size+=len(line);number+=1
 if current:flush()
 assert b''.join((B/x['path']).read_bytes() for x in chunks)==raw
 manifest.append({'source':str(p.relative_to(B)),'sha256':sha(raw),'bytes':len(raw),'exact_ordered_chunks':chunks,'concatenation_exact':True})
save(O/'scan026_source_sections25_27_review_manifest_v01.json',(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode())
print(json.dumps(manifest,ensure_ascii=False,indent=2))
