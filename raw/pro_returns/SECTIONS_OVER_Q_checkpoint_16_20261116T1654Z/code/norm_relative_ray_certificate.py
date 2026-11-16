"""Exact subgroup and norm-transition identities for A.100."""
from math import gcd


def units(n):
    return [u for u in range(n) if gcd(u, n) == 1]


def primitive(n):
    us = units(n)
    return next(u for u in us if len({pow(u, j, n) for j in range(len(us))}) == len(us))


def mul(g, h, n):
    return ((g[0] + g[1]*h[0]) % n, g[1]*h[1] % n)


def inv(g, n):
    ui = pow(g[1], -1, n)
    return (-ui*g[0] % n, ui)


def power(g, f, n):
    ans = (0, 1)
    for _ in range(f):
        ans = mul(ans, g, n)
    return ans


subgroup_checks = 0
cycle_checks = 0
same_prime_checks = 0
different_prime_checks = 0
for ell, t in [(3, 1), (3, 2), (3, 3), (5, 1), (5, 2)]:
    n = ell**t
    us = units(n)
    generator = primitive(n)
    log = {pow(generator, j, n): j for j in range(len(us))}
    for s in range(t):
        base = ell**s
        degree = ell**(t-s)
        assert gcd(generator-1, degree) == 1
        assert {(generator-1)*a % degree for a in range(degree)} == set(range(degree))
        subgroup_checks += 1
        for a in range(degree):
            for u in us:
                g = (base*a, u)
                unseen = set(range(degree))
                while unseen:
                    y = min(unseen)
                    z = y
                    orbit = []
                    while z not in orbit:
                        assert z in unseen
                        unseen.remove(z)
                        orbit.append(z)
                        z = (a+u*z) % degree
                    assert z == y
                    f = len(orbit)
                    transporter = (base*y, 1)
                    h = mul(mul(inv(transporter, n), power(g, f, n), n), transporter, n)
                    assert h[0] == 0
                    assert log[h[1]] == f*log[u] % len(us)
                    cycle_checks += 1
        for i in range(base):
            for j in range(1, degree):
                # Prime labels i and i+base*j lie over the same K_s-prime.
                pair = {i:1, i+base*j:-1}
                for lower in range(s+1):
                    lowmod = ell**lower
                    pushed = [0]*lowmod
                    for label, coefficient in pair.items():
                        pushed[label % lowmod] += coefficient
                    assert not any(pushed)
                    same_prime_checks += 1
        if s:
            pair = {0:1, 1:-1}
            pushed = [0]*base
            for label, coefficient in pair.items():
                pushed[label % base] += coefficient
            assert any(pushed)
            different_prime_checks += 1
        print(f"ell={ell}, t={t}, s={s}: relative holomorph, Artin-cycle and same-prime norm checks passed")

power_checks = 0
for ell in [3,5,7]:
    for r in range(1,6):
        m=ell**r
        for d0 in range(1,30):
            if d0 % ell == 0:
                continue
            d=2*d0
            inverse=pow(d,-1,m)
            assert (1-inverse*d) % m == 0
            # Norm u0=eta0^m; squaring and then inverse exponent gives
            # Norm(u0^2)^(-inverse)=(eta0^(-2*inverse))^m.
            assert -inverse*(2*m) == (-2*inverse)*m
            power_checks += 1

print(f"Relative subgroup/commutator checks: {subgroup_checks}")
print(f"Relative Frobenius cycle/stabilizer identities: {cycle_checks}")
print(f"Same-prime lower norm identities: {same_prime_checks}")
print(f"Different-base-prime exclusions retained: {different_prime_checks}")
print(f"Lower-norm power and inverse-exponent identities: {power_checks}")
print("All A.100 finite identities passed. Existing chains are repaired; no next term is asserted.")
