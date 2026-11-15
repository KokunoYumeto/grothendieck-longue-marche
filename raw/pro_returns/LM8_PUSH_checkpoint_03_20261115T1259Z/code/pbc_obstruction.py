#!/usr/bin/env python3
"""Exact algebra and class-two checks of the central peripheral obstruction.

No input from earlier programs or supplied return coefficients is used.
The symbolic computation treats t and its inverted value as independent.
The numerical calculation uses an independently constructed three-dimensional
Heisenberg Lie group with two prescribed conjugation operators.
"""
from fractions import Fraction as Q
import json
from pathlib import Path
import sympy as S

X,Y,t,ti=S.symbols('X Y t ti', nonzero=True)
d=(X-1)*(Y-1)*(X*Y-1)
di=(1/X-1)*(1/Y-1)*(1/(X*Y)-1)
beta=1+d*t
bi=1+di*ti
N=S.expand(beta*bi-1)
P=S.cancel(-X*Y*N/d)
k=1/X-X+2*X*Y-2*Y
two_a=-2*X*Y*t+k*t*ti
invariant=(X*Y+1/(X*Y)-Y-1/Y)*t*ti
# The inverse-linear term changes sign in R/R^inv.
P_reduced=-2*X*Y*t+d/(X*Y)*t*ti
assert S.cancel(di+d/(X*Y)**2)==0
assert S.cancel(P-(-X*Y*t+ti/(X*Y)+d/(X*Y)*t*ti))==0
assert S.cancel(two_a-P_reduced-invariant)==0
inv=lambda f:S.cancel(f.subs({X:1/X,Y:1/Y,t:ti,ti:t}, simultaneous=True))
assert S.cancel(inv(P)+P)==0
assert S.cancel(inv(invariant)-invariant)==0

def add(v,w):return tuple(a+b for a,b in zip(v,w))
def neg(v):return tuple(-a for a in v)
def sc(k,v):return tuple(k*a for a in v)
def br(u,v):return u[1]*v[0]-u[0]*v[1]
def mul(u,v):
    w=add(u,v)
    return (w[0],w[1],w[2]+br(u,v)/2)

checks=[]
for a,b in [(2,3),(3,5),(5,2)]:
    a,b=Q(a),Q(b)
    xp,yp=(a,1/a),(b,1/b)
    def TX(v):return (a*v[0],v[1]/a,v[2])
    def TY(v):
        ky=-a*b/(a-1)*v[0]-1/(b*(a-1))*v[1]
        return (b*v[0],v[1]/b,v[2]+ky)
    def TW(v):return TX(TY(v))
    c=(Q(1),Q(1),Q(0))
    for v in [(Q(1),Q(0),Q(0)),(Q(0),Q(1),Q(0))]:
        lhs=TX(TY(v)); rhs=TY(TX(v)); rhs=(rhs[0],rhs[1],rhs[2]+br(c,rhs))
        assert lhs==rhs
    for tp,tm in [(0,0),(1,0),(0,1),(1,1),(2,-3)]:
        tp,tm=Q(tp),Q(tm)
        r=((a*b-1)*tp,(1/(a*b)-1)*tm,Q(0))
        s=(a*(b-1)*tp,(1/a)*(1/b-1)*tm,Q(0))
        actual=TX(mul(neg(r),TY(r)))
        expected=mul(neg(s),TW(s))
        error=mul(actual,neg(expected))
        assert error[:2]==(0,0)
        dp=(a-1)*(b-1)*(a*b-1)
        dm=(1/a-1)*(1/b-1)*(1/(a*b)-1)
        nn=(1+dp*tp)*(1+dm*tm)-1
        pplus=-a*b*nn/dp
        pminus=-(1/(a*b))*nn/dm
        assert 2*error[2]==pplus-pminus
        checks.append(dict(a=str(a),b=str(b),t=[str(tp),str(tm)],error=str(error[2])))

out=dict(symbolic_identities=5,heisenberg_operator_checks=6,
         exact_heisenberg_peripheral_checks=len(checks),all_passed=True,
         formula='2 a = [-XY (beta beta^inv - 1)/d] in R/R^inv',
         invariant_remainder=str(S.expand(invariant)),examples=checks)
print(json.dumps(out,indent=2))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
