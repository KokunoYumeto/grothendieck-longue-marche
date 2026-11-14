#!/usr/bin/env python3
"""E.55: integral mixed Kummer section coordinates and their actual equations.

All polynomial arithmetic below is exact over Z or Q.  We set T=X^2;
X=T^(1/2) is an integral change of formal coordinate over Z_3.
The calculation checks the arithmetic presentation in its Kummer image,
the integral divisions in the normal forms, independent recovery from
finite cyclic group rings, and every admissible residue condition below
400 for the three stated base primes and 49 mixed first coordinates.
The infinite arithmetic isomorphism is proved in the paper, using the
opened Wingberg theorem. No finite test is used in place of that proof.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json


def clean(p):
    return {i: a for i, a in p.items() if a}


def add(*ps):
    r = {}
    for p in ps:
        for i, a in p.items():
            r[i] = r.get(i, 0) + a
    return clean(r)


def scale(p, a):
    return clean({i: a*b for i, b in p.items()})


def shift(p, j):
    return {i+j: a for i, a in p.items()}


def mul(p, q):
    r = {}
    for i, a in p.items():
        for j, b in q.items():
            r[i+j] = r.get(i+j, 0) + a*b
    return clean(r)


def sub(p, q):
    return add(p, scale(q, -1))


def power(p, n):
    r = {0: 1}
    for _ in range(n):
        r = mul(r, p)
    return r


def psi(p, q):
    return {q*i: a for i, a in p.items()}


def inv(p):
    return {-i: a for i, a in p.items()}


def divide_binomial(p, a):
    """Exact Laurent division by X^a-1, including a nonzero remainder check."""
    assert a > 0
    if not p:
        return {}
    low = min(p)
    r = shift(p, -low)
    out = {}
    while r and max(r) >= a:
        k = max(r)
        z = r.pop(k)
        out[k-a] = out.get(k-a, 0) + z
        r[k-a] = r.get(k-a, 0) + z
        if not r[k-a]:
            del r[k-a]
    assert not r, (a, r)
    return shift(clean(out), low)


def series(p, n):
    out = [F(0) for _ in range(n)]
    for e, a in p.items():
        z = F(1)
        for j in range(n):
            out[j] += a*z
            z = z*F(e-j, j+1)
    return out


def quotient_series(p, d, n):
    pn, dn = series(p, n), series(d, n)
    assert dn[0] and dn[0].denominator == 1 and dn[0].numerator % 3
    out = []
    for j in range(n):
        out.append((pn[j]-sum(dn[i]*out[j-i] for i in range(1, j+1)))/dn[0])
    assert all(x.denominator % 3 for x in out)
    return out


def phi3(d):
    return 2*3**(d-1)


def canonical_u(s, eps, beta, zs):
    a = 3**s*eps
    p = {0: 3*beta}
    for d, z in enumerate(zs, 1):
        m = 3**d
        q = {2*eps*3**(s-d)*j: 1 for j in range(-(m-1)//2, (m-1)//2+1) if j % 3}
        assert len(q) == phi3(d) and inv(q) == q
        p = add(p, scale(sub(q, {0: phi3(d)}), z))
    return shift(p, a)


def numerator(u, a, q):
    sq = {2*i*a: 1 for i in range(q)}
    return sub(scale(psi(u, q), q), mul(sq, u))


def invariants(q, s):
    m = 3**s
    unseen = set(range(m))
    orbits = []
    while unseen:
        seed = min(unseen)
        orbit, frontier = set(), [seed]
        while frontier:
            x = frontier.pop()
            if x in orbit:
                continue
            orbit.add(x)
            frontier.extend(((q*x) % m, (-x) % m))
        unseen.difference_update(orbit)
        orbits.append(sorted(orbit))
    assert len(orbits) == s+1
    assert sorted(map(len, orbits)) == sorted([1]+[phi3(d) for d in range(1, s+1)])
    return orbits


def reduce_t(p, m):
    # X=T^(1/2), so exponent division by2 is done in the actual cyclic group.
    half = pow(2, -1, m)
    out = [0]*m
    for i, a in p.items():
        out[(i*half) % m] += a
    return out


def affine_mul(g, h):
    x, a, b = g
    y, c, d = h
    return x*y, a+x*c, b+x*d


def affine_inv(g):
    x, a, b = g
    return 1/x, -a/x, -b/x


def affine_conj(g, h):
    return affine_mul(affine_mul(g, h), affine_inv(g))


def primes(n):
    return [p for p in range(2, n) if all(p % d for d in range(2, int(p**0.5)+1))]


def v3(n):
    k = 0
    while n and n % 3 == 0:
        n //= 3
        k += 1
    return k


def multiplicative_order(x, p):
    z = 1
    for i in range(1, p):
        z = z*x % p
        if z == 1:
            return i
    raise AssertionError((x, p))


def primitive(p):
    return next(g for g in range(1, p) if multiplicative_order(g, p) == p-1)


def main():
    arithmetic = []
    for ell in (2, 5, 11, 23, 29):
        q = ell*ell
        assert v3(q-1) == 1
        t, sig, rho, c = [(F(x), F(a), F(b)) for x, a, b in ((1, 1, 0), (q, 0, 0), (1, 0, 1), (-1, 0, 0))]
        assert affine_conj(sig, t) == (F(1), F(q), F(0))
        assert affine_conj(c, t) == affine_inv(t)
        assert affine_conj(c, sig) == sig
        assert affine_conj(c, rho) == affine_inv(rho)
        # The anti-c word is evaluated without assuming its cyclotomic value is1.
        raw = (F(7), F(0), F(5))
        anti = affine_mul(affine_mul(affine_mul(raw, c), affine_inv(raw)), c)
        assert anti == (F(1), F(0), F(10))
        arithmetic.append({'ell': ell, 'q': q, 'cyclotomic_Frattini_coordinate': (q-1)//3 % 3,
                           'tame_and_involution_relations': True})

    orbit_records = []
    for q in (4, 25, 121):
        for s in range(1, 6):
            os = invariants(q, s)
            orbit_records.append({'q': q, 's': s, 'orbit_sizes': list(map(len, os))})

    normal_records = []
    coeff_checks = 0
    V = {2: 1, -2: 1, 0: -2}
    for q, s, eps in [(q, s, eps) for q in (4, 25) for s in (1, 2, 3) for eps in (1, 2)]+[(121, 1, 1)]:
        a, m = 3**s*eps, 3**s
        for b in (-6, 0, 9):
            beta, beta3 = 2-s, s-3
            zs = [(-1)**d*(d+1) for d in range(s)]
            u0 = canonical_u(s, eps, beta, zs)
            w0 = shift(add({0: 3*beta3}, mul(V, add({0: 2}, scale(V, -1), power(V, 2)))), b)
            assert inv(u0) == shift(u0, -2*a)
            assert inv(w0) == shift(w0, -2*b)
            n0 = numerator(u0, a, q)
            p0 = divide_binomial(n0, a)
            den = {i*a: 1 for i in range(2*q)}
            assert mul({a: 1, 0: -1}, den) == {2*q*a: 1, 0: -1}
            assert mul({a: 1, 0: -1}, p0) == n0
            assert inv(n0) == shift(n0, -2*q*a)
            assert sum(p0.values()) == 0
            vs = quotient_series(p0, den, 18)
            coeff_checks += len(vs)

            gauge = {2: 3, -2: -3, 4: -2, -4: 2, 8: 1, -8: -1}
            ra = {2*a: 1, 0: -1}
            rb = clean({2*b: 1, 0: -1}) if b else {}
            u = add(u0, mul(ra, gauge))
            w = add(w0, mul(rb, gauge))
            dv = sub(scale(psi(gauge, q), q), gauge)
            assert sub(numerator(u, a, q), n0) == mul({2*q*a: 1, 0: -1}, dv)
            bar = reduce_t(u, m)
            assert all(bar[i] == bar[(q*i) % m] == bar[(-i) % m] for i in range(m))
            beta_got = sum(bar)//3
            zs_got = [bar[(eps*3**(s-d)) % m] for d in range(1, s+1)]
            assert beta_got == beta and zs_got == zs
            recovered_u = canonical_u(s, eps, beta_got, zs_got)
            recovered_gauge = divide_binomial(sub(u, recovered_u), 2*a)
            assert recovered_u == u0 and recovered_gauge == gauge
            assert inv(recovered_gauge) == scale(recovered_gauge, -1)
            assert sub(w, mul(rb, recovered_gauge)) == w0
            normal_records.append({'q': q, 's': s, 'eps': eps, 'B': b,
                                   'beta_ell': beta, 'beta_3': beta3, 'finite_coordinates': zs,
                                   'integral_denominator_at_one': sum(den.values()),
                                   'numerator_support': len(p0),
                                   'first_six_Frobenius_coefficients': [str(x) for x in vs[:6]],
                                   'recovery_and_relations': True})

    residue_records = []
    residue_checks = 0
    for ell in (2, 5, 11):
        for p in primes(400):
            if p in (ell, 3):
                continue
            g = primitive(p)
            logs = {}
            z = 1
            for i in range(p-1):
                logs[z] = i
                z = z*g % p
            h = v3(p-1)
            modulus = 3**h
            accepted = []
            for a in range(-3, 4):
                for b in range(-3, 4):
                    x = pow(ell % p, 3*a, p)*pow(3, 3*b, p) % p
                    order = multiplicative_order(x, p)
                    via_order = order % 3 != 0
                    via_residue = pow(x, (p-1)//modulus, p) == 1
                    k = 3*(a*logs[ell % p]+b*logs[3 % p])
                    via_log = k % modulus == 0
                    # Independent finite affine fixed point criterion at one level above h.
                    mm = 3**(h+1)
                    via_affine = any(((p-1)*j+k) % mm == 0 for j in range(mm))
                    assert via_order == via_residue == via_log == via_affine
                    residue_checks += 1
                    if via_order:
                        accepted.append([a, b])
            residue_records.append({'ell': ell, 'p': p, 'v3_p_minus_one': h,
                                    'primitive_root': g, 'logs': [logs[ell % p], logs[3 % p]],
                                    'accepted_mixed_coordinates': accepted})

    out = {'statement': 'E.55', 'arithmetic': arithmetic, 'orbits': orbit_records,
           'normal_forms': normal_records, 'integral_series_coefficients': coeff_checks,
           'residue_checks': residue_checks, 'residues': residue_records,
           'all_checks_passed': True}
    target = Path(__file__).with_suffix('.json')
    target.write_text(json.dumps(out, indent=2)+'\n')
    print('E.55 actual two-prime arithmetic and mixed Kummer coordinates')
    print('arithmetic Kummer and involution models', len(arithmetic))
    print('finite cyclic orbit systems', len(orbit_records))
    print('exact normal-form recoveries', len(normal_records))
    print('integral Frobenius series coefficients', coeff_checks)
    print('independent residue/order/log/affine checks', residue_checks)
    print('all_checks_passed true')
    print('certificate', target.name)


if __name__ == '__main__':
    main()
