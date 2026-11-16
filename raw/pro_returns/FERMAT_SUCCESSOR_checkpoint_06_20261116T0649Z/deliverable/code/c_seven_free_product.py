#!/usr/bin/env python3
"""Exact finite arithmetic and boundary checks for Statements B.29--B.30.

This checks the finite inputs; the full pro-3 free-product theorem is
proved cohomologically in B_cusp_counterexample.tex, not inferred here.
Only Python's standard library is required.
"""
from itertools import combinations, product
from math import gcd
import json


def mul(x, y):
    """Multiplication in Z[z]/(z^2+z+1), with x=(a,b)=a+b*z."""
    a, b = x
    c, d = y
    return (a*c-b*d, a*d+b*c-b*d)


def conjugate(x):
    a, b = x
    return (a-b, -b)


def norm(x):
    result = mul(x, conjugate(x))
    assert result[1] == 0
    return result[0]


def det_mod(matrix, modulus=3):
    a = [[entry % modulus for entry in row] for row in matrix]
    result = 1
    for i in range(len(a)):
        pivot = next((j for j in range(i, len(a)) if a[j][i]), None)
        if pivot is None:
            return 0
        if pivot != i:
            a[pivot], a[i] = a[i], a[pivot]
            result = -result
        entry = a[i][i]
        result = result*entry % modulus
        inverse = pow(entry, -1, modulus)
        for j in range(i+1, len(a)):
            coefficient = a[j][i]*inverse % modulus
            a[j] = [(x-coefficient*y) % modulus
                    for x, y in zip(a[j], a[i])]
    return result % modulus


def kummer_unit_character(residue, zeta_residue):
    symbol = pow(residue, 2, 7)
    exponent = next(j for j in range(3) if pow(zeta_residue, j, 7) == symbol)
    return exponent, symbol


def boundary_vector(index):
    """Z^9/<sum e_i>, using e_0,...,e_7 as a basis."""
    if index == 8:
        return [-1]*8
    return [int(i == index) for i in range(8)]


def primitive_rank_two(u, v):
    minors = [u[i]*v[j]-u[j]*v[i] for i, j in combinations(range(8), 2)]
    divisor = 0
    for minor in minors:
        divisor = gcd(divisor, abs(minor))
    return divisor == 1


zeta = (0, 1)
lam = (1, -1)
pi = (2, -1)
pibar = conjugate(pi)
assert pibar == (3, 1)
assert mul(pi, pibar) == (7, 0)
assert norm(lam) == 3
assert norm(pi) == norm(pibar) == 7
assert mul(mul(zeta, zeta), zeta) == (1, 0)

unit_rows = []
residue_checks = []
for root in (2, 4):
    assert (root*root+root+1) % 7 == 0
    residue = (1-root) % 7
    kz, sz = kummer_unit_character(root, root)
    kl, sl = kummer_unit_character(residue, root)
    unit_rows.append([kz, kl])
    residue_checks.append({"zeta": root, "lambda": residue,
                           "symbols": [sz, sl], "characters": [kz, kl]})
assert unit_rows == [[2, 0], [2, 2]]
assert det_mod(unit_rows) == 1

determinants = set()
for a, b, c, d in product(range(3), repeat=4):
    matrix = [[2, 0, a, b], [2, 2, c, d],
              [0, 0, 1, 0], [0, 0, 0, 1]]
    determinants.add(det_mod(matrix))
assert determinants == {1}

# Cusps have labels (zero coordinate, exponent j in -zeta^j).
# Rational cusps are j=0; P has label (0,1), index 1.
cusps = [(zero, exponent) for zero in range(3) for exponent in range(3)]
rational_indices = [i for i, (_, exponent) in enumerate(cusps) if exponent == 0]
assert rational_indices == [0, 3, 6]
P_index = 1
assert cusps[P_index] == (0, 1)
assert all(primitive_rank_two(boundary_vector(P_index), boundary_vector(i))
           for i in rational_indices)
assert all(primitive_rank_two(boundary_vector(i), boundary_vector(j))
           for i, j in combinations(range(9), 2))

# The nine cusps reduce to nine distinct F_7 points.  The cubic has
# no additional F_7 points.  This is auxiliary, not used for a != 0.
projective_points = set()
for x, y, z in product(range(7), repeat=3):
    if (x, y, z) == (0, 0, 0) or (x**3+y**3+z**3) % 7:
        continue
    first = next(v for v in (x, y, z) if v)
    inverse = pow(first, -1, 7)
    projective_points.add(tuple(v*inverse % 7 for v in (x, y, z)))
assert len(projective_points) == 9
assert all(0 in point for point in projective_points)

# B.34 uses this actual integral complex-conjugation matrix from B.28.
C_E = ((1, -1), (0, -1))
h = (0, 1)
c_h = tuple(sum(C_E[i][j]*h[j] for j in range(2)) for i in range(2))
assert c_h == (-1, -1) and c_h != h
frobenius_trace = 7+1-len(projective_points)
frobenius_det = 7
det_one_minus_frobenius = 1-frobenius_trace+frobenius_det
assert frobenius_trace == -1 and det_one_minus_frobenius == 9

output = {
    "status": "all exact finite checks passed",
    "Eisenstein_norms": {"lambda": norm(lam), "pi": norm(pi), "pibar": norm(pibar)},
    "pi_times_pibar": mul(pi, pibar),
    "residue_checks": residue_checks,
    "Frobenius_unit_matrix": unit_rows,
    "Frobenius_unit_determinant_mod3": det_mod(unit_rows),
    "full_matrix_upper_right_blocks_checked": 3**4,
    "full_matrix_determinants_mod3": sorted(determinants),
    "boundary_rank": 8,
    "rational_cusp_indices": rational_indices,
    "chosen_nonrational_cusp_index": P_index,
    "primitive_rank_two_boundary_pairs_checked": 36,
    "cubic_F7_points": len(projective_points),
    "all_F7_points_are_cusps": True,
    "B34_compact_vector": h,
    "B34_conjugate_vector": c_h,
    "Frobenius7_trace": frobenius_trace,
    "det_one_minus_Frobenius7": det_one_minus_frobenius,
    "scope": "Finite inputs only; B.29 contains the full cohomological pro-3 proof."
}
print(json.dumps(output, indent=2))
