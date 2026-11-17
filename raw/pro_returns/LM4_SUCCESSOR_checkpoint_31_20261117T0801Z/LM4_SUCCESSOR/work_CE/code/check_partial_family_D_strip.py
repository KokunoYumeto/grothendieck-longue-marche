#!/usr/bin/env python3
"""Exact input and Nielsen-inverse checks for the whole partial D-strip proof.

No finite-group search, rank heuristic, or orbit truncation is used.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / 'work_DE/next_marginal_source'
ordered = json.loads((P / 'tangent_ordered_family.json').read_text())
mark = json.loads((P / 'tangent_infinity_action.json').read_text())

def red(word):
    out = []
    for x in word:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return out

def inv(word):
    return [-x for x in reversed(word)]

def sub(word, images):
    return red([y for x in word for y in
                (images[abs(x)] if x > 0 else inv(images[abs(x)]))])

def conj(a, b):
    return red(a + b + inv(a))

D = [5, 7]
action = {int(j): w for j, w in mark['alpha1_in_new2'].items()}
assert sub(D, action) == D
pair = {1: [2, 1], 2: [2, 1], 4: [4, 6], 6: [4, 6]}
for j, k in pair.items():
    expected = conj(inv(D), conj(k, [j]))
    assert action[j] == expected
    assert sub(action[j], action) == conj(inv(D + D), conj(k + k, [j]))

basis = {int(j): w for j, w in ordered['ordered_basis_in_V'].items()}
step = {(0,1):[1], (0,2):[2], (0,4):[3], (0,6):[4], (0,7):[9],
        (1,1):[5], (1,2):[6], (1,4):[7], (1,6):[8], (1,7):[10],
        (0,3):[], (1,3):[11], (0,5):[12], (1,5):[13]}

def schreier(word):
    state, out = 0, []
    for x in word:
        nxt = state ^ (abs(x) in (3, 5))
        out += step[state, abs(x)] if x > 0 else inv(step[nxt, abs(x)])
        state = nxt
    assert state == 0
    out = red(out)
    assert sub(out, basis) == red(word)
    return out

def fill(word):
    return red([x for x in schreier(word) if abs(x) > 4])

# U-words expressed in the independently checked V,A,B,C marking.
u6 = [5, 6, -5]
U = {6: u6, 1: conj(u6, [1]), 4: conj(u6, [4]),
     2: conj(u6, [5, 2, -5])}
selected = {1: U[1], 4: U[4], 2: conj(D, U[2]), 6: conj(D, U[6])}
for word in selected.values():
    assert fill(word) == []

surviving = {1: U[2], 2: U[6], 3: conj(D, U[1]),
             4: conj(D, U[4]), 5: D + D}
forward = {1: [12,8,6,-8,-12], 2: [12,8,-12],
           3: [12,10,5,-10,-12], 4: [12,10,7,-10,-12],
           5: [12,10,13,9], 6: [9], 7: [10], 8: [11], 9: [12]}
for j, word in surviving.items():
    assert fill(word) == forward[j]

# The old F9 labels are 5,...,13; the new ones are 1,...,9.
backward = {5: [-7,-9,3,9,7], 6: [-9,-2,1,2,9],
            7: [-7,-9,4,9,7], 8: [-9,2,9],
            9: [6], 10: [7], 11: [8], 12: [9],
            13: [-7,-9,5,-6]}
for j in range(1,10):
    assert sub(forward[j], backward) == [j]
for j in range(5,14):
    assert sub(backward[j], forward) == [j]

result = {
    'input_hashes': {name: hashlib.sha256((P/name).read_bytes()).hexdigest()
                     for name in ('tangent_ordered_family.json',
                                  'tangent_infinity_action.json')},
    'alpha1_squared_pair_inner_checks': 4,
    'selected_ordered_words': {j: schreier(w) for j,w in selected.items()},
    'surviving_ordered_words': {j: schreier(w) for j,w in surviving.items()},
    'partial_quotient_nielsen_basis': forward,
    'inverse_nielsen_basis': backward,
    'nielsen_inverse_checks': 18,
    'scope': 'Supports the whole selected-family kernel intersection in W_even. '
             'No whole J_mov=N_mov or I=R assertion.'
}
(ROOT/'work_CE/partial_family_D_strip_certificate.json').write_text(
    json.dumps(result, indent=2) + '\n')
print('PASS: actual alpha1 fixes D; four squared pair-inner identities.')
print('PASS: four selected generators vanish under the actual partial filling.')
print('PASS: five surviving images and 18 literal Nielsen inverse checks.')
print('SCOPE: complete partial kernel in the ordered rank-nine free factor only.')
