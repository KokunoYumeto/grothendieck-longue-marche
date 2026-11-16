"""Exact homogeneous UT4 s-frame correction for the W_free=0 action.

This checks the coefficient map only. The actual lower/ordinary source
and frame witnesses, and the later scalar refinement, are separate inputs.
"""
from pathlib import Path
import json,itertools
import numpy as np
HERE=Path(__file__).resolve().parent
raw=json.loads((HERE.parent/'next_cup_cocycle_matrices.json').read_text())
cc=json.loads((HERE.parents[1]/'work_A/A63_zero_t_cross_cup_square.json').read_text())
def mul(a,b):
 out=0
 while b:
  if b&1:out^=a
  b>>=1;a<<=1
  if a&8:a^=11
 return out
def pw(a,n):
 out=1
 for _ in range(n):out=mul(out,a)
 return out
M=np.array([[mul(a,b)for b in range(8)]for a in range(8)],dtype=np.uint8)
def mm(A,B):
 out=np.zeros((A.shape[0],B.shape[1]),dtype=np.uint8)
 for j in range(A.shape[1]):out^=M[A[:,j,None],B[j,None,:]]
 return out
def reduce(A):
 A=A.copy();r=0;piv=[]
 for j in range(A.shape[1]):
  v=np.flatnonzero(A[r:,j])
  if not len(v):continue
  k=r+int(v[0]);A[[r,k]]=A[[k,r]]
  A[r]=M[pw(int(A[r,j]),6),A[r]]
  for k in range(A.shape[0]):
   if k!=r and A[k,j]:A[k]^=M[A[k,j],A[r]]
  piv.append(j);r+=1
  if r==A.shape[0]:break
 return A,piv
def rank(A):return len(reduce(A)[1])
def kernel(A):
 R,piv=reduce(A);free=[i for i in range(A.shape[1])if i not in piv];out=[]
 for j in free:
  x=np.zeros(A.shape[1],dtype=np.uint8);x[j]=1
  for i,k in enumerate(piv):x[k]=R[i,j]
  out.append(x)
 return np.array(out,dtype=np.uint8).T
def cube_matrix(key):
 # Input columns have squared scalars; inverse Frobenius gives power4,
 # then cubic gives total power12=5 modulo7.
 return np.array([[pw(a,5)for a in col]for col in raw[key]],dtype=np.uint8).T
S,C,B=[cube_matrix(k)for k in('S2','C2','BETA2')]
D=mm(B,C);I=np.eye(36,dtype=np.uint8)
assert np.array_equal(mm(S,S),I)and np.array_equal(mm(D,D),I)
assert np.array_equal(mm(S,D),mm(D,S))
SF=kernel(I^S);JF=kernel(np.vstack((I^S,I^D)))
SN=mm(I^D,SF)
assert SF.shape[1]==20 and JF.shape[1]==12 and rank(SN)==8
pairs=list(itertools.combinations(range(4),2));pi={p:i for i,p in enumerate(pairs)}
triples=list(itertools.combinations(range(4),3))
L=np.array([row[:4]for row in cc['canonical_c_corrections']],dtype=np.uint8)
J=np.zeros((4,16),dtype=np.uint8)
for k,(i,j,l)in enumerate(triples):
 for r in range(4):
  J[k,4*r+l]^=L[pi[i,j],r]
  J[k,4*r+i]^=L[pi[j,l],r]
chosen=[2,4,8,9]
minor=J[:,chosen]
assert minor.tolist()==[[7,6,7,0],[0,2,0,0],[0,0,2,0],[0,0,0,2]]
assert rank(J)==4
images=[]
for i in range(16):
 for v in JF.T:images.append(M[J[:,i,None],v[None,:]].reshape(-1))
ZI=np.array(images,dtype=np.uint8).T
assert rank(ZI)==48
ui=[]
for i in range(4):
 for v in SN.T:
  a=np.zeros((4,36),dtype=np.uint8);a[i]=v;ui.append(a.reshape(-1))
UI=np.array(ui,dtype=np.uint8).T
assert rank(UI)==32 and rank(np.concatenate((UI,ZI),axis=1))==48
print('Actual L_c upper-right4x16 map rank4; displayed triangular minor: PASS')
print('S-fixed20, joint(S,D)-fixed12, U-only norm8 per copy: PASS')
print('Ordinary joint-fixed homogeneous corrections span all48 UT4 joint-fixed directions.')
print('U-only norm rank32; induced ordinary correction on the Tate quotient rank16: PASS')
out=dict(scope='Conditional homogeneous s-frame repair for actual W_free=0 combined20 quotient; scalar and retained-frame gates stated separately',
 L_c=L.tolist(),J=J.tolist(),minor_columns=chosen,minor=minor.tolist(),rank_J=4,
 S_fixed=20,joint_fixed=12,one_copy_norm_rank=8,
 ordinary_to_UT4_joint_rank=48,U_only_norm_rank=32,Tate_quotient_rank=16)
(HERE.parent/'A66_UT4_frame_surjection.json').write_text(json.dumps(out,indent=2)+'\n')
