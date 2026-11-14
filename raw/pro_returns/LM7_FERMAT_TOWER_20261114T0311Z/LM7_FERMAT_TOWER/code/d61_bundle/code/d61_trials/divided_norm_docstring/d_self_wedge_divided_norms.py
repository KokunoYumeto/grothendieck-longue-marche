#!/usr/bin/env python3
"""Actual intermediate-cover divided norms on the remaining self kernels.

For an involution a in Q, this computes
  Lambda^2(E -> E_<a>) * sum_{<a>\Q} g
on the actual Delta-invariant self-wedge coinvariants.  The integral
transfer and peripheral source interpretation are separate proof inputs.
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
involution_classes=[];seen=set()
for a in range(1,576):
 if T[a,a]!=0 or a in seen:continue
 orbit={int(T[T[g,a],INV[g]]) for g in range(576)};seen|=orbit
 involution_classes.append({'representative':a,'class_size':len(orbit),'matrix':Q['Q_states'][a],
                            'left_coset_representatives':sorted({min(g,int(T[a,g])) for g in range(576)})})
assert [x['representative'] for x in involution_classes]==[1,314,572,573]
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
for C in cases:
 A=C['actions'];H=sorted(A);H0=set(C['H0'])
 reps=sorted({min(int(T[g,h]) for h in H) for g in range(576)})
 orbit=len(reps);assert orbit in [8,12] and reps[0]==0
 loc={}
 for j,g in enumerate(reps):
  for h in H:loc[int(T[g,h])]=(j,h)
 assert len(loc)==576
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
  # Check the full invariant-wedge identification against every literal
  # stabilizer matrix, using all64 basis columns.
  wc=wedge_columns(realcols,16)
  wc0=wedge_columns([1<<i for i in range(16)],16)
  assert wc==[lin(wc0,v) for v in cols]
 norm=[0]*64;rels=[]
 for cols in central.values():
  norm=[a^b for a,b in zip(norm,cols)]
  rels.extend(v^(1<<j) for j,v in enumerate(cols))
 qC,free=quotient(rels,64);coinv=len(free)
 norm_coin=[norm[j] for j in free];nr=xor_rank(norm_coin)
 assert (coinv,nr)==((4,2) if C['multiplicity']==1 else (3,0))
 n=16*orbit
 def matrix_cols(g):
  out=[]
  for a,r in enumerate(reps):
   b,h=loc[int(T[g,r])]
   out.extend(v<<(16*b) for v in real[h])
  assert len(out)==n
  return out
 maps=[];joint=norm_coin[:];shift=64
 for cc in involution_classes:
  a=cc['representative'];ma=matrix_cols(a)
  assert [lin(ma,v) for v in ma]==[1<<i for i in range(n)]
  qa,fr=quotient([v^(1<<i) for i,v in enumerate(ma)],n)
  assert len(fr)==n//2
  qcols=[qa(1<<i) for i in range(n)]
  for i,v in enumerate(ma):assert qa(v)==qcols[i]
  wc=wedge_columns(qcols,len(fr));assert len(wc)==64*orbit
  relative=[0]*64
  for g in cc['left_coset_representatives']:
   b,h=loc[g]
   relative=[v^(w<<(64*b)) for v,w in zip(relative,central[h])]
  out=[lin(wc,v) for v in relative]
  # The divided norm factors through the actual stabilizer coinvariants.
  assert all(lin(out,v)==0 for v in rels)
  ccols=[out[j] for j in free]
  dim=len(fr)*(len(fr)-1)//2
  joint=[v^(w<<shift) for v,w in zip(joint,ccols)];shift+=dim
  maps.append({'involution':a,'target_homology_dimension':len(fr),'target_wedge_dimension':dim,
               'divided_norm_rank_on_coinvariants':xor_rank(ccols),
               'whole_homology_involution_columns':[hex(v) for v in ma],
               'homology_coinvariant_projection_columns':[hex(v) for v in qcols],
               'all64_divided_norm_columns':[hex(v) for v in out],
               'coinvariant_divided_norm_columns':[hex(v) for v in ccols]})
 rankjoint=xor_rank(joint)
 rec={'name':C['name'],'character':C['character'],'identical_action_multiplicity':C['multiplicity'],
      'global_homology_dimension':n,'global_self_dimension':64*orbit,
      'self_coinvariant_dimension':coinv,'ordinary_norm_rank':nr,
      'norm_and_all_involution_divided_norm_rank':rankjoint,
      'remaining_kernel_dimension':coinv-rankjoint,
      'invariant_wedge_identification_all_columns_checked':True,
      'pair_coset_representatives':reps,'coinvariant_representatives':free,
      'ordinary_norm_coinvariant_columns':[hex(v) for v in norm_coin],
      'divided_norm_maps':maps}
 rows.append(rec)
 print(json.dumps({k:v for k,v in rec.items() if not isinstance(v,(list,dict)) or k=='character'}),flush=True)
 print(json.dumps({'case':C['name'],'individual_divided_norm_ranks':[(m['involution'],m['divided_norm_rank_on_coinvariants']) for m in maps]}),flush=True)
result={'summary':{'status':'PASS','actual_arithmetic_base_order':46656,'Q_order':576,
                   'all_four_involution_classes_checked':True,
                   'remaining_self_cases':len(rows),'original_total_norm_kernel_dimension':26,
                   'remaining_joint_kernel_dimension':sum((r['remaining_kernel_dimension']*r['identical_action_multiplicity']) for r in rows),
                   'source_boundary_consequence_requires_separate_integral_transfer_proof':True,
                   'elapsed_seconds':time.time()-start},'involution_classes':involution_classes,'cases':rows,
        'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
(OUT/'d_self_wedge_divided_norms.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps(result['summary'],indent=2),flush=True)
