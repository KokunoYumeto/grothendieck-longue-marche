#!/usr/bin/env python3
"""Finite necessary square tests for the exact standard one-class transporter.

The source is C2(v) coproduct Zhat(z), with g=z^2 and c=[g,v].
Every full centralizing peripheral conjugator supplies a square root of
c^((mu-1)/2)g, after the specified reflection normalization. This script
only records explicit permutation quotients in which selected unit
residues fail that necessary condition. It infers no full existence.
"""
from itertools import permutations
from math import gcd, lcm
from pathlib import Path
import json


def mul(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def inv(a):
    b = [0] * len(a)
    for i, x in enumerate(a):
        b[x] = i
    return tuple(b)


def cycles(a):
    seen, result = set(), []
    for i in range(len(a)):
        if i in seen:
            continue
        current, length = i, 0
        while current not in seen:
            seen.add(current)
            length += 1
            current = a[current]
        result.append(length)
    return sorted(result)


def has_square_root(a):
    lengths = cycles(a)
    return all(lengths.count(k) % 2 == 0 for k in set(lengths) if k % 2 == 0)


def main():
    witnesses, counts = {}, {}
    for degree in range(3, 8):
        ident = tuple(range(degree))
        cases = 0
        for transpositions in range(1, degree // 2 + 1):
            v = list(ident)
            for i in range(transpositions):
                v[2*i], v[2*i+1] = 2*i+1, 2*i
            v = tuple(v)
            for z in permutations(range(degree)):
                g = mul(z, z)
                c = mul(mul(mul(g, v), inv(g)), v)
                order = lcm(*cycles(c))
                power = ident
                for r in range(order):
                    mu = 2*r+1
                    if gcd(mu, 2*order) == 1:
                        cases += 1
                        a = mul(power, g)
                        if not has_square_root(a):
                            key = (2*order, mu)
                            witnesses.setdefault(key, {
                                'degree': degree, 'v': v, 'z': z,
                                'g': g, 'c': c, 'order_of_c': order,
                                'mu_modulus': 2*order, 'mu_residue': mu,
                                'transporter': a, 'transporter_cycles': cycles(a),
                            })
                    power = mul(power, c)
                assert power == ident
        counts[str(degree)] = cases
    result = {
        'scope': 'Explicit finite necessary square-root obstructions only.',
        'source': 'C2(v) coproduct Zhat(z); g=z^2, c=[g,v]',
        'cases_by_permutation_degree': counts,
        'total_unit_residue_cases': sum(counts.values()),
        'forbidden_unit_residues': [witnesses[k] for k in sorted(witnesses)],
        'all_assertions_passed': True,
    }
    path = Path(__file__).with_name('oneclass_square_obstructions_output.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
