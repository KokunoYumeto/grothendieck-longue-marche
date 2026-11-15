#!/usr/bin/env python3
"""An integral coefficient-two failure of the beta cocycle.

All calculations take place in (Z/4)[(Z/15)^k].  Thus this tests
the coefficient-two block without using a pro-two character to
distinguish prime-to-two idempotents.
"""
from collections import defaultdict
from pathlib import Path
import json

MOD=4
N=15
def add(a,b,scale=1):
    r=defaultdict(int,a)
    for k,v in b.items():r[k]=(r[k]+scale*v)%MOD
    return {k:v for k,v in r.items() if v}
def mul(a,b):
    r=defaultdict(int)
    for x,u in a.items():
        for y,v in b.items():
            z=tuple((i+j)%N for i,j in zip(x,y))
            r[z]=(r[z]+u*v)%MOD
    return {k:v for k,v in r.items() if v}

# 225^{-1}=1 modulo four.  The trace of omega^k is 2 or -1.
e={(i,j):(2 if (i+j)%3==0 else 3)
   for i in range(N) for j in range(N)}
assert mul(e,e)==e
beta=add({(0,0):1},e,-2)
assert mul(beta,beta)=={(0,0):1}
def subst(rule):
    r=defaultdict(int)
    for (i,j),v in beta.items():
        k=tuple(z%N for z in rule(i,j));r[k]=(r[k]+v)%MOD
    return {k:v for k,v in r.items() if v}
lhs=mul(subst(lambda i,j:(i,j,0)),subst(lambda i,j:(i,i,j)))
rhs=mul(subst(lambda i,j:(0,i,j)),subst(lambda i,j:(i,j,j)))
diff=add(lhs,rhs,-1)
assert diff

# Independently evaluate on a genuine order-three/order-five pair in
# the unramified quartic ring Z/4[t]/(t^4+t+1).  Squaring a lift of
# the primitive residue root removes the principal-unit factor.
def rm(a,b):
    z=[0]*7
    for i,u in enumerate(a):
        for j,v in enumerate(b):z[i+j]=(z[i+j]+u*v)%4
    for i in range(6,3,-1):
        z[i-3]=(z[i-3]-z[i])%4;z[i-4]=(z[i-4]-z[i])%4
    return tuple(z[:4])
one=(1,0,0,0)
def rp(a,n):
    r=one
    while n:
        if n&1:r=rm(r,a)
        a=rm(a,a);n//=2
    return r
zeta=rp((0,1,0,0),2)
assert rp(zeta,15)==one and all(rp(zeta,n)!=one for n in (1,3,5))
omega=rp(zeta,5);eta=rp(zeta,3)
def ev(poly,values):
    out=[0]*4
    for exponents,c in poly.items():
        val=one
        for a,k in zip(values,exponents):val=rm(val,rp(a,k))
        out=[(u+c*v)%4 for u,v in zip(out,val)]
    return tuple(out)
lv=ev(lhs,(omega,omega,eta));rv=ev(rhs,(omega,omega,eta))
assert lv==(3,0,0,0) and rv==one
out=dict(ring='(Z/4)[(Z/15)^3]',idempotent_verified=True,
         involution_verified=True,nonzero_difference_coefficients=len(diff),
         first_difference={'exponent':list(min(diff)),'coefficient':diff[min(diff)]},
         evaluation_ring='Z/4[t]/(t^4+t+1)',omega=list(omega),eta=list(eta),
         omega_order=3,eta_order=5,lhs=list(lv),rhs=list(rv),
         scope='Exact finite coefficient-two beta-cocycle obstruction')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
