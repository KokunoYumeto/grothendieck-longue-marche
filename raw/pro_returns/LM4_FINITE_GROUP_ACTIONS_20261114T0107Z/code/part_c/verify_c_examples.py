#!/usr/bin/env python3
"""Finite checks accompanying LM4 Part C.  The analytic arguments are in the paper.
No finite calculation is claimed to classify all finite surface actions.
"""
import cmath
import json
import math
from fractions import Fraction
from pathlib import Path


def mm(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
I=((1,0),(0,1))
S=((0,-1),(1,0))
R=((0,-1),(1,1))

def mp(a,n):
    b=I
    for _ in range(n):
        b=mm(b,a)
    return b

def order(a):
    for n in range(1,25):
        if mp(a,n)==I:
            return n
    return None

def fixed_mod_lattice(a,v):
    return all((sum(a[i][j]*v[j] for j in range(2))-v[i]).denominator==1 for i in range(2))

rows={}
rows['modular_matrices']={'S':S,'R':R,'order_S':order(S),'order_R':order(R),'S_squared_equals_R_cubed':mp(S,2)==mp(R,3),'central_common_value':mp(S,2)}
assert order(S)==4 and order(R)==6 and mp(S,2)==mp(R,3)==((-1,0),(0,-1))
cohom=[(a,b) for a in range(4) for b in range(6) if (a-b)%2==0]
gen=[(n%4,n%6) for n in range(12)]
assert len(cohom)==12 and set(cohom)==set(gen)
rows['amalgam_H2']={'kernel_elements':cohom,'generator_order':len(set(gen)),'generator':[1,1]}
rows['two_marked_tori']={'square_order4_fixes_half_diagonal':fixed_mod_lattice(S,(Fraction(1,2),Fraction(1,2))),'hexagonal_order3_fixes_third_diagonal':fixed_mod_lattice(mp(R,2),(Fraction(1,3),Fraction(1,3)))}
assert all(rows['two_marked_tori'].values())

# A peripheral twist whose support shrinks to the puncture at zero.
def eta(x):
    return min(1.,max(0.,3.*x-1.))
def twist(z,s):
    return z*cmath.exp(2j*math.pi*eta(abs(z)/s)) if s else z
samples=[]
for s in [1.,.5,.25,.125,.0625,.03125]:
    displacement=max(abs(twist(r*s/120*cmath.exp(2j*math.pi*k/64),s)-r*s/120*cmath.exp(2j*math.pi*k/64)) for r in range(121) for k in range(64))
    assert displacement <= 4*s/3+1e-12
    samples.append({'scale':s,'grid_max_displacement':displacement,'proved_uniform_bound':4*s/3})
rows['escaping_twist']=samples

# Infinite cyclic example: two identical local radial rotations and a half-turn
# exchanging their supports.  These formulas are extended by the identity.
r0=.2
centres=(-1+0j,1+0j)
def local_f(z):
    for q in centres:
        r=abs(z-q)
        if r<r0:
            return q+(z-q)*cmath.exp(1j*math.sqrt(2)*(1-r/r0))
    return z

def half_turn(z):
    r=abs(z)
    taper=1. if r<=1.5 else max(0.,(2.5-r))
    return z*cmath.exp(1j*math.pi*taper)
pts=[complex(x/40,y/40) for x in range(-100,101) for y in range(-100,101)]
comm=max(abs(local_f(half_turn(z))-half_turn(local_f(z))) for z in pts)
assert comm<1e-12
assert abs(half_turn(-1)-1)<1e-12 and abs(half_turn(1)+1)<1e-12
rows['infinite_cyclic_centralizer']={'grid_points':len(pts),'maximum_commutator_error':comm,'half_turn_exchanges_centres':True,'radial_rotation_angle_at_half_radius':'sqrt(2)/2','infinite_order_proof':'Its angle divided by 2*pi is irrational because pi is transcendental and sqrt(2)/2 is nonzero algebraic.'}

# Exact finite detector for why E/L and E/E_i have different projections to Gamma.
E=list(range(4)); L={0,2}; Ei=set(E)
cosets_L={tuple(sorted((x+l)%4 for l in L)) for x in E}
cosets_Ei={tuple(sorted((x+l)%4 for l in Ei)) for x in E}
well_L=all(len({x%2 for x in c})==1 for c in cosets_L)
well_Ei=all(len({x%2 for x in c})==1 for c in cosets_Ei)
assert well_L and not well_Ei
rows['coset_projection_detector']={'E':'C4','L':'2C4','E_i':'C4','Gamma':'C2','projection_defined_on_E_mod_L':well_L,'projection_defined_on_E_mod_Ei':well_Ei}

out=Path(__file__).with_name('verify_c_examples_output.json')
out.write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps(rows,indent=2))
print('ALL ASSERTIONS PASSED')
