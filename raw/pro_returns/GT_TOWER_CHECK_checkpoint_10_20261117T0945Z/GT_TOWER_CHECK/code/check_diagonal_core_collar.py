#!/usr/bin/env python3
"""Exact collar-lattice calculation with the origin cap retained."""
from pathlib import Path
import json,math
import sympy as sp

eps,n1,nd,m=sp.symbols('epsilon n1 nd m',integer=True)
# Coordinates: origin,a1,a2,a3,outerDplus,outerDminus.
perm=[0,2,1,3,5,4]
def P(v):return sp.Matrix([v[i] for i in perm])
N=sp.Matrix([-eps,n1,-n1,0,nd,-nd])
origin=sp.Matrix([1,0,0,0,0,0])
assert N+P(N)==-2*eps*origin
c=sp.Matrix([0,n1*m,0,0,nd*m,0])
# In the central extension, I^2=t_origin^epsilon.
# The formula I*T^{-1}, T=t^(N*m), has offset -P(N)*m.
action_offset=-P(N)*m
gauge_offset=c-P(c)
assert sp.simplify(action_offset-gauge_offset)==eps*m*origin
square_offset=action_offset+P(action_offset)+eps*origin
assert sp.simplify(square_offset-eps*(2*m+1)*origin)==sp.zeros(6,1)
assert list(action_offset)[1:]==list(gauge_offset)[1:]

checks=0
for exponent in range(2,33):
    for lam in range(1,2*exponent):
        if math.gcd(lam,2*exponent)!=1:continue
        nu=(lam-1)//2
        for e in (-1,1):
            for a in range(-2,3):
                for b in range(-2,3):
                    sub={eps:e,n1:a,nd:b,m:nu}
                    lhs=[int(x.subs(sub))%exponent for x in action_offset]
                    rhs=[int(x.subs(sub))%exponent for x in gauge_offset]
                    assert lhs[1:]==rhs[1:]
                    checks+=1
out={'coordinate_order':['origin','a1','a2','a3','Dplus','Dminus'],
     'involution_permutation':perm,
     'exact_integer_displacement_identity':True,
     'exact_capped_coboundary_identity':True,
     'uncapped_square_maps_to_lambda_power':True,
     'finite_checks':checks,'all_assertions_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS exact symbolic collar identity, including the uncapped origin square.')
print('PASS capped pure-multitwist gauge for',checks,'finite coefficient cases.')
