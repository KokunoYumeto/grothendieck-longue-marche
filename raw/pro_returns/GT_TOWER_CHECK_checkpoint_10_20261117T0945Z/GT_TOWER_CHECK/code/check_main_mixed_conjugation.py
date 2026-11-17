#!/usr/bin/env python3
"""Independent complete central-defect check for the finite braid bridge."""
import json
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
data = np.load(HERE/'check_main_mixed_capping.npz')
certificate = json.loads((HERE/'check_main_mixed_capping.json').read_text())
table = data['multiplication']
edges = data['mixed_edges']
words = certificate['mixed_words']
inverse = [int(np.flatnonzero(row == 0)[0]) for row in table]


def word_value(word):
    current = 0
    for letter in word:
        current = int(edges[current, letter-1])
    return current


def mul(*factors):
    current = 0
    for factor in factors:
        current = int(table[current, factor])
    return current


swap = [word_value([3-letter for letter in word]) for word in words]
assert sorted(swap) == list(range(432))
for i in range(432):
    assert swap[swap[i]] == i
    for j in range(2):
        assert swap[edges[i,j]] == edges[swap[i],1-j]
print('PASS independent cusp-swap automorphism on all432 vertices and864 edges')

derived = certificate['mixed_derived_indices']
D, V = int(edges[0,0]), int(edges[0,1])
values = []
for A in derived:
    B = inverse[swap[A]]
    defect = mul(A,inverse[B])
    assert mul(defect,D) == mul(D,defect)
    assert mul(defect,V) == mul(V,defect)
    assert mul(A,D,inverse[A]) == mul(B,D,inverse[B])
    values.append({'A': A, 'B': B, 'central_defect': defect,
                   'common_conjugate_D': mul(A,D,inverse[A])})
assert len(values) == 27
print('PASS all27 possible derived values give the same conjugation of D')

local=np.load(HERE.parent/'tower_code'/'local_mixed_quaternion_census.npz')['local_signed_matrices']
identity=np.eye(52,dtype=np.int64)
for name, matrix in [('a',local[0]),('d',local[2])]:
    fourth=np.asarray(matrix,dtype=np.int64)
    fourth=fourth@fourth%3
    fourth=fourth@fourth%3
    assert np.array_equal(fourth,identity)
assert mul(V,V,V,V)==0
print('PASS a^4=d^4=V^4=1, so the displayed finite gauge is the identity')

Path(__file__).with_suffix('.json').write_text(json.dumps({
    'scope':'The local conjugation comparison follows from the actual cusp swap and antisymmetry; no finite pentagon action on a larger quotient is inferred.',
    'cusp_swap':swap,'all_derived_value_checks':values,
    'gauge':'q_loc(a)^(8c) q_loc(V)^(-4c)=1 for every c',
    'proof_map':'A=f(D,V^2), B=f(D^2,V); swap(A)=f(V,D^2)=B^-1',
},indent=2)+'\n')
print('PASS complete independent finite conjugation certificate')
