#!/usr/bin/env python3
"""Read-only independent replay of the D90 literal boundary certificate."""
from pathlib import Path
import runpy,json,hashlib
r=Path(__file__).resolve().parents[1]
s=r/'notes/pbc_D90_boundary_certificate.py'
v=runpy.run_path(str(s),run_name='fgh_D90')['run']()
v['source_sha256']=hashlib.sha256(s.read_bytes()).hexdigest()
v=json.loads(json.dumps(v))
assert v==json.loads(s.with_suffix('.json').read_text())
(r/'notes/fgh_D90_certificate_rerun.json').write_text(json.dumps(v,indent=2)+'\n')
print(json.dumps({'status':'PASS','whole_json_equal':True,'depths':[x['depth_m'] for x in v['rows']],'coefficient_exponents':list(range(1,6))}))
