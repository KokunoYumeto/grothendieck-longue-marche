#!/usr/bin/env python3
"""Finite algebra certificates for E.171--E.174.

These computations check the local finite-group identities used in the
proofs. They do not construct the Chebotarev/Poitou--Tate recursion and
do not certify an infinite or higher-depth section by finite sampling.
"""

from math import factorial, gcd, lcm


def primes(n):
    return [p for p in range(2, n + 1)
            if all(p % d for d in range(2, int(p ** 0.5) + 1))]


def valuation(n, p):
    assert n
    ans = 0
    while n % p == 0:
        n //= p
        ans += 1
    return ans


def crt_pair(a, m, b, n):
    assert gcd(m, n) == 1
    return (a + m * (((b - a) * pow(m, -1, n)) % n)) % (m * n)


def product_set(xs, ys, p):
    return {x * y % p for x in xs for y in ys}


ps = primes(500)
factorization_checks = 0
smallest_choices = None
for p in ps:
    if p < 7:
        continue
    good = set(range(2, p - 1))
    assert product_set(good, good, p) == set(range(1, p))
    for u in range(1, p):
        choices = [x for x in good if (u * pow(x, -1, p)) % p in good]
        assert choices
        smallest_choices = len(choices) if smallest_choices is None else min(smallest_choices, len(choices))
        for k in (6, 8, 10):
            x = choices[0]
            factors = [x, u * pow(x, -1, p) % p]
            factors += [2, pow(2, -1, p)] * ((k - 2) // 2)
            value = 1
            for f in factors:
                assert f in good
                value = value * f % p
            assert value == u and len(factors) == k
            factorization_checks += 1
print(f"Nonexceptional factorization: {factorization_checks} targets/counts checked for all primes 7<=p<=500; minimum initial choices={smallest_choices}.")

for p in (23, 41):
    squares = {x * x % p for x in range(1, p)}
    good_squares = squares - {1, p - 1}
    assert good_squares and 2 in good_squares
    for k in (6, 8, 10):
        factors = [2, pow(2, -1, p)] * (k // 2)
        value = 1
        for f in factors:
            assert f in good_squares
            value = value * f % p
        assert value == 1
    print(f"Private p={p}: square subgroup order={len(squares)}, allowed square count={len(good_squares)}; even inverse-pair targets verified.")

shells = []
for k in (6, 8, 10):
    assert pow(5, k, 8) == 1
    assert pow(2 * 3, k // 2, 5) == 1
    shells.append((k, pow(2, k, 9)))
assert {r for _, r in shells} == {1, 4, 7}
print(f"Even count shells (count, product mod9): {shells}; mod8 and mod5 targets equal1.")

a, modulus = 5, 8
for b, n in [(2, 9)] + [(2, p) for p in primes(43) if p >= 5]:
    a = crt_pair(a, modulus, b, n)
    modulus *= n
assert a % 8 == 5 and a % 9 == 2
for p in primes(43):
    if p >= 5:
        assert a % p not in (0, 1, p - 1)
assert pow(a, 11, 23) == 1 and pow(a, 20, 41) == 1
print(f"Simultaneous arithmetic CRT certificate: q={a} mod {modulus}; all active/treated primes 5..43 nonexceptional, private quadratic marks fixed.")
print("This is a residue certificate, not a prime or a higher-section Frobenius certificate.")

frame_checks = 0
for ell in primes(17):
    for q in primes(300):
        if ell == q:
            continue
        e = valuation(q * q - 1, ell)
        u = valuation(q - 1, ell)
        if not e:
            continue
        N = e + u
        modN = ell ** N
        generator = ell ** (N - u)
        for j in range(ell ** u):
            x = j * generator
            assert (q - 1) * x % modN == 0
            assert x % (ell ** e) == 0
            frame_checks += 1
print(f"Finite inertia/abelian-stabilizer precision: {frame_checks} annihilator values verified at N=e+u, ell<=17 and q<=300.")

dyadic = []
for q in (23, 41):
    dyadic.append((q, valuation(q - 1, 2), valuation(q * q - 1, 2), valuation(q * q - 1, 3)))
fresh = [q for q in primes(5000) if q % 8 == 5 and q % 9 == 2]
for q in fresh:
    assert valuation(q - 1, 2) == 2
    assert valuation(q * q - 1, 2) == 3
    assert valuation(q - 1, 3) == 0
    assert valuation(q * q - 1, 3) == 1
assert dyadic == [(23, 1, 4, 1), (41, 3, 4, 1)]
print(f"Private valuation table (q,v2(q-1),v2(q^2-1),v3(q^2-1)): {dyadic}; fresh shell checked at {len(fresh)} primes<5000.")

hall_checks = 0
for a0 in range(256):
    for b0 in range(256):
        for h0 in (0, 1):
            n = 512
            assert n * a0 % 256 == 0 and n * b0 % 256 == 0
            assert (n * h0 + n * (n - 1) // 2 * a0 * b0) % 256 == 0
            hall_checks += 1
assert (256 * 255 // 2) % 256 == 128
print(f"Hall quotient modulo256: {hall_checks} power checks certify exponent dividing512; an odd-odd peripheral has nonzero 256th-power central coordinate128.")

cyclic_checks = 0
for ell in (5, 7, 11, 13):
    for order in range(1, 513):
        ellpart = ell ** valuation(order, ell)
        J = order // ellpart
        L = valuation(order, ell)
        # In an additive cyclic group, x is an n-multiple iff gcd(n,order)|x.
        for x in range(order):
            if x % gcd(J, order) == 0 and x % gcd(ell ** L, order) == 0:
                assert x == 0
                cyclic_checks += 1
print(f"Relative local-unit annihilation: {cyclic_checks} intersections J*C intersect ell^L*C verified trivial for cyclic orders<=512 at ell=5,7,11,13.")

repair_rows = []
active = [p for p in primes(43) if p >= 5][:9]
for stage, ell in enumerate(active, 1):
    M = factorial(stage + 43)
    L = valuation(M, ell) + 2
    J = M // (ell ** valuation(M, ell))
    m = crt_pair(1, ell ** L, 0, J)
    if not m:
        m = ell ** L * J
    assert m > 0 and m % (ell ** L) == 1 and m % J == 0
    for r in (2, 3, 5, 7, 11, 13):
        if r != ell:
            assert valuation(m, r) >= valuation(M, r)
    repair_rows.append((stage, ell, [valuation(m, r) for r in (2, 3, 5, 7, 11, 13)]))
print("Once-per-coefficient CRT repair valuations (stage,active ell,[v2,v3,v5,v7,v11,v13]):")
for row in repair_rows:
    print(row)
print("Only the active coefficient can lose factorial divisibility at its single repair; all other retained coefficients keep it.")
print("ALL FINITE CERTIFICATES PASSED. Infinite existence uses the written E.152--E.174 proofs, not these tests.")
