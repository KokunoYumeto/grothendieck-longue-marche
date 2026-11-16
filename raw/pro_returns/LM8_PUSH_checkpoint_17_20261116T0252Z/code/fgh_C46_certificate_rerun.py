#!/usr/bin/env python3
"""Independent read-only complete replay of the C46 word/derived certificate."""
from pathlib import Path
import runpy,json,hashlib
r=Path(__file__).resolve().parents[1];s=r/'code/pbc_derived_descent_kernel_word.py'
v=runpy.run_path(str(s),run_name='fgh_C46')['run']()
v['source_sha256']=hashlib.sha256(s.read_bytes()).hexdigest()
v=json.loads(json.dumps(v))
assert v==json.loads(s.with_suffix('.json').read_text())
(r/'notes/fgh_C46_certificate_rerun.json').write_text(json.dumps(v,indent=2)+'\n')
print(json.dumps({'status':'PASS','whole_json_equal':True,'word_length':v['reduced_length'],'full_fillings':len(v['six_actual_full_fillings']),'derived_images':v['finite_derived_images']}))
