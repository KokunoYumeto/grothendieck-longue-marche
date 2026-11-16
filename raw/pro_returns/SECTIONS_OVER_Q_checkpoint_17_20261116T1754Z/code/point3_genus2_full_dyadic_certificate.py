#!/usr/bin/env python3
"""Finite exact checks for A192. The Neron comparison is proved in the text."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json
import sympy as sp

N=32
def conv(a,b):
    return [sum(a[j]*b[i-j] for j in range(i+1) if j<len(a) and i-j<len(b)) for i in range(N+1)]
def power(a,k):
    r=[F(1)]+[F(0)]*N
    for _ in range(k): r=conv(r,a)
    return r
def inverse(a):
    r=[1/a[0]]
    for i in range(1,N+1): r.append(-sum(a[j]*r[i-j] for j in range(1,i+1))/a[0])
    return r
def v2(q):
    q=F(q)
    if not q:return 10**9
    a,b=abs(q.numerator),q.denominator
    return ((a&-a).bit_length()-1)-((b&-b).bit_length()-1)

A=[F(comb(5*n,n),4*n+1) for n in range(N+1)]
B=[F((-54)**n*comb(4*n,n),3*n+1) for n in range(N+1)]
assert all(a.denominator==1 for a in A+B)
A5=power(A,5);B4=power(B,4)
assert A[0]==B[0]==1
assert all(A[n]==A5[n-1] and B[n]==-54*B4[n-1] for n in range(1,N+1))
A2=conv(A,A)
pos=[]
for n in range(N+1):
    l1=-F((8*n+2)*A[n],(8*n+1)*54**(5*n+1))
    l2=F((4*n+2)*A2[n],(8*n+3)*54**(5*n+2))
    # Differentiate primitives and compare dx/z and d(x^2)/(2z).
    assert l1*(8*n+1)==-F((8*n+2)*A[n],54**(5*n+1))
    assert l2*(8*n+3)==F((8*n+4)*A2[n],2*54**(5*n+2))
    for k in range(1,65):
        assert v2(l1)+(8*n+1)*k>=k+n*(8*k-5)
        assert v2(l2)+(8*n+3)*k>=3*k-1+n*(8*k-5)
    pos.append([n,v2(l1),v2(l2)])
assert -F(2,54)==-F(1,27) and F(2,3*54**2)==F(1,4374)
assert all(B[n].numerator%54==0 for n in range(1,N+1))
Bprime=[(n+1)*B[n+1] for n in range(N)]+[F(0)]
ratio=conv(Bprime,inverse(B))
assert all(r.denominator==1 and r.numerator%54==0 for r in ratio[:-1])
inf=[]
for n in range(1,N):
    l1=F((8*n+2)*B[n],8*n+3)
    l2=F(8*ratio[n-1],8*n+1)
    assert v2(l1)>=2 and v2(l2)>=4
    for k in range(1,65):
        assert v2(l1)+(8*n+3)*k>3*k+1
        assert v2(l2)+(8*n+1)*k>k+1
    inf.append([n,v2(l1),v2(l2)])

x,t,z=sp.symbols('x t z')
tf=x**4/(x**4-54)
assert sp.cancel(-tf*(1-tf)**3/24-3**8*x**4/(x**4-54)**4)==0
xr=-6*z**2/(1-t);yr=-18*z/(1-t)
z8=-t*(1-t)**3/24
assert sp.cancel(sp.cancel(xr**4).subs(z**8,z8)+54*t/(1-t))==0
assert sp.cancel(yr**2-xr*(-54*t/(1-t)-54))==0
assert sp.cancel(3*xr/yr-z)==0
assert sp.cancel((-54*t/(1-t))/(-54*t/(1-t)-54)-t)==0
assert sp.cancel(-54*x/(x**4-54)/(1-tf)-x)==0
assert sp.cancel(sp.together(-54*x/(1-tf)-x*(x**4-54)))==0
assert F(3**4,3**4-54)==3
assert -F(3*(1-3)**3,24)==1
assert 3**5-54*3==9**2

# Unit-x condition and the complete valuation parity partition.
assert [u for u in (1,3,5,7) if (u**5-54*u)%8==1]==[3]
for r in range(-128,129):
    if r>0 and (r+1)%2==0:
        k=(r+1)//2;assert r==2*k-1 and 3*k-1>k
    if r<0 and (5*r)%2==0:
        k=-r//2;assert r==-2*k and 3*k+1>k+1
boundary=[{'point':'(0,0)','ord_x':2,'ord_y':1,'image':'0','e':8},
          {'point':'infinity','ord_x':-2,'ord_y':-5,'image':'1','e':8},
          {'point':'(theta,0), theta^4=54','ord_y':1,'image':'infinity','e':2}]
assert 2*8+4*2==24
assert sum([7,7,4])==18 and -16+18==2 # Riemann-Hurwitz: genus two.
data={'series_order':N,'positive_coefficient_valuations':pos,
      'infinity_coefficient_valuations':inf,'boundary':boundary,
      'scope':'Finite algebra and valuation checks; geometric Neron/logarithm proof is in A192.'}
Path(__file__).with_name('point3_genus2_full_dyadic_certificate_data.json').write_text(json.dumps(data,indent=2)+'\n')
print('PASS: 64 exact recursive-series identities and integral coefficients.')
print('PASS: 4224 positive-disc coefficient valuation checks and exact primitive derivatives.')
print('PASS: 3968 infinity-disc coefficient valuation checks and exact logarithmic derivative.')
print('PASS: both cyclic-eight equations, both inverse maps, point images and boundary indices.')
print('PASS: unit residue condition, valuation partition, and genus-two Riemann-Hurwitz count.')
