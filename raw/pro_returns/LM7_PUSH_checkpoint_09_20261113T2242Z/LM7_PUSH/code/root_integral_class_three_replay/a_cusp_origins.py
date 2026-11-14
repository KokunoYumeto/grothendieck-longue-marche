#!/usr/bin/env python3
"""Exact tangent-line regularization at all nine Fermat cubic cusps.
K=Q(zeta), zeta^2+zeta+1=0. Output h[d,e] is the e-frame of
3 O(d-O), divided by the O-frame. Negative signs have zero pro-3
Kummer class but are retained in the exact algebraic calculation.
"""
from fractions import Fraction as F
import json
class K:
    def __init__(self,a=0,b=0): self.a,self.b=F(a),F(b)
    def __add__(self,o):
        if not isinstance(o,K): o=K(o)
        return K(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return K(-self.a,-self.b)
    def __sub__(self,o): return self+-o if isinstance(o,K) else self+K(-o)
    def __mul__(self,o):
        if not isinstance(o,K): o=K(o)
        return K(self.a*o.a-self.b*o.b,self.a*o.b+self.b*o.a-self.b*o.b)
    __rmul__=__mul__
    def conj(self): return K(self.a-self.b,-self.b)
    def norm(self): return self.a*self.a-self.a*self.b+self.b*self.b
    def __truediv__(self,o):
        if not isinstance(o,K): o=K(o)
        p=self*o.conj(); n=o.norm()
        return K(p.a/n,p.b/n)
    def __pow__(self,n):
        if n<0:return (K(1)/self)**(-n)
        z=K(1); x=self
        while n:
            if n&1:z=z*x
            x=x*x;n//=2
        return z
    def __eq__(self,o):
        if not isinstance(o,K):o=K(o)
        return self.a==o.a and self.b==o.b
    def pair(self):return [str(self.a),str(self.b)]

z=K(0,1); la=K(1)-z
assert la**2==-3*z
names=['O','P','Q','A','Abar','B','Bbar','C','Cbar']
pts=[(K(1),K(-1),K()),(K(),K(-1),K(1)),(K(-1),K(),K(1)),
     (K(),-z,K(1)),(K(),-(z**2),K(1)),(-z,K(),K(1)),(-(z**2),K(),K(1)),
     (K(1),-z,K()),(K(1),-(z**2),K())]
conjperm=[0,1,2,4,3,6,5,8,7]
assert all(sum(c**3 for c in p)==0 for p in pts)

def tang(d,p):return sum(c*c*v for c,v in zip(pts[d],p))

def regularized(d,e):
    if d==0:return K(1)
    x,y,t=pts[d]
    cO=-3*tang(d,pts[0])
    if e==0:return cO
    if e==d:
        if x==0: eta=-y; return K(1)/(3*eta)
        if y==0: eta=-x; return K(1)/(3*eta)
        eta=-y; return K(-1)/(3*(K(1)-eta))
    return tang(d,pts[e])/tang(0,pts[e])

H=[]
for d in range(9):
    den=regularized(d,0)
    H.append([regularized(d,e)/den for e in range(9)])
assert all(H[d][0]==1 for d in range(9))
assert H[1][1]==K(1)/9 and H[1][2]==K(-1)/3
assert H[1][3]==la**-1 and H[1][5]==la**-2
assert H[1][7]==z**2*la**-3
for d in range(9):
 for e in range(9):assert H[d][e].conj()==H[conjperm[d]][conjperm[e]]

def fact(x):
 n=x.norm(); b=0
 while n.numerator%3==0:n/=3;b+=1
 while n.denominator%3==0:n*=3;b-=1
 assert n==1
 unit=x/(la**b)
 for sign in (1,-1):
  for a in range(3):
   if unit==sign*(z**a):return {'sign':sign,'zeta':a,'lambda':b}
 raise AssertionError(unit.pair())
Fmat=[[fact(H[d][e]) for e in range(1,9)] for d in range(1,9)]
out={'cusp_order':names[1:], 'regularized_frame_values_Qzeta':[[x.pair() for x in row[1:]] for row in H[1:]],
 'factorizations':Fmat,'lambda_exponents':[[v['lambda'] for v in row] for row in Fmat],
 'zeta_exponents':[[v['zeta'] for v in row] for row in Fmat],
 'signs':[[v['sign'] for v in row] for row in Fmat],
 'all_entries_are_3_units':True,'conjugation_equivariance':True,'P_row_matches_E24_6':True}
print(json.dumps(out,indent=2))
