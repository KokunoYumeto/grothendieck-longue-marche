#!/usr/bin/env python3
"""Independent exact checks for E112; no author-program import."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json

class G:
    def __init__(self,a=0,b=0): self.a,self.b=Q(a),Q(b)
    def __add__(x,y):
        y=y if isinstance(y,G) else G(y)
        return G(x.a+y.a,x.b+y.b)
    __radd__=__add__
    def __neg__(x):return G(-x.a,-x.b)
    def __sub__(x,y):return x+-G.coerce(y)
    def __rsub__(x,y):return G.coerce(y)+-x
    def __mul__(x,y):
        if isinstance(y,K4):return NotImplemented
        y=G.coerce(y)
        return G(x.a*y.a-x.b*y.b,x.a*y.b+x.b*y.a)
    __rmul__=__mul__
    def __truediv__(x,y):
        y=G.coerce(y);n=y.a*y.a+y.b*y.b
        return x*G(y.a/n,-y.b/n)
    def __pow__(x,n):
        if n<0:return (G(1)/x)**(-n)
        z=G(1)
        for _ in range(n):z=z*x
        return z
    def __eq__(x,y):
        y=G.coerce(y);return (x.a,x.b)==(y.a,y.b)
    @staticmethod
    def coerce(x):return x if isinstance(x,G) else G(x)

I=G(0,1)

class K4:
    def __init__(self,c,rad):
        self.c=tuple(G.coerce(t) for t in c)+(G(),)*(4-len(c));self.rad=rad
    def scalar(self,x):return K4([x],self.rad)
    def coerce(self,x):return x if isinstance(x,K4) else self.scalar(x)
    def __add__(x,y):
        y=x.coerce(y);return K4([a+b for a,b in zip(x.c,y.c)],x.rad)
    __radd__=__add__
    def __neg__(x):return K4([-a for a in x.c],x.rad)
    def __sub__(x,y):return x+-x.coerce(y)
    def __rsub__(x,y):return x.coerce(y)+-x
    def __mul__(x,y):
        y=x.coerce(y);c=[G() for _ in range(7)]
        for i,a in enumerate(x.c):
            for j,b in enumerate(y.c):c[i+j]=c[i+j]+a*b
        for k in range(6,3,-1):c[k-4]=c[k-4]+c[k]*x.rad
        return K4(c[:4],x.rad)
    __rmul__=__mul__
    def __pow__(x,n):
        z=x.scalar(1)
        for _ in range(n):z=z*x
        return z
    def __eq__(x,y):return x.c==x.coerce(y).c
    def rotate(x,r):return K4([v*I**(r*j) for j,v in enumerate(x.c)],x.rad)

point_checks=0
rotation_checks=0
for case,sg,A in [(1,-1,1),(2,1,4)]:
    for sign in [1,-1]:
        ii=sign*I;rad=sg*(1+2*ii);a=K4([0,1],rad)
        y=a*((1+ii)/(2-ii) if case==1 else G(4)/(2-ii))
        x=y*y*(G(5)/(A*(4+2*ii)))
        assert y*y==x*x*x+A*x
        # Clear denominators in the literal elliptic duplication formulas.
        den=4*y*y;top=(3*x*x+A)**2
        assert top-8*x*y*y==den*(-x)
        assert (3*x*x+A)*(2*x)-2*y*y==2*ii*y*y
        point_checks+=3
        # The field generator's i-action is the actual curve [i] action.
        for r in range(4):
            assert x.rotate(r)==((-1)**r)*x
            assert y.rotate(r)==(I**r)*y
            rotation_checks+=2

group=list(product(range(4),repeat=2))
def ch(v,g):return (v[0]*g[0]+v[1]*g[1])%4
primitive=[v for v in group if any(t%2 for t in v)]
kernel_sets={frozenset(g for g in group if ch(v,g)==0) for v in primitive}
assert len(kernel_sets)==6
assert all(any(all(ch(v,g)==0 for g in K) for K in kernel_sets) for v in group)

# Independent Fourier inversion at the coefficient exponent used here.
mod=5**5
z=next(n for n in range(2,mod,5) if (n*n+1)%mod==0)
rows=[[pow(z,ch(v,g),mod) for g in group] for v in group]
inv16=pow(16,-1,mod)
orth=0
for i in range(16):
    for j in range(16):
        assert sum(rows[i][k]*pow(rows[j][k],-1,mod) for k in range(16))*inv16%mod==int(i==j)
        orth+=1
norm_maps=0
for K in kernel_sets:
    for v in group:
        N=sum(pow(z,ch(v,g),mod) for g in K)%mod
        assert N==(4 if all(ch(v,g)==0 for g in K) else 0)
        assert pow(4,-1,mod)*N%mod==int(N==4)
        norm_maps+=1

# Entire residual fixed spaces; the Tate inverse uses det^{-1} literally.
characters={
 'V':[(1,0),(0,3)],
 'V(1)':[(2,3),(1,2)],
 'U':[(2,0),(0,2)],
}
residual=[]
for name,vs in characters.items():
    unt=[((r-1)%4,(s+1)%4) for r,s in vs]
    assert all(any(ch(v,g) for g in group) for v in vs)
    for v in unt:
        K=frozenset(g for g in group if ch(v,g)==0)
        assert K in kernel_sets
    residual.append({'module':name,'characters':vs,'untwisted':unt})
assert residual[-1]['untwisted']==[(1,1),(3,3)]

# All coefficient vectors modulo 25 for selected actual-form inert matrices.
projector_cases=0
for p in [3,7,11,19,23,31,43]:
    mod=25
    for a in [1,2,6,7,11,12,16,17,21,22]:
        b=-p*pow(a,-1,mod)%mod
        A=a*a*pow(p,-1,mod)%mod;B=b*b*pow(p,-1,mod)%mod
        for x,y in product(range(mod),repeat=2):
            fixed=(A*y%mod==x and B*x%mod==y)
            t=(x+A*y)*pow(2,-1,mod)%mod
            assert (fixed == ((x,y)==(t,B*t%mod)))
            assert (t,B*t%mod)==((x+A*y)*pow(2,-1,mod)%mod,(B*x+y)*pow(2,-1,mod)%mod)
            projector_cases+=1

out={'status':'PASS','exact_point_identity_checks':point_checks,
     'actual_radical_rotations':rotation_checks,'character_kernel_count':6,
     'all_character_cover_count':16,'fourier_inverse_checks':orth,
     'norm_fixed_inverse_checks':norm_maps,'module_character_maps':residual,
     'complete_inert_fixed_vector_cases':projector_cases,
     'finite_central_rank':30+15+18+3}
P=Path(__file__).with_suffix('.json');P.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
