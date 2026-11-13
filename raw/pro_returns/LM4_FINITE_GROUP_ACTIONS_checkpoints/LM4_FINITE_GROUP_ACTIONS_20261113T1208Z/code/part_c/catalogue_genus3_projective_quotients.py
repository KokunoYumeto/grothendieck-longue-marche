#!/usr/bin/env python3
"""All mixed genus-three actions with projective-plane quotient.  Exact
orientation-double kernels from the attributed KNS sphere catalogue;
source fusion uses colored disc braids and one-sided puncture slides.
"""
from pathlib import Path
from collections import Counter
import json,csv,sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from catalogue_genus3_reflection_quotients import Group,braid,braid_generators,ordered,hom,hyperelliptic
from catalogue_genus3_hyperelliptic import SurfaceOrbifold,pmul,pinv
ROOT=HERE.parent/'root'
if not (ROOT/'catalogue_higher_genus.py').exists():ROOT=HERE.parents[1]/'root'

def data(G,v,l):
 x=tuple(v[:l]);y=tuple(G.inv[q] for q in reversed(v[l:]));A=G.inv[G.prod(x)]
 images=y+tuple(G.conj(A,G.inv[q]) for q in reversed(x))
 a=hom(G,v,images)
 if a is not None:
  assert a[A]==A
  assert all(a[a[q]]==G.conj(A,q) for q in range(G.n))
 return x,a,A

def encode(G,x,a):
 v=tuple(x)+tuple(G.inv[a[q]] for q in reversed(x))
 assert G.prod(v)==G.one
 return v

def slide_last(G,x,a):
 q=x[-1]
 xx=x[:-1]+(G.conj(q,G.inv[a[q]]),)
 aa=tuple(G.conj(q,a[h]) for h in range(G.n))
 return xx,aa

def neighbours(G,v,n):
 x,a,A=data(G,v,len(n));assert a is not None
 for word in braid_generators(n):
  xx=x;dd=n
  for i,s in word:xx,dd=braid(G,xx,dd,i,s)
  assert dd==n;yield encode(G,xx,a)
 for i in range(len(n)):
  xx=x;aa=a;dd=n
  for j in range(i,len(n)-1):xx,dd=braid(G,xx,dd,j,1)
  xx,aa=slide_last(G,xx,aa)
  for j in range(len(n)-2,i-1,-1):xx,dd=braid(G,xx,dd,j,-1)
  assert dd==n;yield encode(G,xx,aa)

def make_model(G,x,a,A,cid):
 N=G.n
 def mul(v,w):
  h,b=v%N,v//N;k,c=w%N,w//N
  value=G.mul[h][a[k] if b else k]
  if b and c:value=G.mul[value][A]
  return value+N*(b^c)
 def regular(q):return tuple(mul(q,w) for w in range(2*N))
 t=regular(G.one+N);cones=[regular(q) for q in x]
 model=SurfaceOrbifold(cid,'RP2',cones+[t],[1]*len(cones)+[-1],cones=cones,
  order=2*N,cover_chi=-4,crosscap=t)
 return model

def hyp_key(rec):
 els={g['id']:tuple(g['permutation']) for g in rec['group_elements']}
 t=tuple(rec['presentation']['generators']['a']);ti=pinv(t)
 cones=[els[j] for j in rec['cone_generators']]
 G=Group(cones+[pmul(pmul(t,x),ti) for x in cones])
 x=tuple(G.ids[q] for q in cones)
 a=tuple(G.ids[pmul(pmul(t,q),ti)] for q in G.el)
 n=tuple(sorted(G.orders[q] for q in x))
 x=ordered(G,x,tuple(G.orders[q] for q in x),n)
 return n,G.tuple_key(encode(G,x,a))

def main():
 actions=json.loads((ROOT/'research_data/actions-genus3.json').read_text())['actions']
 rows=[];certs=[];sections=[];lookup={}
 for ai,action in enumerate(actions,1):
  if action['gamma']!=0:continue
  counts=Counter(action['bd'])
  if any(c%2 for c in counts.values()):continue
  n=tuple(m for m in sorted(counts) for _ in range(counts[m]//2))
  ms=tuple(action['bd']);target=n+tuple(reversed(n));l=len(n)
  G=Group([tuple(x-1 for x in p) for p in action['autgreps'][0]])
  vs=[ordered(G,G.ids_of(v),ms,target) for v in action['autgreps']]
  keys={G.tuple_key(v):i for i,v in enumerate(vs)};assert len(keys)==len(vs)
  valid={i for i,v in enumerate(vs) if data(G,v,l)[1] is not None}
  remaining=set(valid);orbits=[]
  while remaining:
   first=min(remaining);orb={first};todo=[first]
   for i in todo:
    for w in neighbours(G,vs[i],n):
     assert tuple(G.orders[q] for q in w)==target
     j=keys[G.tuple_key(w)];assert j in valid
     if j not in orb:orb.add(j);todo.append(j)
   assert orb<=remaining;remaining-=orb;orbits.append(sorted(orb))
  print('O3.'+str(ai),'RP2',n,'valid',len(valid),'orbits',len(orbits),flush=True)
  for orb in orbits:
   cid=f'G3P_{len(rows)+1:03}';v=vs[orb[0]];x,a,A=data(G,v,l)
   model=make_model(G,x,a,A,cid)
   pattern=((0,)*len(x),(),(),0)
   row,sec=model.analyse(pattern,cid,0);row['type']='(3,0)'
   hz=hyperelliptic(G,v,target)
   row.update({'positive_action':f'O3.{ai}','positive_group_code':action['group']['code'],
    'cone_orders':','.join(map(str,n)),'contains_hyperelliptic':hz is not None,
    'kernel_orbit':','.join(map(str,orb)),
    'negative_involutions':sum(model.orientation[q]==-1 and model.elem_order(q)==2 for q in model.group)})
   rec={'class_id':cid,'positive_action':ai,'cone_orders':n,'positive_elements':G.el,
    'positive_one':G.one,'positive_vector':v,'positive_cone_generators':x,
    'negative_conjugation':a,'negative_square':A,'hyperelliptic_element':hz,
    'kernel_orbit':orb,'kernel_orbit_keys':[G.tuple_key(vs[j]) for j in orb]}
   for key in rec['kernel_orbit_keys']:
    kk=(n,tuple(key));assert kk not in lookup;lookup[kk]=cid
   rows.append(row);certs.append(rec);sections.append(sec)
 assert sum(r['contains_hyperelliptic'] for r in rows)==4
 old=json.loads((HERE/'type_3_0_hyperelliptic_sections.json').read_text())
 oldrows={r['class_id']:r for r in csv.DictReader((HERE/'type_3_0_hyperelliptic_catalogue.csv').open())}
 newrows={r['class_id']:r for r in rows}
 fields=['order','positive_order','full_splitting_classes','nontrivial_partial_splitting_classes',
  'maximal_partial_classes_Phi','Gamma_orbits_on_Phi','oval_section_classes']
 mapping=[]
 for rec in old:
  if 'RP2' not in rec['orbifold']:continue
  cid=lookup[hyp_key(rec)]
  assert all(int(oldrows[rec['class_id']][k])==int(newrows[cid][k]) for k in fields)
  mapping.append({'hyperelliptic_class':rec['class_id'],'projective_class':cid})
 assert len(mapping)==4 and len({r['projective_class'] for r in mapping})==4
 with (HERE/'type_3_0_projective_quotient_catalogue.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 (HERE/'type_3_0_projective_quotient_certificates.json').write_text(json.dumps(certs,indent=2)+'\n')
 (HERE/'type_3_0_projective_quotient_sections.json').write_text(json.dumps(sections,indent=2)+'\n')
 (HERE/'genus3_hyperelliptic_projective_crosscheck.json').write_text(json.dumps({'compared_classes':4,'mapping':mapping},indent=2)+'\n')
 summary={'scope':'all mixed genus-three actions with projective-plane quotient',
  'classes':len(rows),'containing_hyperelliptic':4,'additional_to_B34_B37':len(rows)-4,
  'by_order':dict(sorted(Counter(r['order'] for r in rows).items())),
  'no_negative_involution_classes':[r['class_id'] for r in rows if r['negative_involutions']==0]}
 (HERE/'catalogue_genus3_projective_quotients_output.json').write_text(json.dumps(summary,indent=2)+'\n')
 print('FINAL',json.dumps(summary),flush=True)
if __name__=='__main__':main()
