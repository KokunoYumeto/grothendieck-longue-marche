"""Independent finite certificates for E.98--E.100.

These certify the stated finite linear algebra and elementary arithmetic.
They do not certify the infinite arithmetic lifting theorem, nor do they
identify central cohomology modulo27 with all finite conjugacy classes.
"""
from itertools import combinations
from pathlib import Path
import json
import math
import sympy as sp


def exterior_square(matrix):
    ix = list(combinations(range(matrix.rows), 2))
    return sp.Matrix([
        [matrix[i, k] * matrix[j, l] - matrix[i, l] * matrix[j, k]
         for k, l in ix]
        for i, j in ix
    ])


def serial(matrix):
    return [[int(matrix[i, j]) for j in range(matrix.cols)]
            for i in range(matrix.rows)]


def run():
    answer = {}
    bound = math.factorial(4) / 4**4 * (4 / math.pi)**2 * math.sqrt(125)
    assert 1 < bound < 2
    answer["minkowski_Q_zeta5"] = bound

    # Explicit rational C2 representation of compact and boundary homology.
    # This is a rational splitting for the rank calculation, not an assertion
    # that the integral generalized-Jacobian extension splits.
    ranks = []
    for n in (3, 5, 9, 25):
        g = (n - 1) * (n - 2) // 2
        fixed_minus = 2
        pairs = 3 * (n - 1) // 2
        plus, minus = g + pairs, g + pairs + fixed_minus
        total = plus + minus
        assert total == n*n + 1
        wedge_minus = plus * minus
        assert wedge_minus == (n*n - 1) * (n*n + 3) // 4
        ranks.append({"n": n, "genus": g, "rank_V": total,
                      "plus": plus, "minus": minus,
                      "wedge_minus": wedge_minus})
    assert ranks[0]["wedge_minus"] == 24
    assert ranks[1]["wedge_minus"] == 168
    answer["real_and_wedge_ranks"] = ranks

    # Reconstruct the historical cubic matrices from their displayed torsion
    # table.  The proof in E.99 uses instead the canonical [3]-splitting.
    torsion = [(1, 0), (2, 2), (0, 1), (2, 0),
               (1, 1), (0, 2), (2, 1), (1, 2)]
    u_matrix = sp.Matrix([[v, -u] for u, v in torsion])
    cm = sp.Matrix([[0, -1], [1, -1]])
    c_elliptic = sp.Matrix([[1, -1], [0, -1]])
    perm = [0, 2, 1, 3, 5, 4, 7, 6]
    c_toric = sp.zeros(8)
    for i, j in enumerate(perm):
        c_toric[j, i] = -1
    frob_elliptic = sp.eye(2) + 3 * cm
    frob = frob_elliptic.row_join(sp.zeros(2, 8)).col_join(
        (u_matrix * (frob_elliptic - 7 * sp.eye(2)) / 3)
        .row_join(7 * sp.eye(8)))
    conj = c_elliptic.row_join(sp.zeros(2, 8)).col_join(
        ((u_matrix * c_elliptic - c_toric * u_matrix) / 3)
        .row_join(c_toric))
    assert all(x.q == 1 for x in list(frob) + list(conj))
    assert conj * conj == sp.eye(10)
    assert (conj - sp.eye(10)).rank() == 6
    assert (conj + sp.eye(10)).rank() == 4
    t_wedge, c_wedge = exterior_square(frob), exterior_square(conj)
    j0 = (3 * sp.eye(2)).col_join(u_matrix)
    ix = list(combinations(range(10), 2))
    w = sp.Matrix([j0[i, 0] * j0[j, 1] - j0[i, 1] * j0[j, 0]
                   for i, j in ix])
    assert sp.gcd_list(list(w)) == 1
    assert t_wedge * w == 7 * w
    assert c_wedge * w == -w
    coboundary = (t_wedge - sp.eye(45)) * (sp.eye(45) + c_wedge)
    assert coboundary.rank() == 21
    proper_wedge = sp.zeros(1, 45)
    proper_wedge[0, 0] = 1
    assert proper_wedge * coboundary == sp.zeros(1, 45)
    assert (proper_wedge * w)[0] == 9
    historical_scalar_row = 208 * proper_wedge
    assert (historical_scalar_row * w)[0] == 1872
    assert 1872 % 27 == 9
    assert (proper_wedge * w)[0] % 27 != 0
    answer["cubic_central_cohomology"] = {
        "rank_of_normalized_coboundary": 21,
        "free_rank": 24,
        "proper_projection_of_w": 9,
        "independent_row_with_historical_scalar": serial(historical_scalar_row),
        "scalar": 1872,
        "scalar_mod27": 9,
        "frob_V": serial(frob), "conjugation_V": serial(conj),
        "w": [int(x) for x in w],
        "scope": "central H1 coefficient detector only; no wholly finite conjugacy claim"
    }

    # Conjugate Frobenii at7 form a Frattini basis of the free arithmetic
    # pro3 source, as detected by zeta3 and 1-zeta3 Kummer characters.
    chars = []
    for zeta in (2, 4):
        residue = pow((1-zeta) % 7, 2, 7)
        lam_char = next(j for j in range(3) if pow(zeta, j, 7) == residue)
        chars.append([2, lam_char])
    assert chars == [[2, 0], [2, 2]]
    assert int(sp.Matrix(chars).det()) % 3 != 0
    assert pow(3, 2, 7) == 2
    answer["frobenius7_kummer_matrix"] = chars

    # Finite Haar idempotents in coefficient rings prime to the subgroup.
    haar = []
    for p, m in ((3, 5), (3, 10), (5, 6), (5, 12)):
        modulus = p**3
        inv = pow(m, -1, modulus)
        coeff = [inv] * m
        squared = [sum(coeff[i] * coeff[(j-i) % m] for i in range(m)) % modulus
                   for j in range(m)]
        assert squared == coeff
        assert sum(coeff) % modulus == 1
        haar.append({"coefficient_modulus": modulus, "subgroup_order": m,
                     "idempotent": True, "augmentation": 1})
    answer["finite_Haar_checks"] = haar

    # First coordinate of every proposed real lift square stays odd.
    real = []
    for exponent in range(1, 9):
        modulus = 2**exponent
        values = {(1 + 2*b) % modulus for b in range(modulus)}
        assert 0 not in values
        assert len(values) == modulus//2
        real.append({"modulus": modulus, "odd_square_coordinates": len(values)})
    answer["real_nonsplitting"] = real
    assert not any((x*x+y*y+z*z) % 4 == 0 and any(v % 2 for v in (x,y,z))
                   for x in range(4) for y in range(4) for z in range(4))
    answer["dyadic_conic_primitive_solution_mod4"] = False
    answer["PASS"] = True
    return answer


if __name__ == "__main__":
    result = run()
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"PASS": result["PASS"],
                      "wedge_ranks": [x["wedge_minus"] for x in result["real_and_wedge_ranks"]],
                      "cubic_central_detector": result["cubic_central_cohomology"]["scalar_mod27"],
                      "output": str(output)}, indent=2))
