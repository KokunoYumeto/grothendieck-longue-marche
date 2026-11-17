"""Export the exact dual module maps used for the H2 comparison."""
import check_universal_relation_module as b
import numpy as np
import json
import sys

expanded='--expanded' in sys.argv

for p in (2,3):
    qs=[]
    for key in ((('O3','T2') if expanded else ('T2','T3')) if p==2 else ('O2',)):
        rel=np.concatenate([b.matrices[k-1]-np.eye(25,dtype=np.int64)
                            for k in b.data[key+'_indices']],axis=0)%p
        rr,piv=b.rref(rel,p);free=[j for j in range(25) if j not in piv]
        q=np.eye(25,dtype=np.int64)
        for row,j in zip(rr,piv):q=(q-q[:,j,None]*row[None,:])%p
        qs.append(q[:,free])
    q=np.concatenate(qs,axis=1)%p
    _,piv=b.rref(q.T,p)
    assert len(piv)==q.shape[1]
    # Find a right inverse from independent rows.
    selected=piv
    aug=np.concatenate((q[selected,:],np.eye(len(selected),dtype=np.int64)),axis=1)
    rr,pp=b.rref(aug,p)
    assert pp==list(range(len(selected)))
    section=np.zeros((q.shape[1],25),dtype=np.int64)
    section[:,selected]=rr[:,len(selected):]
    assert np.array_equal(section@q%p,np.eye(q.shape[1],dtype=np.int64))
    small=[section@m@q%p for m in b.matrices]
    for m,sm in zip(b.matrices,small):assert not np.any((m@q-q@sm)%p)
    full_dual=[b.matrices[i-1].T%p for i in b.data['inverse_indices']]
    small_dual=[small[i-1].T%p for i in b.data['inverse_indices']]
    embed=q.T%p
    for fm,sm in zip(full_dual,small_dual):assert not np.any((sm@embed-embed@fm)%p)
    text=('RelationFullMats:='+json.dumps([a.tolist() for a in full_dual])+';;\n'
          +'RelationSmallMats:='+json.dumps([a.tolist() for a in small_dual])+';;\n'
          +'RelationEmbed:='+json.dumps(embed.tolist())+';;\n')
    suffix='_expanded' if expanded else ''
    (b.ROOT/f'relation_cohomology_modules_{p}{suffix}.g').write_text(text)
    print(f'Exported p={p}, A dimension={q.shape[1]}, all 144 dual module maps checked.',flush=True)
