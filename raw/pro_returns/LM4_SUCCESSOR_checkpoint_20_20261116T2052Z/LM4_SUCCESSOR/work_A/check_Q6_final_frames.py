"""Read-only direct verification of the regenerated Q6 central witness."""
from pathlib import Path
import json,runpy,sys
HERE=Path(__file__).resolve().parent
globals().update(runpy.run_path(str(HERE/'check_Q6_central_cover.py')))
def tup(x):return tuple(tup(y)for y in x)if isinstance(x,list)else x
path=Path(sys.argv[1])if len(sys.argv)>1 else HERE/'Q6_actual_central_solution.json'
data=json.loads(path.read_text())
WE=tup(data['WE']);PSHIFT=tup(data['PSHIFT'])
BFRAME=tup(data['BFRAME']);JFRAME=tup(data['JFRAME'])
phi0.__globals__['WE']=WE;ph.__globals__['PSHIFT']=PSHIFT
assert ph(TT)==TT
assert ph(SS)==ein(BFRAME,SS)
assert na(na(SS))==SS and na(na(RR))==RR
assert em(ei(BFRAME),na(ei(BFRAME)))==ONE
assert ein(ei(BFRAME),na(SS))==SS
assert na(RR)==ein(JFRAME,ei(RR))
assert em(ei(JFRAME),na(ei(JFRAME)))==ONE
assert ein(ei(JFRAME),na(RR))==ei(RR)
assert BFRAME[2]==HB and JFRAME[2]==HS
print('READ-ONLY ORIGINAL GROUP-LAW VERIFIER: all action, literal head, cusp, and s/r normalizer equations PASS.')
