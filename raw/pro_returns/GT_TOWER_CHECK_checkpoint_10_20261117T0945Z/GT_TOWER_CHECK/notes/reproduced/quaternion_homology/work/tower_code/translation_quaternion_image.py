#!/usr/bin/env python3
"""Exact invariant-form checks for the actual quaternion multiplicity image.
Does not replace the actual generated image by an ambient orthogonal group.
"""
import numpy as np,json
from pathlib import Path
D=Path(__file__).parent;Z=np.load(D/'translation_quaternion_homology.npz');gs=Z['quaternion_kernel_generators'].astype(np.int16);H=Z['H18'].astype(np.int16)
n=18;pairs=[(i,j) for i in range(n) for j in range(i,n)];dim=len(pairs)
basis=np.zeros((dim,n,n),dtype=np.int16)
for k,(i,j) in enumerate(pairs):basis[k,i,j]=basis[k,j,i]=1

def rref(A):
 A=np.asarray(A,dtype=np.int16).copy()%3;r=0;ps=[]
 for j in range(A.shape[1]):
  nz=np.flatnonzero(A[r:,j])
  if not len(nz):continue
  k=r+int(nz[0]);A[[r,k]]=A[[k,r]];A[r]=A[r]*(1 if A[r,j]==1 else 2)%3
  ns=np.flatnonzero(A[:,j]);ns=ns[ns!=r];A[ns]=(A[ns]-A[ns,j,None]*A[r])%3;ps.append(j);r+=1
  if r==len(A):break
 return A[:r],ps
rows=np.zeros((0,dim),dtype=np.int16);used=[]
for k,g in enumerate(gs):
 eq=(np.einsum('ji,kjl,lm->kim',g,basis,g,optimize=True)-basis).reshape(dim,n*n).T%3
 old=len(rows);rows,ps=rref(np.vstack((rows,eq)))
 if len(rows)>old:used.append(k);print('Invariant symmetric form constraints',k,'rank',len(rows),flush=True)
 if len(rows)==dim-1:break
free=[j for j in range(dim) if j not in ps]
assert len(free)==1,('invariant form space',len(free))
v=np.zeros(dim,dtype=np.int16);v[free[0]]=1;v[ps]=-rows[:,free[0]]%3
F=(v[:,None,None]*basis).sum(axis=0)%3
assert len(rref(F)[0])==18
for g in gs:assert np.array_equal(g.T@F%3@g%3,F)
for h in H:assert np.array_equal(h.T@F%3@h%3,F)
# Exact determinant modulo3 and Witt type.
def det(A):
 A=A.copy()%3;d=1
 for j in range(len(A)):
  k=next(k for k in range(j,len(A)) if A[k,j])
  if k!=j:A[[k,j]]=A[[j,k]];d=-d
  x=int(A[j,j]);d=d*x%3;A[j]=A[j]*x%3
  for k in range(j+1,len(A)):A[k]=(A[k]-A[k,j]*A[j])%3
 return d%3
fd=det(F);witt='plus' if fd==2 else 'minus'
print('PASS unique nondegenerate invariant symmetric form, determinant',fd,'orthogonal type',witt,flush=True)
print('Generator determinant counts', {j:sum(det(g)==j for g in gs) for j in (1,2)},flush=True)
I=np.eye(n,dtype=np.int16);stats={}
for g in gs:
 r=len(rref(g-I)[0]);t=1;z=g.copy()
 while not np.array_equal(z,I) and t<=100:z=z@g%3;t+=1
 key=(r,t if t<=100 else '>100');stats[key]=stats.get(key,0)+1
print('Actual generator rank/order census',stats,flush=True)
np.savez_compressed(Path(__file__).with_suffix('.npz'),form=F,constraint_rows=rows,form_vector=v)
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'Exact invariant form of the actual generated18-dimensional representation; ambient orthogonal equality not claimed',
 'dimension':18,'invariant_form_dimension':1,'form':F.tolist(),'determinant':int(fd),'orthogonal_type':witt,
 'independent_constraint_generator_indices':used,'generator_rank_order_census':{str(k):v for k,v in stats.items()}},indent=2)+'\n')
