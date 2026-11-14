#!/usr/bin/env python3
"""Exact finite-ring checks for E.13--E.14; no archived code is imported.

For every matrix in each Cartan coset and every translation vector modulo
ell**M, compute the exponent of the vector's class in coker(F-I).
This is independent of the Haar-law derivation: membership is tested by
forming the entire image of F-I as a set of pairs.
"""
from fractions import Fraction
from itertools import product
import json


def tail(q, n):
    return Fraction(q) ** (2 - n) / (q * q - 1)


def finite_tail(q, n, level):
    if n > level:
        return Fraction(0)
    return tail(q, n) * (1 - Fraction(q) ** (-2 * (level - n + 1)))


def mat_apply(matrix, vector, modulus):
    a, b, c, d = matrix
    x, y = vector
    return ((a * x + b * y) % modulus, (c * x + d * y) % modulus)


def matrices(ell, level, coset):
    modulus = ell**level
    if ell == 5:
        units = [a for a in range(modulus) if a % ell]
        for a, b in product(units, repeat=2):
            yield (a, 0, 0, b) if coset == "cartan" else (0, a, b, 0)
    else:
        # Z/3^M[i], with i^2=-1; multiplication followed, in the other
        # coset, by conjugation (x+iy)->(x-iy).
        for a, b in product(range(modulus), repeat=2):
            if (a * a + b * b) % ell == 0:
                continue
            yield (a, -b, b, a) if coset == "cartan" else (a, b, b, -a)


def enumerate_coset(ell, level, coset):
    modulus = ell**level
    vectors = list(product(range(modulus), repeat=2))
    counts = [0] * (level + 1)
    count_matrices = 0
    for f in matrices(ell, level, coset):
        count_matrices += 1
        d = (f[0] - 1, f[1], f[2], f[3] - 1)
        image = {mat_apply(d, v, modulus) for v in vectors}
        for x, y in vectors:
            order_exponent = 0
            while (x, y) not in image:
                order_exponent += 1
                x, y = ell * x % modulus, ell * y % modulus
            assert order_exponent <= level
            counts[order_exponent] += 1
    total = count_matrices * len(vectors)
    assert sum(counts) == total
    checks = []
    for n in range(1, level + 1):
        observed = Fraction(sum(counts[n:]), total)
        q = 9 if ell == 3 and coset == "cartan" else ell
        t = finite_tail(q, n, level)
        predicted = 2 * t - t * t if ell == 5 and coset == "cartan" else t
        assert observed == predicted, (ell, level, coset, n, observed, predicted)
        checks.append({"n": n, "tail_count": sum(counts[n:]),
                       "tail_exact": str(observed), "formula_exact": str(predicted)})
    return {"ell": ell, "level": level, "coset": coset,
            "matrices": count_matrices, "translations_per_matrix": len(vectors),
            "total_affine_elements": total, "mass_counts": counts,
            "tail_checks": checks}


def law(ell):
    rows = []
    for n in range(1, 9):
        if ell == 3:
            t = (tail(9, n) + tail(3, n)) / 2
            p = Fraction(9) ** (1 - n) / 20 + Fraction(3) ** (1 - n) / 8
            tn = (tail(9, n + 1) + tail(3, n + 1)) / 2
        else:
            a = tail(5, n)
            t = (3 * a - a * a) / 2
            p = Fraction(5) ** (1 - n) / 4 - Fraction(5) ** (2 - 2 * n) / 48
            b = tail(5, n + 1)
            tn = (3 * b - b * b) / 2
        assert p == t - tn
        rows.append({"n": n, "tail": str(t), "mass": str(p)})
    zero = 1 - Fraction(rows[0]["tail"])
    assert zero == (Fraction(121, 160) if ell == 3 else Fraction(817, 1152))
    return {"ell": ell, "zero_mass": str(zero), "positive_exponents": rows}


def special_fibre_check():
    points = [(x, y) for x in range(3) for y in range(3)
              if (y * y - x * x * x - x) % 3 == 0]
    assert len(points) + 1 == 4
    # x([3]P)=x-psi_2*psi_4/psi_3^2 in characteristic three.
    # psi_3=-1, psi_2=-y, psi_4=y*(x^6+2x^4+x^2+2).
    # Coefficients of x+(x^3+x)*(x^6+2x^4+x^2+2).
    coefficients = {1: 1}
    for i in (1, 3):
        for j, a in ((6, 1), (4, 2), (2, 1), (0, 2)):
            coefficients[i + j] = (coefficients.get(i + j, 0) + a) % 3
    coefficients = {i: a for i, a in coefficients.items() if a}
    assert coefficients == {9: 1}
    # At P=(2,1), duplication gives (0,0), so [3]P=-P.
    slope = pow(2, -1, 3)
    x2 = (slope**2 - 4) % 3
    y2 = (slope * (2 - x2) - 1) % 3
    assert (x2, y2) == (0, 0)
    return {"affine_points_F3": points, "total_points_F3": 4,
            "x_tripling_polynomial_mod3": coefficients,
            "double_of_2_1": [x2, y2],
            "conclusion": "[-3](x,y)=(x^9,y^9) on the special fibre"}


def main():
    results = {
        "purpose": "Exact finite affine-quotient certificate for E.13 and E.14",
        "scope": "Finite identities and counts; global image and density limits are proved in E_density.tex",
        "special_fibre": special_fibre_check(),
        "enumerations": [enumerate_coset(ell, level, coset)
                         for ell, levels in ((3, (1, 2, 3)), (5, (1, 2)))
                         for level in levels
                         for coset in ("cartan", "other")],
        "limiting_laws": [law(3), law(5)],
    }
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
