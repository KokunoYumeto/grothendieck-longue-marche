#!/usr/bin/env python3
"""Independent single-word q0 witness; no graph-group reduction is used."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
paths = [
    ROOT / 'work_CE/next_symmetric_nodes/inner_bad_orbifold_words22.json',
    ROOT / 'records/inner_bad_normalized22.json',
    ROOT / 'records/inner_bad_hnn22.json',
]
D, N, H = [json.loads(p.read_text()) for p in paths]

def reduce_word(word):
    out = []
    for x in word:
        x = 2 if abs(x) == 2 else int(x)
        if out and (out[-1] == -x or out[-1] == x == 2):
            out.pop()
        else:
            out.append(x)
    return tuple(out)

def inverse(word):
    return reduce_word(-x for x in reversed(word))

def product(*words):
    return reduce_word(x for word in words for x in word)

def substitute(word, images):
    return product(*(images[abs(x)] if x > 0 else inverse(images[-x])
                     for x in word))

q0 = D['loops'][0]
assert q0['name'] == 'q0'
loop = next(l for l in D['loops'] if l['name'] == 'beta_24')
assert len(loop['nodes']) == 1
relator = tuple(loop['nodes'][0]['relation'])
negative = {int(k): tuple(v) for k, v in q0['negative_pull'].items()}
positive = {int(k): tuple(v) for k, v in q0['positive_push'].items()}
for j in range(1, 7):
    assert substitute(positive[j], negative) == (j,)
    assert substitute(negative[j], positive) == (j,)

first = {int(k): tuple(v) for k, v in N['old_in_new'].items()}
second = {j: (j,) for j in range(1, 7)}
second[6] = tuple(H['branch_f_in_new_generators'])
image = substitute(substitute(substitute(relator, negative), first), second)
expected = (1, 5, 6, 2, 4, 2, -6, -5, -3,
            5, 6, 2, -4, 2, -6, -5, 3, -1)
assert image == expected

# a [e w bar(d) w^-1 e^-1, b^-1] a^-1, literally in C2*F5.
a, b_inv = (1,), (-3,)
h = (5, 6, 2, 4, 2, -6, -5)
commutator = product(h, b_inv, inverse(h), inverse(b_inv))
assert image == product(a, commutator, inverse(a))

# The exact three middle base factors in its Britton decomposition.
middles = [(2, 4, 2), (-5, -3, 5), (2, -4, 2)]
def ordinary_coordinates(word):
    parity = 0
    coords = {}
    for x in word:
        if abs(x) == 2:
            parity ^= 1
        else:
            key = (abs(x), parity)
            coords[key] = coords.get(key, 0) + (1 if x > 0 else -1)
    assert parity == 0
    return {key: val for key, val in coords.items() if val}

coords = [ordinary_coordinates(w) for w in middles]
assert coords == [{(4, 1): 1}, {(3, 0): -1}, {(4, 1): -1}]
source = {(7, 0), (8, 0)}
target = {(5, 0), (3, 1)}
for row, clique in zip(coords, (source, target, source)):
    assert any(vertex not in clique for vertex in row)

record = {
    'status': 'PASS',
    'inputs_sha256': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in paths},
    'producer_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'relator_name': 'beta_24',
    'operator': 'actual negative q0 pull',
    'literal_HNN_word': image,
    'literal_conjugator': a,
    'commutator_first_entry': h,
    'commutator_second_entry': b_inv,
    'stable_signs': [1, -1, 1, -1],
    'intervening_base_words': middles,
    'nonzero_excluding_coordinates': [
        {'vertex': [4, 1], 'value': 1, 'excluded_edge': 'source <p,r>'},
        {'vertex': [3, 0], 'value': -1, 'excluded_edge': 'target <e,bar b>'},
        {'vertex': [4, 1], 'value': -1, 'excluded_edge': 'source <p,r>'},
    ],
    'argument': 'Coordinate retractions exclude all three possible pinches; Britton gives nontriviality.',
    'scope': 'The slit relation has nontrivial negative-q0 image in the slit group; the annular filling imposes a genuinely additional relation.'
}
output = ROOT / 'work_A/review_q0_beta24_witness22.json'
output.write_text(json.dumps(record, indent=2) + '\n')
print('PASS all12 literal q0 inverse-composition checks.')
print('PASS actual negative beta24 image equals the printed18-letter HNN word.')
print('PASS literal conjugacy a [e w bar(d) w^-1 e^-1, b^-1] a^-1.')
print('PASS all3 Britton nonmembership gates by nonzero coordinate retractions.')
print('CONCLUSION four stable letters remain: nontrivial in the actual slit group.')
