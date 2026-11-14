#!/usr/bin/env python3
r"""Actual source-s and full 36-term cusp corrections on the compact kernel.

The coefficient module is the marked kernel of Herm(M)->Herm(P_*), not
the whole Herm(M) module.  Matrices and field conventions are reconstructed
from the immutable D63 inputs; its norm and kernel basis are checked against
the earlier D64 certificate.  The final source-word lift is proved separately.
"""
from pathlib import Path
from itertools import combinations
import numpy as np
import json, hashlib, time
OUT=Path(__file__).resolve().parent; start=time.time()
names=['d_arithmetic_A4_twisted.json','d_compact_splitting_maps.json',
       'd_arithmetic_affine_base.json','d_residual_compact_norm.json']
paths=[OUT/n for n in names]
D,Split,Aff,Norm=[json.loads(p.read_text()) for p in paths]
T=np.array(D['Q_multiplication'],dtype=np.int16)
INV=[next(h for h in range(576) if T[g,h]==0) for g in range(576)]
MUL=np.array([[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]],dtype=np.uint8)
FB=np.array([0,1,3,2],dtype=np.uint8)
def mm(a,b):
 out=np.zeros((a.shape[0],b.shape[1]),dtype=np.uint8)
 for k in range(a.shape[1]):out^=MUL[a[:,k,None],b[k,None,:]]
 return out
def rr(a):
 a=np.array(a,dtype=np.uint8,copy=True);row=0;p=[]
 for c in range(a.shape[1]):
  at=np.flatnonzero(a[row:,c])
  if not len(at):continue
  j=row+int(at[0]);a[[row,j]]=a[[j,row]];a[row]=MUL[FB[a[row,c]],a[row]]
  v=a[:,c].copy();v[row]=0;a^=MUL[v[:,None],a[row,None,:]]
  p.append(c);row+=1
  if row==len(a):break
 return a,p
def null(a):
 r,p=rr(a);free=[j for j in range(a.shape[1]) if j not in p]
 n=np.zeros((a.shape[1],len(free)),dtype=np.uint8);n[free,np.arange(len(free))]=1
 n[np.array(p),:]=r[:len(p),free]
 assert not np.any(mm(a,n));return n
def lin(cols,v):
 r=0
 while v:
  b=v&-v;r^=cols[b.bit_length()-1];v^=b
 return r
def xor_rank(cols):
 b={}
 for v in cols:
  while v:
   p=v.bit_length()-1
   if p not in b:b[p]=v;break
   v^=b[p]
 return len(b)
def coordinates(columns):
 piv={}
 for j,v in enumerate(columns):
  w=1<<j
  while v:
   p=v.bit_length()-1
   if p not in piv:piv[p]=(v,w);break
   a,b=piv[p];v^=a;w^=b
  assert v
 def coord(v,check=True):
  out=0
  for p in sorted(piv,reverse=True):
   if v>>p&1:
    a,b=piv[p];v^=a;out^=b
  if check:assert v==0
  return out
 return coord
def kernel(columns):
 piv={};ans=[]
 for j,v in enumerate(columns):
  mask=1<<j
  while v:
   p=v.bit_length()-1
   if p not in piv:piv[p]=(v,mask);break
   w,m=piv[p];v^=w;mask^=m
  if not v:ans.append(mask)
 assert all(lin(columns,v)==0 for v in ans)
 return ans
def quotient(cols,n):
 b={}
 for v in cols:
  while v:
   p=v.bit_length()-1
   if p not in b:b[p]=v;break
   v^=b[p]
 free=[j for j in range(n) if j not in b]
 def q(v):
  for p in sorted(b,reverse=True):
   if v>>p&1:v^=b[p]
  return sum(((v>>j)&1)<<i for i,j in enumerate(free))
 return q,free
def pack(v):return sum(int(x)<<(2*j) for j,x in enumerate(v))
def unpack(v,n):return np.array([(v>>(2*j))&3 for j in range(n)],dtype=np.uint8)
def scalar(v,z):return pack(MUL[z,unpack(v,16)])
def hermpack(a):
 assert np.array_equal(a,FB[a.T]);assert np.all(a.diagonal()<2)
 v=list(map(int,a.diagonal()))
 for i in range(len(a)):
  for j in range(i+1,len(a)):v.extend([int(a[i,j])&1,int(a[i,j])>>1])
 return sum(x<<j for j,x in enumerate(v))
def wedge(a,b,n):
 out=0;offset=0
 for i in range(n-1):
  row=((b>>(i+1)) if a>>i&1 else 0)^((a>>(i+1)) if b>>i&1 else 0)
  out^=row<<offset;offset+=n-i-1
 return out
def average_wedge(v,w):
 a=unpack(v,16);b=unpack(w,16)
 return hermpack(MUL[a[:,None],FB[b[None,:]]]^MUL[b[:,None],FB[a[None,:]]])
# Verify the Hermitian formula against literal averaging of real wedges.
wc=[]
for i in range(16):wc.append(wedge(1<<(2*i),1<<(2*i+1),32))
for i in range(16):
 for j in range(i+1,16):
  u,v,U,V=[1<<k for k in [2*i,2*i+1,2*j,2*j+1]]
  wc.extend([wedge(u,V,32)^wedge(v,U,32),
             wedge(u,U,32)^wedge(v,U,32)^wedge(v,V,32)])
assert len(wc)==256 and xor_rank(wc)==256
for i,j in combinations(range(32),2):
 a,b=1<<i,1<<j
 real=wedge(a,b,32)^wedge(scalar(a,2),scalar(b,2),32)^wedge(scalar(a,3),scalar(b,3),32)
 assert lin(wc,average_wedge(a,b))==real

qstar=[np.array(m,dtype=np.int16).T for m in Aff['Q_linear_image_matrices']]
QL=np.array([qstar[j] for j in Aff['Q_to_linear_image']],dtype=np.int16)
def normq(v):return min(tuple(int(x)%12 for x in v),tuple(-int(x)%12 for x in v))
qindex={tuple(v):i for i,v in enumerate(D['Q_states'])}
S=qindex[normq((0,1,11,0))];R=qindex[normq((0,11,1,11))];qt=int(T[S,R])
vr=np.array(Aff['affine_r_translation'],dtype=np.int16);vt=QL[S]@vr%3
assert S==1 and not any(Aff['affine_s_translation'])
for g in range(576):
 for h in [S,R]:assert np.array_equal(QL[g]@QL[h]%3,QL[int(T[g,h])])

rows=[]
for rec in Split['cases']:
 char=rec['character'];nrec=next(r for r in Norm['cases'] if r['character']==char)
 src=next(r for r in D['character_blocks'] if r['character']==char)
 flips={a['q_state']:a['flip'] for a in src['all_stabilizer_actions']}
 acts={int(g):np.array(a,dtype=np.uint8).T for g,a in rec['all_complement_actions'].items()}
 H=sorted(acts);phi=np.array(nrec['target_map_columns'],dtype=np.uint8).T
 kn=[int(v,16) for v in nrec['kernel_basis']];coord=coordinates(kn)
 central={int(g):[int(v,16) for v in a] for g,a in nrec['all_action_columns'].items()}
 norms=[int(v,16) for v in nrec['all_norm_columns']]
 rels=[coord(lin(cols,v)^v) for cols in central.values() for v in kn]
 qC,free=quotient(rels,240);coin=len(free)
 norm_coin=[lin(norms,kn[j]) for j in free]
 assert coin==nrec['kernel_self_coinvariants']
 assert xor_rank(norm_coin)==nrec['kernel_self_norm_rank']
 def qactual(v):return qC(coord(v))
 # Only this extension is used on real basis pairs.  Every final pair lies
 # in the actual kernel; that assertion is checked below for source images.
 qext=[qC(coord(1<<j,False)) for j in range(256)]
 assert all(lin(qext,v)==qactual(v) for v in kn)
 km=null(phi);assert km.shape==(16,12)
 kreal=[pack(MUL[z,km[:,j]]) for j in range(12) for z in [1,2]]
 kcoord=coordinates(kreal)
 real={}
 for h,M in acts.items():
  real[h]=[pack(MUL[FB[z] if flips[h] else z,M[:,j]]) for j in range(16) for z in [1,2]]
  for v in kreal:assert not np.any(mm(phi,unpack(lin(real[h],v),16)[:,None]))
 reps=sorted({min(int(T[g,h]) for h in H) for g in range(576)})
 orbit=len(reps);assert orbit==rec['orbit_size']
 loc={int(T[g,h]):(j,h) for j,g in enumerate(reps) for h in H};assert len(loc)==576
 ell=np.array(char,dtype=np.int16);n=32*orbit;ns=24*orbit;mask32=(1<<32)-1
 def matrix_cols(g,translation=None):
  translation=np.zeros(4,dtype=np.int16) if translation is None else np.array(translation,dtype=np.int16)
  out=[]
  for a,r in enumerate(reps):
   b,h=loc[int(T[g,r])]
   phase=int(ell@QL[INV[reps[b]]]@translation%3)
   out.extend(scalar(v,[1,2,3][phase])<<(32*b) for v in real[h])
  return out
 def sourcecoord(v):
  return sum(kcoord((v>>(32*j))&mask32)<<(24*j) for j in range(orbit))
 inputs=[v<<(32*j) for j in range(orbit) for v in kreal]
 ms=matrix_cols(S);mr=matrix_cols(R,vr);mt=matrix_cols(qt,vt);identity=[1<<i for i in range(n)]
 assert [lin(ms,v) for v in ms]==identity
 assert [lin(mr,lin(mr,v)) for v in mr]==identity
 assert [lin(ms,v) for v in mr]==mt
 at=identity[:];N=[0]*n;powers=[]
 for j in range(36):
  powers.append(at[:]);N=[a^b for a,b in zip(N,at)];at=[lin(mt,v) for v in at]
  if j==11:assert at==identity
 assert at==identity and all(lin(mt,v)==v for v in N)
 simg=[lin(ms,v) for v in inputs];rimg=[lin(mr,v) for v in inputs]
 timg=[lin(mt,v) for v in inputs];nimg=[lin(N,v) for v in inputs]
 sk=[sourcecoord(v) for v in simg];rk=[sourcecoord(v) for v in rimg]
 tk=[sourcecoord(v) for v in timg];nk=[sourcecoord(v) for v in nimg]
 pairtable=[[lin(qext,average_wedge(v,1<<j)) for j in range(32)] for v in kreal]
 def projected(i,z):
  j,k=divmod(i,24);return lin(pairtable[k],(z>>(32*j))&mask32)
 # Check that every block pair used on the actual source kernel is in C.
 for i,v in enumerate(kreal):
  for w in kreal:
   a=average_wedge(v,w)
   assert lin([int(z,16) for z in nrec['small_projection_columns']],a)==0
   assert lin(qext,a)==qactual(a)
 scol=[projected(i,v) for i,v in enumerate(simg)]
 tcol=[projected(i,v) for i,v in enumerate(nimg)]
 assert all(lin(norm_coin,v)==0 for v in scol+tcol)
 polar=0
 for i,j in combinations(range(ns),2):
  assert projected(i,simg[j])^projected(j,simg[i])==0
  assert projected(i,nimg[j])^projected(j,nimg[i])==0
  polar+=2
 snorm=[v^(1<<i) for i,v in enumerate(sk)]
 ks=kernel(snorm);kt=kernel(nk)
 assert all(lin(scol,v)==0 for v in ks)
 assert all(lin(tcol,v)==0 for v in kt)
 chosen=[];basis={};combined=scol+tcol
 for i,v in enumerate(combined):
  while v:
   p=v.bit_length()-1
   if p not in basis:basis[p]=v;chosen.append(i);break
   v^=basis[p]
 cusp18_q=0;cusp18_v=np.zeros(4,dtype=np.int16)
 for _ in range(18):cusp18_v=(cusp18_v+QL[cusp18_q]@vt)%3;cusp18_q=int(T[cusp18_q,qt])
 assert matrix_cols(cusp18_q,cusp18_v)==powers[18]
 row={'character':char,'orbit_size':orbit,'compact_kernel_global_dimension':240*orbit,
  'source_homology_kernel_dimension':ns,'coinvariant_dimension':coin,
  'ordinary_norm_rank':xor_rank(norm_coin),'ordinary_norm_kernel_dimension':coin-xor_rank(norm_coin),
  'source_s_correction_rank':xor_rank(scol),'full_cusp36_correction_rank':xor_rank(tcol),
  'joint_correction_rank':len(chosen),'remaining_norm_kernel_dimension':coin-xor_rank(norm_coin)-len(chosen),
  'full_polar_equations_checked':polar,'source_s_norm_kernel_dimension':len(ks),
  'cusp36_norm_kernel_dimension':len(kt),'both_maps_factor_through_actual_cyclic_norms':True,
  'cusp18_q_state':cusp18_q,'cusp18_translation':cusp18_v.tolist(),
  'coinvariant_representatives_in_kernel_basis':free,
  'ordinary_norm_columns_on_coinvariants':[hex(v) for v in norm_coin],
  'actual_homology_kernel_basis_columns':[hex(v) for v in inputs],
  'actual_source_s_columns':[hex(v) for v in ms],'actual_source_r_columns':[hex(v) for v in mr],
  'actual_cusp_columns':[hex(v) for v in mt],'actual_full36_norm_columns':[hex(v) for v in N],
  'source_s_kernel_action_columns':[hex(v) for v in sk],'source_r_kernel_action_columns':[hex(v) for v in rk],
  'cusp_kernel_action_columns':[hex(v) for v in tk],'full36_kernel_norm_columns':[hex(v) for v in nk],
  'source_s_correction_columns':[hex(v) for v in scol],'full36_cusp_correction_columns':[hex(v) for v in tcol],
  'independent_correction_source_indices':chosen,'independent_correction_images':[hex(combined[i]) for i in chosen]}
 rows.append(row)
 print(json.dumps({k:v for k,v in row.items() if not isinstance(v,list)}),flush=True)
result={'summary':{'status':'PASS','actual_source_s_state':S,'actual_source_r_state':R,
 'actual_cusp_q_state':qt,'actual_cusp_translation':vt.tolist(),
 'compact_kernel_global_dimension':sum(r['compact_kernel_global_dimension'] for r in rows),
 'coinvariant_dimension':sum(r['coinvariant_dimension'] for r in rows),
 'ordinary_norm_rank':sum(r['ordinary_norm_rank'] for r in rows),
 'ordinary_norm_kernel_dimension':sum(r['ordinary_norm_kernel_dimension'] for r in rows),
 'joint_actual_correction_rank':sum(r['joint_correction_rank'] for r in rows),
 'remaining_norm_kernel_dimension':sum(r['remaining_norm_kernel_dimension'] for r in rows),
 'polar_equations_checked':sum(r['full_polar_equations_checked'] for r in rows),
 'literal_real_wedge_checks':496,'elapsed_seconds':time.time()-start},'cases':rows,
 'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
(OUT/'d_residual_compact_cusp.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps(result['summary'],indent=2),flush=True)
