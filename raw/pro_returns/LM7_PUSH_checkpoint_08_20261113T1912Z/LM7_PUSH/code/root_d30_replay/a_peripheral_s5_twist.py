#!/usr/bin/env python3
"""Exact integral class-algebra checks for the twisted A5 chief step.

Construct S5 from all120 permutations.  All products, parity-restricted
commutator distributions, A5-conjugacy classes, subgroup exclusions and
annihilation identities are enumerated over integers.  No character
table or group database is used.  The script saves the full coefficient
vectors, not only their class summaries.
"""

from collections import Counter, deque
from itertools import permutations, product
from pathlib import Path
import importlib.util
import json

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('finite_count', HERE/'a_peripheral_count.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def main():
    G = module.Group('S5', permutations(range(5)), module.perm_mul, tuple(range(5)))
    parity = [module.parity(g) for g in G.elements]
    even = {g for g in range(G.size) if parity[g] == 0}
    odd = set(range(G.size))-even
    assert len(even) == len(odd) == 60
    sigma = G.index[(1, 0, 2, 3, 4)]
    tau = [G.conjugate(sigma, g) for g in range(G.size)]

    def vector(elements):
        out = [0]*G.size
        for g in elements:
            out[g] += 1
        return out

    def sub(a, b):
        return [x-y for x, y in zip(a, b)]

    def convolution(a, b):
        out = [0]*G.size
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    if y:
                        out[G.mul[i][j]] += x*y
        return out

    zero = [0]*G.size
    unseen, classes = set(range(G.size)), []
    while unseen:
        g = min(unseen)
        c = {G.conjugate(h, g) for h in even}
        unseen -= c
        classes.append(c)
    assert len(classes) == 8
    class_of = {g: i for i, c in enumerate(classes) for g in c}
    five = [i for i, c in enumerate(classes) if G.orders[min(c)] == 5]
    assert len(five) == 2
    delta = sub(vector(classes[five[0]]), vector(classes[five[1]]))
    assert {tau[g] for g in classes[five[0]]} == classes[five[1]]

    def handles(H):
        hs = []
        for a, b in product(range(2), repeat=2):
            hs.append(vector(G.commutator(x, y) for x in H for y in H
                             if parity[x] == a and parity[y] == b))
        return hs

    K = handles(range(G.size))
    assert K[1] == K[2] == K[3]
    L = K[1]
    difference = sub(K[0], L)
    assert convolution(L, delta) == zero
    assert convolution(L, difference) == zero
    odd_classes = [i for i, c in enumerate(classes) if parity[min(c)]]
    for i in odd_classes:
        cvec = vector(classes[i])
        assert convolution(cvec, delta) == zero
        assert convolution(cvec, difference) == zero
    for a, b in product(classes, repeat=2):
        assert convolution(vector(a), vector(b)) == convolution(vector(b), vector(a))
    print('S5 restricted handle distributions K00, K01=K10=K11 by A5 classes:')
    for i, c in enumerate(classes):
        g = min(c)
        assert all(K[j][u] == K[j][g] for j in range(4) for u in c)
        print(i, 'parity', parity[g], 'order', G.orders[g], 'size', len(c),
              'counts', K[0][g], L[g])
    print('PASS: all integral S5 handle / odd-boundary annihilation identities')

    # Exhaustive subgroup lattice, used only for the precise proper-image
    # statement: a proper subgroup containing an odd permutation and a
    # five-cycle is one of the six normalizers C5 semidirect C4.
    one = frozenset([G.one])
    groups = {one: []}
    todo = deque([one])
    while todo:
        H = todo.popleft()
        for x in range(G.size):
            if x in H:
                continue
            gens = groups[H]+[x]
            J = G.generated(gens)
            if J not in groups:
                groups[J] = gens
                todo.append(J)
    candidates = [H for H in groups if len(H) < 120 and H & odd
                  and any(G.orders[x] == 5 for x in H)]
    assert len(groups) == 156
    assert len(candidates) == 6 and all(len(H) == 20 for H in candidates)
    normalizers = []
    cyclic5 = {G.generated([g]) for g in range(G.size) if G.orders[g] == 5}
    assert len(cyclic5) == 6
    for C in cyclic5:
        N = frozenset(g for g in range(G.size)
                      if {G.conjugate(g, c) for c in C} == C)
        assert len(N) == 20
        normalizers.append(N)
    assert set(candidates) == set(normalizers)
    print('PASS: all156 S5 subgroups; exactly six proper odd/five images, all F20')

    f20_records = []
    for H in sorted(candidates, key=lambda h: sorted(h)):
        J = handles(H)
        assert J[1] == J[2] == J[3]
        Cs = [C for C in cyclic5 if C <= H]
        assert len(Cs) == 1
        C = Cs[0]
        assert J[1] == [20*x for x in vector(C)]
        assert J[0] == [15*int(g in C)+25*int(g == G.one) for g in range(G.size)]
        assert all(G.orders[g] == 4 for g in H & odd)
        dH = [delta[g] if g in H else 0 for g in range(G.size)]
        diff = sub(J[0], J[1])
        assert convolution(J[1], dH) == zero
        assert convolution(J[1], diff) == zero
        for i in odd_classes:
            assert H & classes[i] in (set(), H & odd)
            v = vector(H & classes[i])
            assert convolution(v, dH) == zero
            assert convolution(v, diff) == zero
        # Intersections of all global A5 classes commute in this exact
        # embedded subgroup; this is the multiplication used by the count.
        intersections = [vector(H & c) for c in classes]
        for u, v in product(intersections, repeat=2):
            assert convolution(u, v) == convolution(v, u)
        f20_records.append({'elements': sorted(H), 'generators': groups[H],
                            'C5': sorted(C), 'handles': J,
                            'split_class_difference': dH,
                            'class_intersections': [sorted(H & c) for c in classes]})
    print('PASS: all six F20 handle / odd-boundary annihilation identities')

    # Verify all unit-power operations on every actual A5 conjugacy class
    # in S5, including its three odd classes.
    from math import gcd
    power_records = []
    for lam in range(60):
        if gcd(lam, 60) != 1:
            continue
        target = tau if lam % 5 in (2, 3) else list(range(G.size))
        for c in classes:
            assert {target[g] for g in c} == {G.power(g, lam) for g in c}
        power_records.append({'lambda_mod60': lam,
                              'outer_involution': lam % 5 in (2, 3)})
    print('PASS: all16 unit powers modulo60 on all eight A5 classes in S5')

    payload = {
        'status': 'PASS_TWISTED_S5_CLASS_ALGEBRA',
        'group_elements': G.elements, 'parity': parity,
        'A5_conjugacy_classes': [sorted(c) for c in classes],
        'class_metadata': [{'parity': parity[min(c)], 'order': G.orders[min(c)],
                            'size': len(c)} for c in classes],
        'outer_conjugation': tau, 'five_class_indices': five,
        'restricted_commutator_distributions': K,
        'split_class_difference': delta,
        'all_subgroups': [{'elements': sorted(H), 'generators': groups[H]}
                          for H in sorted(groups, key=lambda H: (len(H), sorted(H)))],
        'proper_odd_five_images': f20_records,
        'unit_powers': power_records,
        'scope': 'Exact finite identities used in the surface counting comparison. '
                 'No arbitrary-base chief theorem is asserted by this computation alone.'}
    HERE.joinpath('a_peripheral_s5_twist.json').write_text(json.dumps(payload, indent=2)+'\n')
    print(payload['status'])


if __name__ == '__main__':
    main()
