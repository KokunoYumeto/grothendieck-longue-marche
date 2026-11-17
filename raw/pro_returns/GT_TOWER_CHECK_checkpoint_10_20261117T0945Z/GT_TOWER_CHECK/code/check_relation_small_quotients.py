"""Find the exact small-module origin of the Shapiro H1 term."""
import check_universal_relation_module as base
import numpy as np
import json

def nullspace(a,p):
    rr,piv=base.rref(a,p)
    free=[j for j in range(a.shape[1]) if j not in piv]
    out=np.zeros((len(free),a.shape[1]),dtype=np.int64)
    for i,j in enumerate(free):
        out[i,j]=1
        for row,k in zip(rr,piv): out[i,k]=-row[j]%p
    assert not np.any(a@out.T%p)
    return out

def cocycles(record,mats,p):
    n=len(record[1]);d=mats[0].shape[0]
    mm=[mats[base.data['inverse_indices'][k-1]-1].T%p for k in record[4]]
    mi=[mats[k-1].T%p for k in record[4]]
    rows=[]
    for word in base.pc_words(record):
        blocks=np.zeros((n,d,d),dtype=np.int64);suffix=np.eye(d,dtype=np.int64)
        for letter in reversed(word):
            k=abs(letter)-1
            if letter>0:
                blocks[k]=(blocks[k]+suffix)%p;suffix=mm[k]@suffix%p
            else:
                blocks[k]=(blocks[k]-mi[k]@suffix)%p;suffix=mi[k]@suffix%p
        assert np.array_equal(suffix,np.eye(d,dtype=np.int64))
        rows.extend(blocks.transpose(2,0,1).reshape(d,n*d))
    rows=np.array(rows,dtype=np.int64)
    cob=np.concatenate([a-np.eye(d,dtype=np.int64) for a in mm],axis=1)%p
    return rows,cob

out=[]
for p in (2,3):
  for which in ('T2','T3','O2','O3'):
    inds=base.data[f'{which}_indices']
    rel=np.concatenate([base.matrices[k-1]-np.eye(25,dtype=np.int64) for k in inds],axis=0)%p
    rr,piv=base.rref(rel,p);free=[j for j in range(25) if j not in piv]
    q=np.eye(25,dtype=np.int64)
    for row,j in zip(rr,piv):q=(q-q[:,j,None]*row[None,:])%p
    q=q[:,free];d=len(free)
    mats=[m[free,:]@q%p for m in base.matrices]
    for m,sm in zip(base.matrices,mats):assert not np.any((m@q-q@sm)%p)
    for name in ('T_pc','J_pc'):
      record=base.data[name];n=len(record[1])
      rows,cob=cocycles(record,mats,p)
      zz=nullspace(rows,p)
      bigh,bigcob=cocycles(record,base.matrices,p)
      included=np.array([z.reshape(n,d)@q.T for z in zz],dtype=np.int64).reshape(len(zz),n*25)%p
      assert not np.any(bigh@included.T%p)
      image=base.rank_mod(np.concatenate((bigcob,included),axis=0),p)-base.rank_mod(bigcob,p)
      dim=len(zz)-base.rank_mod(cob,p)
      row={'p':p,'which':which,'group':name,'quotient_dimension':d,'H1_dimension':dim,'image_dimension':image}
      out.append(row);print('SMALL QUOTIENT:',row,flush=True)
(base.ROOT/'check_relation_small_quotients.json').write_text(json.dumps(out,indent=2)+'\n')
