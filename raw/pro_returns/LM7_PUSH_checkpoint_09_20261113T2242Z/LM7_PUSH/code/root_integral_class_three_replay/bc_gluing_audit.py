#!/usr/bin/env python3
"""Independent audit of the mixed class-three gluing maps at seventeen.

The word evaluation uses truncated noncommutative Magnus polynomials,
not the semidirect word collector of the source computation.  All
linear algebra is recomputed modulo three without importing its routines.
"""
from functools import lru_cache
from itertools import product
from pathlib import Path
import hashlib
import json
import numpy as np

HERE = Path(__file__).resolve().parent
ACTION_PATH = HERE / 'a_ihara_gamma2_action_certificate.npz'
GLUING_PATH = HERE / 'a_frobenius17_mixed_gluing_local_certificate.npz'
actions = np.load(ACTION_PATH)
saved = np.load(GLUING_PATH)
metadata = json.loads((HERE / 'a_frobenius17_mixed_gluing_local.json').read_text())
I = np.eye(375, dtype=np.int64)
C = actions['action_c'].astype(np.int64)
A = [actions['action_' + name].astype(np.int64) for name in ('m', 'n', 't')]
aug = [(a - I) % 3 for a in A]
BM = saved['source_m'].astype(np.int64)
BN = saved['source_n'].astype(np.int64)
H = np.zeros((375, 66), dtype=np.int64)
H[:, 45:] = BM[:, :21]
BT = aug[2] @ H % 3
B = [BM, BN, BT]
Q = saved['target_quotient'].astype(np.int64)
assert BM.shape == BN.shape == H.shape == (375, 66)


def basis_columns(matrix):
    original = np.asarray(matrix, dtype=np.int64) % 3
    reduced = original.copy()
    r = 0
    pivots = []
    for j in range(reduced.shape[1]):
        ids = np.flatnonzero(reduced[r:, j])
        if not len(ids):
            continue
        s = r + int(ids[0])
        reduced[[r, s]] = reduced[[s, r]]
        reduced[r] = reduced[r] * int(reduced[r, j]) % 3
        if r + 1 < reduced.shape[0]:
            reduced[r + 1:] = (reduced[r + 1:]
                - reduced[r + 1:, j, None] * reduced[r, None, :]) % 3
        pivots.append(j)
        r += 1
        if r == reduced.shape[0]:
            break
    return original[:, pivots]


def rank(matrix):
    return basis_columns(matrix).shape[1]


def nullspace(matrix):
    a = np.asarray(matrix, dtype=np.int64).copy() % 3
    r = 0
    pivots = []
    for j in range(a.shape[1]):
        ids = np.flatnonzero(a[r:, j])
        if not len(ids):
            continue
        s = r + int(ids[0])
        a[[r, s]] = a[[s, r]]
        a[r] = a[r] * int(a[r, j]) % 3
        coefficients = a[:, j].copy()
        coefficients[r] = 0
        a = (a - coefficients[:, None] * a[r, None, :]) % 3
        pivots.append(j)
        r += 1
        if r == a.shape[0]:
            break
    free = [j for j in range(a.shape[1]) if j not in pivots]
    out = np.zeros((a.shape[1], len(free)), dtype=np.int64)
    for k, j in enumerate(free):
        out[j, k] = 1
        for row, col in enumerate(pivots):
            out[col, k] = -a[row, j] % 3
    assert not np.any(np.asarray(matrix, dtype=np.int64) @ out % 3)
    return out


# Exact eigenspace lifts and target quotient.
assert np.array_equal(C @ C % 3, I)
assert not np.any((I - C) @ BM % 3)
assert not np.any((I + A[1] @ C) @ BN % 3)
assert not np.any((I - C) @ H % 3)
assert rank(BM[:45, :21]) == 21
assert rank(BN[:45, 21:45]) == 24
assert not np.any(BM[:, 21:]) and not np.any(BN[:, :21])
assert not np.any(BN[:, 45:])
assert np.array_equal(saved['necessary_local_kernel'], np.eye(66, dtype=np.int8))
assert not np.any(saved['class2_local_map'])

old = json.loads((HERE / 'a_frobenius17_eval_m3.json').read_text())
global_image = (actions['A7_to_Schreier_M3'].astype(np.int64)
                @ np.array(old['evaluation_image_mod3_basis'], dtype=np.int64)) % 3
C3 = C[45:, 45:]
assert rank(global_image) == 15
assert rank(I[45:, 45:] + C3) == 164
assert rank(Q) == 149 and Q.shape == (149, 330)
assert not np.any(Q @ global_image % 3)
assert np.array_equal(Q @ C3 % 3, Q)

# Recompute I^j Lbar and certify the affine D6 truncation.
span = I
dimensions = [375]
for degree in range(1, 7):
    span = basis_columns(np.hstack([a @ span % 3 for a in aug]))
    dimensions.append(span.shape[1])
    if not span.shape[1]:
        break
assert dimensions == [375, 249, 132, 47, 4, 0]

# Noncommutative polynomials over F3 through total degree five.
LIMIT = 5
ONE = {(): 1}


def add(p, q, scale=1):
    out = dict(p)
    for word, value in q.items():
        out[word] = (out.get(word, 0) + scale * value) % 3
        if not out[word]:
            del out[word]
    return out


def multiply(p, q):
    out = {}
    for left, a in p.items():
        for right, b in q.items():
            word = left + right
            if len(word) <= LIMIT:
                out[word] = (out.get(word, 0) + a * b) % 3
                if not out[word]:
                    del out[word]
    return out


def inverse(p):
    assert p.get((), 0) == 1
    negative = add({}, add(p, ONE, -1), -1)
    result = dict(ONE)
    term = dict(ONE)
    for _ in range(LIMIT):
        term = multiply(term, negative)
        result = add(result, term)
    assert multiply(p, result) == multiply(result, p) == ONE
    return result


def power(p, n):
    result = dict(ONE)
    while n:
        if n & 1:
            result = multiply(result, p)
        p = multiply(p, p)
        n //= 2
    return result


def comm(p, q):
    return multiply(multiply(multiply(p, q), inverse(p)), inverse(q))


def is_lyndon(word):
    return all(word < word[i:] + word[:i] for i in range(1, len(word)))


@lru_cache(None)
def lyndon(word):
    if len(word) == 1:
        return {(): 1, word: 1}
    cut = next(i for i in range(1, len(word)) if is_lyndon(word[i:]))
    return comm(lyndon(word[:cut]), lyndon(word[cut:]))


@lru_cache(None)
def cocycle_monomial(word):
    assert word
    if len(word) == 1:
        return B[word[0]]
    return aug[word[0]] @ cocycle_monomial(word[1:]) % 3


@lru_cache(None)
def operator_monomial_on_H(word):
    if not word:
        return H
    return aug[word[0]] @ operator_monomial_on_H(word[1:]) % 3


def evaluate_cocycle(p):
    out = np.zeros((375, 66), dtype=np.int64)
    for word, coefficient in p.items():
        if word:
            out += coefficient * cocycle_monomial(word)
    return out % 3


def evaluate_operator_minus_identity_on_H(p):
    out = np.zeros((375, 66), dtype=np.int64)
    for word, coefficient in p.items():
        if word:
            out += coefficient * operator_monomial_on_H(word)
    return out % 3


base_word = multiply(power(lyndon((0,)), 6), lyndon((0, 1, 1)))
base_word = multiply(base_word, power(lyndon((0, 2, 2)), 2))
assert all(not word or len(word) >= 3 for word in base_word)
base_delta = evaluate_cocycle(base_word)
base_correction = evaluate_operator_minus_identity_on_H(base_word)
base_delta = 2 * (base_delta + C @ base_delta) % 3
base_delta -= 2 * (base_correction + C @ base_correction) % 3
base_delta %= 3
assert not np.any(base_delta[:45])
known = Q @ base_delta[45:] % 3
assert np.array_equal(known, saved['known_gluing'])

labels = [tuple(w) for w in metadata['unknown_lyndon_words']]
assert len(labels) == 68
unknown = []
for word in labels:
    polynomial = lyndon(word)
    delta = evaluate_cocycle(polynomial)
    delta = 2 * (delta + C @ delta) % 3
    assert not np.any(delta[:45])
    # Every unknown word has zero retained geometric action; its local
    # conjugator subtraction therefore vanishes as an actual operator.
    correction = evaluate_operator_minus_identity_on_H(polynomial)
    correction = 2 * (correction + C @ correction) % 3
    assert not np.any(correction)
    unknown.append(Q @ delta[45:] % 3)
unknown = np.stack(unknown)
assert np.array_equal(unknown, saved['unknown_gluing'])
nonzero = [i for i, a in enumerate(unknown) if np.any(a)]
assert nonzero == [0, 1, 4]
assert [labels[i] for i in nonzero] == [(0, 1, 2), (0, 2, 1), (0, 0, 1, 1)]

# Quotient all 21 local conjugators simultaneously for every actual case.
all_h = np.hstack([known[:, 45:]] + [a[:, 45:] for a in unknown])
assert rank(all_h) == 6
remove_h = nullspace(all_h.T).T
assert remove_h.shape == (143, 149)
assert not np.any(remove_h @ all_h % 3)
case_rows = []
for coefficients in product(range(3), repeat=3):
    evaluated = known.copy()
    for a, index in zip(coefficients, nonzero):
        evaluated += a * unknown[index]
    evaluated %= 3
    source = evaluated[:, :45]
    conjugator = evaluated[:, 45:]
    row = {'coefficients': list(coefficients),
           'source_rank': rank(source),
           'local_conjugator_rank': rank(conjugator),
           'combined_rank': rank(evaluated),
           'source_rank_after_common_local_quotient': rank(remove_h @ source % 3)}
    assert ([row[k] for k in ('source_rank', 'local_conjugator_rank',
                              'combined_rank', 'source_rank_after_common_local_quotient')]
            == [30, 6, 30, 24])
    case_rows.append(row)

out = {
    'action_input_sha256': hashlib.sha256(ACTION_PATH.read_bytes()).hexdigest(),
    'gluing_input_sha256': hashlib.sha256(GLUING_PATH.read_bytes()).hexdigest(),
    'evaluation_method': 'Truncated noncommutative Magnus polynomials and universal cocycle derivation',
    'augmentation_dimensions_m_n_t': dimensions,
    'affine_cocycle_source_kernel': 'D6 of the free pro-three source on m,n,t',
    'integral_lift_reductions': {'m_plus_rank': 21, 'nc_minus_rank': 24},
    'local_M3_plus_dimension': 164,
    'global_M3_restriction_rank': 15,
    'gluing_target_dimension': 149,
    'all_68_unknown_maps_match': True,
    'nonzero_unknown_words': [list(labels[i]) for i in nonzero],
    'common_local_conjugator_image_rank': 6,
    'common_local_quotient_dimension': 143,
    'coefficient_cases': case_rows,
    'ambient_source_dimension': 45,
    'ambient_kernel_dimension_in_each_case': 21,
    'scope': ('Independent finite maps and ranks. The integral kernel R has '
              'rank24 by the separately proved Frobenius/coboundary map; '
              'no arbitrary mod-three cochain is asserted integrally cuspidal.'),
    'status': 'PASS'
}
encoded = json.dumps(out, indent=2) + '\n'
print(encoded, end='')
Path(__file__).with_suffix('.json').write_text(encoded)
np.savez_compressed(HERE / 'bc_gluing_audit_certificate.npz',
                    known=known.astype(np.int8), unknown=unknown.astype(np.int8),
                    common_local_quotient=remove_h.astype(np.int8))
