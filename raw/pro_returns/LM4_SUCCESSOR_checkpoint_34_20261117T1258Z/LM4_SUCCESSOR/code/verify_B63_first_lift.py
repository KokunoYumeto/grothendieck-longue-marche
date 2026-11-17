"""Independently verify the actual mod-nine identity-fibre calculation.

Use the integral invariant-covector model, independent Schreier
transversals and elimination, and literal source words.  The discovery
matrix coordinates are compared only at the end by the integral basis
change.  This does not construct an element of the full centralizer.
"""
from pathlib import Path
from collections import deque
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / 'work_DE'
DATA = WORK / 'next_3adic_symplectic'
braid_words = json.loads((WORK/'next_B59_image/common_base_braid_words.json').read_text())
short = json.loads((DATA/'short_word_certificate.json').read_text())
rigid = json.loads((DATA/'rigid_lift_certificate.json').read_text())
I = np.eye(10, dtype=np.int64)
eps = np.array([(-1)**j for j in range(11)], dtype=np.int64)
embedding = np.vstack([I, -eps[:10]])
braids = {}
for j in range(1, 11):
    for sign, block in [(1, [[2,-1],[1,0]]), (-1, [[0,1],[-1,2]])]:
        B = np.eye(11, dtype=np.int64)
        B[j-1:j+1,j-1:j+1] = block
        assert np.array_equal(eps@B, eps)
        A = (B@embedding)[:10] % 9
        assert np.array_equal(embedding@A % 9, B@embedding % 9)
        braids[sign*j] = A
    assert np.array_equal(braids[j]@braids[-j] % 9, I)

def normal(A):
    A = A % 9
    lead = next(int(x)%3 for x in A.flat if x%3)
    return A if lead == 1 else (-A)%9

def key(A):
    return (normal(A)%3).astype(np.uint8).tobytes()

def inverse(A):
    B = np.hstack([A%9, I.copy()])
    for j in range(10):
        pivot = next(i for i in range(j,10) if B[i,j]%3)
        B[[j,pivot]] = B[[pivot,j]]
        B[j] = B[j]*pow(int(B[j,j]), -1, 9)%9
        for i in range(10):
            if i != j:
                B[i] = (B[i]-B[i,j]*B[j])%9
    assert np.array_equal(B[:,:10], I)
    return B[:,10:]

def evaluate(word, generators):
    A = I.copy()
    for letter in word:
        A = A@generators[letter]%9
    return normal(A)

def lie(A):
    A = normal(A)
    assert np.array_equal(A%3, I)
    return (((A-I)%9)//3).reshape(-1)

def basis(vectors):
    pivots = {}
    for vector in vectors:
        v = np.array(vector, dtype=np.int64)%3
        for p, b in sorted(pivots.items()):
            v = (v-v[p]*b)%3
        nz = np.flatnonzero(v)
        if len(nz):
            p = int(nz[0])
            pivots[p] = v*pow(int(v[p]), -1, 3)%3
    return list(pivots.values())

def in_span(vector, spanning):
    return len(basis(spanning+[vector])) == len(basis(spanning))

groups = {}
spans = {}
for name, expected, dimension in [('T',144,6), ('C5',1440,9)]:
    ordered = sorted(braid_words[name].items(), key=lambda item:int(item[0]))
    # The braid table labels C5 generators 0,...,5; signed source words
    # in both certificates use 1,...,rank. Normalize that convention here.
    generators = {i+1:evaluate(word,braids) for i,(_,word) in enumerate(ordered)}
    for k,A in list(generators.items()):
        generators[-k] = inverse(A)
    groups[name] = generators
    reps = [I.copy()]
    lookup = {key(I):0}
    queue = deque([0])
    positive = list(range(1,len(ordered)+1))
    edges = []
    while queue:
        i = queue.popleft()
        for j in positive:
            A = normal(reps[i]@generators[j])
            k = key(A)
            if k not in lookup:
                lookup[k] = len(reps)
                reps.append(A)
                queue.append(lookup[k])
            edges.append((i,j,lookup[k]))
    assert len(reps) == expected
    inverses = [inverse(A) for A in reps]
    vectors = [lie(reps[i]@generators[j]@inverses[k]) for i,j,k in edges]
    spans[name] = basis(vectors)
    assert len(spans[name]) == dimension
    print(f'PASS {name}: independent mod3 image order {len(reps)}, '
          f'{len(edges)} Schreier edges, mod9 identity-fibre dimension {dimension}')

assert len(basis(spans['T']+spans['C5'])) == 12
print('PASS the full identity-fibre intersection has dimension 6+9-12=3')

def reduce_word(word):
    out = []
    for letter in word:
        if out and out[-1] == -letter:
            out.pop()
        else:
            out.append(letter)
    return out

def kill_h(word):
    # h=e6 e11 e6^-1 e5^-1, so e11=e6^-1 e5 e6.
    out = []
    for letter in word:
        out.extend([-6,5,6] if letter==11 else
                   [-6,-5,6] if letter==-11 else [letter])
    return reduce_word(out)

linking = json.loads((WORK/'full_pair_linking_certificate.json').read_text())
M = np.array(linking['full_matrix_rows_pairs_columns_basis'], dtype=np.int64)

def exponent_vector(word, rank):
    out = np.zeros(rank, dtype=np.int64)
    for letter in word:
        out[abs(letter)-1] += 1 if letter>0 else -1
    return out

tetra_words = rigid['normal_h_basis_actual_source_words']
assert len(tetra_words)==6
tetra_vectors = []
for word in tetra_words:
    assert not kill_h(word)
    assert not np.any(M@exponent_vector(word,13))
    tetra_vectors.append(lie(evaluate(word,groups['T'])))
assert len(basis(tetra_vectors))==6
assert len(basis(tetra_vectors+spans['T']))==6
print('PASS six actual words in normal<h> span the entire tetrahedral fibre; exact ambient H1 is zero')

cyclic_vectors = []
for word in short['cyclic_basis_words']:
    assert not np.any(exponent_vector(word,6))
    cyclic_vectors.append(lie(evaluate(word,groups['C5'])))
assert len(basis(cyclic_vectors))==9
assert len(basis(cyclic_vectors+spans['C5']))==9
print('PASS nine actual cyclic words with exact zero source abelianization span its entire fibre')

common = []
for i, pair in enumerate(short['common_actual_words']):
    t, c = pair['T_word'], pair['C5_word']
    assert not kill_h(t)
    assert not np.any(M@exponent_vector(t,13))
    assert not np.any(exponent_vector(c,6))
    A, B = evaluate(t,groups['T']), evaluate(c,groups['C5'])
    assert np.array_equal(A,B)
    common.append(lie(A))
    print(f'PASS matched direction {i}: literal source lengths {len(t)}/{len(c)}')
assert len(basis(common))==3
assert all(in_span(v,spans['T']) and in_span(v,spans['C5']) for v in common)
conjugated = (groups['T'][1]@common[0].reshape(10,10)@inverse(groups['T'][1])%3).reshape(-1)
assert not in_span(conjugated,common)
assert 144*3**(6-3)==3888 and 1440*3**(9-3)==1049760
print('PASS explicit nonnormality witness and factor refinement indices 3888/1049760')

change = I + np.ones((10,1),dtype=np.int64)*eps[:10]
change_inv = I - np.ones((10,1),dtype=np.int64)*eps[:10]
assert np.array_equal(change@change_inv,I)
discovery = np.array(short['common_basis'],dtype=np.int64)
for j, v in enumerate(common):
    assert np.array_equal((change@v.reshape(10,10)@change_inv%3).reshape(-1),discovery[:,j])

brackets = []
for i,j in [(0,1),(0,2),(1,2)]:
    A,B = common[i].reshape(10,10),common[j].reshape(10,10)
    bracket = (A@B-B@A)%3
    coeff = short['Lie_brackets'][f'{i},{j}']
    assert np.array_equal(bracket.reshape(-1),sum(int(c)*v for c,v in zip(coeff,common))%3)
    brackets.append(bracket.reshape(-1))
derived = basis(brackets)
assert len(derived)==2
for a in derived:
    for b in derived:
        A,B = a.reshape(10,10),b.reshape(10,10)
        assert not np.any((A@B-B@A)%3)
print('PASS exact displayed Lie brackets: derived algebra dimension2 and abelian')
print('PASS all mod9 certificates in an independent integral model')
print('Scope: exact finite-quotient intersections and source witnesses only; no full K element is constructed.')
