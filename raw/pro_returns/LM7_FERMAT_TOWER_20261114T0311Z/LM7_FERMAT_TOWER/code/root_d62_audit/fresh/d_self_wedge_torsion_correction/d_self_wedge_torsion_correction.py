#!/usr/bin/env python3
r"""Actual peripheral involution corrections on the remaining self kernels.

For each marked involution this computes v -> [v wedge a(v)] in
the actual Delta-invariant self-wedge coinvariants. The actual source
involution is state1. Other classes are retained only as a diagnostic.
The basis and group helpers are copied from frozen D61; the correction
calculation and complete polar verification below are new.
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
 n=16*orbit
 def matrix_cols(g):
  out=[]
  for a,r in enumerate(reps):
   b,h=loc[int(T[g,r])];out.extend(v<<(16*b) for v in real[h])
  return out
 def projected(a,b):
  out=0
  for j in range(orbit):
   x=(a>>(16*j))&65535;y=(b>>(16*j))&65535
   if x and y:out^=qC(average_wedge(x,y))
  return out
 diagnostics=[]
 for a in [1,314,572,573]:
  ma=matrix_cols(a);assert [lin(ma,v) for v in ma]==[1<<i for i in range(n)]
  cols=[projected(1<<i,ma[i]) for i in range(n)]
  assert all(lin(norm_coin,v)==0 for v in cols)
  assert all(lin(cols,v^(1<<i))==0 for i,v in enumerate(ma))
  polar=0
  if a==1:
   for i in range(n):
    for j in range(i+1,n):
     assert projected(1<<i,ma[j])^projected(1<<j,ma[i])==0
     polar+=1
  bcols=[(1<<i)^ma[i] for i in range(n)]
  seen={};selected=[]
  for i,v in enumerate(cols):
   w=v
   while w:
    p=w.bit_length()-1
    if p not in seen:seen[p]=w;selected.append(i);break
    w^=seen[p]
  assert len(selected)==xor_rank(cols)
  diagnostics.append({'involution':a,'is_actual_source_s':a==1,'correction_rank':len(selected),
     'all_correction_columns':[hex(v) for v in cols],
     'all_involution_columns':[hex(v) for v in ma],
     'fixed_parameter_columns':[hex(v) for v in bcols],
     'independent_source_basis_indices':selected,
     'independent_fixed_parameters':[hex(bcols[i]) for i in selected],
     'independent_correction_images':[hex(cols[i]) for i in selected],
     'all_images_in_ordinary_norm_kernel':True,
     'factors_through_cyclic_norm':True,
     'full_source_s_polar_equations_checked':polar})
 rec={'case':C['name'],'character':C['character'],'multiplicity':C['multiplicity'],'homology_dimension':n,
    'self_coinvariant_dimension':coinv,'ordinary_norm_rank':nr,'ordinary_norm_kernel_dimension':coinv-nr,
    'actual_s_correction_rank':diagnostics[0]['correction_rank'],
    'remaining_kernel_after_actual_s_corrections':coinv-nr-diagnostics[0]['correction_rank'],
    'coinvariant_representatives':free,'ordinary_norm_columns_on_coinvariants':[hex(v) for v in norm_coin],
    'diagnostics':diagnostics}
 rows.append(rec)
 print(json.dumps({k:v for k,v in rec.items() if not isinstance(v,list)}),flush=True)
 print(json.dumps({'case':C['name'],'involution_correction_ranks':[(d['involution'],d['correction_rank']) for d in diagnostics]}),flush=True)
result={'summary':{'status':'PASS','actual_source_involution_state':1,
 'original_norm_kernel_dimension':26,
 'actual_source_correction_image_dimension':sum(r['multiplicity']*r['actual_s_correction_rank'] for r in rows),
 'remaining_norm_kernel_dimension':sum(r['multiplicity']*r['remaining_kernel_after_actual_s_corrections'] for r in rows),
 'arithmetic_source_transport_requires_separate_group_proof':True,
 'elapsed_seconds':time.time()-start},'cases':rows,'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
(OUT/'d_self_wedge_torsion_correction.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps(result['summary'],indent=2),flush=True)
