#!/usr/bin/env python3
"""Exact ninth-symbol image of E101's COMPLETE ordinary norm lattice."""
from pathlib import Path
import json
from sympy import Matrix,eye

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent
records=[json.loads(l) for l in (ROOT/'research_e76/code/e_basechange_export.out').read_text().splitlines() if l.startswith('{')]
rec=next(r for r in records if r.get('type')=='global_unit_characters' and r.get('n')==9)
M=Matrix(rec['matrix'])
P=eye(9)
for i in [0,4,7,8]:P[i,i]=3
P[0,1]=P[0,3]=1;P[4,5]=2
MP=M*P
assert all(x%3==0 for x in MP)
D=(MP/3).applyfunc(lambda x:int(x)%3)
def rref3(A):
 a=[list(map(lambda x:int(x)%3,A.row(i))) for i in range(A.rows)]
 h=0;ps=[]
 for j in range(A.cols):
  k=next((k for k in range(h,A.rows) if a[k][j]),None)
  if k is None:continue
  a[h],a[k]=a[k],a[h];v=pow(a[h][j],-1,3);a[h]=[(x*v)%3 for x in a[h]]
  for k in range(A.rows):
   if k!=h and a[k][j]:
    v=a[k][j];a[k]=[(x-v*y)%3 for x,y in zip(a[k],a[h])]
  ps.append(j);h+=1
 return Matrix(a),ps
R,piv=rref3(D)
out={'status':'PASS','ninth_unit_character_matrix':rec['matrix'],'ordinary_norm_lattice_columns':P.tolist(),
     'exact_ninth_character_product':MP.tolist(),'divided_cubic_character_matrix':D.tolist(),
     'image_rank':len(piv),'image_generator_columns':piv,'rref':R.tolist(),
     'B2_class_number_3part':81,'B3_ambiguous_class_number_3part':81*3**(5-len(piv))}
(HERE/'e_next_unit_characters.json').write_text(json.dumps(out,indent=2,default=int)+'\n')
print(json.dumps(out,indent=2,default=int))
