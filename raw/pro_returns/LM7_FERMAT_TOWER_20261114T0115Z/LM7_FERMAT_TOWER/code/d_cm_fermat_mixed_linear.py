#!/usr/bin/env python3
"""All conjugator and multiplier obstructions on the Fermat12 joint homology covers."""
from pathlib import Path
from collections import deque
import json,time
import numpy as np
OUT=Path(__file__).resolve().parent;started=time.time()
D=json.loads((OUT/'d_cm_fermat_joint_base.json').read_text())
Q=[tuple(q) for q in D['Q']];ix={q:i for i,q in enumerate(Q)}
states=np.array(D['states'],dtype=np.int16);LM=np.array(D['Q_linear_matrices'],dtype=np.int16)
size=len(states);rank=len(D['cycle_chords']);nc=np.array(D['cycle_chords'],dtype=np.int32)
ident,hs,hr,ht=(D[k] for k in ['identity','s','r','t']);parent=D['parent']
def canon(a):return min(tuple(a),tuple(-int(x)%12 for x in a))
def qm(a,b):
 return canon(((a[0]*b[0]+a[1]*b[2])%12,(a[0]*b[1]+a[1]*b[3])%12,
               (a[2]*b[0]+a[3]*b[2])%12,(a[2]*b[1]+a[3]*b[3])%12))
qt=np.array([[ix[qm(a,b)] for b in Q] for a in Q],dtype=np.int16)
grid=np.full((576,144),-1,dtype=np.int32)
for h,(q,a,b) in enumerate(states):grid[q,int(a)+12*int(b)]=h
def mul(a,b):
 q,u,v=states[a];qq,x,y=states[b];M=LM[q]
 return int(grid[qt[q,qq],int((u+M[0,0]*x+M[0,1]*y)%12)+12*int((v+M[1,0]*x+M[1,1]*y)%12)])
qi=ix[(1,0,0,1)]
qinv=np.array([ix[canon((q[3],-q[1]%12,-q[2]%12,q[0]))] for q in Q],dtype=np.int16)
inverse=[]
for q,u,v in states:
 qq=qinv[q];M=LM[qq]
 inverse.append(int(grid[qq,int((-M[0,0]*u-M[0,1]*v)%12)+12*int((-M[1,0]*u-M[1,1]*v)%12)]))
inverse=np.array(inverse,dtype=np.int32)
perms={}
def perm(h):
 if h not in perms:
  q,u,v=states[h];M=LM[q]
  aa=(u+states[:,1]*M[0,0]+states[:,2]*M[0,1])%12
  bb=(v+states[:,1]*M[1,0]+states[:,2]*M[1,1])%12
  perms[h]=grid[qt[q,states[:,0]],aa+12*bb]
  assert np.all(perms[h]>=0)
 return perms[h]
def act(v,h):return v[perm(int(inverse[h]))]
C=np.zeros((size,rank),dtype=np.int16)
for j,col in enumerate(D['integral_cycle_columns']):
 for e,v in col:C[e,j]=v
assert np.array_equal(C[nc],np.eye(rank,dtype=np.int16))
Ms=act(C,hs)[nc];Mr=act(C,hr)[nc]
assert np.array_equal(Ms@Ms,np.eye(rank,dtype=np.int16))
assert np.array_equal(Mr@Mr@Mr,np.eye(rank,dtype=np.int16))

def null2(A):
 packed=np.packbits(A%2,axis=1,bitorder='little')
 basis={}
 for v in packed:
  row=int.from_bytes(v.tobytes(),'little')
  while row:
   p=row.bit_length()-1
   if p not in basis:basis[p]=row;break
   row^=basis[p]
 out=[]
 for j in range(A.shape[1]):
  if j in basis:continue
  v=1<<j
  for k in sorted(basis):
   if (v&basis[k]).bit_count()%2:v^=1<<k
  out.append([(v>>i)&1 for i in range(A.shape[1])])
 return np.array(out,dtype=np.int16).reshape((-1,A.shape[1]))
def null3(A):
 A=A.copy()%3;n,m=A.shape;r=0;piv=[]
 for j in range(m):
  inds=np.flatnonzero(A[r:,j])
  if not len(inds):continue
  k=r+int(inds[0]);A[[r,k]]=A[[k,r]];A[r]=A[r]*int(A[r,j])%3
  fac=A[r+1:,j].copy();A[r+1:]=(A[r+1:]-fac[:,None]*A[r])%3
  piv.append(j);r+=1
  if r==n:break
 out=[]
 for j in range(m):
  if j in piv:continue
  v=np.zeros(m,dtype=np.int16);v[j]=1
  for k in range(r-1,-1,-1):v[piv[k]]=(-int(A[k]@v))%3
  out.append(v)
 return np.array(out,dtype=np.int16).reshape((-1,m))

pathcache={0:np.zeros(size,dtype=np.int16)}
def path(h):
 if h not in pathcache:
  out=np.zeros(size,dtype=np.int16);v=h
  while v:
   p,a=parent[v]
   if a==1:out[p]+=1;out[v]-=1
   v=p
  pathcache[h]=out
 return pathcache[h]
Pt=act(path(hr),hs)
P72=np.zeros(size,dtype=np.int16);h=0
for j in range(72):P72+=act(Pt,h);h=mul(h,ht)
assert h==0 and np.array_equal(C@P72[nc],P72)
V4={(1,0,0,1),(1,2,0,1),(1,0,2,1),(1,2,2,1)}
def flift(a):
 a=tuple(a)
 if tuple(x%4 for x in a) in V4:return a
 a=tuple(-x%12 for x in a);assert tuple(x%4 for x in a) in V4
 return a
def invmat(a):return (a[3],-a[1]%12,-a[2]%12,a[0])
def cmbit(a,b):
 A=flift(a);B=flift(b);T=invmat(A);W=invmat(B)
 point=((T[0]+2*T[1])%3,(T[2]+2*T[3])%3)
 assert point in [(1,2),(2,1)]
 b3=int(point==(2,1));wr=tuple(x%3 for x in W)
 b4=int(wr not in [(1,0,0,1),(2,0,0,2)])
 return b3^b4
equations=np.concatenate([(Ms-np.eye(rank,dtype=np.int16)).T,(Mr-np.eye(rank,dtype=np.int16)).T],axis=0)
allrecords=[];summaries=[]
for p in [2,3]:
 dual=null2(equations) if p==2 else null3(equations)
 assert not np.any(dual@equations.T%p)
 multiplier=dual@P72[nc]%p
 print('prime',p,'coinvariant dimension',dual.shape[0],'multiplier',multiplier.tolist(),flush=True)
 records=[]
 for rec in D['candidate_conjugators']:
  lifts=[]
  for v in rec['lifts']:
   a,b,ss,rr=(v[k] for k in ['A','beta','s_image','r_image'])
   E=path(b)-act(path(b),ss)+act(path(a)-act(path(a),rr)+act(path(hr),a),ss)-Pt
   assert np.array_equal(C@E[nc],E)
   obs=dual@E[nc]%p
   allowed=[j for j in range(p) if not np.any((obs-j*multiplier)%p)]
   lifts.append({'A':a,'beta':b,'obstruction':obs.tolist(),
                 'lambda1_lift':not np.any(obs),'lambda_1_mod72_parameters':allowed})
  records.append({'A_Q':rec['A_Q'],'beta_Q':rec['beta_Q'],'extra_CM_coset':bool(cmbit(rec['A_Q'],rec['beta_Q'])),'lifts':lifts})
 summary={'prime':p,'base_order':size,'free_kernel_rank':rank,
          'coinvariant_dimension':int(dual.shape[0]),'cusp_correction_rank':rank-int(dual.shape[0]),
          'multiplier72_obstruction':multiplier.tolist(),
          'matrix_pairs_lambda1':sum(any(t['lambda1_lift'] for t in z['lifts']) for z in records),
          'extra_pairs_lambda1':sum(z['extra_CM_coset'] and any(t['lambda1_lift'] for t in z['lifts']) for z in records),
          'all_base_lifts_lambda1':sum(t['lambda1_lift'] for z in records for t in z['lifts']),
          'matrix_pairs_with_multiplier72':sum(any(t['lambda_1_mod72_parameters'] for t in z['lifts']) for z in records),
          'extra_pairs_with_multiplier72':sum(z['extra_CM_coset'] and any(t['lambda_1_mod72_parameters'] for t in z['lifts']) for z in records),
          'scope':'Complete linear cusp obstruction for all576 base conjugator choices. Generation in the elementary homology kernel is not asserted.'}
 print(json.dumps(summary,indent=2),flush=True)
 allrecords.append({'summary':summary,'dual_coinvariant_rows':dual.tolist(),'pairs':records});summaries.append(summary)
(OUT/'d_cm_fermat_mixed_linear.json').write_text(json.dumps({'summary':summaries,'tests':allrecords,'elapsed_seconds':round(time.time()-started,3)},indent=2)+'\n')
print('elapsed_seconds',round(time.time()-started,3),flush=True)
