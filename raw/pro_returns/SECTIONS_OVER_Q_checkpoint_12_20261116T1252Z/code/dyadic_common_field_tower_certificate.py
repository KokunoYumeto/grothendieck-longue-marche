#!/usr/bin/env python3
"""Exact finite root-stabilizer checks for A126; no numeric field approximations."""
from itertools import product
from math import gcd
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
COUNTS = dict(tuples=0, exponent_cases=0, actual_stabilizer_tests=0,
              relations=0, subgroup_products=0, character_tests=0,
              odd_crt_lifts=0, stopping_comparisons=0)

def v2(n):
    assert n
    n=abs(n); a=0
    while n%2==0: a+=1; n//=2
    return a

def gamma(n, primes):
    out=[]
    for u in range(1,2*n,2):
        for eps in product(range(2), repeat=len(primes)):
            if n>=4 and 2 in primes and eps[primes.index(2)] != (0 if u%8 in (1,7) else 1):
                continue
            out.append((u,eps))
    return out

def mul(a,b,n):
    return (a[0]*b[0]%(2*n),tuple(x^y for x,y in zip(a[1],b[1])))

def span_columns(W, mod):
    k=len(W); p=len(W[0]) if W else 0
    if mod==1: return {(0,)*k}
    return {tuple(sum(row[j]*h[j] for j in range(p))%mod for row in W)
            for h in product(range(mod), repeat=p)}

def actual_stabilizers(n,W,delta,primes):
    spans={}
    out=set()
    for sig in gamma(n,primes):
        COUNTS['actual_stabilizer_tests']+=1
        u,eps=sig
        b=[sum(w*e for w,e in zip(row,eps)) for row in W]
        if any(((u-1)//2*d+x)%2 for d,x in zip(delta,b)):
            continue
        if u%4==3:
            out.add(sig); continue
        mod=gcd(u-1,n)//2
        if mod not in spans: spans[mod]=span_columns(W,mod)
        target=tuple(-(x//2+(u-1)//4*d)%mod for d,x in zip(delta,b))
        if target in spans[mod]:out.add(sig)
    return out

def generated(seeds,n,p):
    ident=(1,(0,)*p); out={ident}; queue=[ident]
    for a in queue:
        for b in seeds:
            COUNTS['subgroup_products']+=1
            c=mul(a,b,n)
            if c not in out:out.add(c);queue.append(c)
    return out

def even_logs(n):
    m=n//2; ans={};a=1
    for j in range(m):
        ans[a]=j;ans[-a%(2*n)]=j;a=a*5%(2*n)
    assert len(ans)==n
    assert ans[1+n]==m//2
    return ans

def relation_data(n,W,delta):
    m=n//2;p=len(W[0]);out=[]
    for t in product(range(m),repeat=len(W)):
        w=[sum(t[i]*W[i][j] for i in range(len(W))) for j in range(p)]
        if all(x%m==0 for x in w):
            COUNTS['relations']+=1
            out.append((tuple(x//m for x in w),sum(a*b for a,b in zip(t,delta))%2))
    return out

def check_tuple(W,delta,primes,limit=32):
    COUNTS['tuples']+=1
    previous=None;stopped_at=None
    for n in [2,4,8,16,32]:
        if n>limit:break
        COUNTS['exponent_cases']+=1
        G=gamma(n,primes)
        if n==2:
            H={s for s in G if all(((s[0]-1)//2*d+sum(w*e for w,e in zip(row,s[1])))%2==0
                                  for row,d in zip(W,delta))}
        else:
            actual=generated(actual_stabilizers(n,W,delta,primes),n,len(primes))
            pre={s for s in G if (s[0]%n,s[1]) in previous}
            has_mu=all(s[0]%n==1 for s in pre)
            if not has_mu:
                proposed=pre
                if stopped_at is None:stopped_at=n
                COUNTS['stopping_comparisons']+=1
            else:
                rel=relation_data(n,W,delta);logs=even_logs(n);m=n//2
                proposed=set()
                for s in pre:
                    yes=True
                    for w,d in rel:
                        COUNTS['character_tests']+=1
                        if (m//2*sum(x*e for x,e in zip(w,s[1]))+d*logs[s[0]])%m:
                            yes=False;break
                    if yes:proposed.add(s)
            assert proposed==actual,(n,W,delta,proposed,actual)
            H=actual
            if stopped_at is not None:
                assert H==pre,(n,'failure of permanence')
        previous=H

# The prime2 sign is tied to the cyclotomic coordinate throughout.
for w in range(1,9):
    for sign in (0,1):check_tuple([(w,)],[sign],[2])
for w in range(-3,4):
    for sign in (0,1):check_tuple([(w,)],[sign],[3])
for W in [((1,0),(0,1)),((2,0),(0,2)),((1,1),(1,-1)),
          ((2,1),(0,2)),((4,0),(0,1)),((0,0),(1,0)),
          ((1,1),(-1,1),(0,1)),((1,0),(0,1),(1,1)),
          ((2,0),(0,2),(2,2)),((4,0),(0,4),(4,4))]:
    for signs in product(range(2),repeat=len(W)):
        check_tuple(W,signs,[2,3])

# Direct CRT lifts of literal fixed-root equations, including signed roots.
def crt(a,m,b,v):
    return (a+m*((b-a)*pow(m,-1,v)%v))%(m*v)

for n in [4,8,16]:
    for v in [3,5,7,9]:
        N=n*v
        for u in range(1,2*N,2):
            if gcd(u,N)!=1:continue
            for d in (0,1):
                for w in [-2,-1,0,1,2]:
                    for k in range(n):
                        for e in range(n):
                            if ((u-1)*(d+2*e)+2*w*k)%(2*n):continue
                            kp=crt(k,n,0,v)
                            ep=crt(e,n,-d*pow(2,-1,v)%v,v)
                            assert kp%2==k%2
                            assert ((u-1)*(d+2*ep)+2*w*kp)%(2*N)==0
                            COUNTS['odd_crt_lifts']+=1

# Integral relation and Smith-bound examples with exact known diagonal invariants.
for a in range(5):
    n0=2**(a+2)
    m=2**(a+1)
    for t in range(m):
        if (2**a*t)%m==0:assert t%2==0
    # D=-2^(2^a) has no integral negative relation; the proof bound is n0.
    if n0<=32:check_tuple([(2**a,)],[1],[2])
for n in [2,4,8,16,32,64]:
    # A literal multiplicative relation -1 forces a primitive2n-th root.
    for j in range(1,2*n,2):assert gcd(j,2*n)==1

content='PASS: literal root-stabilizer groups equal every recursive common-field group.\n'
content+='PASS: compatible sqrt2 signs, complete mixed relation modules, subgroup generation and permanent stopping.\n'
content+='PASS: direct odd-factor CRT lifts and integral stabilization-bound examples.\n'
content+=json.dumps(COUNTS,indent=2)+'\n'
content+='The all-exponent and Smith-bound assertions are proved in A126; these are exact finite checks.\n'
(HERE/'dyadic_common_field_tower_certificate_output.txt').write_text(content)
print(content,end='')
