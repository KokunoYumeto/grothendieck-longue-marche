"""Exact H0/H1 comparison for the first second-cohomology filtration.

Only the specified quotient map V -> V_T2 direct-sum V_T3 is used.
The result does not claim an isomorphism in higher module cohomology.
"""
import json
import numpy as np
import check_universal_relation_module as b
from check_relation_small_quotients import cocycles, nullspace

qs=[]
smalls=[]
for which in ('T2','T3'):
    rel=np.concatenate([b.matrices[k-1]-np.eye(25,dtype=np.int64)
                        for k in b.data[which+'_indices']],axis=0)%2
    rr,piv=b.rref(rel,2)
    free=[j for j in range(25) if j not in piv]
    q=np.eye(25,dtype=np.int64)
    for row,j in zip(rr,piv):q=(q-q[:,j,None]*row[None,:])%2
    q=q[:,free]
    mats=[m[free,:]@q%2 for m in b.matrices]
    qs.append(q);smalls.append(mats)

q=np.concatenate(qs,axis=1)
assert b.rank_mod(q,2)==5
mats=[]
for i,m in enumerate(b.matrices):
    sm=np.zeros((5,5),dtype=np.int64)
    sm[:2,:2]=smalls[0][i]
    sm[2:,2:]=smalls[1][i]
    assert not np.any((m@q-q@sm)%2)
    mats.append(sm)

record=b.data['J_pc'];n=len(record[1])
rows,cob=cocycles(record,mats,2)
bigrows,bigcob=cocycles(record,b.matrices,2)
zz=nullspace(rows,2)
included=np.array([z.reshape(n,5)@q.T for z in zz],dtype=np.int64).reshape(len(zz),n*25)%2
assert not np.any(bigrows@included.T%2)
image=b.rank_mod(np.concatenate((bigcob,included)),2)-b.rank_mod(bigcob,2)
smallh1=len(zz)-b.rank_mod(cob,2)
bigh1=n*25-b.rank_mod(bigrows,2)-b.rank_mod(bigcob,2)
smallh0=5-b.rank_mod(cob,2)
bigh0=25-b.rank_mod(bigcob,2)
assert (smallh0,bigh0,smallh1,bigh1,image)==(0,0,1,1,1)
out={'prime':2,'group_order':record[0],'module_dimensions':[5,25],
     'H0_dimensions':[smallh0,bigh0],
     'H1_dimensions':[smallh1,bigh1],'H1_map_rank':image,
     'small_unknowns':5*n,'small_relation_rank':b.rank_mod(rows,2),
     'small_coboundary_rank':b.rank_mod(cob,2),
     'large_unknowns':25*n,'large_relation_rank':b.rank_mod(bigrows,2),
     'large_coboundary_rank':b.rank_mod(bigcob,2),
     'quotient_projection':q.tolist()}
(b.ROOT/'check_binary_first_filtration.json').write_text(json.dumps(out,indent=2)+'\n')
print('BINARY FIRST FILTRATION:',{k:v for k,v in out.items() if k!='quotient_projection'},flush=True)
