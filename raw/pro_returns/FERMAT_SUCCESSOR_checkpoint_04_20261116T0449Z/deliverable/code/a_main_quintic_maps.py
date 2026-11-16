"""Exact symbolic certificate for Jac(plus Fermat5) ~ Jac(y²+y=x⁵)^3.

The three maps, six differential pullbacks, and the nonzero determinant
are checked over Q(X,Y)/(X^5+Y^5+1). No numerical approximation is used.
"""
from pathlib import Path
import json
import sympy as s

X, Y = s.symbols("X Y")
F = X**5 + Y**5 + 1
G = s.groebner([F], X, Y, domain=s.QQ)
omega_coefficients = [1, -X*Y, X**2, -Y, Y**2, -X]
monomials = [1, X, Y, X**2, X*Y, Y**2]
maps = [(-X*Y, X**5), (-Y/X**2, Y**5/X**5), (-X/Y**2, 1/Y**5)]

def remainder(q):
    numerator, denominator = s.fraction(s.cancel(q))
    assert denominator != 0
    return s.expand(G.reduce(numerator)[1])

def derivative(q):
    return s.diff(q,X) - (X**4/Y**4)*s.diff(q,Y)

checks = []
for i, (u,v) in enumerate(maps):
    assert remainder(v**2+v-u**5) == 0
    c0 = omega_coefficients[2*i]
    c1 = omega_coefficients[2*i+1]
    assert remainder(Y**4*derivative(u)/(2*v+1)-c0) == 0
    assert remainder(Y**4*u*derivative(u)/(2*v+1)-c1) == 0
    checks.append({"u":str(u),"v":str(v),
                   "pullbacks_relative_to_dX_over_Y4":[str(c0),str(c1)],
                   "curve_identity_remainder":0,"differential_remainders":[0,0]})

matrix = s.Matrix([[s.Poly(c,X,Y).coeff_monomial(m)
                    for m in monomials] for c in omega_coefficients])
assert abs(matrix.det()) == 1
report={"model":"X^5+Y^5+Z^5=0", "target":"v^2+v=u^5",
        "chart":"Z=1", "basis":"(1,X,Y,X^2,XY,Y^2) dX/Y^4",
        "maps":checks,"differential_matrix":matrix.tolist(),
        "determinant":int(matrix.det()),
        "conclusion":"The induced product of Jacobian maps is a Q-isogeny to J^3."}
print(json.dumps(report,indent=2,default=int))
print("PASS: all curve identities, differential identities, and determinant are exact")
