#!/usr/bin/env python3
"""Exact finite checks accompanying the D.25 proof; no numerical inference."""
import json
from pathlib import Path

T0 = [[1, 2], [0, 1]]
T1 = [[1, 0], [-2, 1]]
Tinf = [[1, -2], [2, -3]]
I = [[1, 0], [0, 1]]
def mul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)]
            for i in range(2)]
def mv(a, v):
    return [sum(a[i][j]*v[j] for j in range(2)) for i in range(2)]
assert mul(mul(T0, T1), Tinf) == I
monodromy = []
for name, mat, vec in [("0", T0, [1, 0]), ("1", T1, [0, 1]),
                       ("infinity_squared", mul(Tinf, Tinf), [1, 1])]:
    assert mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0] == 1
    assert mv(mat, vec) == vec
    assert mat != I
    assert [[x % 2 for x in row] for row in mat] == I
    monodromy.append({"cusp": name, "matrix": mat, "fixed_vector": vec,
                       "fixed_line_mod_2": vec})
assert len({tuple(x["fixed_line_mod_2"]) for x in monodromy}) == 3
residue = []
for p in [17, 3, 5, 7]:
    roots = [a for a in range(1, p) if pow(a, 8, p) == 16 % p]
    assert roots
    residue.append({"prime": p, "prime_mod_8": p % 8,
                    "all_eighth_roots_of_16_mod_p": roots})
result = {
    "claim": "D.25",
    "T0_times_T1_times_Tinfinity": mul(mul(T0, T1), Tinf),
    "monodromy_and_distinct_fixed_lines": monodromy,
    "single_level_exception_representatives": residue,
    "infinite_argument": "For p=3,5,7 mod8 the eighth-power subgroup of Fp* "
        "is the square, fourth-power, square subgroup respectively, and contains16. "
        "For p=1 mod8, 2 is a square and16=(sqrt(2))^8. Hensel lifts every "
        "nonzero root for odd p. This finite file checks representatives only; "
        "the all-prime proof is in the manuscript.",
    "scope": "Checks the exact matrices and a residue representative in each "
             "odd class mod8; does not compute any global section."
}
out = Path(__file__).resolve().parent.parent / "audit" / "D_legendre_density_certificate.json"
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"output": str(out), "fixed_lines": [x["fixed_line_mod_2"] for x in monodromy],
                  "residue_classes": [x["prime_mod_8"] for x in residue]}, indent=2))
