#!/usr/bin/env python3
"""Independent integral weighted-axis matrices for the proposed D90 range."""
from pathlib import Path
import hashlib
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


def valuation5(a):
    a = abs(int(a))
    if not a:
        return None
    n = 0
    while a % 5 == 0:
        a //= 5
        n += 1
    return n


def run():
    rows = []
    for m in range(4):
        n = 5**m
        eye = sp.eye(n)
        T, P = sp.zeros(n), sp.zeros(n)
        for j in range(n):
            T[(j+1) % n, j] = 1
            P[(2*j) % n, j] = 1
        M = 2*(eye+T)*P
        L = 2*P
        H = T**((-pow(2, -1, n)) % n) if n > 1 else eye
        Md = H*M
        assert (T-eye)*M == L*(T-eye)
        assert H*Md == M*H
        norm = sp.ones(n, 1)
        assert M*norm == 4*norm
        assert L*norm == 2*norm
        variants = {}
        for name, A in [('axis', M), ('diagonal', Md), ('weighted_permutation', L)]:
            snf = smith_normal_form(A-eye, domain=sp.ZZ)
            diag = [abs(int(snf[i, i])) for i in range(n)]
            assert all(diag)
            vals = sorted(v for v in map(valuation5, diag) if v)
            assert vals == list(range(1, m+1))
            variants[name] = {'integer_smith_diagonal': diag,
                              'nonzero_five_valuations': vals}
        rows.append({'depth_m': m, 'cyclic_order': n,
                     'actual_axis_operator': '2*(I+T)*Perm_2',
                     'actual_diagonal_half_gauge_exponent': (-pow(2, -1, n)) % n if n > 1 else 0,
                     'exact_augmentation_intertwining': True,
                     'exact_half_gauge_intertwining': True,
                     'norm_line_weight': 4,
                     'variants': variants,
                     'finite_coefficient_exponents': [
                         {'coefficient_exponent_e': e,
                          'cyclic_factor_exponents': [min(j,e) for j in range(1,m+1)]}
                         for e in range(1,6)]})
    return {'status':'PASS', 'scope':'Literal integral boundary matrices only; no claim about the infinite-layer extension or full D90 classification.',
            'rows':rows}


if __name__ == '__main__':
    result=run()
    result['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
