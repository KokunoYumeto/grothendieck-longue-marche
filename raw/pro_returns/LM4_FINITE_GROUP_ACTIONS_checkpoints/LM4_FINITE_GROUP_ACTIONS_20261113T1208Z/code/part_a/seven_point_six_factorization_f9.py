#!/usr/bin/env python3
"""Exact labels for all 24 six-point maps factoring through the 12 seven-maps.

The topological map is literal forgetting of the other fixed pole.
Its profinite version is the functorial completion of the same map.
"""
import contextlib
import io
import json
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    import a5_centralizer_permutations as a

rows = []
six_seen = set()
seven_seen = set()
for K in sorted(a.five_subgroups,key=lambda H:sorted(H)):
    generator = min(K-{a.one})
    permutation = a.vertex_action(generator)
    poles = [i for i in range(12) if permutation[i] == i]
    assert len(poles) == 2
    remaining = set(range(12))-set(poles)
    orbits = []
    while remaining:
        first = min(remaining)
        orbit = [first]
        j = permutation[first]
        while j != first:
            orbit.append(j)
            j = permutation[j]
        assert len(orbit) == 5
        remaining.difference_update(orbit)
        orbits.append(orbit)
    assert len(orbits) == 2
    for orbit in orbits:
        seven = frozenset(poles+orbit)
        assert seven in a.seven_point_sets
        assert seven not in seven_seen
        seven_seen.add(seven)
        for pole in poles:
            six = frozenset([pole]+orbit)
            omitted = (set(poles)-{pole}).pop()
            assert seven-{omitted} == six
            assert six in a.six_point_sets
            assert six not in six_seen
            six_seen.add(six)
            seven_labels = sorted(seven)
            six_labels = sorted(six)
            rows.append({
                'C5_generator':list(generator),
                'fixed_poles':poles,
                'selected_five_cycle':orbit,
                'seven_labels':seven_labels,
                'six_labels':six_labels,
                'forgotten_pole':omitted,
                'six_positions_in_the_seven_tuple':
                    [seven_labels.index(i) for i in six_labels],
            })
assert len(rows) == 24
assert seven_seen == a.seven_point_sets
assert six_seen == a.six_point_sets
assert all(sum(row['seven_labels'] == sorted(K) for row in rows) == 2
           for K in seven_seen)
result = {
    'claim':'F.9',
    'seven_point_maps':12,
    'six_point_maps':24,
    'exact_label_forgetting_factorizations':rows,
    'map_identity':'f_J = forget_(K_to_J) composed with f_K; J is obtained from K by deleting the other C5-fixed pole.',
    'discrete_kernel_equality':'intersection over all 36 kernels = intersection over the 12 seven-point kernels',
    'completed_kernel_equality':'The same equality holds for the full profinite completions, by functoriality of the displayed forgetting maps.',
    'F9_word_consequence':'The exact F9 word and its full procyclic closure lie in all 36 kernels.',
    'all_assertions_passed':True,
}
Path(__file__).with_name('seven_point_six_factorization_f9_output.json').write_text(
    json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
