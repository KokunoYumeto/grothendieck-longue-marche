#!/usr/bin/env python3
"""The actual one-dimensional sign quotient of N_ab/3 and its centralizer test."""
from pathlib import Path
import json,time
OUT=Path(__file__).resolve().parent;started=time.time()
D=json.loads((OUT/'d_arithmetic_correction_graph.json').read_text());S=D['mod3_s_columns'];R=D['mod3_r_columns'];n=97
records=[]
for char in [1,2]:
 rows=[]
 for j in range(n):
  rows.append([(v-char*int(i==j))%3 for i,v in enumerate(S[j])])
  rows.append([(v-int(i==j))%3 for i,v in enumerate(R[j])])
 piv={}
 for row in rows:
  v=row[:]
  while any(v):
   p=max(i for i,a in enumerate(v) if a)
   if p not in piv:
    u=pow(v[p],-1,3);piv[p]=[a*u%3 for a in v];break
   a=v[p];v=[(x-a*y)%3 for x,y in zip(v,piv[p])]
 free=[i for i in range(n) if i not in piv];basis=[]
 for f in free:
  v=[0]*n;v[f]=1
  for p in sorted(piv):v[p]=-sum(a*b for i,(a,b) in enumerate(zip(piv[p],v)) if i!=p)%3
  assert all(sum(a*b for a,b in zip(v,row))%3==0 for row in rows);basis.append(v)
 records.append({'s_character':char,'r_character':1,'quotient_multiplicity':len(basis),'quotient_covectors':basis})
assert records[0]['quotient_multiplicity']==0 and records[1]['quotient_multiplicity']==1
phi=records[1]['quotient_covectors'][0]
central=[]
for record in D['complete_centralizer_lifting_equations']['r']:
 value=sum(a*b for a,b in zip(phi,record['defect']))%3
 central.append({'q_state':record['q_state'],'q_matrix':record['q_matrix'],'projected_defect':value,'liftable_to_sign_extension':value==0})
five=[r for r in central if r['q_matrix'] in [[5,0,0,5],[7,0,0,7]]]
assert len(five)==1
summary={'scope':'Actual marked quotient of the arithmetic G3 source.',
 'trivial_quotient_multiplicity':0,'sign_quotient_multiplicity':1,
 'sign_character_on_s_r':[2,1],
 'r_centralizer_Q_images_lifted':sum(r['liftable_to_sign_extension'] for r in central),
 'actual_5I_r_centralizer_projected_defect':five[0]['projected_defect'],
 'actual_5I_r_centralizer_lifts':five[0]['liftable_to_sign_extension'],
 'elapsed_seconds':round(time.time()-started,3)}
cert={'summary':summary,'complete_one_dimensional_quotient_checks':records,
 'all18_projected_r_centralizer_equations':central}
(OUT/'d_arithmetic_sign_quotient.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
