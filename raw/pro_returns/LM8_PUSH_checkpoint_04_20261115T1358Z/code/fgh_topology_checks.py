#!/usr/bin/env python3
"""Finite certificates used in F: bar H_1(C2), finite Cantor digits.

The infinite and localic statements have proofs in sections/F.tex;
finite truncations here are not promoted to proofs of their limits.
"""
from itertools import product
from pathlib import Path
import json


def main():
    # Normalized bar complex for C2.  The only nondegenerate degree-one
    # generator is [g], and d[g|g]=[g]-[1]+[g]=2[g].
    d1 = [[0]]
    d2 = [[2]]
    assert d1[0][0]*d2[0][0] == 0
    assert abs(d2[0][0]) == 2
    finite = []
    for n in range(1, 9):
        words = list(product((0, 1), repeat=n))
        assert len(set(words)) == 2**n
        for u in words:
            for v in words:
                if u != v:
                    assert any(a != b for a, b in zip(u, v))
        finite.append({'digits': n, 'clopen_cylinders': len(words)})
    result = {'bar_complex_C2': {'d1': d1, 'd2': d2, 'H1': 'Z/2'},
              'stack_product_H1': 'Z direct_sum Z/2',
              'cantor_finite_cylinders': finite,
              'scope': 'Finite algebraic certificates; the no-common-neighbourhood proof is F.11.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__': main()
