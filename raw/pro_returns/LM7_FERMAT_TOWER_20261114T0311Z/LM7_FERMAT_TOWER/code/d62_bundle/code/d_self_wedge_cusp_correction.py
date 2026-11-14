#!/usr/bin/env python3
r"""Actual cusp and source-involution corrections on the self kernels.

This computes v -> [v wedge s(v)] and v -> [v wedge N_36(t)v]
using the actual affine source matrices. It checks the entire polar maps,
cyclic-norm factorizations, and joint image on each remaining self block.
The source-word/inner-conjugation construction is proved separately.
The finite group, field and induction helpers retain the frozen D61 maps.
"""
from pathlib import Path
import numpy as np
import json,time,hashlib
OUT=Path(__file__).resolve().parent;start=time.time()
paths=[OUT/n for n in ['d_arithmetic_A4_twisted.json','d_arithmetic_A4_projective.json','d_orbit12_projective_kernel.json']]
Q,Old,New=[json.loads(p.read_text()) for p in paths]
T=np.array(Q['Q_multiplication'],dtype=np.int16)
INV=[next(h for h in range(576) if T[g,h]==0) for g in range(576)]
MUL=np.array([[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]],dtype=np.uint8)
FB=np.array([0,1,3,2],dtype=np.uint8)
def xor_rank(cols):
 b={}
 for v in cols:
  while v:
   p=v.bit_length()-1
   if p not in b:b[p]=v;break
   v^=b[p]
 return len(b)
def lin(cols,v):
 r=0
 while v:
  b=v&-v;r^=cols[b.bit_length()-1];v^=b
 return r
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
def gen(gens):
 s={0};todo=[0]
 for g in todo:
  for h in gens:
   w=int(T[g,h])
   if w not in s:s.add(w);todo.append(w)
 return sorted(s)
def hpack(a):
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
def wedge_columns(qcols,n):
 ans=[]
 for block in range(len(qcols)//16):
  c=qcols[16*block:16*block+16]
  ans.extend(wedge(c[2*i],c[2*i+1],n) for i in range(8))
  for i in range(8):
   for j in range(i+1,8):
    u,v,U,V=c[2*i],c[2*i+1],c[2*j],c[2*j+1]
    # The Hermitian offdiagonal1 is u^V+v^U; offdiagonal z is
    # u^U+v^U+v^V under the actual invariant-wedge identification.
    ans.append(wedge(u,V,n)^wedge(v,U,n))
    ans.append(wedge(u,U,n)^wedge(v,U,n)^wedge(v,V,n))
 return ans
cases=[]
B=Old['blocks'][0]
acts={int(g):np.array(m,dtype=np.uint8).T[8:,8:] for g,m in B['all_second_actions'].items()}
H0=gen(B['normal_V4_states']+B['odd_complement_generators'])
cases.append({'name':'old_orbit0001_summand3','character':B['character'],'actions':acts,'H0':H0,'multiplicity':1})
for B in New['blocks']:
 acts0={int(g):np.array(m,dtype=np.uint8).T for g,m in B['all_projective_actions'].items()}
 for M in acts0.values():
  for i in range(4):assert np.array_equal(M[:8,:8],M[8*i:8*i+8,8*i:8*i+8])
 H0=gen(B['V4_states']+[B['C3_generator'],B['normalizing_involution']])
 cases.append({'name':'new_orbit'+''.join(map(str,B['character']))+'_four_identical_summands',
               'character':B['character'],'actions':{g:M[:8,:8] for g,M in acts0.items()},'H0':H0,'multiplicity':4})

rows=[]
hreps=[(i,i,1) for i in range(8)]+[(i,j,z) for i in range(8) for j in range(i+1,8) for z in [1,2]]
wc0=wedge_columns([1<<i for i in range(16)],16)
wb={}
for i,v in enumerate(wc0):
 w=1<<i
 while v:
  p=v.bit_length()-1
  if p not in wb:wb[p]=(v,w);break
  a,b=wb[p];v^=a;w^=b
 assert v
assert len(wb)==64
def wcoord(v):
 w=0
 while v:
  p=v.bit_length()-1;assert p in wb,(p,hex(v))
  a,b=wb[p];v^=a;w^=b
 return w
def scalar(v,z):return sum(int(MUL[z,(v>>(2*i))&3])<<(2*i) for i in range(8))
def average_wedge(v,w):
 return wcoord(wedge(v,w,16)^wedge(scalar(v,2),scalar(w,2),16)^wedge(scalar(v,3),scalar(w,3),16))

pa=OUT/'d_arithmetic_affine_base.json';Aff=json.loads(pa.read_text());paths.append(pa)
qstar=[np.array(m,dtype=np.int16).T for m in Aff['Q_linear_image_matrices']]
QL=np.array([qstar[j] for j in Aff['Q_to_linear_image']],dtype=np.int16)
def normq(v):return min(tuple(int(x)%12 for x in v),tuple(-int(x)%12 for x in v))
qindex={tuple(v):i for i,v in enumerate(Q['Q_states'])}
S=qindex[normq((0,1,11,0))];R=qindex[normq((0,11,1,11))];qt=int(T[S,R])
assert S==1
vr=np.array(Aff['affine_r_translation'],dtype=np.int16);vt=QL[S]@vr%3
assert not any(Aff['affine_s_translation'])
for g in range(576):
 for h in [S,R]:assert np.array_equal(QL[g]@QL[h]%3,QL[int(T[g,h])])

for C in cases:
 A=C['actions'];H=sorted(A);H0=set(C['H0'])
 reps=sorted({min(int(T[g,h]) for h in H) for g in range(576)})
 orbit=len(reps);assert orbit in [8,12] and reps[0]==0
 loc={int(T[g,h]):(j,h) for j,g in enumerate(reps) for h in H};assert len(loc)==576
 real={};central={}
 for h,M in A.items():
  flip=h not in H0;realcols=[]
  for j in range(8):
   for z in [1,2]:
    vals=MUL[FB[z] if flip else z,M[:,j]]
    realcols.append(sum(int(v)<<(2*i) for i,v in enumerate(vals)))
  real[h]=realcols;cols=[]
  for i,j,z in hreps:
   z=int(FB[z]) if flip else z
   out=MUL[z,MUL[M[:,i,None],FB[M[None,:,j]]]]
   if i!=j:out^=MUL[FB[z],MUL[M[:,j,None],FB[M[None,:,i]]]]
   cols.append(hpack(out))
  central[h]=cols
  assert wedge_columns(realcols,16)==[lin(wc0,v) for v in cols]
 norm=[0]*64;rels=[]
 for cols in central.values():
  norm=[a^b for a,b in zip(norm,cols)]
  rels.extend(v^(1<<j) for j,v in enumerate(cols))
 qC,free=quotient(rels,64);coinv=len(free)
 norm_coin=[norm[j] for j in free];nr=xor_rank(norm_coin)
 n=16*orbit;ell=np.array(C['character'],dtype=np.int16)
 def matrix_cols(g,translation=None):
  translation=np.zeros(4,dtype=np.int16) if translation is None else np.array(translation,dtype=np.int16)
  out=[]
  for a,r in enumerate(reps):
   b,h=loc[int(T[g,r])]
   phase=int(ell@QL[INV[reps[b]]]@translation%3)
   out.extend(scalar(v,[1,2,3][phase])<<(16*b) for v in real[h])
  return out
 def projected(a,b):
  out=0
  for j in range(orbit):
   x=(a>>(16*j))&65535;y=(b>>(16*j))&65535
   if x and y:out^=qC(average_wedge(x,y))
  return out
 ms=matrix_cols(S);mr=matrix_cols(R,vr);mt=matrix_cols(qt,vt);identity=[1<<i for i in range(n)]
 assert [lin(ms,v) for v in ms]==identity
 assert [lin(mr,lin(mr,v)) for v in mr]==identity
 assert [lin(ms,v) for v in mr]==mt
 at=identity[:];N=[0]*n;powers=[]
 for j in range(36):
  powers.append(at[:]);N=[a^b for a,b in zip(N,at)];at=[lin(mt,v) for v in at]
  if j==11:assert at==identity
 assert at==identity
 assert all(lin(mt,v)==v for v in N)
 # Exact action of the pure Q class314 is kept separate from the actual cusp power.
 cusp18_q=0;cusp18_v=np.zeros(4,dtype=np.int16)
 for _ in range(18):cusp18_v=(cusp18_v+QL[cusp18_q]@vt)%3;cusp18_q=int(T[cusp18_q,qt])
 cusp18=matrix_cols(cusp18_q,cusp18_v)
 assert cusp18==powers[18]
 scol=[projected(1<<i,ms[i]) for i in range(n)]
 tcol=[projected(1<<i,N[i]) for i in range(n)]
 assert all(lin(norm_coin,v)==0 for v in scol+tcol)
 assert all(lin(tcol,v^(1<<i))==0 for i,v in enumerate(mt))
 assert all(lin(scol,v^(1<<i))==0 for i,v in enumerate(ms))
 polar=0
 for i in range(n):
  for j in range(i+1,n):
   assert projected(1<<i,N[j])^projected(1<<j,N[i])==0
   assert projected(1<<i,ms[j])^projected(1<<j,ms[i])==0
   polar+=2
 combined=scol+tcol;rk=xor_rank(combined)
 assert rk==coinv-nr
 chosen=[];bas={}
 for i,v in enumerate(combined):
  while v:
   p=v.bit_length()-1
   if p not in bas:bas[p]=v;chosen.append(i);break
   v^=bas[p]
 assert len(chosen)==rk
 rec={'case':C['name'],'character':C['character'],'multiplicity':C['multiplicity'],
  'homology_dimension':n,'self_global_dimension':64*orbit,
  'self_coinvariant_dimension':coinv,'ordinary_norm_rank':nr,'norm_kernel_dimension':coinv-nr,
  's_correction_rank':xor_rank(scol),'cusp_correction_rank':xor_rank(tcol),
  'joint_correction_rank':rk,'full_norm_kernel_spanned':True,
  'cusp_actual_q_state':qt,'cusp_translation':vt.tolist(),'cusp18_q_state':cusp18_q,
  'cusp18_translation':cusp18_v.tolist(),'cusp_coefficient_order_divides12':True,
  'full_polar_equations_checked':polar,
  'coinvariant_representatives':free,
  'ordinary_norm_columns_on_coinvariants':[hex(v) for v in norm_coin],
  'actual_source_s_columns':[hex(v) for v in ms],
  'actual_source_r_columns':[hex(v) for v in mr],
  'actual_cusp_columns':[hex(v) for v in mt],
  'actual_cusp_norm36_columns':[hex(v) for v in N],
  's_correction_columns':[hex(v) for v in scol],
  'cusp_correction_columns':[hex(v) for v in tcol],
  'independent_correction_source_indices':chosen,
  'independent_correction_images':[hex(combined[i]) for i in chosen],
  'full_integral_source_transport_required':True}
 rows.append(rec)
 print(json.dumps({k:v for k,v in rec.items() if not isinstance(v,list)}),flush=True)
result={'summary':{'status':'PASS','actual_s_state':S,'actual_r_state':R,
 'actual_cusp_q_state':qt,'actual_cusp_translation':vt.tolist(),
 'original_norm_kernel_dimension':26,
 'joint_actual_s_cusp_correction_dimension':sum(r['multiplicity']*r['joint_correction_rank'] for r in rows),
 'retained_self_module_dimension':sum(r['multiplicity']*r['self_global_dimension'] for r in rows),
 'retained_self_coinvariant_dimension':sum(r['multiplicity']*r['self_coinvariant_dimension'] for r in rows),
 'remaining_norm_kernel_dimension':0,
 'arithmetic_source_transport_requires_separate_group_proof':True,
 'elapsed_seconds':time.time()-start},'cases':rows,'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
(OUT/'d_self_wedge_cusp_correction.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps(result['summary'],indent=2),flush=True)
