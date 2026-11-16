#!/usr/bin/env python3
"""Independent read-only execution of DE's exact D86 certificate."""
from pathlib import Path
import hashlib, importlib.util, json, time
r=Path(__file__).resolve().parents[1]
p=r/'notes/de_sha_cusp_infinite_torsion_certificate.py'
start=time.time(); spec=importlib.util.spec_from_file_location('fgh_D86_independent',p)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
expected=json.loads(p.with_suffix('.json').read_text());assert m.result==expected
out=r/'notes/fgh_D86_certificate_rerun.json';out.write_text(json.dumps(m.result,indent=2)+'\n')
print(json.dumps({'status':'PASS','whole_json_equal':True,'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'json_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'operator_checks':m.result['operator_check_count'],'shell_levels':len(m.result['weighted_shell_checks']),'boundary_checks':len(m.result['integral_boundary_checks']),'elapsed_seconds':round(time.time()-start,3)},indent=2))
