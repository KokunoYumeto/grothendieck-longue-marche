#!/usr/bin/env python3
"""Literal rank73 quaternion cover of the index-nine torus surface.
Computes actual mapping-class and three-division deck matrices, without
asserting that their finite image equals an ambient classical group.
"""
import numpy as np,json
from pathlib import Path
D=Path(__file__).parent
F=json.loads((D/'translation_cover_basis.json').read_text())
P=json.loads((D/'translation_class2_image.json').read_text())
def red(w):
 o=[]
 for j in w:
  if o and o[-1]==-j:o.pop()
  else:o.append(int(j))
 return tuple(o)
def inv(w):return tuple(-j for j in reversed(w))
def sub(w,gs):return red(k for j in w for k in (gs[j-1] if j>0 else inv(gs[-j-1])))
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
def qiword(w,gs):
 q=0
 for j in w:q=qm(q,gs[j-1] if j>0 else qi[gs[-j-1]])
 return q
stdE=F['standard_basis_E'];qgs=[qiword(w,[1,2]) for w in stdE]
assert qgs==[6,5]+[4]*8
sections={0:()};order=[0];tree=set()
for q in order:
 for j in list(range(1,11))+list(range(-1,-11,-1)):
  dst=qm(q,qgs[j-1] if j>0 else qi[qgs[-j-1]])
  if dst not in sections:
   sections[dst]=sections[q]+(j,);order.append(dst);tree.add((q,j) if j>0 else (dst,-j))
chords=[(q,j) for q in range(8) for j in range(1,11) if (q,j) not in tree];ci={e:i for i,e in enumerate(chords)}
assert len(chords)==73
basis=[red(sections[q]+(j,)+inv(sections[qm(q,qgs[j-1])])) for q,j in chords]
def rewrite(w,hom=False):
 q=0;o=np.zeros(73,dtype=np.int32) if hom else []
 for j in w:
  if j>0:e=(q,j);q=qm(q,qgs[j-1]);sg=1
  else:q=qm(q,qi[qgs[-j-1]]);e=(q,-j);sg=-1
  if e in ci:
   if hom:o[ci[e]]+=sg
   else:o.append(sg*(ci[e]+1))
 assert q==0
 return o if hom else red(o)
for i,w in enumerate(basis):assert rewrite(w)==(i+1,)
Id=tuple((j,) for j in range(1,11))
handles=[((1,),(2,1))+Id[2:],((1,-2),(2,))+Id[2:]]
rawpush=[tuple(tuple(w) for w in g) for g in P['pointpush_free_words']]
disks=[]
for j in range(3,10):
 g=list(Id);g[j-1]=(j,j+1,-j);g[j]=(j,);disks.append(tuple(g))
H=[tuple(tuple(w) for w in g) for g in F['deck_automorphisms']]
inners=[tuple((j,)+w+(-j,) for w in Id) for j in (1,2)]
gwords=handles+rawpush+disks+H+inners
names=['handle_U','handle_L','push_1','push_2']+[f'puncture_braid_{j}' for j in range(3,10)]+['deck_a','deck_b','inner_A','inner_B']
Ms=[];qauts=[]
for name,g in zip(names,gwords):
 images=[qiword(w,qgs) for w in g]
 qa=[qiword(sections[q],images) for q in range(8)]
 assert sorted(qa)==list(range(8))
 assert all(qm(qa[a],qa[b])==qa[qm(a,b)] for a in range(8) for b in range(8))
 assert images==[qa[q] for q in qgs]
 M=np.stack([rewrite(sub(w,g),True) for w in basis],axis=1);Ms.append(M);qauts.append(qa)
 print('Built actual rank73 action',name,'max integral entry',int(np.max(np.abs(M))),flush=True)
def rref(A):
 A=np.asarray(A,dtype=np.int16).copy()%3;r=0;ps=[]
 for j in range(A.shape[1]):
  nz=np.flatnonzero(A[r:,j])
  if not len(nz):continue
  k=r+int(nz[0]);A[[r,k]]=A[[k,r]];A[r]=A[r]*(1 if A[r,j]==1 else 2)%3
  ns=np.flatnonzero(A[:,j]);ns=ns[ns!=r];A[ns]=(A[ns]-A[ns,j,None]*A[r])%3;ps.append(j);r+=1
  if r==len(A):break
 return A[:r],ps
def minv(A):
 n=len(A);R,ps=rref(np.hstack((A,np.eye(n,dtype=np.int16))));assert ps[:n]==list(range(n));return R[:,n:]
for M in Ms:assert len(rref(M)[0])==73
# All eight actual inner deck matrices from the retained sections.
deck=[]
for q in range(8):deck.append(np.stack([rewrite(sections[q]+w+inv(sections[q]),True) for w in basis],axis=1)%3)
assert len({A.tobytes() for A in deck})==8
for M,qa in zip(Ms,qauts):
 for h in range(8):assert np.array_equal(M@deck[h]%3,deck[qa[h]]@M%3)
assert all(np.array_equal(deck[a]@deck[b]%3,deck[qm(a,b)]) for a in range(8) for b in range(8))
# Central (-1)-eigenspace, and a literal primitive idempotent for M2(F3).
I=np.eye(73,dtype=np.int16);C,piv=rref((I-deck[4]).T);C=C.T;assert C.shape==(73,36)
# For column basis C, the selected row positions invert C.
_,pivrows=rref(C.T);Ci=minv(C[pivrows,:])
def restrict(A,B=C,rows=pivrows,Bi=Ci):
 X=Bi@(A@B%3)[rows,:]%3;assert np.array_equal(B@X%3,A@B%3);return X
Di=restrict(deck[1]);Dj=restrict(deck[2]);assert np.array_equal((Di+Dj)@(Di+Dj)%3,np.eye(36,dtype=np.int16))
E=2*(np.eye(36,dtype=np.int16)+Di+Dj)%3;K,_=rref(E.T);K=K.T;assert K.shape==(36,18)
_,kr=rref(K.T);Ki=minv(K[kr,:]);CB=C@K%3
_,cbr=rref(CB.T);CBi=minv(CB[cbr,:])
# Enumerate all 24 quaternion-automorphism residues and complete Schreier generators.
auts=[tuple(range(8))];ai={auts[0]:0};paths=[()];reps=[I]
for t,alpha in enumerate(auts):
 for j,beta in enumerate(qauts):
  gamma=tuple(alpha[beta[q]] for q in range(8))
  if gamma not in ai:ai[gamma]=len(auts);auts.append(gamma);paths.append(paths[t]+(j+1,));reps.append(reps[t]@Ms[j]%3)
assert len(auts)==24
repi=[minv(A) for A in reps];kernels=[];kw=[]
for t,alpha in enumerate(auts):
 for j,beta in enumerate(qauts):
  z=ai[tuple(alpha[beta[q]] for q in range(8))];M=reps[t]@Ms[j]%3@repi[z]%3
  assert all(np.array_equal(M@deck[h]%3,deck[h]@M%3) for h in (1,2))
  X=restrict(M,CB,cbr,CBi);kernels.append(X);kw.append(paths[t]+(j+1,)+inv(paths[z]))
print('PASS actual quaternion-automorphism residue group24; complete Schreier generators',len(kernels),'on quaternion multiplicity18',flush=True)
# Literal order-three deck lifts: a^4,b^4 in N8, with the original C3² labels.
# Conjugation by a^4 is (Ad a)^4 on K3, and similarly b.
H73=[np.linalg.matrix_power(Ms[11+k].astype(np.int64),4)%3 for k in (0,1)]
# The integral matrix powers are small here; cast before every later product.
H73=[x.astype(np.int16) for x in H73]
for h in H73:
 assert np.array_equal(h@h%3@h%3,I)
 assert all(np.array_equal(h@deck[k]%3,deck[k]@h%3) for k in (1,2))
assert np.array_equal(H73[0]@H73[1]%3,H73[1]@H73[0]%3)
H18=[restrict(h,CB,cbr,CBi) for h in H73]
hall=[]
for i in range(3):
 for j in range(3):hall.append(np.linalg.matrix_power(H18[0],i)%3@np.linalg.matrix_power(H18[1],j)%3)
assert len({h.tobytes() for h in hall})==9
for label,h in zip(((i,j) for i in range(3) for j in range(3)),hall):
 if label!=(0,0):assert len(rref(h-np.eye(18,dtype=np.int16))[0])==12
# The module is free rank2 over F3[C3²]: each orbit span has dimension9.
N1=H18[0]-np.eye(18,dtype=np.int16);N2=H18[1]-np.eye(18,dtype=np.int16)
socle=N1@N1%3@N2%3@N2%3;assert len(rref(socle)[0])==2
print('PASS literal C3² deck action on18-dimensional component: free group-algebra rank2',flush=True)
np.savez_compressed(Path(__file__).with_suffix('.npz'),actual_integral_generators=np.array(Ms),deck_matrices=np.array(deck),
 quaternion_component_basis=C,multiplicity_basis=CB,quaternion_kernel_generators=np.array(kernels),H73=np.array(H73),H18=np.array(H18))
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'Exact actual rank73 quaternion-cover mapping-class matrices and their18-dimensional isotypic multiplicity factor; no ambient-group equality claimed',
 'rank':73,'source_quaternion_images':qgs,'schreier_basis_K3':basis,'generator_names':names,'actual_generator_words':gwords,
 'quaternion_automorphism_images':qauts,'kernel_generator_words':kw,'quaternion_component_dimension':36,
 'multiplicity_dimension':18,'quaternion_automorphism_image_order':24,'kernel_Schreier_generator_count':len(kernels),
 'translation_group_order':9,'translation_multiplicity_module':'F3[C3²]^2'},indent=2)+'\n')
