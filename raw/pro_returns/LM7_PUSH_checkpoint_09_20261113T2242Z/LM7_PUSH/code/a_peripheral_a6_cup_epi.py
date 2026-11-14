#!/usr/bin/env python3
"""Exhaustive proper-image subtraction for the Aut(A6) cup test.

The companion C++ program enumerates every subgroup surjecting onto the
actual V4 quotient.  We verify its subgroup and adjoining certificates,
then use exact integer class-algebra convolution and subgroup subtraction.
"""

from collections import Counter
from itertools import product
from pathlib import Path
import importlib.util
import json
import struct
import subprocess

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
    outer = raw['outer_coordinates']
    table_path = HERE/'a_peripheral_a6_outer_table.bin'
    numbers = [G.size, G.one]+G.inv+outer+[g for row in G.mul for g in row]
    table_path.write_bytes(struct.pack('<'+'H'*len(numbers), *numbers))
    binary = HERE/'a_peripheral_a6_outer_subgroups'
    subprocess.run(['g++', '-O3', '-std=c++17', str(HERE/'a_peripheral_a6_outer_subgroups.cpp'),
                    '-o', str(binary)], check=True)
    subgroup_path = HERE/'a_peripheral_a6_outer_subgroups.json'
    with (HERE/'a_peripheral_a6_outer_subgroups.out').open('w') as log:
        subprocess.run([str(binary), str(table_path), str(subgroup_path)],
                       stdout=log, stderr=log, check=True)
    sub = json.loads(subgroup_path.read_text())
    assert sub['status'] == 'PASS_EXHAUSTIVE_OUTER_SURJECTIVE_SUBGROUPS'
    reps = [frozenset(record['members']) for record in sub['representatives']]
    all_subgroups = [(frozenset(record['members']), record['representative'])
                     for record in sub['all_subgroups']]
    subgroup_index = {H: j for H, j in all_subgroups}
    assert len(subgroup_index) == len(all_subgroups)
    for record, H in zip(sub['representatives'], reps):
        assert G.generated(record['generators']) == H
        assert {outer[g] for g in H} == {0, 1, 2, 3}
    # Complete actual conjugacy orbits, with literal source generators.
    for record in sub['all_subgroups']:
        H = frozenset(record['members'])
        assert G.generated(record['generators']) == H
        assert len(H) == len(reps[record['representative']])
    # Independently verify the finite closure under adjoining all inner
    # elements.  Seed exhaustiveness is the C++ full pair loop together
    # with these actual inner-conjugacy representatives.
    inner = [g for g in range(G.size) if outer[g] == 0]
    seed_classes = [{G.conjugate(h, x) for h in inner}
                    for x in sub['first_inner_class_representatives']]
    assert set().union(*seed_classes) == {g for g in range(G.size) if outer[g] == 1}
    assert sum(map(len, seed_classes)) == 360
    for record, H in zip(sub['representatives'], reps):
        for g in inner:
            if g not in H:
                assert G.generated(record['generators']+[g]) in subgroup_index
    print('Verified complete full-outer subgroup family:', len(reps), 'conjugacy classes,',
          len(all_subgroups), 'actual subgroups', flush=True)
    print('Subgroup order histogram:', dict(sorted(Counter(len(H) for H, j in all_subgroups).items())), flush=True)

    genus_list = list(range(2, 7))
    counts = [None]*len(reps)
    for ri, H in sorted(enumerate(reps), key=lambda pair: len(pair[1])):
        K = {g for g in H if outer[g] == 0}
        remaining, classes = set(K), []
        while remaining:
            g = min(remaining)
            cls = {G.conjugate(h, g) for h in K}
            remaining -= cls
            classes.append(cls)
        representatives = list(map(min, classes))
        identity_class = next(i for i, cls in enumerate(classes) if G.one in cls)
        cosets = [[g for g in H if outer[g] == value] for value in range(4)]
        kernels = {}
        for r, s in ((0, 0), (1, 0), (2, 0), (1, 2)):
            distribution = Counter(G.commutator(x, y) for x in cosets[r] for y in cosets[s])
            assert set(distribution) <= K
            assert all(len({distribution[g] for g in cls}) == 1 for cls in classes)
            kernels[r, s] = [distribution[g] for g in representatives]
        size = len(classes)
        structure = [[[sum(G.mul[G.inv[x]][g] in right for x in left)
                       for g in representatives] for right in classes] for left in classes]

        def multiply(u, v):
            return [sum(u[i]*v[j]*structure[i][j][k]
                        for i in range(size) for j in range(size) if u[i] and v[j])
                    for k in range(size)]

        one = [int(i == identity_class) for i in range(size)]
        powers = [one]
        for _ in range(max(genus_list)-1):
            powers.append(multiply(powers[-1], kernels[0, 0]))
        cup0_start = multiply(kernels[1, 0], kernels[2, 0])
        all_counts = []
        for genus in genus_list:
            c0 = multiply(cup0_start, powers[genus-2])[identity_class]
            c1 = multiply(kernels[1, 2], powers[genus-1])[identity_class]
            all_counts.append([c0, c1])
        contained = Counter(j for L, j in all_subgroups if L < H)
        epimorphisms = [[value-sum(multiplicity*counts[j]['epimorphism_counts'][gi][type_]
                                  for j, multiplicity in contained.items())
                        for type_, value in enumerate(row)]
                       for gi, row in enumerate(all_counts)]
        assert all(value >= 0 for row in epimorphisms for value in row)
        counts[ri] = {'order': len(H), 'inner_kernel_order': len(K),
                      'inner_class_representatives': representatives,
                      'inner_classes': [sorted(cls) for cls in classes],
                      'commutator_vectors': {str(pair): value for pair, value in kernels.items()},
                      'all_counts': all_counts,
                      'proper_subgroup_multiplicities': dict(contained),
                      'epimorphism_counts': epimorphisms,
                      'differences_cup0_minus_cup1': [row[0]-row[1] for row in epimorphisms]}
        print('Representative', ri, 'order', len(H), 'epi differences g2..6',
              counts[ri]['differences_cup0_minus_cup1'], flush=True)
    whole = next(i for i, H in enumerate(reps) if len(H) == G.size)
    result = counts[whole]
    assert all(value % G.size == 0 for row in result['epimorphism_counts'] for value in row)
    print('Aut(A6) exact generating counts:', result['epimorphism_counts'], flush=True)
    payload = {'status': 'PASS_EXACT_AUT_A6_FIXED_OUTER_EPIMORPHISM_COUNTS',
               'genera': genus_list, 'full_group_representative': whole,
               'subgroup_class_count': len(reps), 'actual_subgroup_count': len(all_subgroups),
               'subgroup_order_histogram': dict(sorted(Counter(len(H) for H, j in all_subgroups).items())),
               'representative_counts': counts,
               'AutA6_epimorphism_counts': result['epimorphism_counts'],
               'AutA6_differences': result['differences_cup0_minus_cup1'],
               'scope': 'Exact surface generating counts for the two rank-two V4-character cup types; all proper images are subtracted.'}
    HERE.joinpath('a_peripheral_a6_cup_epi.json').write_text(json.dumps(payload, indent=2)+'\n')
    print(payload['status'])


if __name__ == '__main__':
    main()
