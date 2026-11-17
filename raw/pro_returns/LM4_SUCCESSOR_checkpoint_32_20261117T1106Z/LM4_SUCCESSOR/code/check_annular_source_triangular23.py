"""Check the new literal triangular source basis in the exact unfolded graph.

This independently evaluates the actual common-marking source words in
Gamma_infty semidirect (Z_h times C2). It imports no earlier evaluator.
It does not prove the presentation equivalence; that is the separate
two-sided proof in B112.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'work_DE/next_marginal_source/inner_q0_source22.json'
data = json.loads(SOURCE.read_text())


def inverse(word):
    return tuple(-x for x in reversed(word))


def free_reduce(word, cone=None):
    result = []
    for x in word:
        x = cone if cone is not None and abs(x) == cone else x
        if result and (result[-1] == -x or result[-1] == x == cone):
            result.pop()
        else:
            result.append(x)
    return tuple(result)


def product(*words, cone=None):
    return free_reduce((x for word in words for x in word), cone)


def conjugate(g, word):
    return product(g, word, inverse(g), cone=3)


def commutator(x, y):
    return product(x, y, inverse(x), inverse(y), cone=3)


def bar(word):
    return conjugate((3,), word)


def delta(word):
    return product(word, bar(word), cone=3)


# Ordinary graph vertices have form (family, level, barred).
# The two k vertices use level zero and their sheet bit.
def transform(vertex, height, parity):
    family, level, bit = vertex
    if family == 'k':
        return family, 0, bit ^ (height % 2) ^ parity
    return family, level + height, bit ^ parity


def commute(left, right):
    if left == right:
        return True
    lf, ln, lb = left
    rf, rn, rb = right
    if lf == rf == 'k':
        return False
    if lf == 'k':
        return lb == ((rn % 2) ^ rb)
    if rf == 'k':
        return rb == ((ln % 2) ^ lb)
    if lf == rf and ln == rn and lb != rb:
        return True
    if ln == rn:
        families = frozenset((lf, rf))
        if families == frozenset(('a', 'b')):
            return lb == rb
        if families in (frozenset(('a', 'd')), frozenset(('a', 'e')),
                        frozenset(('d', 'e'))):
            return lb != rb
    if lf == 'b' and rf in ('d', 'e') and rn == ln + 1:
        return lb == rb
    if rf == 'b' and lf in ('d', 'e') and ln == rn + 1:
        return lb == rb
    return False


def graph_reduce(word):
    word = list(word)
    while True:
        removed = False
        for i, (v, sign) in enumerate(word):
            for j in range(i + 1, len(word)):
                w, other_sign = word[j]
                if v == w and sign == -other_sign:
                    del word[j]
                    del word[i]
                    removed = True
                    break
                if not commute(v, w):
                    break
            if removed:
                break
        if not removed:
            return tuple(word)


ordinary = {1: 'a', 2: 'b', 5: 'd', 6: 'e'}


def evaluate(word):
    expanded = []
    for x in word:
        if x == 4:       # f = h k^-1
            expanded.extend((7, -8))
        elif x == -4:
            expanded.extend((8, -7))
        else:
            expanded.append(x)
    graph_word = []
    height = parity = 0
    for x in expanded:
        if abs(x) == 3:
            parity ^= 1
        elif abs(x) == 7:
            height += 1 if x > 0 else -1
        else:
            vertex = ('k', 0, 0) if abs(x) == 8 else (ordinary[abs(x)], 0, 0)
            graph_word.append((transform(vertex, height, parity), 1 if x > 0 else -1))
    return graph_reduce(graph_word), height, parity


def equal(left, right):
    value = evaluate(product(left, inverse(right)))
    assert value == ((), 0, 0), value


a, b, d, e, h = (1,), (2,), (5,), (6,), (7,)
E = (4, 5, 6, -5, -4)
T = product((3, 2, 3, 2, 3), E, (3, -2, 3, -2), cone=3)
printed = [
    product(bar(b), b, cone=3),
    product(T, T, cone=3),
    product((3, 2), commutator(d, bar(d)), (-2, 3), delta(d), cone=3),
    product((3, 2), commutator(a, bar(a)), (-2, 3), delta(a), cone=3),
]
actual = [tuple(row['source_word_in_q0_adapted_Y_basis'])
          for row in data['four_contact_source_words_in_common_q0_marking']]
assert printed == actual

diagonal_basis = [
    delta(b),
    conjugate(product(delta(b), h, delta(d)), delta(e)),
    delta(d),
    delta(a),
    h,
]
for left, right in zip(actual + [h], diagonal_basis):
    equal(left, right)
equal(commutator(E, bar(E)), ())
equal(delta(E), conjugate(product(h, delta(d)), delta(e)))
equal(product(T, T, cone=3), conjugate(delta(b), delta(E)))

out = {
    'status': 'PASS',
    'completed_at': datetime.now(timezone.utc).isoformat(),
    'input': str(SOURCE.relative_to(ROOT)),
    'input_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    'producer_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'four_printed_words_equal_actual_arrays': True,
    'five_actual_source_words_equal_triangular_diagonal_basis': True,
    'E_bar_E_commute': True,
    'delta_E_and_T_squared_reductions': True,
    'actual_words': actual,
    'triangular_words': diagonal_basis,
    'independence': 'No earlier evaluator or producer imported; symbolic integer levels and a fresh commutation-cancellation evaluator.',
    'scope': 'Literal source-basis identities in the already proved unfolded annular presentation; no extra geometric or global comparison.',
}
(ROOT / 'records/annular_source_triangular23.json').write_text(json.dumps(out, indent=2) + '\n')
print('PASS four printed source expressions are the actual common-marking words.')
print('PASS all five actual source words equal the triangular diagonal free basis.')
print('PASS E commutes with bar E; delta_E and T squared reductions retain order.')
print('PASS independent exact infinite-graph evaluator; no finite truncation.')
