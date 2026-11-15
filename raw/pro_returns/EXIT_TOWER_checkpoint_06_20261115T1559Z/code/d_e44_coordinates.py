"""Exact rational and finite-colour certificates for the E.44 audit."""
from itertools import permutations
from pathlib import Path
import json
import sympy as sp

z = sp.symbols("z")
u = (z*z+1)**2/(4*z*z)
lam = ((z*z-1)/(z*z+1))**2
ell_b = z*z
ell_a = ((z-1)/(z+1))**2
U = lambda ell: (ell+1)**2/(4*ell)
checks = {
    "lambda_equals_1_minus_1_over_u": sp.cancel(lam-(1-1/u)) == 0,
    "U_b_equals_u": sp.cancel(U(ell_b)-u) == 0,
    "U_a_equals_u_over_u_minus_1": sp.cancel(U(ell_a)-u/(u-1)) == 0,
}
assert all(checks.values())

identity = (0, 1, 2, 3)
compose = lambda p, q: tuple(p[q[i]] for i in range(4))
V = {identity, (1,0,3,2), (2,3,0,1), (3,2,1,0)}
blocks = {frozenset((0,1)), frozenset((2,3))}
C4 = {p for p in permutations(range(4))
      if frozenset(p[i] for i in (0,1)) == frozenset((0,1))
      and frozenset(p[i] for i in (2,3)) == frozenset((2,3))}
D8 = {p for p in permutations(range(4))
      if {frozenset(p[i] for i in b) for b in blocks} == blocks}
assert len(V) == len(C4) == 4
assert len(D8) == 8
assert len(C4 & V) == 2
assert {compose(p,q) for p in C4 for q in V} == D8
result = {
    "rational_identities": checks,
    "colour_groups": {
        "V_order": len(V), "C4_order": len(C4), "D8_order": len(D8),
        "C4_intersection_V_order": len(C4 & V),
        "C4_times_V_equals_D8": True,
    },
    "scope": "Exact rational identities and finite permutation groups only; the group and profinite comparisons are proved in the audit note."
}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
