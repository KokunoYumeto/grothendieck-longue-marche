"""Bounded full WF source delta; every line retained exactly."""
from pathlib import Path
import hashlib,json
B=Path('/workspace/scratch/94548b74fbe0');O=B/'out/checks'
sha=lambda x:hashlib.sha256(x).hexdigest()
p=O/'scan026_source_wf_extension_delta_v01.diff';raw=p.read_bytes();chunks=[];current=[];size=0;start=1;number=0
def flush():
 data=b''.join(current);path=O/f'scan026_source_wf_extension_delta_review_v01_{len(chunks)+1:02d}.txt'
 if path.exists():assert path.read_bytes()==data
 else:path.write_bytes(data)
 chunks.append({'path':str(path.relative_to(B)),'bytes':len(data),'sha256':sha(data),'first_line':start,'last_line':number})
for line in raw.splitlines(keepends=True):
 if current and size+len(line)>8500:flush();current=[];size=0;start=number+1
 current.append(line);size+=len(line);number+=1
if current:flush()
assert b''.join((B/r['path']).read_bytes() for r in chunks)==raw
manifest={'scope':'Complete WF evidence delta, without filtering or rewriting.',
 'source_path':str(p.relative_to(B)),'source_sha256':sha(raw),'source_bytes':len(raw),'chunks':chunks,
 'concatenation_reconstructs_full_delta_bytes':True,
 'proposal_path':'out/checks/scan026_source_wf_extension_proposal_v01.json',
 'inverse_proof_source':'out/checks/scan026_source_wf_extension_build_v01.py'}
data=(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode();path=O/'scan026_source_wf_extension_review_manifest_v01.json'
if path.exists():assert path.read_bytes()==data
else:path.write_bytes(data)
print(json.dumps(manifest,ensure_ascii=False,indent=2))
