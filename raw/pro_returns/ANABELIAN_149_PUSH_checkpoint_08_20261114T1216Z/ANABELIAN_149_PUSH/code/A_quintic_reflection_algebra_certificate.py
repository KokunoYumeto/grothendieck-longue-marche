#!/usr/bin/env python3
"""Exact rational-polynomial certificate for the quintic reflection example.

No symbolic algebra package is used. The Weil polynomial is irreducible
modulo7. Its nontrivial eigenvalue-ratio polynomial has degree8 and is coprime
to every possible cyclotomic polynomial. Full Bezout identities are saved.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def add(a,b):
    c=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=x
    return trim(c)

def neg(a):return [-x for x in a]
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)

def div(a,b):
    a=list(map(F,trim(a)));b=list(map(F,trim(b)));assert b!=[0]
    q=[F(0)]*max(1,len(a)-len(b)+1)
    while a!=[0] and len(a)>=len(b):
        i=len(a)-len(b);v=a[-1]/b[-1];q[i]+=v
        for j,x in enumerate(b):a[i+j]-=v*x
        a=trim(a)
    return trim(q),a

def xgcd(a,b):
    r0,r1=list(map(F,a)),list(map(F,b));s0,s1=[F(1)],[F(0)];t0,t1=[F(0)],[F(1)]
    while r1!=[0]:
        q,r=div(r0,r1)
        r0,r1=r1,r;s0,s1=s1,add(s0,neg(mul(q,s1)));t0,t1=t1,add(t0,neg(mul(q,t1)))
    lead=r0[-1]
    return [v/lead for v in r0],[v/lead for v in s0],[v/lead for v in t0]

def cyclotomic(n,cache={}):
    if n in cache:return cache[n]
    f=[-1]+[0]*(n-1)+[1]
    for d in range(1,n):
        if n%d==0:
            f,r=div(f,cyclotomic(d));assert r==[0]
    assert all(x.denominator==1 for x in map(F,f))
    cache[n]=list(map(int,f));return cache[n]

def phi(n):
    ans=n;m=n;p=2
    while p*p<=m:
        if m%p==0:
            ans=ans//p*(p-1)
            while m%p==0:m//=p
        p+=1
    if m>1:ans=ans//m*(m-1)
    return ans

P=[4096,320,123,5,1]
mod_checks=[]
def modrem(a,b,p):
    a=trim([x%p for x in a]);b=trim([x%p for x in b])
    while a!=[0] and len(a)>=len(b):
        j=len(a)-len(b);v=a[-1]*pow(b[-1],-1,p)%p
        for i,x in enumerate(b):a[j+i]=(a[j+i]-v*x)%p
        a=trim(a)
    return a
for degree in [1,2]:
    for coeff in product(range(7),repeat=degree):
        f=list(coeff)+[1];rem=modrem(P,f,7);assert rem!=[0]
        mod_checks.append(dict(divisor=f,remainder=rem))
assert len(mod_checks)==56
q=64;s=-5;t=-5 # t_i=alpha_i+q/alpha_i have sum s and product t.
ss=s*s-2*t
C=[q,-t,ss-2*q,-t,q]
B=[q*q,-q*(ss-4*q),t*t-2*q*ss+6*q*q,-q*(ss-4*q),q*q]
assert C==[64,5,-93,5,64]
assert B==[4096,14144,20121,14144,4096]
ratio=mul(B,C)
orders=sorted({2**a*3**b*5**c*7**d for a in range(5) for b in range(3) for c in range(2) for d in range(2) if phi(2**a*3**b*5**c*7**d)<=8})
assert orders==[1,2,3,4,5,6,7,8,9,10,12,14,15,16,18,20,24,30]
bezout=[]
for n in orders:
    f=cyclotomic(n);g,u,v=xgcd(ratio,f);assert g==[1]
    assert add(mul(u,ratio),mul(v,f))==[1]
    bezout.append(dict(order=n,cyclotomic=f,u=[str(z) for z in u],v=[str(z) for z in v]))
result=dict(status='passed',weil_polynomial_low_to_high=P,
            irreducibility_mod7_cases=mod_checks,
            self_pair_ratio_polynomial=B,cross_pair_ratio_polynomial=C,
            squarefree_candidate_ratio_polynomial=[int(x) for x in ratio],
            exhaustive_cyclotomic_orders=orders,bezout_identities=bezout,
            ordinary_middle_coefficient=123,
            proof='audit/A_quintic_reflection_obstruction_candidate.md')
out=Path(__file__).with_suffix('.json');out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(status='passed',mod7_cases=len(mod_checks),cyclotomic_cases=len(bezout),output=str(out))))
