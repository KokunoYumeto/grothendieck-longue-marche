#!/usr/bin/env python3
"""Independent finite certificate for the Haran rank-three quotient.

Uses integer labels and a separate multiplication implementation.  The
output is compared with the existing Part A certificate, and records the
actual quotient map on l,a,b,t, including the intertwining identity.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json

HERE=Path(__file__).resolve().parent

def encode(x,y,e):return 6*(x%3)+2*(y%3)+(e%2)
def decode(a):return a//6,(a//2)%3,a%2
def multiply(a,b):
 x,y,e=decode(a);u,v,f=decode(b)
 return encode(x+(-1)**e*u,y+(-1)**e*v,e+f)
def generate(gens):
 seen={0};todo=[0]
 for a in todo:
  for g in gens:
   b=multiply(a,g)
   if b not in seen:seen.add(b);todo.append(b)
 return sorted(seen)
def power(a,n):
 out=0
 for _ in range(n):out=multiply(out,a)
 return out
def mm(A,B):
 return [[sum(a*b for a,b in zip(row,col))%3 for col in zip(*B)] for row in A]

def main():
 Q=range(18);table=[[multiply(a,b) for b in Q] for a in Q]
 assert all(table[0][a]==a==table[a][0] for a in Q)
 inverse=[next(b for b in Q if table[a][b]==table[b][a]==0) for a in Q]
 assert all(table[table[a][b]][c]==table[a][table[b][c]] for a,b,c in product(Q,repeat=3))
 orders=[next(k for k in range(1,19) if power(a,k)==0) for a in Q]
 assert Counter(orders)=={1:1,2:9,3:8}
 positive=[a for a in Q if a%2==0]
 assert len(positive)==9 and generate([encode(1,0,0),encode(0,1,0)])==positive
 assert all(table[a][b]%2==(a+b)%2 for a,b in product(Q,repeat=2))
 pair_sizes=Counter(len(generate([a,b])) for a,b in product(Q,repeat=2))
 assert pair_sizes=={1:1,2:27,3:32,6:216,9:48}
 triple_sizes=Counter(len(generate([a,b,c])) for a,b,c in product(Q,repeat=3))
 assert triple_sizes[18]>0 and 18 not in pair_sizes
 images={'l':encode(1,0,0),'a':encode(0,1,0),
         'b':encode(0,-1,0),'t':encode(0,0,1),'c':0}
 assert len(generate([images[k] for k in ('l','a','t')]))==18
 # Columns correspond to the free generators l,a,b.  M is alpha on mod-3
 # abelianization; q is the displayed rank-two quotient map.
 M=[[2,0,0],[0,0,1],[0,1,0]]
 q=[[1,0,0],[0,1,2]]
 assert mm(q,M)==[[(-x)%3 for x in row] for row in q]
 alpha_images={'l':power(images['l'],2),'a':images['b'],'b':images['a']}
 t=images['t'];checks={}
 for name in ('l','a','b'):
  actual=table[table[t][images[name]]][inverse[t]]
  assert actual==alpha_images[name]
  checks[name]={'image':images[name],'alpha_image':alpha_images[name],
                'conjugate_by_t':actual}
 assert table[t][t]==images['c']==0
 # All finite compatibility identities implied by q alpha = -q and q(c)=0.
 assert all(table[table[t][v]][inverse[t]]==inverse[v] for v in positive)
 oldroot=HERE.parent if (HERE.parent/'root').is_dir() else HERE.parents[1]
 oldpath=oldroot/'part_a'/'haran_rank3_output.json'
 if not oldpath.exists():oldpath=oldroot/'part_a'/'code'/'haran_rank3_output.json'
 old=json.loads(oldpath.read_text())
 assert old['quotient_order']==18 and old['associativity_checks']==18**3
 assert old['ordered_generating_pairs_tested']==18**2
 assert old['pair_generated_subgroup_order_histogram']=={str(k):v for k,v in sorted(pair_sizes.items())}
 out={'quotient':'(F_3)^2 semidirect C_2 by inversion',
  'elements':[{'id':a,'coordinates':decode(a),'order':orders[a],'inverse':inverse[a]} for a in Q],
  'multiplication':table,'identity':0,'positive_elements':positive,
  'group_order':18,'associativity_checks':18**3,'orientation_product_checks':18**2,
  'ordered_pairs_tested':18**2,'ordered_triples_tested':18**3,
  'pair_generated_subgroup_order_histogram':dict(sorted(pair_sizes.items())),
  'triple_generated_subgroup_order_histogram':dict(sorted(triple_sizes.items())),
  'minimum_number_of_generators':3,'quotient_map_on_generators':images,
  'mod3_alpha_matrix':M,'mod3_quotient_matrix':q,
  'q_alpha_equals_minus_q':True,'kappa_mod3':0,'q_c':0,
  'all_conjugation_relation_checks':checks,'t_squared_equals_q_c':True,
  'existing_haran_output_agrees':True,
  'profinite_rank_consequence':{'rank_H':3,'index_H_in_E':2,'free_rank_forced_by_Schreier':2,
   'finite_quotient_generator_rank':3,'E_topological_generator_rank':3,
   'contradiction':'A quotient of a two-generator profinite group is two-generated.'}}
 (HERE/'haran_quotient_independent_audit.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ('elements','multiplication')},indent=2))

if __name__=='__main__':main()
