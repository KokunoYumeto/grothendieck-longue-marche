#!/usr/bin/env python3
"""Retain all six actual compact cross blocks in each repaired orbit.

The four rank-eight projective summands were constructed in the preceding
certificate.  This checks their literal invariant decomposition and the
two extra cross norms, beyond the four blocks between its two large sums.
"""
from pathlib import Path
from itertools import combinations
import hashlib,json,time
import numpy as np
OUT=Path(__file__).resolve().parent;start=time.time()
path=OUT/'d_arithmetic_A4_projective.json';D=json.loads(path.read_text())
T=np.array(json.loads((OUT/'d_arithmetic_A4_twisted.json').read_text())['Q_multiplication'],dtype=np.int16)
MUL=np.array([[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]],dtype=np.uint8);FB=np.array([0,1,3,2],dtype=np.uint8)
def mm(a,b):
 out=np.zeros((a.shape[0],b.shape[1]),dtype=np.uint8)
 for k in range(a.shape[1]):out^=MUL[a[:,k,None],b[k,None,:]]
 return out
def rank(cols):
 bas={}
 for v in cols:
  while v:
   p=v.bit_length()-1
   if p not in bas:bas[p]=v;break
   v^=bas[p]
 return len(bas)
def pack(a):return sum(int(v)<<(2*j) for j,v in enumerate(a.ravel()))
records=[]
for B in D['blocks']:
 allM=[{int(q):np.array(m,dtype=np.uint8).T for q,m in B[k].items()} for k in ['all_first_actions','all_second_actions']]
 H=sorted(allM[0]);sig=B['central_exchange_state'];V4=B['normal_V4_states'];c9=B['odd_complement_generators']
 H0=set()
 todo=[0];H0.add(0)
 for q in todo:
  for r in V4+c9:
   s=int(T[q,r])
   if s not in H0:H0.add(s);todo.append(s)
 assert len(H0)==36
 smaller=[]
 for M in allM:
  assert all(not np.any(m[:8,8:]) and not np.any(m[8:,:8]) for m in M.values())
  smaller.extend([{q:m[:8,:8] for q,m in M.items()},{q:m[8:,8:] for q,m in M.items()}])
 # Every actual matrix product is checked with its semilinear field action.
 for matrices in smaller:
  for q in H:
   for r in V4+c9+[sig]:
    expected=mm(matrices[q],FB[matrices[r]] if q not in H0 else matrices[r])
    assert np.array_equal(expected,matrices[int(T[q,r])])
 pairs=[]
 for a,b in combinations(range(4),2):
  norm=[0]*128;relations=[]
  for q in H:
   L,R=smaller[a][q],smaller[b][q];flip=q not in H0;cols=[]
   for i in range(8):
    for j in range(8):
     outer=MUL[L[:,i,None],FB[R[None,:,j]]]
     for z in [1,2]:cols.append(pack(MUL[FB[z] if flip else z,outer]))
   assert rank(cols)==128
   norm=[x^y for x,y in zip(norm,cols)]
   if q in V4+c9+[sig]:relations.extend(v^(1<<j) for j,v in enumerate(cols))
  nr=rank(norm);cd=128-rank(relations);assert nr==cd
  pairs.append({'summands':[a,b],'dimension_per_pair':128,'global_dimension':1024,
                'coinvariant_dimension':cd,'full_norm_rank':nr,'norm_injective':True,
                'all_norm_columns':[hex(v) for v in norm]})
 assert sum(p['coinvariant_dimension'] for p in pairs if p['summands'][0]<2<=p['summands'][1])==B['cross_coinvariant_dimension']
 rec={'character':B['character'],'four_projective_dimensions_F4':[8,8,8,8],
      'all_six_cross_blocks':pairs,'global_central_dimension':6144,
      'coinvariant_dimension':sum(p['coinvariant_dimension'] for p in pairs),
      'whole_semilinear_action_verified':True}
 records.append(rec)
 print(json.dumps({k:v for k,v in rec.items() if k!='all_six_cross_blocks'}),flush=True)
result={'summary':{'status':'PASS','actual_base_order':46656,'target_base_order':3888,
                   'two_orbits_checked':2,'global_new_central_dimension':sum(r['global_central_dimension'] for r in records),
                   'new_invariant_equation_dimension':sum(r['coinvariant_dimension'] for r in records),
                   'all_twelve_cross_norms_injective':True,
                   'remaining_in_366080_block':366080-sum(r['global_central_dimension'] for r in records),
                   'remaining_coinvariant_dimension':640-sum(r['coinvariant_dimension'] for r in records),
                   'elapsed_seconds':time.time()-start},'blocks':records,
        'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
(OUT/'d_arithmetic_A4_cross_completion.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps(result['summary'],indent=2),flush=True)
