#!/usr/bin/env python3
"""Exact finite data for the modular-group comparison in the F.7 attack.

The profinite extension, peripheral, and normalization arguments are in
f_modular_gt0_comparison.tex.  This checks their finite quotient inputs.
"""
from itertools import permutations, combinations
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
    cosets.remove(frozenset(subgroup))
    cosets.insert(0, frozenset(subgroup))
    index = {c: i for i, c in enumerate(cosets)}
    action = {g: tuple(index[frozenset(multiply(g, h) for h in c)]
                       for c in cosets) for g in group}
    assert len(set(action.values())) == len(group)
    return cosets, action


def inspect(n, group, automorphism_conjugators):
    involutions = sorted(g for g in group if order(g) == 2)
    triples = sorted(g for g in group if order(g) == 3)
    pairs = [(a, b) for a in involutions for b in triples
             if generated([a, b], n) == group]
    if n == 5:
        a, b = (1, 0, 3, 2, 4), (2, 1, 4, 3, 0)
    else:
        a, b = (0, 2, 1), (1, 2, 0)
    assert (a, b) in pairs
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


def free_product_reduce(word):
    out = []
    for value in word:
        if out and abs(out[-1]) == abs(value):
            old = out.pop()
            if abs(value) == 2:
                residue = ((1 if old > 0 else 2) +
                           (1 if value > 0 else 2)) % 3
                if residue:
                    out.append(2 if residue == 1 else -2)
        else:
            out.append(value)
    return tuple(out)


def free_product_inverse(word):
    return tuple(1 if value == 1 else -value for value in reversed(word))


def quotient_transversal(group, a, b):
    one = tuple(range(len(a)))
    words = {one: ()}
    queue = [one]
    for g in queue:
        for letter, permutation in ((1, a), (2, b)):
            h = multiply(g, permutation)
            if h not in words:
                words[h] = free_product_reduce(words[g] + (letter,))
                queue.append(h)
    assert set(words) == group
    return words, queue


def pants_schreier_check(group, a, b):
    words, queue = quotient_transversal(group, a, b)
    x, y = (1, 2, 1, 2), (2, 1, 2, 1)
    known = {(): (), x: (1,), y: (2,),
             free_product_inverse(x): (-1,),
             free_product_inverse(y): (-2,)}
    rows = []
    rewrite = {}
    for g in queue:
        for letter, permutation in ((1, a), (2, b)):
            h = multiply(g, permutation)
            kernel_word = free_product_reduce(
                words[g] + (letter,) + free_product_inverse(words[h]))
            assert kernel_word in known
            rewrite[g, letter] = known[kernel_word]
            rows.append({'representative': words[g], 'generator': letter,
                         'next_representative': words[h],
                         'kernel_word_in_a_b': kernel_word,
                         'kernel_word_in_x_y': known[kernel_word]})
    assert free_product_reduce((1,) + x + (1,)) == y
    assert free_product_reduce((1,) + y + (1,)) == x
    assert free_product_reduce((2,) + x + (-2,)) == y
    assert free_product_reduce((2,) + y + (-2,)) == free_product_reduce(
        free_product_inverse(x) + free_product_inverse(y))
    relator_checks = 0
    for g in queue:
        for relator in ((1, 1), (2, 2, 2)):
            current, rewritten = g, []
            for letter in relator:
                for value in rewrite[current, letter]:
                    if rewritten and rewritten[-1] == -value:
                        rewritten.pop()
                    else:
                        rewritten.append(value)
                current = multiply(current, a if letter == 1 else b)
            assert current == g and not rewritten
            relator_checks += 1
    return {'x': x, 'y': y, 'rewriting_table': rows,
            'rewritten_orbifold_relators_are_all_tautologies': relator_checks,
            'a_action': ['y', 'x'],
            'b_action': ['y', 'x^-1 y^-1']}


def triple_detector_orbits(group, a, b, d):
    cyclic = generated([d], 5)
    words, queue = quotient_transversal(group, a, b)
    cosets, representatives = [], []
    seen = set()
    for g in queue:
        coset = frozenset(multiply(g, h) for h in cyclic)
        if coset not in seen:
            seen.add(coset)
            cosets.append(coset)
            representatives.append(g)
    index = {c: i for i, c in enumerate(cosets)}
    action = {g: tuple(index[frozenset(multiply(g, h) for h in c)]
                       for c in cosets) for g in group}
    assert len(cosets) == 12 and len(set(action.values())) == 60
    remaining = set(combinations(range(12), 3))
    rows = []
    while remaining:
        triple = min(remaining)
        orbit = {tuple(sorted(action[g][i] for i in triple)) for g in group}
        stabilizer = [g for g in group
                      if tuple(sorted(action[g][i] for i in triple)) == triple]
        assert len(orbit) * len(stabilizer) == 60
        assert len(stabilizer) in (1, 3)
        transports = []
        for target in sorted(orbit):
            g = next(g for g in sorted(group)
                     if tuple(sorted(action[g][i] for i in triple)) == target)
            transports.append({'target_triple': target,
                               'A5_transporter': g,
                               'transporter_word_in_a_b': words[g]})
        rows.append({'representative_triple': triple, 'orbit_size': len(orbit),
                     'stabilizer_order': len(stabilizer),
                     'transporters': transports})
        remaining -= orbit
    assert sorted(row['orbit_size'] for row in rows) == [20, 20, 60, 60, 60]
    return {
        'cusp_labels': [
            {'label': i, 'coset_representative': g,
             'word_in_a_b': words[g],
             'peripheral_word': list(words[g] + (1, 2)*5 +
                                     free_product_inverse(words[g]))}
            for i, g in enumerate(representatives)],
        'triple_count': 220,
        'orbit_count': len(rows),
        'orbits': rows,
    }


def main():
    s3 = set(permutations(range(3)))
    s5 = set(permutations(range(5)))
    a5 = {g for g in s5 if parity(g) == 0}
    small, (small_a, small_b, _) = inspect(3, s3, s3)
    large, (large_a, large_b, d) = inspect(5, a5, s5)
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
        'pants_kernel_exact_Schreier_basis': pants_schreier_check(
            s3, small_a, small_b),
        'three_cusp_detector_orbits': triple_detector_orbits(
            a5, large_a, large_b, d),
        'all_assertions_passed': True,
    }
    Path(__file__).with_name('modular_a5_gt0_f7_output.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
