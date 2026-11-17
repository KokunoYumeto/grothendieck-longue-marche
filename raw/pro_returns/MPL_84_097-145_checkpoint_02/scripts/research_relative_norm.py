#!/usr/bin/env python3
"""Universal local relative-norm checks for scans 103, 105-107.

Research only: no transcription files are read or changed. Monic reductions
use integer polynomial coefficients; no base parameter is inverted.
"""
import json
import sympy as s

b1, b2, c1, c2, t, u, v = s.symbols('b1 b2 c1 c2 t u v')
xs = s.symbols('x0:4')
ys = s.symbols('y0:4')
C = b1*b1*c2 + b2*b2*c1 - 4*c1*c2
rel_A = t*t + b1*b2*t + C
rel_u = u*u + b1*u + c1
rel_v = v*v + b2*v + c2

def red_B(e):
    return s.expand(s.rem(s.rem(s.expand(e), rel_u, u), rel_v, v))

def red_A(e):
    return s.expand(s.rem(s.expand(e), rel_A, t))

def elem(z):
    return z[0] + z[1]*u + z[2]*v + z[3]*u*v

def coeffs(e):
    p = s.Poly(red_B(e), u, v)
    return [p.coeff_monomial(m) for m in [1, u, v, u*v]]

def conjugate(e):
    return red_B(e.subs({u: -b1-u, v: -b2-v}, simultaneous=True))

def trace(z):
    return 2*z[0] - b1*z[1] - b2*z[2] + (t+b1*b2)*z[3]

def norm(z):
    a, b, c, d = z
    return s.expand(a*a + c1*b*b + c2*c*c + c1*c2*d*d
                    - b1*a*b - b2*a*c + (t+b1*b2)*a*d
                    - t*b*c - b2*c1*b*d - b1*c2*c*d)

x, y = elem(xs), elem(ys)
w = 2*u*v + b1*v + b2*u
checks = {}
checks['iN_equals_x_conjugate_x'] = red_B(norm(xs).subs(t,w) - x*conjugate(x)) == 0
checks['polarization_equals_trace_x_conjugate_y'] = red_A(norm([a+b for a,b in zip(xs,ys)]) - norm(xs) - norm(ys) - trace(coeffs(x*conjugate(y)))) == 0
checks['multiplicativity_of_relative_norm'] = red_A(norm(coeffs(x*y)) - norm(xs)*norm(ys)) == 0
a, b, c, d = s.symbols('a b c d')
checks['A_linearity_of_relative_trace'] = red_A(trace(coeffs((a+b*w)*x)) - (a+b*t)*trace(xs)) == 0
checks['pure_tensor_norm'] = s.expand(norm([a*c,b*c,a*d,b*d]) - (a*a-b1*a*b+c1*b*b)*(c*c-b2*c*d+c2*d*d)) == 0
checks['restriction_to_A_is_square'] = red_A(norm(coeffs(a+b*w)) - (a+b*t)**2) == 0

# Absolute rank-four norm is the product of the four conjugates.
x1 = red_B(x.subs(u,-b1-u))
x2 = red_B(x.subs(v,-b2-v))
x3 = conjugate(x)
absolute = red_B(red_B(x*x1)*red_B(x2*x3))
relative = red_A(norm(xs)*norm(xs).subs(t,-b1*b2-t))
checks['norm_transitivity'] = s.expand(absolute-relative) == 0
assert all(checks.values()), checks
print(json.dumps({
    'coefficient_ring': 'Z[b1,b2,c1,c2,x0,x1,x2,x3,y0,y1,y2,y3]',
    'method': 'Exact symbolic reduction by monic quadratic relations; no scalar parameter inverted.',
    'ordered_B_basis': ['1','u','v','uv'],
    'quadratic_form_diagonal_coefficients': ['1','c1','c2','c1*c2'],
    'quadratic_form_mixed_coefficients_in_01_02_03_12_13_23_order': ['-b1','-b2','t+b1*b2','-t','-b2*c1','-b1*c2'],
    'checks': checks,
    'scope': 'Local algebraic identities only; no reading correction, global coherence claim, or literature novelty claim.',
},indent=2))
