#!/usr/bin/env python3
"""Exact identities for the punctured elliptic maps of statement A.13."""
from pathlib import Path
import json
import sympy as S

x,y,t,u,v,a,b,c,z,X,Y=S.symbols('x y t u v a b c z X Y')
checks={}


def check(name, expr):
    value=S.factor(expr)
    assert value == 0, (name,value)
    checks[name]='zero'


# X^4+Y^4=2 Z^4, in the Z=1 chart.
for label,A,B in [('sign_X',4*y**2,-8*S.I*y*x**2),
                  ('sign_Y',4*x**2,-8*S.I*x*y**2)]:
    check(label+'_degree4_map',
          S.rem(B**2-(A**3-32*A),x**4+y**4-2,x))
check('quartic_infinity_divisor_norm',(u-S.I*t**2)*(u+S.I*t**2)-(u**2+t**4))
# The quartic quotient followed by the two-isogeny.
aq=2*(v+t**2);bq=4*t*(v+t**2)
check('quartic_to_cubic',S.rem(bq**2-(aq**3+8*aq),v**2-t**4+2,v))
check('two_isogeny_to_j1728',
      S.factor((b*(1-8/a**2))**2-((a+8/a)**3-32*(a+8/a))).subs(b**2,a**3+8*a))
check('composite_first_coordinate',
      S.rem(S.together(aq+8/aq-4*t**2).as_numer_denom()[0],v**2-t**4+2,v))
check('composite_second_coordinate',
      S.rem(S.together(bq*(1-8/aq**2)-8*t*v).as_numer_denom()[0],v**2-t**4+2,v))
# Stable D4 complementary quotient.
dc=(t**2-4*c)*(t**4-4*c*t**2+2*c**2)
ec=X**3-8*c*X**2+18*c**2*X-8*c**3
check('D4_complementary_map',dc-ec.subs(X,t**2))
check('D4_translate_torsion_point',ec.subs(X,x+4*c)-(x**3+4*c*x**2+2*c**2*x))
source=x**3+4*c*x**2+2*c**2*x
xp=x+4*c+2*c**2/x;yp=y*(1-2*c**2/x**2)
target=lambda r:r**3-8*c*r**2+8*c**2*r
check('D4_CM_two_isogeny',S.factor(yp**2-target(xp)).subs(y**2,source))
check('D4_CM_target_isomorphism',target(-2*x)+8*source)


def invariants(a2,a4,a6):
    b2=4*a2;b4=2*a4;b6=4*a6;b8=4*a2*a6-a4**2
    c4=S.expand(b2**2-24*b4)
    disc=S.factor(-b2**2*b8-8*b4**3-27*b6**2+9*b2*b4*b6)
    return {'c4':str(c4),'discriminant':str(disc),'j':str(S.factor(c4**3/disc))}


inv=invariants(-8*c,18*c**2,-8*c**3)
assert inv == {'c4':'160*c**2','discriminant':'512*c**6','j':'8000'},inv
inv_i=invariants(0,-32,0)
assert inv_i['j']=='1728'
# Quartic elliptic j formula used for the three sign quotients.
jq=lambda B,C:S.factor(16*(B**2+12*C)**3/(C*(B**2-4*C)**2))
assert jq(S.Integer(0),S.Integer(-2))==1728
assert jq(S.Integer(0),S.Integer(1))==1728
out={
 'symbolic_identities':checks,
 'quaternion_sign_X_Y_targets':inv_i,
 'stable_D4_complement':inv,
 'fibres':{'Q8_sign_X':'four cusps, each multiplicity 1, degree 4',
           'Q8_sign_Y':'four cusps, each multiplicity 1, degree 4',
           'Q8_sign_Z_then_2':'four cusps, each multiplicity 2, degree 8',
           'stable_D4':'two cusps, each multiplicity 1, degree 2'},
 'stable_D3_obstruction':'RH gives degree <=3; degree2 incompatible with the canonical divisor at a Weierstrass cusp; degree3 gives the unique differential line with zero divisor 2P.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
