#!/usr/bin/env python3
"""Exact degree-three peripheral lifting obstruction at the nine-point cover.

The quotient of the free degree-three Lie module by [L2,C_i] is
computed as actual tensor rows, not inferred from its expected dimension.
The kernel on peripheral outer IA is compared to the module generated
by the literal mapping-class words in translation_class2_image.py.
"""
import translation_class2_image as I
import numpy as np,json
from pathlib import Path
p=3;n=10;pairs=I.pairs

def quotient(A):
 R,piv=I.rref(np.asarray(A,dtype=np.int16))
 free=[j for j in range(A.shape[1]) if j not in piv]
 def project(X):return (X[...,free]-X[...,piv]@R[:,free])%3
 return project,R,piv,free
def null_left(A):
 R,piv=I.rref(A.T);free=[j for j in range(len(A)) if j not in piv]
 N=np.zeros((len(free),len(A)),dtype=np.int16)
 N[:,free]=np.eye(len(free),dtype=np.int16);N[:,piv]=-R[:,free].T%3
 assert not np.any(N@A%3)
 return N

# Degree-three tensors [[X_i,X_j],X_k] in the literal associative basis.
def triple(i,j,k):
 row=np.zeros(n**3,dtype=np.int16)
 for a,b,c,s in ((i,j,k,1),(j,i,k,-1),(k,i,j,-1),(k,j,i,1)):
  row[(a*n+b)*n+c]+=s
 return row%3
T=np.array([[triple(i,j,k) for k in range(n)] for i,j in pairs])
L3,l3p=I.rref(T.reshape(-1,n**3));assert len(L3)==330
kill,kp=I.rref(T[:,:, :].transpose(1,0,2)[2:].reshape(-1,n**3))
assert len(kill)==304
proj,_,_,_=quotient(kill)
Q,qp=I.rref(proj(L3));assert len(Q)==26
def q3(X):
 Y=proj(X);coords=Y[...,qp]
 assert not np.any((Y-coords@Q)%3)
 return coords
qT=q3(T.reshape(-1,n**3)).reshape(45,10,26)

# Literal finite Magnus multiplication through degree three. In particular
# the exponent is nine, not three; the ten cubic powers remain independent.
def pmul(a,b):
 out={}
 for x,c in a.items():
  for y,d in b.items():
   if len(x)+len(y)<=3:
    key=x+y;out[key]=(out.get(key,0)+c*d)%3
 return {w:c for w,c in out.items() if c}
def pinv(a):
 u=dict(a);u.pop((),None);u2=pmul(u,u);u3=pmul(u2,u)
 out={():1}
 for factor,pol in ((-1,u),(1,u2),(-1,u3)):
  for w,c in pol.items():out[w]=(out.get(w,0)+factor*c)%3
 return {w:c for w,c in out.items() if c}
def ppow(a,k):
 out={():1}
 for _ in range(k):out=pmul(out,a)
 return out
def pcomm(a,b):return pmul(pmul(pmul(a,b),pinv(a)),pinv(b))
GX=[{():1,(i,):1} for i in range(n)]
for i,g in enumerate(GX):
 assert ppow(g,3)=={():1,(i,i,i):1} and ppow(g,9)=={():1}
for z,(i,j) in enumerate(pairs):
 c=pcomm(GX[i],GX[j]);assert ppow(c,3)=={():1}
 for k in range(n):
  t=pcomm(c,GX[k]);row=np.zeros(n**3,dtype=np.int16)
  for word,coef in t.items():
   if word:
    assert len(word)==3
    row[(word[0]*n+word[1])*n+word[2]]=coef
  assert np.array_equal(row,T[z,k])
cubes=np.zeros((10,n**3),dtype=np.int16)
for i in range(n):cubes[i,(i*n+i)*n+i]=1
assert len(I.rref(np.vstack((L3,cubes)))[0])==340
print('PASS finite Magnus group: generators order9, commutators order3, third layer330+10',flush=True)

# Rebuild the actual peripheral outer IA conditions.
eye=np.eye(440,dtype=np.int16);lifts=I.outer_lift(eye).reshape(440,45,10)
S=np.array([0,0]+[1]*8,dtype=np.int16)
conj=np.array([I.wedge(np.eye(10,dtype=np.int16)[i],S) for i in range(10)])
projS,RS,ps,fs=quotient(conj)
conditions=[]
for i in range(2,10):
 forbidden=[j for j,(a,b) in enumerate(pairs) if i not in (a,b)]
 conditions.append(lifts[:,forbidden,i])
conditions.append(projS(lifts[:,:,2:].sum(axis=2)%3))
Cper=np.hstack(conditions);Pper=null_left(Cper);assert len(Pper)==117

# Retain row witnesses for y -> [y,S], so normalization is an actual inner map.
A=conj.copy();V=np.eye(10,dtype=np.int16);rank=0;pivs=[]
for c in range(45):
 nz=np.flatnonzero(A[rank:,c])
 if not len(nz):continue
 k=rank+int(nz[0]);A[[rank,k]]=A[[k,rank]];V[[rank,k]]=V[[k,rank]]
 scale=1 if A[rank,c]==1 else 2;A[rank]=A[rank]*scale%3;V[rank]=V[rank]*scale%3
 ns=np.flatnonzero(A[:,c]);ns=ns[ns!=rank];co=A[ns,c].copy()
 A[ns]=(A[ns]-co[:,None]*A[rank])%3;V[ns]=(V[ns]-co[:,None]*V[rank])%3
 pivs.append(c);rank+=1
 if rank==9:break
assert rank==9 and not np.any(A[rank:])
inner=np.array([np.stack([I.wedge(np.eye(10,dtype=np.int16)[i],np.eye(10,dtype=np.int16)[j]) for j in range(10)],axis=1) for i in range(10)])
def obstruction(C):
 D=I.outer_lift(C).reshape(-1,45,10)
 target=D[:,:,2:].sum(axis=2)%3
 y=target[:,pivs]@V[:rank]%3
 assert np.array_equal(y@conj%3,target)
 normalized=(D-np.einsum('bi,ijk->bjk',y,inner))%3
 assert not np.any(normalized[:,:,2:].sum(axis=2)%3)
 # Every normalized peripheral conjugator has no A or B component.
 for i in range(2,10):
  forbidden=[j for j,(a,b) in enumerate(pairs) if a<2 or b<2]
  assert not np.any(normalized[:,forbidden,i])
 out=(normalized[:,:,0]@qT[:,1]-normalized[:,:,1]@qT[:,0])%3
 return out,y,normalized

O,normalizing_y,normalD=obstruction(Pper)
rankO=len(I.rref(O)[0]);assert rankO==26
K=null_left(O)@Pper%3
assert len(K)==91 and len(I.rref(K)[0])==91
assert not np.any(obstruction(I.W)[0])
assert len(I.rref(np.vstack((K,I.W)))[0])==91
print('PASS actual degree-three Lie quotient: 330 / 304 = 26',flush=True)
print('PASS peripheral lifting obstruction rank26 on dimension117',flush=True)
print('PASS kernel dimension91 equals actual geometric outer IA module',flush=True)

# Save literal actual words witnessing the geometric lower bound. A rank
# certificate for these rows suffices; no presentation-completeness claim
# is needed for the new peripheral-image theorem.
base_words=list(I.handle_words)+list(I.pointpush_words)
for i in range(3,10):
 w=list(I.identity_words);w[i-1]=(i,i+1,-i);w[i]=(i,);base_words.append(tuple(w))
base_aut=[I.aut(w) for w in base_words]
def join(*words):return I.F.red(x for w in words for x in w)
def inverse(w):return I.F.inv(w)
push_words=[]
for i in range(8):
 c=tuple(4+j for j in range(i,0,-1))
 for j in range(2):
  e=I.Bi[j];b=(3,)*int(e[0])+(4,)*int(e[1])
  push_words.append(join(c,b,inverse(c)))
witness_words=[];families=[]
for q,M in enumerate(I.linear2):
 for j,h in enumerate(I.handles,1):
  r=I.li2[tuple((M@h[1][:2,:2]%3).reshape(-1))]
  witness_words.append(join(I.paths[q],(j,),inverse(I.paths[r])));families.append('handle Schreier word')
for w in push_words:witness_words.append(join(w,w,w));families.append('push cube')
for i,g in enumerate(push_words):
 for h in push_words[:i]:witness_words.append(join(g,h,inverse(g),inverse(h)));families.append('push commutator')
for hi,h in enumerate(I.handles,1):
 for pi,g in enumerate(I.push):
  z=I.mul(h,I.mul(g,I.inv(h)));B=z[1][2:,:2]
  correction=()
  for k,e in enumerate(B.reshape(-1)):
   for _ in range(int(e)):correction=join(correction,push_words[k])
  witness_words.append(join((hi,),push_words[pi],(-hi,),inverse(correction)));families.append('handle push correction')
for i in range(1,8):
 for j in range(i+1,9):
  c=tuple(4+k for k in range(j-1,i,-1));w=(4+i,4+i)
  witness_words.append(join(c,w,inverse(c)));families.append('pure disk pair twist')
assert len(witness_words)==244
for w,v in zip(witness_words,I.rels):
 a=I.aword(w,base_aut)
 assert np.array_equal(a[1],I.Id[1]) and np.array_equal(a[0],v)
raw_rows=np.array(I.rels,dtype=np.int16)
_,chosen=I.rref(raw_rows.T);assert len(chosen)==91
assert len(I.rref(raw_rows[chosen])[0])==91
print('PASS91 independent geometric witnesses among244 literal IA words',flush=True)

# The previous six relative directions all disappear after this necessary lift.
delta=np.hstack([(eye-I.act(h[1],eye))%3 for h in I.H])
dW=I.W@delta%3;dK=K@delta%3
relative=len(I.rref(np.vstack((dW,dK)))[0])-len(I.rref(dW)[0])
assert relative==0
print('PASS remaining relative conjugacy directions after degree-three peripheral lift:0',flush=True)

np.savez_compressed(Path(__file__).with_suffix('.npz'),lie3_basis=L3,kill_basis=kill,
 kill_pivots=np.array(kp),quotient_basis=Q,quotient_pivots=np.array(qp),triple_quotient=qT,
 peripheral_conditions=Cper,peripheral_basis=Pper,normalizing_inner_y=normalizing_y,
 normalized_peripheral_derivations=normalD,obstruction_matrix=O,liftable_outer_IA=K,
 actual_outer_IA=I.W,geometric_witness_rows=raw_rows,independent_witness_indices=np.array(chosen),
 cubic_power_tensors=cubes)
Path(__file__).with_suffix('.json').write_text(json.dumps({
 'scope':'Necessary finite peripheral lifting restriction; exact image equals actual class-two pure mapping-class image',
 'prime':3,'surface_rank':10,'class2_group_order':'3^55',
 'full_degree3_Zassenhaus_group_order':'3^395','peripheral_degree3_quotient_order':'3^91',
 'free_Lie3_dimension':330,'killed_degree3_dimension':304,'retained_Lie3_dimension':26,
 'peripheral_outer_IA_dimension':117,'lifting_obstruction_rank':26,
 'liftable_outer_IA_dimension':91,'actual_mapping_class_outer_IA_dimension':91,
 'relative_conjugacy_kernel_after_lift':0,
 'geometric_base_automorphism_words':base_words,
 'geometric_IA_witness_words':witness_words,'geometric_witness_families':families,
 'independent_geometric_witness_indices':chosen},indent=2)+'\n')
