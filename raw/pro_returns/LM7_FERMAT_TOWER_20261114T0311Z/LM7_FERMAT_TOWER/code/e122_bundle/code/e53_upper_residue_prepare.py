"""Retain the literal lower S-unit coefficients for the finite-prime tests."""
from pathlib import Path
import hashlib,json,shutil
r=Path(__file__).resolve().parents[1]
p=r.parent/'research_e119/code/e53_six_character_witness.out'
q=r/'inputs/e119_six_character_witness.out'
shutil.copyfile(p,q)
d={'status':'PASS','source':str(p),'path':str(q.relative_to(r)),
   'sha256':hashlib.sha256(q.read_bytes()).hexdigest(),'bytes':q.stat().st_size,
   'scope':'Literal coefficients and verified divisors of the complete lower S-unit basis; no candidate upper BNF completeness is inferred.'}
(r/'inputs/residue_manifest.json').write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps(d,indent=2))
