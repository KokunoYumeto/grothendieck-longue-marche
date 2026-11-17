#!/usr/bin/env python3
"""Literal commuting diagrams from the complete two-operator input to B119."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / 'work_CE/next_symmetric_nodes/annular_two_operator25.json'
D = json.loads(PATH.read_text())


def red(w):
    a = []
    for x in w:
        if a and a[-1] == -x:
            a.pop()
        else:
            a.append(x)
    return tuple(a)


def inv(w):
    return tuple(-x for x in reversed(w))


def sub(w, mapping):
    return red(x for j in w for x in (mapping[abs(j)] if j > 0 else inv(mapping[-j])))


def conj(u, w):
    return red((*u, *w, *inv(u)))


fill = {i: () for i in range(1, 12)}
fill.update({5: (1,), 10: (2,), 11: (3,)})
am = {1: (-1, 2, 1), 2: (1,), 3: (3, -2, 1)}
ami = {1: (2,), 2: (2, 1, -2), 3: (3, 1, -2)}
ap = {1: (1, 3, 2, -3, -1), 2: (2, -3, 1, 3, -2), 3: (1, 3, -2)}
api = {1: (3, 2, -3), 2: (-3, 1, 3), 3: (3, -2, -3, 1, 3)}
av = {i: conj((-1,), ap[i]) for i in range(1, 4)}
avi = {i: sub(conj((1,), (i,)), api) for i in range(1, 4)}
delta = {1: (3, 2, -3), 2: (3, 1, -3), 3: (-3,)}
expected = {'m': am, 'm_inverse': ami, 'v': av, 'v_inverse': avi}
for name, action in D['source_ordinary_actions'].items():
    A = {int(i): tuple(w) for i, w in action.items()}
    for i in range(1, 12):
        assert sub(A[i], fill) == sub(fill[i], expected[name]), (name, i)
for i, w in D['selected_plus_involution'].items():
    assert sub(w, fill) == sub(fill[int(i)], delta)
for node in D['all20_orbifold_node_relations']:
    for w in node['ordinary_two_sheets']:
        assert not sub(w, fill)
assert sub(D['actual_source_v_correction_fiber11'], fill) == (-1,)
for row in D['actual_six_source_normal_forms'][:4]:
    assert not sub(row['fiber11'], fill)
for name, inverse in (('m', 'm_inverse'), ('v', 'v_inverse')):
    for i in range(1, 4):
        assert sub(expected[name][i], expected[inverse]) == (i,)
        assert sub(expected[inverse][i], expected[name]) == (i,)
for action in (am, ami, av, avi):
    for i in range(1, 4):
        assert sub(delta[i], action) == sub(action[i], delta)

out = {'status': 'PASS_COMPLETE_TWO_OPERATOR_TO_COARSE_DIAGRAMS',
       'input': {'path': str(PATH.relative_to(ROOT)),
                 'sha256': hashlib.sha256(PATH.read_bytes()).hexdigest()},
       'filling_F11_to_F3': fill, 'coarse_source_actions': expected,
       'coarse_selected_plus_involution': delta,
       'counts': {'signed_operator_diagrams': 44, 'cone_diagrams': 11,
                  'node_words_killed': 40, 'contact_words_killed': 4},
       'scope': 'All actual family-kernel and source/filling maps commute literally. No fixed-element lifting or family-kernel freeness is claimed.'}
target = ROOT / 'work_CE/next_symmetric_nodes/two_operator_filling25.json'
target.write_text(json.dumps(out, indent=2) + '\n')
print('PASS all44 signed source-operator filling diagrams and all11 selected-cone diagrams')
print('PASS all40 node seeds and all4 contact source words vanish under the actual family filling')
print('PASS literal source correction q maps to f^-1; coarse source v is f^-1 p')
print('PASS all12 inverse source-action comparisons and all12 coarse cone commutations')
print('OUTPUT', target.relative_to(ROOT))
