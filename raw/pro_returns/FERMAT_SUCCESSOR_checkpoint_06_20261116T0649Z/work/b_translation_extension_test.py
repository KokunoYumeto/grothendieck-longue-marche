#!/usr/bin/env python3
"""Restriction of the residual extension to the deck translation group."""
import runpy
import numpy as np
from collections import Counter
base=runpy.run_path('work/b_geometric_extension_test.py')
globals().update({key:value for key,value in base.items() if not key.startswith('__')})
all_trans=[g for g in glob['projective_automorphisms']
           if np.array_equal(g[:2,:2],np.eye(2,dtype=np.int64))]
assert len(all_trans)==9
chosen=[]
for index in [0,2]:
    target=np.eye(8,dtype=np.int64)[:,index]
    found=[g for g in all_trans if np.array_equal(-g[2:,2:]@np.ones(8,dtype=np.int64),target)]
    assert len(found)==1
    chosen.append(found[0])
actions=[projection@lie3(g)%MOD@inclusion%MOD for g in chosen]
invrank=sum((int(np.trace(g))**3-int(np.trace(g@g@g)))//3-int(np.trace(g))
           for g in all_trans)//9
stack=np.hstack([(g-np.eye(320,dtype=np.int64)).T%MOD for g in actions])
vals,rows=partial_smith(stack,320-invrank)
K=rows.T[:,320-invrank:]
assert not np.any(stack.T@K%MOD)
aug=np.column_stack((K%3,z))
rr=0;piv=[]
for col in range(aug.shape[1]):
    nz=np.flatnonzero(aug[rr:,col])
    if not len(nz):continue
    j=rr+int(nz[0]);aug[[rr,j]]=aug[[j,rr]]
    aug[rr]=aug[rr]*int(aug[rr,col])%3
    for j in range(len(aug)):
        if j!=rr:aug[j]=(aug[j]-aug[j,col]*aug[rr])%3
    piv.append(col);rr+=1
assert piv[:invrank]==list(range(invrank))
print('Translation invariant rank:',invrank,flush=True)
print('Translation Smith:',dict(sorted(Counter(vals).items())),flush=True)
print('Residual restriction trivial on translations:',len(piv)==invrank,flush=True)
np.savez_compressed('work/b_translation_extension_test_matrices.npz',
                    translation_V=np.stack(chosen),translation_Q=np.stack(actions),
                    invariant_basis=K,residual=z,augmented_rref=aug)
