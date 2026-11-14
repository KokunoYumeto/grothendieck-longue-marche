#!/usr/bin/env python3
"""Independent symbolic ideal-reduction check of the degree-nine norm.

This uses SymPy polynomial division over F_2, independently of the
bit-field arithmetic in A_theta_nine_certificate.py. It verifies the
finite polynomial and local-value inputs; the paper proves the divisor,
theta, deck-action, and section assertions.
"""
import json
from pathlib import Path
import sympy as sp

x, t = sp.symbols('x t')
phi = sp.Poly(t**4+t**3+t**2+t+1, t, modulus=2)

def reduce_coefficient(c):
    return sp.rem(sp.Poly(c, t, modulus=2), phi).as_expr()

def reduce_polynomial(f):
    f = sp.Poly(sp.expand(f), x)
    return sp.expand(sum(reduce_coefficient(c)*x**monomial[0]
                         for monomial,c in f.terms()))

alpha = t+t**4
a = x**3+t*x**2+t*x+t**2
b = x**3+(t**2+t+1)*x**2+(t**2+t+1)*x+t**2
u = x*(x+1)
artin_schreier_numerator = x**3+x**2+(alpha+1)*x+1
norm_numerator = u*(a*a+a*b)+b*b*(artin_schreier_numerator+(t+1)*u)
residual = reduce_polynomial(norm_numerator-(x+t)**9)
assert residual == 0
assert reduce_coefficient(alpha**2+alpha+1) == 0
assert reduce_coefficient(t**5-1) == 0
assert reduce_coefficient(a.subs(x,t)) == 0
assert reduce_coefficient(b.subs(x,t)-1) == 0
assert reduce_coefficient(b.subs(x,0)) != 0
assert reduce_coefficient(b.subs(x,1)) != 0
assert reduce_coefficient(artin_schreier_numerator.subs(x,t)
                          -(t+1)*u.subs(x,t)) == 0

# These are exact divisor vectors in the ordered support
# (R, W0, W1, Winfinity), deduced geometrically in the paper.
div_h = (9,-1,-1,-7)
div_u = (0,2,2,-4)
div_quotient = tuple(a-4*b for a,b in zip(div_h,div_u))
assert div_quotient == (9,-9,-9,9)
assert sum(div_h) == sum(div_u) == sum(div_quotient) == 0

result = {
    'status':'PASS',
    'method':'symbolic coefficient reduction modulo 2 and t^4+t^3+t^2+t+1',
    'norm_identity_residual':str(residual),
    'reduced_norm_numerator':str(reduce_polynomial(norm_numerator)),
    'local_values':{
        'a(t)':str(reduce_coefficient(a.subs(x,t))),
        'b(t)':str(reduce_coefficient(b.subs(x,t))),
        'b(0)':str(reduce_coefficient(b.subs(x,0))),
        'b(1)':str(reduce_coefficient(b.subs(x,1)))},
    'divisor_support':['R','W0','W1','Winfinity'],
    'div_h_minus_four_div_u':div_quotient,
    'limitations':'Finite identities only; divisor orders, exact torsion order, theta orbit and injectivity are proved in the manuscript.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
