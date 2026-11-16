"""Retained exact root execution code; author outputs are not changed."""
from pathlib import Path
import runpy,json,hashlib,time
root=Path('.')
checks=[]
for source,label in [('notes/de_sha_cusp_finite_depth_certificate.py','owner'),('notes/pbc_D88_boundary_certificate.py','independent_boundary')]:
    p=Path(source)
    before=hashlib.sha256(p.read_bytes()).hexdigest()
    begin=time.monotonic()
    result=runpy.run_path(str(p),run_name='root_audit_only')['run']()
    if label=='independent_boundary': result['source_sha256']=before
    actual=json.dumps(result,indent=2)+'\n'
    out=Path('notes/root_D88_'+label+'_rerun.json')
    out.write_text(actual)
    expected=json.loads(p.with_suffix('.json').read_text())
    if label=='owner':
        assert actual==p.with_suffix('.json').read_text()
        mode='whole JSON byte equal'
    else:
        result.pop('elapsed_seconds');expected.pop('elapsed_seconds')
        assert result==expected
        mode='all mathematical and source fields equal; execution duration differs'
    checks.append({'source':source,'source_sha256':before,'verification':mode,'result_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'elapsed_seconds':time.monotonic()-begin})
record={'status':'PASS','full_sources_read':True,'checks':checks}
Path('notes/root_D88_certificate_verification.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
