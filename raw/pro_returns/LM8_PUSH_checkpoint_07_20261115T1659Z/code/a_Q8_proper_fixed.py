"""Finite exact certificates for the A.35 surface normal form.

The unbounded proof is in A.35. Modular full column ranks certify that
these sample integer slot matrices are injective over every Q_ell.
"""
from itertools import product
from pathlib import Path
import json


def rank(cols, prime=1000003):
    pivots = {}
    for raw in cols:
        v = {k: c % prime for k, c in raw.items() if c % prime}
        while v:
            k = max(v)
            if k not in pivots:
                inv = pow(v[k], -1, prime)
                pivots[k] = {j: c*inv % prime for j, c in v.items()}
                break
            fac = v[k]
            for j, c in pivots[k].items():
                a = (v.get(j, 0)-fac*c) % prime
                if a:
                    v[j] = a
                elif j in v:
                    del v[j]
    return len(pivots)


# Three distinct forbidden words have no self/mutual suffix-prefix overlap.
leading = [(0, 1), (2, 3), (4, 5)]
assert all(a[1:] != b[:1] for a in leading for b in leading)

# B = Q<u1,u2>, u0=-u1-u2, a=2,b=3, m=(5,5,7), w=3(u1+u2).
w = {0: 3, 1: 3}
us = [{0: -1, 1: -1}, {0: 1}, {1: 1}]
ms = [5, 5, 7]
rows = []
for n in range(10):
    words = list(product(range(2), repeat=n))
    for i in range(3):
        cols = []
        for word in words:
            col = {}
            for j, c in w.items():
                col[(j,)+word] = col.get((j,)+word, 0)+c
            for j, c in us[i].items():
                col[word+(j,)] = col.get(word+(j,), 0)+ms[i]*c
            cols.append(col)
        r = rank(cols)
        assert r == len(words)
        row = dict(first_tail=i, first_slot_degree=n, columns=len(words), rank=r)
        rows.append(row)
        print(row)

answer = {'nonoverlapping_leading_words': leading,
          'sample_lengths': {'a': 2, 'b': 3, 'd1': 5, 'd2': 7},
          'first_slot_operator': 'L_w + m_i R_ui',
          'finite_degree_only': rows,
          'unbounded_proof': 'A.35 normal-word slots and greatest first-slot degree'}
Path(__file__).with_suffix('.json').write_text(json.dumps(answer, indent=2)+'\n')
print('PASS: no overlap ambiguity and full column rank in every tested slot degree.')
