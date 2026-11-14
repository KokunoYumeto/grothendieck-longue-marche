#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,shutil
R=Path(__file__).resolve().parents[1]
p=R.parent/'research_e122/code/e53_upper_unit_candidate_bnf.bin'
q=R/'inputs/e122_L2_candidate_bnf.bin'
if q.exists():assert q.read_bytes()==p.read_bytes()
else:shutil.copyfile(p,q)
d={'status':'PASS','source':str(p.relative_to(R.parent)),'copy':str(q.relative_to(R)),
 'sha256':hashlib.sha256(q.read_bytes()).hexdigest(),
 'scope':'Existing candidate object only; no class assertion before the new certification and independent E121 lower bound.'}
(R/'inputs/pivot_manifest.json').write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps(d,indent=2))
