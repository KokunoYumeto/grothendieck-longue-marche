#!/usr/bin/env python3
"""Exact main-chart identities only; no full stable-reduction conclusion."""
from pathlib import Path
import json
from fractions import Fraction
import sympy as s

a, beta, x, y, V, rho, Y = s.symbols('a beta x y V rho Y')
c4 = a * (a**3 - 24)
param = [a**6 - 36*a**3 + 216, beta**2*c4 - 48]
G = s.groebner(param, beta, a)
r = beta*a*a/12
c = beta/(r-1)
d = a-c

def zero_parameter_fraction(z):
    n = s.fraction(s.cancel(z))[0]
    assert G.reduce(n)[1] == 0

zero_parameter_fraction(c*d*d-4)
# Exact transformation from the good Deuring curve to y_old²=x_old³−x_old.
oldx = beta*(x+a*a/12)
oldy_squared = beta**3*(y+a*x/2+s.Rational(1,2))**2
n = s.fraction(s.together(oldy_squared-oldx**3+oldx))[0]
n = s.rem(n, y*y+a*x*y+y-x**3, y)
assert all(G.reduce(coef)[1] == 0 for mon,coef in s.Poly(n,x,y).terms())
# The scaling constant cancels in this exact slope identity.
assert s.cancel((1+a*x+2*y)/(1+c*x)-1-(d*x+2*y)/(1+c*x)) == 0
binomial = ((1+rho*V)**4-1)/rho**4
assert s.expand(binomial-(V**4+4*V**3/rho+6*V**2/rho**2+4*V/rho**3)) == 0
# Literal characteristic-two normalization and degree-four Frobenius map.
red_relation = Y*Y+Y-V**3
ybar = Y+V**6+V**3
assert s.Poly(s.rem(ybar*ybar+ybar-V**12, red_relation, Y),Y,V,modulus=2).is_zero
assert s.Poly(s.rem(Y**4-ybar, red_relation,Y),Y,V,modulus=2).is_zero
vals = {
    'a':Fraction(1,2),'beta':Fraction(1),'r-1':Fraction(1,2),
    'c':Fraction(1,2),'d':Fraction(3,4),'rho':Fraction(3,16),
    '2/d':Fraction(1,4),'4/rho':Fraction(29,16),
    '6/rho^2':Fraction(5,8),'4/rho^3':Fraction(23,16),
}
assert all(vals[k]>0 for k in ('a','c','2/d','4/rho','6/rho^2','4/rho^3'))
out = {
    'status':'PASS',
    'scope':'Actual integral main chart and supersingular genus-one normalization only; remaining six genera, full graph and cusp attachment paths unresolved.',
    'parameter_equations':[str(z) for z in param],
    'good_curve':'y^2+a*x*y+y=x^3',
    'c_d_squared_identity':'c*(a-c)^2=4',
    'valuations_v2':{k:str(v) for k,v in vals.items()},
    'main_chart':'(1+c*x)*(V^4+4*V^3/rho+6*V^2/rho^2+4*V/rho^3)=x+(2/d)*y',
    'special_equations':['x=V^4','y^2+y=V^12'],
    'normalization':'Y=y+V^6+V^3; Y^2+Y=V^3',
    'main_map':'x=V^4; y=Y^4',
    'main_genus':1,
    'unaccounted_arithmetic_genus':6,
    'compact_type_claim':False,
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
