"""Retained exact root execution code; author outputs are not changed."""
from pathlib import Path
import hashlib,json,time
p=Path('notes/fgh_A73_certificate.py')
s=p.read_text();body=s[:s.index("Path(__file__).with_suffix('.json').write_text")]
start=time.monotonic();ns={'__file__':str(p),'__name__':'root_audit_only'}
exec(compile(body,str(p),'exec'),ns)
raw=json.dumps(ns['out'],indent=2)+'\n'
Path('notes/root_A73_certificate_rerun.json').write_text(raw)
assert raw==p.with_suffix('.json').read_text()
r={'status':'PASS','whole_JSON_byte_equal':True,'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'result_sha256':hashlib.sha256(raw.encode()).hexdigest(),'seconds':time.monotonic()-start,'levels':[x['n'] for x in ns['out']['levels']]}
Path('notes/root_A73_certificate_verification.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
