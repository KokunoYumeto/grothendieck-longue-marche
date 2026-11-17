#!/usr/bin/env python3
"""Finite C3² straightening and centralizer tests in the actual class2 image."""
import translation_class2_image as I
import numpy as np,json,itertools
from pathlib import Path
W=I.W;H=I.H;odim=I.odim

def null_left(A):
 rr,piv=I.rref(np.array(A,dtype=np.int16).T);free=[j for j in range(A.shape[0]) if j not in piv]
 N=np.zeros((len(free),A.shape[0]),dtype=np.int16)
 N[:,free]=np.eye(len(free),dtype=np.int16);N[:,piv]=-rr[:,free].T;N%=3
 assert not np.any(N@A%3)
 return N

def quotient(A):
 rr,piv=I.rref(A);free=[j for j in range(A.shape[1]) if j not in piv]
 def project(X):return (X[...,free]-X[...,piv]@rr[:,free])%3
 return project,rr,piv,free

# Exact necessary peripheral IA constraints, including the ninth cusp.
eye=np.eye(odim,dtype=np.int16);lift=I.outer_lift(eye).reshape(odim,I.nc,I.n)
constraints=[]
for i in range(2,10):
 forbidden=[j for j,(a,b) in enumerate(I.pairs) if a!=i and b!=i]
 constraints.append(lift[:,forbidden,i])
v9=np.array([0,0]+[2]*8,dtype=np.int16)
conjugacy=np.array([I.wedge(np.eye(10,dtype=np.int16)[:,i],v9) for i in range(10)])
proj9,_,_,_=quotient(conjugacy)
constraints.append(proj9((lift[:,:,2:].sum(axis=2))%3))
Cper=np.hstack(constraints);ambient_peripheral=null_left(Cper)
assert not np.any(W@Cper%3)
print('Ambient outer IA dimension440; peripheral outer IA dimension',len(ambient_peripheral),flush=True)

AH=[I.act(h[1],eye) for h in H]
delta=np.hstack([(eye-A)%3 for A in AH])
dW=W@delta%3;rank_W=len(I.rref(dW)[0]);projectW,*_=quotient(W)

def relative_kernel(V,name):
 D=V@delta%3
 condition=np.hstack((projectW(D[:,:odim]),projectW(D[:,odim:])))
 pre=null_left(condition);S=pre@V%3;intersection=S@delta%3
 rank_inter=len(I.rref(intersection)[0]);dim=rank_inter-rank_W
 assert dim>=0
 print(name,'conjugator space',len(S),'intersection rank',rank_inter,'actual coboundary rank',rank_W,'relative H1 kernel',dim,flush=True)
 return {'ambient_dimension':len(V),'admissible_conjugator_dimension':len(S),
         'coboundary_intersection_rank':rank_inter,'actual_coboundary_rank':rank_W,
         'relative_H1_kernel_dimension':dim},S
full,Sfull=relative_kernel(eye,'Full outer IA')
peripheral,Sper=relative_kernel(ambient_peripheral,'Peripheral outer IA')

# All pure homological matrices centralizing the two translations.
# M=[[C,0],[B,I8]], where C is in SL2(F3), B has16 entries.
# Solve the two displayed linear commutation equations, not3^16 guesses.
rows=[]
for i in range(16):
 B=np.zeros((8,2),dtype=np.int16);B.reshape(-1)[i]=1
 rows.append(np.concatenate([((np.eye(8,dtype=np.int16)-h[1][2:,2:])@B%3).reshape(-1) for h in H]))
L=np.array(rows,dtype=np.int16)
projL,_,_,_=quotient(L);NL=null_left(L)
print('Pure homological centralizer homogeneous dimension:',len(NL),flush=True)
# Fixed row-space solver with witnesses for its input16 coordinates.
def row_solve(A,b):
 A=A.copy()%3;Wit=np.eye(len(A),dtype=np.int16);r=0;piv=[]
 for c in range(A.shape[1]):
  nz=np.flatnonzero(A[r:,c])
  if not len(nz):continue
  k=r+int(nz[0]);A[[r,k]]=A[[k,r]];Wit[[r,k]]=Wit[[k,r]]
  scale=1 if A[r,c]==1 else 2;A[r]=A[r]*scale%3;Wit[r]=Wit[r]*scale%3
  ns=np.flatnonzero(A[:,c]);ns=ns[ns!=r];sc=A[ns,c].copy()
  A[ns]=(A[ns]-sc[:,None]*A[r])%3;Wit[ns]=(Wit[ns]-sc[:,None]*Wit[r])%3
  piv.append(c);r+=1
  if r==len(A):break
 v=b.copy()%3;x=np.zeros(len(A),dtype=np.int16)
 for i,c in enumerate(piv):
  a=int(v[c]);v=(v-a*A[i])%3;x=(x+a*Wit[i])%3
 return None if np.any(v) else x

pure_candidates=[]
for ci,C in enumerate(I.linear2):
 rhs=np.concatenate([(h[1][2:,:2]@(C-np.eye(2,dtype=np.int16))%3).reshape(-1) for h in H])
 base=row_solve(L,rhs)
 if base is None:continue
 for coeffs in itertools.product(range(3),repeat=len(NL)):
  bv=(base+np.array(coeffs,dtype=np.int16)@NL)%3;B=bv.reshape(8,2)
  M=np.eye(10,dtype=np.int16);M[:2,:2]=C;M[2:,:2]=B
  assert all(np.array_equal(M@h[1]%3,h[1]@M%3) for h in H)
  representative=I.mul(I.push_word(B@I.minv(C)%3),I.aword(I.paths[ci],I.handles))
  assert np.array_equal(representative[1],M)
  rhs=np.concatenate([(h[0]+I.act(h[1],representative[0])-representative[0]-I.act(M,h[0]))%3 for h in H])
  ok=row_solve(dW,rhs) is not None
  pure_candidates.append({'closed_matrix':C.tolist(),'pointpush_matrix':B.tolist(),'lifts_to_actual_centralizer':ok})
print('Exact pure centralizer census:',sum(r['lifts_to_actual_centralizer'] for r in pure_candidates),'of',len(pure_candidates),'homological candidates lift',flush=True)
# Actual normalizer N0 and its level-three kernel, via the covering maps.
normalizer_kernel=[]
for q,M in enumerate(I.linear2):
 for j,h in enumerate(I.handles,1):
  r=I.li2[tuple((M@h[1][:2,:2]%3).reshape(-1))]
  # The standard handle enumeration differs by the explicit swap in the
  # covering basis, but the same abstract U,L words define the source.
  z=I.aword(I.paths[q]+(j,)+I.F.inv(I.paths[r]),I.normalizers)
  assert np.array_equal(z[1][:2,:2],np.eye(2,dtype=np.int16))
  assert np.array_equal(z[1][2:,2:],np.eye(8,dtype=np.int16))
  normalizer_kernel.append(z[1][2:,:2].reshape(-1))
NK,_=I.rref(np.array(normalizer_kernel))
while True:
 images=[]
 for h in I.normalizers:
  for row in NK:
   M=np.eye(10,dtype=np.int16);M[2:,:2]=row.reshape(8,2)
   N=h[1]@M@I.minv(h[1])%3;images.append(N[2:,:2].reshape(-1))
 N,_=I.rref(np.vstack((NK,np.array(images))))
 if len(N)==len(NK):NK=N;break
 NK=N
print('Actual geometric N0 level-three homological image dimension:',len(NK),flush=True)
projectNK,*_=quotient(NK)
for rec in pure_candidates:
 in_geometric=not np.any(projectNK(np.array(rec['pointpush_matrix']).reshape(-1)))
 rec['in_geometric_normalizer_image']=bool(in_geometric)
print('Centralizer image equals actual normalizer image:',all(r['lifts_to_actual_centralizer']==r['in_geometric_normalizer_image'] for r in pure_candidates),flush=True)
out={'scope':'Exact finite C3² comparison in the actual Γ1,9 image at free class2/exponent3; no higher finite naturality conclusion',
 'actual_outer_IA_dimension':len(W),'full_relative_kernel':full,'peripheral_relative_kernel':peripheral,
 'pure_homological_centralizer_dimension':len(NL),'pure_homological_candidates':len(pure_candidates),
 'pure_class2_centralizer_survivors':sum(r['lifts_to_actual_centralizer'] for r in pure_candidates),
 'geometric_normalizer_homological_dimension':len(NK),'records':pure_candidates}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'),ambient_peripheral=ambient_peripheral,
 delta=delta,actual_coboundaries=dW,full_conjugators=Sfull,peripheral_conjugators=Sper,
 homological_centralizer_kernel=NL,geometric_normalizer_image=NK)
