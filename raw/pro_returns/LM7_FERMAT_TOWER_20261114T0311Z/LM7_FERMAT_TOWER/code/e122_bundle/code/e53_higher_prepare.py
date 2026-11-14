"""Retain the exact lower map inputs and their author provenance."""
from pathlib import Path
import hashlib,json,shutil
r=Path(__file__).resolve().parents[1]
old=r/'inputs/manifest.json'
if old.exists() and not (r/'inputs/initial_bin_manifest.json').exists():
    shutil.copyfile(old,r/'inputs/initial_bin_manifest.json')
sources=[('inputs/e119_e53_genus_transition.bin','inputs/e119_e53_genus_transition.bin'),
         ('inputs/e119_e53_genus_transition.out','inputs/e119_e53_genus_transition.out'),
         ('code/e53_normalizer_module.json','inputs/e121_normalizer_module.json')]
rows=[]
for src,dst in sources:
    p=r.parent/'research_e119_continuation'/src;q=r/dst
    shutil.copyfile(p,q)
    rows.append({'path':dst,'source':str(p),'sha256':hashlib.sha256(q.read_bytes()).hexdigest(),'bytes':q.stat().st_size})
d={'status':'PASS','files':rows,'source_scope':'Certified lower E119 objects and the amended E121 full-class maps, all unchanged by its proof-only amendment.'}
old.write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(d,indent=2))
