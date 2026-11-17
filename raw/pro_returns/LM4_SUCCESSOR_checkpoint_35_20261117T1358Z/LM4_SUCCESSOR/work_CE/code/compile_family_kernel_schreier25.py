#!/usr/bin/env python3
"""Complete marked node factors and uniform family-kernel operator data.

No source orbit is enumerated. Every infinite basis label is retained as a
literal retained F3 word, and every nonlinear conjugator is retained.
"""
from pathlib import Path
import json
import hashlib

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / 'work_CE/next_symmetric_nodes/annular_two_operator25.json'
D = json.loads(PATH.read_text())
CONES = (6, 7)
FAMILY = (1, 2, 3, 4, 6, 7, 8, 9)
RETAINED = {5: 1, 10: 2, 11: 3}
RETAINED_BACK = {1: (5,), 2: (10,), 3: (11,)}


def red(w, cones=()):
    a = []
    for x in w:
        if abs(x) in cones:
            x = abs(x)
        if a and (a[-1] == -x or x in cones and a[-1] == x):
            a.pop()
        else:
            a.append(x)
    return tuple(a)


def inv(w, cones=()):
    return red((-x for x in reversed(w)), cones)


def sub(w, table, cones=()):
    return red((x for j in w for x in
                (table[abs(j)] if j > 0 else inv(table[-j], cones))), cones)


def conj(a, b, cones=()):
    return red((*a, *b, *inv(a, cones)), cones)


def comm(a, b, cones=()):
    return red((*a, *b, *inv(a, cones), *inv(b, cones)), cones)


def ordinary(w, state=0):
    out = []
    for j in red(w, CONES):
        if j == 6:
            state ^= 1
        elif j == 7:
            out.append(11 if state == 0 else -11)
            state ^= 1
        else:
            out.append((abs(j) + 5 * state) * (1 if j > 0 else -1))
    assert state == 0
    return red(out)


def kred(word):
    out = []
    for sign, head, family in word:
        letter = (sign, tuple(head), family)
        if out and out[-1] == (-sign, tuple(head), family):
            out.pop()
        else:
            out.append(letter)
    return tuple(out)


def kinv(word):
    return tuple((-s, t, i) for s, t, i in reversed(word))


def kernel_rewrite(word):
    out, head = [], ()
    for j in word:
        if abs(j) in FAMILY:
            out.append((1 if j > 0 else -1, head, abs(j)))
        else:
            head = red((*head, RETAINED[abs(j)] * (1 if j > 0 else -1)))
    return kred(out), head


def expand(word, head=()):
    result = []
    for sign, t, family in word:
        result.extend(conj(sub(t, RETAINED_BACK), (sign * family,)))
    result.extend(sub(head, RETAINED_BACK))
    return red(result)


def peel(word):
    word = red(word)
    prefix = []
    while len(word) > 1 and word[0] == -word[-1]:
        prefix.append(word[0])
        word = word[1:-1]
    assert len(word) == 1 and abs(word[0]) in FAMILY, word
    return tuple(prefix), word[0]


def peripheral_record(word):
    conjugator, core = peel(word)
    n, t = kernel_rewrite(conjugator)
    assert expand(n, t) == conjugator
    actual, head = kernel_rewrite(word)
    assert not head
    target = kred((*n, (1 if core > 0 else -1, t, abs(core)), *kinv(n)))
    assert actual == target
    assert expand(actual) == red(word)
    return {'word_F11': word, 'conjugator_F11': conjugator, 'signed_core': core,
            'kernel_conjugator': n, 'retained_head': t, 'kernel_word': actual}


local_pairs = {}
for name, i in (('a', 1), ('b', 2), ('d', 3), ('e', 4)):
    local_pairs['diagonal_' + name] = ((i,), (6, i, 6))
local_pairs.update({'pair_ab': ((1,), (2,)),
                   'pair_bara_d': ((6, 1, 6), (3,)),
                   'pair_bara_e': ((6, 1, 6), (4,)),
                   'pair_d_bare': ((3,), (6, 4, 6)),
                   'pair_b_hdh': ((2,), (5, 3, -5)),
                   'pair_b_heh': ((2,), (5, 4, -5))})
outward = {side: {int(i): tuple(w) for i, w in D[side + '_local_to_global'].items()}
           for side in ('minus', 'plus')}
nodes = []
for row in D['all20_orbifold_node_relations']:
    local_u, local_v = local_pairs[row['name']]
    u = sub(local_u, outward[row['side']], CONES)
    v = sub(local_v, outward[row['side']], CONES)
    assert comm(u, v, CONES) == tuple(row['orbifold_fiber7'])
    for sheet in (0, 1):
        us = ordinary(conj((6,) if sheet else (), u, CONES))
        vs = ordinary(conj((6,) if sheet else (), v, CONES))
        assert comm(us, vs) == tuple(row['ordinary_two_sheets'][sheet])
        pu, pv = peripheral_record(us), peripheral_record(vs)
        chain, head = kernel_rewrite(comm(us, vs))
        assert not head and expand(chain) == comm(us, vs)
        expected = kred((*pu['kernel_word'], *pv['kernel_word'],
                         *kinv(pu['kernel_word']), *kinv(pv['kernel_word'])))
        assert chain == expected
        nodes.append({'side': row['side'], 'name': row['name'], 'sheet': sheet,
                      'first_factor': pu, 'second_factor': pv, 'kernel_relator': chain})

operators = {}
for name, table in D['source_ordinary_actions'].items():
    A = {int(i): tuple(w) for i, w in table.items()}
    family = {i: peripheral_record(A[i]) for i in FAMILY}
    retained = {}
    for i in RETAINED:
        word, head = kernel_rewrite(A[i])
        assert expand(word, head) == A[i]
        retained[i] = {'word_F11': A[i], 'kernel_correction': word, 'retained_head': head}
    operators[name] = {'family_images': family, 'retained_images': retained}

delta = {int(i): tuple(w) for i, w in D['selected_plus_involution'].items()}
delta_T = {1: (3, 2, -3), 2: (3, 1, -3), 3: (-3,)}
for i in RETAINED:
    word, head = kernel_rewrite(delta[i])
    assert not word and head == delta_T[RETAINED[i]]
for i in FAMILY:
    mate = i + 5 if i < 5 else i - 5
    assert delta[i] == (11, mate, -11)

# Finite exact cross-check of the uniform delta formula on every label actually
# occurring in the complete input. Its all-label proof is in the companion note.
labels = {(tuple(t), i) for row in nodes for s, t, i in row['kernel_relator']}
for row in operators.values():
    for rec in row['family_images'].values():
        labels.add((tuple(rec['retained_head']), abs(rec['signed_core'])))
for t, i in labels:
    actual = sub(conj(sub(t, RETAINED_BACK), (i,)), delta)
    mate = i + 5 if i < 5 else i - 5
    target_t = red((*sub(t, delta_T), 3))
    target = conj(sub(target_t, RETAINED_BACK), (mate,))
    assert actual == target

out = {'status': 'PASS_COMPLETE_FAMILY_KERNEL_FACTORS_AND_UNIFORM_OPERATOR_INPUT',
       'input': {'path': str(PATH.relative_to(ROOT)),
                 'sha256': hashlib.sha256(PATH.read_bytes()).hexdigest()},
       'family_indices_F11': FAMILY, 'retained_F11_to_F3': RETAINED,
       'all40_node_factor_pairs': nodes, 'all_four_signed_source_operators': operators,
       'retained_cone_action': delta_T, 'checked_actual_labels': len(labels),
       'counts': {'node_relators': 40, 'peripheral_node_factors': 80,
                  'signed_operator_family_images': 32, 'signed_retained_images': 12},
       'scope': 'Every node is a commutator of two explicitly conjugated Schreier vertices. All nonlinear kernel conjugators are retained. This is not a graph-product presentation: one simultaneous all-orbit change eliminating those conjugators remains unproved.'}
target = ROOT / 'work_CE/next_symmetric_nodes/family_kernel_schreier25.json'
target.write_text(json.dumps(out, indent=2) + '\n')
print('PASS all20 orbifold node factor pairs and both ordinary sheets, with literal commutator words')
print('PASS all80 node factors are conjugates of individual actual family basis letters')
print('PASS all40 complete kernel rewrites and full F11 expansion round trips')
print('PASS all32 signed source peripheral images and all12 retained correction words')
print('PASS literal delta-equivariant retained section and paired Schreier basis formula')
print('PASS actual-label delta checks', len(labels))
print('SOURCE_CORE_MAPS', {name: {i: rec['signed_core'] for i, rec in row['family_images'].items()}
                           for name, row in operators.items()})
print('OUTPUT', target.relative_to(ROOT))
print('SCOPE no simultaneous untwisting or graph-product assertion; all source/deck translates required')
