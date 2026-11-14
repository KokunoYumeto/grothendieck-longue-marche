#!/usr/bin/env python3
"""E.75: exact integral kernel coordinates for the wild relative source.

Every operation is over Q intersect Z_3.  Matrices and inverse maps are
retained as exact numerator/denominator pairs.  The module presentation
itself is proved in the accompanying section, not inferred from ranks.
"""
from __future__ import annotations

import importlib.util
import json
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

import sympy as sp
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SOURCE = HERE / 'e_unramified_sections.py'
if not SOURCE.is_file():
    SOURCE = ROOT / 'LM7_FERMAT_TOWER/code/e_unramified_sections.py'
spec = importlib.util.spec_from_file_location('e41_wild_kernel', SOURCE)
hall = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(hall)


def dense(columns):
    n = len(columns)
    return sp.Matrix(n, n, lambda i, j: columns[j].get(i, 0))


def v3(value):
    value = F(value)
    assert value
    n, d = abs(value.numerator), value.denominator
    ans = 0
    while n % 3 == 0:
        n //= 3
        ans += 1
    while d % 3 == 0:
        d //= 3
        ans -= 1
    return ans


def pivots_mod3(A):
    """Choose columns whose reductions are a basis of the column space."""
    basis, chosen = {}, []
    for j in range(A.cols):
        col = [int(A[i, j]) % 3 for i in range(A.rows)]
        for p in sorted(basis):
            if col[p]:
                f = col[p]
                col = [(a-f*b) % 3 for a, b in zip(col, basis[p])]
        if any(col):
            p = next(i for i, x in enumerate(col) if x)
            inv = pow(col[p], -1, 3)
            basis[p] = [inv*x % 3 for x in col]
            chosen.append(j)
    return chosen


def encoded(A):
    return [[[int(x.p), int(x.q)] for x in A.row(i)] for i in range(A.rows)]


def decoded(rows):
    return sp.Matrix([[sp.Rational(a,b) for a,b in row] for row in rows])


def mod3(A,m):
    modulus=3**m
    return A.applyfunc(lambda x: int(x.p)*pow(int(x.q),-1,modulus)%modulus)


def dvr_kernel(A):
    """Exact row reduction with integral changes of domain and codomain.

    Choosing the least 3-valuation pivot ensures every elimination factor
    is 3-integral.  The zero columns give a saturated kernel basis; the
    inverse domain map gives its coordinate inverse on the exact kernel.
    """
    B = [[F(x) for x in A.row(i)] for i in range(A.rows)]
    m, n = A.shape
    left = [[F(i == j) for j in range(m)] for i in range(m)]
    right = [[F(i == j) for j in range(n)] for i in range(n)]
    right_inv = [[F(i == j) for j in range(n)] for i in range(n)]
    valuations, operations = [], []
    for k in range(min(m, n)):
        options = [(v3(B[i][j]), i, j) for i in range(k, m)
                   for j in range(k, n) if B[i][j]]
        if not options:
            break
        valuation, i, j = min(options)
        assert valuation >= 0
        if i != k:
            B[i], B[k] = B[k], B[i]
            left[i], left[k] = left[k], left[i]
        if j != k:
            for matrix in [B, right]:
                for row in matrix:
                    row[j], row[k] = row[k], row[j]
            right_inv[j], right_inv[k] = right_inv[k], right_inv[j]
        pivot = B[k][k]
        assert v3(pivot) == valuation
        row_factors = []
        for i2 in range(m):
            if i2 == k or not B[i2][k]:
                continue
            f = B[i2][k]/pivot
            assert v3(f) >= 0
            B[i2] = [x-f*y for x, y in zip(B[i2], B[k])]
            left[i2] = [x-f*y for x, y in zip(left[i2], left[k])]
            row_factors.append([i2, f.numerator, f.denominator])
        column_factors = []
        for j2 in range(n):
            if j2 == k or not B[k][j2]:
                continue
            f = B[k][j2]/pivot
            assert v3(f) >= 0
            for matrix in [B, right]:
                for row in matrix:
                    row[j2] -= f*row[k]
            right_inv[k] = [x+f*y for x, y in zip(right_inv[k], right_inv[j2])]
            column_factors.append([j2, f.numerator, f.denominator])
        valuations.append(valuation)
        operations.append({'pivot':k, 'row_swap':i, 'column_swap':j,
                           'value':[pivot.numerator,pivot.denominator],
                           'rows':row_factors, 'columns':column_factors})
    L, R, Ri, D = map(sp.Matrix, [left, right, right_inv, B])
    rank = len(valuations)
    assert all(D[i,j] == 0 for i in range(m) for j in range(n) if i != j)
    assert L*A*R == D
    assert R*Ri == sp.eye(n) and Ri*R == sp.eye(n)
    assert all(F(x).denominator % 3 for matrix in [L,R,Ri] for x in matrix)
    K, C = R[:,rank:], Ri[rank:,:]
    assert A*K == sp.zeros(m,n-rank)
    assert C*K == sp.eye(n-rank)
    return {'rank':rank, 'dimension':n-rank,
            'valuation_counts':dict(sorted(Counter(valuations).items())),
            'kernel_basis':encoded(K), 'kernel_coordinate_map':encoded(C),
            'domain_transform':encoded(R), 'domain_inverse':encoded(Ri),
            'left_transform':encoded(L), 'diagonal':encoded(D),
            'operations':operations}


def main():
    H = hall.Hall(3)
    inputs = hall.arithmetic_inputs()
    out = {'status':'PASS', 'presentation':'(1-J)(T-7):A -> A-minus',
           'layers':{}, 'source_c_Kummer_matrix': [[-1,1],[0,1]],
           'relative_generator_character_columns': [[0,1],[1,1]]}
    assert sp.Matrix(out['source_c_Kummer_matrix'])**2 == sp.eye(2)
    G = sp.Matrix(out['relative_generator_character_columns'])
    assert G.det() % 3 and sp.Matrix(out['source_c_Kummer_matrix'])*G == G*sp.Matrix([[0,1],[1,0]])
    for r in [1,2,3]:
        T = dense(H.action(inputs['tau'],r)[0])
        J = dense(H.action(inputs['c'],r)[0])
        n = T.rows
        I = sp.eye(n)
        assert J*J == I
        plus, minus = I+J, I-J
        pc, mc = pivots_mod3(plus), pivots_mod3(minus)
        B = plus[:,pc].row_join(minus[:,mc])
        Bi = B.inv()
        assert B.cols == n and all(F(x).denominator % 3 for x in Bi)
        assert Bi*J*B == sp.diag(*([1]*len(pc)+[-1]*len(mc)))
        M = Bi[len(pc):,:]*(I-J)*(T-7*I)
        assert all(F(x).denominator % 3 for x in M)
        print('START',r,'RANK',n,'MINUS',len(mc),flush=True)
        row = dvr_kernel(M)
        D0 = (T-I)*plus[:,pc]
        d0 = dvr_kernel(D0)
        assert d0['rank'] == len(pc) and d0['dimension'] == 0
        # Exact index-two comparison with the Q3 invariant normalization.
        Pm = (I-J)/2
        assert Pm*(J+I) == sp.zeros(n,n)
        assert (I-J)*Pm == I-J
        assert Pm*minus[:,mc] == minus[:,mc]
        assert (I-J)*(T-7*I) == minus[:,mc]*M
        assert Pm*(T-7*I) == (T-7*I)-(I+J)*(T-7*I)/2
        finite_counts = []
        for m in range(1,7):
            d0_tors = sum(min(m,int(v))*int(count)
                          for v,count in d0['valuation_counts'].items())
            d1_tors = sum(min(m,int(v))*int(count)
                          for v,count in row['valuation_counts'].items())
            finite_h1_exp = m*(n-d0['rank'])+d0_tors+m*row['dimension']+d1_tors
            compact_h1_exp = m*(n+{1:5,2:1,3:0}[r])+d0_tors
            assert finite_h1_exp == compact_h1_exp+d1_tors
            finite_counts.append({'m':m, 'log3_H1_finite':finite_h1_exp,
                                  'log3_H1_compact_mod':compact_h1_exp,
                                  'log3_H2_compact_3m_torsion':d1_tors})
        Q=decoded(row['domain_transform'])
        Qi=decoded(row['domain_inverse'])
        diagonal=decoded(row['diagonal'])
        finite_transitions=[]
        transition_checks=0
        for m in range(2,8):
            source_factors=[]
            lower_factors=[]
            transition_factors=[]
            orders=[]
            for i in range(n):
                v=v3(diagonal[i,i]) if i<row['rank'] else None
                source_factors.append(3**max(m-v,0) if v is not None else 1)
                lower_factors.append(3**max(m-1-v,0) if v is not None else 1)
                transition_factors.append(source_factors[-1]//lower_factors[-1])
                orders.append(3**min(m,v) if v is not None else 3**m)
            modulus=3**m
            lower_modulus=3**(m-1)
            # Reducing the three-integral entries before multiplication is
            # exactly the same ring map, and avoids large rational products.
            Mm=np.array(mod3(M,m).tolist(),dtype=np.int64)
            Qm=np.array(mod3(Q,m).tolist(),dtype=np.int64)
            Qim=np.array(mod3(Qi,m-1).tolist(),dtype=np.int64)
            reps=Qm*np.array(source_factors,dtype=np.int64)[None,:]%modulus
            assert not np.any(Mm@reps%modulus)
            recovered=Qim@(reps%lower_modulus)%lower_modulus
            expected=np.diag([a*b%lower_modulus for a,b in zip(lower_factors,transition_factors)])
            assert np.array_equal(recovered,expected)
            transition_checks+=sum(o>1 for o in orders)
            finite_transitions.append({'from_m':m,'to_m':m-1,
                'source_generator_orders':orders,
                'coefficient_reduction_multipliers':transition_factors})
        b = {1:5,2:1,3:0}[r]
        assert row['dimension'] == len(pc)+b
        row.update({'degree':r,'A_rank':n,'plus_rank':len(pc),'minus_rank':len(mc),
                    'target_basis':encoded(minus[:,mc]),'split_basis':encoded(B),
                    'split_inverse':encoded(Bi),'matrix':encoded(M),
                    'degree0_map':{'matrix':encoded(D0),**d0},
                    'finite_cohomology_checks':finite_counts,
                    'finite_kernel_transitions':finite_transitions,
                    'verified_finite_transition_generators':transition_checks,
                    'index_two_invariant_comparison':'y maps to [y/2]; inverse [x] maps to [(1-J)x]',
                    'index_two_identities_exact':True})
        out['layers'][r] = row
        print('DEGREE',r,'EXTRA_KERNEL',row['dimension'],'MAP_RANK',row['rank'],
              'VALUATIONS',row['valuation_counts'],flush=True)
    (HERE/'a_wild_kernel.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
    print('PASS: exact saturated kernel bases, coordinate inverses and source involution.',flush=True)


if __name__ == '__main__':
    main()
