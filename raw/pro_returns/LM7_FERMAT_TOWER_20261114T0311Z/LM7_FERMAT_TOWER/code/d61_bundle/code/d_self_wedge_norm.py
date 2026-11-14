#!/usr/bin/env python3
"""Literal self-wedge norm kernels on the eight D60 projective summands."""
from pathlib import Path
import numpy as np
import json,time,hashlib
OUT=Path(__file__).resolve().parent;start=time.time()
path=OUT/'d_arithmetic_A4_projective.json';D=json.loads(path.read_text())
T=np.array(json.loads((OUT/'d_arithmetic_A4_twisted.json').read_text())['Q_multiplication'],dtype=np.int16)
MUL=np.array([[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]],dtype=np.uint8)
FB=np.array([0,1,3,2],dtype=np.uint8)
def pack(h):
 assert np.array_equal(h,FB[h.T]);assert np.all(h.diagonal()<2)
 values=list(map(int,h.diagonal()))
 for i in range(len(h)):
  for j in range(i+1,len(h)):values.extend([int(h[i,j])&1,int(h[i,j])>>1])
 return sum(v<<j for j,v in enumerate(values))
def lin(cols,v):
 r=0
 while v:
  b=v&-v;r^=cols[b.bit_length()-1];v^=b
 return r
def echelon(cols):
 bas={};null=[]
 for i,v in enumerate(cols):
  w=1<<i
  while v:
   p=v.bit_length()-1
   if p not in bas:bas[p]=(v,w);break
   x,y=bas[p];v^=x;w^=y
  if not v:null.append(w)
 return bas,null
def quot(cols,n):
 b,_=echelon(cols);free=[j for j in range(n) if j not in b]
 def q(v):
  for p in sorted(b,reverse=True):
   if v>>p&1:v^=b[p][0]
  return sum(((v>>p)&1)<<j for j,p in enumerate(free))
 return q,free
def generated(gens):
 s={0};todo=[0]
 for g in todo:
  for h in gens:
   k=int(T[g,h])
   if k not in s:s.add(k);todo.append(k)
 return s
rows=[]
for B in D['blocks']:
 H0=generated(B['normal_V4_states']+B['odd_complement_generators']);assert len(H0)==36
 actions=[{int(g):np.array(m,dtype=np.uint8).T for g,m in B[n].items()} for n in ['all_first_actions','all_second_actions']]
 blocks=[]
 for A in actions:
  blocks += [{g:M[:8,:8] for g,M in A.items()},{g:M[8:,8:] for g,M in A.items()}]
 H=sorted(blocks[0]);gens=B['normal_V4_states']+B['odd_complement_generators']+[B['central_exchange_state']]
 records=[]
 for at,A in enumerate(blocks):
  reps=[(i,i,1) for i in range(8)]+[(i,j,z) for i in range(8) for j in range(i+1,8) for z in [1,2]]
  assert len(reps)==64
  norm=[0]*64;rels=[];allcols={}
  for g in H:
   M=A[g];cols=[];flip=g not in H0
   for i,j,z in reps:
    z=int(FB[z]) if flip else z
    a=MUL[z,MUL[M[:,i,None],FB[M[None,:,j]]]]
    if i!=j:a^=MUL[FB[z],MUL[M[:,j,None],FB[M[None,:,i]]]]
    cols.append(pack(a))
   assert len(echelon(cols)[0])==64
   norm=[x^y for x,y in zip(norm,cols)]
   if g in gens:rels.extend(v^(1<<j) for j,v in enumerate(cols))
   allcols[g]=cols
  q,free=quot(rels,64)
  for v in rels:assert lin(norm,v)==0
  ncols=[norm[j] for j in free];nrank=len(echelon(ncols)[0]);null=echelon(ncols)[1]
  assert len(free)-nrank==len(null)
  ker=[sum(((v>>j)&1)<<free[j] for j in range(len(free))) for v in null]
  assert all(lin(norm,v)==0 and q(v)!=0 for v in ker)
  rec={'summand':at,'global_dimension':512,'coinvariant_dimension':len(free),'norm_rank':nrank,
       'norm_kernel_dimension':len(null),'coinvariant_representatives':free,
       'actual_norm_kernel_lifts':[hex(v) for v in ker],
       'all_norm_columns':[hex(v) for v in norm],
       'all_stabilizer_action_columns':{str(g):[hex(v) for v in cs] for g,cs in allcols.items()}}
  records.append(rec)
  print(json.dumps({k:v for k,v in rec.items() if k not in ['all_norm_columns','all_stabilizer_action_columns']}),flush=True)
 rows.append({'character':B['character'],'summands':records})
result={'summary':{'status':'PASS','self_blocks_checked':8,'global_self_dimension':4096,
                   'coinvariant_dimension':sum(r['coinvariant_dimension'] for b in rows for r in b['summands']),
                   'norm_rank':sum(r['norm_rank'] for b in rows for r in b['summands']),
                   'norm_kernel_dimension':sum(r['norm_kernel_dimension'] for b in rows for r in b['summands']),
                   'arithmetic_boundary_determined':False,'elapsed_seconds':time.time()-start},
        'blocks':rows,'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
(OUT/'d_self_wedge_norm.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps(result['summary'],indent=2),flush=True)
