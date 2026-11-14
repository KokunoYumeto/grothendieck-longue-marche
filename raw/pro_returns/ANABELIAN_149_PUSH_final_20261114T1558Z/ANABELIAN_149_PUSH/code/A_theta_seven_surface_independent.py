#!/usr/bin/env python3
"""Independent theta-seven surface review: rational identities and a quadratic F16 tower.

Does not import the candidate verifier. Universal rational identities are in
GF(2)(x,t). Finite norm checks evaluate a degree-at-most-seven polynomial at
all sixteen field elements, independently of coefficient multiplication.
"""
import json
from pathlib import Path
from itertools import product
from sympy.polys.domains import GF
from sympy.polys.fields import field

K, x, t = field("x,t", GF(2))
u = x*(x+1)
q = (x+t)**7/u
H = u**3/((x+t)**5*(x*x+t)**2)
qp = (x+t)**6*(x*x+t)/u**2
rho = (x+t)*u/(x*x+t)
assert q.diff(x) == qp
assert H == q/qp**2
assert H.diff(x) == u**2/((x+t)**6*(x*x+t))
assert H*qp == rho and H*q == rho**2
assert H*(x+t)**4*(x*x+t)**2+u**2 == u**2*(x*x+t)/(x+t)
U=t*(t+1)
aa=1/U**2
bb=t**3/(t+1)**2
cc=(t+1)**3/t**2
ph=aa*x+bb/x+cc/(x+1)
pt=aa*(t+1)
assert aa*t+bb/t+cc/(t+1) == pt
z=x+t
assert u*(ph+pt) == z+aa*z**3
A=x+t
B=x*x+t
assert u*(A*A+A*B)+B*B*u*(ph+pt) == aa*(x+t)**7
assert (aa+bb+cc)**3+aa*bb*cc == (U**3+U+1)/U**3

# F4 = F2[a]/(a^2+a+1), F16 = F4[w]/(w^2+w+a).
F4mul = ((0,0,0,0),(0,1,2,3),(0,2,3,1),(0,3,1,2))
def plus(a,b): return (a[0]^b[0],a[1]^b[1])
def times(a,b):
    v=F4mul[a[1]][b[1]]
    return (F4mul[a[0]][b[0]]^F4mul[2][v],
            F4mul[a[0]][b[1]]^F4mul[a[1]][b[0]]^v)
ZERO=(0,0); ONE=(1,0); W=(0,1)
def powe(a,n):
    r=ONE
    while n:
        if n&1:r=times(r,a)
        a=times(a,a);n//=2
    return r
def quotient(a,b):
    assert b!=ZERO
    return times(a,powe(b,14))
def summ(*args):
    out=ZERO
    for a in args:out=plus(out,a)
    return out
F=list(product(range(4),repeat=2))
assert summ(powe(W,4),W,ONE)==ZERO
assert all(a==ZERO or powe(a,15)==ONE for a in F)
def hval(y,tt):
    return quotient(powe(times(y,plus(y,ONE)),3),
                    times(powe(plus(y,tt),5),powe(plus(powe(y,2),tt),2)))
def obstruction(a,b,c):
    return plus(powe(summ(a,b,c),3),times(times(a,b),c))
def verify_norm(tt,a,b,c,Afunc,Bfunc):
    pht=summ(times(a,tt),quotient(b,tt),quotient(c,plus(tt,ONE)))
    assert Afunc(tt)==ZERO and Bfunc(tt)!=ZERO
    assert Bfunc(ZERO)!=ZERO and Bfunc(ONE)!=ZERO
    # Degree bound <=7: u(A^2+AB)+B^2(u phi+u phi(t))-a(x+t)^7.
    for xx in F:
        ux=times(xx,plus(xx,ONE))
        fx=summ(times(a,powe(xx,3)),times(a,powe(xx,2)),
                times(plus(b,c),xx),b)
        av,bv=Afunc(xx),Bfunc(xx)
        left=plus(times(ux,plus(powe(av,2),times(av,bv))),
                  times(powe(bv,2),plus(fx,times(pht,ux))))
        assert left==times(a,powe(plus(xx,tt),7))
    return pht

pairs=0;outside=0;example=None
target=(W,plus(powe(W,3),W),summ(powe(W,3),powe(W,2),ONE))
for tt in F:
    if tt in (ZERO,ONE):continue
    good=[r for r in F if r not in (ZERO,ONE,tt) and powe(r,2)!=tt]
    for i,r in enumerate(good):
        for s in good[i+1:]:
            val=hval(r,tt)
            if val!=hval(s,tt):continue
            e=plus(r,s);kap=times(powe(e,2),val)
            a=kap
            b=quotient(times(kap,powe(tt,7)),powe(times(r,s),2))
            c=quotient(times(kap,powe(plus(tt,ONE),7)),
                       powe(times(plus(r,ONE),plus(s,ONE)),2))
            rr=quotient(times(plus(r,tt),times(r,plus(r,ONE))),
                        plus(powe(r,2),tt))
            rs=quotient(times(plus(s,tt),times(s,plus(s,ONE))),
                        plus(powe(s,2),tt))
            const=plus(quotient(rr,plus(tt,r)),quotient(rs,plus(tt,s)))
            BF=lambda xx:times(plus(xx,r),plus(xx,s))
            AF=lambda xx:summ(times(rr,plus(xx,s)),times(rs,plus(xx,r)),
                              times(const,BF(xx)))
            pht=verify_norm(tt,a,b,c,AF,BF)
            obs=obstruction(a,b,c)
            pairs+=1;outside+=obs!=ZERO
            if tt==target[0] and {r,s}==set(target[1:]):
                assert (a,b,c)==(plus(powe(W,2),W),
                                summ(powe(W,3),powe(W,2),ONE),
                                summ(powe(W,3),W,ONE))
                assert obs==summ(powe(W,2),W,ONE)
                example={"parameters":[tt,r,s],"coefficients":[a,b,c],
                         "H_value":val,"phi_t":pht,"obstruction":obs}
assert example is not None and pairs==12 and outside==12
oneparam=0
for tt in F:
    if tt in (ZERO,ONE):continue
    UU=times(tt,plus(tt,ONE))
    a=quotient(ONE,powe(UU,2))
    b=quotient(powe(tt,3),powe(plus(tt,ONE),2))
    c=quotient(powe(plus(tt,ONE),3),powe(tt,2))
    AF=lambda xx:plus(xx,tt)
    BF=lambda xx:plus(powe(xx,2),tt)
    assert verify_norm(tt,a,b,c,AF,BF)==times(a,plus(tt,ONE))
    oneparam+=1
out={"status":"PASS","universal_rational_identities":True,
     "finite_field":"F4[w]/(w^2+w+a), a^2+a+1=0",
     "surface_unordered_pairs":pairs,"outside_cubic":outside,
     "one_parameter_checks":oneparam,
     "norm_method":"Degree<=7 numerator evaluated at all16 field elements",
     "example_in_quadratic_tower":example,
     "scope":"Independent algebra; the audit review supplies etaleness, divisor, dimension, and A1 arguments."}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))

