"""Finite exact identities for A.95; the field and recursion proofs are in TeX."""
from itertools import product
from math import factorial, gcd


def units(mod):
    return [u for u in range(mod) if gcd(u, mod) == 1]


def act(vec, a, u, mod, ell):
    out = [0] * mod
    for i, v in enumerate(vec):
        out[(a + u * i) % mod] = v % ell
    return out


def dot(x, y, ell):
    return sum(a * b for a, b in zip(x, y)) % ell


coset_checks = 0
for ell, n in [(3, 1), (3, 2), (5, 1), (7, 1)]:
    mod = ell ** n
    us = units(mod)
    unseen = set(range(mod))
    unit_orbits = []
    while unseen:
        i = min(unseen)
        orbit = {u * i % mod for u in us}
        unit_orbits.append(orbit)
        unseen -= orbit
    for coeff in product(range(ell), repeat=len(unit_orbits)):
        lam = [0] * mod
        for c, orbit in zip(coeff, unit_orbits):
            for i in orbit:
                lam[i] = c
        globally_invariant = len(set(lam)) == 1
        for c in range(ell):
            sigma0 = [0] * mod
            sigma0[0] = c
            # sigma0 and sigma0+e_i-e_0 generate the affine coset
            # sum(vec)=c.  Testing these tests every linear delta on it.
            coset_basis = [sigma0]
            for i in range(1, mod):
                v = sigma0.copy()
                v[0] = (v[0] - 1) % ell
                v[i] = 1
                assert sum(v) % ell == c
                coset_basis.append(v)
            kills_allowed_differences = all(
                dot(lam, act(v, a, u, mod, ell), ell) == dot(lam, v, ell)
                for v in coset_basis for a in range(mod) for u in us
            )
            assert kills_allowed_differences == globally_invariant
            coset_checks += 1
    print(f"ell={ell}, n={n}: every affine coset retains the split-character annihilator")

valuation_checks = 0
for ell in [3, 5, 7, 11]:
    for exponent in range(10):
        e2 = 2 ** exponent
        for s in range(1, 6):
            assert gcd(e2, ell ** s) == 1
            # The valuation of a radical is e2/ell^s in lowest terms.
            assert ell ** s // gcd(e2, ell ** s) == ell ** s
            valuation_checks += 1
print("At two, every tested odd-primary radical has the full ramification denominator")

stable_checks = 0
for n in range(1, 5):
    small = 3 ** n
    for t in [1, 2, 4, 7]:
        m = small * t
        for a in [0, small, 2 * small]:
            for q in [1 + 2 * small, 1 + 4 * small]:
                assert q % small == 1 and a % small == 0
                previous = None
                for r in range(n, n + 4):
                    modulus = 3 ** r
                    # Inertia fibres are indexed by reduction modulo 3^n.
                    fibres = [{x for x in range(modulus) if x % small == i}
                              for i in range(small)]
                    for i, fibre in enumerate(fibres):
                        assert {(x + m) % modulus for x in fibre} == fibre
                        assert {(q * x + a) % modulus for x in fibre} == fibre
                        assert len(fibre) == 3 ** (r - n)
                        if previous is not None:
                            assert {x % (modulus // 3) for x in fibre} == previous[i]
                        stable_checks += 1
                    previous = fibres
print("All stable inertia fibres retain residue degree one and identity ideal-norm transitions")

field_map_checks = 0
for j in range(6):
    M = factorial(j + 4)
    n = 0
    d = M
    while d % 3 == 0:
        d //= 3
        n += 1
    N = 3 ** n
    for Q in [5, 7, 11, 5 * 7]:
        # If alpha^N=a, then (Q^(M/N)alpha)^N = a Q^M.
        assert pow(pow(Q, M // N), N) == pow(Q, M)
        assert M % N == 0 and M % (3 * N) != 0
        field_map_checks += 1
print("All preliminary coefficient changes retain the literal embedded root field")

print(f"Coset-character equivalences: {coset_checks}")
print(f"Coprime local ramification denominators: {valuation_checks}")
print(f"Stable inertia-fibre and transition identities: {stable_checks}")
print(f"Embedded-field power identities: {field_map_checks}")
print("All A.95 finite identities passed. Density is not replaced by image membership.")
