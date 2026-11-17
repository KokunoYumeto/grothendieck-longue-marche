#!/usr/bin/env python3
"""Exact generic F11/two-source-operator reduction of the actual whole neck.

Only immutable JSON inputs are read. All node relations and both ordinary
sheets are retained. No orbit truncation or quotient word oracle is used.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / 'work_CE/next_symmetric_nodes'
INPUT = DATA / 'annular_neck_presentation23.json'
ORDINARY = DATA / 'annular_ordinary13_24.json'
G = json.loads(INPUT.read_text())
Q = json.loads(ORDINARY.read_text())
CONES = (6, 7)


def red(w, cones=()):
    out = []
    for x in w:
        if abs(x) in cones:
            x = abs(x)
        if out and (out[-1] == -x or x in cones and out[-1] == x):
            out.pop()
        else:
            out.append(x)
    return tuple(out)


def inv(w, cones=()):
    return red((-x for x in reversed(w)), cones)


def cat(*words, cones=()):
    return red((x for w in words for x in w), cones)


def sub(w, mapping, cones=()):
    return red((x for j in w for x in
                (mapping[abs(j)] if j > 0 else inv(mapping[-j], cones))), cones)


def conj(a, w, cones=()):
    return cat(a, w, inv(a, cones), cones=cones)


ID = {i: (i,) for i in range(1, 8)}
eta = {int(j): tuple(w) for j, w in G['eta_in_common_K'].items()}
gauge = {int(j): tuple(w) for j, w in Q['selected_cone_old_to_new'].items()}

# Global fiber: (a,B,d,e,f,c,tau); local fiber:
# (a_local,b_local,d_local,e_local,f_local,C_local,other_gap_cone).
Cminus = (-1, 6, 1)
Cplus = conj(inv(eta[1]), (7,), CONES)
minus_out = {**ID, 2: conj(Cminus, (2,), CONES), 6: Cminus}
minus_in = {**ID, 2: (6, 2, 6), 6: (1, 6, -1)}
plus_out = {i: eta[i] for i in range(1, 6)}
plus_out.update({2: conj(Cplus, eta[2], CONES), 6: Cplus, 7: (6,)})
local_K = {**{i: (i,) for i in range(1, 6)}, 2: (6, 2, 6)}
plus_in = {i: sub(eta[i], local_K, CONES) for i in range(1, 6)}
plus_in.update({6: (7,), 7: (1, 6, -1)})
for outward, inward in ((minus_out, minus_in), (plus_out, plus_in)):
    for i in range(1, 8):
        assert sub(outward[i], inward, CONES) == (i,)
        assert sub(inward[i], outward, CONES) == (i,)

# Conjugation by the far zero lift k: partial Inn(f^-1 C) on <C,f>,
# fixing all four outsiders and the other selected gap cone.
local_action = dict(ID)
local_inverse = dict(ID)
for i in (5, 6):
    local_action[i] = conj((-5, 6), (i,), CONES)
    local_inverse[i] = conj((6, 5), (i,), CONES)
for i in range(1, 8):
    assert sub(local_action[i], local_inverse, CONES) == (i,)
    assert sub(local_inverse[i], local_action, CONES) == (i,)


def transfer(inward, outward, local):
    return {i: sub(sub(inward[i], local, CONES), outward, CONES)
            for i in range(1, 8)}


am = transfer(minus_in, minus_out, local_action)
ami = transfer(minus_in, minus_out, local_inverse)
ap = transfer(plus_in, plus_out, local_action)
api = transfer(plus_in, plus_out, local_inverse)
for action, inverse in ((am, ami), (ap, api)):
    for i in range(1, 8):
        assert sub(action[i], inverse, CONES) == (i,)
        assert sub(inverse[i], action, CONES) == (i,)
        assert sum(abs(j) in CONES for j in action[i]) % 2 == (i in CONES)
assert am[7] == (7,) and ap[6] == (6,)
assert sub(eta[1], ap, CONES) == eta[1]


def normal(w, actions, fiber_rank, cones=()):
    fiber, head = (), ()
    for j in w:
        if abs(j) <= fiber_rank:
            image = red((j,), cones)
            for h in reversed(head):
                image = sub(image, actions[h], cones)
            fiber = cat(fiber, image, cones=cones)
        else:
            head = cat(head, (j,))
    return fiber, head


far_actions = {8: am, -8: ami, 9: ap, -9: api}
generic_names = {'h_fixes_cone', 'h_swaps_k', 'k_fixes_a', 'k_fixes_b',
                 'k_fixes_d', 'k_fixes_e'}
generic_checks, node_records = [], []
for row in G['regional_relators']:
    w = sub(row['word'], gauge, CONES)
    fiber, head = normal(w, far_actions, 7, CONES)
    assert not head
    if row['name'] in generic_names:
        assert not fiber, row
        generic_checks.append({'side': row['side'], 'name': row['name']})
    else:
        assert fiber
        node_records.append({'side': row['side'], 'name': row['name'],
                             'selected9': w, 'orbifold_fiber7': fiber})
for row in G['cross_relators']:
    assert normal(sub(row['word'], gauge, CONES), far_actions, 7, CONES) == ((), ())
assert len(generic_checks) == 12 and len(node_records) == 20

# Exact ordinary fiber E0^0 = F11; transversal (1,c).
back = {i: (i,) for i in range(1, 6)}
back.update({i + 5: (6, i, 6) for i in range(1, 6)})
back[11] = (7, 6)


def rs(w, state=0):
    out = []
    for j in red(w, CONES):
        if j == 6:
            state ^= 1
        elif j == 7:
            out.append(11 if not state else -11)
            state ^= 1
        else:
            out.append((abs(j) + 5 * state) * (1 if j > 0 else -1))
    return red(out), state


for i in range(1, 12):
    assert rs(back[i]) == ((i,), 0)
    w, end = rs(conj((7,), back[i], CONES))
    assert end == 0
    assert sub(w, back, CONES) == conj((7,), back[i], CONES)
delta = {i: rs(conj((7,), back[i], CONES))[0] for i in range(1, 12)}
for i in range(1, 12):
    assert sub(delta[i], delta) == (i,)


def ordinary(action):
    result = {}
    for i in range(1, 12):
        w, end = rs(sub(back[i], action, CONES))
        assert end == 0
        assert sub(w, back, CONES) == sub(back[i], action, CONES)
        result[i] = w
    return result


am11, ami11, ap11, api11 = map(ordinary, (am, ami, ap, api))

# The actual fixed source lift v=a_+ f_+ p a_+^-1=q p.
q = conj(eta[1], eta[5], CONES)
q11, end = rs(q)
assert end == 0
source_far = []
for row in G['actual_six_source_words']:
    w = sub(row['word'], gauge, CONES)
    fiber, head = normal(w, far_actions, 7, CONES)
    source_far.append({'name': row['name'], 'fiber7': fiber, 'far_head': head})
assert source_far[4]['fiber7'] == q and source_far[4]['far_head'] == (9,)
assert source_far[5]['fiber7'] == () and source_far[5]['far_head'] == (8,)
assert all(not row['far_head'] for row in source_far[:4])
assert normal(conj((7,), cat(q, (9,)), CONES), far_actions, 7, CONES) == (q, (9,))
av = {i: conj(q, ap[i], CONES) for i in range(1, 8)}
avi = {i: sub(conj(inv(q, CONES), (i,), CONES), api, CONES)
       for i in range(1, 8)}
av11, avi11 = map(ordinary, (av, avi))
for action, inverse in ((am11, ami11), (ap11, api11), (av11, avi11)):
    for i in range(1, 12):
        assert sub(action[i], inverse) == sub(inverse[i], action) == (i,)
for action in (am11, ami11, av11, avi11):
    for i in range(1, 12):
        assert sub(delta[i], action) == sub(action[i], delta)

# Keep both ordinary sheets of all twenty orbifold node relators.
for row in node_records:
    records = []
    for state in (0, 1):
        w, end = rs(row['orbifold_fiber7'], state)
        assert end == state
        expected = conj((6,) if state else (), row['orbifold_fiber7'], CONES)
        assert sub(w, back, CONES) == expected
        records.append(w)
    row['ordinary_two_sheets'] = records
    assert sub(records[0], delta) == conj((11,), records[1])
    assert sub(records[1], delta) == conj((11,), records[0])

# Literal all64-row comparison with the independent stable ordinary13 compiler.
# New normal form: fiber1..11, source base12=m,13=v; p=q^-1 v.
source_actions = {12: am11, -12: ami11, 13: av11, -13: avi11}
ordinary13_to_source = {i: (i,) for i in range(1, 11)}
ordinary13_to_source.update({11: (12,), 12: cat(inv(q11), (13,)), 13: (11,)})
by_node = {(row['side'], row['name']): row for row in node_records}
row_comparisons = []
for row in Q['all32_regional_two_sheet_rewrites']:
    for ordinary_row in row['ordinary_rewrites']:
        w = sub(ordinary_row['free13'], ordinary13_to_source)
        result = normal(w, source_actions, 11)
        assert not result[1]
        expected = () if row['name'] in generic_names else \
            by_node[(row['side'], row['name'])]['ordinary_two_sheets'][ordinary_row['state']]
        assert result[0] == expected, (row['name'], ordinary_row['state'])
        row_comparisons.append({'side': row['side'], 'name': row['name'],
                                'state': ordinary_row['state'], 'fiber11': result[0]})
assert len(row_comparisons) == 64
source_words = []
for i, row in enumerate(Q['actual_six_source_words']):
    result = normal(sub(row['ordinary13'], ordinary13_to_source), source_actions, 11)
    if i < 4:
        assert not result[1]
        assert sub(result[0], back, CONES) == source_far[i]['fiber7']
    else:
        assert result == ((), (13,) if i == 4 else (12,))
    source_words.append({'name': row['name'], 'fiber11': result[0], 'source_head': result[1]})

out = {
    'status': 'PASS_EXACT_GENERIC_F11_TWO_SOURCE_OPERATORS_ALL40_NODE_SEEDS',
    'inputs': [{'path': str(p.relative_to(ROOT)), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
               for p in (INPUT, ORDINARY)],
    'fiber7_names': ['a','B','d','e','f','c_minus_gap','tau_plus_gap'],
    'local7_names': ['a_local','b_local','d_local','e_local','f_local','C_local','other_gap_cone'],
    'minus_local_to_global': minus_out, 'minus_global_to_local': minus_in,
    'plus_local_to_global': plus_out, 'plus_global_to_local': plus_in,
    'local_partial_conjugation': local_action, 'local_partial_inverse': local_inverse,
    'far_orbifold_actions': {'m':am,'m_inverse':ami,'p':ap,'p_inverse':api},
    'ordinary_fiber11_to_fiber7': back, 'selected_plus_involution': delta,
    'far_ordinary_actions': {'m':am11,'m_inverse':ami11,'p':ap11,'p_inverse':api11},
    'actual_source_v_correction_fiber7': q, 'actual_source_v_correction_fiber11': q11,
    'source_ordinary_actions': {'m':am11,'m_inverse':ami11,'v':av11,'v_inverse':avi11},
    'all12_generic_relations': generic_checks, 'all20_orbifold_node_relations': node_records,
    'ordinary13_to_source_normal_form': ordinary13_to_source,
    'all64_ordinary_row_comparisons': row_comparisons,
    'actual_six_source_normal_forms': source_words,
    'counts': {'orbifold_nodes':20,'ordinary_node_seeds':40,'full_rows_checked':64,
               'actual_source_words':6,'ordinary_fiber_rank':11,'source_operator_rank':2},
    'scope': 'The full node normal closure uses ALL signed words in the two exact source operators and ordinary fiber conjugation. The finite forty seeds are not asserted to be stable by themselves. This gives a compact exact presentation and the remaining fixed-kernel gate, not fixed-source equality or a simultaneous free-basis theorem.'}
OUTPUT = DATA / 'annular_two_operator25.json'
OUTPUT.write_text(json.dumps(out, indent=2) + '\n')
print('PASS all28 regional-basis inverse substitutions and both local partial-inner inverse maps')
print('PASS all28 global far-action inverse substitutions, ordinary parity, and both actual cross relations')
print('PASS all12 generic regional relations; all20 node relations retained in the genuine free fiber')
print('PASS actual ordinary F11 basis; all66 signed action inverse comparisons')
print('PASS source lift v=q p matches literal stored source and is fixed by the selected plus cone')
print('PASS all44 source-operator/involution commutation identities')
print('PASS all40 complete two-sheet node seeds and exact cone-mate conjugacies')
print('PASS all64 stable ordinary13 rows compare literally with the compact operator presentation')
print('PASS all6 actual source normal forms: four fiber contacts, v, m')
print('OUTPUT', OUTPUT.relative_to(ROOT))
print('SCOPE all signed operator translates remain required; unfilled fixed-source equality remains open')
