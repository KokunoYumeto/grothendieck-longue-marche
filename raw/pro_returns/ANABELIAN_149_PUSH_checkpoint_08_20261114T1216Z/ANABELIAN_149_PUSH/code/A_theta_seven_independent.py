#!/usr/bin/env python3
"""Independent arithmetic checks for A.C2.13; no candidate-code imports.

F16 is built as the quadratic extension F4[beta]/(beta^2+beta+alpha),
and point counts enumerate y rather than using the trace criterion.
The integer endomorphism identities are checked on the companion matrix.
"""
from itertools import product
from pathlib import Path
import json

F4 = list(product(range(2), repeat=2))
Z4, O4, A4 = (0, 0), (1, 0), (0, 1)


def plus4(x, y):
    return (x[0] ^ y[0], x[1] ^ y[1])


def times4(x, y):
    # alpha^2 = alpha + 1.
    return (x[0]*y[0] ^ x[1]*y[1],
            x[0]*y[1] ^ x[1]*y[0] ^ x[1]*y[1])


F16 = list(product(F4, repeat=2))
Z16, O16 = (Z4, Z4), (O4, Z4)


def plus16(x, y):
    return (plus4(x[0], y[0]), plus4(x[1], y[1]))


def times16(x, y):
    bd = times4(x[1], y[1])
    return (plus4(times4(x[0], y[0]), times4(A4, bd)),
            plus4(plus4(times4(x[0], y[1]), times4(x[1], y[0])), bd))


def point_count(elements, zero, one, alpha, add, mul):
    inv = {x: next(y for y in elements if mul(x, y) == one)
           for x in elements if x != zero}
    alpha2 = mul(alpha, alpha)
    fibres = []
    for x in elements:
        if x in (zero, one):
            continue
        rhs = add(add(x, mul(alpha, inv[x])),
                  mul(alpha2, inv[add(x, one)]))
        solutions = [y for y in elements if add(mul(y, y), y) == rhs]
        assert len(solutions) in (0, 2)
        fibres.append({"x": x, "solutions": solutions})
    return 3 + sum(len(d["solutions"]) for d in fibres), fibres


def padd(a, b):
    return {i: plus4(a.get(i, Z4), b.get(i, Z4))
            for i in set(a) | set(b)
            if plus4(a.get(i, Z4), b.get(i, Z4)) != Z4}


def pmul(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            out[i+j] = plus4(out.get(i+j, Z4), times4(x, y))
    return {i: x for i, x in out.items() if x != Z4}


def ppow(a, n):
    out = {0: O4}
    for _ in range(n):
        out = pmul(out, a)
    return out


def madd(A, B):
    return [[x+y for x, y in zip(a, b)] for a, b in zip(A, B)]


def mscale(c, A):
    return [[c*x for x in row] for row in A]


def mmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(4))
             for j in range(4)] for i in range(4)]


I = [[int(i == j) for j in range(4)] for i in range(4)]
ZERO = [[0]*4 for _ in range(4)]


def mpow(A, n):
    out = I
    for _ in range(n):
        out = mmul(out, A)
    return out


def meval(coefficients, A):
    out = ZERO
    for c in reversed(coefficients):
        out = madd(mmul(out, A), mscale(c, I))
    return out


def main():
    alpha2 = times4(A4, A4)
    u = {1: O4, 2: O4}
    a = {0: alpha2, 1: O4}
    b = {0: alpha2, 2: O4}
    F = {0: A4, 1: O4, 2: O4, 3: O4}
    lhs = padd(pmul(u, padd(ppow(a, 2), pmul(a, b))),
               pmul(ppow(b, 2), padd(F, pmul({0: A4}, u))))
    assert lhs == ppow(a, 7)

    n4, fibres4 = point_count(F4, Z4, O4, A4, plus4, times4)
    n16, fibres16 = point_count(F16, Z16, O16, (A4, Z4), plus16, times16)
    assert (n4, n16) == (3, 15)
    beta = (Z4, O4)
    beta2 = times16(beta, beta)
    assert plus16(beta2, beta) == (A4, Z4)
    assert plus16(plus16(times16(beta2, beta2), beta), O16) == Z16

    trace1, trace2 = 5-n4, 17-n16
    e2 = (trace1*trace1-trace2)//2
    P = [16, -4*trace1, e2, -trace1, 1]
    assert P == [16, -8, 1, -2, 1]
    M = [[0, 0, 0, -16], [1, 0, 0, 8],
         [0, 1, 0, -1], [0, 0, 1, 2]]
    assert meval(P, M) == ZERO
    R = madd(mpow(M, 5), mscale(-1, I))
    assert R == meval([-33, 0, 6, 3], M)
    assert all(x % 3 == 0 for row in R for x in row)
    assert mmul(R, meval([856, 248, -57, -207], M)) == mscale(40344, I)
    assert 40344 == 3*13448 and 13448 % 3 == 2

    cycles = [{pow(2, j, 7) for j in range(3)},
              {3*pow(2, j, 7) % 7 for j in range(3)}]
    assert cycles == [{1, 2, 4}, {3, 5, 6}]
    assert {-i % 7 for i in cycles[0]} == cycles[1]
    result = {
        "status": "PASS",
        "field_implementation": "F4 pairs; F16 quadratic tower beta^2+beta=alpha",
        "count_method": "Enumerate every affine pair (x,y), plus three branch points",
        "point_counts": {"F4": n4, "F16": n16},
        "F4_fibres": fibres4,
        "F16_fibres": fibres16,
        "norm_polynomial_coefficients_as_F4_pairs": [lhs.get(i, Z4) for i in range(8)],
        "frobenius_polynomial_low_first": P,
        "companion_fifth_power_minus_identity": R,
        "annihilator_matrix_identity": "(M^5-I)(-207M^3-57M^2+248M+856I)=40344I",
        "three_primary_exponent_bound": 3,
        "doubling_cycles": [sorted(c) for c in cycles],
        "scope": "Arithmetic checks only; divisor, theta, covering, and A1 proofs are in the independent review."
    }
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "point_counts": [n4, n16],
                      "norm_identity": True, "endomorphism_identities": True,
                      "output": str(path)}, indent=2))


if __name__ == "__main__":
    main()
