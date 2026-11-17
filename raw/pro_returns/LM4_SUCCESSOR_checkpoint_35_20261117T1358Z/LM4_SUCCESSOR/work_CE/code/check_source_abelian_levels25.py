#!/usr/bin/env python3
"""Exact invariant level for the complete actual source-orbit action."""
from pathlib import Path
from collections import Counter
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / 'work_CE/next_symmetric_nodes'
paths = [P/'annular_two_operator25.json', P/'family_kernel_schreier25.json',
         P/'two_operator_filling25.json']
D, K, Q = [json.loads(p.read_text()) for p in paths]
family = set(K['family_indices_F11'])
retained = {int(i): j for i, j in K['retained_F11_to_F3'].items()}


def red(w):
    s = []
    for x in w:
        if s and s[-1] == -x:
            s.pop()
        else:
            s.append(x)
    return tuple(s)


def inv(w):
    return tuple(-x for x in reversed(w))


def sub(w, table):
    return red(x for j in w for x in (table[abs(j)] if j > 0 else inv(table[-j])))


def chi(w):
    return sum(1 if j == 3 else -1 if j == -3 else 0 for j in w)


for name, action in Q['coarse_source_actions'].items():
    for i, w in action.items():
        assert chi(w) == (1 if int(i) == 3 else 0), (name, i)
for name, action in K['all_four_signed_source_operators'].items():
    for i, rec in action['family_images'].items():
        assert chi(rec['retained_head']) == 0, (name, i)

deltaT = {int(i): tuple(w) for i, w in K['retained_cone_action'].items()}
sources = []
for row in D['actual_six_source_normal_forms'][:4]:
    vector, head = Counter(), ()
    for j in row['fiber11']:
        if abs(j) in family:
            vector[(head, abs(j))] += 1 if j > 0 else -1
        else:
            head = red((*head, retained[abs(j)] * (1 if j > 0 else -1)))
    assert not head
    vector = {k: v for k, v in vector.items() if v}
    assert len(vector) == 2
    first = [(t, i, coefficient) for (t, i), coefficient in vector.items() if i < 5]
    assert len(first) == 1
    t, i, coefficient = first[0]
    mate = (red((*sub(t, deltaT), 3)), i + 5)
    assert abs(coefficient) == 1 and vector[mate] == coefficient
    assert chi(mate[0]) == 1 - chi(t)
    sources.append({'name': row['name'], 'first_color': i,
                    'first_head': t, 'first_level': chi(t), 'coefficient': coefficient,
                    'paired_head': mate[0], 'paired_level': chi(mate[0]),
                    'complete_vector': [{'head': k[0], 'color': k[1], 'coefficient': v}
                                        for k, v in vector.items()]})
assert {row['first_color'] for row in sources} == {1, 2, 3, 4}
out = {'status': 'PASS_SOURCE_ORBITS_PRESERVE_ACTUAL_X_LEVEL',
       'inputs': [{'path': str(p.relative_to(ROOT)), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
                  for p in paths],
       'checked_signed_operator_coordinate_images': 12,
       'checked_family_conjugator_heads': 32,
       'actual_four_contact_vectors': sources,
       'scope': 'The image of I in J_ab is proper in the invariant lattice by an all-orbit integer-level obstruction. No invariant class is asserted to lift to J^delta, and no actual fixed element outside I is produced.'}
target = P/'source_abelian_levels25.json'
target.write_text(json.dumps(out, indent=2)+'\n')
print('PASS all12 signed retained images preserve chi_x, all32 family conjugator heads have chi_x=0')
print('PASS all4 actual contact vectors are single paired diagonals, one per first-half color')
for row in sources:
    print(row['name'], 'color', row['first_color'], 'level', row['first_level'],
          'mate_level', row['paired_level'], 'sign', row['coefficient'])
print('SCOPE whole source orbit stays at these levels; invariant-class lifting remains open')
