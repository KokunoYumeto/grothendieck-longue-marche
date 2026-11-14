#!/usr/bin/env python3
"""Exact polynomial witness for the intrinsic two-Hom tangential test."""
from pathlib import Path
import json
import sympy as sp

z=sp.symbols('z')
b=2*z**2-z**4
p=z
q=z**2/2
assert sp.expand(sp.diff(b,z)-4*z*(1-z)*(z+1))==0
assert sp.expand(b+z**2*(z**2-2))==0
assert sp.expand((b-1)+(z-1)**2*(z+1)**2)==0
critical=[sp.Integer(0),sp.Integer(1),sp.Integer(-1)]
assert [sp.expand(b.subs(z,c)) for c in critical]==[0,1,1]
assert sp.degree(b,z)==4
assert sp.limit(p/z,z,0)==1
assert sp.limit(q/z**2,z,0)==sp.Rational(1,2)
assert sp.Rational(1,2)*2**2==2

out={
 'belyi_polynomial':str(b),
 'degree':4,
 'derivative_factorization':str(sp.factor(sp.diff(b,z))),
 'zero_factorization':str(sp.factor(b)),
 'one_factorization':str(sp.factor(b-1)),
 'finite_critical_points':[str(c) for c in critical],
 'finite_critical_values':[str(b.subs(z,c)) for c in critical],
 'infinity_ramification_degree':4,
 'boundary':['0','1','-1','sqrt(2)','-sqrt(2)','infinity'],
 'P':str(p),'Q':str(q),
 'local_degrees_at_zero':[1,2],
 'leading_coefficients':['1','1/2'],
 'equal_image_parameter_equation':'beta = -kappa(2) + 2 beta',
 'unique_parameter':'beta = kappa(2)',
 'tangent_value':2,
 'both_image_tangent_values':[2,2],
 'all_checks_passed':True,
 'scope':'Exact finite polynomial witness; the general theorem uses open Hom reconstruction and marked Belyi maps.'
}
Path(__file__).with_name('two_hom_tangents_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
