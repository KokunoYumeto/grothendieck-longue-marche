#!/usr/bin/env python3
"""Third, independent point and orbit audit of the large F4 certificate.

No search, C arithmetic, discrete-log normalization, HNF, or Jacobian code
is imported. Binary-field operations use shift/XOR. Doubling-orbit equality
is tested by the elementary compatibility criterion for simultaneous
congruences, after enumerating the tiny local doubling orbits.
"""
from pathlib import Path
from math import gcd, lcm, prod, isqrt
import json, hashlib, time

ROOT = Path(__file__).parent
SOURCE = ROOT / 'A_F4_large_theta_search.json'
MOD = (1 << 18) | (1 << 7) | 1
Q = 1 << 18
PRIMES = (7, 31, 2503, 4519)
M = prod(PRIMES)


def remainder(a, b):
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length() - b.bit_length())
    return a


def poly_gcd(a, b):
    while b:
        a, b = b, remainder(a, b)
    return a


def mul(a, b):
    c = 0
    while b:
        if b & 1:
            c ^= a
        a <<= 1
        if a & Q:
            a ^= MOD
        b >>= 1
    return c


def power(a, n):
    b = 1
    while n:
        if n & 1:
            b = mul(b, a)
        a = mul(a, a)
        n >>= 1
    return b


def local_orbits(p):
    assert all(p % n for n in range(2, isqrt(p) + 1))
    remaining = set(range(1, p))
    answer = {}
    lengths = set()
    while remaining:
        representative = min(remaining)
        x, exponent = representative, 0
        while x not in answer:
            answer[x] = (representative, exponent)
            remaining.remove(x)
            x = 2 * x % p
            exponent += 1
        assert x == representative
        lengths.add(exponent)
    assert len(lengths) == 1
    return answer, lengths.pop()


def main():
    start = time.time()
    data = json.loads(SOURCE.read_text())
    assert data['field_binary_modulus'] == MOD
    assert data['field_size'] == Q and data['odd_exponent'] == M
    # Rabin's irreducibility criterion over F2, with prime divisors 2,3 of 18.
    squares = {0: 2}
    for i in range(1, 19):
        squares[i] = mul(squares[i - 1], squares[i - 1])
    assert squares[18] == 2
    assert poly_gcd(squares[9] ^ 2, MOD) == 1
    assert poly_gcd(squares[6] ^ 2, MOD) == 1
    alpha = data['alpha']
    assert mul(alpha, alpha) ^ alpha == 1
    # Independent integer Newton recurrence for P4(X)=X4+2X3+X2+8X+16.
    trace = [4, -2, 2, -26, 2]
    for n in range(5, 19):
        trace.append(-2 * trace[n-1] - trace[n-2]
                     - 8 * trace[n-3] - 16 * trace[n-4])
    e2 = (trace[9] ** 2 - trace[18]) // 2
    order = 1 - trace[9] + e2 - Q * trace[9] + Q ** 2
    assert order == 4 * 7 * M == data['Jacobian_order']
    local = [local_orbits(p) for p in PRIMES]
    periods = [entry[1] for entry in local]
    period = lcm(*periods)
    orbit_count = prod(p - 1 for p in PRIMES) // period
    assert period == 1570005 and orbit_count == 1296
    packet = data['packets'][data['positive_direction']]
    assert len(packet) == orbit_count
    signatures = set()
    point_count = 0
    first_index = data['positive_theta_generator']['index']
    for witness in packet.values():
        j = witness['index_relative_to_theta_generator']
        assert gcd(j, M) == 1
        assert j * first_index % M == witness['index']
        coordinates = [entry[0][j % p] for p, entry in zip(PRIMES, local)]
        # j,j' lie in the same global orbit precisely when their local
        # representatives agree and the exponent-difference congruences
        # admit one common shift. General CRT says pairwise gcd agreement
        # is necessary and sufficient, including noncoprime periods.
        differences = tuple((coordinates[a][1] - coordinates[b][1])
                            % gcd(periods[a], periods[b])
                            for a in range(4) for b in range(a+1, 4))
        signature = tuple(t[0] for t in coordinates), differences
        assert signature not in signatures
        signatures.add(signature)
        x, y = witness['x'], witness['y']
        assert 0 <= x < Q and 0 <= y < Q
        h = mul(x, x) ^ x ^ alpha
        assert h
        g = mul(mul(x, x), x) ^ mul(x, x) ^ x ^ mul(alpha, alpha)
        # y is the Artin--Schreier coordinate, Y=h*y in the Mumford model.
        assert mul(h, mul(y, y) ^ y) == g
        point_count += 1
    result = {
        'status': 'PASS',
        'source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        'field_modulus': MOD, 'field_irreducible': True,
        'conductor': M, 'prime_factors': PRIMES,
        'local_doubling_periods': periods,
        'global_doubling_period': period,
        'primitive_orbit_count': orbit_count,
        'distinct_generalized_CRT_signatures': len(signatures),
        'curve_point_equations_checked': point_count,
        'jacobian_order_by_integer_Newton_recurrence': order,
        'curve_point_count_by_integer_Newton_recurrence': Q + 1 - trace[9],
        'scope': 'Independent field, curve-point and complete primitive-orbit audit; exact divisor multiples are checked in the separate canonical verifier.',
        'runtime_seconds': time.time() - start,
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
