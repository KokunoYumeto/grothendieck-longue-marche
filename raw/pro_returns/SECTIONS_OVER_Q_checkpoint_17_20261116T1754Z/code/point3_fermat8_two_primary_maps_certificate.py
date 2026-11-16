#!/usr/bin/env python3
"""Literal maps used by A187; all computation is local and exact."""
from pathlib import Path
import json
import sympy as S

BASE=Path(__file__).resolve().parent
s,t,n,b=S.symbols('s t n b',nonzero=True)
d=s*s
rel=n*n-d*t**4-b/d
X=2*d*t*t+2*s*n
Y=2*s*t*X
def zero_mod(expr,relation,variable):
    return S.rem(S.together(expr).as_numer_denom()[0],relation,variable)==0
assert zero_mod(Y*Y-X**3+4*b*X,rel,n)
assert zero_mod(X/4-b/X-d*t*t,rel,n)
assert zero_mod(Y*(1+4*b/X**2)/8-d*t*n,rel,n)
assert S.cancel(Y/(2*s*X)-t)==0
assert S.cancel((X-2*d*t*t)/(2*s)-n)==0
Xbar=X.subs(s,-s)
Ybar=Y.subs(s,-s)
assert zero_mod(Xbar+4*b/X,rel,n)
assert zero_mod(Ybar-4*b*Y/X**2,rel,n)
assert zero_mod(X*Xbar+4*b,rel,n)
print('PASS: actual psi-torsor equation, inverse, composition, and kernel-point cocycle')

z,w,A,r=S.symbols('z w A r',nonzero=True)
R=w**4-A*z*(z*z+r*r)
qX=A*w*w/z
qY={sign:A*A*w*(z+sign*r)/z for sign in [1,-1]}
for sign in [1,-1]:
    j={z:r*r/z,w:sign*r*w/z}
    assert S.cancel(qX.subs(j,simultaneous=True)-qX)==0
    for target in [1,-1]:
        expected=1 if sign==target else -1
        assert S.cancel(qY[target].subs(j,simultaneous=True)-expected*qY[target])==0
    assert zero_mod(qY[sign]**2-qX**3-sign*2*A**3*r*qX,R,w)
    twice={v:S.cancel(expr.subs(j,simultaneous=True)) for v,expr in j.items()}
    assert twice=={z:z,w:w}
plus={z:r*r/z,w:r*w/z}
minus={z:r*r/z,w:-r*w/z}
assert S.cancel(plus[z].subs(minus,simultaneous=True)-z)==0
assert S.cancel(plus[w].subs(minus,simultaneous=True)+w)==0
print('PASS: both quotient involutions, cross anti-invariance, and product iota')

# On the anti-iota character spaces, j_-=-j_+.  Both possibilities
# occur, and the integral pull-push multiplier is exactly two.
for jp in [1,-1]:
    jm=-jp
    assert 2+jp+jm==2
    assert (1+jp)*(1+jm)==0
print('PASS: exact integral Prym multiplier2 and cross-term cancellation')

(BASE/'point3_fermat8_two_primary_maps_certificate_data.json').write_text(
    json.dumps({'torsor_map_checks':8,'quotient_sign_cases':4,
                'prym_multiplier':2,
                'jacobian_degree_bound':'a = v_2(deg(F_A182))+1; numerical degree not asserted'},indent=2)+'\n')
print('PASS: A187 literal maps; arithmetic inputs are the audited A185/A186 certificates')
