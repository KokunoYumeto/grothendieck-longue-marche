"""Exact torsion-diagonal spanning test in the two actual pair coinvariants.

The matrices are reconstructed from all integral graph actions, not inferred
from a representation name.  The A4 diagonal uses beta=r*s*r^-1, whose
action sends coordinate 1 to coordinate 5 by Ad_tau.
"""
import itertools
import json
import numpy as np
import check_universal_relation_module as b

out = []
for which in (2, 3):
    inds = b.data['T2_indices' if which == 2 else 'T3_indices']
    rel = np.concatenate([b.matrices[k-1]-np.eye(25,dtype=np.int64)
                          for k in inds],axis=0) % 2
    rr, piv = b.rref(rel, 2)
    free = [j for j in range(25) if j not in piv]
    q = np.eye(25,dtype=np.int64)
    for row,j in zip(rr,piv):
        q = (q-q[:,j,None]*row[None,:]) % 2
    q = q[:,free]
    n = len(free)
    assert n == (2 if which == 2 else 3)
    mats = [m[free,:]@q % 2 for m in b.matrices]
    for m, sm in zip(b.matrices,mats):
        assert not np.any((m@q-q@sm) % 2)
    ms = mats[b.data['s_index']-1]
    mr = mats[b.data['r_index']-1]
    mt = ms@mr % 2
    if which == 2:
        pairs = [(ms,mt),(mt,ms)]
        diagonal_action = np.eye(n,dtype=np.int64)
    else:
        pairs = [(ms,ms),(mt,ms@mr@mr@ms % 2)]
        # Right module g acts by Ad_(g^-1); Ad_tau is M_(tau^-1).
        diagonal_action = mr@mr@ms % 2
    flip = np.zeros((n*n,n*n),dtype=np.int64)
    for i in range(n):
        for j in range(n):
            if which == 2:
                flip[i*n+j,j*n+i] = 1
            else:
                for k in range(n): flip[i*n+j,j*n+k] = ms[i,k]
    eye = np.eye(n*n,dtype=np.int64)
    relations = np.concatenate([np.kron(a,c)-eye for a,c in pairs]
                               + [flip-eye],axis=0) % 2
    diagonals = np.array([np.kron(np.array(v,dtype=np.int64),
                                 np.array(v,dtype=np.int64)@diagonal_action % 2)
                          for v in itertools.product(range(2),repeat=n)],
                         dtype=np.int64)
    rank = b.rank_mod(relations,2)
    total = b.rank_mod(np.concatenate((relations,diagonals)),2)
    assert rank == len(b.rref(relations,2)[1])
    assert total == len(b.rref(np.concatenate((relations,diagonals)),2)[1])
    assert total == n*n
    coinvariant_dimension = n*n-rank
    assert coinvariant_dimension == (1 if which == 2 else 2)
    row = {'matching':'S3' if which == 2 else 'A4',
           'coordinates':[1,2] if which == 2 else [1,5],
           'torsion':'s' if which == 2 else 'r*s*r^-1',
           'factor_dimension':n,'s_matrix':ms.tolist(),'r_matrix':mr.tolist(),
           'diagonal_action':diagonal_action.tolist(),
           'relation_rank':rank,'coinvariant_dimension':coinvariant_dimension,
           'rank_after_diagonals':total,
           'diagonal_image_rank':total-rank,
           'relations':relations.tolist(),'diagonals':diagonals.tolist(),
           'quotient_projection':q.tolist()}
    out.append(row)
    print('TORSION DIAGONALS:', {k:v for k,v in row.items()
                                if k not in ('relations','diagonals','quotient_projection')},
          flush=True)

(b.ROOT/'check_binary_torsion_diagonals.json').write_text(json.dumps(out,indent=2)+'\n')
print('All three actual binary pair coinvariant classes are spanned by torsion diagonals.',flush=True)
