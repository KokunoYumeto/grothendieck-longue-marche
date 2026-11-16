#!/usr/bin/env python3
"""Exact finite checks supporting the unbounded criterion in A.38.

No Galois element is constructed from this finite linear certificate.
The all-weight and actual-group arguments are in the manuscript.
"""
from itertools import product
from pathlib import Path
import json
import sympy as sp


def sparse_rank(columns):
    pivots = {}
    for col in columns:
        v = {k: sp.Rational(a) for k, a in col.items() if a}
        while v:
            p = max(v)
            if p not in pivots:
                c = v[p]
                pivots[p] = {k: a/c for k, a in v.items()}
                break
            c = v[p]
            for k, a in pivots[p].items():
                v[k] = v.get(k, 0) - c*a
                if not v[k]:
                    del v[k]
    return len(pivots)


slots = []
for n in range(5):
    words = list(product(range(4), repeat=n))  # 0=t, 1,2,3=u_i
    for lam, m, ui in [(0,1,1),(1,2,2),(-2,3,3)]:
        columns = []
        for word in words:
            c = {}
            for target, coefficient in [((0,)+word,lam),
                                         (word+(ui,),m)]:
                c[target] = c.get(target,0)+coefficient
            columns.append(c)
        rank = sparse_rank(columns)
        assert rank == len(words)
        slots.append({'slot_length':n,'lambda':lam,'m':m,
                      'u_index':ui,'rank':rank,'dimension':len(words)})


# Filtered Frobenius with four scalar graded blocks of dimension two.
# Arbitrary extensions between distinct eigenvalue blocks are allowed.
q = 7
weights = [1,1,2,2,3,3,4,4]
dim = len(weights)
F = sp.diag(*(q**m for m in weights))
for i in range(dim):
    for j in range(dim):
        if weights[i] < weights[j]:
            F[i,j] = (i+2)*(j+3) - 1
minimal_product = sp.eye(dim)
for m in sorted(set(weights)):
    minimal_product = minimal_product*(F-q**m*sp.eye(dim))
assert minimal_product == sp.zeros(dim)

# A filtered automorphism inducing the identity on all graded pieces is
# I+N with N strictly above the graded block diagonal. Commutation with
# F gives a homogeneous linear system in N, whose kernel must be zero.
positions = [(i,j) for i in range(dim) for j in range(dim)
             if weights[i] < weights[j]]
columns = []
for i,j in positions:
    N = sp.zeros(dim)
    N[i,j] = 1
    M = F*N-N*F
    columns.append(sp.Matrix(dim*dim,1,list(M)))
commutator_matrix = sp.Matrix.hstack(*columns)
rank = commutator_matrix.rank()
assert rank == len(positions)

result = {
 'status':'PASS',
 'first_slot_exact_ranks':slots,
 'commuting_frobenius':{
   'q':q,'graded_exponents':weights,
   'frobenius_matrix':[list(F.row(i)) for i in range(dim)],
   'distinct_factor_polynomial_annihilates':True,
   'strict_filtration_parameters':len(positions),
   'commutator_rank':rank,'kernel_dimension':0},
 'scope':'Finite exact checks only. A.38 proves the criterion in all weights and applies it to actual pro-prime fixed subgroups.'
}
out=json.dumps(result,indent=2,default=int)+'\n'
Path(__file__).with_suffix('.json').write_text(out)
print(out,end='')
