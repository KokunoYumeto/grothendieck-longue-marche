from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
p=R/'notes/de_ordinary_unbounded_finite_kernel_certificate.py'
ns={'__name__':'fgh_independent_D93','__file__':str(p)}
exec(compile(p.read_text(),str(p),'exec'),ns)
result=ns['run']()
expected=json.loads(p.with_suffix('.json').read_text())
assert result==expected
out=R/'notes/fgh_D93_certificate_rerun.json'
out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({'status':'PASS','whole_json_equal':True,'owner_source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'owner_result_sha256':hashlib.sha256(p.with_suffix('.json').read_bytes()).hexdigest(),'rerun_result_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'matrix_dimensions':[row['matrix_dimension'] for row in result['matrix_rows']]},indent=2))
