#!/usr/bin/env python3
"""Independent execution of the complete D85 exact certificate, preserving its outputs."""
from pathlib import Path
import hashlib, json, runpy, time
root=Path(__file__).resolve().parents[1]
source=root/'notes/de_sha_global_independence_certificate.py'
t0=time.time()
ns=runpy.run_path(str(source),run_name='fgh_D85_independent')
result=ns['result']
expected=json.loads(source.with_suffix('.json').read_text())
assert result==expected, 'Complete certificate JSON differs'
output={'status':'PASS','whole_json_equal':True,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'author_json_sha256':hashlib.sha256(source.with_suffix('.json').read_bytes()).hexdigest(),'elapsed_seconds':time.time()-t0,'result':result}
(root/'notes/fgh_D85_certificate_rerun.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
