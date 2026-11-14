#!/usr/bin/env python3
"""Exact universal and finite checks for the ordinary theta-five surface.

The universal identities are in GF(2)(x,t,r), using SymPy's exact fraction
field. The finite illustration is independently evaluated in F16.
The divisor and section arguments are in the accompanying mathematical proof.
"""
from pathlib import Path
import json
from sympy.polys.fields import field
from sympy.polys.domains import GF
K,x,t,r=field('x,t,r',GF(2))
u=x*(x+1)
kappa=(r*(r+1))**3/((r+t)**3*(r*r+t)**2)
d=r*(r+1)/(r*r+t)
a=kappa
b=kappa*t**5/r**2
c=kappa*(t+1)**5/(r+1)**2
phi=a*x+b/x+c/(x+1)
delta=a*t+b/t+c/(t+1)
A=d*(x+t)
B=x+r
q=(x+t)**5/u
rho=(r+t)*d
v=rho/(x+r)+rho/(t+r)
assert A==B*v
assert q.diff(x)==(x+t)**4*(x*x+t)/u**2
assert kappa*q/B**2+v*v+v==phi+delta
assert u*(A*A+A*B)+B*B*(u*phi+delta*u)==kappa*(x+t)**5
assert kappa==((r*(r+1))**3/((r+t)**3*(r*r+t)**2))

def mul(a,b):
    c=0
    while b:
        if b&1:c^=a
        b>>=1
        a<<=1
        if a&16:a^=19
    return c

def pw(a,n):
    c=1
    while n:
        if n&1:c=mul(c,a)
        a=mul(a,a);n>>=1
    return c

def div(a,b):
    assert b
    return mul(a,pw(b,14))

parameter_count=outside=0
example=None
for tv in range(2,16):
    for rv in range(2,16):
        if rv==tv or mul(rv,rv)==tv:continue
        ur=mul(rv,rv^1)
        kap=div(pw(ur,3),mul(pw(rv^tv,3),pw(mul(rv,rv)^tv,2)))
        av=kap
        bv=div(mul(kap,pw(tv,5)),mul(rv,rv))
        cv=div(mul(kap,pw(tv^1,5)),mul(rv^1,rv^1))
        assert av and bv and cv
        dv=div(ur,mul(rv,rv)^tv)
        deltav=mul(av,tv)^div(bv,tv)^div(cv,tv^1)
        obstruction=pw(av^bv^cv,3)^mul(mul(av,bv),cv)
        parameter_count+=1
        outside+=bool(obstruction)
        if (tv,rv)==(2,4):
            beta=10
            assert mul(beta,beta)^beta==deltav
            assert [av,bv,cv,dv,deltav,obstruction]==[1,2,3,7,2,6]
            # Check the norm at every available affine x as an additional finite check.
            for xv in range(2,16):
                uv=mul(xv,xv^1)
                phiv=mul(av,xv)^div(bv,xv)^div(cv,xv^1)
                Ax=mul(dv,xv^tv);Bx=xv^rv
                lhs=mul(uv,mul(Ax,Ax)^mul(Ax,Bx))^mul(mul(Bx,Bx),mul(uv,phiv^deltav))
                assert lhs==mul(kap,pw(xv^tv,5))
            example={'t':tv,'r':rv,'a_b_c':[av,bv,cv],'d':dv,'delta':deltav,
                     'beta':beta,'cubic_obstruction':obstruction,
                     'A_coefficients_low_first':[mul(dv,tv),dv],
                     'B_coefficients_low_first':[rv,1]}
assert parameter_count==168 and outside==156 and example
orbit=[];j=1
while j not in orbit:
    orbit.append(j);j=2*j%5
assert orbit==[1,2,4,3]
result={'status':'PASS','universal_fraction_field':'GF(2)(x,t,r)',
        'universal_identity_checks':['A=B*v','q derivative','principal-part cancellation plus constant','norm polynomial'],
        'F16_modulus':'omega^4+omega+1','finite_parameter_pairs':parameter_count,
        'pairs_outside_cubic_locus':outside,'example':example,
        'nonzero_doubling_orbit_mod5':orbit,'cover_genus':6,'cover_two_rank_from_proved_character_argument':2,
        'scope':'Universal algebra and finite illustration verified. Geometry, exact order, converse, moduli dimension and point-section consequence are proved in the candidate.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
