#!/usr/bin/env python3
"""Exact closed-surface counts in the actual Aut(A6) outer extension.

Compare the two symplectic types of a surjective V4 character.  This
initial certificate counts all homomorphisms; any later epimorphism
deduction must separately remove every proper image.
"""

from collections import Counter
from itertools import product
from pathlib import Path
import importlib.util
import json

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('finite_count', HERE/'a_peripheral_count.py')
finite = importlib.util.module_from_spec(spec)
spec.loader.exec_module(finite)


def main():
    raw = json.loads(HERE.joinpath('a_peripheral_a6_outer.json').read_text())
    pairs = [tuple(p) for p in raw['automorphism_generator_pairs']]
    maps = dict(zip(pairs, raw['automorphism_maps']))
    a, b = raw['A6_generators']
    G = finite.Group('Aut(A6)', pairs,
                     lambda x, y: (maps[x][y[0]], maps[x][y[1]]), (a, b))
    inner = frozenset(raw['inner_indices'])
    outer = raw['outer_coordinates']
    classes = [frozenset(c) for c in raw['relative_classes'] if outer[c[0]] == 0]
    assert len(classes) == 7 and frozenset().union(*classes) == inner
    class_of = {g: i for i, cls in enumerate(classes) for g in cls}
    representatives = list(map(min, classes))
    identity_class = class_of[G.one]
    cosets = [[g for g in range(G.size) if outer[g] == value] for value in range(4)]
    K = {}
    for r, s in product(range(4), repeat=2):
        counts = Counter(G.commutator(x, y) for x in cosets[r] for y in cosets[s])
        assert set(counts) <= inner
        assert all(len({counts[g] for g in cls}) == 1 for cls in classes)
        K[r, s] = [counts[g] for g in representatives]
    print('Actual inner classes (order,size):',
          [(G.orders[g], len(cls)) for g, cls in zip(representatives, classes)], flush=True)
    print('K00,K10,K20,K12:', [K[pair] for pair in ((0, 0), (1, 0), (2, 0), (1, 2))], flush=True)

    # Structure constants per element of the target class, so vectors
    # remain coefficients of actual central group-algebra elements.
    structure = [[[sum(G.mul[G.inv[x]][g] in right for x in left)
                   for g in representatives] for right in classes] for left in classes]

    def multiply(u, v):
        return [sum(u[i]*v[j]*structure[i][j][k] for i in range(7) for j in range(7))
                for k in range(7)]

    one = [int(k == identity_class) for k in range(7)]

    def power(v, n):
        out = one
        for _ in range(n):
            out = multiply(out, v)
        return out

    comparisons = []
    for genus in range(2, 9):
        cup_one = multiply(K[1, 2], power(K[0, 0], genus-1))[identity_class]
        cup_zero = multiply(multiply(K[1, 0], K[2, 0]), power(K[0, 0], genus-2))[identity_class]
        comparisons.append({'genus': genus, 'cup0_all_maps': cup_zero,
                            'cup1_all_maps': cup_one, 'difference_cup0_minus_cup1': cup_zero-cup_one})
        print('Genus', genus, 'cup0', cup_zero, 'cup1', cup_one, 'difference', cup_zero-cup_one, flush=True)
    payload = {'status': 'PASS_ACTUAL_A6_OUTER_CUP_HOMOMORPHISM_COUNTS',
               'scope': 'All homomorphisms with the specified outer character; proper-image subtraction is not performed.',
               'inner_classes': [sorted(cls) for cls in classes],
               'inner_class_representatives': representatives,
               'identity_class': identity_class,
               'outer_commutator_counts_per_element': {str(k): v for k, v in K.items()},
               'class_algebra_structure_constants_per_element': structure,
               'comparisons': comparisons}
    HERE.joinpath('a_peripheral_a6_cup_count.json').write_text(json.dumps(payload, indent=2)+'\n')
    print(payload['status'])


if __name__ == '__main__':
    main()
