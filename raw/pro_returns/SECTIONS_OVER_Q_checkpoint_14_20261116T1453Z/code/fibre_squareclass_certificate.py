#!/usr/bin/env python3
"""Exact finite checks for A.80's stabilizer-generated squareclass criterion.

This enumerates the finite Galois presentation proved in A.57.  It does
not infer a general theorem from finite enumeration.  For every permitted
case it also constructs the actual fixed-root tuple used in A.80.
"""
from itertools import product
from math import gcd

from fibre_character_certificate import (
    admissible, gamma_group, generated_subgroup,
)


def fixes_quadratic_field(g, weights, signs):
    u, eps = g
    return all((((u - 1) // 2) * delta
                + sum(w * e for w, e in zip(row, eps))) % 2 == 0
               for row, delta in zip(weights, signs))


def minus_one_in_span(weights, signs):
    for bits in product((0, 1), repeat=len(weights)):
        if sum(t * d for t, d in zip(bits, signs)) % 2 != 1:
            continue
        if all(sum(t * row[j] for t, row in zip(bits, weights)) % 2 == 0
               for j in range(len(weights[0]))):
            return True
    return False


def fixed_tuple(g, n, weights, signs):
    u, eps = g
    assert u % 4 == 3
    assert fixes_quadratic_field(g, weights, signs)
    d = gcd(n, u - 1)
    assert d % 4 == 2
    odd = d // 2
    k = tuple(next(a for a in range(n)
                   if a % 2 == e and a % odd == 0) for e in eps)
    roots = []
    for row, delta in zip(weights, signs):
        numerator = (u - 1) // 2 * delta + sum(w * a for w, a in zip(row, k))
        assert numerator % d == 0
        e = next(e for e in range(n)
                 if ((u - 1) * (delta + 2 * e)
                     + 2 * sum(w * a for w, a in zip(row, k))) % (2 * n) == 0)
        roots.append(e)
    return k, tuple(roots)


def main():
    cases = witnesses = 0
    excluded = 0
    for n in (4, 8, 12, 20, 24):
        for primes in ((2,), (3,), (5,), (2, 3), (3, 5)):
            gamma = gamma_group(n, primes)
            for seed in range(12):
                rows = tuple(tuple((seed + 2 * i + 3 * j) % 7 - 3
                                   for j in range(len(primes)))
                             for i in range(1 + seed % 3))
                signs = tuple((seed + i) % 2 for i in range(len(rows)))
                kernel = {g for g in gamma if fixes_quadratic_field(g, rows, signs)}
                in_span = minus_one_in_span(rows, signs)
                assert in_span == all(g[0] % 4 == 1 for g in kernel)
                if in_span:
                    excluded += 1
                    continue
                generators = {g for g in gamma if admissible(g, n, rows, signs)}
                subgroup = generated_subgroup(generators, n, len(primes))
                assert subgroup == kernel
                assert any(g[0] % 4 == 3 for g in kernel)
                for g in kernel:
                    if g[0] % 4 == 3:
                        fixed_tuple(g, n, rows, signs)
                        witnesses += 1
                cases += 1
    print(f"Squareclass criterion and exact generated-subgroup equality: {cases} cases.")
    print(f"Constructed actual root-stabilizer witnesses with u=3 mod4: {witnesses}.")
    print(f"Cases outside the stated squareclass hypothesis retained separately: {excluded}.")

    for n, primes, rows, signs in (
        (4, (5,), ((-1,), (-1,)), (0, 1)),
        (4, (5,), ((-2,),), (1,)),
    ):
        gamma = gamma_group(n, primes)
        kernel = {g for g in gamma if fixes_quadratic_field(g, rows, signs)}
        generators = {g for g in gamma if admissible(g, n, rows, signs)}
        subgroup = generated_subgroup(generators, n, len(primes))
        assert minus_one_in_span(rows, signs)
        assert subgroup < kernel
        print(f"Excluded example n={n}, rows={rows}, signs={signs}: "
              f"[K:Q]={len(gamma)//len(kernel)}, [B:Q]={len(gamma)//len(subgroup)}.")
    print("All A.80 finite certificates passed.")


if __name__ == '__main__':
    main()
