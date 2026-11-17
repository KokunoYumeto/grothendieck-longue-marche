"""Exact word-level quotient analysis of the freshly reconstructed marginal.

This computes full free-group words, not abelian or nilpotent shadows.
It does not claim that the source orbit subgroup equals the filling kernel.
"""
from pathlib import Path
import json

P = Path(__file__).resolve().parents[1]
data = json.loads((P / 'work_DE/next_marginal_source/positive_fiber_data.json').read_text())


def red(word):
    out = []
    for a in word:
        if out and out[-1] == -a:
            out.pop()
        else:
            out.append(a)
    return out


def inv(word):
    return [-a for a in reversed(word)]


def mul(*words):
    return red([a for word in words for a in word])


def conj(v, word):
    return mul(v, word, inv(v))


def fill(word):
    return red([a for a in word if abs(a) in (2, 4, 6)])


def cyclic(word):
    word = red(word)
    i = 0
    while len(word) - 2*i > 1 and word[i] == -word[-i-1]:
        i += 1
    v, core = word[:i], word[i:len(word)-i] if i else word
    assert conj(v, core) == word
    return v, core


def inner_word(images):
    v, core = cyclic(images[2])
    assert core == [2], core
    w = conj(inv(v), images[4])
    u, core = cyclic(w)
    if core != [4] or not all(abs(a) == 2 for a in u):
        return None
    q = mul(v, u)
    if not all(conj(q, [j]) == images[j] for j in (2, 4, 6)):
        return None
    return q


answer = {'scope': 'Exact full-free-group index actions; no source-image equality inferred.',
          'old_action_data': {}, 'new_peripheral_data': {}}
for key, action in data['old_actions'].items():
    images = {j: fill(action[str(j)]) for j in (2, 4, 6)}
    q = inner_word(images)
    inverse_images = {j: fill(data['old_inverse_actions'][key][str(j)]) for j in (2, 4, 6)}
    qinverse = inner_word(inverse_images)
    assert ((q is None and qinverse is None) or
            (q is not None and qinverse == inv(q))), (key, q, qinverse)
    entry = {'quotient_images': images, 'quotient_inverse_images': inverse_images,
             'quotient_inner_word': q, 'killed_peripheral_data': {}}
    for j in (1, 3, 5, 7):
        v, core = cyclic(action[str(j)])
        assert core == [j], (key, j, core)
        vbar = fill(v)
        right = mul(inv(q), vbar) if q is not None else None
        entry['killed_peripheral_data'][str(j)] = {
            'conjugator_length': len(v), 'filled_conjugator': vbar,
            'index_right_word': right,
        }
    answer['old_action_data'][key] = entry
    print('OLD', key, 'q=', q, 'quotient_images=', images,
          'filled_conjugators=', {j: e['filled_conjugator'] for j, e in entry['killed_peripheral_data'].items()})

for key, word in data['new_fiber_words'].items():
    v, core = cyclic(word)
    answer['new_peripheral_data'][key] = {
        'conjugator': v, 'filled_conjugator': fill(v), 'cyclic_core': core,
    }
    print('NEW', key, 'filled_conjugator=', fill(v), 'cyclic_core=', core)

out = P / 'records/positive_marginal_index_actions.json'
out.write_text(json.dumps(answer, indent=2) + '\n')
print('PASS: quotient actions classified exactly; every old killed peripheral is a conjugate of itself.')
print('No transitivity or subgroup equality is asserted.')
