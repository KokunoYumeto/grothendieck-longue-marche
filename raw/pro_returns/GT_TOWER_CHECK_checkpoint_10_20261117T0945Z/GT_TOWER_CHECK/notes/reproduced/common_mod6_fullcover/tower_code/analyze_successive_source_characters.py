#!/usr/bin/env python3
"""Find the exact source-character support of the successive-prime test."""
import test_fivepoint_cm_level as T
import numpy as np,json
from pathlib import Path
s=np.load(Path(__file__).with_name('build_coupled_cubic_two_layer.npz'))
e=np.load(Path(__file__).with_name('extract_coupled_base_fibers.npz'))
seed=481;v=[]
for _ in range(8):v.append(seed%3);seed//=3
lams=np.array(sorted({tuple(A@v%3) for A in s['actions']}),dtype=np.int16)
def rr(A):
 A=A.copy()%3;r=0;piv=[]
 for c in range(A.shape[1]):
  nz=np.flatnonzero(A[r:,c])
  if not len(nz):continue
  j=r+int(nz[0]);A[[r,j]]=A[[j,r]];A[r]=A[r]*pow(int(A[r,c]),-1,3)%3
  ns=np.flatnonzero(A[:,c]);ns=ns[ns!=r];A[ns]=(A[ns]-A[ns,c,None]*A[r])%3
  piv.append(c);r+=1
  if r==len(A):break
 return A[:r],piv
small,_=rr(lams);JI=(e['joint_R8_images'].reshape(289,8,8)@small.T).reshape(289,16)%3
chosen=[];B=[]
for j,row in enumerate(JI):
 R,_=rr(np.array(B+[row],dtype=np.int16))
 if len(R)>len(B):chosen.append(j);B.append(row)
B=np.array(B,dtype=np.int16);_,piv=rr(B);R,_=rr(np.hstack((B[:,piv],np.eye(4,dtype=np.int16))));C=JI[:,piv]@R[:,4:]%3
jci={q:j for j,q in enumerate(T.jchords)}
def chain(q,w):
 a=np.zeros(289,dtype=np.int16)
 for j in w:
  k=abs(j)-1
  if j>0:edge=(q,k);q=int(T.jtable[q,T.jgens[k]]);sign=1
  else:q=int(T.jtable[q,T.jinverse[T.jgens[k]]]);edge=(q,k);sign=-1
  if edge in jci:a[jci[edge]]+=sign
 return q,a
ops=[]
for q,sub in [(T.jgens[0],None),(T.jgens[1],None),(0,((2,),(1,))),(0,((2,),(-2,-1)))]:
 rows=[]
 for w in T.jloops:
  end,a=chain(q,w if sub is None else T.subst(w,sub));assert end==q
  rows.append(a@C%3)
 rows=np.array(rows);A=rows[chosen]
 assert np.array_equal(C@A%3,rows)
 ops.append(A)
chars=set()
for i in range(8):
 matrix=e['joint_R8_images'].reshape(289,8,8)[chosen,i,:]
 for lam in lams:chars.add(tuple(matrix@lam%3))
chars.discard((0,0,0,0));todo=list(chars)
for a in todo:
 for A in ops:
  b=tuple(A@a%3)
  if b not in chars:chars.add(b);todo.append(b)
print('Source nontrivial character support closed under free generators and S3:',len(chars),flush=True)
print('S-fixed characters:',sum(np.array_equal(ops[2]@a%3,a) for a in chars),flush=True)
print('Source sigma matrix:',ops[2].tolist(),flush=True)
np.savez_compressed(Path(__file__).with_suffix('.npz'),characters=np.array(sorted(chars)),coords=C,
 chosen=np.array(chosen),X=ops[0],Y=ops[1],S=ops[2],R=ops[3])
Path(__file__).with_suffix('.json').write_text(json.dumps({'nontrivial_character_count':len(chars),
 'S_fixed_count':sum(np.array_equal(ops[2]@a%3,a) for a in chars)},indent=2)+'\n')
