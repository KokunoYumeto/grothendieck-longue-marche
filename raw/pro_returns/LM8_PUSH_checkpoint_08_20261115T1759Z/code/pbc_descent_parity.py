#!/usr/bin/env python3
"""Explore Delta after descent using actual two peripheral frames.

This is a necessary finite framed locus. A row is not asserted to
lift to a full peripheral automorphism. SL2 matrices retain the
central signs discarded by separate projective reductions.
"""
import itertools
import json
from pathlib import Path

n=12
I=(1,0,0,1)
def mm(a,b):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%n
                 for i in range(2) for j in range(2))
def mi(a):return (a[3],-a[1]%n,-a[2]%n,a[0])
def neg(a):return tuple(-x%n for x in a)
def pw(a,k):
    r=I
    while k:
        if k&1:r=mm(r,a)
        a=mm(a,a);k//=2
    return r
def cj(a,b):return mm(mm(a,b),mi(a))
def gen(gs):
    seen={I};todo=[I]
    while todo:
        a=todo.pop()
        for b in gs:
            c=mm(a,b)
            if c not in seen:seen.add(c);todo.append(c)
    return seen
def der(g):return gen(list({mm(mm(a,b),mm(mi(a),mi(b))) for a in g for b in g}))
def mod(a,m):return tuple(x%m for x in a)
U=(1,1,0,1);S=(0,1,11,0);R=(0,11,1,11);tau=mi(U)
assert mm(S,R)==tau and mm(S,tau)==neg(R) and pw(R,3)==I
G=gen([S,tau]);basic=mm(mm(S,tau),mm(mi(S),mi(tau)))
D=gen(list({cj(g,basic) for g in G}))
assert len(G)==1152 and len(D)==96
nilres={a for a in D if mod(a,3)==mod(I,3)}
assert len(nilres)==12
def canonical(a):
    assert mod(a,2)==mod(I,2)
    assert a[0]%4 in (1,3) and a[3]%4==a[0]%4
    return a if a[0]%4==1 else neg(a)
Rpow=[pw(R,k) for k in range(3)]
Spow=[pw(S,k) for k in range(4)]
rows=[];rejected={}
for v in sorted(D):
    image_y=cj(mi(v),tau)
    if len(gen([S,image_y]))!=1152:continue
    ts=[t for t in range(12) if cj(pw(U,t),S)==cj(v,S)]
    if len(ts)!=1:
        rejected[str((v,len(ts)))]=1
        continue
    t=ts[0];V=pw(U,t)
    for h in sorted(D):
        if mm(S,image_y)!=cj(mi(h),mm(S,tau)):continue
        assert mod(v,2)==mod(I,2)
        k=next(k for k in range(3) if mod(h,2)==mod(Rpow[k],2))
        A=mm(mm(v,mi(h)),Rpow[k]);beta=v
        T=mm(mi(canonical(A)),V);W=mm(mi(canonical(beta)),V)
        assert mm(T,R)==mm(R,T) and mm(W,S)==mm(S,W)
        if mod(T,4)!=mod(I,4) or mod(W,4)!=mod(I,4):
            rejected[str(('mod4',v,h,t,k,T,W))]=1
            continue
        tv=((T[0]-T[1])%3,(T[2]-T[3])%3)
        e3=0 if tv==(1,2) else 1
        assert tv in ((1,2),(2,1))
        j=next(j for j in range(4) if mod(W,3)==mod(Spow[j],3))
        e2=j%2
        rows.append(dict(v=v,h=h,t=t,k=k,T=T,W=W,eps3=e3,eps2=e2,
                         Delta=e3^e2,both_in_nilres=v in nilres and h in nilres))
out=dict(group_order=len(G),derived_order=len(D),nilres_order=len(nilres),
         finite_rows=len(rows),parity_counts={str(e):sum(r['Delta']==e for r in rows) for e in (0,1)},
         nilres_rows=sum(r['both_in_nilres'] for r in rows),
         nilres_parity_counts={str(e):sum(r['both_in_nilres'] and r['Delta']==e for r in rows) for e in (0,1)},
         rows=rows,rejected_covariances=rejected,
         scope='Necessary framed finite equations only; no full lift asserted')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('rows','rejected_covariances')},indent=2))
print('rejected_covariance_count',len(rejected))
for e in (0,1):
    print('nilres example',e,next((r for r in rows if r['both_in_nilres'] and r['Delta']==e),None))
