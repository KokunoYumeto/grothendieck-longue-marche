#!/usr/bin/env python3
"""Exact characteristic-two identities for the rational Livsic obstruction."""
from pathlib import Path
import json

# Polynomials in F2[x,y], represented by their nonzero monomials.
def add(*ps):
    out=set()
    for p in ps:out.symmetric_difference_update(p)
    return out

def mul(a,b):
    out=set()
    for i,j in a:
        for k,l in b:
            v=(i+k,j+l)
            if v in out:out.remove(v)
            else:out.add(v)
    return out

def power(a,n):
    out={(0,0)}
    while n:
        if n&1:out=mul(out,a)
        a=mul(a,a);n//=2
    return out

def reduce_curve(a):
    # y²=xy+x³+1 on E.
    out=set(a)
    while any(j>=2 for i,j in out):
        i,j=next((i,j) for i,j in out if j>=2)
        out.remove((i,j))
        out.symmetric_difference_update({(i+1,j-1),(i+3,j-2),(i,j-2)})
    return out

one={(0,0)};x={(1,0)};y={(0,1)}
x2=power(x,2);x4=power(x,4)
nx=add(x2,one)
ny=add(mul(y,nx),x2,x,one)
# Vx=nx/x, Vy=ny/x². Clear x^4 from its curve equation.
curve_num=add(power(ny,2),mul(mul(x,nx),ny),mul(x,power(nx,3)),x4)
assert reduce_curve(curve_num)==set()
# b=(x+1)/x and b²=Vx/x.
assert power(add(x,one),2)==nx
# pi(V)=doubling. The y-doubling numerator over x^4 is
# (x²+y+x)*x*(x^4+1)+x^6.
double_y_num=add(mul(mul(add(x2,y,x),x),add(x4,one)),power(x,6))
assert reduce_curve(add(power(ny,2),double_y_num))==set()
points=[(a,b) for a in range(2) for b in range(2)
        if (b*b+a*b+a*a*a+1)%2==0]
assert points==[(0,1),(1,0),(1,1)]
for a,b in points[1:]:
    lam=(a+b)%2
    xx=(lam*lam+lam)%2
    yy=((lam+1)*xx+a*a)%2
    assert (xx,yy)==(0,1)
out={
 "status":"all exact polynomial and rational-point assertions passed",
 "curve":"y^2+x*y=x^3+1 over F2",
 "rational_affine_points":points,
 "verschiebung_x":"(x^2+1)/x",
 "verschiebung_y":"(y*(x^2+1)+x^2+x+1)/x^2",
 "curve_equation_remainder":[],
 "frobenius_times_verschiebung_equals_doubling":True,
 "cocycle":"(x+1)/x",
 "cocycle_square_equals_x_return_ratio":True,
 "scope":"The all-periodic holonomy and non-coboundary conclusions are proved using these identities and divisor/degree arguments in dynamical_livsic_research.md."
}
Path(__file__).with_name('verschiebung_livsic_check_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
