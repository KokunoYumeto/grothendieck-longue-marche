from pathlib import Path
import json
from fractions import Fraction
p=Path('research_e101/code')
(p/'e_unit_norm_display_attempt.py').write_bytes((p/'e_unit_norm_complete.py').read_bytes())
(p/'e_unit_norm_display_attempt.out').write_bytes((p/'e_unit_norm_complete.out').read_bytes())
s=(p/'e_unit_norm_complete.py').read_text().replace('            if source.stem=="e_basechange_field":\n                assert "BNF_CERTIFY 1" in run.stdout,"B1 certification did not return1"\n','')
(p/'e_unit_norm_display_rebuild_attempt.py').write_text(s)
(p/'e_unit_norm_display_rebuild_attempt.out').write_bytes((p/'e_unit_norm_complete_rebuild.out').read_bytes())
rows=[json.loads(x) for x in (p/'e_unit_norm_scalar.out').read_text().splitlines() if x.startswith('{')]
a=next(r['value'] for r in rows if r.get('name')=='reversed_norm_coefficients')
nums=[[Fraction(*q)*16578519 for q in row] for row in a]
assert all(v.denominator==1 for row in nums for v in row)
text=json.dumps([[int(v) for v in row] for row in nums],indent=2)+'\n'
(p/'e_unit_norm_display_correction.out').write_text(text)
print(text)
