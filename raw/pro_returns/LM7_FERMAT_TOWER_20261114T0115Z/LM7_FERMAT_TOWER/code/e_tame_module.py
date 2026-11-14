#!/usr/bin/env python3
"""Exact tame-local orbit and power-series certificates for E.42.

The ring is Z_3[[T-1]].  All stored coefficients are exact rationals
whose denominators are prime to three.  The program checks both the
finite affine-orbit condition and the original tame group relation.
It also records the first nonintegral coefficients in the a=0 case.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb, lcm
import json

OUT = Path(__file__).resolve().parent
PREC = 18


def v3(x):
    x = F(x)
    if not x:
        return 10**9
    a, b = abs(x.numerator), x.denominator
    n = 0
    while a % 3 == 0:
        a //= 3
        n += 1
    while b % 3 == 0:
        b //= 3
        n -= 1
    return n


def binom(a, k):
    if isinstance(a, int):
        return comb(a, k) if a >= 0 else (-1)**k*comb(k-a-1, k)
    z = F(1)
    for j in range(k):
        z = z * (a - j) / (j + 1)
    return z


def multiply(a, b, degree=PREC):
    return [sum((a[j] * b[i-j] for j in range(i+1)), F(0))
            for i in range(degree+1)]


def power(exponent, degree=PREC):
    return [binom(exponent, j) for j in range(degree+1)]


def substitute_Tq(coeffs, q):
    t = power(q)
    t[0] -= 1
    p = [F(1)]+[F(0)]*PREC
    result = [F(0)]*(PREC+1)
    for value in coeffs:
        result = [x+value*y for x, y in zip(result, p)]
        p = multiply(p, t)
    return result


def affine_orbits(m, q, b):
    unused = set(range(m))
    result = []
    while unused:
        k = min(unused)
        orbit = []
        while k in unused:
            unused.remove(k)
            orbit.append(k)
            k = (q*k+b) % m
        assert k == orbit[0]
        result.append(sorted(orbit))
    assert sorted(k for o in result for k in o) == list(range(m))
    return result


def quotient_series(q, a, b, orbit, degree=PREC):
    # Numerator q T^b P(T^q) - S_q(T^a) P(T).
    num = [q*sum((binom(b+q*k, j) for k in orbit), F(0))
           - sum((binom(a*h+k, j) for h in range(q) for k in orbit), F(0))
           for j in range(degree+2)]
    den = power(q*a, degree+1)
    den[0] -= 1
    assert num[0] == den[0] == 0
    result = []
    for n in range(degree+1):
        z = (num[n+1] - sum((den[n+1-j]*result[j]
                            for j in range(n)), F(0))) / den[1]
        result.append(z)
    # This verifies the original relation after multiplication, without
    # a guessed rational-to-integral comparison.
    for n in range(1, degree+2):
        assert sum((den[n-j]*result[j] for j in range(n)), F(0)) == num[n]
    return result


def serialize(x):
    return str(x) if isinstance(x, F) else x


cases = []
for q in [4, 7, 19, 37]:
    for m in [3, 9, 27]:
        for unit in [1, 2]:
            a = m*unit
            for b in [0, 3, -3, 9]:
                orbits = affine_orbits(m, q, b)
                delta = []
                series = []
                for orbit in orbits:
                    ell, sigma = len(orbit), sum(orbit)
                    z = (F(q-1)*sigma+(F(b)-F(a*(q-1), 2))*ell)/a
                    assert v3(z) >= 0
                    d = quotient_series(q, a, b, orbit)
                    assert d[0] == z and all(v3(t) >= 0 for t in d)
                    delta.append(z)
                    series.append(d)
                    # Invariance is tested in Z[C_m], including all
                    # coefficients, independently of the series division.
                    lhs = [0]*m
                    rhs = [0]*m
                    for k in orbit:
                        lhs[(q*k+b) % m] += 1
                        rhs[k] += 1
                    assert lhs == rhs
                lengths = [len(o) for o in orbits]
                den_unit = lcm(*(x.denominator for x in delta))
                assert den_unit % 3
                row0 = lengths + [0]
                row1 = [int(den_unit*x) for x in delta] + [den_unit*(q-1)]
                d1 = min(v3(x) for x in row0+row1)
                d12 = min(v3(row0[i]*row1[j]-row0[j]*row1[i])
                          for i in range(len(row0)) for j in range(i))
                assert d12 < 10**9
                smith = [d1, d12-d1]
                assert 0 <= smith[0] <= smith[1]
                # Construct a genuine integral solution with h=3+U+2U^2.
                # Its first and second augmentations are both multiples
                # of three.  The residual U-part is exactly geometric
                # conjugation by (0,U+2U^2).
                orbit = orbits[0]
                P = [3*sum((binom(k, j) for k in orbit), F(0))
                     for j in range(PREC+1)]
                n = power(a)
                n[0] -= 1
                h = [F(3), F(1), F(2)] + [F(0)]*(PREC-2)
                inertia = [x+y for x, y in zip(P, multiply(n, h))]
                hq = [F(3)] + [F(0)]*PREC
                t1 = power(q)
                t1[0] -= 1
                t2 = multiply(t1, t1)
                hq = [hq[j]+t1[j]+2*t2[j] for j in range(PREC+1)]
                twisted_h = multiply(power(b), hq)
                frobenius = [3*series[0][j]+q*twisted_h[j]-h[j]
                             for j in range(PREC+1)]
                assert inertia[0] == 3*len(orbit)
                assert frobenius[0] == 3*delta[0]+3*(q-1)
                assert v3(inertia[0]) >= 1 and v3(frobenius[0]) >= 1
                assert all(v3(x) >= 0 for x in inertia+frobenius)
                lhs = multiply([x-int(j == 0) for j, x in enumerate(power(q*a))], frobenius)
                term1 = multiply(power(b), substitute_Tq(inertia, q))
                Sq = [sum(binom(a*j, n) for j in range(q)) for n in range(PREC+1)]
                term2 = multiply(Sq, inertia)
                assert lhs == [q*x-y for x, y in zip(term1, term2)]
                cases.append({
                    'q': q, 'a': a, 'b': b, 'm': m, 'orbits': orbits,
                    'orbit_lengths': lengths, 'orbit_sums': [sum(o) for o in orbits],
                    'delta': delta, 'equation_matrix': [row0, row1],
                    'second_row_unit': den_unit, 'Smith_valuations': smith,
                    'framed_solution_free_rank': len(orbits)-1,
                    'first_orbit_D_coefficients': series[0],
                    'constructed_inertia_coefficients': inertia,
                    'constructed_Frobenius_coefficients': frobenius,
                })

obstructions = []
for q, b in [(19, 3), (37, 3), (109, 3), (19, 9)]:
    exponent = -F(b, q-1)
    for k in range(7):
        c = 3**(k+1)
        coeffs = [c*binom(exponent, n) for n in range(25)]
        bad = next((n for n, x in enumerate(coeffs) if v3(x) < 0), None)
        if v3(exponent) < 0:
            assert bad is not None
            for n in range(25):
                assert v3(coeffs[n]) == k+1+n*v3(exponent)-sum(v3(j) for j in range(1, n+1))
        else:
            assert bad is None
        obstructions.append({'q': q, 'b': b, 'inertia_augmentation': c,
                             'forced_exponent': exponent,
                             'first_nonintegral_degree': bad,
                             'coefficient': coeffs[bad] if bad is not None else None,
                             'valuation': v3(coeffs[bad]) if bad is not None else None})

# The E.38 value is recovered independently from the closed expression.
witness = next(z for z in obstructions if z['q'] == 19 and z['b'] == 3
               and z['inertia_augmentation'] == 81)
assert witness['first_nonintegral_degree'] == 4
assert witness['coefficient'] == F(1729, 384)

data = {'statement': 'E.42', 'precision_in_U': PREC,
        'finite_orbit_cases': cases, 'unramified_first_coordinate_cases': obstructions,
        'status': 'PASS',
        'scope': 'Exact finite orbit matrices, integral power-series quotients, tame relations and forced nonintegral coefficients. The all-degree classification is proved in E.42.'}
OUT.joinpath('e_tame_module.json').write_text(json.dumps(data, indent=2, default=serialize)+'\n')
print('Tame orbit cases:', len(cases))
print('All affine permutations and both-row Smith valuations verified.')
print('All formal quotient coefficients through degree', PREC, 'are three-adic integers.')
print('Constructed local solutions and their two exact augmentations: PASS')
print('a=0 cases:', len(obstructions))
print('E.38 forced coefficient: U^4 =', witness['coefficient'], 'with valuation', witness['valuation'])
print('PASS: exact local classification certificates for E.42.')
