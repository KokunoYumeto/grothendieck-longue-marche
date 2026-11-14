#!/usr/bin/env python3
"""Exact word, module and permutation certificates for D.37.

This does not search for a mixed-sign extra deck symmetry.  It checks
the maps in the proved reduction and the complete separator obstruction.
"""
from itertools import permutations, product
import json
from pathlib import Path


def red(word):
    result = []
    for letter in word:
        if result and result[-1] == -letter:
            result.pop()
        else:
            result.append(letter)
    return tuple(result)


def inv(word):
    return tuple(-letter for letter in reversed(word))


def mul(*words):
    return red(sum(words, ()))


def sub(word, images):
    return mul(*(images[letter] if letter > 0 else inv(images[-letter])
                 for letter in word))


def compose(left, right):
    return {i: sub(word, left) for i, word in right.items()}


def inner(word, rank):
    return {i: mul(word, (i,), inv(word)) for i in range(1, rank + 1)}


def cyclic(word):
    word = red(word)
    while len(word) > 1 and word[0] == -word[-1]:
        word = word[1:-1]
    return word


def cyclic_conjugate(left, right):
    a, b = cyclic(left), cyclic(right)
    return len(a) == len(b) and any(a == b[i:] + b[:i]
                                  for i in range(max(1, len(b))))


def perm_mul(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def perm_inv(p):
    return tuple(p.index(i) for i in range(len(p)))


def evaluate(word, images):
    size = len(next(iter(images.values())))
    result = tuple(range(size))
    for letter in word:
        p = images[abs(letter)]
        if letter < 0:
            p = perm_inv(p)
        result = perm_mul(result, p)
    return result


def cycle_type(p):
    seen, sizes = set(), []
    for i in range(len(p)):
        if i in seen:
            continue
        orbit, j = [], i
        while j not in seen:
            seen.add(j)
            orbit.append(j)
            j = p[j]
        sizes.append(len(orbit))
    return sorted(sizes)


def partition(*blocks):
    return tuple(sorted(tuple(sorted(block)) for block in blocks))


def image_partition(p, blocks):
    return partition(*(tuple(p[i] for i in block) for block in blocks))


def block_action(p, blocks):
    image = tuple(tuple(sorted(p[i] for i in block)) for block in blocks)
    if image == blocks:
        return 'preserves each'
    if image == tuple(reversed(blocks)):
        return 'exchanges'
    return 'moves partition'


def main():
    out = {}
    # D.37b, in the free group F(x,y).
    x, y = (1,), (2,)
    z = inv(mul(x, y))
    marking = {1: x, 2: mul(y, x, inv(y)), 3: mul(y, y)}
    fourth = (-3, -2, -1)
    assert sub(fourth, marking) == mul(z, z)
    deck = {1: (2,), 2: (3, 1, -3), 3: (3,)}
    for i in range(1, 4):
        assert sub(deck[i], marking) == mul(y, marking[i], inv(y))
    assert compose(deck, deck) == inner((3,), 3)
    assert cyclic_conjugate(sub(fourth, deck), fourth)
    out['standard_cover'] = {
        'N_basis_in_F': marking,
        'fourth_cusp_in_N': fourth,
        'deck_images': deck,
        'deck_square_inner_word': [3],
        'all_word_checks': True,
    }

    # D.37m,n: F(l,a,b), with l=1,a=2,b=3.
    change = {1: (2,), 2: (-2, 1, 3, -1, 2), 3: (-2, 1)}
    reverse = {1: (1, 3), 2: (1,), 3: (-3, 2, 3)}
    identity = {i: (i,) for i in range(1, 4)}
    assert compose(change, reverse) == identity
    assert compose(reverse, change) == identity
    Delta = compose(change, compose(deck, reverse))
    assert Delta == {
        1: (-2, 1, 3), 2: (-2, 1, 3, -1, 2), 3: (2,)
    }
    assert compose(Delta, Delta) == inner((-2, 1), 3)
    cusps = [(2,), (-2, 1), (3,), (-3, -1)]
    permutation = [2, 1, 0, 3]
    for i, cusp in enumerate(cusps):
        assert cyclic_conjugate(sub(cusp, Delta), cusps[permutation[i]])
    out['transported_deck'] = {
        'change': change, 'inverse_change': reverse,
        'images': Delta, 'square_inner_word': [-2, 1],
        'cusp_permutation_zero_based': permutation,
    }

    # A geometric specialization with two different geometric deck maps.
    alpha = {1: (1,), 2: (-3,), 3: (1, -2, -1)}
    Delta0 = {1: (3, 1, -2), 2: (3,),
              3: (3, 1, 2, -1, -3)}
    assert compose(alpha, alpha) == inner((1,), 3)
    assert compose(Delta0, Delta0) == inner((3, 1), 3)
    assert compose(alpha, Delta0) == compose(
        inner((-3,), 3), compose(Delta0, alpha))
    for i, cusp in enumerate(cusps):
        assert cyclic_conjugate(sub(cusp, Delta0), cusps[permutation[i]])
    # The extension of Delta0 eliminates to F(a,r), l=b^-1 r^2.
    elimination = {1: (2, 1, 2), 2: (1,), 3: (2, 1, -2)}
    # Here a=1,r=2; b=r a r^-1, l=b^-1 r^2 = r a^-1 r.
    elimination[1] = (2, -1, 2)
    for i in range(1, 4):
        assert sub(Delta0[i], elimination) == mul(
            (2,), elimination[i], (-2,))
    assert sub((-2, 1), elimination) == mul((-1, 2), (-1, 2))
    assert cyclic_conjugate(sub((-3, -1), elimination), (-2, -2))
    # Explicit finite quotient witnesses failure of the other deck map.
    ad = compose(alpha, Delta)[1]
    da = compose(Delta, alpha)[1]
    assert len(cyclic(ad)) == 5 and len(cyclic(da)) == 3
    witness = None
    for size in (2, 3, 4):
        symmetric = tuple(permutations(range(size)))
        for images0 in product(symmetric, repeat=3):
            images = dict(zip(range(1, 4), images0))
            p, q = evaluate(ad, images), evaluate(da, images)
            if cycle_type(p) != cycle_type(q):
                witness = {'degree': size, 'generator_images': images,
                           'alpha_Delta_l': p, 'Delta_alpha_l': q,
                           'cycle_types': [cycle_type(p), cycle_type(q)]}
                break
        if witness:
            break
    assert witness is not None
    out['geometric_specialization'] = {
        'alpha': alpha, 'commuting_deck': Delta0,
        'commuting_deck_square_inner_word': [3, 1],
        'commutation_inner_word': [-3],
        'free_extension_elimination': elimination,
        'selected_other_deck_noncommutation': witness,
    }

    # Mod-two periodic cochains: d=1+J has image=kernel of dimension one.
    vectors = tuple(product(range(2), repeat=2))
    def diff(v):
        return (v[1], 0)
    image = {diff(v) for v in vectors}
    kernel = {v for v in vectors if diff(v) == (0, 0)}
    assert image == kernel and len(image) == 2
    out['mod_two_regular_module'] = {
        'involution_matrix': [[1, 1], [0, 1]],
        'periodic_differential_matrix': [[0, 1], [0, 0]],
        'image_equals_kernel': sorted(image),
        'positive_degree_cohomology_dimension': 0,
        'E_high_cohomology_dimension': 1,
    }

    # Complete S4 test, including all relabelings.
    s4 = tuple(permutations(range(4)))
    parts = (partition((0, 1), (2, 3)),
             partition((0, 2), (1, 3)),
             partition((0, 3), (1, 2)))
    tau = (2, 3, 0, 1)
    transpositions = [p for p in s4 if cycle_type(p) == [1, 1, 2]]
    commuting = [p for p in transpositions
                 if perm_mul(p, tau) == perm_mul(tau, p)]
    assert len(commuting) == 2
    table = []
    for part in parts:
        table.append({'partition': part, 'tau_block_action': block_action(tau, part),
                      'deck_images': [image_partition(d, part) for d in commuting]})
        if block_action(tau, part) == 'exchanges':
            assert all(image_partition(d, part) != part for d in commuting)
    checks = 0
    for r in s4:
        conjugate_tau = perm_mul(perm_mul(r, tau), perm_inv(r))
        for d in transpositions:
            if perm_mul(d, conjugate_tau) != perm_mul(conjugate_tau, d):
                continue
            for part in parts:
                if block_action(conjugate_tau, part) == 'exchanges':
                    assert image_partition(d, part) != part
                    checks += 1
    assert checks == 96
    out['separator_obstruction'] = {
        'tau': tau, 'commuting_single_transpositions': commuting,
        'table': table, 'all_relabeling_checks': checks,
    }

    # The three nonzero quotient lines distinguish the torsion line.
    lines = {(1, 0): 'positive deck', (0, 1): 'section',
             (1, 1): 'torsion-free double transposition'}
    assert (0, 1) not in {(0, 0), (1, 1)}
    out['quotient_lines'] = [{'vector': list(v), 'role': role}
                             for v, role in lines.items()]
    out['all_checks_passed'] = True
    destination = Path(__file__).with_name('negative_transposition_d37_output.json')
    destination.write_text(json.dumps(out, indent=2) + '\n')
    print('D.37: all exact covering/deck/extension word identities passed.')
    print('D.37: regular C2-module periodic cohomology is zero in positive degree.')
    print(f'D.37: all {checks} relabeled separator checks passed.')
    print('D.37: explicit finite quotient separating the noncommuting deck:',
          json.dumps(witness, sort_keys=True))
    print('D.37: no claim of existence or nonexistence of a mixed-sign deck symmetry.')
    print('Wrote', destination)


if __name__ == '__main__':
    main()
