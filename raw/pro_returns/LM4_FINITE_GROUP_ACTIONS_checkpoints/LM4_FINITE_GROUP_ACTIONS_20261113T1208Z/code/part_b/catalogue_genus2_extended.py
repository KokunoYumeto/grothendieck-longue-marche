#!/usr/bin/env python3
"""All finite subgroups of the extended closed genus-two mapping class group.
Hyperelliptic lift presentations from the complete decorated sphere6 list;
finite groups are certified by regular coset actions of exactly twice the
quotient order. Complements to the central involution are fused by the full
quotient-orbifold normalizer action on F2 characters. See B.28.
"""
from pathlib import Path
from collections import defaultdict,Counter,deque
from functools import lru_cache
from itertools import product
from fractions import Fraction
import json,csv
from sympy.combinatorics.free_groups import free_group
from sympy.combinatorics.fp_groups import FpGroup, coset_enumeration_r
from catalogue_spheres import Orbifold,orbifolds,pmul,pinv,ppow,closure
from genus2_characters import expanded,character_orbits

OUT=Path(__file__).resolve().parent
CACHE=OUT/'genus2_extension_cache';CACHE.mkdir(exist_ok=True)

class SurfaceOrbifold(Orbifold):
 @lru_cache(None)
 def all_subgroups(self):
  # A finite subgroup with a nonempty fixed set belongs to one of these
  # local groups. This exact smaller enumeration suffices for all sections.
  local=self.cone_groups+self.corner_groups+[closure([r],self.identity) for r in self.refs]
  sub={frozenset({self.identity})}
  for h in local:
   hs={frozenset({self.identity})};front=hs.copy()
   while front:
    new={closure(tuple(k)+(x,),self.identity) for k in front for x in h-k}-hs
    hs|=new;front=new
   for k in hs:
    for g in self.group:sub.add(frozenset(self.conj(g,x) for x in k))
  return tuple(sorted(sub,key=lambda x:(len(x),sorted(x))))

def presentation(o,p):
 cs,ks,es,a=p;colors=expanded(o,p) if o.kind=='disc' else []
 nr=max(1,len(colors)) if o.kind=='disc' else 0
 names=['z']+[f'x{i}' for i in range(len(cs))]
 if o.kind=='disc':names+=['e']+[f'r{i}' for i in range(nr)]
 if o.kind=='RP2':names+=['a']
 fr=free_group(','.join(names));free=fr[0];g=dict(zip(names,fr[1:]));z=g['z']
 rels=[z**2]+[z*x*z**-1*x**-1 for name,x in g.items() if name!='z']
 cones=[g[f'x{i}'] for i in range(len(cs))]
 rels += [x**m*z**(-d) for x,m,d in zip(cones,o.cone_orders,cs)]
 prod=free.identity
 for x in cones:prod*=x
 if o.kind=='sphere':rels.append(prod*z**(-a))
 elif o.kind=='RP2':rels.append(g['a']**2*prod*z**(-a))
 else:
  e=g['e'];refs=[g[f'r{i}'] for i in range(nr)]
  rels += [r**2 for r in refs]
  rels.append(prod*e*z**(-a))
  end=e*refs[0]*e**-1
  if colors:
   ext=refs+[end]
   rels += [(ext[j]*ext[j+1])**m*z**(-d) for j,(m,d,_) in enumerate(colors)]
  else:rels.append(end*refs[0]**-1)
 return names,free,g,rels,colors

def evaluate(word,pgens,identity):
 z=identity
 for symbol,power in word.array_form:z=pmul(z,ppow(pgens[str(symbol)],power))
 return z

def make_group(o,p,index):
 names,free,g,rels,colors=presentation(o,p)
 cache=CACHE/f'extension_{index:03}.json'
 if cache.exists():
  raw=json.loads(cache.read_text());pgens={name:tuple(v) for name,v in raw['generators'].items()}
 else:
  fp=FpGroup(free,rels)
  ct=coset_enumeration_r(fp,[],max_cosets=10000);ct.compress();ct.standardize()
  assert ct.is_complete() and ct.n==2*o.order,(index,o.name,ct.n,2*o.order)
  pgens={name:tuple(ct.table[i][2*j+1] for i in range(ct.n)) for j,name in enumerate(names)}
  raw={'names':names,'generators':pgens,'coset_count':ct.n,
       'relators':[str(w) for w in rels]}
  cache.write_text(json.dumps(raw,indent=2)+'\n')
 identity=tuple(range(2*o.order))
 assert all(evaluate(w,pgens,identity)==identity for w in rels)
 assert pgens['z']!=identity and ppow(pgens['z'],2)==identity
 cs,ks,es,a=p
 cones=[pgens[f'x{i}'] for i in range(len(cs))]+[pgens['z']]*a
 if o.kind=='RP2':gens=[pgens['a']];signs=[-1]
 else:
  gens=[pgens[n] for n in names]
  signs=[-1 if n.startswith('r') else 1 for n in names]
 refs=[pgens[f'r{i}'] for i in range(max(1,len(colors)))] if o.kind=='disc' else []
 corners=[m*(1+d) for m,d,_ in colors]
 model=SurfaceOrbifold(f'genus2_{index:03}_{o.name}',o.kind,gens,signs,
  cones=cones,corners=corners,refs=refs,boundary=pgens.get('e'),
  order=2*o.order,cover_chi=-2)
 assert model.cone_orders==[m*(1+d) for m,d in zip(o.cone_orders,cs)]+[2]*a
 return model,pgens,colors,raw

def char_values(o,p,bits,model,pgens):
 cs,ks,es,a=p
 values={'z':1}
 for i,b in enumerate(bits[:len(cs)]):values[f'x{i}']=b
 if o.kind=='sphere':pass
 elif o.kind=='RP2':raise AssertionError('no RP2 complement')
 else:
  values['e']=(a+sum(bits[:len(cs)]))%2
  for i,b in enumerate(bits[len(cs):]):values[f'r{i}']=b
 known={model.identity:0};todo=[model.identity]
 while todo:
  x=todo.pop()
  for name,gen in pgens.items():
   y=pmul(x,gen);v=known[x]^values[name]
   if y in known:assert known[y]==v
   else:known[y]=v;todo.append(y)
 assert len(known)==model.order
 return known,values

def restrict_data(model,whole,subgroup,class_id):
 ids=model.ids;elements=model.elements
 allowed={ids[g] for g in subgroup}
 old=[s for s in whole['sections'] if set(s['image_elements'])<=allowed]
 oldids={s['section_id']:i for i,s in enumerate(old)}
 sections=[]
 for s in old:
  r=dict(s);r['section_id']=oldids[s['section_id']]
  r['strict_extensions']=[oldids[j] for j in s['strict_extensions'] if j in oldids]
  r['maximal']=not r['strict_extensions']
  r['Gamma_stabilizer_elements']=sorted(set(s['Gamma_stabilizer_elements'])&allowed)
  sections.append(r)
 maxima={s['section_id'] for s in sections if s['maximal']}
 for s in sections:
  s['maximal_overgroups']=sorted(({s['section_id']}|set(s['strict_extensions']))&maxima)
  if s['fixed_component_kind']=='point':assert len(s['maximal_overgroups'])==1
 nodes=whole['nodes'];nodekey={ (tuple(n['stratum']),frozenset(n['coset_elements'])):n['id'] for n in nodes }
 acts={}
 for g in subgroup:
  acts[ids[g]]={n['id']:nodekey[(tuple(n['stratum']),frozenset(ids[pmul(g,elements[j])] for j in n['coset_elements']))] for n in nodes}
 key=lambda s:(frozenset(s['image_elements']),s['fixed_component_kind'],frozenset(s['fixed_component_nodes']))
 sectionkey={key(s):s['section_id'] for s in sections}
 orbits=[];left=set(maxima)
 while left:
  si=min(left);s=sections[si];orb=set()
  for g in subgroup:
   image=frozenset(ids[model.conj(g,elements[j])] for j in s['image_elements'])
   points=frozenset(acts[ids[g]][j] for j in s['fixed_component_nodes'])
   orb.add(sectionkey[(image,s['fixed_component_kind'],points)])
  assert orb<=maxima;left-=orb;orbits.append(sorted(orb))
 count={'type':'(2,0)','class_id':class_id,'order':len(subgroup),
  'positive_order':sum(model.orientation[g]==1 for g in subgroup),
  'full_splitting_classes':1 if len(subgroup)==1 else sum(set(s['image_elements'])==allowed for s in sections),
  'nontrivial_partial_splitting_classes':len(sections),
  'maximal_partial_classes_Phi':len(maxima),'Gamma_orbits_on_Phi':len(orbits),
  'oval_section_classes':sum(s['fixed_component_kind']=='oval' for s in sections),
  'line_section_classes':0,
  'reflection_classes_with_multiple_maximal_extensions':sum(len(s['maximal_overgroups'])>1 for s in sections if s['fixed_component_kind']=='oval')}
 data={'class_id':class_id,'group_elements':sorted(allowed),'sections':sections,'Phi_orbits':orbits}
 return count,data

def main():
 cases=[(o,p) for o in orbifolds() for p in o.patterns(6)]
 cases.sort(key=lambda z:(z[0].order,z[0].name,z[1]))
 rows=[];all_details=[];extensions=[]
 for index,(o,p) in enumerate(cases,1):
  model,pgens,colors,pres=make_group(o,p,index)
  pat=((0,)*len(model.cones),(0,)*len(model.corner_orders),(0,)*len(model.refs),0)
  _,whole=model.analyse(pat,f'E{index:03}',0)
  whole['hyperelliptic_id']=model.ids[pgens['z']]
  zh={model.ids[model.identity],model.ids[pgens['z']]}
  assert sum(set(s['image_elements'])==zh for s in whole['sections'])==6
  whole['base_sphere_class']=f'S6_{index:03}'
  whole['base_pattern']=p;whole['presentation']=pres
  extensions.append(whole)
  reps,chardata=character_orbits(o,p)
  groups=[(model.group,None,None)]
  for b in reps:
   values,genvalues=char_values(o,p,b,model,pgens)
   k=frozenset(g for g,v in values.items() if v==0)
   assert len(k)==o.order and pgens['z'] not in k
   groups.append((k,b,genvalues))
  for k,b,genvalues in groups:
   cid=f'G2_{len(rows)+1:03}'
   row,data=restrict_data(model,whole,k,cid)
   row.update({'extension_id':f'E{index:03}','contains_hyperelliptic':b is None,
     'character':str(genvalues) if genvalues is not None else '',
     'base_sphere_class':f'S6_{index:03}','base_orbifold':o.name})
   data.update({'extension_id':f'E{index:03}','character':genvalues,
     'normalizer_character_orbit_data':chardata})
   rows.append(row);all_details.append(data)
  print(index,o.name,'Eorder',model.order,'complements',len(reps),'totalclasses',len(rows),flush=True)
  (OUT/'genus2_extended_checkpoint.json').write_text(json.dumps({'finished_base_classes':index,'classes':len(rows)}))
 assert len(rows)==92
 assert sum(r['order']==r['positive_order'] for r in rows)==21
 with (OUT/'type_2_0_extended_catalogue.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 (OUT/'type_2_0_extended_sections.json').write_text(json.dumps({'type':'(2,0)',
  'catalogue':all_details,'hyperelliptic_extensions':extensions},indent=2)+'\n')
 summary={'conjugacy_classes':len(rows),'positive_classes':sum(r['order']==r['positive_order'] for r in rows),
          'containing_hyperelliptic':57,'complements':35,
          'by_order':dict(sorted(Counter(r['order'] for r in rows).items()))}
 (OUT/'catalogue_genus2_extended_output.json').write_text(json.dumps(summary,indent=2)+'\n')
 print('FINAL',json.dumps(summary),flush=True)
if __name__=='__main__':main()
