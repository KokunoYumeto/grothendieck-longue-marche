"""Independent read-only verification of the completed A61 central witness.
The imported source's baseline output is redirected into work_CE.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import json,hashlib
HERE=Path(__file__).resolve().parent;root=HERE.parents[1]
src=root/'work_A/check_A59_integral_center.py'
s=src.read_text().replace("(HERE/'A59_integral_center_baseline.json')",'Path('+repr(str(HERE.parent/'A59_baseline_A61_review.json'))+')')
A={'__file__':str(src),'__name__':'_independent_A61_review'}
with redirect_stdout(StringIO()):exec(compile(s,str(src),'exec'),A)
p=root/'work_A/A61_integral_frame_solution.json';raw=p.read_bytes();w=json.loads(raw)
tup=A['tup'];B=tup(w['BFRAME']);J=tup(w['JFRAME']);SS=A['SS'];RR=A['RR'];TT=A['TT'];ONE=A['ONE'];ph=A['ph'];na=A['na'];em=A['em'];ei=A['ei'];ein=A['ein']
assert tup(w['WE'])==A['WE'] and tup(w['PSHIFT'])==A['PSHIFT']
assert ph(TT)==TT
assert na(na(SS))==SS and na(na(RR))==RR
assert ph(SS)==ein(B,SS)
assert em(ei(B),na(ei(B)))==ONE
assert ein(ei(B),na(SS))==SS
assert na(RR)==ein(J,ei(RR))
assert em(ei(J),na(ei(J)))==ONE
assert ein(ei(J),na(RR))==ei(RR)
assert B[2]==A['HB'] and J[2]==A['HS']
for name in ('s_half','r_half'):
 z=tup(w[name]);e=(A['AA0'],z,A['HN0']);assert na(e)==e
 assert A['zs'](2,z)==tup(w['s_old_square'if name=='s_half'else'r_old_square'])
print('Independent full original-law A61 witness verification: PASS')
print('Both conjugacy equations, both normalizer norms, cusp and quotient action square: PASS')
print('Both chosen central halves are b-fixed and double to the actual old square: PASS')
print('Witness SHA256',hashlib.sha256(raw).hexdigest())
print('Scope: actual scalar-stable quotient; newer A56 central frames change; no full negative involution.')
