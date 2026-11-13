#!/usr/bin/env python3
"""Exact proper Nielsen orbit counts in the two split (6,8,8) profiles.

Fix the first literal automorphism.  Its inner centralizer acts on the
remaining finite pairs, and its orbits identify exactly the simultaneous
Inn(A6)-conjugacy classes.  Every generated subgroup order and every
orbit is saved; no weak count is substituted for a proper count.
"""

from collections import Counter
from pathlib import Path
import importlib.util
import json

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('finite_count', HERE/'a_peripheral_count.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def main():
    raw = json.loads(HERE.joinpath('a_peripheral_a6_outer.json').read_text())
    pairs = [tuple(p) for p in raw['automorphism_generator_pairs']]
    maps = {p: tuple(v) for p, v in zip(pairs, raw['automorphism_maps'])}
    x, y = raw['A6_generators']
    E = module.Group('Aut(A6)', pairs,
                     lambda a, b: (maps[a][b[0]], maps[a][b[1]]), (x, y))
    inner = frozenset(raw['inner_indices'])
    classes = [frozenset(c) for c in raw['relative_classes']]
    u = min(classes[0])
    cent = {g for g in inner if E.conjugate(g, u) == u}
    class_size = len(classes[0])
    assert len(cent)*class_size == 360 and E.orders[u] == 6
    records = []
    for third_class in (5, 9):
        valid = {v for v in classes[7] if E.inv[E.mul[u][v]] in classes[third_class]}
        unseen, orbits = set(valid), []
        while unseen:
            v = min(unseen)
            orbit = {E.conjugate(g, v) for g in cent}
            assert orbit <= valid
            unseen -= orbit
            subgroup = E.generated([u, v])
            orbits.append({'representative': [u, v, E.inv[E.mul[u][v]]],
                           'fixed_first_orbit': sorted(orbit),
                           'generated_order': len(subgroup),
                           'generated_subgroup': sorted(subgroup)})
        full_counts = Counter()
        for orb in orbits:
            full_counts[orb['generated_order']] += class_size*len(orb['fixed_first_orbit'])
        proper = [r for r in orbits if r['generated_order'] == 1440]
        assert all(len(r['fixed_first_orbit']) == len(cent) for r in proper)
        record = {'profile': [0, 7, third_class], 'fixed_first': u,
                  'inner_centralizer': sorted(cent), 'orbits': orbits,
                  'all_weak_count': class_size*len(valid),
                  'proper_count': 360*len(proper),
                  'proper_orbit_representatives': [r['representative'] for r in proper],
                  'full_counts_by_image_order': dict(full_counts)}
        records.append(record)
        print('Profile', record['profile'], 'weak', record['all_weak_count'],
              'proper', record['proper_count'], 'proper orbits', len(proper),
              'image-order counts', dict(full_counts))
    payload = {'status': 'PASS_A6_EXACT_PROPER_NIELSEN_COUNTS', 'profiles': records}
    HERE.joinpath('a_peripheral_a6_nielsen.json').write_text(json.dumps(payload, indent=2)+'\n')
    print(payload['status'])


if __name__ == '__main__':
    main()
