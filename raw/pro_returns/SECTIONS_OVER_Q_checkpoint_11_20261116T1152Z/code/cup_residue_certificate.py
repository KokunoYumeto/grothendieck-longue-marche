#!/usr/bin/env python3
"""Exact finite certificates for the strict tame residue map of A.27.

We check the full linear functional on arbitrary one-cochains, not only
on selected cocycles, and separately check the alternating cup formula.
The infinite/coherent conclusion is proved in the TeX fragment.
"""
from collections import defaultdict
from itertools import product


def order_mod(q, n):
    r, k = q % n, 1
    while r != 1:
        r = r * q % n
        k += 1
    return k


def check(q, n):
    h = order_mod(q, n)

    def mul(g, k):
        u, j = g
        v, r = k
        return ((u + pow(q, j, n) * v) % n, (j + r) % h)

    identity, tau, frob = (0, 0), (1, 0), (0, 1 % h)
    finv = (0, (-1) % h)
    assert mul(mul(frob, tau), finv) == (q % n, 0)

    # A dictionary represents a linear functional on normalized cochains.
    def delta_terms(g, k, weight):
        answer = defaultdict(int)
        answer[k] += weight * pow(q, 2 * g[1], n)
        answer[mul(g, k)] -= weight
        answer[g] += weight
        answer.pop(identity, None)
        return answer

    linear = defaultdict(int)
    terms = [(frob, tau, 1), (mul(frob, tau), finv, 1), (frob, finv, -1)]
    terms += [((j % n, 0), tau, -1) for j in range(1, q)]
    for g, k, weight in terms:
        for point, value in delta_terms(g, k, weight).items():
            linear[point] += value
    qinv = pow(q, -1, n)
    linear = {g: (qinv * value) % n for g, value in linear.items()}
    linear[tau] = (linear.get(tau, 0) - (q - 1)) % n
    assert not {g: value for g, value in linear.items() if value}

    geometric_sums = [sum(pow(q, r, n) for r in range(j)) % n for j in range(h + 1)]
    alpha_values = [a for a in range(n) if geometric_sums[h] * a % n == 0]
    # Retain bounded, deterministic samples when the full residue ring is larger.
    if n > 9:
        alpha_values = sorted(set(alpha_values[:3] + alpha_values[-3:]))
        inertia_values = sorted({0, 1, 2, n // 3, n - 1})
    else:
        inertia_values = range(n)
    count = 0
    half = pow(2, -1, n)
    for alpha, beta, a, b in product(alpha_values, alpha_values, inertia_values, inertia_values):

        def cocycle(point, first, ramification):
            u, j = point
            return (u * ramification + geometric_sums[j] * first) % n

        def cup_alt(g, k):
            ag, bg = cocycle(g, alpha, a), cocycle(g, beta, b)
            ak, bk = cocycle(k, alpha, a), cocycle(k, beta, b)
            return (half * pow(q, g[1], n) * (ag * bk - bg * ak)) % n

        residue = qinv * sum(weight * cup_alt(g, k) for g, k, weight in terms) % n
        assert residue == (alpha * b - beta * a) % n
        count += 1
    return count


def main():
    total = 0
    for n in (3, 9, 27, 81):
        for q in (2, 5, 7, 19, 109):
            count = check(q, n)
            total += count
            print(f"mod {n}, q={q}: strict coboundary functional verified; {count} cup checks")
    print(f"Passed 20 entire one-cochain functional identities and {total} cup identities.")


if __name__ == "__main__":
    main()
