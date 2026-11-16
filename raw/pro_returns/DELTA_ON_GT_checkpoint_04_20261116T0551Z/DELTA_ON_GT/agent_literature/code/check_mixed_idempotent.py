#!/usr/bin/env python3
"""Independent exact coefficient-ring checks for KM.5 / MD.4.

No profinite free-group word or GT lift is constructed.  The finite rings are
(Z/4)[C_(4*3^n)] and their two-variable analogues.  The pro-three factor is
embedded by its CRT idempotent exponent, so the order-four exponent component
is retained rather than accidentally discarded.
"""
from collections import defaultdict
from math import gcd
import json

MOD = 4


def clean(a):
    return {k: v % MOD for k, v in a.items() if v % MOD}


def add(a, b, scale=1):
    d = defaultdict(int, a)
    for k, v in b.items():
        d[k] += scale * v
    return clean(d)


def mul(a, b, n):
    d = defaultdict(int)
    for i, x in a.items():
        for j, y in b.items():
            k = tuple((u + v) % n for u, v in zip(i, j))
            d[k] += x * y
    return clean(d)


def scale(a, c):
    return clean({k: c * v for k, v in a.items()})


def push(a, matrix, n):
    """Substitution: row j is the exponent vector of old variable j."""
    d = defaultdict(int)
    for key, val in a.items():
        new = tuple(sum(key[j] * matrix[j][i] for j in range(len(key))) % n
                    for i in range(len(matrix[0])))
        d[new] += val
    return clean(d)


def evaluate_one(a, variable, n):
    matrix = [[int(i == j) for i in range(len(next(iter(a))) - 1)]
              for j in range(len(next(iter(a))) - 1)]
    matrix.insert(variable, [0] * (len(matrix)))
    return push(a, matrix, n)


def crt_prothree_exponent(m):
    # 0 in C4 and 1 in C_m.
    return next(k for k in range(0, 4*m, 4) if k % m == 1)


def idempotent(m):
    n = 4*m
    k = crt_prothree_exponent(m)
    e = defaultdict(int)
    for j in range(m // 3):
        e[((3*k*j) % n,)] += pow(m // 3, -1, MOD)
    for j in range(m):
        e[((k*j) % n,)] -= pow(m, -1, MOD)
    return clean(e)


def ring_case(m):
    n = 4*m
    one = {(0,): 1}
    one2 = {(0, 0): 1}
    e = idempotent(m)
    assert mul(e, e, n) == e
    gamma = add(one, e, -2)
    assert mul(gamma, gamma, n) == one
    assert push(gamma, [[-1]], n) == gamma
    assert push(gamma, [[2]], n) == gamma
    for u in range(n):
        if gcd(u, n) == 1:
            assert push(gamma, [[u]], n) == gamma
    # D is well-defined modulo 4 because n is divisible by 4.
    assert clean({key: key[0] * val for key, val in gamma.items()}) == {}

    gu = push(gamma, [[1, 0]], n)
    gv = push(gamma, [[0, 1]], n)
    guv = push(gamma, [[1, 1]], n)
    beta = mul(mul(gu, gv, n), guv, n)  # gamma^{-1}=gamma
    numerator = add(beta, one2, -1)
    assert push(beta, [[1], [0]], n) == one
    assert push(beta, [[0], [1]], n) == one
    assert push(beta, [[1], [-1]], n) == one
    assert push(beta, [[0, 1], [1, 0]], n) == beta
    assert push(beta, [[2, 0], [0, 2]], n) == beta
    for u in range(n):
        if gcd(u, n) == 1:
            assert push(beta, [[u, 0], [0, u]], n) == beta

    # Construct an inverse of U-1 on the nontrivial pro-three block.
    # With v=U^k, P=sum(j v^j)/m satisfies (v-1)P=1-H.
    k = crt_prothree_exponent(m)
    p = clean({((k*j) % n,): j * pow(m, -1, MOD) for j in range(m)})
    s = {(j,): 1 for j in range(k)}
    q = mul(p, s, n)
    qu = push(q, [[1, 0]], n)
    qv = push(q, [[0, 1]], n)
    a = mul(mul(numerator, qu, n), qv, n)
    divisor = {(1, 1): 1, (1, 0): 3, (0, 1): 3, (0, 0): 1}
    assert mul(divisor, a, n) == numerator
    assert push(a, [[1], [0]], n) == {}
    assert push(a, [[0], [1]], n) == {}
    assert push(a, [[0, 1], [1, 0]], n) == a

    # Exact coefficient form of the lambda-one metabelian three-cycle.
    # W=(UV)^-1: V^-1 A(W,U)+(UV)^-1 A(V,W)+A(U,V)=0.
    first = mul({(0, n-1): 1}, push(a, [[-1, -1], [1, 0]], n), n)
    second = mul({(n-1, n-1): 1}, push(a, [[0, 1], [-1, -1]], n), n)
    assert add(add(first, second), a) == {}
    second_other = push(a, [[0, 1], [-1, -1]], n)
    third_other = mul({(1, 0): 1}, a, n)
    assert add(add(first, second_other), third_other) == {}

    # At (omega,omega), reduction to (Z/4)[omega].
    def omega_value(poly, u, v):
        d = [0, 0, 0]
        for (i, j), coeff in poly.items():
            d[(u*i + v*j) % 3] += coeff
        return ((d[0]-d[2]) % 4, (d[1]-d[2]) % 4)

    assert omega_value(beta, 1, 1) == (3, 0)
    assert omega_value(a, 1, 0) == (0, 0)
    assert omega_value(a, 1, 1) == (2, 2)  # 2/(3*omega) modulo 4

    # B(-1,omega)=1.  The first variable contributes (-1)^i.
    e0 = e1 = 0
    for (i, j), coeff in beta.items():
        coeff *= (-1)**i
        if j % 3 == 0:
            e0 += coeff
        elif j % 3 == 1:
            e1 += coeff
        else:
            e0 -= coeff
            e1 -= coeff
    assert (e0 % 4, e1 % 4) == (1, 0)
    return {"three_power": m, "full_exponent_order": n,
            "idempotent_terms": len(e), "integral_A_terms": len(a),
            "diagonal_beta": [3, 0], "minus_one_beta": [1, 0],
            "order_three_Kummer_translation": [0, 0],
            "coefficient_two_Frobenius_substitution": "PASS",
            "all_checks": "PASS"}, gamma, beta, a


def main():
    results = []
    previous = None
    for m in (3, 9, 27):
        record, gamma, beta, a = ring_case(m)
        if previous:
            m0, g0, b0, a0 = previous
            assert push(gamma, [[1]], 4*m0) == g0
            assert push(beta, [[1, 0], [0, 1]], 4*m0) == b0
            assert push(a, [[1, 0], [0, 1]], 4*m0) == a0
        previous = (m, gamma, beta, a)
        results.append(record)
    print(json.dumps({"scope": "coefficient-ring identities only; no GT lift",
                      "cases": results, "compatibility": "PASS"}, indent=2))


if __name__ == "__main__":
    main()
