#!/usr/bin/env python3
"""Exact certificates used in A.11--A.16; no supplied code is imported."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import json
import sympy as S

def add(*args):
    r=defaultdict(int)
    for a in args:
        for w,c in a.items():r[w]+=c
    return {w:c for w,c in r.items() if c}
def scale(a,c):return {w:c*v for w,v in a.items() if c*v}
def mul(a,b):
    r=defaultdict(int)
    for u,c in a.items():
        for v,d in b.items():r[u+v]+=c*d
    return dict(r)
def bracket(a,b):return add(mul(a,b),scale(mul(b,a),-1))
def deriv(a,dx,dy):
    r={}
    for w,c in a.items():
        for j,letter in enumerate(w):
            image=dx if letter=='x' else dy
            r=add(r,{w[:j]+v+w[j+1:]:c*d for v,d in image.items()})
    return r
def lyndon(w):return all(w<w[j:] for j in range(1,len(w)))
def L(w):
    if len(w)==1:return {w:1}
    j=next(j for j in range(1,len(w)) if lyndon(w[j:]))
    return bracket(L(w[:j]),L(w[j:]))
x,y=L('x'),L('y')
omega=bracket(x,y)
ad=lambda a,b:bracket(a,b)
e4x=ad(x,ad(x,ad(x,ad(x,y))))
e4y=add(ad(y,ad(x,ad(x,ad(x,y)))),scale(ad(omega,ad(x,ad(x,y))),-1))
Tx=add(deriv(e4x,y,{}),scale(e4y,-1))
Ty=deriv(e4y,y,{})
assert not deriv(omega,Tx,Ty)
assert Tx==add(scale(L('xxxyy'),-2),scale(L('xxyxy'),-1))
assert Ty==add(scale(L('xxyyy'),2),scale(L('xyxyy'),3))
ax=bracket(x,L('xxyy'))
words=sorted(set(ax)|set(Tx))
matrix=S.Matrix([[ax.get(w,0),Tx.get(w,0)] for w in words])
assert matrix.rank()==2

def points(p,coeff,degree):
    infinity=1 if degree%2 else 2
    n=infinity
    for z in range(p):
        q=sum(a*pow(z,j,p) for j,a in coeff.items())%p
        n+=1 if q==0 else 2 if pow(q,(p-1)//2,p)==1 else 0
    return n
counts={}
for name,coeff,degree,primes in [
    ('S3_complement',{3:1,1:-3,0:6},3,[5,11]),
    ('D8_nonstable_complement',{4:1,2:-4,0:8},4,[5,7]),
]:
    for p in primes:
        n=points(p,coeff,degree);a=p+1-n;disc=a*a-4*p
        assert a%p!=0
        counts[f'{name}_p{p}']={'points':n,'trace':a,'discriminant':disc}
assert [counts[f'S3_complement_p{p}']['discriminant'] for p in [5,11]]==[-19,-35]
assert [counts[f'D8_nonstable_complement_p{p}']['discriminant'] for p in [5,7]]==[-16,-12]

# F25 = F5[t]/(t^2+t+1). Multiplication by t is a fixed-point-free
# order-three automorphism of the additive group.
els=list(product(range(5),range(5)))
def plus(u,v):return tuple((u[j]+v[j])%5 for j in range(2))
def neg(u):return tuple(-a%5 for a in u)
def tau(u):return (-u[1]%5,(u[0]-u[1])%5)
def act(u,k):
    for _ in range(k%3):u=tau(u)
    return u
G=list(product(els,range(3)))
def gm(g,h):return (plus(g[0],act(h[0],g[1])),(g[1]+h[1])%3)
def gi(g):return (act(neg(g[0]),-g[1]),-g[1]%3)
def comm(g,h):return gm(gm(gm(g,h),gi(g)),gi(h))
def closure(gens):
    seen={((0,0),0)};todo=list(seen)
    while todo:
        g=todo.pop()
        for h in gens:
            z=gm(g,h)
            if z not in seen:seen.add(z);todo.append(z)
    return seen
gp=closure({comm(g,h) for g in G for h in G})
gpp=closure({comm(g,h) for g in gp for h in gp})
gamma3=closure({comm(g,h) for g in gp for h in G})
assert len(gp)==25 and len(gpp)==1 and gamma3==gp
assert len(closure([((0,0),1),((1,0),1)]))==75
out={'degree_four':{'T_x_Lyndon':{'xxxyy':-2,'xxyxy':-1},
                    'T_y_Lyndon':{'xxyyy':2,'xyxyy':3},
                    'rank_ad_x_L4_and_Tx':2,'boundary_derivative':0},
     'ordinary_Frobenius_counts':counts,
     'order_75_residual_detector':{'order':75,'derived_order':len(gp),
        'second_derived_order':len(gpp),'third_lower_central_order':len(gamma3)}}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
