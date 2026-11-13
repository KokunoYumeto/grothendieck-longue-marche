#!/usr/bin/env python3
"""Actual A6 unit-power class maps for the odd-base chief comparison.

The exceptional outer group is retained from the independently certified
D31 automorphism enumeration. The target automorphism below is the
literal conjugation by (01) in S6, not an abstract class permutation.
"""
from itertools import permutations
from math import gcd
from pathlib import Path
import json
from a_peripheral_count import Group, parity, perm_mul

HERE = Path(__file__).resolve().parent


def inverse(a):
    b = [0]*len(a)
    for i, j in enumerate(a):
        b[j] = i
    return tuple(b)


def main():
    S = Group('A6', [p for p in permutations(range(6)) if parity(p) == 0],
              perm_mul, tuple(range(6)))
    odd = (1, 0, 2, 3, 4, 5)
    tau = [S.index[perm_mul(perm_mul(odd, g), inverse(odd))]
           for g in S.elements]
    assert sorted(tau) == list(range(360))
    assert all(tau[S.mul[g][h]] == S.mul[tau[g]][tau[h]]
               for g in range(360) for h in range(360))
    classes, unused = [], set(range(360))
    while unused:
        c = sorted(S.conjugacy_class(min(unused)))
        unused.difference_update(c)
        classes.append(c)
    assert len(classes) == 7
    class_of = {g: i for i, c in enumerate(classes) for g in c}
    odd_action = [class_of[tau[c[0]]] for c in classes]
    moved = [i for i, j in enumerate(odd_action) if i != j]
    assert len(moved) == 2
    assert all(S.orders[classes[i][0]] == 5 for i in moved)
    rows = []
    for lam in range(60):
        if gcd(lam, 60) != 1:
            continue
        use_odd = lam % 5 in (2, 3)
        actual = [class_of[S.power(c[0], lam)] for c in classes]
        expected = odd_action if use_odd else list(range(7))
        assert actual == expected
        for c in classes:
            powers = {S.power(g, lam) for g in c}
            images = {tau[g] if use_odd else g for g in c}
            assert powers == images
        rows.append({'lambda_mod_60': lam, 'odd_conjugation': use_odd,
                     'class_permutation': actual})
    raw = json.loads(HERE.joinpath('a_peripheral_a6_outer.json').read_text())
    aa, bb = raw['A6_generators']
    pair = [tau[aa], tau[bb]]
    index = raw['automorphism_generator_pairs'].index(pair)
    assert raw['automorphism_maps'][index] == tau
    outer = raw['outer_coordinates'][index]
    assert outer in (1, 2, 3)
    payload = {
        'status': 'PASS_A6_ODD_BASE_TARGET_COMPARISON',
        'group': 'Actual even permutations on six letters',
        'class_metadata': [{'index': i, 'size': len(c),
                            'order': S.orders[c[0]],
                            'representative': list(S.elements[c[0]])}
                           for i, c in enumerate(classes)],
        'odd_target_automorphism': {'permutation': list(odd),
                                    'map_on_360_elements': tau,
                                    'D31_Aut_A6_index': index,
                                    'D31_outer_coordinate': outer,
                                    'class_permutation': odd_action},
        'all_unit_power_checks': rows,
        'executed_units': len(rows),
        'proof_input': 'D31 certifies Z(A6)=1, simplicity and Out(A6)=C2^2. For odd D every homomorphism from a subgroup of D into this outer group is trivial.',
        'scope': 'Exact target maps in the odd-base A6 chief lifting/count proof. Mixed even bases remain outside this statement.'
    }
    HERE.joinpath('a_weight5_a6_odd.json').write_text(json.dumps(payload, indent=2)+'\n')
    print('PASS: seven A6 classes;', len(rows), 'unit powers modulo60;',
          'literal odd-S6 conjugation is Aut(A6) index', index,
          'with outer coordinate', outer)
    print(payload['status'])


if __name__ == '__main__':
    main()
