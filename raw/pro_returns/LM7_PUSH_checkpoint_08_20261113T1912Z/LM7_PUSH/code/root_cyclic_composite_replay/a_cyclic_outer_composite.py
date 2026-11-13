#!/usr/bin/env python3
"""Exact composite-cyclic surface phase and character certificates.

The general proof uses the displayed free-word maps, CRT, and integral
symplectic elimination.  Finite enumerations here check their exact
conventions, including nonzero nonunit boundary characters.
"""
from collections import deque
from itertools import product
from math import gcd
from pathlib import Path
import json

from a_relative_prop import mul, inv, comm, subst, compose, exact_word_checks

HERE = Path(__file__).resolve().parent


def power_word(word, n):
    return mul(*([word if n >= 0 else inv(word)] * abs(n)))


def power_map(phi, reverse, n):
    answer = {j: [j] for j in phi}
    step = phi if n >= 0 else reverse
    for _ in range(abs(n)):
        answer = compose(step, answer)
    return answer


def character(word, values, modulus):
    return sum((1 if k > 0 else -1)*values[abs(k)-1]
               for k in word) % modulus


def prime_powers(n):
    answer = []
    p = 2
    while p*p <= n:
        if n % p:
            p += 1
            continue
        q = 1
        while n % p == 0:
            n //= p
            q *= p
        answer.append((p, q))
        p += 1
    if n > 1:
        answer.append((n, n))
    return answer


def balanced(a, n):
    a %= n
    return a if 2*a <= n else a-n


def source_phase_certificate():
    old = exact_word_checks()
    push = {int(k): v for k, v in old['bounding_pair_map'].items()}
    push_inv = {int(k): v for k, v in old['bounding_pair_inverse'].items()}
    twist = {1: [1], 2: [2, 1], 3: [3]}
    twist_inv = {1: [1], 2: [2, -1], 3: [3]}
    chart = {1: [1, 2], 2: [2], 3: [3]}
    chart_inv = {1: [1, -2], 2: [2], 3: [3]}
    identity = {j: [j] for j in (1, 2, 3)}
    surface = mul(comm([1], [2]), [3])
    assert compose(push, twist) == compose(twist, push)
    assert subst([-3, -1], push) == [-3, -1]
    assert compose(twist, twist_inv) == compose(twist_inv, twist) == identity
    assert subst(surface, twist) == surface

    maps = {}
    modulus_rows = []
    samples = []
    moduli = [2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20]
    for modulus in moduli:
        counts = {'onto_handle_boundary_characters': 0,
                  'corrected_handle_prime_components': 0,
                  'boundary_supplier_prime_components': 0,
                  'already_class_invariant_prime_components': 0}
        for aa, bb, jj in product(range(modulus), repeat=3):
            if gcd(gcd(gcd(aa, bb), jj), modulus) != 1:
                continue
            counts['onto_handle_boundary_characters'] += 1
            for ell, q in prime_powers(modulus):
                other = modulus // q
                crt = (other*pow(other, -1, q)) % modulus
                if jj % ell:
                    assert crt % gcd(jj, modulus) == 0
                    counts['already_class_invariant_prime_components'] += 1
                    continue
                change = 0 if aa % ell else 1
                chart_a = (aa + change*bb) % modulus
                assert chart_a % ell
                N = balanced(crt, modulus)
                k = balanced(crt*(-jj*pow(chart_a, -1, q) % q), modulus)
                assert (N*jj+k*chart_a) % modulus == 0
                phase = -N*(jj+chart_a) % modulus
                assert phase % ell
                assert phase % other == 0
                key = (N, k, change)
                if key not in maps:
                    pn = power_map(push, push_inv, N)
                    pni = power_map(push, push_inv, -N)
                    tk = power_map(twist, twist_inv, k)
                    tki = power_map(twist, twist_inv, -k)
                    theta = compose(pn, tk)
                    theta_inv = compose(tki, pni)
                    conjugator = power_word([-3, -1], N)
                    if change:
                        theta = compose(chart, compose(theta, chart_inv))
                        theta_inv = compose(chart, compose(theta_inv, chart_inv))
                        conjugator = subst(conjugator, chart)
                    assert compose(theta, theta_inv) == identity
                    assert compose(theta_inv, theta) == identity
                    assert subst(surface, theta) == subst(surface, theta_inv) == surface
                    assert theta[3] == mul(conjugator, [3], inv(conjugator))
                    maps[key] = {'N': N, 'k': k, 'replace_a_by_ab': bool(change),
                                 'map': theta, 'inverse': theta_inv,
                                 'literal_boundary_conjugator': conjugator}
                row = maps[key]
                values = [aa, bb, jj]
                assert [character(row['map'][i], values, modulus)
                        for i in (1, 2, 3)] == values
                assert character(row['literal_boundary_conjugator'], values,
                                 modulus) == phase
                assert gcd(phase, q) == 1
                counts['corrected_handle_prime_components'] += 1
                if modulus == 12 and (aa, bb, jj) in [(2, 3, 4), (3, 4, 6)]:
                    samples.append({'modulus': modulus, 'character': values,
                                    'prime_power': q, 'N': N, 'k': k,
                                    'chart_a': chart_a, 'phase': phase})

        # Pure boundary supplier: the secondary phase is in <d>, so
        # every S-conjugacy-invariant set in that coset is unchanged.
        for jj, dd in product(range(modulus), repeat=2):
            for ell, q in prime_powers(modulus):
                if jj % ell or dd % ell == 0:
                    continue
                other = modulus // q
                N = balanced(other*pow(other, -1, q), modulus)
                c_conj = power_word([1, 2], N)
                d_conj = mul(c_conj, power_word([2], -N))
                theta = {1: mul(c_conj, [1], inv(c_conj)),
                         2: mul(c_conj, [2], inv(c_conj))}
                theta_inv = {1: mul(inv(c_conj), [1], c_conj),
                             2: mul(inv(c_conj), [2], c_conj)}
                ident2 = {1: [1], 2: [2]}
                assert compose(theta, theta_inv) == compose(theta_inv, theta) == ident2
                assert subst([1, 2], theta) == [1, 2]
                assert theta[2] == mul(d_conj, [2], inv(d_conj))
                c_phase = character(c_conj, [jj, dd], modulus)
                d_phase = character(d_conj, [jj, dd], modulus)
                assert c_phase == N*(jj+dd) % modulus
                assert d_phase == N*jj % modulus
                assert gcd(c_phase, q) == 1 and c_phase % other == 0
                assert d_phase % gcd(dd, modulus) == 0
                counts['boundary_supplier_prime_components'] += 1
        modulus_rows.append({'modulus': modulus, **counts})
    return {'scope': 'Exact free-word maps and all stated finite character cases.',
            'push': push, 'push_inverse': push_inv,
            'twist': twist, 'twist_inverse': twist_inv,
            'a_to_ab_chart': chart, 'a_to_ab_chart_inverse': chart_inv,
            'all_moduli': modulus_rows,
            'distinct_literal_maps': [maps[key] for key in sorted(maps)],
            'composite_nonunit_examples': samples}


def character_orbits():
    """The actual handle twists and boundary-ideal translations on H1."""
    rows = []
    for modulus in [2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20]:
        orbit_count = 0
        source_count = 0
        for jj, kk in product(range(modulus), repeat=2):
            pending = set(product(range(modulus), repeat=2))
            by_divisor = {}
            while pending:
                start = min(pending)
                todo = deque([start])
                orbit = {start}
                while todo:
                    aa, bb = todo.popleft()
                    successors = [(aa, (bb+aa) % modulus),
                                  ((aa+bb) % modulus, bb),
                                  ((aa+jj) % modulus, bb),
                                  ((aa+kk) % modulus, bb),
                                  (aa, (bb+jj) % modulus),
                                  (aa, (bb+kk) % modulus)]
                    for nxt in successors:
                        if nxt not in orbit:
                            orbit.add(nxt)
                            todo.append(nxt)
                divisors = {gcd(gcd(gcd(gcd(aa, bb), jj), kk), modulus)
                            for aa, bb in orbit}
                assert len(divisors) == 1
                divisor = divisors.pop()
                assert divisor not in by_divisor
                by_divisor[divisor] = len(orbit)
                pending -= orbit
                orbit_count += 1
                source_count += len(orbit)
            expected = {}
            for aa, bb in product(range(modulus), repeat=2):
                d = gcd(gcd(gcd(gcd(aa, bb), jj), kk), modulus)
                expected[d] = expected.get(d, 0)+1
            assert by_divisor == expected
        assert source_count == modulus**4
        rows.append({'modulus': modulus,
                     'all_boundary_pairs': modulus**2,
                     'all_handle_boundary_characters': source_count,
                     'actual_generator_orbits': orbit_count,
                     'orbit_invariant': 'gcd(modulus,a,b,c1,c2)'})
    return rows


def main():
    phases = source_phase_certificate()
    orbits = character_orbits()
    payload = {'status': 'PASS_COMPOSITE_CYCLIC_SOURCE_PHASES_AND_CHARACTERS',
               'phase_maps': phases, 'character_orbits': orbits,
               'proof_scope': 'Finite checks of exact maps. The arbitrary-modulus theorem uses CRT, the displayed surface automorphisms, and integral symplectic elimination.'}
    HERE.joinpath('a_cyclic_outer_composite.json').write_text(json.dumps(payload, indent=2)+'\n')
    print('PASS all literal CRT-corrected push maps and their exact inverses')
    print('PASS nonzero nonunit boundary characters, supplier phases, and every prescribed prime component')
    print('PASS all genus-one character orbits for the twelve recorded composite/prime moduli')
    print('Distinct literal corrected maps:', len(phases['distinct_literal_maps']))
    print('Total handle-boundary characters checked:', sum(row['all_handle_boundary_characters'] for row in orbits))
    print(payload['status'])


if __name__ == '__main__':
    main()
