"""Exact checks for F.46's finite-etale tangent correspondences.

The uniformization and commensurator proof is in sections/F.tex.
This program checks the explicit rational witnesses over Q.
"""
import json
from pathlib import Path
import sympy as sp

u, v = sp.symbols("u v")
maps = {
    "P": 4*u/(1+u)**2,
    "Q_plus": u**2,
    "Q_minus": u**2/(u**2-1),
}
boundary = [sp.Integer(0), sp.Integer(1), sp.Integer(-1), sp.oo]

def valuation_at_zero(expr, variable):
    num, den = sp.fraction(sp.cancel(expr))
    def order(poly):
        terms = sp.Poly(poly, variable).terms()
        return min(monomial[0] for monomial, coeff in terms if coeff != 0)
    return order(num)-order(den)

def value_and_degree(f, point):
    parameter = v
    local = sp.cancel(f.subs(u, 1/v if point == sp.oo else point+v))
    order = valuation_at_zero(local, parameter)
    if order < 0:
        return "infinity", -order
    value = sp.cancel(local).limit(parameter, 0)
    return str(value), valuation_at_zero(local-value, parameter)

out = {}
for name, f in maps.items():
    num, den = sp.fraction(sp.cancel(f))
    degree = max(sp.degree(num, u), sp.degree(den, u))
    assert degree == 2
    assert sp.degree(sp.gcd(num, den), u) == 0
    finite_preimages = set()
    for polynomial in (num, den, num-den):
        finite_preimages.update(sp.solve(polynomial, u))
    assert finite_preimages == {sp.Integer(-1), sp.Integer(0), sp.Integer(1)}
    table = {str(point): value_and_degree(f, point) for point in boundary}
    assert all(value in {"0", "1", "infinity"} for value, _ in table.values())
    total_ramification = sum(local_degree-1 for _, local_degree in table.values())
    assert total_ramification == 2*degree-2 == 2
    leading = sp.limit(f/u**(1 if name == "P" else 2), u, 0)
    out[name] = {
        "map": str(sp.factor(f)),
        "degree": int(degree),
        "boundary_value_and_local_degree": table,
        "total_boundary_ramification": int(total_ramification),
        "leading_at_zero": str(leading),
    }

assert sp.limit(maps["P"]/u, u, 0) == 4
assert sp.limit(maps["Q_plus"]/u**2, u, 0) == 1
assert sp.limit(maps["Q_minus"]/u**2, u, 0) == -1
out["selected_parameters"] = {
    "P_and_Q_plus": "16",
    "P_and_Q_minus": "-16",
    "source_tangents": ["4", "-4"],
}
out["all_checks_passed"] = True
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(out, indent=2)+"\n")
print(json.dumps(out, indent=2))
