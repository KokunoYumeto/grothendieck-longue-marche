#!/usr/bin/env python3
"""Actual ordinary modular/deck joint image on the faithful first-order module.
All representatives come from four literal free-surface automorphisms.
"""
import numpy as np,json,itertools
from pathlib import Path
D=Path(__file__).parent;Q=np.load(D/'modular_quaternion_compact_setup.npz');F=np.load(D/'modular_quaternion_compact_faithful.npz')
G14=Q['actual_generator_matrices'].astype(np.int16);W=F['T_image_basis'].astype(np.int16)
def rref(A):
 A=np.asarray(A,dtype=np.int16).copy()%3;r=0;ps=[]
 for j in range(A.shape[1]):
  ns=np.flatnonzero(A[r:,j])
  if not len(ns):continue
  k=r+int(ns[0]);A[[r,k]]=A[[k,r]];A[r]=A[r]*(1 if A[r,j]==1 else 2)%3
  ns=np.flatnonzero(A[:,j]);ns=ns[ns!=r];A[ns]=(A[ns]-A[ns,j,None]*A[r])%3;ps.append(j);r+=1
  if r==len(A):break
 return A[:r],ps
def inv(M):
 n=len(M);R,p=rref(np.hstack((M,np.eye(n,dtype=np.int16))));assert p[:n]==list(range(n));return R[:,n:]
def power(g,k):
 z=np.eye(len(g),dtype=np.int16)
 for _ in range(k):z=z@g%3
 return z
_,wr=rref(W.T);Wi=inv(W[wr])
def r12(g):
 M=Wi@(g@W%3)[wr]%3;assert np.array_equal(W@M%3,g@W%3);return M
G12=[r12(g) for g in G14];Di=power(G12[2],9);Dj=power(G12[3],9)
E=2*(np.eye(12,dtype=np.int16)+Di+Dj)%3;B,p=rref(E.T);B=B.T;assert B.shape==(12,6);primitive_basis=B.copy()
_,br=rref(B.T);Bi=inv(B[br])
def r6(g):
 M=Bi@(g@B%3)[br]%3;assert np.array_equal(B@M%3,g@B%3);return M
H6=[r6(power(G12[j],4)) for j in (2,3)];I6=np.eye(6,dtype=np.int16);N1=(H6[0]-I6)%3;N2=(H6[1]-I6)%3
assert not np.any(N1@N1%3) and not np.any(N1@N2%3) and not np.any(N2@N2%3)
chosen=None
for i,j in itertools.combinations(range(6),2):
 V=I6[:,[i,j]];T=np.hstack((V,N1@V%3,N2@V%3))
 if len(rref(T)[0])==6:chosen=(i,j,T);break
assert chosen is not None
vcols,T=chosen[:2],chosen[2];Ti=inv(T)
# Exact Q8 automorphisms from the original four based substitutions.
def qm(a,b):
 sa=-1 if a>=4 else 1;sb=-1 if b>=4 else 1;a%=4;b%=4;s=sa*sb
 if a==0:c=b
 elif b==0:c=a
 elif a==b:c=0;s=-s
 else:
  c=6-a-b
  if (a,b) not in ((1,2),(2,3),(3,1)):s=-s
 return c+(4 if s<0 else 0)
qi=[next(j for j in range(8) if qm(i,j)==0) for i in range(8)]
def qaut(i,j):
 out=[0,i,j,qm(i,j)];return tuple(out+[qm(4,x) for x in out])
qa=[qaut(1,qm(2,1)),qaut(qm(1,qi[2]),2),tuple(qm(qm(1,x),qi[1]) for x in range(8)),tuple(qm(qm(2,x),qi[2]) for x in range(8))]
I2=np.eye(2,dtype=np.int16);U=np.array([[1,1],[0,1]],dtype=np.int16);L=np.array([[1,0],[-1,1]],dtype=np.int16);qg=[U,L,I2,I2]
auts=[tuple(range(8))];ai={auts[0]:0};paths=[()];reps=[np.eye(12,dtype=np.int16)];qreps=[I2]
for k,alpha in enumerate(auts):
 for j,beta in enumerate(qa):
  z=tuple(alpha[beta[h]] for h in range(8))
  if z not in ai:ai[z]=len(auts);auts.append(z);paths.append(paths[k]+(j+1,));reps.append(reps[k]@G12[j]%3);qreps.append(qreps[k]@qg[j]%12)
assert len(auts)==24

def inv12(A):return np.array([[A[1,1],-A[0,1]],[-A[1,0],A[0,0]]],dtype=np.int16)%12
gs=[];sourcewords=[]
for k,alpha in enumerate(auts):
 for j,beta in enumerate(qa):
  z=ai[tuple(alpha[beta[h]] for h in range(8))]
  g=reps[k]@G12[j]%3@inv(reps[z])%3;M=Ti@r6(g)%3@T%3;q=qreps[k]@qg[j]%12@inv12(qreps[z])%12
  assert np.array_equal(q%2,I2)
  for h,hh in enumerate(H6):
   lhs=r6(g)@hh%3@inv(r6(g))%3;rhs=power(H6[0],int(q[0,h]%3))@power(H6[1],int(q[1,h]%3))%3
   assert np.array_equal(lhs,rhs)
  gs.append((M,q));sourcewords.append(paths[k]+(j+1,)+tuple(-t for t in paths[z][::-1]))
# Exact split linear-normalizer coordinates: constant2x2 and q3 action on X,Y.
def split(A,q):
 S=np.zeros((6,6),dtype=np.int16);S[:2,:2]=A
 for i in range(2):
  for j in range(2):S[2+2*i:4+2*i,2+2*j:4+2*j]=q[i,j]*A%3
 return S

def coordinates(M,q):
 A=M[:2,:2];S=split(A,q%3);C=M@inv(S)%3
 assert np.array_equal(C[:2],I6[:2]) and np.array_equal(C[2:,2:],I6[2:,2:])
 return C[2:,:2].reshape(-1),A

gens=[(*coordinates(M,q),q) for M,q in gs]
def act(A,q,C):
 return (split(A,q)[2:,2:]@np.asarray(C).reshape(4,2)%3@inv(A)%3).reshape(-1)
def mul(g,h):
 C,A,q=g;E,B,r=h;return (C+act(A,q%3,E))%3,A@B%3,q@r%12
identity=(np.zeros(8,dtype=np.int16),I2,I2)
base=[(I2,I2)];idx={(I2.tobytes(),I2.tobytes()):0};reps=[identity];bwords=[()]
for k,(A,q) in enumerate(base):
 for j,g in enumerate(gens):
  E,B,r=mul(reps[k],g);key=(B.tobytes(),r.tobytes())
  if key not in idx:idx[key]=len(base);base.append((B,r));reps.append((E,B,r));bwords.append(bwords[k]+(j+1,))
assert len(base)==384,len(base)
rows=[]
for k,(A,q) in enumerate(base):
 for j,g in enumerate(gens):
  E,B,r=mul(reps[k],g);z=idx[B.tobytes(),r.tobytes()];rows.append((E-reps[z][0])%3)
K,kp=rref(rows);assert len(K)==6
for C,A,q in gens:
 assert len(rref(np.vstack((K,[act(A,q%3,v) for v in K])))[0])==6
print('PASS actual modular/deck joint image: base384, complete36864 Schreier rows, IA rank6, order384*3^6',flush=True)
print('PASS all96 actual source generators have H-label map exactly signed period mod3',flush=True)
np.savez_compressed(Path(__file__).with_suffix('.npz'),module6_basis=T,primitive_basis=primitive_basis,actual_generators=np.array([g for g,q in gs]),
 periods=np.array([q for g,q in gs]),source_Schreier_rows=np.array(rows),kernel=K,base_constant=np.array([A for A,q in base]),base_period=np.array([q for A,q in base]))
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'Exact actual modular/deck joint image in first-order faithful quaternion module plus signed period mod12',
 'source_generators4':['u','l','Inn(a)','Inn(b)'],'quaternion_automorphism_kernel_words':sourcewords,
 'module_free_basis_columns':vcols,'joint_base_order':384,'kernel_rank':6,'order':'384*3^6',
 'complete_Schreier_rows':len(rows),'H_label_period_checks':len(gs),'base_representative_words96':bwords},indent=2)+'\n')
