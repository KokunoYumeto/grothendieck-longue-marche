#!/usr/bin/env python3
"""Search an exact root-radical certificate in the actual orthogonal image."""
import numpy as np,json
from pathlib import Path
D=Path(__file__).parent;Z=np.load(D/'translation_quaternion_homology.npz');gs=Z['quaternion_kernel_generators'].astype(np.int16)
F=np.load(D/'translation_quaternion_image.npz')['form'].astype(np.int16);n=18;I=np.eye(n,dtype=np.int16)
def rref(A):
 A=np.asarray(A,dtype=np.int16).copy()%3;r=0;ps=[]
 for j in range(A.shape[1]):
  ns=np.flatnonzero(A[r:,j])
  if not len(ns):continue
  k=r+int(ns[0]);A[[r,k]]=A[[k,r]];A[r]=A[r]*(1 if A[r,j]==1 else 2)%3
  ns=np.flatnonzero(A[:,j]);ns=ns[ns!=r];A[ns]=(A[ns]-A[ns,j,None]*A[r])%3;ps.append(j);r+=1
  if r==len(A):break
 return A[:r],ps
def canon(v):
 v=v%3;nz=np.flatnonzero(v)
 return tuple(map(int,v*(1 if not len(nz) or v[nz[0]]==1 else 2)%3))
def U(e,v):
 ef=e@F%3;vf=v@F%3
 return (I+np.outer(v,ef)-np.outer(e,vf)-2*(v@F@v%3)*np.outer(e,ef))%3
best=0;seen=set()
for gi,g in enumerate(gs):
 N=(g-I)%3
 if len(rref(N)[0])!=2 or np.any(N@N%3):continue
 B,ps=rref(N.T);B=B.T
 for t in ((1,0),(0,1),(1,1),(1,2)):
  e=np.array(canon(B@t));ek=tuple(e)
  if ek in seen:continue
  seen.add(ek)
  ef=e@F%3;j=next(j for j in range(n) if ef[j]);x=np.zeros(n,dtype=np.int16);x[j]=ef[j]
  v=N@x%3
  assert np.array_equal(U(e,v),g)
  stab=[]
  for hi,h in enumerate(gs):
   he=h@e%3
   if np.array_equal(he,e):stab.append((hi,1,h))
   elif np.array_equal(he,2*e%3):stab.append((hi,2,h))
  W,wp=rref([e,v]);witness=[([],e),([],v)]
  while True:
   old=len(W);new=[]
   for hi,s,h in stab:new.append(W@h.T%3)
   W,wp=rref(np.vstack([W]+new))
   if len(W)==old:break
  dim=len(W)-1
  if dim>best:best=dim;print('BEST radical',dim,'at generator',gi,'line',list(e),'stabilizing original generators',len(stab),flush=True)
  if dim==16:
   print('COMPLETE RADICAL FOUND',gi,flush=True)
   Path(__file__).with_suffix('.json').write_text(json.dumps({'source_generator':gi,'e':e.tolist(),'v':v.tolist(),'stabilizer_generators':[(a,b) for a,b,h in stab],'radical_dimension':dim},indent=2)+'\n')
   raise SystemExit
print('MAX',best,'isotropic lines checked',len(seen),flush=True)
