#!/usr/bin/env python3
"""The complete N_B-prime correction fibre in the rank-ten cubic cover mod4.

H=ker(F->C3^2); the finite target is B/[H,H]H^4.  The common target
with G6 has kernel K6 intersect [H,H]H^4.  Multipliers here are exactly
lambda=1 (m=0).  Only corrections in N_B' are enumerated; a negative
row does not exclude a whole CM matrix fibre or all K6 corrections.
"""
from pathlib import Path
from itertools import combinations, product
import importlib.util, json
import numpy as np
import sympy as sp

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('fermat_integral',HERE/'de_fermat_schreier.py')
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)
data=json.loads((HERE/'bc_cm_literal_words.json').read_text())
cert=np.load(HERE/'bc_cm_fermat_factorization.npz')
C=cert['N_B_commutator_images']
translation=cert['translation']
Ax,Ay=cert['deck_x'],cert['deck_y']
T=cert['T']
I=np.eye(10,dtype=np.int64)

def pivot_columns(A):
    A=np.asarray(A,dtype=np.int64).copy()%2;r=0;cols=[]
    for j in range(A.shape[1]):
        ids=np.flatnonzero(A[r:,j])
        if not len(ids):continue
        k=r+int(ids[0]);A[[r,k]]=A[[k,r]]
        for i in range(A.shape[0]):
            if i!=r and A[i,j]:A[i]^=A[r]
        cols.append(j);r+=1
        if r==A.shape[0]:break
    return cols

cols=pivot_columns(C)
assert len(cols)==6
D=C[:,cols]
rows=pivot_columns(D.T)
assert len(rows)==6
minor=sp.Matrix(D[rows,:])
det=int(minor.det())
assert det%2
minv=np.array(minor.adjugate(),dtype=np.int64)*pow(det,-1,4)%4
allconj=np.concatenate([C,translation@C,translation@translation@C],axis=1)%4
coordinates=minv@allconj[rows,:]%4
assert not np.any((D@coordinates-allconj)%4)
assert not np.any(T@D)
# These six actual commutators form a free rank-six Z/4 basis of the
# complete derived image, because their unit minor proves injectivity,
# every basis commutator is in their span, and that span is stable under
# the entire cyclic deck image of N_B.
pairs=list(combinations(range(97),2))
nw=data['N_B_basis_in_F']
basis_words=[]
for j in cols:
    a,b=pairs[j]
    basis_words.append(nw[a]+nw[b]+f.inverse_word(nw[a])+f.inverse_word(nw[b]))
assert all(np.array_equal(f.integral_abel(w),D[:,j]) for j,w in enumerate(basis_words))

def substitute(word,images):
    out=[]
    for a in word:
        out+=images[a] if a>0 else f.inverse_word(images[-a])
    return out
S=np.stack([f.integral_abel(substitute(w,{1:[2],2:[1]})) for w in f.NWORDS],axis=1)
R=np.stack([f.integral_abel(substitute(w,{1:[2],2:[-2,-1]})) for w in f.NWORDS],axis=1)
assert np.array_equal(S@S,I) and np.array_equal(R@R@R,I)
E=np.concatenate([I+S,I+R+R@R],axis=0)

Aq={(a,b):np.linalg.matrix_power(Ax,a)@np.linalg.matrix_power(Ay,b)
    for a,b in product(range(3),repeat=2)}
derivatives=[]
for w in f.NWORDS:
    q=(0,0);d=np.zeros((10,10),dtype=np.int64)
    for letter in w:
        qn=f.step(q,letter)
        if abs(letter)==2:d+=Aq[qn]-Aq[q]
        q=qn
    assert q==(0,0)
    derivatives.append(d)
def action_matrix(z):
    return (I+np.stack([d@z for d in derivatives],axis=1))%4

grid=np.array(list(product(range(4),repeat=6)),dtype=np.int64).T
deltas=D@grid%4
assert len({tuple(x) for x in deltas.T})==4**6
correction_errors=E@deltas%4
output=[]
for index,item in enumerate(data['CM_words_in_F']):
    z=f.integral_abel(item['word'])%4
    good=np.flatnonzero(np.all((E@z[:,None]+correction_errors)%4==0,axis=0))
    generating=[]
    parity_cache={}
    for j in good:
        target=(z+deltas[:,j])%4
        parity=tuple(target%2)
        if parity not in parity_cache:
            parity_cache[parity]=(len(pivot_columns(action_matrix(target)))==10)
        if parity_cache[parity]:generating.append(int(j))
    witness=None
    if generating:
        j=generating[0];v=grid[:,j];target=(z+deltas[:,j])%4
        word=list(item['word'])
        for a,w in zip(v,basis_words):word+=w*int(a)
        assert np.array_equal(f.integral_abel(word)%4,target)
        matrix=action_matrix(target)
        assert not np.any(E@target%4)
        assert int(sp.Matrix(matrix).det())%2
        witness={'correction_coefficients':v.tolist(),'literal_F_word':word,
                 'H_abelianization_mod4':target.tolist(),
                 'H_automorphism_matrix_mod4':matrix.tolist()}
    row={'certificate_index':index,'extra_CM_coset':item['extra_CM_coset'],
         'original_H_abelianization_mod4':z.tolist(),
         'number_of_hexagon_corrections':int(len(good)),
         'number_of_generating_corrections':len(generating),'witness':witness}
    output.append(row)
    print(json.dumps({k:v for k,v in row.items() if k not in ('witness','original_H_abelianization_mod4')}),flush=True)
result={'finite_target':'B/[H,H]H^4, H=ker(F->(Z/3)^2)',
        'literal_B_convention':'x=(r^-1 s)^2, y=(s r^-1)^2; r:x->y,y->(xy)^-1',
        'multiplier':1,'correction_source':'N_B-prime',
        'correction_image_invariant_factors':[4]*6,
        'correction_basis_commutator_indices':[list(pairs[j]) for j in cols],
        'correction_basis_F_words':basis_words,'unit_minor_rows':rows,
        'unit_minor_determinant':det,'S_matrix':S.tolist(),'R_matrix':R.tolist(),
        'records':output,
        'scope':'Exact generating correction fibres for the stated 24 G6 words with lambda=1 and corrections in N_B-prime. Negative rows do not exclude complete CM matrix fibres.'}
(HERE/'bc_cm_fermat_boundary.json').write_text(json.dumps(result,indent=2)+'\n')
np.savez_compressed(HERE/'bc_cm_fermat_boundary.npz',correction_basis=D,
                    correction_coordinates=coordinates,S=S,R=R,E=E,
                    abelian_action_derivatives=np.stack(derivatives))
print('Correction image: (Z/4)^6, certified by a unit minor of determinant',det)
print('Generating point counts [compatible, extra]:',
      [sum(bool(x['witness']) and x['extra_CM_coset']==c for x in output) for c in (False,True)])
print('PASS: exact cubic-cover boundary correction fibres computed.')
