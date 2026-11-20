"""Exact, elementary SL2 block examples prompted by scan 123/019.
No OCR, external data or classification theorem is used to construct examples.
"""
from pathlib import Path
import json
import sympy as s

def partitions(n,hi=None):
 if n==0:
  yield ()
 else:
  for a in range(min(n,hi or n),1-1,-1):
   for tail in partitions(n-a,a):yield (a,)+tail

def block(d):
 m=d-1
 E=s.zeros(d);F=s.zeros(d);H=s.diag(*[m-2*j for j in range(d)])
 for j in range(1,d):E[j-1,j]=j
 for j in range(d-1):F[j+1,j]=m-j
 return E,F,H

out={'scope':'Constructed SL2 polynomial-representation examples. Enumeration covers these block constructions, not an independently proved classification of every orbit.','ranks':{}}
for n in [3,4,5]:
 rows=[]
 for p in partitions(n):
  bs=[block(d) for d in p]
  E,F,H=[s.diag(*[b[i] for b in bs]) for i in range(3)]
  assert H*E-E*H==2*E and H*F-F*H==-2*F and E*F-F*E==H
  weights=sorted([int(H[i,i]) for i in range(n)],reverse=True)
  distinct=sorted(set(weights),reverse=True)
  multiplicities=[weights.count(w) for w in distinct]
  dims=[];total=0
  for m in multiplicities[:-1]:total+=m;dims.append(total)
  rows.append({'partition':list(p),'weights':weights,'parabolic_block_sizes':multiplicities,'proper_flag_dimensions':dims,'sl2_relations_verified':True,'trace_H':int(s.trace(H))})
 collisions=[]
 for i,a in enumerate(rows):
  for b in rows[i+1:]:
   if a['parabolic_block_sizes']==b['parabolic_block_sizes'] and a['weights']!=b['weights']:
    collisions.append({'partitions':[a['partition'],b['partition']],'weights':[a['weights'],b['weights']],'parabolic_block_sizes':a['parabolic_block_sizes'],'proper_flag_dimensions':a['proper_flag_dimensions']})
 assert collisions
 out['ranks'][f'A{n-1}']={'examples':rows,'distinct_cocharacter_collisions':collisions}
dest=Path(__file__).resolve().parents[1]/'math_checks'/'123_019_type_a_certificate.json'
dest.write_text(json.dumps(out,indent=2))
print(json.dumps({k:v['distinct_cocharacter_collisions'] for k,v in out['ranks'].items()}))
