#!/usr/bin/env python3
"""Exact Frobenius identities bounding the three-primary theta packet."""
from pathlib import Path
from math import gcd
import json

def trim(a):
    a=a[:]
    while a and a[-1]==0:a.pop()
    return a
def add(a,b):
    r=[0]*max(len(a),len(b))
    for i,v in enumerate(a):r[i]+=v
    for i,v in enumerate(b):r[i]+=v
    return trim(r)
def mul(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):r[i+j]+=u*v
    return trim(r)
def monic_div(a,b):
    assert b[-1]==1
    r=trim(a);q=[0]*max(0,len(r)-len(b)+1)
    while len(r)>=len(b):
        d=len(r)-len(b);c=r[-1];q[d]=c
        for i,v in enumerate(b):r[i+d]-=c*v
        r=trim(r)
    return trim(q),r

def count(d,mod):
    Q=1<<d
    def mm(a,b):
        r=0
        while b:
            if b&1:r^=a
            b>>=1;a<<=1
            if a&Q:a^=mod
        return r
    def pp(a,n):
        r=1
        while n:
            if n&1:r=mm(r,a)
            a=mm(a,a);n>>=1
        return r
    alpha=next(a for a in range(Q) if mm(a,a)^a==1)
    N=3
    for x in range(2,Q):
        v=x^pp(x,Q-2)^mm(alpha,pp(x^1,Q-2));tr=0
        for _ in range(d):tr^=v;v=mm(v,v)
        assert tr in [0,1]
        N+=2 if tr==0 else 0
    return N

N1,N2=count(2,7),count(4,19)
q=4;a1=N1-q-1;a2=(a1*a1+N2-q*q-1)//2
P=[q*q,q*a1,a2,a1,1]
assert (N1,N2)==(5,15) and P==[16,0,-1,0,1]
A=[-1]+[0]*11+[1]
Q1,R1=monic_div(A,P)
assert R1==[-3345,0,705] and all(v%3==0 for v in R1)
Q2,R2=monic_div(add(mul(A,[176,0,47]),[27*41440]),P)
assert not R2
assert Q2==[69919,0,4367,0,-4097,0,-529,0,223,0,47]
assert gcd(41440,3)==1
out={"status":"PASS","counts":{"F4":N1,"F16":N2},
     "frobenius_polynomial_low_first":P,
     "X12_minus_1_quotient":Q1,"X12_minus_1_remainder":R1,
     "remainder_divisible_by_3":True,
     "annihilator_multiplier":[176,0,47],"constant":27*41440,
     "annihilator_quotient":Q2,"annihilator_remainder":R2,
     "prime_to_3_factor":41440,"three_primary_theta_exponent_bound":27,
     "scope":"Exact identities only; the Frobenius orbit/intersection proof supplies rationality of the theta packet. No exact order27 point is inferred."}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
