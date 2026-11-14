"""Exact finite checks accompanying the all-orders proof of F.51."""
from fractions import Fraction
from itertools import product
from math import factorial, lcm
from pathlib import Path
import json

supports = []
rotation_tests = 0
nonradial_witnesses = []
for n in range(1, 17):
    scale = Fraction(1, 2**n)
    lower, center, upper = (Fraction(11, 16)*scale,
                            Fraction(3, 4)*scale,
                            Fraction(13, 16)*scale)
    assert scale/2 < lower < center < upper < scale
    if supports:
        assert upper < supports[-1][0]
    supports.append((lower, upper))
    for m in range(1, n+1):
        for residue in range(m):
            assert (factorial(n)*residue) % m == 0
            rotation_tests += 1
    # At phase 0 and phase 1/(2*n!) of one full turn, cosine is +1,-1.
    assert factorial(n)*Fraction(1, 2*factorial(n)) == Fraction(1, 2)
    nonradial_witnesses.append({"n": n, "radius": str(center),
                               "positive_value": str(scale),
                               "negative_value": str(-scale)})

tuple_tests = 0
for degree in (1, 2, 3):
    for orders in product(range(1, 9), repeat=degree):
        stage = max(orders)
        assert factorial(stage) % lcm(*orders) == 0
        tuple_tests += 1

# The parabolic matrix [[1,0],[1,1]] has nth power [[1,0],[n,1]].
def mul(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))

for m in range(-20, 21):
    for n in range(-20, 21):
        assert mul(((1, 0), (m, 1)), ((1, 0), (n, 1))) == ((1, 0), (m+n, 1))

result = {
    "status": "all checks passed",
    "annular_supports_checked": len(supports),
    "rotation_residue_tests": rotation_tests,
    "tuple_subgroup_tests": tuple_tests,
    "parabolic_matrix_products": 41**2,
    "nonradial_witnesses": nonradial_witnesses,
    "scope": "Finite exact checks support the explicit formulas; the proofs in F.51 establish all orders and all neighbourhoods."
}
dest = Path(__file__).with_suffix('.output.json')
dest.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k:v for k,v in result.items() if k != 'nonradial_witnesses'}, indent=2))
