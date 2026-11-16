#!/usr/bin/env python3
"""Independent read-only rerun of the exact C44 source certificate."""
from pathlib import Path
import runpy, hashlib, json
root=Path(__file__).resolve().parents[1]
src=root/'code/pbc_exact_descent_kernel_word.py'
result=runpy.run_path(str(src),run_name='fgh_C44_independent')['run']()
result['source_sha256']=hashlib.sha256(src.read_bytes()).hexdigest()
expected=json.loads(src.with_suffix('.json').read_text())
result=json.loads(json.dumps(result))
assert result==expected
out={'status':'PASS','whole_json_equal':True,'source_sha256':result['source_sha256'],'expected_json_sha256':hashlib.sha256(src.with_suffix('.json').read_bytes()).hexdigest(),'result':result}
(root/'notes/fgh_C44_certificate_rerun.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','whole_json_equal':True,'reduced_length':result['reduced_length'],'full_fillings':len(result['six_actual_full_fillings']),'signed_moduli':[v['modulus'] for v in result['signed_original_matrices']]}))
