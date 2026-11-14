"""Exact orbit certificates for the characteristic-two theta criterion.

These check the finite arithmetic used in A.C2.5--6.  The geometric
Frobenius formula and the dihedral argument are proved in the paper.
No external packages or numerical approximations are used.
"""
from math import gcd
import json


def doubling_orbits(n):
    remaining = set(range(1, n))
    result = []
    while remaining:
        start = min(remaining)
        orbit = []
        current = start
        while current not in orbit:
            orbit.append(current)
            remaining.remove(current)
            current = 2 * current % n
        assert current == start
        result.append(orbit)
    return result


def binary_rank(rows):
    pivots = {}
    for row in rows:
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def surviving_rank(n, zero_edges):
    """Rank of a sufficiently high power of the character permutation map."""
    columns = []
    for index in range(1, n):
        current = index
        alive = True
        for _ in range(n):
            if current in zero_edges:
                alive = False
                break
            current = 2 * current % n
        columns.append((1 << (current - 1)) if alive else 0)
    return binary_rank(columns)


checks = []


def check(name, condition, **detail):
    assert condition, name
    checks.append(dict(name=name, passed=True, **detail))


o13 = doubling_orbits(13)
check("thirteen has a single nonzero doubling orbit", len(o13) == 1,
      orbits=o13)
o7 = doubling_orbits(7)
check("seven has two doubling orbits exchanged by sign",
      len(o7) == 2 and set(o7[1]) == {-i % 7 for i in o7[0]},
      orbits=o7)
check("symmetric theta point kills both seven-character orbits",
      surviving_rank(7, {1, 6}) == 0)
o17 = doubling_orbits(17)
check("seventeen has a surviving orbit after one symmetric theta pair",
      surviving_rank(17, {1, 16}) == 8,
      orbits=o17)
o9 = doubling_orbits(9)
check("nine separates primitive and order-three characters",
      {tuple(sorted(o)) for o in o9} == {(1, 2, 4, 5, 7, 8), (3, 6)},
      orbits=o9)
check("primitive theta intersections do not kill the order-three block",
      surviving_rank(9, {1, 8}) == 2)

cases = 0
for n in range(3, 42, 2):
    orbits = doubling_orbits(n)
    samples = [set(), set(range(1, n)), {1, n - 1}]
    samples += [{i, n - i} for i in range(1, n)]
    for zero_edges in samples:
        predicted = sum(len(o) for o in orbits if set(o).isdisjoint(zero_edges))
        actual = surviving_rank(n, zero_edges)
        assert predicted == actual, (n, zero_edges, predicted, actual)
        cases += 1
check("exact stable-rank calculation agrees with all-orbit formula",
      cases > 400, cases=cases)

condition_primes = []
for ell in (3, 5, 7, 11, 13, 17, 19, 23, 31, 41, 43, 47):
    orbit = next(o for o in doubling_orbits(ell) if 1 in o)
    generated = set(orbit) | {-i % ell for i in orbit}
    if len(generated) == ell - 1:
        condition_primes.append(ell)
check("arithmetic criterion distinguishes useful small primes",
      condition_primes == [3, 5, 7, 11, 13, 19, 23, 47],
      accepted=condition_primes)

for n in range(3, 100, 2):
    assert gcd(2, n) == 1
    assert {2 * i % n for i in range(n)} == set(range(n))
check("product of the chosen reflections generates every odd deck group", True)

for n, expected in ((9, 3), (15, 1), (25, 5), (27, 3)):
    surviving = [i for o in doubling_orbits(n)
                 if set(o).isdisjoint({1, n - 1}) for i in o]
    common_divisor = n
    for i in surviving:
        common_divisor = gcd(common_divisor, i)
    kernel = [k for k in range(n)
              if all(i * k % n == 0 for i in surviving)]
    check(f"deck-kernel formula at cyclic degree {n}",
          len(kernel) == common_divisor == expected,
          surviving=surviving, kernel_powers=kernel)


def f8_multiply(a, b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        if a & 8:
            a ^= 0b1011  # alpha^3 + alpha + 1
        b >>= 1
    return result


orbit = [1]
for _ in range(6):
    orbit.append(f8_multiply(orbit[-1], 2))
check("a free seven-element orbit need only span three F2 dimensions",
      set(orbit) == set(range(1, 8))
      and f8_multiply(orbit[-1], 2) == 1
      and orbit[0] ^ orbit[1] ^ orbit[3] == 0
      and binary_rank(orbit) == 3,
      orbit=orbit, relation_indices=[0, 1, 3], dimension=3)

print(json.dumps({"checks": checks, "passed": len(checks),
                  "failed": 0}, indent=2))
