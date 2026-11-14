"""Finite checks accompanying the precisely bounded Part A conclusions."""
from pathlib import Path
from itertools import product
import json
import math
import sympy as S

x=S.symbols('x')
f=S.Poly(x**5-x,x,modulus=3)
gcd=S.gcd(f,f.diff())
assert gcd.degree()==0
points=[(a,b) for a in range(3) for b in range(3) if (b*b-(a**5-a))%3==0]

def hyperplanes(ell,d):
    vs=list(product(range(ell),repeat=d))
    forms=[]
    for a in vs[1:]:
        lead=next(t for t in a if t)
        if lead==1:forms.append(a)
    counts=[]
    for v in vs:
        counts.append(sum(sum(ai*vi for ai,vi in zip(a,v))%ell==0 for a in forms))
    c=(ell**(d-1)-1)//(ell-1)
    assert counts[0]==ell**(d-1)+c and all(t==c for t in counts[1:])
    return {'ell':ell,'dimension':d,'hyperplanes':len(forms),
      'zero_multiplicity':counts[0],'nonzero_multiplicity':c,
      'identity_coefficient':ell**(d-1)}

out={'explicit_curve_for_kernel_counterexample':{
 'field':'F_3','curve':'y^2=x^5-x','genus':2,'base_point':'infinity',
 'gcd_f_derivative_mod_3':str(gcd.as_expr()),'affine_rational_points':points,
 'rational_infinity_points':1,'K2_geometric_order':2**34,
 'pullback_JC8_geometric_order':4**4},
 'incidence_checks':[hyperplanes(2,4),hyperplanes(3,4),hyperplanes(5,2)],
 'local_system_sufficient_condition_limits':{
  str(p):{'max_order_mod_p':p-1,'max_abelian_dimension_for_strict_inequality':(p-2)//2}
  for p in [2,3,5,7,11,17]}}
Path(__file__).with_name('A_finite_route_checks_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
