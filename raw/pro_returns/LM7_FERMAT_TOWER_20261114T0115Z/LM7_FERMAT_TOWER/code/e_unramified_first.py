#!/usr/bin/env python3
"""Exact certificates for E.51; all arithmetic uses integers or Fractions.

Checks four unramified first-coordinate valuations, integral normal-form
recovery and arbitrary-input division, actual affine root-torsor orbits,
telescoping field factors, and local residue/norm transitions.
The all-level proofs and the actual arithmetic comparison are in E.51.
"""
from collections import deque
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
from random import Random
import json


def tidy(p):
    return {i: Q(c) for i, c in p.items() if c}


def plus(*polys):
    out = {}
    for p in polys:
        for i, c in p.items():
            out[i] = out.get(i, Q(0)) + c
    return tidy(out)


def scale(p, c):
    return tidy({i: c*x for i, x in p.items()})


def shift(p, a):
    return {i+a: c for i, c in p.items()}


def sub(p, q):
    return plus(p, scale(q, -1))


def subst(p, a):
    return {i*a: c for i, c in p.items()}


def times(p, q):
    out = {}
    for i, a in p.items():
        for j, b in q.items():
            out[i+j] = out.get(i+j, Q(0)) + a*b
    return tidy(out)


def C(p):
    return scale(subst(p, -1), -1)


def S(p, M):
    return scale(shift(subst(p, 7), M), 7)


def R(p, M):
    return shift(p, -2*M)


def D(p, M):
    return sub(S(p, M), p)


def divide_exact(p, d):
    """Laurent-polynomial division by T^d-1, with an exact check."""
    if not p:
        return {}
    lowest = min(p)
    work = shift(p, -lowest)
    result = {}
    while work and max(work) >= d:
        a = max(work)
        c = work[a]
        result[a-d] = result.get(a-d, Q(0)) + c
        work = sub(work, {a: c, a-d: -c})
    assert not work
    result = shift(tidy(result), lowest)
    assert times(result, {d: Q(1), 0: Q(-1)}) == p
    return result


W = {1: Q(1, 2), -1: Q(-1, 2)}
W2 = times(W, W)


def evaluate(coefficients, p):
    out = {}
    for c in reversed(coefficients):
        out = plus(times(out, p), {0: Q(c)})
    return out


def eta(M, i):
    return {0: Q(1), -i: Q(-1, 2), i-M: Q(-1, 2)}


def residues(p, M):
    out = [Q(0)]*M
    for i, c in p.items():
        out[i % M] += c
    return out


def finite_coordinates(u, M):
    coeff = residues(u, M)
    a = sum(u.values(), Q(0))
    z = [-(coeff[i]+coeff[M-i]) for i in range(1, (M+1)//2)]
    representative = {0: a}
    for i, zi in enumerate(z, 1):
        representative = plus(representative, scale(eta(M, i), zi))
    rem = sub(u, representative)
    rr = residues(rem, M)
    assert all(rr[i] == -rr[-i % M] for i in range(M))
    # The representative is the inversion-symmetric projection modulo T^M-1.
    ss = residues(representative, M)
    assert all(ss[i] == (coeff[i]+coeff[-i % M])/2 for i in range(M))
    return a, z, representative, rem


def recover_even_polynomial(p):
    work = dict(p)
    terms = {}
    while work:
        degree = max(work)
        assert degree >= 0 and degree % 2 == 0
        a = work[degree] * 2**degree
        terms[degree//2] = a
        work = sub(work, scale(evaluate([0]*(degree//2)+[1], W2), a))
    out = [terms.get(i, Q(0)) for i in range(max(terms, default=-1)+1)]
    assert evaluate(out, W2) == p
    return out


def polynomial_normal_form(u, M):
    a, z, base, ustar = finite_coordinates(u, M)
    numerator = sub(C(ustar), R(ustar, M))
    m = divide_exact(scale(shift(numerator, 2*M), -1), 2*M)
    assert C(m) == m
    v = sub(ustar, D(m, M))
    assert C(v) == R(v, M)
    f = recover_even_polynomial(divide_exact(scale(shift(v, 1-M), 2), 2))
    expected = plus(base, shift(times(W, evaluate(f, W2)), M))
    assert sub(u, D(m, M)) == expected
    return a, z, f, m


def trim(xs):
    xs = list(xs)
    while xs and xs[-1] == 0:
        xs.pop()
    return xs


rng = Random(510051)
normal_forms = []
for k in range(4):
    M = 3**(k+1)
    h = (M-1)//2
    for case in range(16):
        b3 = rng.randrange(-5, 6)
        z = [Q(rng.randrange(-4, 5)) for _ in range(h)]
        f = trim([Q(rng.randrange(-3, 4)) for _ in range(1+case % 4)])
        g = trim([Q(rng.randrange(-3, 4)) for _ in range(1+case % 3)])
        m = times(W, evaluate(g, W2))
        canonical = {0: Q(3*b3)}
        for i, zi in enumerate(z, 1):
            canonical = plus(canonical, scale(eta(M, i), zi))
        canonical = plus(canonical, shift(times(W, evaluate(f, W2)), M))
        u = plus(canonical, D(m, M))
        assert polynomial_normal_form(u, M) == (Q(3*b3), z, f, m)
        assert C(S(C(u), M)) == R(S(u, M), M)
        assert C(R(C(u), M)) == shift(u, 2*M)
        assert sub(C(D(m, M)), R(D(m, M), M)) == sub(R(m, M), m)
        normal_forms.append({'k': k, 'M': M, 'case': case,
                             'b3': b3, 'finite_compact_rank': h,
                             'z': [str(x) for x in z],
                             'f': [str(x) for x in f]})
print('PASS: 64 exact normal-form recoveries for M=3,9,27,81, including every finite coordinate.')

# Arbitrary Laurent inputs need division by the unit T^M+1.  Retain that
# denominator exactly, rather than assuming the quotient is a polynomial.
PREC = 16


def series_mul(a, b):
    out = [Q(0)]*PREC
    for i, ai in enumerate(a):
        if ai:
            for j in range(PREC-i):
                if b[j]:
                    out[i+j] += ai*b[j]
    return tuple(out)


def series_inv(a):
    assert a[0]
    out = [1/a[0]]+[Q(0)]*(PREC-1)
    for n in range(1, PREC):
        out[n] = -sum(a[i]*out[n-i] for i in range(1, n+1))/a[0]
    return tuple(out)


T_W = [Q(0)]*PREC
T_W[0] = Q(1)
T_W[1] = Q(1)
coefficient = Q(1)
for j in range(1, (PREC+1)//2):
    coefficient *= (Q(1, 2)-(j-1))/j
    T_W[2*j] = coefficient
T_W = tuple(T_W)
ONE = (Q(1),)+(Q(0),)*(PREC-1)


@lru_cache(None)
def T_power(a):
    if a == 0:
        return ONE
    if a < 0:
        return series_inv(T_power(-a))
    half = T_power(a//2)
    out = series_mul(half, half)
    return series_mul(out, T_W) if a % 2 else out


def substitute_T_W(p):
    out = [Q(0)]*PREC
    for exponent, c in p.items():
        term = T_power(exponent)
        for i in range(PREC):
            out[i] += c*term[i]
    return tuple(out)


arbitrary_inputs = []
for M in (3, 9, 27, 81):
    for case in range(4):
        u = tidy({i: Q(rng.randrange(-6, 7))
                  for i in rng.sample(range(-M-4, M+5), 9)})
        a0 = sum(u.values(), Q(0))
        u = plus(u, {0: 3*Q(case)-a0})
        a, z, base, ustar = finite_coordinates(u, M)
        numerator = sub(C(ustar), R(ustar, M))
        q = divide_exact(numerator, M)
        P = scale(shift(q, 2*M), -1)  # m=P/(T^M+1)
        A = {0: Q(1), M: Q(1)}
        A7 = {0: Q(1), 7*M: Q(1)}
        assert P == scale(shift(subst(P, -1), M), -1)
        B = times(A, A7)
        V = plus(times(ustar, B),
                 scale(shift(times(subst(P, 7), A), M), -7),
                 times(P, A7))
        assert V == scale(shift(subst(V, -1), 10*M), -1)
        m_series = series_mul(substitute_T_W(P), series_inv(substitute_T_W(A)))
        odd_series = series_mul(substitute_T_W(shift(V, -M)),
                                series_inv(substitute_T_W(B)))
        assert all(m_series[i] == 0 for i in range(0, PREC, 2))
        assert all(odd_series[i] == 0 for i in range(0, PREC, 2))
        assert all(x.denominator % 3 for x in m_series+odd_series)
        arbitrary_inputs.append({'M': M, 'case': case,
                                 'augmentation': str(a),
                                 'f_first_coefficients': [str(odd_series[i])
                                              for i in range(1, PREC, 2)],
                                 'exact_rational_involution_identity': True,
                                 'three_integral_coefficients_checked': 2*PREC})
print('PASS: 16 arbitrary inputs, exact unit-denominator division, involution identities, and integral W-series.')


def primes(bound):
    for p in range(2, bound):
        if all(p % d for d in range(2, int(p**0.5)+1)):
            yield p


def valuation3(a):
    assert a
    out = 0
    while a % 3 == 0:
        a //= 3
        out += 1
    return out


def order(a, p):
    if p == 2:
        return 1
    x = 1
    for d in range(1, p):
        x = (x*a) % p
        if x == 1:
            return d
    raise AssertionError('Invalid nonzero residue')


def primitive_and_log3(p):
    if p == 2:
        return 1, 0
    g = next(g for g in range(2, p) if order(g, p) == p-1)
    x = 1
    for d in range(p-1):
        if x == 3 % p:
            return g, d
        x = (x*g) % p
    raise AssertionError('Missing discrete logarithm')


def affine_orbits(p, b, n):
    mod = 3**n
    todo = set(range(mod))
    out = []
    while todo:
        start = min(todo)
        orbit = []
        x = start
        while x in todo:
            todo.remove(x)
            orbit.append(x)
            x = (p*x+b) % mod
        assert x == start
        out.append(orbit)
    return out


local_rows = []
norm_transition_count = 0
for p in primes(300):
    if p == 3:
        continue
    o = order(3 % p, p)
    g, log3 = primitive_and_log3(p)
    s = valuation3(p-1) if p > 2 else 0
    thresholds = []
    for k in range(4):
        M = 3**(k+1)
        b = M*log3
        eligible = valuation3(o) <= k+1
        assert eligible == (b % 3**s == 0)
        assert eligible == (order(pow(3, M, p), p) % 3 != 0)
        previous = None
        levels = []
        for n in range(1, 6):
            orbits = affine_orbits(p, b, n)
            if eligible:
                center = (-b//3**s * pow((p-1)//3**s, -1, 3**n)) % 3**n
                assert (p*center+b) % 3**n == center
                assert any(orbit == [center] for orbit in orbits)
            else:
                t = valuation3(b)
                assert t < s
                assert all(len(orbit) == 3**max(0, n-t) for orbit in orbits)
                center = None
            if previous is not None:
                lowmod = 3**(n-1)
                index = {x: orbit for orbit in previous for x in orbit}
                for orbit in orbits:
                    lower = index[orbit[0] % lowmod]
                    counts = {y: 0 for y in lower}
                    for x in orbit:
                        counts[x % lowmod] += 1
                    degree = len(orbit)//len(lower)
                    assert set(counts.values()) == {degree}
                    norm_transition_count += 1
            levels.append({'n': n, 'cycle_lengths': sorted(map(len, orbits)),
                           'fixed_chain_position': center})
            previous = orbits
        thresholds.append({'k': k, 'eligible': eligible, 'levels': levels})
    local_rows.append({'prime': p, 'order_of_3': o,
                       'v3_order_of_3': valuation3(o),
                       'primitive_root': g, 'discrete_log_3': log3,
                       'first_coordinate_cases': thresholds})
print('PASS: exact local criteria at', len(local_rows),
      'primes, four first-coordinate valuations, and', norm_transition_count,
      'ideal-norm positional transitions.')


def arithmetic_orbits(M, n):
    mod = 3**n
    remaining = set(range(mod))
    out = []
    while remaining:
        start = min(remaining)
        orbit = {start}
        queue = deque([start])
        while queue:
            x = queue.popleft()
            for y in ((7*x+M) % mod, (-x) % mod):
                if y not in orbit:
                    orbit.add(y)
                    queue.append(y)
        remaining.difference_update(orbit)
        out.append(orbit)
    return out


field_rows = []
for k in range(4):
    M = 3**(k+1)
    preceding = None
    for d in range(3):
        n = d+k+1
        factors = [{3**d: Q(1), 0: Q(-3)}]
        for j in range(1, k+2):
            a = 3**(d+j-1)
            b = 3**(j-1)
            factors.append({2*a: Q(1), a: Q(3**b), 0: Q(3**(2*b))})
        product = {0: Q(1)}
        for factor in factors:
            product = times(product, factor)
        assert product == {3**n: Q(1), 0: Q(-3**M)}
        orbits = arithmetic_orbits(M, n)
        degrees = [3**d]+[2*3**(d+j-1) for j in range(1, k+2)]
        assert sorted(map(len, orbits)) == sorted(degrees)
        roots = [0]+[3**(k+1-j) for j in range(1, k+2)]
        ordered = [next(o for o in orbits if x in o) for x in roots]
        assert [len(o) for o in ordered] == degrees
        if preceding is not None:
            for new, old in zip(ordered, preceding):
                lowmod = 3**(n-1)
                assert {x % lowmod for x in new} == old
                assert all(sum(x % lowmod == y for x in new) == 3 for y in old)
        field_rows.append({'k': k, 'd': d, 'n': n,
                            'polynomial_degree': 3**n,
                            'factor_degrees': degrees,
                            'actual_arithmetic_orbit_degrees': list(map(len, ordered)),
                            'root_positions': roots,
                            'vertical_field_degree': 3 if d else None})
        preceding = ordered
print('PASS: 12 exact field factorizations through degree729, actual arithmetic root orbits, and cubic tower transitions.')

new_examples = {}
for k in range(4):
    new_examples[str(k)] = [r['prime'] for r in local_rows
        if r['first_coordinate_cases'][k]['eligible']
        and (k == 0 or not r['first_coordinate_cases'][k-1]['eligible'])]
print('Newly permitted primes at each k below300:', new_examples)

payload = {'statement': 'E.51', 'status': 'PASS',
           'normal_forms': normal_forms,
           'arbitrary_input_checks': arbitrary_inputs,
           'local_prime_cases': local_rows,
           'ideal_norm_transition_count': norm_transition_count,
           'radical_field_factors_and_orbits': field_rows,
           'newly_permitted_primes_below300': new_examples,
           'scope': 'Exact finite certificates for the all-level proof of E.51; intrinsic lifts are not asserted.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(payload, indent=2)+'\n')
print('E.51 PASS')
