#!/usr/bin/env python3
"""Actual fixed-cone source peripherals, independently from the HNN proof.

The input is the complete based six-strand record.  This checker uses its
literal positive-push words, not a numerical or unbased meridian choice.
The geometric Borel-strip identification is proved in the companion note.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "work_CE/next_symmetric_nodes/inner_bad_orbifold_words22.json"
NORM = ROOT / "records/inner_bad_normalized22.json"
HNN = ROOT / "records/inner_bad_hnn22.json"
OUT = Path(__file__).with_name("inner_fixed_source22.json")
D, C, H = [json.loads(p.read_text()) for p in (RAW, NORM, HNN)]

def red(w):
    ans = []
    for x in w:
        x = 2 if abs(x) == 2 else int(x)
        if ans and (ans[-1] == -x or ans[-1] == x == 2):
            ans.pop()
        else:
            ans.append(x)
    return tuple(ans)

def mul(*ws):
    return red(x for w in ws for x in w)

def inv(w):
    return red(-x for x in reversed(w))

def sub(w, images):
    return mul(*(images[abs(x)] if x > 0 else inv(images[-x]) for x in w))

def conj(g, w):
    return mul(g, w, inv(g))

def free_red(w):
    ans = []
    for x in w:
        if ans and ans[-1] == -x:
            ans.pop()
        else:
            ans.append(x)
    return tuple(ans)

def cone_conjugator(w):
    """Unique orientation-even conjugator of c in C2(c)*F5."""
    core = list(red(w))
    v = []
    while len(core) > 1 and (core[0] == -core[-1]
                            or core[0] == core[-1] == 2):
        v.append(core.pop(0))
        core.pop()
    assert core == [2]
    raw_v = tuple(v)
    if sum(x == 2 for x in v) % 2:
        v.append(2)
    v = red(v)
    assert sum(x == 2 for x in v) % 2 == 0
    assert conj(v, (2,)) == red(w)
    return raw_v, v

# Ordinary index-two free basis: a,b,d,e,f and their cone conjugates.
positions = {1: 1, 3: 2, 4: 3, 5: 4, 6: 5}
def ordinary(w):
    parity = 0
    ans = []
    for x in red(w):
        if x == 2:
            parity ^= 1
        else:
            ans.append((1 if x > 0 else -1)
                       * (positions[abs(x)] + 5 * parity))
    assert parity == 0
    return free_red(ans)

def cone_only_normal_form(w):
    """Normal form in (*_{i=1}^4 Z^2_i) * F(f,bar_f)."""
    stack = []
    for x in ordinary(w):
        i = (abs(x) - 1) % 5 + 1
        side = int(abs(x) > 5)
        sign = 1 if x > 0 else -1
        if i == 5:
            letter = sign * (side + 1)
            if stack and stack[-1][0] == 5:
                value = free_red(stack.pop()[1] + (letter,))
            else:
                value = (letter,)
            if value:
                stack.append((5, value))
        else:
            value = [0, 0]
            if stack and stack[-1][0] == i:
                value = list(stack.pop()[1])
            value[side] += sign
            if value != [0, 0]:
                stack.append((i, tuple(value)))
    return tuple(stack)

old_new = {int(k): tuple(v) for k, v in C['old_in_new'].items()}
new_old = {int(k): tuple(v) for k, v in C['new_in_old'].items()}
for j in range(1, 7):
    assert sub(old_new[j], new_old) == (j,)
    assert sub(new_old[j], old_new) == (j,)
f_to_w = {j: (j,) for j in range(1, 7)}
w_to_f = dict(f_to_w)
f_to_w[6] = tuple(H['branch_f_in_new_generators'])
w_to_f[6] = tuple(H['w_in_old_normalized_generators'])
for j in range(1, 7):
    assert sub(f_to_w[j], w_to_f) == (j,)
    assert sub(w_to_f[j], f_to_w) == (j,)

def project_free4(w):
    # After the f/w change: keep unbarred a,b,d,e; kill all barred
    # generators and w,bar_w.  All entries are literal based words.
    return free_red(x for x in ordinary(w) if 1 <= abs(x) <= 4)

rows = []
expected = {'beta_11': 1, 'beta_22': 4, 'beta_33': 5, 'beta_44': 3}
for loop in D['loops']:
    if loop['name'] not in expected:
        continue
    assert len(loop['nodes']) == 1
    assert loop['nodes'][0]['kind'] == 'cone_contact'
    cone_image = red(loop['positive_push']['2'])
    peeled, v = cone_conjugator(cone_image)
    nv = sub(v, old_new)
    wv = sub(nv, f_to_w)
    j = expected[loop['name']]
    delta = (j, 2, j, 2)
    assert cone_only_normal_form(mul(nv, inv(delta))) == ()
    projection = project_free4(wv)
    assert projection == (positions[j],)
    rows.append({
        'loop_index': loop['index'], 'loop_name': loop['name'],
        'positive_push_of_cone_mod_c2': cone_image,
        'initial_peeled_conjugator': peeled,
        'unique_orientation_even_conjugator': v,
        'source_word_in_same_sheet_normalization': nv,
        'source_word_in_w_normalization': wv,
        'equal_mod_only_four_cone_relations_to': delta,
        'cone_only_normal_form_of_difference': [],
        'free4_projection': projection,
        'free4_basis_order': ['a', 'b', 'd', 'e'],
    })
assert len(rows) == 4
assert [r['free4_projection'] for r in rows] == [(1,), (3,), (4,), (2,)]

# The free-four detector factors through the COMPLETE regional ordinary
# group, not merely its cone-only preliminary quotient.  Reidemeister--
# Schreier requires the raw ten words and their c conjugates.
relations_checked = 0
for loop in D['loops'][1:]:
    for node in loop['nodes']:
        w = sub(sub(node['relation'], old_new), f_to_w)
        assert project_free4(w) == ()
        assert project_free4(conj((2,), w)) == ()
        relations_checked += 2
assert relations_checked == 20

out = {
    'status': 'PASS',
    'input_sha256': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in (RAW, NORM, HNN)},
    'producer_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'four_source_peripherals': rows,
    'two_sided_nielsen_checks': 12,
    'two_sided_branch_stable_letter_checks': 12,
    'complete_regional_detector_relations_checked': relations_checked,
    'projected_source_basis': [[1], [3], [4], [2]],
    'inverse_basis_words': [[1], [4], [2], [3]],
    'geometric_convention': 'g_far^-1 x g_far = positive_push(x); g_source=g_far*v',
    'scope': 'Actual positive fixed-cone source peripherals after filling the far critical lassos. '
             'They equal the four diagonal cone generators; no annular invariance or global gluing is inferred.'
}
OUT.write_text(json.dumps(out, indent=2) + '\n')
print('PASS four unique even cone conjugators from the actual positive pushes.')
print('PASS all four source words equal their diagonal generators using only cone relations.')
print('PASS exact free-four projected basis a,d,e,b and its inverse permutation.')
print('PASS all20 complete ordinary regional relators under the free-four detector.')
for r in rows:
    print(r['loop_name'], 'normalized', r['source_word_in_same_sheet_normalization'],
          'projection', r['free4_projection'])
