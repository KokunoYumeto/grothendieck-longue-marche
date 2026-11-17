#!/usr/bin/env python3
"""Project exact source-framed solution fibers to the successive-prime base."""
import test_full_source_framing as S
T=S.T;R=S.R
import numpy as np,json
from pathlib import Path

def affine(A,b,p):
 A=A.copy()%p;b=b.copy()%p;r=0;piv=[]
 for c in range(A.shape[1]):
  nz=np.flatnonzero(A[r:,c])
  if not len(nz):continue
  k=r+int(nz[0]);A[[r,k]]=A[[k,r]];b[[r,k]]=b[[k,r]]
  scale=pow(int(A[r,c]),-1,p);A[r]=A[r]*scale%p;b[r]=b[r]*scale%p
  ns=np.flatnonzero(A[:,c]);ns=ns[ns!=r];sc=A[ns,c].copy()
  A[ns]=(A[ns]-sc[:,None]*A[r])%p;b[ns]=(b[ns]-sc*b[r])%p
  piv.append(c);r+=1
  if r==len(A):break
 assert not np.any(A[r:]) and not np.any(b[r:])
 free=[j for j in range(A.shape[1]) if j not in piv]
 v=np.zeros(A.shape[1],dtype=np.int16);v[piv]=b[:r]
 N=np.zeros((len(free),A.shape[1]),dtype=np.int16)
 N[:,free]=np.eye(len(free),dtype=np.int16);N[:,piv]=-A[:r,free].T;N%=p
 return v,N

fr=next(fr for fr in T.frames if fr['rho']==0 and fr['T_sign']==-1 and fr['T_R_power']==0 and fr['W_power']==0)
data=np.load(Path(__file__).with_name('build_coupled_cubic_two_layer.npz'))
nextq=data['nextq'];shift=data['shift']
def eval_R8(w):
 q=0;v=np.zeros(8,dtype=np.int16)
 for j in w:
  l=j-1 if j>0 else -j+4
  v=(v+shift[q,l])%3;q=int(nextq[q,l])
 return q,v
images=[]
for ws in T.mappedloops:
 rows=[]
 for w in ws:
  q,v=eval_R8(w);assert q==0;rows.append(v)
 images.append(np.array(rows,dtype=np.int16))
images=np.concatenate(images,axis=1)
arrays={'joint_R8_images':images};summary={}
for p in (2,3):
 As=[];bs=[]
 for name,tokens in S.expressions.items():
  A,b=S.equation(0,tokens,p);As.append(A);bs.append(b)
 v=T.expression_matrix(0,T.expressions['pentagon'],2) if p==2 else R.expression_matrix(0,T.expressions['pentagon'])
 A,b=v;As.append(A);bs.append(b);As.append(T.abloops%p);bs.append(np.zeros(2,dtype=np.int16))
 A,b=S.source_frame(0,fr,p);As.append(A);bs.append(b)
 A=np.vstack(As);b=np.concatenate(bs);part,N=affine(A,b,p)
 arrays[f'A{p}']=A;arrays[f'b{p}']=b;arrays[f'particular{p}']=part;arrays[f'nullspace{p}']=N
 rec={'source_fiber_dimension':len(N)}
 if p==3:
  V,_=T.row_space_projection(N@images%3,3);rec['joint_R8_image_dimension']=len(V)
  arrays['R8_particular']=part@images%3;arrays['R8_directions']=V
 print('Projected source-framed odd fiber:',p,rec,flush=True);summary[str(p)]=rec
np.savez_compressed(Path(__file__).with_suffix('.npz'),**arrays)
Path(__file__).with_suffix('.json').write_text(json.dumps(summary,indent=2)+'\n')
