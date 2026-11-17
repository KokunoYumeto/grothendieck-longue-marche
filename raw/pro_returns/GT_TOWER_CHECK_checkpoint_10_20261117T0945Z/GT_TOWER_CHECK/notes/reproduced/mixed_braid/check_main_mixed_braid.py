#!/usr/bin/env python3
"""Independent Reidemeister--Schreier certificate for the A.4.26 bridge.

This reconstructs the three cosets and every positive Schreier generator
from the strand-stabilizer permutation action, rewrites every conjugate
of the defining B_3 relation, and verifies the Tietze elimination.  The
Artin computations below are independent of the tower producer script.
"""
import json
from pathlib import Path


def red(word):
    out = []
    for letter in word:
        if out and out[-1] == -letter:
            out.pop()
        else:
            out.append(letter)
    return tuple(out)


def inv(word):
    return tuple(-letter for letter in reversed(word))


def mul(*words):
    return red(letter for word in words for letter in word)


def subst(word, images):
    return mul(*(images[abs(letter)] if letter > 0
                 else inv(images[abs(letter)]) for letter in word))


def power(word, n):
    return mul(*([word if n >= 0 else inv(word)] * abs(n)))


# u=(12), w=(23).  Left cosets H\B_3 are the orbit of strand 3 under
# right multiplication; the prefix-closed transversal is 1,w,wu.
reps = {3: (), 2: (2,), 1: (2, 1)}


def next_state(state, generator):
    pair = (1, 2) if abs(generator) == 1 else (2, 3)
    return pair[1] if state == pair[0] else pair[0] if state == pair[1] else state


positive_edges = []
schreier_words = {}
for state in (3, 2, 1):
    for generator in (1, 2):
        target = next_state(state, generator)
        word = mul(reps[state], (generator,), inv(reps[target]))
        positive_edges.append((state, generator, target, word))
        if word:
            schreier_words[(state, generator)] = word
assert len(schreier_words) == 4
names = {(3, 1): 1, (2, 2): 2, (1, 1): 3, (1, 2): 4}
assert schreier_words == {
    (3, 1): (1,),
    (2, 2): (2, 2),
    (1, 1): (2, 1, 1, -2),
    (1, 2): (2, 1, 2, -1, -2),
}
print('PASS all6 coset transitions and all4 nontrivial Schreier generators')


def rewrite(word, state=3):
    out = []
    initial = state
    for letter in word:
        target = next_state(state, letter)
        key = (state, letter) if letter > 0 else (target, -letter)
        if key in names:
            out.append(names[key] if letter > 0 else -names[key])
        state = target
    return red(out), state, initial


relator = (1, 2, 1, -2, -1, -2)
relations = []
for state in (3, 2, 1):
    word = mul(reps[state], relator, inv(reps[state]))
    result, end, start = rewrite(word)
    assert start == end == 3
    relations.append(result)
assert relations == [(1, -4), (4, 3, -1, -2), (3, 2, 1, -2, -3, -4)]
print('PASS all3 rewritten B3 defining relations')

# Exact Tietze substitutions t=u, k=u^{-1}vu.  The last relator is
# u^{-1} ((vu)^2 (uv)^{-2}) u, so conjugating the relator by u gives
# precisely the claimed Artin type-B_2 relation.
elimination = {1: (1,), 2: (2,), 3: (-1, 2, 1), 4: (1,)}
eliminated = [subst(word, elimination) for word in relations]
assert eliminated[:2] == [(), ()]
remaining = mul((1,), eliminated[2], (-1,))
target = mul(power((2, 1), 2), inv(power((1, 2), 2)))
assert remaining == target
print('PASS Tietze elimination leaves exactly (vu)^2=(uv)^2')


def artin_generator(n, j):
    images = {i: (i,) for i in range(1, n + 1)}
    k = abs(j)
    if j > 0:
        images[k] = (k, k + 1, -k)
        images[k + 1] = (k,)
    else:
        images[k] = (k + 1,)
        images[k + 1] = (-k - 1, k, k + 1)
    return images


def artin(n, word):
    images = {i: (i,) for i in range(1, n + 1)}
    for j in word:
        generator = artin_generator(n, j)
        images = {i: subst(image, generator) for i, image in images.items()}
    return images


artin_checks = []


def check(n, name, left, right=()):
    assert artin(n, left) == artin(n, right), name
    artin_checks.append({'rank': n, 'name': name, 'left': left, 'right': right})
    print('PASS', name)


u, w = (1,), (2,)
v = power(w, 2)
check(3, '(u w^2)^2=(u w)^3', power(mul(u, v), 2), power(mul(u, w), 3))
a, b, d = (1,), (2,), (3,)
V = power(mul(a, b), 3)
omega = power(mul(a, b, d), 4)
check(4, '(d V)^2=omega a^2', power(mul(d, V), 2), mul(omega, power(a, 2)))
check(4, 'mixed presentation maps to d,V', power(mul(d, V), 2), power(mul(V, d), 2))
check(4, 'V=a^2 b a^2 b', V, mul(power(a, 2), b, power(a, 2), b))
for name, x, y in [('a,V', a, V), ('b,V', b, V), ('a,d', a, d),
                   ('omega,a', omega, a), ('omega,b', omega, b), ('omega,d', omega, d)]:
    check(4, '[' + name + ']=1', mul(x, y, inv(x), inv(y)))

# Induction of the mixed-subgroup map into Q wreath S_3.  Coordinates
# are literal B_4 words, so the multiplication identity is checked in
# the faithful Artin action before it is specialized to any finite Q.
def wreath_mul(left, right):
    coords, perm = left
    other, next_perm = right
    return (tuple(mul(coords[i], other[perm[i]]) for i in range(3)),
            tuple(next_perm[perm[i]] for i in range(3)))


def wreath_power(element, n):
    assert n >= 0
    result = (((), (), ()), (0, 1, 2))
    for _ in range(n):
        result = wreath_mul(result, element)
    return result


U = ((d, (), mul(inv(d), V, d)), (0, 2, 1))
W = (((), V, d), (1, 0, 2))
UWU = wreath_mul(wreath_mul(U, W), U)
WUW = wreath_mul(wreath_mul(W, U), W)
assert UWU[1] == WUW[1]
for i in range(3):
    assert artin(4, UWU[0][i]) == artin(4, WUW[0][i])
assert U[1][0] == 0 and U[0][0] == d
W2 = wreath_power(W, 2)
assert W2[1][0] == 0 and W2[0][0] == V
UW3 = wreath_power(wreath_mul(U, W), 3)
assert UW3[1] == (0, 1, 2)
assert artin(4, UW3[0][0]) == artin(4, mul(omega, power(a, 2)))
print('PASS literal induced B3 map into Q wreath S3 and exact base component')

certificate = {
    'scope': 'Independent exact mixed-braid Schreier and Artin audit of A.4.26; no finite pentagon implication is asserted.',
    'transversal': reps,
    'positive_coset_edges': positive_edges,
    'Schreier_names': {'u': 1, 'v': 2, 'k': 3, 't': 4},
    'rewritten_relators': relations,
    'Tietze_substitutions': elimination,
    'eliminated_relators': eliminated,
    'conjugated_final_relator': remaining,
    'Artin_checks': artin_checks,
    'induced_wreath': {'state_order': [3, 2, 1], 'U': U, 'W': W,
                      'UWU': UWU, 'WUW': WUW, 'W_squared': W2,
                      'UW_cubed': UW3, 'order_bound': '6*|Q|^3'},
}
Path(__file__).with_suffix('.json').write_text(json.dumps(certificate, indent=2) + '\n')
print('PASS complete independent mixed-braid certificate')
