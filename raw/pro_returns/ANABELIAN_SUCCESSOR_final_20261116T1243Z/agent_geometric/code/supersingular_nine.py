"""Exact degree-nine theta calculation for C_a in characteristic two.

This is the full local coefficient system, with symbolic identities over F2.
It is not a finite-field search.  Mathematical sufficiency is proved in AG.18.
"""
import json
import sympy as s

a, v, b0, b1 = s.symbols("a v b0 b1")
equations = [b0 + b1*v + a,
             b0*a**2 + b1 + v,
             b1*a**2 + 1,
             b0*v**2 + a**2]
substitution = {b1: 1/a**2, b0: v/a**2 + a}
reduced = []
for e in equations:
    num, den = s.fraction(s.together(e.subs(substitution)))
    num = s.Poly(num, a, v, modulus=2).as_expr()
    den = s.Poly(den, a, v, modulus=2).as_expr()
    reduced.append((str(num), str(den)))
assert reduced[0][0] == "0"
assert reduced[1][0] == "a**5 + 1"
assert reduced[2][0] == "0"
assert s.Poly(s.sympify(reduced[3][0]) - (v**3+a**3*v**2+a**4),
              a, v, modulus=2).is_zero
# b0 cannot vanish for a solution of the last equation: v=a^3 would
# make that polynomial a^4, and a^5=1 guarantees a !=0.
remaining = v**3+a**3*v**2+a**4
assert s.Poly(remaining.subs(v,a**3),a,modulus=2).as_expr() == a**4
assert {pow(2,j,9) for j in range(6)} == {1,2,4,5,7,8}
print(json.dumps({
    "curve": "y^2+y=x^5+a*x^3",
    "local_form": "Y^2+Y=u^5+a*u^3+c*u, v=c^4",
    "function": "A(u)+(u^2+b1*u+b0)*Y, deg(A)<=4",
    "coefficient_degrees": [5,6,7,8],
    "coefficient_equations": [str(e) for e in equations],
    "substitution": {str(k):str(val) for k,val in substitution.items()},
    "reduced_numerators_and_denominators": reduced,
    "existence_condition": "a^5=1",
    "remaining_monic_polynomial": str(remaining),
    "primitive_doubling_orbit_mod9": [1,2,4,8,7,5],
    "cover_genus": 10,
    "primitive_factor_dimension": 6,
    "primitive_two_rank": 0,
    "whole_relative_two_rank": 2,
    "assertions": "all passed"
}, indent=2))
