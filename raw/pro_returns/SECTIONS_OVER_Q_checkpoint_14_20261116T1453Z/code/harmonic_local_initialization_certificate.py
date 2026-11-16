#!/usr/bin/env python3
"""Exact finite checks for A.112. The unrestricted local proof is in the text."""
from fractions import Fraction as Q
from itertools import product
from math import isqrt

def vu(a,p):
    a=Q(a); n,d=a.numerator,a.denominator
    if n==0:return None
    v=0
    while n%p==0:n//=p;v+=1
    while d%p==0:d//=p;v-=1
    return v,(n*pow(d,-1,p))%p

def sq(a,p):
    if not a:return True
    v,u=vu(a,p)
    return v%2==0 and pow(u,(p-1)//2,p)==1

translations=0
for p in (3,7,11,19):
    for unit in range(1,p):
        d=Q(p*unit)
        for e in range(-4,7):
            for u in range(1,3*p):
                if u%p==0:continue
                x=Q(p)**e*u
                y2=x*(x*x-d*d)
                if y2==0 or not sq(y2,p):continue
                if e<=0:
                    if e<0:assert e%2==0
                    translations+=1;continue
                if e>=2:
                    x1=-d*d/x
                else:
                    signs=[s for s in (1,-1) if vu(x-s*d,p)[0]>=2]
                    assert len(signs)==1
                    s=signs[0]
                    x1=s*d+2*d*d/(x-s*d)
                assert vu(x1,p)[0]<=0
                translations+=1

# Finite-field norm maps for good reduction, using F_p(i), p=3 mod4.
norm_cases=norm_points=0
for p in (3,7,11,19):
    zero=(0,0);one=(1,0)
    def add(a,b):return ((a[0]+b[0])%p,(a[1]+b[1])%p)
    def neg(a):return ((-a[0])%p,(-a[1])%p)
    def sub(a,b):return add(a,neg(b))
    def mul(a,b):return ((a[0]*b[0]-a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
    def inv(a):
        q=pow((a[0]*a[0]+a[1]*a[1])%p,-1,p)
        return (a[0]*q%p,-a[1]*q%p)
    def div(a,b):return mul(a,inv(b))
    def scale(n,a):return (n*a[0]%p,n*a[1]%p)
    def conj(a):return (a[0],-a[1]%p)
    field=list(product(range(p),repeat=2))
    roots={}
    for y in field:roots.setdefault(mul(y,y),[]).append(y)
    for d in range(1,min(p,5)):
        a4=(-d*d%p,0)
        def ec_add(P,Q0):
            if P is None:return Q0
            if Q0 is None:return P
            x,y=P;xx,yy=Q0
            if x==xx and add(y,yy)==zero:return None
            if P==Q0:
                slope=div(add(scale(3,mul(x,x)),a4),scale(2,y))
            else:slope=div(sub(yy,y),sub(xx,x))
            xxx=sub(sub(mul(slope,slope),x),xx)
            yyy=sub(mul(slope,sub(x,xxx)),y)
            return (xxx,yyy)
        pts=[None]
        for x in field:
            rhs=add(mul(mul(x,x),x),mul(a4,x))
            pts.extend((x,y) for y in roots.get(rhs,[]))
        rational={P for P in pts if P is None or (P[0][1]==P[1][1]==0)}
        image=set()
        for P in pts:
            Pc=None if P is None else (conj(P[0]),conj(P[1]))
            image.add(ec_add(P,Pc))
        assert image==rational
        norm_cases+=1;norm_points+=len(pts)

# The explicit nonzero source class killed by the actual Jacobian pullback.
d=138;PR=(150,720);source=(162,1080)
for x,y in (PR,source):assert y*y==x**3-d*d*x
R=(1+Q(PR[0],d))/2
c=(1-Q(source[0],d))/2
rho=Q(source[1],PR[1])
assert (R,c,rho)==(Q(24,23),Q(-2,23),Q(3,2))
squares27={x*x%27 for x in range(27)}
quartic=lambda m:-m**4+972*m*m+8640*m+2556
assert all(quartic(m)%27==(18-m**4)%27 for m in range(27))
assert all(quartic(m)%27 not in squares27 for m in range(27))
assert pow(2,(3-1)//2,3)==2
# Negative-valuation dominance: the three correction depths relative to m^4.
for v in range(-20,0):
    assert min(5-2*v,3-3*v,2-4*v)>0  # v3 of972,8640,2556.
assert all(972%(3**k)==0 for k in range(1,6))
assert 972%3**6!=0 and 8640%3**3==0 and 8640%3**4!=0
assert 2556%9==0 and 2556%27!=0

print("Exact odd-place translation cases:",translations)
print("Finite-field norm surjectivity cases:",norm_cases)
print("Actual finite-field points whose norms were computed:",norm_points)
print("Explicit d138 source: all27 residue classes obstructed modulo27.")
print("Checked negative-valuation dominance and the exact R,c,rho values.")
print("All exact checks passed; unbounded local assertions are proved in A.112.")

