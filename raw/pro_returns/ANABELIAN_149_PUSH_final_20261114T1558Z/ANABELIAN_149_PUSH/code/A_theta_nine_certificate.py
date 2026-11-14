#!/usr/bin/env python3
"""Exact polynomial/divisor inputs for the nine-torsion theta point."""
from pathlib import Path
import json

MOD=31
def mul(a,b):
    r=0
    while b:
        if b&1:r^=a
        b>>=1;a<<=1
        if a&16:a^=MOD
    return r
def power(a,n):
    r=1
    while n:
        if n&1:r=mul(r,a)
        a=mul(a,a);n>>=1
    return r
def inv(a):
    assert a
    return power(a,14)
def addp(a,b):
    r=[0]*max(len(a),len(b))
    for i,v in enumerate(a):r[i]^=v
    for i,v in enumerate(b):r[i]^=v
    while r and not r[-1]:r.pop()
    return r
def mulp(a,b):
    if not a or not b:return []
    r=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):r[i+j]^=mul(u,v)
    while r and not r[-1]:r.pop()
    return r
def evalp(a,x):
    r=0
    for v in reversed(a):r=mul(r,x)^v
    return r

t=2;alpha=t^inv(t);t2=mul(t,t);f0=t^1
assert power(t,5)==1 and t!=1
assert mul(alpha,alpha)^alpha^1==0
assert alpha==13
assert t^inv(t)^mul(alpha,inv(t^1))==f0
trace=0;s=f0
for _ in range(4):trace^=s;s=mul(s,s)
assert trace==1

b=[t2,t2^t^1,t2^t^1,1]
a=[t2,t,t,1]
u=[0,1,1];F=[1,1^alpha,1,1]
N=addp(mulp(u,addp(mulp(a,a),mulp(a,b))),
       mulp(mulp(b,b),addp(F,[mul(f0,z) for z in u])))
rhs=[1]
for _ in range(9):rhs=mulp(rhs,[t,1])
assert N==rhs
assert evalp(a,t)==0 and evalp(b,t)==1
assert evalp(b,0)==t2 and evalp(b,1)==1^t2
assert evalp(b,0) and evalp(b,1)

orbits=[];remaining=set(range(1,9))
while remaining:
    i=min(remaining);O=[];j=i
    while j not in O:O.append(j);j=2*j%9
    remaining-=set(O);orbits.append(O)
assert orbits==[[1,2,4,8,7,5],[3,6]]
kernel=[k for k in range(9) if all(i*k%9==0 for i in [3,6])]
assert kernel==[0,3,6]

def count_curve(d,poly):
    q=1<<d
    def mm(a,b):
        r=0
        while b:
            if b&1:r^=a
            b>>=1;a<<=1
            if a&q:a^=poly
        return r
    def pw(a,n):
        r=1
        while n:
            if n&1:r=mm(r,a)
            a=mm(a,a);n>>=1
        return r
    al=next(a for a in range(q) if mm(a,a)^a==1)
    count=3
    for x in range(2,q):
        f=x^pw(x,q-2)^mm(al,pw(x^1,q-2))
        count+=sum(mm(y,y)^y==f for y in range(q))
    return count

counts=[count_curve(2,7),count_curve(4,19)]
assert counts==[5,15]
out={"status":"PASS","field_polynomial":"t^4+t^3+t^2+t+1",
     "alpha_binary":alpha,"a_coefficients":a,"b_coefficients":b,
     "norm_numerator_coefficients":N,"norm_rhs_coefficients":rhs,
     "local_values":{"a(t)":evalp(a,t),"b(t)":evalp(b,t),
                     "b(0)":evalp(b,0),"b(1)":evalp(b,1)},
     "trace_F16_F2_of_t_plus_1":trace,"doubling_orbits_mod9":orbits,
     "kernel_exponents":[0,3,6],"base_two_rank":2,"cover_two_rank":4,
     "cover_genus":10,"connected_top_prym_dimension":6,
     "connected_top_prym_two_rank":0,"curve_point_counts":dict(zip(["F4","F16"],counts)),
     "scope":"Exact algebraic inputs. Divisor, line-bundle order, cohomology, and section arguments are in audit/A_theta_nine_candidate.md."}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
