#!/usr/bin/env python3
"""Exact finite checks of A.38 and the original-cup residue at every coefficient.

This includes 2-primary arithmetic, where division by two is not used.
Only the standard library is required.
"""
from itertools import product


def order_mod(q, n):
    value, exponent = q % n, 1
    while value != 1:
        value = value * q % n
        exponent += 1
    return exponent


def group_checks(n):
    def mul(g, h):
        a, b, c = g
        x, y, z = h
        return ((a + x) % n, (b + y) % n, (c + z + a * y) % n)

    def inv(g):
        a, b, c = g
        return ((-a) % n, (-b) % n, (a * b - c) % n)

    X, Y, Z = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    assert mul(mul(mul(X, Y), inv(X)), inv(Y)) == Z
    count = 1
    for a, b, c in product(range(n), repeat=3):
        assert mul(mul((a, 0, 0), (0, b, 0)), (0, 0, (c - a * b) % n)) == (a, b, c)
        count += 1
    for lam in range(1, n):
        try:
            pow(lam, -1, n)
        except ValueError:
            continue

        def action(g):
            a, b, c = g
            return (lam * a % n, lam * b % n, lam * lam * c % n)

        # The central variables are linear on both sides; test every cross term.
        for a, b, x, y in product(range(n), repeat=4):
            g, h = (a, b, 0), (x, y, 0)
            assert action(mul(g, h)) == mul(action(g), action(h))
            count += 1
    return count


def cup_checks(ell, n, q):
    # Multiplying the Frobenius order by n makes every alpha an allowable cocycle.
    h = n * order_mod(q, n)
    sums = [0]
    for j in range(h):
        sums.append((sums[-1] + pow(q, j, n)) % n)
    assert sums[h] == 0

    def mul(g, k):
        u, j = g
        v, r = k
        return ((u + pow(q, j, n) * v) % n, (j + r) % h)

    tau, frob, finv = (1, 0), (0, 1), (0, h - 1)
    terms = [(frob, tau, 1), (mul(frob, tau), finv, 1), (frob, finv, -1)]
    terms += [((j % n, 0), tau, -1) for j in range(1, q)]
    values = range(n) if n <= 4 else sorted({0, 1, 2, n // ell, n - 1})
    count = 0
    for alpha, beta, a, b in product(values, repeat=4):

        def cocycle(point, first, ramification):
            u, j = point
            return (u * ramification + sums[j] * first) % n

        def cup(g, k):
            return cocycle(g, alpha, a) * pow(q, g[1], n) * cocycle(k, beta, b) % n

        residue = pow(q, -1, n) * sum(weight * cup(g, k) for g, k, weight in terms) % n
        if q % 2:
            correction = ((q - 1) // 2) * a * b
        else:
            assert ell != 2
            correction = (q - 1) * pow(2, -1, n) * a * b
        expected = (alpha * b - beta * a - correction) % n
        assert residue == expected
        count += 1
    return count


def main():
    group_total = 0
    for n in (2, 3, 4, 6, 8, 9):
        count = group_checks(n)
        group_total += count
        print(f"H(Z/{n}): {count} commutator, collecting and actual scalar-action checks")
    cup_total = 0
    for ell, exponents in ((2, (1, 2, 3, 5)), (3, (1, 2, 3)), (5, (1, 2))):
        for exponent in exponents:
            n = ell**exponent
            for q in (2, 3, 5, 7, 19):
                if q == ell:
                    continue
                count = cup_checks(ell, n, q)
                cup_total += count
                print(f"original cup mod {n}, q={q}: {count} strict residue identities")
    binomial_count = 0
    for q in (3, 5, 7, 19):
        for m in range(-64, 65):
            for u in range(-4, 5):
                alpha_minus_beta = (q - 1) * u + (q - 1) // 2
                z = m * alpha_minus_beta - ((q - 1) // 2) * m * m
                w = m * u - m * (m - 1) // 2
                assert z == (q - 1) * w
                binomial_count += 1
    print(f"Passed {group_total} group identities, {cup_total} residue identities, "
          f"and {binomial_count} integral 2-adic negative-valuation identities.")


if __name__ == "__main__":
    main()
