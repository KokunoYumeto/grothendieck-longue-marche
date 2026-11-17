#!/usr/bin/env python3
"""Exact modular CM census on the characteristic Q8 cover's class-two F3 quotient."""
import numpy as np,json
from pathlib import Path
D=json.loads(Path(__file__).with_name('modular_quaternion_surface.json').read_text())
words=D['actual_automorphism_words'];n=9;pairs=[(i,j) for i in range(n) for j in range(i+1,n)];nc=36;dim=324
def rref(A):
 A=np.asarray(A,dtype=np.int16).copy()%3;r=0;p=[]
 for c in range(A.shape[1]):
  ns=np.flatnonzero(A[r:,c])
  if not len(ns):continue
  k=r+int(ns[0]);A[[r,k]]=A[[k,r]];A[r]=A[r]*(1 if A[r,c]==1 else 2)%3
  ns=np.flatnonzero(A[:,c]);ns=ns[ns!=r]
  A[ns]=(A[ns]-A[ns,c,None]*A[r])%3;p.append(c);r+=1
  if r==len(A):break
 return A[:r],p
def minv(M):
 A,p=rref(np.hstack((M,np.eye(n,dtype=np.int16))))
 assert p[:n]==list(range(n));return A[:,n:]
def wedge(v,w):return np.array([(v[i]*w[j]-v[j]*w[i])%3 for i,j in pairs],dtype=np.int16)
def wedgeM(M):return np.array([[(M[i,a]*M[j,b]-M[i,b]*M[j,a])%3 for a,b in pairs] for i,j in pairs],dtype=np.int16)
inner=np.array([np.stack([wedge(np.eye(n,dtype=np.int16)[i],np.eye(n,dtype=np.int16)[j]) for j in range(n)],axis=1).reshape(-1) for i in range(n)])
inner,ipiv=rref(inner);free=[j for j in range(dim) if j not in ipiv];odim=len(free);assert odim==315
def project(C):
 C=np.asarray(C,dtype=np.int16).reshape(-1,dim)%3;out=(C[:,free]-C[:,ipiv]@inner[:,free])%3
 return out[0] if len(out)==1 else out
def lift(C):
 C=np.asarray(C);one=C.ndim==1
 if one:C=C[None,:]
 out=np.zeros((len(C),dim),dtype=np.int16);out[:,free]=C
 return out.reshape(-1,nc,n)
def wordlie(w):
 v=np.zeros(n,dtype=np.int16);z=np.zeros(nc,dtype=np.int16)
 for j in w:
  u=np.zeros(n,dtype=np.int16);u[abs(j)-1]=1 if j>0 else 2
  z=(z+2*wedge(v,u))%3;v=(v+u)%3
 return v,z
def aut(words):
 vz=[wordlie(w) for w in words];M=np.stack([x[0] for x in vz],axis=1);D=np.stack([x[1] for x in vz],axis=1)
 return project(D@minv(M)%3),M
cache={}
def act(M,C):
 key=M.tobytes()
 if key not in cache:cache[key]=(wedgeM(M),minv(M))
 W,Mi=cache[key];A=lift(C);out=np.einsum('ij,kjl,lm->kim',W,A,Mi,optimize=True)%3
 ans=project(out.reshape(len(A),dim))
 return ans
def mul(g,h):return ((g[0]+act(g[1],h[0]))%3,g[1]@h[1]%3)
def inverse(g):
 M=minv(g[1]);return -act(M,g[0])%3,M
identity=(np.zeros(odim,dtype=np.int16),np.eye(n,dtype=np.int16))
gens=[aut(w) for w in words]
left=mul(gens[0],mul(gens[1],gens[0]));right=mul(gens[1],mul(gens[0],gens[1]))
assert np.array_equal(left[0],right[0]) and np.array_equal(left[1],right[1])
deck=[identity];didx={deck[0][1].tobytes():0}
deck_words=[()]
for g in deck:
 gi=didx[g[1].tobytes()]
 for hj,h in enumerate(gens[2:],3):
  k=mul(g,h);key=k[1].tobytes()
  if key not in didx:didx[key]=len(deck);deck.append(k);deck_words.append(deck_words[gi]+(hj,))
  else:assert np.array_equal(k[0],deck[didx[key]][0])
assert len(deck)==8
z=identity
for j in (0,1)*6:z=mul(z,gens[j])
inner_comm=mul(mul(mul(gens[2],gens[3]),inverse(gens[2])),inverse(gens[3]))
assert np.array_equal(z[0],inner_comm[0]) and np.array_equal(z[1],inner_comm[1])
for g in gens:
 for h in gens[2:]:
  k=mul(mul(g,h),inverse(g));assert k[1].tobytes() in didx
  assert np.array_equal(k[0],deck[didx[k[1].tobytes()]][0])
U=np.array([[1,1],[0,1]],dtype=np.int16);L=np.array([[1,0],[-1,1]],dtype=np.int16);I2=np.eye(2,dtype=np.int16)
modgens=[U,L,I2,I2]
modular=[I2];midx={tuple(I2.reshape(-1)):0};mpaths=[()]
for qi,A in enumerate(modular):
 for j,B in enumerate((U,L)):
  C=A@B%12;key=tuple(C.reshape(-1))
  if key not in midx:midx[key]=len(modular);modular.append(C);mpaths.append(mpaths[qi]+(j,))
base=[(identity[1],I2)];idx={(identity[1].tobytes(),tuple(I2.reshape(-1))):0};reps=[identity];basepaths=[()]
for qi,(A,B) in enumerate(base):
 for j,g in enumerate(gens):
  C=A@g[1]%3;E=B@modgens[j]%12;key=(C.tobytes(),tuple(E.reshape(-1)))
  if key not in idx:idx[key]=len(base);base.append((C,E));reps.append(mul(reps[qi],g));basepaths.append(basepaths[qi]+(j+1,))
assert len(base)==9216
print('PASS exact quaternion class-two image over9216-element joint base, with normal deckQ8',flush=True)
rels=[]
for qi,(A,B) in enumerate(base):
 for j,g in enumerate(gens):
  C=A@g[1]%3;E=B@modgens[j]%12;ri=idx[C.tobytes(),tuple(E.reshape(-1))]
  h=mul(reps[qi],g);assert np.array_equal(h[1],reps[ri][1])
  rels.append((h[0]-reps[ri][0])%3)
W,wp=rref(rels);iteration=0
_,independent_source_rows=rref(np.array(rels).T)
print('Initial actual modular IA rank:',len(W),flush=True)
while True:
 old=len(W);W,wp=rref(np.vstack([W]+[act(g[1],W) for g in gens]));iteration+=1
 print('Actual IA normal closure',iteration,'rank',len(W),flush=True)
 if len(W)==old:break

CM=mul(gens[0],gens[1]);CM12=U@L%12;records=[];small_equations=[];small_rhs=[]
for qi,Q in enumerate(modular):
 if not np.array_equal(Q@CM12%12,CM12@Q%12):continue
 g=identity
 for j in mpaths[qi]:g=mul(g,gens[j])
 comm=mul(mul(mul(g,CM),inverse(g)),inverse(CM))
 dk=didx[comm[1].tobytes()];d=deck[dk]
 A=comm[1]@CM[1]%3
 eq=(W-act(A,W))%3;R,piv=rref(eq);fr=[j for j in range(odim) if j not in piv]
 rhs=(d[0]-comm[0])%3;obs=(rhs[fr]-rhs[piv]@R[:,fr])%3
 assert np.array_equal(rhs[wp]@W%3,rhs)
 assert np.array_equal(eq[:,wp]@W%3,eq)
 eq8=eq[:,wp];rhs8=rhs[wp];R8,p8=rref(eq8);f8=[j for j in range(8) if j not in p8]
 obs8=(rhs8[f8]-rhs8[p8]@R8[:,f8])%3
 assert bool(np.any(obs8))==bool(np.any(obs))
 small_equations.append(eq8);small_rhs.append(rhs8)
 records.append({'mod12_matrix':Q.tolist(),'deck_commutator':dk,
                 'representative_word_ab':[j+1 for j in mpaths[qi]],'deck_word_in_four_generators':deck_words[dk],
                 'lifts_to_CM_centralizer':bool(not np.any(obs)),
                 'affine_rank':len(R),'obstruction':obs.tolist(),
                 'actual_kernel_equation_8x8':eq8.tolist(),'actual_kernel_rhs':rhs8.tolist(),
                 'four_coordinate_obstruction':obs8.tolist()})
print('Exact CM base candidates:',len(records),'survivors:',sum(r['lifts_to_CM_centralizer'] for r in records),flush=True)
for r in records:
 if r['lifts_to_CM_centralizer']:print('SURVIVOR',r['mod12_matrix'],flush=True)
np.savez_compressed(Path(__file__).with_suffix('.npz'),actual_IA=W,actual_IA_pivots=np.array(wp),
 source_Schreier_rows=np.array(rels),deck_C=np.array([g[0] for g in deck]),deck_M=np.array([g[1] for g in deck]),
 CM_C=CM[0],CM_M=CM[1],finite_affine_equations=np.array(small_equations),finite_affine_rhs=np.array(small_rhs))
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'Actual modular surface image at characteristic quaternion class-two level, with literal signed mod12 map',
 'surface_quotient_order':'8*3^45','with_abelian_mod12_quotient_order':'4*(8*3^45)',
 'joint_linear_base_order':9216,'normal_deck_order':8,'actual_modular_IA_rank':len(W),
 'actual_detected_modular_image_order':f'1152*3^{len(W)}',
 'actual_outer_generators_free_words':words,'base_representative_words':basepaths,
 'independent_Schreier_rows':independent_source_rows,'deck_representative_words':deck_words,
 'CM_base_candidates':len(records),'CM_base_survivors':sum(r['lifts_to_CM_centralizer'] for r in records),
 'records':records},indent=2)+'\n')
