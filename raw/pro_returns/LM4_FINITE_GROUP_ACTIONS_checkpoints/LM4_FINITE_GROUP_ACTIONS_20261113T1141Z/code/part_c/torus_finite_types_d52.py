#!/usr/bin/env python3
"""Exact finite identities used in D.52, without a realization inference."""
import itertools
import json
from pathlib import Path


I = ((1, 0), (0, 1))


def mm(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def mp(a, n):
    z = I
    for _ in range(n):
        z = mm(z, a)
    return z


def det(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def dihedral(n):
    elements = list(itertools.product(range(n), range(2)))

    def mul(x, y):
        return ((x[0] + (-1)**x[1] * y[0]) % n,
                (x[1] + y[1]) % 2)
    return elements, mul, (0, 0)


def power(x, n, mul, identity):
    z = identity
    for _ in range(n):
        z = mul(z, x)
    return z


def element_order(x, elements, mul, identity):
    z = identity
    for k in range(1, len(elements) + 1):
        z = mul(z, x)
        if z == identity:
            return k
    raise AssertionError("finite group power did not return to identity")


def check_isomorphism(source, smul, target, tmul, mapping):
    images = [mapping(x) for x in source]
    assert len(set(images)) == len(source) == len(target)
    assert set(images) == set(target)
    for x in source:
        for y in source:
            assert mapping(smul(x, y)) == tmul(mapping(x), mapping(y))
    return len(source)**2


def semidirect_three(qelts, qmul, qidentity, character):
    elts = [(a, q) for a in range(3) for q in qelts]

    def mul(x, y):
        a, q = x
        b, r = y
        return ((a + (-1)**character(q) * b) % 3, qmul(q, r))
    return elts, mul, (0, qidentity)


def main():
    r = ((0, -1), (1, 1))
    s = ((0, 1), (1, 0))
    assert mp(r, 6) == mp(s, 2) == I
    assert mm(s, mm(r, s)) == mp(r, 5)
    matrices = [mm(mp(r, i), mp(s, j))
                for i in range(6) for j in range(2)]
    assert len(set(matrices)) == 12
    assert all(det(mm(mp(r, i), mp(s, j))) == (-1)**j
               for i in range(6) for j in range(2))
    assert len({mm(mp(r, 2*i), mp(s, j))
                for i in range(3) for j in range(2)}) == 6

    zeta = ((0, -1), (1, -1))
    sigma = ((1, -1), (0, -1))
    assert mp(zeta, 3) == I
    assert mp(sigma, 2) == I
    assert mm(sigma, mm(zeta, sigma)) == mp(zeta, 2)
    assert det(sigma) == -1
    norm_checks = 0
    for a in range(-5, 6):
        for b in range(-5, 6):
            multiplication = ((a, -b), (b, a-b))
            norm = a*a - a*b + b*b
            assert det(multiplication) == norm
            semilinear = mm(multiplication, sigma)
            assert mm(semilinear, semilinear) == ((norm, 0), (0, norm))
            assert det(semilinear) == -norm
            square = mm(multiplication, multiplication)
            assert square == ((a*a-b*b, -b*(2*a-b)),
                              (b*(2*a-b), a*a-2*a*b))
            norm_checks += 1

    assert {a*a % 8 for a in range(1, 8, 2)} == {1}
    assert (-1) % 8 == 7
    assert pow(3, -1, 8) == 3
    three_unit_checks = []
    for u, v in itertools.product(range(9), repeat=2):
        if u % 3 == 0 and v % 3 == 0:
            continue
        norm = (u*u-u*v+v*v) % 9
        if (u+v) % 3:
            assert norm % 3 == 1
            valuation = 0
        else:
            assert norm == 3
            valuation = 1
        three_unit_checks.append((u, v, norm, valuation))
    assert len(three_unit_checks) == 72

    d8, d8mul, d8id = dihedral(4)
    automorphisms = set()
    for rotation_image in ((1, 0), (3, 0)):
        for reflection_image in ((j, 1) for j in range(4)):
            def f(x):
                return d8mul(power(rotation_image, x[0], d8mul, d8id),
                             power(reflection_image, x[1], d8mul, d8id))
            check_isomorphism(d8, d8mul, d8, d8mul, f)
            automorphisms.add(tuple(f(x) for x in d8))
    assert len(automorphisms) == 8

    # C3 semidirect V4, with the unique positive involution centralizing C3.
    v4 = list(itertools.product(range(2), repeat=2))
    def v4mul(x, y):
        return ((x[0]+y[0]) % 2, (x[1]+y[1]) % 2)
    g12, g12mul, _ = semidirect_three(v4, v4mul, (0, 0), lambda x: x[1])
    d12, d12mul, _ = dihedral(6)
    checks12 = check_isomorphism(
        d12, d12mul, g12, g12mul,
        lambda x: (x[0] % 3, (x[0] % 2, x[1]))
    )

    # C3 semidirect D8 by the reflection character is D24.
    g24, g24mul, _ = semidirect_three(d8, d8mul, d8id, lambda x: x[1])
    d24, d24mul, _ = dihedral(12)
    checks24 = check_isomorphism(
        d24, d24mul, g24, g24mul,
        lambda x: (x[0] % 3, (x[0] % 4, x[1]))
    )

    c4 = list(range(4))
    def c4mul(x, y):
        return (x+y) % 4
    cyclic12, cyclic12mul, cyclic12id = semidirect_three(
        c4, c4mul, 0, lambda x: 0)
    checks_c12 = check_isomorphism(
        list(range(12)), lambda x, y: (x+y) % 12,
        cyclic12, cyclic12mul, lambda x: (x % 3, x % 4)
    )
    dic12, dicmul, dicid = semidirect_three(
        c4, c4mul, 0, lambda x: x % 2)
    d, t = (1, 2), (0, 1)
    assert element_order(d, dic12, dicmul, dicid) == 6
    assert element_order(t, dic12, dicmul, dicid) == 4
    assert power(t, 2, dicmul, dicid) == power(d, 3, dicmul, dicid)
    assert dicmul(t, dicmul(d, power(t, 3, dicmul, dicid))) == power(
        d, 5, dicmul, dicid)
    assert len({dicmul(power(d, i, dicmul, dicid),
                       power(t, j, dicmul, dicid))
                for i in range(6) for j in range(2)}) == 12
    assert sum(element_order(x, dic12, dicmul, dicid) == 2
               for x in dic12) == 1

    result = {
        "claim": "D.52",
        "allowed_abstract_types": [
            "1", "C2", "C3", "C4", "V4", "C6", "S3", "D8",
            "C12", "D12", "Dic12", "D24"
        ],
        "realized_types": [
            "1", "C2", "C3", "C4", "V4", "C6", "S3", "D8", "D12"
        ],
        "occurrence_unresolved": ["C12", "Dic12", "D24"],
        "twelve_distinct_integral_torus_matrices": matrices,
        "normalizer_matrix_identities_checked": norm_checks,
        "three_adic_unit_residue_cases": len(three_unit_checks),
        "Aut_D8_size": len(automorphisms),
        "multiplication_pairs_checked_for_exact_isomorphisms": {
            "C3_semidirect_V4_to_D12": checks12,
            "C3_semidirect_D8_to_D24": checks24,
            "C3_times_C4_to_C12": checks_c12
        },
        "dicyclic_presentation_and_unique_involution": True,
        "scope": (
            "These are finite certificates for displayed maps and residue identities. "
            "The proof uses the exact A2 kernel 1 or C3 and faithfulness of A3 only "
            "on an actual C3. It does not infer occurrence of C12, Dic12, or D24, "
            "geometric conjugacy, or a global cyclic order-three/four multiplier."
        )
    }
    path = Path(__file__).with_name("torus_finite_types_d52_output.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
