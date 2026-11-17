#!/usr/bin/env python3
"""Complete actual-word certificate for Omega containment and exact SO image."""
import numpy as np,json
from pathlib import Path
D=Path(__file__).parent;Z=np.load(D/'translation_quaternion_homology.npz');gs=Z['quaternion_kernel_generators'].astype(np.int16)
F=np.load(D/'translation_quaternion_image.npz')['form'].astype(np.int16);data=json.loads((D/'translation_quaternion_radical.json').read_text())
e=np.array(data['e'],dtype=np.int16);v=np.array(data['v'],dtype=np.int16);gi=data['source_generator'];n=18;I=np.eye(n,dtype=np.int16)
def rref(A):
 A=np.asarray(A,dtype=np.int16).copy()%3;r=0;ps=[]
 for j in range(A.shape[1]):
  ns=np.flatnonzero(A[r:,j])
  if not len(ns):continue
  k=r+int(ns[0]);A[[r,k]]=A[[k,r]];A[r]=A[r]*(1 if A[r,j]==1 else 2)%3
  ns=np.flatnonzero(A[:,j]);ns=ns[ns!=r];A[ns]=(A[ns]-A[ns,j,None]*A[r])%3;ps.append(j);r+=1
  if r==len(A):break
 return A[:r],ps
def minv(A):
 R,ps=rref(np.hstack((A,np.eye(len(A),dtype=np.int16))));assert ps[:len(A)]==list(range(len(A)));return R[:,len(A):]
def U(e,v):return (I+np.outer(v,e@F)-np.outer(e,v@F)-2*(v@F@v%3)*np.outer(e,e@F))%3
stabs=[(h,s,gs[h]) for h,s in data['stabilizer_generators']]
vs=[v];paths=[()];W,wp=rref([e,v])
for k,z in enumerate(vs):
 for hi,s,h in stabs:
  zz=s*h@z%3;T,tp=rref(np.vstack((W,zz)))
  if len(T)>len(W):W,wp=T,tp;vs.append(zz);paths.append((hi+1,)+paths[k])
  if len(vs)==16:break
 if len(vs)==16:break
assert len(vs)==16 and len(W)==17
mats=[]
for v,path in zip(vs,paths):
 h=I.copy()
 for j in path:h=h@gs[j-1]%3
 g=h@gs[gi]%3@minv(h)%3
 assert np.array_equal(g,U(e,v));mats.append(g)
for i,v in enumerate(vs):
 for j,w in enumerate(vs):assert np.array_equal(mats[i]@mats[j]%3,U(e,(v+w)%3))
op=next(j for j,h in enumerate(gs) if e@F@h@e%3)
f=gs[op]@e%3
assert f@F@f%3==0 and e@F@f%3
print('PASS16 explicit conjugate words generate full root radical; opposite generator',op,flush=True)
# Exact Cartan--Dieudonne reduction and spinor norm of every actual generator.
H=I.copy();orth=[]
while H.shape[1]:
 B=H.T@F%3@H%3;k=len(B);x=np.zeros(k,dtype=np.int16)
 ds=[i for i in range(k) if B[i,i]]
 if ds:x[ds[0]]=1
 else:
  i,j=next((i,j) for i in range(k) for j in range(i+1,k) if B[i,j]);x[i]=x[j]=1
 b=H@x%3;orth.append(b);row=b@F@H%3;R,ps=rref(row[None,:]);free=[i for i in range(k) if i not in ps]
 N=np.zeros((k,len(free)),dtype=np.int16);N[free]=np.eye(len(free),dtype=np.int16);N[ps]=-R[:,free]%3
 H=H@N%3
B=np.stack(orth,axis=1);assert len(rref(B)[0])==18 and np.count_nonzero(B.T@F%3@B%3)==18

def refl(v):
 q=int(v@F@v%3);assert q
 return (I+q*np.outer(v,v@F))%3,q
spinors=[];reflections=[]
for g in gs:
 A=g.copy();sn=1;rs=[]
 for b in orth:
  u=A@b%3
  if np.array_equal(u,b):continue
  w=(u-b)%3
  if w@F@w%3:
   R,q=refl(w);A=R@A%3;sn=sn*q%3;rs.append(w.tolist())
  else:
   w=(u+b)%3;R,q=refl(w);A=R@A%3;sn=sn*q%3;rs.append(w.tolist())
   R,q=refl(b);A=R@A%3;sn=sn*q%3;rs.append(b.tolist())
  assert np.array_equal(A@b%3,b)
 assert np.array_equal(A,I) and len(rs)%2==0
 spinors.append(sn);reflections.append(rs)
print('PASS actual determinant1 image contains Omega; generator spinor-norm counts',{j:spinors.count(j) for j in (1,2)},flush=True)
name='Omega_minus(18,3)' if all(s==1 for s in spinors) else 'SO_minus(18,3)'
print('EXACT ACTUAL QUATERNION MULTIPLICITY IMAGE',name,flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'Complete radical word certificate, opposite radical, and exact reflection reductions for actual quaternion multiplicity image',
 'actual_image':name,'root_generator_index':gi,'root_vector':e.tolist(),'radical_parameter_vectors':[v.tolist() for v in vs],
 'conjugating_words_in_360_generators':paths,'opposite_generator_index':op,'opposite_vector':f.tolist(),
 'orthogonal_basis':B.tolist(),'all_generator_spinor_norms':spinors,'all_reflection_factorizations':reflections},indent=2)+'\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'),radical_parameters=np.array(vs),radical_matrices=np.array(mats),root_vector=e,opposite_vector=f,orthogonal_basis=B)
