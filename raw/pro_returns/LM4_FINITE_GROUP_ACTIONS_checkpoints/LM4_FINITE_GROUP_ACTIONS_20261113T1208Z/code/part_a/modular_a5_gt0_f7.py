#!/usr/bin/env python3
"""Exact finite data for the modular-group comparison in the F.7 attack.

The profinite extension, peripheral, and normalization arguments are in
f_modular_gt0_comparison.tex.  This checks their finite quotient inputs.
"""
from itertools import permutations
from pathlib import Path
import json


def multiply(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def inverse(a):
    return tuple(a.index(i) for i in range(len(a)))


def conjugate(g, a):
    return multiply(multiply(g, a), inverse(g))


def parity(a):
    return sum(a[i] > a[j] for i in range(len(a))
               for j in range(i+1, len(a))) % 2


def generated(generators, n):
    one = tuple(range(n))
    found = {one}
    queue = [one]
    for a in queue:
        for b in generators:
            c = multiply(a, b)
            if c not in found:
                found.add(c)
                queue.append(c)
    return found


def order(a):
    one = tuple(range(len(a)))
    x = one
    for k in range(1, 121):
        x = multiply(x, a)
        if x == one:
            return k
    raise AssertionError('unexpected element order')


def coset_action(group, subgroup):
    cosets = sorted({frozenset(multiply(g, h) for h in subgroup)
                     for g in group}, key=lambda c: sorted(c))
    index = {c: i for i, c in enumerate(cosets)}
    action = {g: tuple(index[frozenset(multiply(g, h) for h in c)]
                       for c in cosets) for g in group}
    assert len(set(action.values())) == len(group)
    return cosets, action


def inspect(n, group, automorphism_conjugators):
    involutions = [g for g in group if order(g) == 2]
    triples = [g for g in group if order(g) == 3]
    pairs = [(a, b) for a in involutions for b in triples
             if generated([a, b], n) == group]
    a, b = pairs[0]
    pair_orbit = {(conjugate(g, a), conjugate(g, b))
                  for g in automorphism_conjugators}
    assert pair_orbit == set(pairs)
    assert len(pair_orbit) == len(automorphism_conjugators)
    d = multiply(a, b)
    cyclic = generated([d], n)
    centralizer = [g for g in group if multiply(g, d) == multiply(d, g)]
    assert set(centralizer) == cyclic
    cosets, action = coset_action(group, cyclic)
    one = tuple(range(n))
    centre = [g for g in group
              if all(multiply(g, h) == multiply(h, g) for h in group)]
    assert centre == [one]
    stabilizer = [g for g in group if action[g][0] == 0]
    assert len(stabilizer) == order(d)
    index = len(group)
    cusp_count = len(cosets)
    genus = (2 + index//6 - cusp_count)//2
    assert 2 + index//6 - cusp_count == 0
    return {
        'group_order': index,
        'involution_count': len(involutions),
        'order_three_count': len(triples),
        'epimorphism_pair_count': len(pairs),
        'single_postcomposition_orbit': True,
        'chosen_order_two': list(a),
        'chosen_order_three': list(b),
        'cusp_product': list(d),
        'cusp_product_order': order(d),
        'cusp_product_centralizer_order': len(centralizer),
        'cusp_coset_count': cusp_count,
        'faithful_cusp_action': True,
        'free_kernel_rank_from_orbifold_euler_characteristic': 1+index//6,
        'surface_type_from_cusp_degrees': [genus, cusp_count],
    }, (a, b, d)


def main():
    s3 = set(permutations(range(3)))
    s5 = set(permutations(range(5)))
    a5 = {g for g in s5 if parity(g) == 0}
    small, _ = inspect(3, s3, s3)
    large, (_, _, d) = inspect(5, a5, s5)
    assert small['epimorphism_pair_count'] == 6
    assert large['epimorphism_pair_count'] == 120

    # The five Sylow-two groups are intrinsically the five V4 groups.
    v4s = {frozenset(generated([a, b], 5))
           for a in a5 if order(a) == 2
           for b in a5 if order(b) == 2
           if a != b and multiply(a, b) == multiply(b, a)}
    assert len(v4s) == 5 and all(len(v) == 4 for v in v4s)
    v4s = sorted(v4s, key=lambda v: sorted(v))
    v4index = {v: i for i, v in enumerate(v4s)}
    five_action = {
        g: tuple(v4index[frozenset(conjugate(g, a) for a in v)] for v in v4s)
        for g in a5}
    assert len(set(five_action.values())) == 60

    # Odd S5 conjugation exchanges the two A5 conjugacy classes of 5-cycles.
    cusp_class = {conjugate(g, d) for g in a5}
    assert len(cusp_class) == 12
    preserving = [g for g in s5 if conjugate(g, d) in cusp_class]
    assert set(preserving) == a5
    outer_class = {conjugate(g, d) for g in s5 if parity(g)}
    assert len(outer_class) == 12 and not cusp_class.intersection(outer_class)
    assert cusp_class | outer_class == {g for g in a5 if order(g) == 5}

    result = {
        'scope': 'Finite quotient inputs to the exact C2 coproduct C3 / A5 / S3 comparison; no residual centralizer triviality or finite-lift sufficiency claim.',
        'S3': small,
        'A5': large,
        'A5_intrinsic_V4_count': len(v4s),
        'A5_action_on_V4s_faithful': True,
        'A5_five_cycle_class_size': len(cusp_class),
        'S5_conjugators_preserving_the_A5_cusp_class': len(preserving),
        'those_conjugators_are_exactly_A5': True,
        'all_assertions_passed': True,
    }
    Path(__file__).with_name('modular_a5_gt0_f7_output.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
