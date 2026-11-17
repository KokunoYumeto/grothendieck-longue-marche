#!/usr/bin/env python3
"""Pending exact crossing-mod8 refinement and lambda=5 fusion.

The sphere relation lattice is reduced over Z/4 with unit pivots.  The
lambda=5 correction solves the actual map V4 -> V4^2, not a reduction
of its target modulo2.
"""
from pathlib import Path
from itertools import combinations
import json
import numpy as np

HERE=Path(__file__).resolve().parent
B=json.loads((HERE/'check_sphere10_binary_extension.json').read_text())
pairs=list(combinations(range(10),2));ei={e:i for i,e in enumerate(pairs)}
rows=np.array([[int(i in e) for e in pairs] for i in range(10)]+[[1]*45],dtype=np.int64)
original_relations=rows.copy();pivots=[];rank=0
# The nine stars at0,...,8 together with the total relation are an
# integral basis of the relation lattice.  On the columns e_i9 and
# e01 their block determinant is 1-(1+1)=-1, proving saturation over Z.
minor_columns=[ei[(i,9)] for i in range(9)]+[ei[(0,1)]]
minor=original_relations[list(range(9))+[10]][:,minor_columns]
assert np.array_equal(minor[:9,:9],np.eye(9,dtype=np.int64))
assert np.array_equal(minor[9,:9],np.ones(9,dtype=np.int64))
assert minor[9,9]-int(minor[9,:9]@minor[:9,9])==-1
for j in range(44,-1,-1):
    options=np.flatnonzero(rows[rank:,j]%2)
    if not len(options):continue
    k=rank+int(options[0]);rows[[rank,k]]=rows[[k,rank]]
    rows[rank]=rows[rank]*int(rows[rank,j])%4
    for r in range(len(rows)):
        if r!=rank:rows[r]=(rows[r]-rows[r,j]*rows[rank])%4
    pivots.append(j);rank+=1
assert rank==10 and not rows[rank:].any()
free=[j for j in range(45) if j not in pivots]
assert free==B['quotient_basis_edges']


def quotient(vector):
    vector=np.asarray(vector,dtype=np.int64).copy()%4
    for row,pivot in zip(rows[:rank],pivots):vector=(vector-vector[pivot]*row)%4
    return vector[free]


permutations=[tuple(p) for p in B['colored_permutations']]
edge_perms=[[ei[tuple(sorted((p[a],p[b])))] for a,b in pairs] for p in permutations]
actions=[];crossings=[];beta=[]
for p,ep in zip(permutations,edge_perms):
    columns=[]
    for j in free:
        v=np.zeros(45,dtype=np.int64);v[ep[j]]=1;columns.append(quotient(v))
    actions.append(np.array(columns).T)
    inverse=[p.index(i) for i in range(10)]
    c=np.array([int(inverse[a]>inverse[b]) for a,b in pairs],dtype=np.int64)
    crossings.append(c);beta.append(quotient(c))
actions=np.array(actions);beta=np.array(beta)
for mask in range(32):
    for j in range(35):
        binary=sum(int(actions[mask,i,j]%2)<<i for i in range(35))
        assert binary==B['actions'][mask][j]
kappa=np.zeros((32,32,35),dtype=np.int64)
for a in range(32):
    for b in range(32):
        permuted=np.zeros(45,dtype=np.int64)
        permuted[edge_perms[a]]=crossings[b]
        d=crossings[a]+permuted-crossings[a^b]
        assert not (d%2).any()
        kappa[a,b]=quotient(d//2)
for a in range(32):
    for b in range(32):
        for c in range(32):
            assert np.array_equal((kappa[a,b]+kappa[a^b,c])%4,
                                  (actions[a]@kappa[b,c]+kappa[a,b^c])%4)
print('PASS saturated sphere quotient (Z/4)^35 and full colored crossing-mod8 cocycle',flush=True)


def binary_solve(matrix,vector):
    matrix=matrix.copy()%2;vector=vector.copy()%2;rank=0;piv=[]
    for j in range(matrix.shape[1]):
        options=np.flatnonzero(matrix[rank:,j])
        if not len(options):continue
        k=rank+int(options[0]);matrix[[rank,k]]=matrix[[k,rank]];vector[[rank,k]]=vector[[k,rank]]
        for r in range(len(matrix)):
            if r!=rank and matrix[r,j]:matrix[r]^=matrix[rank];vector[r]^=vector[rank]
        piv.append(j);rank+=1
        if rank==len(matrix):break
    assert not vector[rank:].any(),'inconsistent residual binary equations'
    solution=np.zeros(matrix.shape[1],dtype=np.int64)
    for i,j in enumerate(piv):solution[j]=vector[i]
    return solution,rank


def solve_mod4(matrix,vector):
    source=matrix.copy()%4;rhs=vector.copy()%4
    matrix=source.copy();vector=rhs.copy();rank=0;piv=[]
    for j in range(matrix.shape[1]):
        options=np.flatnonzero(matrix[rank:,j]%2)
        if not len(options):continue
        k=rank+int(options[0]);matrix[[rank,k]]=matrix[[k,rank]];vector[[rank,k]]=vector[[k,rank]]
        factor=int(matrix[rank,j]);matrix[rank]=matrix[rank]*factor%4;vector[rank]=vector[rank]*factor%4
        for r in range(len(matrix)):
            if r!=rank:
                coefficient=int(matrix[r,j])
                matrix[r]=(matrix[r]-coefficient*matrix[rank])%4
                vector[r]=(vector[r]-coefficient*vector[rank])%4
        piv.append(j);rank+=1
        if rank==len(matrix):break
    free=[j for j in range(matrix.shape[1]) if j not in piv]
    assert not (matrix[rank:]%2).any()
    assert not (vector[rank:]%2).any(),'odd residual obstruction'
    parity,even_rank=binary_solve(matrix[rank:,free]//2,vector[rank:]//2)
    solution=np.zeros(matrix.shape[1],dtype=np.int64);solution[free]=parity
    for i,j in enumerate(piv):solution[j]=(vector[i]-matrix[i,free]@parity)%4
    assert np.array_equal(source@solution%4,rhs)
    return solution,rank,even_rank


a,b=B['H_masks'];identity=np.eye(35,dtype=np.int64)
correction_matrix=np.vstack((identity-actions[a],identity-actions[b]))%4
correction_rhs=np.concatenate((2*beta[a],2*beta[b]))%4
w,unit_rank,even_rank=solve_mod4(correction_matrix,correction_rhs)
assert (unit_rank,even_rank)==(23,1)
assert np.array_equal(correction_matrix@w%4,correction_rhs)
print('PASS lambda5 exact pure correction over Z/4:23 unit pivots and1 residual2 pivot',flush=True)
for mask in (0,a,b,a^b):
    assert np.array_equal((identity-actions[mask])@w%4,2*beta[mask]%4)

raw_w=np.zeros(45,dtype=np.int64);raw_w[free]=w
relation_witnesses=[]
for mask in (a,b):
    transformed=np.zeros(45,dtype=np.int64);transformed[edge_perms[mask]]=raw_w
    defect=raw_w-transformed-2*crossings[mask]
    total_coefficient=int(defect[ei[(0,9)]]+defect[ei[(1,9)]]-defect[ei[(0,1)]])%4
    star_coefficients=[int(defect[ei[(i,9)]]-total_coefficient)%4 for i in range(9)]
    witness=np.array(star_coefficients)@original_relations[:9]+total_coefficient*original_relations[10]
    assert not ((defect-witness)%4).any()
    relation_witnesses.append({'permutation_mask':mask,'star_coefficients':star_coefficients,'total_coefficient':total_coefficient})
print('PASS exact star/total-relation witnesses and pointwise correction on the entire H preimage',flush=True)


def braid_crossings(word):
    permutation=list(range(10));raw=np.zeros(45,dtype=np.int64)
    for letter in word:
        j=abs(letter)-1
        edge=ei[tuple(sorted((permutation[j],permutation[j+1])))]
        raw[edge]=(raw[edge]+(1 if letter>0 else -1))%8
        permutation[j],permutation[j+1]=permutation[j+1],permutation[j]
    return tuple(permutation),raw


basis_words=[]
for edge in free:
    i,j=pairs[edge]
    basis_words.append(list(range(j,i+1,-1))+[i+1,i+1]+[-r for r in range(i+2,j+1)])
word=[letter for i,block in enumerate(basis_words) for repetition in range(int(w[i])) for letter in block]
p,raw=braid_crossings(word)
assert p==tuple(range(10)) and not (raw%2).any()
assert np.array_equal(quotient(raw//2),w)
print('PASS literal pure-braid correction word, length',len(word),flush=True)

# Raw crossing scaling is the standard finite GT generator formula.
# Verify every mixed generator and both sphere relations at all four units.
sphere=list(range(1,9))+[9,9]+list(range(8,0,-1))
full=list(range(1,10))*10
for lam in (1,3,5,7):
    for source_word in (sphere,full):
        target_word=[letter for j in source_word for letter in [j]*lam]
        p,raw=braid_crossings(target_word)
        assert p==tuple(range(10)) and not (raw%2).any()
        assert not quotient(raw//2).any()
    for i in range(1,10):
        p,raw=braid_crossings([i]*lam)
        normal=quotient((raw-np.eye(1,45,ei[(i-1,i)],dtype=np.int64)[0])//2)
        expected=((lam-1)//2)*quotient(np.eye(1,45,ei[(i-1,i)],dtype=np.int64)[0])%4
        assert np.array_equal(normal,expected)
for i in range(1,10):
    edge=np.zeros(45,dtype=np.int64);edge[ei[(i-1,i)]]=1
    assert (quotient(edge)%2).any()
print('PASS standard finite action at all lambda mod8 units and both global sphere relations',flush=True)

result={
    'scope':'Exact mod-four pure-abelian ten-point quotient and pure correction for lambda5, valid for every section over the named H permutations.',
    'label_order':['A0_first','A0_second','B0_first','B0_second','C0_first','C0_second','z','-z','1/z','-1/z'],
    'edge_order':pairs,'quotient_basis_edges':free,'relation_unit_pivots':pivots,
    'integral_relation_minor_columns':minor_columns,'integral_relation_minor_determinant':-1,
    'reduced_relation_rows':rows.tolist(),'actions':actions.tolist(),'cocycle':kappa.tolist(),
    'inversion_vectors':beta.tolist(),'H_masks':[a,b],
    'correction_matrix':correction_matrix.tolist(),'correction_rhs':correction_rhs.tolist(),
    'correction_vector':w.tolist(),'unit_pivots':unit_rank,'residual_two_pivots':even_rank,
    'correction_braid_word':word,'pure_basis_words':basis_words,
    'correction_relation_witnesses':relation_witnesses,
    'standard_finite_action':'(x,pi) -> (lambda*x+((lambda-1)/2)*c_pi,pi) modulo4',
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'),actions=actions,cocycle=kappa,beta=beta,
                    correction_matrix=correction_matrix,correction_rhs=correction_rhs,correction_vector=w)
print('PASS complete quaternary-extension certificate',flush=True)
