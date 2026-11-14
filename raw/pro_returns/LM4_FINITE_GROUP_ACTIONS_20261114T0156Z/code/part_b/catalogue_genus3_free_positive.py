#!/usr/bin/env python3
"""Complete mixed genus-three actions with positive subgroup free C2,
and all six actions with trivial positive subgroup. Exact F2 monodromy
orbits, explicit NEC presentations, and complete mirror-section graphs.
"""
from collections import Counter,deque
from itertools import product
from pathlib import Path
import csv,json
OUT=Path(__file__).resolve().parent
V4=frozenset(product(range(2),repeat=2));C2=frozenset({(0,0),(0,1)});ID=(0,0)
def mul(a,b):return a[0]^b[0],a[1]^b[1]
def closure(gs):
 out={ID};todo=list(gs)
 while todo:
  x=todo.pop()
  if x in out:continue
  out.add(x)
  todo.extend(mul(x,y) for y in tuple(out) if mul(x,y) not in out)
 return frozenset(out)

def char_orbits(orient,genus,boundaries):
 n=2*genus if orient else genus;b=boundaries
 eps=(0 if orient else 1,)*n+(0,)*b+(1,)*b
 chars=[v for v in product(range(2),repeat=n+2*b)
         if sum(v[n:n+b])%2==0 and v!=(0,)*(n+2*b) and v!=eps]
 def moves(v):
  yield tuple(a^e for a,e in zip(v,eps))
  for j in range(b-1):
   w=list(v)
   for start in (n,n+b):w[start+j],w[start+j+1]=w[start+j+1],w[start+j]
   yield tuple(w)
  if orient and genus==1:
   w=list(v);w[0],w[1]=w[1],w[0];yield tuple(w)
   w=list(v);w[0]^=w[1];yield tuple(w)
  if not orient:
   for j in range(genus-1):
    w=list(v);w[j],w[j+1]=w[j+1],w[j];yield tuple(w)
   if genus==1 and b==2:
    w=list(v);w[0]^=w[n];yield tuple(w)
 left=set(chars);orbits=[]
 while left:
  v=min(left);seen={v};todo=[v]
  while todo:
   x=todo.pop()
   for y in moves(x):
    assert y in chars
    if y not in seen:seen.add(y);todo.append(y)
  left-=seen;orbits.append(sorted(seen))
 return orbits

def monodromy(orient,genus,b,alpha,group):
 n=2*genus if orient else genus
 top=alpha[:n];betas=alpha[n:n+b];gammas=alpha[n+b:]
 generators={}
 if orient:
  for i in range(genus):
   generators[f'a{i+1}']=(top[2*i],0)
   generators[f'b{i+1}']=(top[2*i+1],0)
 else:
  for i in range(genus):generators[f'u{i+1}']=(top[i],1)
 for j in range(b):
  generators[f'e{j+1}']=(betas[j],0)
  generators[f'c{j+1}']=(gammas[j],1)
 assert closure(generators.values())==group
 assert sum(betas)%2==0
 assert all(g[1]==int(name.startswith(('u','c'))) for name,g in generators.items())
 assert all(mul(generators[f'c{j+1}'],generators[f'c{j+1}'])==ID for j in range(b))
 chi=2-(2*genus if orient else genus)-b
 assert len(group)*chi==-4
 relators=[f'c{j+1}^2=1' for j in range(b)]+[f'[e{j+1},c{j+1}]=1' for j in range(b)]
 relators.append(' '.join(([f'[a{i+1},b{i+1}]' for i in range(genus)] if orient else [f'u{i+1}^2' for i in range(genus)])+[f'e{j+1}' for j in range(b)])+'=1')
 return generators,betas,gammas,relators,chi

def sections(group,generators,b,classid):
 elements=sorted(group);ids={g:i for i,g in enumerate(elements)}
 nodes=[];nodekeys={};stabs={};graph={}
 for j in range(b):
  r=generators[f'c{j+1}'];e=generators[f'e{j+1}'];h=frozenset({ID,r})
  cosets=sorted({frozenset(mul(g,x) for x in h) for g in group},key=lambda c:sorted(c))
  for c in cosets:
   for t in range(3):
    key=(j,c,t);nodekeys[key]=len(nodes);nodes.append(key);stabs[key]=h
  for c in cosets:
   nextc=frozenset(mul(e,x) for x in c)
   path=[(j,c,0),(j,c,1),(j,c,2),(j,nextc,0)]
   for x,y in zip(path,path[1:]):graph.setdefault(x,set()).add(y);graph.setdefault(y,set()).add(x)
 assert all(len(v)==2 for v in graph.values())
 records=[];objects=[]
 for r in group-{ID}:
  if not r[1]:continue
  fixed={x for x in graph if r in stabs[x]};left=set(fixed)
  while left:
   x=min(left,key=lambda a:nodekeys[a]);seen=set();todo=[x]
   while todo:
    y=todo.pop()
    if y in seen:continue
    seen.add(y);todo.extend((graph[y]&fixed)-seen)
   left-=seen;objects.append((r,frozenset(seen)))
 def act(g,obj):
  r,ns=obj
  return r,frozenset((j,frozenset(mul(g,x) for x in c),t) for j,c,t in ns)
 object_ids={x:i for i,x in enumerate(objects)};left=set(objects);orbits=[]
 while left:
  x=next(iter(left));orb={act(g,x) for g in group};assert orb<=set(objects)
  left-=orb;orbits.append(sorted(object_ids[y] for y in orb))
 for i,obj in enumerate(objects):
  r,ns=obj
  records.append({'section_id':i,'image_elements':[ids[ID],ids[r]],'kind':'oval',
   'fixed_component_nodes':sorted(nodekeys[x] for x in ns),'centralizer':'Z',
   'mu':{ids[ID]:'0',ids[r]:'1/2'},'maximal':True,'strict_extensions':[],
   'maximal_overgroups':[i],'Gamma_stabilizer':sorted(ids[g] for g in group if act(g,obj)==obj)})
 full=len(objects) if len(group)==2 else 0
 row={'class_id':classid,'type':'(3,0)','order':len(group),'positive_order':len(group)//2,
  'full_splitting_classes':full,'nontrivial_partial_splitting_classes':len(objects),
  'maximal_partial_classes_Phi':len(objects),'Gamma_orbits_on_Phi':len(orbits),
  'oval_section_classes':len(objects),'line_section_classes':0}
 data={'class_id':classid,'group_elements':[{'id':ids[g],'coordinates':g,'orientation':(-1)**g[1]} for g in elements],
  'multiplication':[[ids[mul(g,h)] for h in elements] for g in elements],
  'nodes':[{'id':nodekeys[x],'boundary':x[0],'coset_elements':sorted(ids[g] for g in x[1]),'subdivision_position':x[2],
            'stabilizer_elements':sorted(ids[g] for g in stabs[x])} for x in nodes],
  'graph_edges':sorted({tuple(sorted((nodekeys[x],nodekeys[y]))) for x in graph for y in graph[x]}),
  'sections':records,'Phi_orbits':orbits}
 return row,data

def main():
 signatures=[(True,0,3),(True,1,1),(False,1,2),(False,2,1),(False,3,0)]
 expected=[4,1,4,2,1];rows=[];details=[];orbitmap=[]
 for (orient,g,b),count in zip(signatures,expected):
  orbs=char_orbits(orient,g,b);assert len(orbs)==count
  orbitmap.append({'orientable':orient,'genus_or_crosscaps':g,'boundary_components':b,'count':len(orbs),'character_orbits':orbs})
  for orb in orbs:
   alpha=orb[0];gens,betas,gammas,rels,chi=monodromy(orient,g,b,alpha,V4)
   cid=f'G3freeC2_{len(rows)+1:02}';row,data=sections(V4,gens,b,cid)
   assert row['maximal_partial_classes_Phi']==sum(1 if q else 2 for q in betas)
   assert row['Gamma_orbits_on_Phi']==b
   row.update({'positive_source':'O3.2','quotient_orientable':orient,'quotient_genus_or_crosscaps':g,
    'mirror_boundary_components':b,'monodromy_alpha':str(alpha)})
   data.update({'monodromy':gens,'quotient_relators':rels,'quotient_euler_characteristic':chi,
    'cover_euler_characteristic':len(V4)*chi,'monodromy_orbit':orb})
   rows.append(row);details.append(data)
 assert len(rows)==12
 # All pure anti-involutions are the orientation-double covers of these six surfaces.
 anti=[(True,0,4),(True,1,2),(False,1,3),(False,2,2),(False,3,1),(False,4,0)]
 for j,(orient,g,b) in enumerate(anti,1):
  n=2*g if orient else g;alpha=(0,)*(n+2*b)
  gens,betas,gammas,rels,chi=monodromy(orient,g,b,alpha,C2)
  cid=f'G3anti_{j:02}';row,data=sections(C2,gens,b,cid)
  assert row['full_splitting_classes']==b and row['maximal_partial_classes_Phi']==b
  row.update({'positive_source':'O3.1','quotient_orientable':orient,'quotient_genus_or_crosscaps':g,
   'mirror_boundary_components':b,'monodromy_alpha':str(alpha)})
  data.update({'monodromy':gens,'quotient_relators':rels,'quotient_euler_characteristic':chi,
   'cover_euler_characteristic':len(C2)*chi})
  rows.append(row);details.append(data)
 odd_squares=[{'crosscap_images':v,'relator_value':sum(2*x for x in v)%4} for v in product((1,3),repeat=3)]
 assert all(v['relator_value']==2 for v in odd_squares)
 with (OUT/'type_3_0_free_positive_and_anti_catalogue.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 (OUT/'type_3_0_free_positive_and_anti_sections.json').write_text(json.dumps({'catalogue':details,
  'monodromy_orbits':orbitmap,'C4_obstruction':odd_squares},indent=2)+'\n')
 summary={'free_positive_C2_mixed_classes':12,'by_quotient_signature':[r['count'] for r in orbitmap],
  'trivial_positive_mixed_classes':6,'total':len(rows),'C4_orientation_compatible_free_extensions':0}
 (OUT/'catalogue_genus3_free_positive_output.json').write_text(json.dumps(summary,indent=2)+'\n')
 print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
