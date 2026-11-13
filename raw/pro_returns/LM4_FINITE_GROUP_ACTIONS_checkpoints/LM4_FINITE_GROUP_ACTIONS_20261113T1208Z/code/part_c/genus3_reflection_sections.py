#!/usr/bin/env python3
"""Construct each reflected genus-three action as H semidirect C2, certify
its NEC presentation, calculate every section, and identify its overlap
with B34 by an explicit canonical monodromy isomorphism.
"""
from pathlib import Path
import json,csv,sys
from collections import Counter
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from catalogue_genus3_reflection_quotients import Group,encode,ordered,rotate,reverse
from catalogue_genus3_hyperelliptic import SurfaceOrbifold,pmul,pinv

def construct(rec):
 positive=[tuple(p) for p in rec['positive_elements']]
 G=Group(positive)
 # The constructor sorts the same regular positive group, so ids are preserved.
 assert G.el==positive and G.one==rec['positive_one']
 a=rec['reflection_automorphism'];N=G.n
 def mul(v,w):
  h,b=v%N,v//N;k,c=w%N,w//N
  return G.mul[h][a[k] if b else k]+N*(b^c)
 def regular(v):return tuple(mul(v,w) for w in range(2*N))
 one=G.one;t=one+N
 x=rec['positive_generators_interior'];z=rec['positive_generators_corners']
 cone=[regular(q) for q in x]
 refs=[];p=one
 for q in z:
  refs.append(regular(mul(t,p)));p=G.mul[p][q]
 if not refs:refs=[regular(t)]
 e=G.inv[G.prod(x)]
 corners=rec['corner_orders']
 model=SurfaceOrbifold(rec['class_id'],'disc',cone+refs,[1]*len(cone)+[-1]*len(refs),
  cones=cone,corners=corners,refs=refs,boundary=regular(e),order=2*N,cover_chi=-4)
 return model

def hyp_key(rec):
 els={g['id']:tuple(g['permutation']) for g in rec['group_elements']}
 r0=els[rec['mirror_reflections'][0]]
 ri=pinv(r0)
 cones=[els[j] for j in rec['cone_generators']]
 corners=[els[j] for j in rec['corner_rotations']]
 gens=cones+corners+[pmul(pmul(r0,c),ri) for c in cones]
 if not gens:raise AssertionError('positive quotient is not hyperbolic')
 G=Group(gens)
 x=tuple(G.ids[q] for q in cones);z=tuple(G.ids[q] for q in corners)
 a=tuple(G.ids[pmul(pmul(r0,q),ri)] for q in G.el)
 c=tuple(G.orders[q] for q in z);n=tuple(G.orders[q] for q in x)
 if c:
  canonical=min(v[s:]+v[:s] for v in (c,tuple(reversed(c))) for s in range(len(c)))
  found=False
  for reflection in (False,True):
   zz,xx,aa=z,x,a;cc=c
   if reflection:zz,xx,aa=reverse(G,zz,xx,aa);cc=tuple(reversed(c))
   for shift in range(len(c)):
    if cc==canonical:
     z,x,a,c=zz,xx,aa,cc;found=True;break
    zz,xx,aa=rotate(G,zz,xx,aa);cc=cc[1:]+cc[:1]
   if found:break
  assert found
  n=tuple(G.orders[q] for q in x)
 target=tuple(sorted(n));x=ordered(G,x,n,target)
 v=encode(G,z,x,a)
 return c,target,G.tuple_key(v)

def main():
 certs=json.loads((HERE/'type_3_0_reflection_quotient_certificates.json').read_text())
 original=list(csv.DictReader((HERE/'type_3_0_reflection_quotient_catalogue.csv').open()))
 byid={r['class_id']:r for r in original}
 rows=[];all_data=[]
 for rec in certs:
  model=construct(rec)
  pat=((0,)*len(model.cones),(0,)*len(model.corner_orders),(0,)*len(model.refs),0)
  row,data=model.analyse(pat,rec['class_id'],0);row['type']='(3,0)'
  row.update({k:byid[rec['class_id']][k] for k in ('positive_action','positive_group_code','contains_hyperelliptic')})
  data['type']='(3,0)';data['reflection_certificate']=rec['class_id']
  rows.append(row);all_data.append(data)
  print(rec['class_id'],'order',model.order,'partial',len(data['sections']),flush=True)
 with (HERE/'type_3_0_reflection_quotient_sections_catalogue.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 (HERE/'type_3_0_reflection_quotient_sections.json').write_text(json.dumps(all_data,indent=2)+'\n')
 lookup={}
 for rec in certs:
  for key in rec['kernel_orbit_keys']:
   z=(tuple(rec['corner_orders']),tuple(rec['cone_orders']),tuple(key))
   assert z not in lookup;lookup[z]=rec['class_id']
 old=json.loads((HERE/'type_3_0_hyperelliptic_sections.json').read_text())
 oldrows={r['class_id']:r for r in csv.DictReader((HERE/'type_3_0_hyperelliptic_catalogue.csv').open())}
 newrows={r['class_id']:r for r in rows}
 fields=['order','positive_order','full_splitting_classes','nontrivial_partial_splitting_classes',
  'maximal_partial_classes_Phi','Gamma_orbits_on_Phi','oval_section_classes',
  'reflection_classes_with_multiple_maximal_extensions']
 mapping=[]
 for rec in old:
  if not rec['mirror_reflections']:continue
  key=hyp_key(rec);new=lookup[key]
  assert all(int(oldrows[rec['class_id']][k])==int(newrows[new][k]) for k in fields),(rec['class_id'],new)
  mapping.append({'hyperelliptic_class':rec['class_id'],'reflection_class':new})
 assert len(mapping)==57 and len({r['reflection_class'] for r in mapping})==57
 cross={'compared_classes':57,'method':'canonical rooted colored Cayley graph of the doubled NEC monodromy',
  'matched_invariant_columns':fields,'mapping':mapping}
 (HERE/'genus3_hyperelliptic_reflection_crosscheck.json').write_text(json.dumps(cross,indent=2)+'\n')
 print('FINAL: all 145 section catalogues and 57 explicit hyperelliptic comparison isomorphisms passed.',flush=True)
if __name__=='__main__':main()
