#!/usr/bin/env python3
"""Exact theta-torsion elimination for Y^2+X^2 Y=X^5+X over F2.

For odd n=2m+5, a function of pole order at most n at infinity is
A(X)+B(X)Y, deg A<=m+2, deg B<=m.  Its order at a finite unramified
point (r,s) is >=n exactly when the (m+2)x(m+1) Hasse-Taylor matrix
(c[i-j]) has deficient rank, rows i=m+3,...,n-1 and columns j=0,...,m.
We compute every maximal minor in F2(r)[s]/(s^2+r^2*s+r^5+r), then
the gcd of their quadratic norms.  Gcd 1 rigorously excludes n-torsion
on the theta curve.  At r=0 the point class has order two and is
separately excluded.  A nonconstant gcd is only a candidate locus.
"""
from pathlib import Path
from itertools import combinations
import json, sys, time
from sympy.polys.fields import field
from sympy.polys.domains import GF

R, r = field('r', GF(2))
zero, one = R.zero, R.one
h, f = r**2, r**5+r

class Q:
    __slots__=('a','b')
    def __init__(self,a=0,b=0): self.a,self.b=R(a),R(b)
    def __bool__(self): return bool(self.a or self.b)
    def __add__(self,v): return Q(self.a+v.a,self.b+v.b)
    __sub__=__add__
    def __mul__(self,v):
        return Q(self.a*v.a+self.b*v.b*f,
                 self.a*v.b+self.b*v.a+self.b*v.b*h)
    def norm(self): return self.a*self.a+self.a*self.b*h+self.b*self.b*f
    def inv(self):
        z=self.norm(); assert z
        return Q((self.a+self.b*h)/z,self.b/z)
    def __truediv__(self,v): return self*v.inv()
    def square(self): return self*self

def det(M):
    M=[list(row) for row in M]; n=len(M);result=Q(1)
    for j in range(n):
        pivot=next((i for i in range(j,n) if M[i][j]),None)
        if pivot is None:return Q()
        M[j],M[pivot]=M[pivot],M[j]
        z=M[j][j];result=result*z
        inv=z.inv()
        for i in range(j+1,n):
            if not M[i][j]:continue
            scale=M[i][j]*inv
            for k in range(j+1,n): M[i][k]=M[i][k]+scale*M[j][k]
            M[i][j]=Q()
    return result

def monomial(poly):return len(poly.terms())==1
def exponents(poly):return sorted(m[0] for m,c in poly.terms() if c)
def norm_numerator(x):
    # Original Taylor coefficients, hence minors and norms, have poles only at r=0.
    assert monomial(x.a.denom) and monomial(x.b.denom)
    a=x.norm();assert monomial(a.denom)
    pol=a.numer
    while pol and not pol[(0,)]:pol=pol.exquo(R.ring.gens[0])
    return pol.monic() if pol else pol

def run(n):
    start=time.monotonic();m=(n-5)//2
    c=[Q(0,1)]
    for i in range(1,n):
        rhs=Q({1:r**4+1,4:r,5:one}.get(i,zero))
        if i%2==0:rhs=rhs+c[i//2].square()
        if i>=2:rhs=rhs+c[i-2]
        c.append(rhs/Q(h))
    M=[[c[i-j] for j in range(m+1)] for i in range(m+3,n)]
    assert len(M)==m+2
    gcd=None; norms=[]
    for omit in range(m+2):
        z=det([row for i,row in enumerate(M) if i!=omit])
        pol=norm_numerator(z);norms.append(exponents(pol))
        gcd=pol if gcd is None else gcd.gcd(pol)
        print('n',n,'minor',omit,'degree',pol.degree(),'gcd degree',gcd.degree(),flush=True)
    record={'n':n,'minor_norm_numerators':norms,'gcd_exponents':exponents(gcd),
            'excluded':gcd==R.ring.one,'seconds':time.monotonic()-start}
    print(json.dumps(record),flush=True)
    return record

if __name__=='__main__':
    ns=list(map(int,sys.argv[1:])) or [5,7,9,11,13]
    records=[run(n) for n in ns]
    Path(__file__).with_suffix('.json').write_text(json.dumps(records,indent=2)+'\n')
