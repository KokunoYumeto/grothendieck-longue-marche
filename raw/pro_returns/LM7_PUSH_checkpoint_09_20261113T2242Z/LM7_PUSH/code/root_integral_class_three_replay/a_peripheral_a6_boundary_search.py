#!/usr/bin/env python3
"""Exact nontrivial-boundary search in the order-five degree20 family.

Use the literal surface presentation, every actual prescribed local
conjugator, and the complete full-outer subgroup family.  Counts include
all proper-image subtraction and retain the five distinct source maps.
"""

from collections import Counter
from itertools import product
from pathlib import Path
import argparse
import importlib.util
import json

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('finite_count', HERE/'a_peripheral_count.py')
finite = importlib.util.module_from_spec(spec)
spec.loader.exec_module(finite)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--surface', type=Path, default=HERE/'a_peripheral_surface20.json')
    parser.add_argument('--prefix', default='a_peripheral_a6_boundary_search')
    parser.add_argument('--boundary-flip', type=int)
    parser.add_argument('--flip-outer', type=int, choices=range(4), default=0)
    args = parser.parse_args()
    raw = json.loads(HERE.joinpath('a_peripheral_a6_outer.json').read_text())
    surface = json.loads(args.surface.read_text())
    sub = json.loads(HERE.joinpath('a_peripheral_a6_outer_subgroups.json').read_text())
    pairs = [tuple(p) for p in raw['automorphism_generator_pairs']]
    maps = dict(zip(pairs, raw['automorphism_maps']))
    a, b = raw['A6_generators']
    G = finite.Group('Aut(A6)', pairs,
                     lambda x, y: (maps[x][y[0]], maps[x][y[1]]), (a, b))
    outer = raw['outer_coordinates']
    classes = [frozenset(cls) for cls in raw['relative_classes']]
    class_of = {g: i for i, cls in enumerate(classes) for g in cls}
    inverse_class = [class_of[G.inv[min(cls)]] for cls in classes]
    outer_action = raw['outer_class_action']
    profiles = list(product(*[[i for i, cls in enumerate(classes) if outer[min(cls)] == bit]
                              for bit in (1, 2, 3)]))
    assert len(profiles) == 75
    problems = []
    for profile in profiles:
        rows = []
        for j in range(5):
            row = [outer_action[surface['boundary_base_path_outer'][i] ^
                                surface['source_path_module_outer_changes'][j][i] ^
                                surface['local_conjugator_outer_values'][j][i] ^
                                (args.flip_outer if i == args.boundary_flip else 0)][profile[i//4]]
                   for i in range(12)]
            assert [outer[min(classes[ci])] for ci in row] == surface['boundary_outer_characters'][j]
            rows.append(row)
        problems.append(rows)
    reps = [frozenset(record['members']) for record in sub['representatives']]
    actual_subgroups = [(frozenset(record['members']), record['representative'])
                        for record in sub['all_subgroups']]
    counts = [None]*len(reps)
    whole = next(i for i, H in enumerate(reps) if len(H) == G.size)
    boundary_order = [abs(a)-22 for a in surface['final_boundary_word']]
    assert all(a < 0 for a in surface['final_boundary_word'])
    for ri, H in sorted(enumerate(reps), key=lambda pair: len(pair[1])):
        K = {g for g in H if outer[g] == 0}
        remainder, relative = set(H), []
        while remainder:
            g = min(remainder)
            cls = {G.conjugate(h, g) for h in K}
            remainder -= cls
            relative.append(cls)
        representatives = list(map(min, relative))
        identity_class = next(i for i, cls in enumerate(relative) if G.one in cls)
        cosets = [[g for g in H if outer[g] == value] for value in range(4)]
        kernels = {}
        for r, s in product(range(4), repeat=2):
            distribution = Counter(G.commutator(x, y) for x in cosets[r] for y in cosets[s])
            assert set(distribution) <= K
            assert all(len({distribution[g] for g in cls}) == 1 for cls in relative)
            kernels[r, s] = [distribution[g] for g in representatives]
        size = len(relative)
        # Sparse target structure constants: each ordered pair of classes
        # contributes to a small number of classes of the forced outer bit.
        structure = [[[(k, value) for k, g in enumerate(representatives)
                       if (value := sum(G.mul[G.inv[x]][g] in right for x in left))]
                      for right in relative] for left in relative]

        def multiply(u, v):
            out = [0]*size
            for i, a in enumerate(u):
                if a:
                    for j, b in enumerate(v):
                        if b:
                            scalar = a*b
                            for k, coefficient in structure[i][j]:
                                out[k] += scalar*coefficient
            return out

        one = [int(i == identity_class) for i in range(size)]
        handle_products = []
        for j in range(5):
            value = one
            for r, s in surface['handle_outer_characters'][j]:
                value = multiply(value, kernels[r, s])
            handle_products.append(value)
        boundary_vectors = [[int(g in cls) for g in representatives] for cls in classes]
        hom_counts = []
        for problem in problems:
            row = []
            for j in range(5):
                value = handle_products[j]
                for index in boundary_order:
                    value = multiply(value, boundary_vectors[inverse_class[problem[j][index]]])
                row.append(value[identity_class])
            hom_counts.append(row)
        contained = Counter(rj for L, rj in actual_subgroups if L < H)
        epi = [[value-sum(multiplicity*counts[rj]['epimorphism_counts'][pi][j]
                          for rj, multiplicity in contained.items())
                for j, value in enumerate(row)] for pi, row in enumerate(hom_counts)]
        assert all(value >= 0 for row in epi for value in row)
        counts[ri] = {'order': len(H), 'relative_class_representatives': representatives,
                      'all_counts': hom_counts, 'proper_subgroup_multiplicities': dict(contained),
                      'epimorphism_counts': epi}
        nonconstant = sum(len(set(row)) > 1 for row in epi)
        print('Subgroup representative', ri, 'order', len(H), 'nonconstant five-power rows', nonconstant, flush=True)
    whole_counts = counts[whole]['epimorphism_counts']
    witnesses = []
    for pi, (profile, row) in enumerate(zip(profiles, whole_counts)):
        stabilizer = [o for o in range(4) if all(outer_action[o][ci] == ci for ci in profile)]
        denominator = 360*len(stabilizer)
        assert all(value % denominator == 0 for value in row)
        kernel_counts = [value//denominator for value in row]
        if len(set(row)) > 1:
            witnesses.append({'profile': profile, 'epimorphism_counts': row,
                              'global_outer_stabilizer': stabilizer,
                              'distinct_kernel_counts': kernel_counts,
                              'boundary_class_rows': problems[pi]})
            print('NONCONSTANT', profile, 'counts', row, 'kernels', kernel_counts, flush=True)
    payload = {'status': 'PASS_EXACT_A6_NONTRIVIAL_BOUNDARY_SEARCH',
               'profiles': profiles, 'boundary_profiles_for_each_power': problems,
               'source_surface_file': args.surface.name,
               'additional_fixed_boundary_flip': {'boundary': args.boundary_flip, 'outer': args.flip_outer},
               'subgroup_counts': counts, 'whole_group_representative': whole,
               'whole_group_epimorphism_counts': whole_counts,
               'nonconstant_rows': witnesses,
               'scope': 'The75 uniformly transported three-profile boundary families with every actual local conjugator and all proper images. No claim about other boundary patterns.'}
    HERE.joinpath(args.prefix+'.json').write_text(json.dumps(payload, indent=2)+'\n')
    print('Nonconstant generating-count rows:', len(witnesses), 'of75', flush=True)
    print(payload['status'])


if __name__ == '__main__':
    main()
