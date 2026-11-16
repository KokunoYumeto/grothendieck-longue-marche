"""Read-only original group-law verifier for the A61 existential witness."""
from pathlib import Path
import runpy,json
HERE=Path(__file__).resolve().parent
globals().update(runpy.run_path(str(HERE/'check_A59_integral_center.py')))
w=json.loads((HERE/'A61_integral_frame_solution.json').read_text())
bb=tup(w['BFRAME']);jj=tup(w['JFRAME'])
assert tup(w['WE'])==WE and tup(w['PSHIFT'])==PSHIFT
assert ph(TT)==TT
assert na(na(SS))==SS and na(na(RR))==RR
assert ph(SS)==ein(bb,SS)
assert em(ei(bb),na(ei(bb)))==ONE
assert ein(ei(bb),na(SS))==SS
assert na(RR)==ein(jj,ei(RR))
assert em(ei(jj),na(ei(jj)))==ONE
assert ein(ei(jj),na(RR))==ei(RR)
assert bb[2]==HB and jj[2]==HS
print('READ-ONLY A61 VERIFIER: exact original group-law, both frames, cusp, square and heads PASS.')
