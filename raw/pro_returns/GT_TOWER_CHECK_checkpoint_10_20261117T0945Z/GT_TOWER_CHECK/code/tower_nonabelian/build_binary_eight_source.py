#!/usr/bin/env python3
"""Literal eight-map image in the signed exponent-four class-two target.
All source generators are the289 recorded Schreier words in F(x,y).
Retain97 actual generators, all4656 commutators, and192 central discrepancies.
No finite record is asserted to lift to a genuine associator.
"""
from pathlib import Path
import json,hashlib,sys,time
import numpy as np
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
sys.path.insert(0,str(ROOT/'ghost_code'))
import fivepoint_signed_level_data as C
start_time=time.time()
target=np.load(HERE/'build_signed_binary_class2.npz')
old=np.load(ROOT/'ghost_mod4/check_fivepoint_quartic_mixed_module.npz')
record=json.loads((ROOT/'ghost_mod4/check_fivepoint_quartic_mixed_module.json').read_text())
loops=[tuple(w) for w in record['Schreier_words']]
pairs=[tuple(tuple(w) for w in p) for p in record['pairwords']]
P=target['raw_linear_projection'].astype(np.int16)
GC=target['generator_central_correction'].astype(np.uint8)
GV=P.copy();GV[:,100:]=(GV[:,100:]+2*GC[:,:2])%4
GZ=GC[:,2:]
ii=target['wedge_i'];jj=target['wedge_j']
cpiv=target['central_pivots'];cfree=target['central_free']
CR=target['central_relation_rref'];dc=len(cfree);nw=len(ii)
CF=CR[:,cfree];cr_nonzero=[np.flatnonzero(row) for row in CF]
def reduce_z(z):
 z=np.asarray(z,dtype=np.uint8)%2;out=z[...,cfree].copy()
 for p,cols in zip(cpiv,cr_nonzero):
  if len(cols):out[...,cols]^=z[...,p,None]
 return out
def inverse(w):return tuple(-j for j in reversed(w))
def subst(w,images):
 return tuple(j for z in w for j in (images[z-1] if z>0 else inverse(images[-z-1])))
def schreier(w):
 q=0;out=[]
 for z in w:
  if z>0:edge=(q,z-1);q=int(C.table[q,C.ig[z-1]]);sgn=1
  else:q=int(C.table[q,C.inverses[C.ig[-z-1]]]);edge=(q,-z-1);sgn=-1
  if edge in C.chordidx:out.append(sgn*(C.chordidx[edge]+1))
 assert q==0
 return out
def cross(v,w):return (v[...,jj]*w[...,ii]%2).astype(np.uint8)
def evaluate(w):
 v=np.zeros(102,dtype=np.int16);z=np.zeros(nw,dtype=np.uint8)
 for a in w:
  g=GV[abs(a)-1];u=g if a>0 else -g%4;c=GZ[abs(a)-1].copy()
  if a<0:c^=cross(g,g)
  z^=c;z^=cross(v,u);v=(v+u)%4
 return v,z
V=np.empty((289,8,102),dtype=np.int16);Z=np.empty((289,8,nw),dtype=np.uint8)
for i,w in enumerate(loops):
 for j,pair in enumerate(pairs):V[i,j],Z[i,j]=evaluate(schreier(subst(w,pair)))
linear=V.copy();linear[:,:,100:]%=2
assert np.array_equal(linear.reshape(289,816),old['raw_eight_map'])
print('PASS all2312 literal source evaluations and exact old abelian projection',flush=True)
def rref2(a):
 a=np.asarray(a,dtype=np.uint8).copy()%2;r=0;pv=[]
 for c in range(a.shape[1]):
  if r==len(a):break
  nz=np.flatnonzero(a[r:,c])
  if not len(nz):continue
  k=r+int(nz[0]);a[[r,k]]=a[[k,r]]
  nz=np.flatnonzero(a[:,c]);nz=nz[nz!=r];a[nz]^=a[r];pv.append(c);r+=1
 return a[:r],pv
def inv4(a):
 n=len(a);a=np.hstack((a%4,np.eye(n,dtype=np.int16)))
 for c in range(n):
  nz=np.flatnonzero(a[c:,c]%2);assert len(nz)
  k=c+int(nz[0]);a[[c,k]]=a[[k,c]];a[c]=a[c]*int(a[c,c])%4
  nz=np.flatnonzero(a[:,c]);nz=nz[nz!=c];a[nz]=(a[nz]-a[nz,c,None]*a[c])%4
 assert np.array_equal(a[:,:n],np.eye(n,dtype=np.int16))
 return a[:,n:]
Q=old['common_projection'].astype(np.int16)%4
_,basis=rref2(Q.T%2);assert len(basis)==97
S=Q[basis];Si=inv4(S);A=Q@Si%4
assert np.array_equal(A[basis],np.eye(97,dtype=np.int16))
assert np.array_equal(A@S%4,Q)
BV=V[basis];BZ=Z[basis]
PV=np.zeros_like(V);PZ=np.zeros_like(Z)
for j in range(97):
 n=A[:,j];iv=n[:,None,None]*BV[j][None,:,:]%4
 iz=(n[:,None,None]%2)*BZ[j][None,:,:]
 iz^=((n*(n-1)//2)%2)[:,None,None]*cross(BV[j],BV[j])[None,:,:]
 PZ^=iz.astype(np.uint8);PZ^=cross(PV,iv);PV=(PV+iv)%4
 if j%25==0:print('actual97-generator section products',j,'elapsed',round(time.time()-start_time,1),flush=True)
rv=(V-PV)%4
assert not np.any(rv[:,:,:100]) and not np.any(rv[:,:,100:]%2)
rz=Z^PZ^cross(PV,PV)^cross(V,-PV%4)
raw=np.concatenate((rv[:,:,100:]//2,rz),axis=2).astype(np.uint8)
extra=reduce_z(raw);assert not np.any(extra[basis])
print('PASS actual central discrepancies for the other192 source generators',flush=True)
echelon={};comm_basis=[];extra_basis=[]
def as_int(row):
 return int.from_bytes(np.packbits(np.asarray(row,dtype=np.uint8).reshape(-1),bitorder='little').tobytes(),'little')
def add_row(x):
 while x:
  p=x.bit_length()-1
  if p not in echelon:echelon[p]=x;return True
  x^=echelon[p]
 return False
bi,bj=np.triu_indices(97,1);comm_rows=[]
for start in range(0,len(bi),96):
 is_=bi[start:start+96];js=bj[start:start+96]
 w=cross(BV[is_],BV[js])^cross(BV[js],BV[is_])
 raw=np.concatenate((np.zeros((len(is_),8,2),dtype=np.uint8),w),axis=2)
 reduced=reduce_z(raw)
 for k,row in enumerate(reduced):
  x=as_int(row);comm_rows.append(x)
  if add_row(x):comm_basis.append(start+k)
 if start%960==0:print('commutator rows',start+len(is_),'rank',len(echelon),'elapsed',round(time.time()-start_time,1),flush=True)
comm_rank=len(echelon)
for i,row in enumerate(extra):
 if add_row(as_int(row)):extra_basis.append(i)
central_rank=len(echelon);packed_width=(8*dc+7)//8
packed_comm=np.array([np.frombuffer(x.to_bytes(packed_width,'little'),dtype=np.uint8) for x in comm_rows],dtype=np.uint8)
out={'scope':'Actual eight-map finite source image; no associator lifting assertion',
 'base_order':288,'source_cover_rank':289,'target_central_dimension':dc,
 'abelian_common_image':'C4^97','actual_basis_source_indices':basis,
 'commutator_rank':comm_rank,'extra_central_rank':central_rank-comm_rank,
 'central_rank':central_rank,'kernel_order_power_of_2':194+central_rank,
 'joint_source_order':'288 * 2^'+str(194+central_rank),
 'extra_source_indices':extra_basis,'all_assertions_passed':True,
 'runtime_seconds':round(time.time()-start_time,3),
 'input_sha256':{'build_signed_binary_class2.npz':hashlib.sha256((HERE/'build_signed_binary_class2.npz').read_bytes()).hexdigest(),
 'ghost_mod4/check_fivepoint_quartic_mixed_module.npz':hashlib.sha256((ROOT/'ghost_mod4/check_fivepoint_quartic_mixed_module.npz').read_bytes()).hexdigest()}}
HERE.joinpath('build_binary_eight_source.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(HERE/'build_binary_eight_source.npz',source_raw_linear=V,source_raw_central=Z,
 source_abelian=linear,source_basis_indices=np.array(basis),source_basis_coordinates=A,
 central_discrepancies=extra,commutator_pairs=np.stack((bi,bj),axis=1),
 packed_commutator_map=packed_comm,commutator_basis_rows=np.array(comm_basis),extra_basis_rows=np.array(extra_basis))
print(json.dumps(out,indent=2),flush=True)
