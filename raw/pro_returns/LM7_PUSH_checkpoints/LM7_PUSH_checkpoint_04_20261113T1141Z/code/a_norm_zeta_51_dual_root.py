#!/usr/bin/env python3
"""Construct norm-zeta at radicand51 by the dual cyclic algebra.

In E=K(eta), eta^3=zeta, find A17 with norm17, multiply by
A3=-eta^2(1-eta)^2, and put T(v)=A51*sigma(v).  Then T^3=51.
Express multiplication by eta on1 in the K-basis (1,T1,T^2 1).
This gives an exact norm-zeta element in K(cuberoot51).
All arithmetic and the matrix comparison are rational and exact.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json

class K:
    __slots__=('a','b')
    def __init__(self,a=0,b=0):
        if isinstance(a,K): self.a,self.b=a.a,a.b
        elif isinstance(a,(tuple,list)): self.a,self.b=map(Q,a)
        else: self.a,self.b=Q(a),Q(b)
    def __add__(self,o):
        o=K(o); return K(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return K(-self.a,-self.b)
    def __sub__(self,o): return self+-K(o)
    def __rsub__(self,o): return K(o)+-self
    def __mul__(self,o):
        o=K(o)
        return K(self.a*o.a-self.b*o.b,
                 self.a*o.b+self.b*o.a-self.b*o.b)
    __rmul__=__mul__
    def inverse(self):
        den=self.a*self.a-self.a*self.b+self.b*self.b
        assert den
        return K((self.a-self.b)/den,-self.b/den)
    def __truediv__(self,o): return self*K(o).inverse()
    def __pow__(self,n):
        if n<0: return self.inverse()**(-n)
        out=K(1);b=self
        while n:
            if n&1:out=out*b
            b=b*b;n//=2
        return out
    def __eq__(self,o):
        o=K(o);return self.a==o.a and self.b==o.b
    def __bool__(self): return bool(self.a or self.b)
    def encode(self): return [str(self.a),str(self.b)]

zeta=K(0,1);zero=K(0);one=K(1)
def emul(a,b):
    out=[K(0) for _ in range(5)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    for i in (4,3):out[i-3]+=zeta*out[i]
    return out[:3]
def sigma(a): return [x*zeta**i for i,x in enumerate(a)]
def enorm(a):
    out=emul(emul(a,sigma(a)),sigma(sigma(a)))
    assert out[1:]==[zero,zero]
    return out[0]

# Integer-pair search, with no numerical root approximation.
def pmul(a,b):
    u,v=a;c,d=b
    return u*c-v*d,u*d+v*c-v*d
def padd(a,b): return a[0]+b[0],a[1]+b[1]
def pscale(n,a): return n*a[0],n*a[1]
coeff=list(product(range(-2,3),repeat=2))
cubes={a:pmul(pmul(a,a),a) for a in coeff}
witnesses=[]
for a,b,c in product(coeff,repeat=3):
    val=padd(padd(cubes[a],pmul((0,1),cubes[b])),
             padd(pmul((-1,-1),cubes[c]),pscale(-3,pmul((0,1),pmul(pmul(a,b),c)))))
    if val==(17,0):witnesses.append((a,b,c))
assert witnesses
A17=[K(a) for a in witnesses[0]]
assert enorm(A17)==17
A3=[2*zeta,-zeta,-one]
assert enorm(A3)==3
A51=emul(A3,A17)
assert enorm(A51)==51

def T(v):return emul(A51,sigma(v))
unit=[one,zero,zero]
columns=[unit,T(unit),T(T(unit))]
rhs=[zero,one,zero]
matrix=[[columns[j][i] for j in range(3)]+[rhs[i]] for i in range(3)]
for col in range(3):
    row=next(i for i in range(col,3) if matrix[i][col])
    matrix[col],matrix[row]=matrix[row],matrix[col]
    scale=matrix[col][col]
    matrix[col]=[x/scale for x in matrix[col]]
    for row in range(3):
        if row!=col:
            scale=matrix[row][col]
            matrix[row]=[x-scale*y for x,y in zip(matrix[row],matrix[col])]
delta=[matrix[i][3] for i in range(3)]
assert [sum((columns[j][i]*delta[j] for j in range(3)),zero) for i in range(3)]==rhs
for i in range(3):
    v=[K(int(i==j)) for j in range(3)]
    assert T(T(T(v)))==[51*x for x in v]
    S=lambda w:emul([zero,one,zero],w)
    assert T(S(v))==[zeta*x for x in S(T(v))]
a,b,c=delta
norm=a**3+51*b**3+51**2*c**3-153*a*b*c
assert norm==zeta
out={'field':'K=Q(zeta), zeta^2+zeta+1=0; E=K(eta), eta^3=zeta',
     'norm17_search_bound':2,'norm17_exact_witness_count':len(witnesses),
     'norm17_element':[x.encode() for x in A17],
     'norm3_element':[x.encode() for x in A3],
     'norm51_element':[x.encode() for x in A51],
     'cyclic_basis_columns':[[x.encode() for x in col] for col in columns],
     'delta_in_K_beta_beta3_equals51':[x.encode() for x in delta],
     'norm_delta':norm.encode(),
     'T_cubed_equals51':True,'T_S_equals_zeta_S_T':True,
     'status':'PASS_EXACT_NORM_ZETA'}
encoded=json.dumps(out,indent=2)+'\n'
print(encoded,end='')
Path(__file__).with_suffix('.json').write_text(encoded)
