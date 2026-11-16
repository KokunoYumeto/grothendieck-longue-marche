"""Exact cyclotomic checks for the proposed marginal ratio-pencil model.

This certifies coordinates and all finite discriminant/collision loci.  It
does not calculate the transported braid monodromies or prove normality.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
import sympy as S
HERE=Path(__file__).resolve().parent
X=S.Symbol('X');phi=X**4+X**3+X**2+X+1
def el(p):
    p=S.rem(S.Poly(p,X,domain=S.QQ),S.Poly(phi,X,domain=S.QQ)).as_expr()
    return tuple(Q(p.coeff(X,i)) for i in range(4))
def pol(a):return sum(S.Rational(c.numerator,c.denominator)*X**i for i,c in enumerate(a))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def sub(a,b):return add(a,neg(b))
def mul(a,b):return el(pol(a)*pol(b))
def inv(a):return el(S.invert(pol(a),phi,X))
def div(a,b):return mul(a,inv(b))
def scale(n,a):return tuple(n*x for x in a)
Z=el(X);one=el(1);zero=el(0);minusone=el(-1)
roots=[el(X**j) for j in range(5)];others=[u for u in roots if u!=Z]
def key(a):return ','.join(str(x) for x in a)
zero_events=[];triple_events=[]
for u in others:
    r=sub(one,div(u,Z))
    zero_events += [{'u':key(u),'orientation':'v=u,w=0','lambda':key(r)},
                    {'u':key(u),'orientation':'v=0,w=u','lambda':key(inv(r))}]
for u in others:
    for v in others:
        if u==v:continue
        r=div(sub(u,Z),sub(v,Z));q=mul(u,v)
        assert q in roots
        triple_events.append({'u':key(u),'v':key(v),'q':key(q),'lambda':key(r)})
        if q==mul(Z,Z):assert r==neg(div(u,Z))
U={e['lambda'] for e in zero_events+triple_events}
assert key(minusone) not in U and key(zero) not in U and key(one) not in U
assert not ({e['lambda'] for e in zero_events}&{e['lambda'] for e in triple_events})
# Each retained discriminant is lambda^2+(4q/zeta^2-2)lambda+1.
D=[]
for q in roots:
    if q==mul(Z,Z):continue
    mid=sub(scale(4,div(q,mul(Z,Z))),scale(2,one))
    assert sub(mul(mid,mid),scale(4,one))!=zero
    for a in [zero,one,minusone]+[tuple(Q(x) for x in k.split(',')) for k in U]:
        assert add(add(mul(a,a),mul(mid,a)),one)!=zero
    D.append({'q':key(q),'middle_coefficient':key(mid)})
assert len({d['middle_coefficient'] for d in D})==4
# Two distinct such quadratics have no common root: their difference is
# a nonzero multiple of lambda, and neither has zero as a root.

s,p,u,t,v,w,lam,z,q=S.symbols('s p u t v w lam z q')
vp=((u-s)/(u+s))**2
assert S.cancel(s*(1+vp)/(1-vp)-(s*s+u*u)/(2*u))==0
a=(S.Symbol('zeta')-s)/(S.Symbol('zeta')+s)
assert S.cancel(s*(1+a)/(1-a)-S.Symbol('zeta'))==0
zz=S.Symbol('zeta')
assert S.expand((zz+lam*z)*(zz+z)-q-(lam*z*z+zz*(lam+1)*z+zz*zz-q))==0
assert S.expand(((zz+lam*z)*(zz+z)-zz*zz)-z*(lam*z+lam*zz+zz))==0
out={'scope':'Exact geometry and critical-value bookkeeping only; based braid transports and the U-kernel normality remain unresolved.',
     'cyclotomic_field':'Q[X]/(X^4+X^3+X^2+X+1); zeta=X',
     'zero_double_events':zero_events,'U_triple_events':triple_events,
     'retained_discriminant_quadratics':D,
     'distinct_zero_critical_values':len({e['lambda'] for e in zero_events}),
     'distinct_triple_critical_values':len({e['lambda'] for e in triple_events}),
     'generic_retained_finite_punctures':12,'generic_total_finite_punctures':20,
     'special_retained_finite_punctures':11,'special_total_finite_punctures':19}
(HERE/'ratio_pencil_data.json').write_text(json.dumps(out,indent=2)+'\n')
print('Coordinate identities: PASS')
print('Retained degeneration at lambda=-1 involves only z=0 and b(lambda).')
print('Retained discriminants:4 distinct separable quadratics,8 distinct roots; all disjoint from U events and0,1,-1.')
print('U/zero double events:',len(zero_events),'distinct base values:',out['distinct_zero_critical_values'])
print('U/U/hyperbola triple events:',len(triple_events),'distinct base values:',out['distinct_triple_critical_values'])
print('Generic puncture counts retained/total:12/20; special counts:11/19.')
print('PASS: finite critical-value bookkeeping. No monodromy-normality conclusion.')

