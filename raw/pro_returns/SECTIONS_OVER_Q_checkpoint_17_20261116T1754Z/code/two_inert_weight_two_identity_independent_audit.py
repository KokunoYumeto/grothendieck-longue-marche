#!/usr/bin/env python3
"""Independent exact algebra for the least-weight-two cochain comparison.

This certifies the displayed coefficient identities only. The finite-S
global dimension, Bockstein and integral-inflation arguments are in the proof.
"""
from math import comb
from pathlib import Path
import json
def add(a,b,m):return [(x+y)%m for x,y in zip(a,b)]
def mul(a,b,m):
    return [sum(a[j]*b[i-j]for j in range(i+1))%m for i in range(3)]
def xp(k,m):return [1,k%m,comb(k,2)%m]
def theta(a,c,m):
    # T -> c*T+binom(c,2)*T^2.
    return [a[0]%m,a[1]*c%m,(a[1]*comb(c,2)+a[2]*c*c)%m]
def psi(a,k,c,m):return mul(xp(k,m),theta(a,c,m),m)
w=[3,3,1];X=[1,1,0];identities=[]
for a in range(9):
 for c in (1,2,4,5,7,8):
    theta9=(c*c-1)//3%3
    pw=psi(w,a,c,9);d=[(x-y)%9 for x,y in zip(pw,w)]
    assert all(x%3==0 for x in d)
    lhs=[x//3%3 for x in d]
    rhs=add([(x-y)%3 for x,y in zip(psi(X,a,c,3),X)],
            [0,0,theta9],3)
    assert lhs==rhs
    # The top D2 line has action chi^3; the bottom has chi^2.
    assert psi([0,0,1],a,c,9)==[0,0,c**2%9]
    v=psi([0,1,0],a,c,9)
    assert v[1]==c%9
    identities.append({'a':a,'chi':c,'theta9':theta9,'divided_defect':lhs})
assert len(identities)==54
print('PASS: all54 exact divided augmentation identities modulo9.')
# Multiplying by chi is the exterior (1)-twist in V_A.
# The coefficient embedding I3(1)->D2/9 is multiplication by3/T.
for a in range(9):
 for c in (1,2,4,5,7,8):
  for b0 in range(3):
   for b1 in range(3):
    v=[0,b0,b1]
    gv=[c*x%3 for x in psi(v,a,c,3)]
    jgv=[3*gv[1]%9,3*gv[2]%9]
    # D2 is I/T^3I written after division by T.
    before=[0,3*b0%9,3*b1%9]
    actual=[c*x%9 for x in psi(before,a,c,9)]
    assert jgv==actual[1:]
    assert (c**3-c)%3==0
print('PASS: all486 actual twisted coefficient-embedding squares.')
assert 8*2%3==1
print('PASS: nonzero bottom tame cup value8*2=1 modulo3.')
Path(__file__).with_name('two_inert_weight_two_identity_independent_audit_data.json').write_text(
    json.dumps({'identities':identities,'embedding_checks':486,
                'bottom_tame_value':1,
                'scope':'Finite coefficient algebra; no global cohomology dimension inferred.'},indent=2)+'\n')
