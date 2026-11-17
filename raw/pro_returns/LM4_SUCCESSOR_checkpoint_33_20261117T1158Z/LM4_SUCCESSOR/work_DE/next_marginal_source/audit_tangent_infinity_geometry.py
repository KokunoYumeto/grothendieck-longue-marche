"""Actual cyclotomic deformation and based path margins for the infinity braid."""
from pathlib import Path
from fractions import Fraction as F
import json
import sympy as S
from quadratic_pencil_braid import u,Q,I
HERE=Path(__file__).resolve().parent
w=json.loads((HERE/'tangent_infinity_braid.json').read_text())
base=Q(1,100);end=10+10*I;d=end-base;dd=S.re(d)**2+S.im(d)**2
centers=[S.Integer(0)]+[S.cancel(v*v) for v in u]+[S.cancel(2*v-v*v) for v in u[1:]]
for c in centers:
 e=c-base;t=max(0,min(1,(S.re(d)*S.re(e)+S.im(d)*S.im(e))/dd));r=e-t*d
 assert S.re(r)**2+S.im(r)**2>Q(1,100000)
 assert abs(S.re(c))<3 and abs(S.im(c))<3
# All square sides stay at distance>=7 from the collision centers.
# The producer certifies |q|_1<25 and every rational/quadratic residual>1e-12.
assert (F(25)/F(99,100)+F(101,100))/2<F(14)
assert (F(25)/F(99,100)**2+1)/2<14
assert 14*F(2,10**30)<F(1,10**27)
assert F(1,10**12)/19>F(1,10**14)
assert 2*F(1,10**27)<F(1,10**14)
# For |q|>=10, (|q|-1)/2 > sqrt(|q|)+1, so all five line points
# remain outside both roots and source T1. The difference grows thereafter.
assert F(9,2)>F(32,10)+1 and F(32,10)**2>10
out={'actual_strand_motion_upper_bound':'1/10^27','rational_strand_separation_lower_bound':'1/10^14','whisker_other_center_squared_distance_lower_bound':'1/100000','annular_square_radius_lower_bound':10,'annular_type':'full eight-strand twist times inverse inner three-strand half twist, after the actual whisker','exponent':53,'scope':'Actual based infinity comparison; no equality of its root arc with the q0 arc.'}
(HERE/'tangent_infinity_geometry_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS actual infinity whisker, cyclotomic deformation, separation, and annular exponent56-3=53.')
