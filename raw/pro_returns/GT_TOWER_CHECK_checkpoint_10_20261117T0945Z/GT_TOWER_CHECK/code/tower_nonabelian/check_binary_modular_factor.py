#!/usr/bin/env python3
"""Compare the literal eight-map source with the modular free class-two quotient."""
from pathlib import Path
import json,hashlib,time
import numpy as np
H=Path(__file__).resolve().parent;R=H.parent;t=time.time()
z=np.load(H/'build_binary_eight_source.npz')
o=np.load(R/'ghost_mod4/check_fivepoint_quartic_mixed_module.npz')
rec=json.loads((R/'ghost_mod4/check_fivepoint_quartic_mixed_module.json').read_text())
loops=rec['Schreier_words'];basis=z['source_basis_indices'];A=z['source_basis_coordinates']
M=z['packed_commutator_map'];extra=z['central_discrepancies'];n=97
ii,jj=np.triu_indices(n,1);nc=len(ii)
E={}
for k,row in enumerate(M):
 x=int.from_bytes(row.tobytes(),'little');c=1<<k
 while x:
  p=x.bit_length()-1
  if p not in E:E[p]=(x,c);break
  a,b=E[p];x^=a;c^=b
 assert x
assert len(E)==4656
coef=np.zeros((289,4656),dtype=np.uint8)
for i,row in enumerate(extra):
 x=int.from_bytes(np.packbits(row.reshape(-1),bitorder='little').tobytes(),'little');c=0
 while x:
  p=x.bit_length()-1;assert p in E
  a,b=E[p];x^=a;c^=b
 coef[i]=np.unpackbits(np.frombuffer(c.to_bytes((nc+7)//8,'little'),dtype=np.uint8),bitorder='little')[:nc]
print('PASS all192 extra central values have unique explicit4656 commutator coordinates',flush=True)
kt=o['modular_table'];kg=o['modular_generators'];ki=np.array([np.flatnonzero(row==0)[0] for row in kt])
kci={tuple(v):i for i,v in enumerate(o['modular_chords'])}
def kw(w):
 q=0;out=[]
 for a in w:
  if a>0:edge=(q,a-1);q=int(kt[q,kg[a-1]]);sgn=1
  else:q=int(kt[q,ki[kg[-a-1]]]);edge=(q,-a-1);sgn=-1
  if edge in kci:out.append(sgn*(kci[edge]+1))
 assert q==0
 return out
def cross(v,w):return (v[...,jj]*w[...,ii]%2).astype(np.uint8)
def ev(w):
 v=np.zeros(n,dtype=np.int16);c=np.zeros(nc,dtype=np.uint8)
 for a in w:
  j=abs(a)-1;u=np.zeros(n,dtype=np.int16);u[j]=1 if a>0 else 3
  c^=cross(v,u);v=(v+u)%4
 return v,c
KV=np.empty((289,n),dtype=np.int16);KZ=np.empty((289,nc),dtype=np.uint8)
for i,w in enumerate(loops):KV[i],KZ[i]=ev(kw(w))
assert np.array_equal(KV,o['common_projection']%4)
BV=KV[basis];BZ=KZ[basis];PV=np.zeros_like(KV);PZ=np.zeros_like(KZ)
for j in range(n):
 a=A[:,j];v=a[:,None]*BV[j]%4
 c=(a%2)[:,None]*BZ[j]
 c^=((a*(a-1)//2)%2)[:,None]*cross(BV[j],BV[j])
 PZ^=c.astype(np.uint8);PZ^=cross(PV,v);PV=(PV+v)%4
assert np.array_equal(PV,KV)
DK=KZ^PZ^cross(PV,PV)^cross(KV,-PV%4)
def inv2(a):
 a=np.hstack((a%2,np.eye(len(a),dtype=np.uint8))).astype(np.uint8);n=len(a)
 for i in range(n):
  nz=np.flatnonzero(a[i:,i]);assert len(nz)
  j=i+int(nz[0]);a[[i,j]]=a[[j,i]]
  nz=np.flatnonzero(a[:,i]);nz=nz[nz!=i];a[nz]^=a[i]
 assert np.array_equal(a[:,:n],np.eye(n,dtype=np.uint8))
 return a[:,n:]
Si=inv2(BV).astype(np.int16)
DM=np.zeros((289,n,n),dtype=np.int16);DM[:,ii,jj]=DK;DM[:,jj,ii]=DK
DC=(Si.T[None,:,:]@DM@Si[None,:,:])%2
assert not np.any(np.diagonal(DC,axis1=1,axis2=2))
expected=DC[:,ii,jj].astype(np.uint8)
assert np.array_equal(coef,expected)
print('PASS all289 literal J generators agree through the actual modular class-two map',flush=True)
out={'scope':'Exact actual source factorization, before any associator census',
 'source_cover_rank':289,'modular_free_rank':97,'common_commutator_rank':4656,
 'extra_central_rank':0,'all289_generator_comparisons_passed':True,
 'common_source_kernel':'(gamma3(K) K^4) intersect J',
 'pure_source_order':'288 * 2^4850','B0_source_order':'1728 * 2^4850',
 'B0_normality':'K and J are the previously verified B0-normal kernels; gamma3(K) K^4 is characteristic in K',
 'all_assertions_passed':True,'runtime_seconds':round(time.time()-t,3),
 'input_sha256':{'build_binary_eight_source.npz':hashlib.sha256((H/'build_binary_eight_source.npz').read_bytes()).hexdigest(),
 'ghost_mod4/check_fivepoint_quartic_mixed_module.npz':hashlib.sha256((R/'ghost_mod4/check_fivepoint_quartic_mixed_module.npz').read_bytes()).hexdigest()}}
np.savez_compressed(H/'check_binary_modular_factor.npz',extra_commutator_coordinates=coef,
 modular_raw_linear=KV,modular_raw_central=KZ,modular_section_discrepancies=DK,
 modular_basis_inverse_mod2=Si)
(H/'check_binary_modular_factor.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2),flush=True)
