#!/usr/bin/env python3
r"""Actual coordinate-orbit modules supporting the peripheral corrections.

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
 if C['multiplicity']!=4:continue
 A=C['actions'];H=sorted(A);H0=set(C['H0'])
 reps=sorted({min(int(T[g,h]) for h in H) for g in range(576)})
 orbit=len(reps);assert orbit==12 and reps[0]==0
 loc={int(T[g,h]):(j,h) for j,g in enumerate(reps) for h in H}
 real={};central={};perms={}
 for h,M in A.items():
  assert all(np.count_nonzero(M[:,j])==1 for j in range(8))
  assert all(np.count_nonzero(M[i,:])==1 for i in range(8))
  perms[h]=[int(np.flatnonzero(M[:,j])[0]) for j in range(8)]
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
 pairs=sorted(set((i,j) for i,j,z in hreps));seen=set();blocks=[]
 for pair in pairs:
  if pair in seen:continue
  po={tuple(sorted((p[pair[0]],p[pair[1]]))) for p in perms.values()};seen|=po
  support=[k for k,(i,j,z) in enumerate(hreps) if (i,j) in po]
  mask=sum(1<<i for i in support)
  assert all(not(v&~mask) for cols in central.values() for k,v in enumerate(cols) if k in support)
  assert all(not(v&mask) for cols in central.values() for k,v in enumerate(cols) if k not in support)
  def project(v):return sum(((v>>j)&1)<<i for i,j in enumerate(support))
  cols_by_h={h:[project(v[k]) for k in support] for h,v in central.items()}
  norm=[0]*len(support);rels=[]
  for cols in cols_by_h.values():
   norm=[a^b for a,b in zip(norm,cols)];rels.extend(v^(1<<j) for j,v in enumerate(cols))
  qC,free=quotient(rels,len(support));norm_coin=[norm[j] for j in free]
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
    if x and y:out^=qC(project(average_wedge(x,y)))
   return out
  ma=matrix_cols(1);cols=[projected(1<<i,ma[i]) for i in range(n)]
  assert all(lin(norm_coin,v)==0 for v in cols)
  assert all(lin(cols,v^(1<<i))==0 for i,v in enumerate(ma))
  polar=0
  for i in range(n):
   for j in range(i+1,n):
    assert projected(1<<i,ma[j])^projected(1<<j,ma[i])==0;polar+=1
  rec={'pair_representative':pair,'pair_orbit':sorted(po),'hermitian_support':support,
   'fiber_dimension':len(support),'global_dimension':orbit*len(support),
   'coinvariant_dimension':len(free),'ordinary_norm_rank':xor_rank(norm_coin),
   'actual_s_correction_rank':xor_rank(cols),'full_source_s_polar_equations_checked':polar,
   'all_correction_columns':[hex(v) for v in cols],
   'coinvariant_basis_indices':[support[k] for k in free],
   'all_stabilizer_action_columns':{str(h):[hex(v) for v in cols] for h,cols in cols_by_h.items()}}
  blocks.append(rec)
  print(json.dumps({'character':C['character'],**{k:v for k,v in rec.items() if k in ['pair_representative','fiber_dimension','global_dimension','coinvariant_dimension','ordinary_norm_rank','actual_s_correction_rank']}}),flush=True)
 assert len(seen)==36 and sum(r['fiber_dimension'] for r in blocks)==64
 rows.append({'character':C['character'],'multiplicity':4,'coordinate_blocks':blocks})
result={'summary':{'status':'PASS','orbit_cases':len(rows),'each_has_four_identical_summands':True,
 'elapsed_seconds':time.time()-start},'cases':rows,'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
(OUT/'d_self_wedge_coordinate_blocks.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps(result['summary'],indent=2),flush=True)
