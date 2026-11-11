#!/usr/bin/env python3
"""Exact element orders in the full PSL2(F7) characteristic GT shadow.

The supplied finite_shadows.json certifies the 512-element color-preserving
subgroup D1 acting on generating pairs modulo simultaneous inner conjugacy.
We reconstruct those pair classes in precisely the original order and adjoin
complex conjugation c: [(x,y)] -> [(x^-1,y^-1)].  Its nontrivial power-class
action, together with the already established index two, identifies the
resulting 1024-element permutation group with the full finite shadow.

This computes a finite shadow, not the unknown full Galois image in it.
Every group element and every product of two group elements is checked.
Only Python's standard library and finite_groups.py are required.
"""

from collections import Counter
from math import lcm
from pathlib import Path
import json

from finite_groups import matrix_group, orbit_pair_classes


HERE = Path(__file__).resolve().parent


def compose(left, right):
    """Permutation multiplication with the right factor acting first."""
    return tuple(left[i] for i in right)


def permutation_order(permutation):
    seen = set()
    answer = 1
    for start in range(len(permutation)):
        if start in seen:
            continue
        current, length = start, 0
        while current not in seen:
            seen.add(current)
            length += 1
            current = permutation[current]
        assert current == start
        answer = lcm(answer, length)
    return answer


def generated_group(generators, identity):
    elements = {identity}
    queue = [identity]
    for element in queue:
        for generator in generators:
            product = compose(element, generator)
            if product not in elements:
                elements.add(product)
                queue.append(product)
    return elements


def order_distribution(elements, identity):
    counts = Counter()
    for element in elements:
        order = permutation_order(element)
        # The cycle calculation gives minimality; also check the stated power.
        power = identity
        for _ in range(order):
            power = compose(power, element)
        assert power == identity
        counts[order] += 1
    return dict(sorted(counts.items()))


def main():
    recorded = json.loads((HERE / 'finite_shadows.json').read_text())['PSL2F7']
    group = matrix_group(7, projective=True)
    representatives, which = orbit_pair_classes(group)
    degree = len(representatives)
    identity = tuple(range(degree))
    actual_representatives = [
        [list(group.elements[x]), list(group.elements[y])]
        for x, y in representatives
    ]
    assert actual_representatives == recorded['pair_representatives']
    assert degree == recorded['inner_pair_classes'] == 114

    generators = list(dict.fromkeys(tuple(g) for g in recorded['generators']))
    theta, delta, outer = (
        tuple(recorded[name]) for name in ('theta', 'delta', 'outer')
    )
    conjugation = tuple(which[(group.inv[x], group.inv[y])]
                        for x, y in representatives)
    for permutation in generators + [theta, delta, outer, conjugation]:
        assert sorted(permutation) == list(identity)
    assert theta == tuple(which[(y, x)] for x, y in representatives)
    assert delta == tuple(which[(group.inv[group.mul(x, y)], y)]
                          for x, y in representatives)
    colors = [(group.classes[x], group.classes[y])
              for x, y in representatives]

    d1 = generated_group(generators, identity)
    assert len(d1) == recorded['order'] == 512
    for element in d1:
        assert all(colors[element[i]] == colors[i] for i in range(degree))
        assert all(compose(element, operator) == compose(operator, element)
                   for operator in (theta, delta, outer))
    d1_orders = order_distribution(d1, identity)
    assert {str(k): v for k, v in d1_orders.items()} == recorded['element_orders']

    assert permutation_order(conjugation) == 2
    assert compose(conjugation, conjugation) == identity
    assert conjugation not in d1
    assert group.exponent == recorded['exponent'] == 84
    assert (-1) % group.exponent not in recorded['power_class_kernel']
    changed_classes = [i for i in range(degree)
                       if colors[conjugation[i]] != colors[i]]
    assert changed_classes
    assert all(compose(conjugation, operator) == compose(operator, conjugation)
               for operator in (theta, delta, outer))
    for generator in generators:
        assert compose(compose(conjugation, generator), conjugation) in d1

    full = generated_group(generators + [conjugation], identity)
    other_coset = {compose(conjugation, element) for element in d1}
    assert d1.isdisjoint(other_coset)
    assert full == d1 | other_coset
    assert len(full) == recorded['full_GT_shadow_order'] == 1024
    print('Reconstructed PSL2(F7) inner generating-pair classes:', degree,
          flush=True)
    print('D1: order', len(d1), 'element-order distribution', d1_orders,
          flush=True)
    print('Complex conjugation: order 2, outside D1, normalizes all',
          len(generators), 'recorded generators.', flush=True)
    print('Generated full shadow:', len(full), 'elements.', flush=True)

    # Exhaustive closure, not just a generator-edge or sampled verification.
    products_checked = 0
    for left in full:
        for right in full:
            assert compose(left, right) in full
            products_checked += 1
    full_orders = order_distribution(full, identity)
    coset_orders = order_distribution(other_coset, identity)
    assert sum(full_orders.values()) == 1024
    assert full_orders.get(1) == 1
    assert all(order in (1, 2, 4, 8) for order in full_orders)

    result = {
        'group': 'PSL2(F7)',
        'permutation_degree': degree,
        'D1_order': len(d1),
        'D1_generator_count': len(generators),
        'D1_element_orders': d1_orders,
        'complex_conjugation_order': 2,
        'complex_conjugation_permutation': conjugation,
        'complex_conjugation_outside_D1': True,
        'complex_conjugation_normalizes_D1': True,
        'power_class_minus_one_mod_exponent': (-1) % group.exponent,
        'power_class_minus_one_in_kernel': False,
        'full_shadow_order': len(full),
        'full_shadow_element_orders': full_orders,
        'nontrivial_coset_element_orders': coset_orders,
        'full_shadow_exponent': lcm(*full_orders),
        'pair_representative_order_matches_input': True,
        'all_permutations_valid': True,
        'all_products_checked': products_checked,
        'all_element_orders_checked': True,
        'success': True,
        'scope': ('The full finite characteristic shadow is computed. '
                  'The full Galois image in this shadow remains undetermined.'),
    }
    (HERE / 'finite_shadow_orders.json').write_text(
        json.dumps(result, indent=2) + '\n')
    print('Full-shadow element-order distribution:', full_orders)
    print('Nontrivial coset element-order distribution:', coset_orders)
    print('Full-shadow exponent:', result['full_shadow_exponent'])
    print('Exhaustively checked products:', products_checked)
    print('All permutation orders verified; all checks passed.')
    print(result['scope'])


if __name__ == '__main__':
    main()
