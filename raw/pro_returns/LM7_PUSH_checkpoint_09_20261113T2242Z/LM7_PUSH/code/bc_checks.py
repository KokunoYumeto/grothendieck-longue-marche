#!/usr/bin/env python3
"""Exact checks for LM7_PUSH B/C; no arithmetic assertion is inferred from sampling."""
from fractions import Fraction as F
from itertools import product
import json

class K:
    def __init__(self,a=0,b=0): self.a,self.b=F(a),F(b)
    def __add__(self,o):
        o=o if isinstance(o,K) else K(o)
        return K(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return K(-self.a,-self.b)
    def __sub__(self,o): return self+-o if isinstance(o,K) else self+K(-o)
    def __rsub__(self,o): return K(o)+-self
    def __mul__(self,o):
        o=o if isinstance(o,K) else K(o)
        return K(self.a*o.a-self.b*o.b,self.a*o.b+self.b*o.a-self.b*o.b)
    __rmul__=__mul__
    def conj(self): return K(self.a-self.b,-self.b)
    def norm(self): return self.a*self.a-self.a*self.b+self.b*self.b
    def inv(self): return self.conj()*(1/self.norm())
    def __truediv__(self,o): return self*(o if isinstance(o,K) else K(o)).inv()
    def __rtruediv__(self,o): return K(o)*self.inv()
    def __pow__(self,n):
        if n<0:return self.inv()**(-n)
        r=K(1)
        for _ in range(n):r=r*self
        return r
    def __eq__(self,o):
        o=o if isinstance(o,K) else K(o)
        return self.a==o.a and self.b==o.b
    def __repr__(self):return f'({self.a})+({self.b})*zeta'

z=K(0,1); lam=1-z
assert z*z+z+1==0
assert 3==-z*z*lam*lam
cusps=[(K(0),-z,K(1)),(-z,K(0),K(1)),(K(1),-z,K(0))]
fP=lambda x,y,w:(y+w)/(x+y)
fQ=lambda x,y,w:(x+w)/(x+y)
h=lambda x,y,w:(x+y+w)/(x+y)
frameP=[fP(*d)/3 for d in cusps]
frameQ=[fQ(*d)/(-3) for d in cusps]
frameSum=[h(*d)/(-3) for d in cusps]
assert frameP==[lam**-1,lam**-2,z*z*lam**-3]
assert frameQ==[-lam**-2,-lam**-1,z*lam**-3]
assert frameSum==[-lam**-1,-lam**-1,z*lam**-2]
print('Framed 3P coordinates (A,B,C):',frameP)
print('Framed 3Q coordinates (A,B,C):',frameQ)
print('Framed P+Q coordinates (A,B,C):',frameSum)
print('All three exact Q(zeta) identities: PASS')
torP=[K(F(1,9)),K(F(-1,3))]+frameP
torQ=[K(F(1,3)),K(F(-1,9))]+frameQ
torSum=[K(F(1,3)),K(F(1,3))]+frameSum
assert all(a*b==c**3 for a,b,c in zip(torP,torQ,torSum))
print('(3zP)*(3zQ)=(zP+zQ)^3 in all five torus coordinates: PASS')
def retraction(t):
    a,b,A,B,C=t
    return a*A.norm()/C.norm(),b*B.norm()/C.norm()
assert retraction(torP)==(K(1),K(-1))
assert retraction(torQ)==(K(1),K(-1))
assert retraction(torSum)==(K(1),K(1))
print('Retractions of 3zP,3zQ,zP+zQ:',[retraction(t) for t in [torP,torQ,torSum]])
# Vector order: zprime, lambda2, lambda3, tau1, tau2, tau3.
g1=(-3,-2,-3,0,0,2); g2=(0,1,0,0,0,0); g3=(0,0,1,0,0,0)
qvec=tuple(-g1[i]-g2[i]-2*g3[i]+(1 if i==5 else 0)-(1 if i==0 else 0) for i in range(6))
assert qvec==(2,1,1,0,0,-1)
print('Qc origin in eliminated E24 basis:',qvec)
eO=(-1,-1);eP=(1,0);eQ=(0,1)
lead_drafter=tuple(eO[i]+eP[i] for i in range(2))
assert lead_drafter==(0,-1)
lines={tuple(t*x%3 for x in e) for e in [eO,eP,eQ] for t in range(3)}
assert (1,2) not in lines
print('Drafter eO+eP toric vector:',lead_drafter,'(Qc line)')
print('Replacement toric vector (1,2) lies outside all cusp lines modulo 3: PASS')
points=[]
for x,y,w in product(range(2),repeat=3):
    if (x,y,w)!=(0,0,0) and (x**3+y**3+w**3)%2==0:
        points.append((x,y,w))
assert len(points)==3
print('Fermat cubic F2 points:',points)
print('Finite F2 count = 3: PASS')

