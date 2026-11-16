#!/usr/bin/env python3
"""Test the residual coset against the actual finite geometric extension.

This is a WORK calculation, not a claim that the geometric extension
has been identified.  It asks whether the residual class restricts
trivially to H^1(A,Q), Q=Lie_3(V)/ad_w(V), for A of order54.
For y=z/3 the answer is yes iff z modulo3 lifts to Q^A.
"""
import ast
from collections import Counter
import json
from pathlib import Path
import time
import numpy as np

start=time.monotonic()
MOD=3**10
PREC=10
hall=[(i,j,k) for i in range(10) for j in range(i) for k in range(j,10)]
lookup={h:i for i,h in enumerate(hall)}
source=ast.parse(Path('deliverable/code/b_char2_symmetry.py').read_text())
exec(compile(ast.Module(body=[x for x in source.body if isinstance(x,ast.FunctionDef)
       and x.name in {'bracket','lie3','inverse_unit'}],type_ignores=[]),'Hall_functions','exec'))
glob=np.load('deliverable/code/b_global_action_ambiguity_matrices.npz')
ref=np.load('deliverable/code/b_action_ambiguity_refinement_matrices.npz')
quo=np.load('deliverable/code/c_char2_inner_quotient_matrices.npz')
projection=quo['quotient_projection']
inclusion=quo['Lie_basis_change'][:,quo['kept_indices']]
assert np.array_equal(projection@inclusion%MOD,np.eye(320,dtype=np.int64))
actions=[projection@g%MOD@inclusion%MOD for g in glob['geometric_actions']]
traces=sum((int(np.trace(g))**3-int(np.trace(g@g@g)))//3-int(np.trace(g))
           for g in glob['projective_automorphisms'])
assert traces%54==0
invariant_rank=traces//54
rank=320-invariant_rank
print('Exact character-average invariant rank:',invariant_rank,flush=True)

def partial_smith(B,rank):
    A=B.copy()%MOD
    n,m=A.shape
    Q=np.eye(n,dtype=np.int64)
    vals=[]
    for k in range(rank):
        active=A[k:,k:]
        power=1
        for val in range(PREC):
            nz=np.argwhere((active//power)%3)
            if len(nz):break
            power*=3
        else:raise AssertionError('Uncertified nonzero Smith pivot')
        i,j=map(int,nz[0]);i+=k;j+=k
        A[[k,i]]=A[[i,k]];Q[[k,i]]=Q[[i,k]]
        A[:,[k,j]]=A[:,[j,k]]
        inv=pow(int(A[k,k])//power,-1,MOD)
        A[k]=A[k]*inv%MOD;Q[k]=Q[k]*inv%MOD
        assert A[k,k]==power
        quotient=A[:,k]//power
        assert not np.any(A[:,k]%power)
        quotient[k]=0
        A=(A-quotient[:,None]*A[k][None,:])%MOD
        Q=(Q-quotient[:,None]*Q[k][None,:])%MOD
        for j in range(k+1,m):
            assert A[k,j]%power==0
            fac=int(A[k,j])//power
            if fac:A[:,j]=(A[:,j]-fac*A[:,k])%MOD
        vals.append(val)
    assert not np.any(A[rank:])
    return vals,Q

stack=np.hstack([(g-np.eye(320,dtype=np.int64)).T%MOD for g in actions])
vals,rows=partial_smith(stack,rank)
K=rows.T[:,rank:]
assert not np.any(stack.T@K%MOD)
print('Nonzero invariant-equation Smith pivots:',dict(sorted(Counter(vals).items())),flush=True)

# K reduces to the saturated invariant lattice: it is a direct summand,
# and the exact average /54 sends each approximate column to an actual
# integral invariant congruent modulo3 (error divisible3^7).
average_sum=np.zeros((320,4),dtype=np.int64)
for g in glob['projective_automorphisms']:
    qg=projection@lie3(g)%MOD@inclusion%MOD
    average_sum=(average_sum+qg@K)%MOD
assert np.array_equal(average_sum%MOD,(54*K)%MOD)

z=projection@ref['remaining_numerator']%MOD%3
aug=np.column_stack((K%3,z))
rr=0;piv=[]
for col in range(aug.shape[1]):
    nonzero=np.flatnonzero(aug[rr:,col])
    if not len(nonzero):continue
    i=rr+int(nonzero[0]);aug[[rr,i]]=aug[[i,rr]]
    aug[rr]=aug[rr]*int(aug[rr,col])%3
    for j in range(len(aug)):
        if j!=rr:aug[j]=(aug[j]-aug[j,col]*aug[rr])%3
    piv.append(col);rr+=1
assert piv[:4]==list(range(4))
trivial=len(piv)==4
print('Residual coset restricts trivially to geometric H1:',trivial,flush=True)
result={'invariant_rank':invariant_rank,
        'nonzero_Smith_histogram':dict(sorted(Counter(vals).items())),
        'residual_restriction_trivial':trivial,
        'scope':'Tests an additional fixed-geometric-extension condition only; does not identify the actual extension or select an arithmetic phase.',
        'elapsed_seconds':time.monotonic()-start}
Path('work/b_geometric_extension_test.json').write_text(json.dumps(result,indent=2)+'\n')
np.savez_compressed('work/b_geometric_extension_test_matrices.npz',
                    quotient_actions=np.stack(actions),invariant_basis_modulus=K,
                    residual_quotient_mod3=z,augmented_rref=aug)
print('Elapsed seconds:',round(time.monotonic()-start,3),flush=True)
