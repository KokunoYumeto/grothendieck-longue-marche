#!/usr/bin/env python3
"""Exact linear algebra for the independent scan084 hypothesis test.

No manuscript, image, attachment, or context file is read.  The input is the
explicit scheme D={x0*x1*x2*x3=0} in P^3/F_q, and X=D x P^1.  The matrices are
the alternating restrictions among its projective-space strata.  This checks
the incidence ranks, not the general cohomological comparison theorems used
to interpret the result (explained in research_arithmetic.md).
"""

from fractions import Fraction
from itertools import combinations
import json


def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return 0
    row = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        scalar = a[row][col]
        a[row] = [x / scalar for x in a[row]]
        for i in range(len(a)):
            if i != row and a[i][col]:
                scalar = a[i][col]
                a[i] = [x - scalar * y for x, y in zip(a[i], a[row])]
        row += 1
        if row == len(a):
            break
    return row


def coboundary(source, target):
    matrix = []
    for simplex in target:
        faces = {simplex[:i] + simplex[i + 1:]: (-1)**i
                 for i in range(len(simplex))}
        matrix.append([faces.get(face, 0) for face in source])
    return matrix


def main():
    strata = [list(combinations(range(4), r)) for r in (1, 2, 3)]
    d0, d1 = (coboundary(strata[i], strata[i + 1]) for i in (0, 1))
    assert all(sum(d1[i][j] * d0[j][k] for j in range(6)) == 0
               for i in range(4) for k in range(4))
    r0, r1 = rank(d0), rank(d1)
    assert (r0, r1) == (3, 3)
    # E_1^{a,b}: a = component-complex degree; b = stratum cohomology.
    rows = {
        0: {"dimensions": [4, 6, 4], "ranks": [r0, r1]},
        2: {"dimensions": [4, 6, 0], "ranks": [r0, 0]},
        4: {"dimensions": [4, 0, 0], "ranks": [0, 0]},
    }
    geometric = {}
    for b, row in rows.items():
        dims, ranks = row["dimensions"], row["ranks"]
        e2 = [dims[a] - (ranks[a - 1] if a else 0)
              - (ranks[a] if a < 2 else 0) for a in range(3)]
        row["E2_dimensions"] = e2
        for a, dimension in enumerate(e2):
            if dimension:
                geometric.setdefault(a + b, {})[b // 2] = dimension
    # Eigenvalue q^e is labelled e.  P^1 contributes 1 in degree0 and q
    # in degree2, while the single Tate twist divides eigenvalues by q.
    product_twisted = {}
    for degree, eigenspaces in geometric.items():
        for exponent, dimension in eigenspaces.items():
            for projective_degree, projective_exponent in ((0, 0), (2, 1)):
                target = product_twisted.setdefault(degree + projective_degree, {})
                e = exponent + projective_exponent - 1
                target[e] = target.get(e, 0) + dimension
    invariant4 = product_twisted[4].get(0, 0)
    coinvariant3 = product_twisted[3].get(0, 0)
    assert invariant4 == 1 and coinvariant3 == 3
    print(json.dumps({
        "scheme": "D=union of four coordinate planes in P3/Fq; X=D x P1; ell!=p",
        "d0": d0,
        "d1": d1,
        "rows": rows,
        "H_Dbar_eigenvalue_q_exponent_multiplicities": geometric,
        "H4_D_Qell1_dimension_by_Hochschild_Serre": (
            geometric.get(3, {}).get(1, 0) + geometric.get(4, {}).get(1, 0)
        ),
        "H_Xbar_Qell1_eigenvalue_q_exponent_multiplicities": product_twisted,
        "H4_Xbar_Qell1_Frobenius_invariant_dimension": invariant4,
        "H3_Xbar_Qell1_Frobenius_coinvariant_dimension": coinvariant3,
        "H4_X_Qell1_dimension_by_Hochschild_Serre": invariant4 + coinvariant3,
        "scope": "Arithmetic interpretation uses component resolution, projective-space cohomology, Kunneth and Hochschild-Serre; see research_arithmetic.md."
    }, indent=2) + "\n", end="")


if __name__ == "__main__":
    main()
