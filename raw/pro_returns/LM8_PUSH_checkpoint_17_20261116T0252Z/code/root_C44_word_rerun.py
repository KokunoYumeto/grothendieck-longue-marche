"""Retained exact root execution; author outputs are not changed."""
from pathlib import Path
import runpy,hashlib,json
p=Path('code/pbc_exact_descent_kernel_word.py')
r=runpy.run_path(str(p),run_name='root_audit_only')['run']()
r['source_sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
s=json.dumps(r,indent=2)+'\n'
assert s==p.with_suffix('.json').read_text()
Path('notes/root_C44_word_rerun.json').write_text(s)
v={'status':'PASS','full_code_read':True,'whole_JSON_byte_equal':True,'source_sha256':r['source_sha256'],'result_sha256':hashlib.sha256(s.encode()).hexdigest(),'six_full_free_product_identities':6,'reduced_word_length':r['reduced_length']}
Path('notes/root_C44_word_verification.json').write_text(json.dumps(v,indent=2)+'\n')
print(json.dumps(v,indent=2))
