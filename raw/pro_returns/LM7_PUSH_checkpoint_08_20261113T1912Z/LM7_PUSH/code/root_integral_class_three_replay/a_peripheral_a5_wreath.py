#!/usr/bin/env python3
"""Exact finite constants for the A5-wreath proper lifting theorem.

Construct A5 from all even permutations, enumerate its full subgroup
lattice and all automorphisms from images of a generating pair, and
enumerate all 3600 commutators.  The resulting uniform counting bounds
certify proper solutions for every allowed boundary-class pattern;
no representation is sampled probabilistically.
"""

from collections import Counter, deque
from fractions import Fraction
from itertools import permutations, product
from math import comb
from pathlib import Path
import importlib.util
import json

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('finite_count', HERE/'a_peripheral_count.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def main():
    S = module.Group('A5', [p for p in permutations(range(5)) if module.parity(p) == 0],
                     module.perm_mul, tuple(range(5)))
    assert S.size == 60
    a = S.index[(1, 2, 0, 3, 4)]
    b = S.index[(1, 2, 3, 4, 0)]
    assert len(S.generated([a, b])) == 60
    center = [g for g in range(60)
              if all(S.mul[g][h] == S.mul[h][g] for h in range(60))]
    assert center == [S.one]

    commutators = Counter(S.commutator(x, y) for x, y in product(range(60), repeat=2))
    assert len(commutators) == 60 and min(commutators.values()) >= 1
    classes, remaining = [], set(range(60))
    while remaining:
        rep = min(remaining)
        c = S.conjugacy_class(rep)
        remaining -= c
        assert len({commutators[h] for h in c}) == 1
        classes.append({'representative': rep, 'order': S.orders[rep],
                        'size': len(c), 'commutator_pair_count_per_element': commutators[rep]})
    print('A5 commutator counts by class:',
          [(c['order'], c['size'], c['commutator_pair_count_per_element']) for c in classes])

    # Exhaustive subgroup lattice by adjoining one element at a time.
    trivial = frozenset([S.one])
    subgroups = {trivial: []}
    queue = deque([trivial])
    while queue:
        H = queue.popleft()
        for g in range(60):
            if g in H:
                continue
            gens = subgroups[H]+[g]
            K = S.generated(gens)
            if K not in subgroups:
                subgroups[K] = gens
                queue.append(K)
    proper = [h for h in subgroups if len(h) < 60]
    maximal = [h for h in proper if not any(h < k for k in proper)]
    assert len(subgroups) == 59
    assert Counter(map(len, maximal)) == {12: 5, 10: 6, 6: 10}
    assert all(any(h <= k for k in maximal) for h in proper)
    assert len(S.generated([S.commutator(g, h) for g in range(60) for h in range(60)])) == 60
    normal_subgroups = [h for h in subgroups
                        if all(S.conjugate(g, u) in h for g in range(60) for u in h)]
    assert sorted(map(len, normal_subgroups)) == [1, 60]
    print('Complete subgroup lattice:', len(subgroups), 'subgroups; maximal orders:',
          dict(sorted(Counter(map(len, maximal)).items())))

    # Enumerate every proposed automorphism by the images of the fixed
    # generating pair.  The propagation checks all literal generator edges.
    def proposed_map(aa, bb):
        image = {S.one: S.one}
        todo = deque([S.one])
        for_current = (a, b)
        for_target = (aa, bb)
        while todo:
            g = todo.popleft()
            for x, y in zip(for_current, for_target):
                h = S.mul[g][x]
                value = S.mul[image[g]][y]
                if h in image:
                    if image[h] != value:
                        return None
                else:
                    image[h] = value
                    todo.append(h)
        if len(image) == len(set(image.values())) == 60:
            return tuple(image[i] for i in range(60))
        return None

    automorphisms = []
    for aa, bb in product(range(60), repeat=2):
        candidate = proposed_map(aa, bb)
        if candidate is not None:
            automorphisms.append(candidate)
    assert len(set(automorphisms)) == len(automorphisms) == 120
    inners = {tuple(S.conjugate(h, g) for g in range(60)) for h in range(60)}
    assert len(inners) == 60 and inners <= set(automorphisms)
    print('Aut(A5):', len(automorphisms), 'Inn(A5):', len(inners), 'Out(A5): 2')

    nonsurjective_fraction = Fraction(21*60**2, 5**12)
    repeated_kernel_fraction = Fraction(comb(24, 4), 60**4)
    total_fraction = nonsurjective_fraction+repeated_kernel_fraction
    assert total_fraction < Fraction(1, 500)
    monotone_ratio_bound = Fraction(29**4, 21**4*60)
    assert monotone_ratio_bound < 1
    print('Uniform proper-subgroup fraction bound:', nonsurjective_fraction)
    print('Uniform repeated-kernel fraction bound:', repeated_kernel_fraction)
    print('Their sum:', total_fraction, '< 1/500')
    print('Successive n->n+5 deck-bound ratio <=', monotone_ratio_bound, '< 1')

    # The first regular noncyclic example D=C5^2, with actual peripheral
    # permutations on its 25 elements and all six order-five subgroups.
    D = list(product(range(5), repeat=2))
    dindex = {d: i for i, d in enumerate(D)}
    directions = [(1, 0), (0, 1), (4, 4)]
    actions = [[dindex[((d[0]+e[0]) % 5, (d[1]+e[1]) % 5)] for d in D]
               for e in directions]
    cycles = []
    for p in actions:
        unseen = set(range(25))
        cs = []
        while unseen:
            first = min(unseen)
            c, j = [], first
            while j in unseen:
                c.append(j)
                unseen.remove(j)
                j = p[j]
            assert j == first and len(c) == 5
            cs.append(c)
        cycles.append(cs)
    assert [len(c) for c in cycles] == [5, 5, 5]
    lines = {frozenset(((k*a) % 5, (k*b) % 5) for k in range(5))
             for a, b in D if (a, b) != (0, 0)}
    assert len(lines) == 6
    print('C5^2 cover: degree25, boundary counts5+5+5, genus6, six order5 subgroups')

    payload = {'status': 'PASS_UNIFORM_A5_WREATH_LIFTING_CONSTANTS',
               'group_elements': S.elements, 'generating_pair_indices': [a, b],
               'classes_and_commutator_counts': classes,
               'every_element_is_a_commutator': True,
               'minimum_commutator_pair_count': min(commutators.values()),
               'all_subgroups': [{'elements': sorted(h), 'generators': subgroups[h]}
                                 for h in sorted(subgroups, key=lambda h: (len(h), sorted(h)))],
               'maximal_subgroups': [sorted(h) for h in maximal],
               'automorphisms': automorphisms,
               'automorphism_order': 120, 'inner_order': 60, 'center_order': 1,
               'normal_subgroup_orders': [1, 60],
               'uniform_bound': {
                   'minimum_degree': 25, 'minimum_genus': 6,
                   'proper_subgroup_fraction': str(nonsurjective_fraction),
                   'repeated_kernel_fraction': str(repeated_kernel_fraction),
                   'total_fraction': str(total_fraction), 'strict_upper_bound': '1/500',
                   'monotone_ratio_bound': str(monotone_ratio_bound)},
               'first_regular_example': {'D': D, 'peripheral_actions': actions,
                                         'peripheral_cycles': cycles, 'genus': 6,
                                         'order_five_subgroups': [sorted(h) for h in sorted(lines, key=lambda h: sorted(h))]},
               'scope': 'Exact finite constants and uniform inequalities. The full nonabelian Shapiro and properness argument is proved in D.28.'}
    HERE.joinpath('a_peripheral_a5_wreath.json').write_text(json.dumps(payload, indent=2)+'\n')
    print(payload['status'])


if __name__ == '__main__':
    main()
