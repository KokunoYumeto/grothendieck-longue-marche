#!/usr/bin/env python3
"""Exploratory exact point counts. No arithmetic classification is inferred."""
import json
from pathlib import Path
from sympy import primerange

def leg(a,p):
    a%=p
    return 0 if a==0 else (1 if pow(a,(p-1)//2,p)==1 else -1)

def roots3(p):
    return [a for a in range(p) if (3*a**4-6*a*a-1)%p==0]

def phi_counts(p,q):
    inv27=pow(27,-1,p)
    A=(9-30*q*q)%p; B=(42*q-70*q**3)%p
    C=lambda u:(inv27*pow(u,9,p)-q*pow(u,6,p)+(3-q*q)*pow(u,3,p)+15*q-7*q**3)%p
    N1D=1+sum(1+leg(C(u),p) for u in range(p))
    N1E=1+sum(1+leg(x**3-x,p) for x in range(p))
    N1E0=1+sum(1+leg(x**3+108,p) for x in range(p))
    n=next(a for a in range(2,p) if leg(a,p)==-1)
    def mul(a,b): return ((a[0]*b[0]+n*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
    def add(a,b): return ((a[0]+b[0])%p,(a[1]+b[1])%p)
    def scale(a,k): return (a[0]*k%p,a[1]*k%p)
    def pw(a,k):
        o=(1,0)
        while k:
            if k&1:o=mul(o,a)
            a=mul(a,a);k//=2
        return o
    def leg2(a):
        if a==(0,0):return 0
        z=pw(a,(p*p-1)//2)
        assert z in [(1,0),(p-1,0)]
        return 1 if z==(1,0) else -1
    N2D=1
    for a in range(p):
        for b in range(p):
            u3=pw((a,b),3);u6=mul(u3,u3);u9=mul(u3,u6)
            z=add(add(scale(u9,inv27),scale(u6,-q)),add(scale(u3,3-q*q),( (15*q-7*q**3)%p,0)))
            N2D+=1+leg2(z)
    aE=p+1-N1E;a0=p+1-N1E0
    s1=p+1-N1D-aE-a0
    s2=p*p+1-N2D-(aE*aE-2*p)-(a0*a0-2*p)
    e2=(s1*s1-s2)//2
    assert (s1*s1-s2)%2==0
    # Candidate surface factor after the two known elliptic isogeny factors.
    P=[1,-s1,e2,-p*s1,p*p]
    square=(s1%2==0 and e2==s1*s1//4+2*p)
    return {'p':p,'kernel_x':q,'N1_genus4':N1D,'N2_genus4':N2D,'trace_E':aE,'trace_E0':a0,'candidate_surface_weil_polynomial':P,'square_elliptic_polynomial':square,'candidate_elliptic_trace':s1//2 if square else None}

out=[]
for p in primerange(7,250):
    if p%12!=1:continue
    rs=roots3(p)
    if len(rs)!=4 or not all(leg(q**3-q,p)==1 for q in rs):continue
    for q in rs[:1]:
        a=phi_counts(p,q);out.append(a);print(a,flush=True)
res={'status':'exploratory exact counts','rows':out}
Path(__file__).with_suffix('.json').write_text(json.dumps(res,indent=2)+'\n')
