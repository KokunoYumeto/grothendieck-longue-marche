#!/usr/bin/env python3
"""Exact flex/unit certificates used in A.59--A.60 for conductor 243.

The global obstruction in A.60 is a proof using Faltings, not extrapolation
from this finite calculation.  All polynomial checks here are exact.
"""
import sympy as s

x,y,z,a,w=s.symbols('x y z a w')
F=y*y*z+y*z*z-x**3+z**3
f=F.subs(z,1)
H=s.det(s.hessian(F,(x,y,z)))
assert s.expand(H-24*x*(y*y+y*z-2*z*z))==0
assert s.rem(H.subs(z,1)-24*x*(x**3-3),f,y)==0
assert s.expand(f.subs({x:1,y:0}))==0
print('Minimal curve: y^2+y=x^3-1; discriminant=-243; P=(1,0).')
print('Hessian determinant:',s.factor(H))
print('On the affine curve: Hessian=24*x*(x^3-3).')
psi3=3*x**4-9*x
assert s.factor(psi3)==3*x*(x**3-3)
print('Three-division polynomial:',s.factor(psi3))
print('Flex residue fields: Q at O; Q(zeta_3) at x=0;')
print('  Q(cuberoot(3)) at y=1 and y=-2 (two separate degree-three orbits).')

def reduce_a(poly):
    return s.rem(s.expand(poly),a**3-3,a)

assert s.rem(s.expand(f.subs(y,w)-x**3*(-1)),w*w+w+1,w)==0
for yp in (a*a*x-2,1-a*a*x):
    assert reduce_a(f.subs(y,yp)+(x-a)**3)==0
print('All finite flex tangents meet the cubic with multiplicity exactly three.')
units=[w-y,a*a*x-y-2,1-a*a*x-y]
values=[s.expand(u.subs({x:1,y:0})) for u in units]
norms=[s.resultant(w*w+w+1,values[0],w),
       s.resultant(a**3-3,values[1],a),
       s.resultant(a**3-3,values[2],a)]
assert values==[w,a*a-2,1-a*a]
assert norms==[1,1,-8]
print('Normalized units (leading coefficient +1 at O, parameter -x/y):')
for u,v,norm in zip(units,values,norms):
    assert s.limit(z**3*u.subs({x:z**-2,y:-z**-3}),z,0)==1
    print(' ',str(u),'; value at P =',v,'; field norm =',norm)
print('Each normalized unit has divisor 3(d-O).')
print('Hence its square-root cover is geometrically connected, branched at d,O, genus2.')

# Exact cyclic-group check of the primary-component argument.  A point in
# any finite abelian group generates a cyclic group, so these test that model.
sets=[(2,),(3,),(5,),(2,3),(2,5),(3,5),(2,3,5)]
tested=0
for primes in sets:
    M=s.prod(primes)
    for order in range(1,301):
        primary=1
        complement=order
        for p in primes:
            while complement % p==0:
                complement//=p
                primary*=p
        # Q is zero on all removed primary components and one on the others.
        if complement==1:
            Q=0
        else:
            Q=(primary*pow(int(primary),-1,complement)) % order
        T=(1-Q) % order
        assert (complement*Q) % order==0
        assert (primary*T) % order==0
        for k in range(8):
            mk=pow(int(M),k,order) if order>1 else 0
            if 3*mk % order:
                continue
            assert (3*Q) % order==0
            assert (3*mk*T) % order==0
            if 3 not in primes:
                assert mk*T % order==0
            else:
                assert Q % order==0
            tested+=1
print(f'Primary-component reductions verified in {tested} cyclic test cases.')
print('All exact rank-one unit checks passed.')
