"""Retained exact root replay; author outputs are not changed."""
from pathlib import Path
import hashlib,json,runpy
p=Path('notes/pbc_D90_boundary_certificate.py')
r=runpy.run_path(str(p),run_name='root_read_only')['run']()
r['source_sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
s=json.dumps(r,indent=2)+'\n';assert s==p.with_suffix('.json').read_text()
Path('notes/root_D90_boundary_rerun.json').write_text(s)
v={'status':'PASS','whole_JSON_byte_equal':True,'source_sha256':r['source_sha256'],'result_sha256':hashlib.sha256(s.encode()).hexdigest(),'depths_m':[x['depth_m'] for x in r['rows']],'full_source_read':True}
Path('notes/root_D90_boundary_verification.json').write_text(json.dumps(v,indent=2)+'\n')
print(json.dumps(v,indent=2))
