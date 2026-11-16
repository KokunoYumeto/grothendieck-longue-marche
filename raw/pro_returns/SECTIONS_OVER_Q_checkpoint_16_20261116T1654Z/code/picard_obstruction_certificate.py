#!/usr/bin/env python3
"""Exact finite certificate for A.88's explicit divisor and coordinate-symbol obstruction.

The infinite Brauer/Picard comparison is proved in the accompanying text.
This code checks its rational data, finite divisor identities, and local
values; it does not approximate a Jacobian cohomology class numerically.
"""
from fractions import Fraction as Q
from itertools import product
from sympy import factorint


def square_vector(a):
    ans = {-1} if a < 0 else set()
    for z in (abs(a.numerator), a.denominator):
        for p, e in factorint(z).items():
            if e % 2:
                ans.symmetric_difference_update({int(p)})
    return frozenset(ans)


def v2_unit(a):
    n, d = a.numerator, a.denominator
    valuation = 0
    while n % 2 == 0:
        n //= 2
        valuation += 1
    while d % 2 == 0:
        d //= 2
        valuation -= 1
    return valuation, n * pow(d, -1, 8) % 8


def hilbert_two(a, b):
    va, ua = v2_unit(a)
    vb, ub = v2_unit(b)
    return (((ua - 1) // 2) * ((ub - 1) // 2)
            + va * ((ub * ub - 1) // 8)
            + vb * ((ua * ua - 1) // 8)) % 2


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def neg(x):
    return tuple(-a for a in x)


def sigma(x):
    return x[1], x[0], x[2]


def main():
    punctures = (Q(0), Q(1), Q(-9563, 59024))
    base, new = Q(1, 17), Q(-11, 68)
    coefficients = tuple(base - c for c in punctures)
    expected = (
        (Q(17, 16), Q(9563, 13035)),
        (Q(17), Q(68587, 13035)),
        (Q(-9563, 3472), Q(68587, 55552)),
    )
    boundary = tuple(tuple((c - d) / coefficients[j]
                           for j, d in enumerate(punctures) if i != j)
                     for i, c in enumerate(punctures))
    assert boundary == expected
    for row in boundary:
        v0, v1 = map(square_vector, row)
        span = {frozenset(), v0, v1, v0 ^ v1}
        assert frozenset({-1}) not in span
    assert 9563 == 73 * 131 and 68587 == 107 * 641
    assert 3472 == 2**4 * 7 * 31 and 55552 == 2**8 * 7 * 31
    print("All six exact boundary constants and all three no-minus-one squareclass tests passed.")

    fibre = tuple((new - c) / a for c, a in zip(punctures, coefficients))
    assert fibre == (Q(-11, 4), Q(79, 64), Q(1, 869))
    assert 4**4 * fibre[0] * fibre[1] * fibre[2] == -1
    degree = 4**3
    boundary_degree = degree // 4
    genus = 1 + degree // 2
    assert (degree, boundary_degree, genus) == (64, 16, 33)
    assert degree // 2 - 2 * boundary_degree == 0
    print("The primitive-eighth-root fibre identity and divisor degrees (32,32,16) passed.")

    # Coordinates are Z_+, Z_-, D_infinity.
    D = (1, 0, -2)
    div_f = (1, 1, -4)
    assert add(D, sigma(D)) == div_f
    identities = 0
    for g, h in product((0, 1), repeat=2):
        E_g = D if g else (0, 0, 0)
        E_h = D if h else (0, 0, 0)
        E_gh = D if g ^ h else (0, 0, 0)
        delta = add(add(sigma(E_h) if g else E_h, neg(E_gh)), E_g)
        assert delta == (div_f if g and h else (0, 0, 0))
        identities += 1
    # sigma(D)-D = -2D + div(f), giving the stated sign coboundary in Pic^0.
    assert add(sigma(D), neg(D)) == add(tuple(-2*a for a in D), div_f)
    print(f"Exact cyclic divisor-cochain identities: {identities}; sign coboundary passed.")

    precision = 128
    w = 0
    def H(w):
        return w + 6*w*w + 16*w**3 + 16*w**4
    for k in range(1, precision + 1):
        modulus = 2**k
        target = 217 * pow(869, -1, modulus) % modulus
        candidates = [v for v in (w, w + 2**(k-1)) if H(v) % modulus == target]
        assert len(candidates) == 1
        w = candidates[0]
    r = 1 + 4*w
    modulus = 2**(precision + 4)
    assert (pow(r, 4, modulus) * 869 - 4341) % modulus == 0
    assert r % 8 == 5
    point_t = Q(16, 17)
    assert ((point_t - new)/(base - new)) == 5
    assert (point_t - punctures[0])/coefficients[0] == 16
    assert (point_t - punctures[1])/coefficients[1] == Q(1, 16)
    assert (point_t - punctures[2])/coefficients[2] == Q(4341, 869)
    print(f"The chosen fourth root was lifted through {precision} exact binary steps.")
    print(f"Its residue modulo2^64 is {r % 2**64}; its unit squareclass is5.")

    for row in boundary[:2]:
        assert all(v2_unit(b)[0] % 2 == 0 and v2_unit(b)[1] == 1 for b in row)
    assert tuple(v2_unit(b) for b in boundary[2]) == ((-4, 5), (-8, 3))
    at_bad = (Q(2), Q(1, 2), Q(r))
    count = 0
    for bits in product((0, 1), repeat=6):
        value = 0
        for i, row in enumerate(boundary):
            for j, b in enumerate(row):
                value ^= bits[2*i+j] * hilbert_two(at_bad[i], b)
        assert value == 0
        count += 1
    assert hilbert_two(Q(1), Q(2)) == 0
    assert hilbert_two(Q(5), Q(2)) == 1
    print(f"All {count} allowed coordinate-character combinations evaluate equally at the two points.")
    print("The joint quaternion evaluations differ by invariant1/2.")

    norms = 0
    for k in range(1, 13):
        modulus = 2**k
        image = {(a*a + a - 1) % modulus for a in range(modulus)}
        assert image == set(range(1, modulus, 2))
        norms += modulus
    print(f"Literal unit-norm images a^2+a-1: {norms} inputs over twelve dyadic quotients.")
    print("All A.88 finite certificates passed.")


if __name__ == "__main__":
    main()
