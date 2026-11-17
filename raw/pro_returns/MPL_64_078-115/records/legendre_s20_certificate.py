#!/usr/bin/env python3
"""Exact certificates for RC13. Research calculations, not manuscript readings.

Run with Python and SymPy. Outputs a JSON record to stdout. The rational
identity is over Q(x,lambda). Finite-field checks use 4*L to avoid denominators;
all listed primes are odd, so this is equivalent to checking L.
"""
from math import comb
import json
import sympy as sp

x, lam = sp.symbols("x lambda")
P = x*(x-1)*(x-lam)
f = x*(x-1)/(2*(x-lam))
# omega=dx/y; partial_lambda omega/omega = 1/(2*(x-lambda)).
first = 1/(2*(x-lam))
second = sp.diff(first, lam) + first**2
Lomega = lam*(1-lam)*second + (1-2*lam)*first - sp.Rational(1, 4)
exact = sp.diff(f, x) - f*sp.diff(P, x)/(2*P)
residual = sp.cancel(Lomega-exact)
assert residual == 0

finite = []
for p in (3, 5, 7, 11):
    m = (p-1)//2
    H = sum(comb(m,k)**2*lam**k for k in range(m+1))
    # Integer identity, stronger than its reduction modulo p.
    coefficient = sp.Poly(sp.expand(P**m), x).coeff_monomial(x**(p-1))
    coefficient_residual = sp.expand(coefficient-(-1)**m*H)
    assert coefficient_residual == 0
    fourLH = sp.expand(4*lam*(1-lam)*sp.diff(H,lam,2)
                       +4*(1-2*lam)*sp.diff(H,lam)-H)
    mod_residual = sp.Poly(fourLH,lam,modulus=p)
    assert mod_residual.is_zero
    recurrence_residuals = [
        (j+1)**2*(comb(m,j+1)**2 if j<m else 0)
        -(m-j)**2*comb(m,j)**2
        for j in range(m+1)
    ]
    assert all(v == 0 for v in recurrence_residuals)
    finite.append({
        "p":p, "m":m,
        "H_coefficients_ascending_mod_p":[comb(m,k)**2 % p for k in range(m+1)],
        "x_power_coefficient_ascending_mod_p":[
            ((-1)**m*comb(m,k)**2) % p for k in range(m+1)],
        "integer_coefficient_identity_residual":str(coefficient_residual),
        "four_LH_mod_p":str(mod_residual.as_expr()),
        "integer_binomial_recurrence_residuals":recurrence_residuals,
    })

print(json.dumps({
    "calculation":"RC13: conventional Legendre comparison, not a manuscript assertion",
    "sympy_version":sp.__version__,
    "P":str(P), "f":str(f),
    "Lomega_divided_by_omega":str(sp.factor(Lomega)),
    "d_x_f_over_y_divided_by_omega":str(sp.factor(exact)),
    "rational_residual":str(residual),
    "finite_field_checks":finite,
    "scope":"A polynomial solution of this order-two equation does not establish zero p-curvature."
},ensure_ascii=False,indent=2))
