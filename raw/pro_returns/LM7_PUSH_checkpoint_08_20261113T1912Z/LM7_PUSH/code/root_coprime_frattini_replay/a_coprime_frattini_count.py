#!/usr/bin/env python3
"""Brute-force full peripheral fibres of small actual Frattini covers."""
from itertools import product
from pathlib import Path
import json
import numpy as np
from a_peripheral_count import Group
from a_coprime_frattini import Cover

HERE = Path(__file__).resolve().parent


def main():
    rows = []
    for order, p, y_exponent in ((3, 2, 1), (3, 2, 0), (2, 3, 0)):
        D = Group('C'+str(order), list(range(order)),
                  lambda a, b: (a+b) % order, 0)
        C = Cover(D, 1, y_exponent, p)
        elements = [(d, tuple(v)) for d in range(order)
                    for v in product(range(p), repeat=C.m)]
        def multiplication(a, b):
            v = (np.array(a[1])+C.actions[a[0]] @ np.array(b[1])) % p
            return D.mul[a[0]][b[0]], tuple(map(int, v))
        E = Group('actual universal Frattini cover', elements, multiplication,
                  (D.one, (0,)*C.m))
        Xi = []
        for value in C.peripherals:
            v = C.Mleft @ (value[1]-C.split(value[0])[1]) % p
            Xi.append(E.index[(value[0], tuple(map(int, v)))])
        assert len(E.generated(Xi[:2])) == E.size
        for lam in range(1, p*order):
            if np.gcd(lam, p*order) != 1:
                continue
            alpha = [(lam*d) % order for d in range(order)]
            classes = [E.conjugacy_class(E.power(a, lam)) for a in Xi]
            first = [a for a in classes[0] if E.elements[a][0] == alpha[C.x[0]]]
            second = [b for b in classes[1] if E.elements[b][0] == alpha[C.y[0]]]
            weak, proper = [], []
            for a, b in product(first, second):
                c = E.inv[E.mul[a][b]]
                if c not in classes[2]:
                    continue
                weak.append([a, b])
                if len(E.generated([a, b])) == E.size:
                    proper.append([a, b])
            compact = C.m-C.b
            if compact == 2:
                # C3 over F2: the compact module is F4 with nontrivial
                # C3 multiplication, so its automorphism group has order3.
                assert order == 3 and p == 2 and y_exponent == 1
                aut_compact, hom_compact_boundary = 3, 1
            else:
                assert compact == 0
                aut_compact, hom_compact_boundary = 1, 1
            ordinary_boundary_maps = 1
            for value in C.peripherals:
                ordinary_boundary_maps *= len(D.centralizer(value[0]))//D.orders[value[0]]
            predicted = (p**(order-1)*aut_compact*hom_compact_boundary*
                         ordinary_boundary_maps)
            assert len(proper) == predicted
            assert len(weak) == (16 if compact == 2 else predicted)
            rows.append({'base_order': order, 'p': p, 'y_exponent': y_exponent,
                         'actual_cover_order': E.size, 'lambda': lam,
                         'source_pair': Xi[:2], 'compact_rank': compact,
                         'boundary_map_count': ordinary_boundary_maps,
                         'predicted_generating_count': predicted,
                         'actual_generating_count': len(proper),
                         'actual_weak_count': len(weak),
                         'all_generating_source_pairs': proper,
                         'all_weak_source_pairs': weak})
            print('PASS D=C'+str(order), 'p='+str(p), 'y='+str(y_exponent),
                  'lambda='+str(lam), 'weak='+str(len(weak)),
                  'onto='+str(len(proper)), 'boundary maps='+str(ordinary_boundary_maps))
    payload = {'status': 'PASS_COMPLETE_SMALL_COPRIME_FRATTINI_FIBRES',
               'cases': rows,
               'scope': 'Exhaustive source pairs in actual groups of orders48 and54; includes the complete ordinary base-centralizer union.'}
    HERE.joinpath('a_coprime_frattini_count.json').write_text(
        json.dumps(payload, indent=2)+'\n')
    print(payload['status'])


if __name__ == '__main__':
    main()
