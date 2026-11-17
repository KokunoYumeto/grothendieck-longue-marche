#!/usr/bin/env python3
"""Lift the finite C3² relative conjugacy test from exponent3 to exponent9.

All actual mapping-class generators are retained. Module arithmetic is
performed over Z/9, including nonfree3-torsion summands; no field rank is
substituted for the integral lifting equation.
"""
import translation_class2_image as I
import numpy as np,json
from pathlib import Path
mod=9;n=10;nc=45;odim=440;dim=450;inv2=5
inner=np.where(I.inner==2,-1,I.inner).astype(np.int64);ipiv=I.ipiv;ifree=I.ifree

def unit_reduce(A):
 A=np.array(A,dtype=np.int64).copy()%9;r=0;piv=[]
 for c in range(A.shape[1]):
  nz=np.flatnonzero(A[r:,c]%3)
  if not len(nz):continue
  k=r+int(nz[0]);A[[r,k]]=A[[k,r]];A[r]=A[r]*pow(int(A[r,c]),-1,9)%9
  ns=np.flatnonzero(A[:,c]);ns=ns[ns!=r];A[ns]=(A[ns]-A[ns,c,None]*A[r])%9
  piv.append(c);r+=1
  if r==len(A):break
 assert not np.any(A[r:]%3)
 return A[:r],piv,A[r:]
def module_basis(A):
 U,piv,tail=unit_reduce(A);T,tp=I.rref(tail//3)
 assert not np.any(T[:,piv]) if len(T) else True
 return U,piv,T,tp
def member(v,data):
 U,piv,T,tp=data;v=np.array(v,dtype=np.int64).copy()%9
 if len(U):v=(v-v[...,piv]@U)%9
 if np.any(v%3):return False
 w=v//3
 if len(T):w=(w-w[...,tp]@T)%3
 return not np.any(w)
def minv(M):
 U,piv,tail=unit_reduce(np.hstack((M,np.eye(len(M),dtype=np.int64))))
 assert piv[:len(M)]==list(range(len(M))) and len(U)==len(M)
 return U[:,len(M):]
def wedge(v,w):return np.array([(v[i]*w[j]-v[j]*w[i])%9 for i,j in I.pairs],dtype=np.int64)
def wedgeM(M):return np.array([[(M[i,a]*M[j,b]-M[i,b]*M[j,a])%9 for a,b in I.pairs] for i,j in I.pairs],dtype=np.int64)
def outer_project(C):
 C=np.array(C,dtype=np.int64);one=C.ndim==1;A=C.reshape(-1,450)
 out=(A[:,ifree]-A[:,ipiv]@inner[:,ifree])%9
 return out[0] if one else out
def outer_lift(C):
 C=np.array(C,dtype=np.int64);one=C.ndim==1
 if one:C=C[None,:]
 out=np.zeros((len(C),450),dtype=np.int64);out[:,ifree]=C
 return out[0] if one else out
cache={}
def act(M,C):
 key=tuple(map(int,M.reshape(-1)))
 if key not in cache:cache[key]=(wedgeM(M),minv(M))
 W,Mi=cache[key];one=np.asarray(C).ndim==1;A=outer_lift(C).reshape(-1,45,10)
 out=np.einsum('ij,kjl,lm->kim',W,A,Mi,optimize=True)%9
 out=outer_project(out.reshape(len(A),450))
 return out[0] if one else out

def word_lie(w):
 v=np.zeros(n,dtype=np.int64);z=np.zeros(nc,dtype=np.int64)
 for j in w:
  u=np.zeros(n,dtype=np.int64);u[abs(j)-1]=1 if j>0 else 8
  z=(z+inv2*wedge(v,u))%9;v=(v+u)%9
 return v,z
shift=np.zeros((45,10),dtype=np.int64);shift[0,0]=-inv2;shift[0,1]=inv2;CF=outer_project(shift.reshape(-1))
def aut(words):
 values=[word_lie(w) for w in words];M=np.stack([v for v,z in values],axis=1);D=np.stack([z for v,z in values],axis=1)
 C=outer_project((D@minv(M)%9).reshape(-1))
 C=(C-CF+act(M,CF))%9
 return C,M
Id=(np.zeros(440,dtype=np.int64),np.eye(10,dtype=np.int64))
def mul(g,h):return ((g[0]+act(g[1],h[0]))%9,g[1]@h[1]%9)
def inv(g):
 M=minv(g[1]);return (-act(M,g[0])%9,M)
def power(g,k):
 if k<0:return power(inv(g),-k)
 h=Id
 for _ in range(k):h=mul(h,g)
 return h
def aword(w,gens):
 h=Id
 for j in w:h=mul(h,gens[j-1] if j>0 else inv(gens[-j-1]))
 return h
handles=[aut(w) for w in I.handle_words];assert all(not np.any(g[0]) for g in handles)
disk=[]
for i in range(3,10):
 w=list(I.identity_words);w[i-1]=(i,i+1,-i);w[i]=(i,);disk.append(aut(tuple(w)))
raw=[aut(w) for w in I.pointpush_words];B=np.stack([g[1][2,:2] for g in raw]);Bi=minv(B)
push=[]
for i in range(8):
 conjugator=aword(tuple(range(i,0,-1)),disk)
 for j in range(2):
  v=Bi[j];base=mul(power(raw[0],int(v[0])),power(raw[1],int(v[1])))
  g=mul(conjugator,mul(base,inv(conjugator)));M=np.eye(10,dtype=np.int64);M[i+2,j]=1
  assert np.array_equal(g[1],M);push.append(g)
pairtwists=[]
for i in range(1,8):
 for j in range(i+1,9):
  t=aword(tuple(range(j-1,i,-1)),disk)
  g=mul(t,mul(power(disk[i-1],2),inv(t)));assert np.array_equal(g[1],Id[1]);pairtwists.append(g)
H=[aut(w) for w in I.F.deck]
for h in H:
 z=power(h,3);assert not np.any(z[0]) and np.array_equal(z[1],Id[1])
z=mul(H[0],H[1]);zz=mul(H[1],H[0]);assert np.array_equal(z[0],zz[0]) and np.array_equal(z[1],zz[1])
# The zero IA handle action realizes its entire matrix quotient literally.
M2=[np.eye(2,dtype=np.int64)];midx={tuple(M2[0].reshape(-1)):0}
for M in M2:
 for h in handles:
  N=M@h[1][:2,:2]%9;key=tuple(N.reshape(-1))
  if key not in midx:midx[key]=len(M2);M2.append(N)
assert len(M2)==648
print('PASS literal exponent9 source, translation action, and handle image SL2(Z/9) of order648',flush=True)

def push_word(B):
 out=Id
 for j,v in enumerate(np.asarray(B).reshape(-1)):
  if v:out=mul(out,power(push[j],int(v)))
 return out
rels=[]
for g in push:
 h=power(g,9);assert np.array_equal(h[1],Id[1]);rels.append(h[0])
for i,g in enumerate(push):
 for h in push[:i]:
  z=mul(g,mul(h,mul(inv(g),inv(h))));assert np.array_equal(z[1],Id[1]);rels.append(z[0])
for h in handles:
 for g in push:
  z=mul(h,mul(g,inv(h)));z=mul(z,inv(push_word(z[1][2:,:2])))
  assert np.array_equal(z[1],Id[1]);rels.append(z[0])
rels += [g[0] for g in pairtwists]
U,up,T,tp=module_basis(np.array(rels));iteration=0
print('Initial Z/9 actual IA module:',len(U),'free and',len(T),'order3 summands',flush=True)
while True:
 old=2*len(U)+len(T);B=np.vstack((U,3*T));images=[B]
 for g in handles+push:images.append(act(g[1],B))
 U,up,T,tp=module_basis(np.vstack(images));iteration+=1
 print('Z/9 closure iteration',iteration,':',len(U),'free and',len(T),'order3 summands',flush=True)
 if 2*len(U)+len(T)==old:break
for h in H:
 assert member(act(h[1],np.vstack((U,3*T))),(U,up,T,tp))
print('PASS actual finite mapping-class IA module over Z/9',flush=True)

# Peripheral outer IA is a free module; prove this by unit elimination.
eye=np.eye(440,dtype=np.int64);lift=outer_lift(eye).reshape(440,45,10)
conditions=[]
for i in range(2,10):
 forbidden=[j for j,(a,b) in enumerate(I.pairs) if a!=i and b!=i];conditions.append(lift[:,forbidden,i])
v9=np.array([0,0]+[8]*8,dtype=np.int64)
conj=np.array([wedge(np.eye(10,dtype=np.int64)[:,i],v9) for i in range(10)])
CU,cp,tail=unit_reduce(conj);assert not np.any(tail);cf=[i for i in range(45) if i not in cp]
sums=lift[:,:,2:].sum(axis=2)%9
conditions.append((sums[:,cf]-sums[:,cp]@CU[:,cf])%9)
Cper=np.hstack(conditions)
RU,rp,tail=unit_reduce(Cper.T);assert not np.any(tail)
rf=[i for i in range(440) if i not in rp]
Pper=np.zeros((len(rf),440),dtype=np.int64);Pper[:,rf]=np.eye(len(rf),dtype=np.int64);Pper[:,rp]=-RU[:,rf].T%9
assert not np.any(Pper@Cper%9) and len(Pper)==117
print('PASS saturated peripheral outer IA over Z/9, free rank117',flush=True)
Delta=np.hstack([(Pper-act(h[1],Pper))%9 for h in H])
# Membership of both cocycle coordinates in the ACTUAL integral module.
zeroU=np.zeros_like(U);zeroT=np.zeros_like(T)
Eq=np.vstack((Delta,np.hstack((-U,zeroU)),np.hstack((zeroU,-U)),
              np.hstack((-3*T,zeroT)),np.hstack((zeroT,-3*T))))%9

def field_null_left(A):
 R,piv=I.rref(A.T);free=[i for i in range(A.shape[0]) if i not in piv]
 N=np.zeros((len(free),A.shape[0]),dtype=np.int64);N[:,free]=np.eye(len(free),dtype=np.int64);N[:,piv]=-R[:,free].T%3
 assert not np.any(N@A%3);return N
K0=field_null_left(Eq%3)
carry=(K0@Eq%9)//3
R,piv=I.rref(Eq%3);free=[j for j in range(Eq.shape[1]) if j not in piv]
obstruction=(carry[:,free]-carry[:,piv]@R[:,free])%3
liftable=field_null_left(obstruction)@K0%3
C0=liftable[:,:117]@(Pper%3)%3
lower_delta=np.hstack([(C0-I.act(h[1]%3,C0))%3 for h in H])
dW=np.hstack([(I.W-I.act(h[1]%3,I.W))%3 for h in H]);rW=len(I.rref(dW)[0])
rUnion=len(I.rref(np.vstack((dW,lower_delta)))[0]);surviving=rUnion-rW
print('Integral conjugacy lift: field kernel',len(K0),'Bockstein obstruction rank',len(I.rref(obstruction)[0]),'liftable dimension',len(liftable),flush=True)
print('Remaining lower-level relative conjugacy directions after exponent9:',surviving,flush=True)
np.savez_compressed(Path(__file__).with_suffix('.npz'),unit_basis=U,unit_pivots=np.array(up),
 torsion_basis=T,torsion_pivots=np.array(tp),peripheral_basis=Pper,H_C=np.array([g[0] for g in H]),
 H_M=np.array([g[1] for g in H]),equation_matrix=Eq,field_kernel=K0,
 bockstein_obstruction=obstruction,liftable_residues=liftable,lower_conjugators=C0,
 lower_cocycle_directions=lower_delta)
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'Actual exponent9 mapping-class image and finite conjugacy-lifting comparison',
 'actual_IA_Z9_free_rank':len(U),'actual_IA_Z3_torsion_rank':len(T),
 'pure_homological_image_order':'648*9^16','peripheral_IA_Z9_rank':117,
 'field_equation_kernel_dimension':len(K0),'bockstein_obstruction_rank':len(I.rref(obstruction)[0]),
 'liftable_field_solution_dimension':len(liftable),
 'lower_relative_conjugacy_directions_surviving':surviving},indent=2)+'\n')
