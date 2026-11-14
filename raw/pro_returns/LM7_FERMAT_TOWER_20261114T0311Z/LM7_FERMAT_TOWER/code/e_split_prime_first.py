#!/usr/bin/env python3
"""E.56 exact certificates: actual arithmetic choices and all coordinate maps.

Laurent polynomials use X=T^(1/D), with 3 not dividing D. Every division
is checked as an exact Laurent identity before its unit-denominator
power-series expansion. The proof, not these finite checks, covers all
three-adic exponents and all primes in the stated family.
"""
from fractions import Fraction as F
from math import gcd
from pathlib import Path
import itertools
import json


def clean(p):
    return {i: F(a) for i, a in p.items() if a}


def add(*ps):
    q = {}
    for p in ps:
        for i, a in p.items():
            q[i] = q.get(i, F(0))+a
    return clean(q)


def scale(p, c):
    return clean({i: c*a for i, a in p.items()})


def sub(p, q):
    return add(p, scale(q, -1))


def shift(p, n):
    return {i+n: a for i, a in p.items()}


def mul(p, q):
    ans = {}
    for i, a in p.items():
        for j, b in q.items():
            ans[i+j] = ans.get(i+j, F(0))+a*b
    return clean(ans)


def inv(p):
    return {-i: a for i, a in p.items()}


def psi(p, ell):
    return {ell*i: a for i, a in p.items()}


def aug(p):
    return sum(p.values(), F(0))


def power(p, n):
    q = {0: F(1)}
    for _ in range(n):
        q = mul(q, p)
    return q


def divide(p, a):
    """Exact Laurent division by X^a-1, including negative a."""
    assert a
    if a < 0:
        return scale(shift(divide(p, -a), -a), -1)
    if not p:
        return {}
    lo = min(p)
    r = shift(p, -lo)
    q = {}
    while r and max(r) >= a:
        i = max(r)
        c = r.pop(i)
        q[i-a] = q.get(i-a, F(0))+c
        r[i-a] = r.get(i-a, F(0))+c
        if not r[i-a]:
            del r[i-a]
    assert not r, (a, r)
    answer = shift(clean(q), lo)
    assert mul({a: F(1), 0: F(-1)}, answer) == p
    return answer


def series(p, n):
    q = [F(0)]*n
    for e, a in p.items():
        c = F(1)
        for j in range(n):
            q[j] += a*c
            c *= F(e-j, j+1)
    return q


def quotient_series(p, q, n):
    P, Q = series(p, n), series(q, n)
    assert Q[0] and Q[0].denominator % 3 and Q[0].numerator % 3
    out = []
    for j in range(n):
        out.append((P[j]-sum(Q[i]*out[j-i] for i in range(1, j+1)))/Q[0])
    assert all(a.denominator % 3 for a in out)
    return out


def v3(n):
    if not n:
        return 10**9
    n = abs(n)
    a = 0
    while n % 3 == 0:
        n //= 3
        a += 1
    return a


def primes(n):
    return [p for p in range(2, n)
            if all(p % j for j in range(2, int(p**.5)+1))]


def order(a, p):
    x = 1
    for j in range(1, p):
        x = x*a % p
        if x == 1:
            return j
    raise AssertionError((a, p))


def affine_mul(g, h):
    x, a, b = g
    y, c, d = h
    return x*y, a+x*c, b+x*d


def affine_inv(g):
    x, a, b = g
    return 1/x, -a/x, -b/x


def affine_conj(g, h):
    return affine_mul(affine_mul(g, h), affine_inv(g))


def orbit_sum(s, eps, d, sign, D):
    m = 3**d
    js = [j for j in range(-(m-1)//2, (m-1)//2+1) if j % 3 == sign % 3]
    assert len(js) == 3**(d-1)
    assert sum(js) == sign*3**(d-1)
    p = {D*eps*3**(s-d)*j: F(1) for j in js}
    assert sum(F(i, D)*a for i, a in p.items()) == F(sign*3**s*eps, 3)
    return p


def finite_orbits(ell, s):
    m = 3**s
    unseen = set(range(m))
    ans = []
    while unseen:
        x = min(unseen)
        cyc = []
        while x not in cyc:
            cyc.append(x)
            x = ell*x % m
        assert x == cyc[0]
        unseen.difference_update(cyc)
        ans.append(sorted(cyc))
    assert len(ans) == 1+2*s
    assert sorted(map(len, ans)) == sorted([1]+[3**(d-1) for d in range(1, s+1) for _ in range(2)])
    return ans


def bar(p, M, D):
    answer = [F(0)]*M
    Di = pow(D, -1, M)
    for i, a in p.items():
        answer[i*Di % M] += a
    return answer


def local_operator(p, ell, B, D):
    return sub(scale(shift(psi(p, ell), B*D), ell), p)


def main():
    arithmetic = []
    for ell in (7, 13, 31, 43, 79, 97):
        h = (ell-1)//3
        assert v3(ell-1) == 1 and pow(3, h, ell) != 1
        for t in (F(1), F(4), F(7), F(10), F(-2), F(-5)):
            sig = (F(ell), F(0), t)
            c = (F(-1), F(0), F(0))
            conjugate = affine_conj(c, sig)
            rho0 = affine_mul(conjugate, affine_inv(sig))
            assert rho0 == (F(1), F(0), -2*t)
            k = (1-t)/(2*t*(ell-1))
            assert k.denominator % 3
            g = (F(1), F(0), -2*t*k)
            normalized = affine_conj(g, sig)
            assert normalized == (F(ell), F(0), F(1))
            assert affine_conj(c, normalized) == (F(ell), F(0), F(-1))
            assert (-2*h) % 3
            arithmetic.append({"ell": ell, "old_t": str(t), "conjugating_exponent": str(k),
                               "normalized_t": 1, "Frattini_determinant_mod3": (-2*h) % 3})
    orbits = []
    for ell in (7, 13, 31):
        for s in range(1, 6):
            cs = finite_orbits(ell, s)
            orbits.append({"ell": ell, "s": s, "sizes": list(map(len, cs))})

    normals = []
    coeff_checks = 0
    for ell, s, eps, b in itertools.product((7, 13, 31), (1, 2, 3), (1, 2, -1), (-2, 0, 3)):
        A, B = 3**s*eps, 3*b
        h, r = F(ell-1, 3), F(B, ell-1)
        D = r.denominator
        assert D % 3
        M = 3**s
        beta, beta3 = F(s-2), F(3-s)
        eta = F(2-s)
        minus = [F((-1)**d*(d+2)) for d in range(s)]
        plus = [F(0)]+[F(d-3) for d in range(1, s)]
        plus[0] = 3*eta+sum(minus)-sum(plus[1:])
        assert sum(plus)-sum(minus) == 3*eta
        f0 = {0: 3*beta}
        for d in range(1, s+1):
            for sign, z in ((1, plus[d-1]), (-1, minus[d-1])):
                Q = orbit_sum(s, eps, d, sign, D)
                f0 = add(f0, scale(sub(Q, {0: F(3**(d-1))}), z))
        u0 = shift(f0, int(-r*D))
        R = {A*D: F(1), 0: F(-1)}
        S = {i*A*D: F(1) for i in range(ell)}
        numerator = sub(scale(shift(psi(u0, ell), B*D), ell), mul(S, u0))
        p0 = divide(numerator, A*D)
        assert mul(R, p0) == numerator
        assert mul(R, S) == {ell*A*D: F(1), 0: F(-1)}
        v0series = quotient_series(p0, S, 18)
        coeff_checks += len(v0series)
        expected_aug = (ell-1)*(eta-F(3, 2)*beta)
        assert v0series[0] == expected_aug
        assert expected_aug.denominator % 3 and expected_aug.numerator % 3 == 0
        V = {D: F(1), -D: F(1), 0: F(-2)}
        fV = add({0: F(2)}, scale(V, -1), power(V, 2))
        constant = beta3/h-eta+F(3, 2)*beta
        z_even = add({0: constant}, mul(V, fV))
        assert inv(z_even) == z_even
        odd = {D: F(3), -D: F(-3), 2*D: F(-2), -2*D: F(2)}
        assert inv(odd) == scale(odd, -1)
        u = add(u0, mul(R, add(z_even, odd)))
        # Exact relation for every gauge term, before any series truncation.
        original_num = sub(scale(shift(psi(u, ell), B*D), ell), mul(S, u))
        extra = local_operator(add(z_even, odd), ell, B, D)
        assert sub(original_num, numerator) == mul({ell*A*D: F(1), 0: F(-1)}, extra)
        assert expected_aug+aug(extra) == 3*beta3

        # Recover all orbit, lattice, toric, and even-series coordinates.
        finite = bar(shift(u, int(r*D)), M, D)
        assert all(finite[i] == finite[ell*i % M] for i in range(M))
        got_beta = sum(finite)/3
        got_plus = [finite[(eps*3**(s-d)) % M] for d in range(1, s+1)]
        got_minus = [finite[(-eps*3**(s-d)) % M] for d in range(1, s+1)]
        got_eta = (sum(got_plus)-sum(got_minus))/3
        assert (got_beta, got_plus, got_minus, got_eta) == (beta, plus, minus, eta)
        z = divide(sub(u, u0), A*D)
        recovered_even = scale(add(z, inv(z)), F(1, 2))
        recovered_odd = scale(sub(z, inv(z)), F(1, 2))
        assert recovered_even == z_even and recovered_odd == odd
        assert aug(u) == 3*beta
        assert sub(recovered_even, {0: constant}) == mul(V, fV)
        # Moving one finite orbit coordinate by1 violates the unique mod3
        # condition. Every further integral correction changes aug(v) by ell-1.
        bad_aug = expected_aug+h
        assert bad_aug.denominator % 3 and bad_aug.numerator % 3
        normals.append({"ell": ell, "s": s, "epsilon": eps, "b": b, "r": str(r), "D": D,
                        "beta_ell": str(beta), "beta_three": str(beta3),
                        "eta": str(eta), "plus": list(map(str, plus)),
                        "minus": list(map(str, minus)),
                        "Frobenius_augmentation_before_even_correction": str(expected_aug),
                        "constant_even_correction": str(constant),
                        "first_six_Frobenius_coefficients": list(map(str, v0series[:6])),
                        "all_exact_identities": True})

    residue_rows = []
    residue_count = 0
    for ell in (7, 13, 31):
        for p in primes(400):
            if p in (ell, 3):
                continue
            h = v3(p-1)
            mod = 3**h
            generator = next(g for g in range(1, p) if order(g, p) == p-1)
            logs = {pow(generator, j, p): j for j in range(p-1)}
            for a, b in itertools.product(range(-3, 4), repeat=2):
                element = pow(ell % p, 3*a, p)*pow(3, 3*b, p) % p
                criterion = pow(element, (p-1)//mod, p) == 1
                torsion_free = order(element, p) % 3 != 0
                log_value = 3*a*logs[ell % p]+3*b*logs[3 % p]
                log_condition = log_value % mod == 0
                # One affine fixed point condition in the actual 3-primary
                # residue quotient; p-1 is zero there.
                fixed = any(((p-1)*x+log_value) % mod == 0 for x in range(mod))
                assert criterion == torsion_free == log_condition == fixed
                residue_count += 1
            residue_rows.append({"ell": ell, "p": p, "three_primary_order": mod})
    result = {"statement": "E.56", "status": "PASS",
              "arithmetic_normalizations": arithmetic, "orbit_systems": orbits,
              "exact_normal_forms": normals, "integral_series_coefficients": coeff_checks,
              "residue_prime_rows": residue_rows, "four_way_residue_checks": residue_count}
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n")
    print(f"PASS {len(arithmetic)} actual Frobenius normalizations and Frattini determinants")
    print(f"PASS {len(orbits)} complete cyclic orbit systems")
    print(f"PASS {len(normals)} exact finite-lattice/gauge/toric coordinate recoveries")
    print(f"PASS {coeff_checks} integral Frobenius series coefficients")
    print(f"PASS {residue_count} four-way residue/order/log/affine criteria")
    print("E.56 PASS")


if __name__ == "__main__":
    main()
