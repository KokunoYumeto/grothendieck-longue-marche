#!/usr/bin/env python3
"""Independent exact-integer invariant-lattice test for the residual C3.

Build A54 from the four integral degree-one generators, take an EXACT
integer group sum on the primitive rank320 quotient, select four
rationally independent columns, and saturate them by literal division
by three.  This does not reuse the other verifier's Smith transport.
"""
from pathlib import Path
import json
import time
import numpy as np

started=time.monotonic()
MOD=3**10
hall=[(i,j,k) for i in range(10) for j in range(i) for k in range(j,10)]
hi={h:i for i,h in enumerate(hall)}
inner=[hi[1,0,k] for k in range(10)]
keep=[i for i in range(330) if i not in inner]
global_data=np.load('deliverable/code/c_global_action_ambiguity_matrices.npz')
quotient_data=np.load('deliverable/code/c_char2_inner_quotient_matrices.npz')
residual_data=np.load('deliverable/code/c_action_ambiguity_refinement_matrices.npz')

def centered(A):
    return (A+MOD//2)%MOD-MOD//2

# Both degree-one matrices are exact unimodular integer inverses.
VB=quotient_data['VB']
VI=quotient_data['VBinv']
assert np.array_equal(VI@VB,np.eye(10,dtype=np.int64))

def key(A):return tuple(map(int,A.flatten()))
gens=global_data['geometric_generators_V']
group={key(np.eye(10,dtype=np.int64)):np.eye(10,dtype=np.int64)}
queue=list(group.values())
while queue:
    g=queue.pop()
    for h in gens:
        gh=g@h
        if key(gh) not in group:
            group[key(gh)]=gh;queue.append(gh)
            assert len(group)<=54
assert len(group)==54

def triple(i,j,k):
    if i==j:return []
    sign=1
    if i<j:i,j,sign=j,i,-1
    if k>=j:return [(hi[i,j,k],sign)]
    return [(hi[i,k,j],sign),(hi[j,k,i],-sign)]

def lie3_exact(M):
    nz=[[(i,int(M[i,j])) for i in range(10) if M[i,j]] for j in range(10)]
    L=np.zeros((330,330),dtype=np.int64)
    for column,(i,j,k) in enumerate(hall):
        for a,x in nz[i]:
            for b,y in nz[j]:
                for c,z in nz[k]:
                    for row,sign in triple(a,b,c):
                        L[row,column]+=sign*x*y*z
    return L

S=np.zeros((320,320),dtype=np.int64)
Qactions=[]
traces=[]
for g in group.values():
    adapted=VI@g@VB
    L=lie3_exact(adapted)
    assert not np.any(L[np.ix_(keep,inner)])
    Q=L[np.ix_(keep,keep)]
    Qactions.append(Q)
    S+=Q
    traces.append((int(np.trace(g))**3-int(np.trace(g@g@g)))//3-int(np.trace(g)))
assert sum(traces)==54*4
assert np.array_equal(S@S,54*S)
for q in Qactions:
    assert np.array_equal(q@S,S)
print('Exact integer average has rank4 and satisfies S^2=54S, gS=S: PASS',flush=True)

def rref(A,p):
    A=A.copy()%p
    piv=[];r=0
    for j in range(A.shape[1]):
        nz=np.flatnonzero(A[r:,j])
        if not len(nz):continue
        i=r+int(nz[0]);A[[r,i]]=A[[i,r]]
        A[r]=A[r]*pow(int(A[r,j]),-1,p)%p
        for k in range(A.shape[0]):
            if k!=r:A[k]=(A[k]-A[k,j]*A[r])%p
        piv.append(j);r+=1
        if r==A.shape[0]:break
    return A,piv

_,columns=rref(S,101)
assert len(columns)==4
K=S[:,columns].copy()
divisions=0
while True:
    reduced,piv=rref(K,3)
    if len(piv)==4:break
    j=next(i for i in range(4) if i not in piv)
    coeff=np.zeros(4,dtype=np.int64);coeff[j]=1
    for i,p in enumerate(piv):coeff[p]=-reduced[i,j]%3
    vector=K@coeff
    assert not np.any(vector%3)
    K[:,j]=vector//3
    divisions+=1
    assert divisions<50
for q in Qactions:
    assert np.array_equal(q@K,K)
print('Four exact invariant columns saturated at3 in',divisions,'literal divisions: PASS',flush=True)

# A unit minor makes their span primitive; rank4 is the entire invariant space.
_,minor_rows=rref(K.T,3)
minor_rows=minor_rows[:4]
assert len(minor_rows)==4
print('Unit minor rows:',minor_rows,flush=True)
print('Selected average columns:',columns,flush=True)

# The C-oriented residual is the same canonical negative line-cube vector.
if 'remaining_numerator' in residual_data:
    zfull=residual_data['remaining_numerator']%3
elif 'residual_numerator' in residual_data:
    zfull=residual_data['residual_numerator']%3
else:
    # Same vector independently saved by B; its canonical tensor formula was
    # independently checked by both scripts before this invariant test.
    zfull=np.load('deliverable/code/b_action_ambiguity_refinement_matrices.npz')['remaining_numerator']%3
projection=centered(quotient_data['quotient_projection'])
inclusion=centered(quotient_data['Lie_basis_change'][:,keep])
assert np.array_equal(projection@inclusion,np.eye(320,dtype=np.int64))
z=projection@zfull%3
_,piv=rref(np.column_stack((K,z)),3)
assert piv==[0,1,2,3,4]
print('Residual numerator is NOT in reduction of the exact invariant lattice: PASS',flush=True)

# A short explicit separating row: solve the four invariant coordinates on
# the selected unit minor, then test a fifth row.
minor=K[minor_rows,:]%3
aug,_=rref(np.column_stack((minor,z[minor_rows])),3)
coeff=aug[:4,4]
residue=(z-K@coeff)%3
r=int(np.flatnonzero(residue)[0])
inverse=np.zeros((4,4),dtype=np.int64)
for j in range(4):
    rhs=np.eye(4,dtype=np.int64)[:,j]
    rr,_=rref(np.column_stack((minor,rhs)),3)
    inverse[:,j]=rr[:4,4]
ell=np.zeros(320,dtype=np.int64)
ell[r]=1
for i,s in enumerate(minor_rows):ell[s]-=int((K[r,:]@inverse)[i])
ell%=3
assert not np.any(ell@K%3)
assert not np.any(ell@S%3)
assert int(ell@z%3)!=0
small=[(i,int(a)) for i,a in enumerate(ell) if a]
print('Five-or-fewer-entry invariant-lattice separator:',small,'; value',int(ell@z%3),flush=True)

result={'status':'independent exact integral average and saturation verified',
        'invariant_rank':4,'saturation_divisions':divisions,
        'unit_minor_rows':minor_rows,
        'selected_average_columns':columns,
        'average_unit_minor':S[np.ix_(minor_rows,columns)].tolist(),
        'residual_geometric_restriction_nonzero':True,
        'separator_quotient_coordinates':small,
        'separator_value':int(ell@z%3),
        'elapsed_seconds':time.monotonic()-started,
        'scope':'The fixed actual A54-module extension distinguishes the three formal B38 phases; this calculation alone does not identify that extension or select the actual phase.'}
Path('deliverable/code/c_geometric_extension_test.json').write_text(json.dumps(result,indent=2)+'\n')
np.savez_compressed('deliverable/code/c_geometric_extension_test_matrices.npz',
                    average_sum=S,invariant_basis_exact=K,residual_quotient_mod3=z,
                    separator=ell,quotient_projection_exact=projection)
print('Elapsed seconds:',round(time.monotonic()-started,3),flush=True)
