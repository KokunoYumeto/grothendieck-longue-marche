"""Affine symbolic check on R/2Z x [-1,1], theta measured in pi units."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
# (a,b,c,d): (theta,t) -> (a theta+b t+c,d t)
def comp(f,g):
    a,b,c,d=f; A,B,C,D=g
    return (a*A,a*B+b*D,(a*C+c)%2,d*D)
I=(F(1),F(0),F(0),F(1))
r=(F(-1),F(0),F(0),F(-1))
s=(F(1),F(0),F(1),F(1))
t=(F(1),F(0),F(1),F(-1))
for f in (r,s,t):
    assert comp(f,f)==I
for f in (r,s,t):
    for g in (r,s,t):
        assert comp(f,g)==comp(g,f)
allmaps=set()
for a,b,c in product(range(2),repeat=3):
    f=I
    for bit,g in zip((a,b,c),(r,s,t)):
        if bit:f=comp(f,g)
    allmaps.add(f)
assert len(allmaps)==8
change=(F(1),F(1,2),F(0),F(1))
unchange=(F(1),F(-1,2),F(0),F(1))
old=(F(1),F(1),F(1),F(-1))
assert comp(change,comp(old,unchange))==t
out={'all_eight_distinct_commuting_involutions':True,'coordinate_change_conjugates_manuscript_antipodism':True,
     'maps':[[str(x) for x in f] for f in sorted(allmaps)]}
Path(__file__).with_name('verify_tube_local_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
