"""Exact finite certificates for E190--E191.

Braid equalities are certified by paths of defining positive relations
after explicit Garside-denominator clearing.  No finite braid quotient
or presumed faithful matrix representation substitutes for those paths.
The other checks are polynomial identities and exhaustive small rings.
"""
from collections import deque
from functools import lru_cache
from hashlib import sha256
from itertools import permutations, product
from pathlib import Path
import json
import sympy as sp


def neighbors(w):
    for i in range(len(w)-1):
        if abs(w[i]-w[i+1]) > 1:
            yield w[:i]+(w[i+1],w[i])+w[i+2:]
    for i in range(len(w)-2):
        a,b,c=w[i:i+3]
        if a==c and abs(a-b)==1:
            yield w[:i]+(b,a,b)+w[i+3:]


@lru_cache(None)
def path(start, finish):
    if start==finish:
        return (start,)
    assert len(start)==len(finish)
    parents=[{start:None},{finish:None}]
    fronts=[{start},{finish}]
    meet=None
    while meet is None:
        side=0 if len(fronts[0])<=len(fronts[1]) else 1
        new=set()
        for w in sorted(fronts[side]):
            for v in neighbors(w):
                if v in parents[side]:
                    continue
                parents[side][v]=w
                new.add(v)
                if v in parents[1-side]:
                    meet=v
                    break
            if meet is not None:
                break
        assert new or meet is not None
        fronts[side]=new
    a=[]; w=meet
    while w is not None:
        a.append(w); w=parents[0][w]
    a.reverse()
    b=[]; w=parents[1][meet]
    while w is not None:
        b.append(w); w=parents[1][w]
    ans=tuple(a+b)
    assert all(v in set(neighbors(w)) for w,v in zip(ans,ans[1:]))
    return ans


def invcount(p):
    return sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))


def right(p,i):
    p=list(p);p[i-1],p[i]=p[i],p[i-1];return tuple(p)


def left(p,i):
    return tuple(i+1 if a==i else i if a==i+1 else a for a in p)


ID=(1,2,3,4)
W0=(4,3,2,1)
simple={ID:()}
todo=deque([ID])
while todo:
    p=todo.popleft()
    for i in (1,2,3):
        q=right(p,i)
        if invcount(q)==invcount(p)+1 and q not in simple:
            simple[q]=simple[p]+(i,)
            todo.append(q)
assert len(simple)==24
DELTA=simple[W0]
twist=lambda w:tuple(4-i for i in w)
complements={i:simple[left(W0,i)] for i in (1,2,3)}
foundation=[]
for i in (1,2,3):
    foundation.append(path((i,)+complements[i],DELTA))
    foundation.append(path(DELTA+(i,),(4-i,)+DELTA))


def positive_fraction(w):
    """w = positive * Delta**(-k), using certified elementary identities."""
    pos=();k=0
    for i in w:
        if i>0:
            v=(i,)
        else:
            v=complements[-i]
        if k%2:
            v=twist(v)
        pos+=v
        if i<0:
            k+=1
    return pos,k


def greedy(w):
    """Only its recorded relation paths, not completeness, certify use."""
    factors=[right(ID,i) for i in w]
    proofs=[]
    while True:
        moved=False
        for j in range(len(factors)-1):
            u,v=factors[j:j+2]
            choices=[i for i in (1,2,3)
                     if invcount(left(v,i))==invcount(v)-1
                     and invcount(right(u,i))==invcount(u)+1]
            if not choices:
                continue
            i=choices[0]
            a,b=right(u,i),left(v,i)
            proofs.append(path(simple[u]+simple[v],simple[a]+simple[b]))
            factors[j:j+2]=[a]+([b] if b!=ID else [])
            moved=True
            break
        if not moved:
            break
    return tuple(simple[p] for p in factors),proofs


def inverse(w):
    return tuple(-i for i in reversed(w))


def equality(a,b):
    pa,ka=positive_fraction(a);pb,kb=positive_fraction(b)
    k=max(ka,kb)
    pa+=DELTA*(k-ka);pb+=DELTA*(k-kb)
    na,ca=greedy(pa);nb,cb=greedy(pb)
    assert na==nb,(a,b,na,nb)
    return {'left':a,'right':b,'denominator':k,
            'left_positive':pa,'right_positive':pb,
            'normal_factors':na,'local_paths':ca+cb}


a=(1,);b=(2,);c=(3,)
x=c+inverse(a)
y=a+b+a+inverse(c)+inverse(b)+inverse(a)
conj=lambda u,v:u+v+inverse(u)
claims={
    'a_x':(conj(a,x),x),
    'a_y':(conj(a,y),y+x),
    'b_x':(conj(b,x),x+inverse(y)),
    'b_y':(conj(b,y),y),
    'c_x':(conj(c,x),x),
    'c_y':(conj(c,y),x+y),
}
braids={name:equality(*words) for name,words in claims.items()}

# The signed matrices and the exact projective-affine marking.
I=(1,0,0,1);U=(1,1,0,1);L=(1,0,-1,1);R=(0,-1,1,1)
def mm(a,b,m):
    return tuple(v%m for v in
        (a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],
         a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]))
def pw(a,n,m):
    r=I
    for _ in range(n):
        r=mm(r,a,m)
    return r
def mv(a,v,m):
    return ((a[0]*v[0]+a[1]*v[1])%m,
            (a[2]*v[0]+a[3]*v[1])%m)
Rp=mm(U,L,12);S=mm(Rp,U,12);R0=tuple(-v%12 for v in Rp)
assert pw(R,3,12)==(11,0,0,11)
assert pw(Rp,3,12)==(11,0,0,11)
assert all(pw(Rp,k,4)!=I for k in range(1,6))
assert pw(Rp,6,4)==I
labels={None:(0,0),0:(1,0),2:(0,1),1:(1,1)}
def mobius(M,z):
    num,den=(M[0],M[2]) if z is None else (M[0]*z+M[1],M[2]*z+M[3])
    return None if den%3==0 else num*pow(den,-1,3)%3
affine_checks=0
for mat,t,A in [(S,(1,0),I),(R0,(1,0),pw(R,4,2)),
                ((1,-1,0,1),(0,0),R)]:
    for z,v in labels.items():
        w=mv(A,v,2)
        assert labels[mobius(mat,z)]==tuple((w[i]+t[i])%2 for i in range(2))
        affine_checks+=1
common_exponents=[]
for eps3,eps2,k in product(range(2),range(2),range(6)):
    line_condition=(k%2==eps3)
    mod4_condition=(pw(Rp,k,4)==tuple(((-1)**eps2)*v%4 for v in I))
    if line_condition and mod4_condition:
        assert eps3==eps2
        common_exponents.append((eps3,eps2,k))
assert common_exponents==[(0,0,0),(1,1,3)]

# Actual quartic birational coordinates; eliminate using its literal equation.
xx,tt,aa,bb,ZZ,YY=sp.symbols('x t a b Z Y')
D=4*aa**3+27*bb**2
quartic=xx**4+2*aa*xx**2+4*bb*xx-aa**2/3
XX=(tt+xx**2+aa)/2
z=XX-aa/3;ycoord=XX*xx+bb/2
forward=sp.rem(sp.expand(ycoord**2-z**3-D/108),tt**2-quartic,tt)
assert sp.simplify(forward)==0
xinv=(YY-bb/2)/(ZZ+aa/3)
tinv=2*(ZZ+aa/3)-xinv**2-aa
back=sp.together(tinv**2-quartic.subs(xx,xinv))
numer=sp.fraction(back)[0]
assert sp.rem(sp.expand(numer),YY**2-ZZ**3-D/108,YY)==0
assert sp.simplify(z.subs({xx:xinv,tt:tinv})-ZZ)==0
assert sp.simplify(ycoord.subs({xx:xinv,tt:tinv})-YY)==0

data={
    'scope':'Exact braid-relation paths, projective-affine marking and quartic identities; no enumeration of GT source elements.',
    'braid_identities':len(braids),
    'positive_foundation_paths':foundation,
    'braid_certificates':braids,
    'local_relation_paths':sum(len(v['local_paths']) for v in braids.values()),
    'local_relation_steps':sum(len(p)-1 for v in braids.values() for p in v['local_paths']),
    'affine_label_checks':affine_checks,
    'normalized_common_exponents':common_exponents,
    'quartic_identities':4,
}
canonical=json.dumps(data,sort_keys=True,separators=(',',':')).encode()
data['sha256']=sha256(canonical).hexdigest()
Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({k:v for k,v in data.items()
                  if k not in ('positive_foundation_paths','braid_certificates')},indent=2))
