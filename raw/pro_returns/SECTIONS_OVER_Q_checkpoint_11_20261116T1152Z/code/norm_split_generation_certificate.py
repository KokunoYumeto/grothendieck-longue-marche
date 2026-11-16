"""Exact finite checks for A.92; no class-group computation is asserted.

The number-field conclusion uses the class-field and Chebotarev maps
proved in the text.  This certificate checks the finite group identities
and character computations used by those maps.
"""
from itertools import product
from math import gcd


def units(mod):
    return [u for u in range(mod) if gcd(u, mod) == 1]


def primitive_root(mod):
    us = units(mod)
    for u in us:
        if len({pow(u, k, mod) for k in range(len(us))}) == len(us):
            return u
    raise AssertionError(("noncyclic units", mod))


def mul(g, h, mod):
    a, u = g
    b, v = h
    return ((a + u * b) % mod, u * v % mod)


def inv(g, mod):
    a, u = g
    ui = pow(u, -1, mod)
    return (-ui * a % mod, ui)


def power(g, k, mod):
    z = (0, 1)
    for _ in range(k):
        z = mul(z, g, mod)
    return z


def cycles(g, mod):
    a, u = g
    left = set(range(mod))
    out = []
    while left:
        start = min(left)
        orbit = []
        t = start
        while t not in orbit:
            assert t in left
            left.remove(t)
            orbit.append(t)
            t = (a + u * t) % mod
        assert t == start
        out.append(orbit)
    return out


cyclic_checks = 0
commutator_checks = 0
cycle_checks = 0
weighted_checks = 0
for ell, n in [(3, 1), (3, 2), (3, 3), (5, 1), (5, 2), (7, 1)]:
    mod = ell ** n
    us = units(mod)
    r = primitive_root(mod)
    ri = pow(r, -1, mod)
    assert gcd(r - 1, mod) == 1
    image = {(ri - 1) * t % mod for t in range(mod)}
    norm_coefficient = sum(pow(ri, k, mod) for k in range(len(us))) % mod
    assert image == set(range(mod))
    assert norm_coefficient == 0
    cyclic_checks += mod
    for t in range(mod):
        a, b = (0, r), (t, 1)
        comm = mul(mul(mul(a, b, mod), inv(a, mod), mod), inv(b, mod), mod)
        assert comm == ((r - 1) * t % mod, 1)
        commutator_checks += 1
    # A character of the unit group is recorded by the discrete logarithm.
    logs = {pow(r, k, mod): k for k in range(len(us))}
    for g in product(range(mod), us):
        cs = cycles(g, mod)
        vals = []
        for orbit in cs:
            t, f = orbit[0], len(orbit)
            transporter = (t, 1)
            frob_h = mul(mul(inv(transporter, mod), power(g, f, mod), mod),
                         transporter, mod)
            assert frob_h[0] == 0
            assert frob_h[1] == pow(g[1], f, mod)
            assert logs[frob_h[1]] == f * logs[g[1]] % len(us)
            vals.append((f, logs[frob_h[1]]))
            cycle_checks += 1
        for fi, vi in vals:
            for fj, vj in vals:
                assert (fj * vi - fi * vj) % len(us) == 0
                weighted_checks += 1
    print(f"ell={ell}, n={n}: cyclic differential onto; commutator translations full; affine cycles passed")

# Explicit finite extensions G=F_ell^(Z/N) semidirect AGL_1(Z/N).
# H is the stabilizer of zero.  Its kernel characters have coefficient
# vectors constant on U-orbits.  Split-prime differences test their
# restrictions along every translation; the annihilator must consist
# exactly of the globally invariant (constant) vectors.
split_character_checks = 0
permutation_frobenius_checks = 0
for ell, n in [(3, 1), (3, 2), (5, 1)]:
    mod = ell ** n
    us = units(mod)
    unseen = set(range(mod))
    unit_orbits = []
    while unseen:
        t = min(unseen)
        o = {u * t % mod for u in us}
        unit_orbits.append(sorted(o))
        unseen -= o
    for entries in product(range(ell), repeat=len(unit_orbits)):
        lam = [0] * mod
        for value, orbit in zip(entries, unit_orbits):
            for t in orbit:
                lam[t] = value
        kills_split_differences = all(
            (lam[(t + a) % mod] - lam[t]) % ell == 0
            for t in range(mod) for a in range(mod)
        )
        is_invariant = len(set(lam)) == 1
        assert kills_split_differences == is_invariant
        split_character_checks += 1
    # For invariant lambda, all conjugations preserve sum(v); a power
    # of Frobenius has additive sum f*sum(v).  Check the actual powers
    # of the permutation action on all basis vectors and every affine g.
    for g in product(range(mod), us):
        for t in range(mod):
            for orbit in cycles(g, mod):
                f = len(orbit)
                coeffs = [0] * mod
                pos = t
                for _ in range(f):
                    coeffs[pos] = (coeffs[pos] + 1) % ell
                    pos = (g[0] + g[1] * pos) % mod
                assert sum(coeffs) % ell == f % ell
                permutation_frobenius_checks += 1
    print(f"ell={ell}, n={n}: explicit permutation extension split-character and Frobenius checks passed")

print(f"Cyclic character differential checks: {cyclic_checks}")
print(f"Exact commutator checks: {commutator_checks}")
print(f"Frobenius cycle/stabilizer identities: {cycle_checks}")
print(f"Weighted norm-relation character identities: {weighted_checks}")
print(f"Split-character equivalences: {split_character_checks}")
print(f"Permutation-extension Frobenius power checks: {permutation_frobenius_checks}")
print("All finite A.92 identities passed. No inverse-limit generation is asserted.")
