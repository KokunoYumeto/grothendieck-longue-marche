#!/usr/bin/env python3
"""Exact finite certificates for the all-prime argument in D.41."""
from itertools import product
from pathlib import Path
import json
import sympy as sp


def primes_below(limit):
    return [n for n in range(2, limit)
            if all(n % p for p in range(2, int(n**0.5) + 1))]


def prime_factors(n):
    return [p for p in primes_below(n + 1) if n % p == 0]


def multiplicative_order(p, q):
    a, order = p % q, 1
    while a != 1:
        a = a * p % q
        order += 1
    return order


def fp_red(word, q):
    result = []
    for gen, exponent in word:
        exponent %= q
        if not exponent:
            continue
        if result and result[-1][0] == gen:
            exponent = (result.pop()[1] + exponent) % q
            if exponent:
                result.append((gen, exponent))
        else:
            result.append((gen, exponent))
    return tuple(result)


def fp_mul(*words, q):
    return fp_red(sum(words, ()), q)


def fp_inv(word, q):
    return fp_red(tuple((g, -e) for g, e in reversed(word)), q)


def degree_two(word, rank):
    v = [0] * rank
    matrix = [[0] * rank for _ in range(rank)]
    for letter in word:
        i, sign = abs(letter) - 1, 1 if letter > 0 else -1
        for j in range(rank):
            matrix[j][i] += v[j] * sign
        if sign < 0:
            matrix[i][i] += 1
        v[i] += sign
    assert not any(v)
    return sp.Matrix(matrix)


def frobenius_orbits(p, q):
    remaining, orbits = set(range(1, q)), []
    while remaining:
        start = min(remaining)
        orbit, j = [], start
        while j not in orbit:
            orbit.append(j)
            remaining.remove(j)
            j = p * j % q
        assert j == start
        orbits.append(orbit)
    return orbits


def cover_check(q):
    y, z = ((0, 1),), ((1, 1),)
    us = [fp_red(((0, i), (1, 1), (0, -i-1)), q) for i in range(q)]
    assert fp_mul(*us, q=q) == ()
    for i in range(q):
        assert fp_mul(y, us[i], fp_inv(y, q=q), q=q) == us[(i+1) % q]
    x = fp_mul(fp_inv(z, q=q), fp_inv(y, q=q), q=q)
    boundary = fp_mul(*(x for _ in range(q)), q=q)
    indices = [(q-1-2*j) % q for j in range(q)]
    assert fp_mul(*(fp_inv(us[i], q=q) for i in indices), q=q) == boundary
    assert sorted(indices) == list(range(q))
    # Eliminate u_(q-1)=(u_0 ... u_(q-2))^-1.
    rank = q - 1
    boundary_basis_word = []
    for i in indices:
        if i == q-1:
            boundary_basis_word.extend(range(1, q))
        else:
            boundary_basis_word.append(-(i+1))
    omega = degree_two(boundary_basis_word, rank)
    assert omega == -omega.T
    assert omega.det() == 1
    deck = sp.zeros(rank)
    for i in range(rank-1):
        deck[i+1, i] = 1
    for i in range(rank):
        deck[i, rank-1] = -1
    assert deck**q == sp.eye(rank)
    assert deck.charpoly().all_coeffs() == [1] * q
    assert deck * omega * deck.T == omega
    inverse_form = omega.inv()
    assert deck.T * inverse_form * deck == inverse_form
    # Every involutive scalar assignment to a self-reciprocal
    # Frobenius factor has product +1 on paired eigenspaces.
    selected = next(p for p in prime_factors(q-1)
                    if multiplicative_order(p, q) % 2 == 0)
    orbits = frobenius_orbits(selected, q)
    assert all(set(orbit) == {-j % q for j in orbit} for orbit in orbits)
    assignments = 0
    for signs in product((-1, 1), repeat=len(orbits)):
        values = {j: signs[i] for i, orbit in enumerate(orbits) for j in orbit}
        assert all(values[j] * values[-j % q] == 1 for j in range(1, q))
        assignments += 1
    return {
        'q': q, 'genus': rank // 2, 'rank': rank,
        'surviving_boundary_indices': indices,
        'surviving_boundary_basis_word': boundary_basis_word,
        'boundary_bivector': [list(map(int, row)) for row in omega.tolist()],
        'boundary_form_determinant': int(omega.det()),
        'deck_characteristic_coefficients': [1] * q,
        'chosen_prime': selected,
        'chosen_prime_order_mod_q': multiplicative_order(selected, q),
        'self_reciprocal_frobenius_orbits': orbits,
        'all_involutive_factor_sign_assignments': assignments,
        'all_checks_passed': True,
    }


def main():
    covers = [cover_check(q) for q in primes_below(44) if q != 2]
    arithmetic = []
    for q in primes_below(2000):
        if q == 2:
            continue
        factors = prime_factors(q-1)
        orders = {p: multiplicative_order(p, q) for p in factors}
        candidates = [p for p in factors if orders[p] % 2 == 0]
        assert candidates
        p = min(candidates)
        d = orders[p]
        assert p < q and pow(p, d//2, q) == q-1
        orbits = frobenius_orbits(p, q)
        assert all(set(orbit) == {-j % q for j in orbit} for orbit in orbits)
        arithmetic.append({'q': q, 'prime_divisors_of_q_minus_one': factors,
                           'orders': orders, 'chosen_p': p,
                           'orbit_count': len(orbits), 'orbit_degree': d})
    result = {
        'purpose': 'Exact validation of the maps and finite arithmetic in D41',
        'covers': covers, 'prime_factor_checks': arithmetic,
        'all_checks_passed': True,
        'scope': 'The written prime-factor argument proves every odd q; this program validates its exact maps and arithmetic over a finite range.'
    }
    destination = Path(__file__).with_name('negative_multiplier_d41_output.json')
    destination.write_text(json.dumps(result, indent=2) + '\n')
    print('D41 exact filled-cover, boundary and cyclotomic-module checks:',
          [r['q'] for r in covers])
    print('Every boundary alternating matrix is unimodular and deck-invariant.')
    print('D41 prime-factor/Frobenius checks:', len(arithmetic), 'odd primes below2000.')
    print('Small witnesses (q,p,ord_q(p)):',
          [(r['q'], r['chosen_prime'], r['chosen_prime_order_mod_q']) for r in covers])
    print('All checks passed. Wrote', destination)


if __name__ == '__main__':
    main()
