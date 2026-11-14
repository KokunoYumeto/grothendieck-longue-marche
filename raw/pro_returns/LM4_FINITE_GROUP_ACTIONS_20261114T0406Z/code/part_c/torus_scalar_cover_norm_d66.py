#!/usr/bin/env python3
"""Exact certificates for D.66; no automorphism-realization assertion.

The module calculations are over the integers.  Thus their reductions
hold at every primary precision, not merely at the small moduli tested.
"""

from __future__ import annotations

import json
from math import gcd, isqrt
from pathlib import Path


HERE = Path(__file__).resolve().parent
COUNTS = {
    "scalar_coordinate_cases": 0,
    "frobenius_section_labels": 0,
    "inverse_module_basis_vectors": 0,
    "deck_conjugacy_basis_vectors": 0,
    "deck_average_basis_vectors": 0,
    "integral_norm_preimages": 0,
    "integral_splitting_cocycle_pairs": 0,
    "primary_precision_unit_checks": 0,
    "handle_polynomial_checks": 0,
    "vector_coordinate_equalities": 0,
}


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def check_vector(a, b):
    assert a == b, (a, b)
    COUNTS["vector_coordinate_equalities"] += len(a)


def vadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def vscale(t, a):
    return tuple(t * x for x in a)


def matrix_mul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def matrix_add(a, b):
    return tuple(tuple(a[i][j] + b[i][j] for j in range(2))
                 for i in range(2))


def handle_check(d, p):
    identity = ((1, 0), (0, 1))
    zero = ((0, 0), (0, 0))
    h = ((0, -1), (1, -1 if d == 3 else 0))
    power = identity
    norm = zero
    for _ in range(d):
        norm = matrix_add(norm, power)
        power = matrix_mul(power, h)
    assert power == identity and norm == zero
    difference = tuple(tuple(h[i][j] - identity[i][j]
                             for j in range(2)) for i in range(2))
    determinant = (difference[0][0] * difference[1][1]
                   - difference[0][1] * difference[1][0])
    entry_gcd = 0
    for row in difference:
        for value in row:
            entry_gcd = gcd(entry_gcd, abs(value))
    assert determinant == p and entry_gcd == 1
    COUNTS["handle_polynomial_checks"] += 1
    return {"d": d, "p": p, "matrix": h, "norm": norm,
            "determinant_T_minus_I": determinant,
            "smith_invariants_T_minus_I": [1, p]}


def scalar_case(d, p, q, a):
    assert q % d == 1 and q != p
    assert pow(a, d, q) == 1
    assert all(pow(a, j, q) != 1 for j in range(1, d))
    a_inverse = pow(a, -1, q)
    dim = q - 1
    zero = (0,) * dim

    def boundary(i):
        i %= q
        if not i:
            return (-1,) * dim
        return tuple(int(j == i) for j in range(1, q))

    def action(v):
        return tuple(v[(a_inverse * j) % q - 1]
                     for j in range(1, q))

    def action_inverse(v):
        return tuple(v[(a * j) % q - 1] for j in range(1, q))

    def deck(v, shift):
        # Coordinates use b_1,...,b_(q-1), with b_0=-sum b_i.
        coordinates = (0,) + v
        origin_coefficient = coordinates[-shift % q]
        return tuple(coordinates[(j - shift) % q] - origin_coefficient
                     for j in range(1, q))

    def norm(v):
        answer = zero
        for _ in range(d):
            answer = vadd(answer, v)
            v = action(v)
        return answer

    unseen = set(range(1, q))
    orbits = []
    while unseen:
        representative = min(unseen)
        orbit = [representative * pow(a, j, q) % q for j in range(d)]
        assert len(set(orbit)) == d
        assert set(orbit) <= unseen
        unseen.difference_update(orbit)
        orbits.append(orbit)
    assert len(orbits) == (q - 1) // d
    labels = [i for orbit in orbits for i in orbit]
    label_position = {i: j for j, i in enumerate(labels)}
    assert set(labels) == set(range(1, q))

    def phi(v):
        return tuple(v[label_position[i]] for i in range(1, q))

    def psi(v):
        return tuple(v[i - 1] for i in labels)

    def free_action(v):
        answer = [0] * dim
        for start in range(0, dim, d):
            for j in range(d):
                answer[start + (j + 1) % d] = v[start + j]
        return tuple(answer)

    total = zero
    for i in range(q):
        total = vadd(total, boundary(i))
    check_vector(total, zero)
    check_vector(psi(boundary(0)), (-1,) * dim)
    check_vector(action(boundary(0)), boundary(0))

    for i in range(1, q):
        b = boundary(i)
        check_vector(phi(psi(b)), b)
        e = tuple(int(j == i - 1) for j in range(dim))
        check_vector(psi(phi(e)), e)
        check_vector(phi(free_action(psi(b))), action(b))
        COUNTS["inverse_module_basis_vectors"] += 1

        check_vector(action(deck(action_inverse(b), 1)), deck(b, a))
        check_vector(deck(b, q), b)
        COUNTS["deck_conjugacy_basis_vectors"] += 1
        average_numerator = zero
        for shift in range(q):
            average_numerator = vadd(average_numerator, deck(b, shift))
        check_vector(average_numerator, zero)
        COUNTS["deck_average_basis_vectors"] += 1

    w = zero
    for orbit in orbits:
        w = vadd(w, vscale(-1, boundary(orbit[0])))
    check_vector(norm(w), boundary(0))
    COUNTS["integral_norm_preimages"] += 1

    # The exact factor-set identity verifies the two extension maps for
    # every pair of kernel vectors, since those maps are affine-linear.
    partial = [zero]
    running = zero
    current = w
    for _ in range(d):
        running = vadd(running, current)
        partial.append(running)
        current = action(current)
    check_vector(partial[d], boundary(0))
    for j in range(d):
        for k in range(d):
            shifted = partial[k]
            for _ in range(j):
                shifted = action(shifted)
            left = vadd(partial[j], shifted)
            right = vadd(partial[(j + k) % d],
                         vscale((j + k) // d, boundary(0)))
            check_vector(left, right)
            COUNTS["integral_splitting_cocycle_pairs"] += 1

    # Q=Cq semidirect Cd, with the exact quotient label retained.
    def multiply(x, y):
        return ((x[0] + pow(a, x[1], q) * y[0]) % q,
                (x[1] + y[1]) % d)

    def power(x, n):
        answer = (0, 0)
        for _ in range(n):
            answer = multiply(answer, x)
        return answer

    for j in range(q):
        s_image = (j, 1)
        assert power(s_image, d) == (0, 0)
        k = j * pow(a - 1, -1, q) % q
        conjugated = multiply(multiply((k, 0), s_image), (-k % q, 0))
        assert conjugated == (0, 1)
        COUNTS["frobenius_section_labels"] += 1

    for exponent in range(1, 5):
        modulus = p**exponent
        # Every unit at these precisions is checked; the integral identity
        # above, rather than this enumeration, proves all precisions.
        for kappa in range(1, modulus):
            if kappa % p:
                correction = vscale(-kappa, w)
                equation = vadd(norm(correction),
                                vscale(kappa, boundary(0)))
                assert all(value % modulus == 0 for value in equation)
                COUNTS["primary_precision_unit_checks"] += 1

    # Cover labels: q degree-one boundaries and Euler characteristic -q.
    genus = (2 - q + q) // 2
    assert genus == 1
    COUNTS["scalar_coordinate_cases"] += 1
    return {
        "d": d, "p": p, "q": q, "deck_scalar": a,
        "cover_degree": q, "cover_type": [1, q],
        "boundary_orbits": orbits, "free_cyclic_module_rank": len(orbits),
        "norm_preimage_nonzero_coordinates": {
            str(i): w[i - 1] for i in range(1, q) if w[i - 1]},
        "norm_image": "b_0=-sum_{i=1}^{q-1} b_i",
        "primary_abelianized_extension_splits": True,
        "full_action_realization_asserted": False,
    }


def main():
    handles = [handle_check(3, 3), handle_check(4, 2)]
    cases = []
    for d, p in [(3, 3), (4, 2)]:
        for q in range(2, 98):
            if prime(q) and q % d == 1:
                for a in range(2, q):
                    if (pow(a, d, q) == 1
                            and all(pow(a, j, q) != 1 for j in range(1, d))):
                        cases.append(scalar_case(d, p, q, a))
    result = {
        "claim": "D.66", "status": "PASS", "counts": COUNTS,
        "handle_checks": handles, "cases": cases,
        "scope": "Exact quotient and integral module identities only; no scalar full action is constructed.",
    }
    output = HERE / "torus_scalar_cover_norm_d66_output.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"claim": "D.66", "status": "PASS", "counts": COUNTS,
                      "output": str(output)}, indent=2))


if __name__ == "__main__":
    main()
