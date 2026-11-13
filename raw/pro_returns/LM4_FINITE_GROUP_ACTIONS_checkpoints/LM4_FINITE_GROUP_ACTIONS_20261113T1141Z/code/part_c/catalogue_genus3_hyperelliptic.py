#!/usr/bin/env python3
"""Finite genus-three actions containing a hyperelliptic involution.
Hyperelliptic lift presentations from the complete decorated sphere8 list;
finite groups are certified by regular coset actions of exactly twice the
quotient order. Only full inverse images are retained; the central hyperelliptic involution is
unique inside each finite group, so forgetting it creates no further fusion.
"""
from pathlib import Path
from collections import defaultdict,Counter,deque
from functools import lru_cache
from itertools import product
from fractions import Fraction
import json,csv
from sympy.combinatorics.free_groups import free_group
from sympy.combinatorics.fp_groups import FpGroup, coset_enumeration_r
import sys
_here=Path(__file__).resolve().parent
_bdir=_here.parent/'part_b'
if not (_bdir/'catalogue_spheres.py').exists():_bdir=_here.parents[1]/'part_b'/'code'
sys.path.insert(0,str(_bdir))
from catalogue_spheres import Orbifold,orbifolds,pmul,pinv,ppow,closure
from genus2_characters import expanded

OUT=Path(__file__).resolve().parent
CACHE=OUT/'genus3_hyperelliptic_extension_cache';CACHE.mkdir(exist_ok=True)

class SurfaceOrbifold(Orbifold):
 def __init__(self,name,kind,gens,signs,cones=(),corners=(),refs=(),boundary=None,order=None,cover_chi=-4,crosscap=None):
  if kind!='RP2':
   super().__init__(name,kind,gens,signs,cones,corners,refs,boundary,order,cover_chi)
   return
  self.name=name;self.kind=kind;self.identity=tuple(range(len(gens[0])))
  self.gens=tuple(gens);self.group=closure(gens,self.identity);self.order=order
  assert len(self.group)==order
  self.elements=sorted(self.group);self.ids={g:i for i,g in enumerate(self.elements)}
  self.inv={g:pinv(g) for g in self.group};self.orientation={self.identity:1}
  todo=[self.identity]
  while todo:
   x=todo.pop()
   for g,sg in zip(gens,signs):
    y=pmul(x,g);value=self.orientation[x]*sg
    if y in self.orientation:assert self.orientation[y]==value
    else:self.orientation[y]=value;todo.append(y)
  self.cones=tuple(cones);self.corner_orders=();self.refs=();self.boundary=self.identity
  self.cone_groups=[closure([c],self.identity) for c in cones]
  self.cone_orders=[len(h) for h in self.cone_groups]
  self.corner_rotations=[];self.corner_groups=[]
  assert crosscap is not None and self.orientation[crosscap]==-1
  word=ppow(crosscap,2)
  for c in cones:word=pmul(word,c)
  assert word==self.identity
  assert all(self.orientation[c]==1 for c in cones)
  self.orbifold_chi=Fraction(1)-sum((1-Fraction(1,m) for m in self.cone_orders),Fraction())
  assert order*self.orbifold_chi==cover_chi
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
 gens=[pgens[n] for n in names]
 signs=[-1 if n.startswith('r') or n=='a' else 1 for n in names]
 refs=[pgens[f'r{i}'] for i in range(max(1,len(colors)))] if o.kind=='disc' else []
 corners=[m*(1+d) for m,d,_ in colors]
 model=SurfaceOrbifold(f'genus3_hyperelliptic_{index:03}_{o.name}',o.kind,gens,signs,
  cones=cones,corners=corners,refs=refs,boundary=pgens.get('e'),
  order=2*o.order,cover_chi=-4,crosscap=pgens.get('a'))
 assert model.cone_orders==[m*(1+d) for m,d in zip(o.cone_orders,cs)]+[2]*a
 return model,pgens,colors,raw

def main():
 cases=[(o,p) for o in orbifolds(max_n=8) for p in o.patterns(8)]
 cases.sort(key=lambda z:(z[0].order,z[0].name,z[1]))
 rows=[];details=[]
 for index,(o,p) in enumerate(cases,1):
  model,pgens,colors,pres=make_group(o,p,index)
  pattern=((0,)*len(model.cones),(0,)*len(model.corner_orders),(0,)*len(model.refs),0)
  row,data=model.analyse(pattern,f'G3H_{index:03}',0)
  row['type']='(3,0)';row['base_sphere_class']=f'S8_{index:03}'
  row['base_orbifold']=o.name;row['contains_hyperelliptic']=True
  row['base_branch_pattern']=str(p)
  hid=model.ids[pgens['z']];identityid=model.ids[model.identity]
  assert sum(set(s['image_elements'])=={identityid,hid} for s in data['sections'])==8
  data.update({'type':'(3,0)','hyperelliptic_id':hid,'base_sphere_class':f'S8_{index:03}',
   'base_branch_pattern':p,'presentation':pres,'scope':'contains a hyperelliptic involution'})
  rows.append(row);details.append(data)
  print(index,o.name,'grouporder',model.order,'partialsections',len(data['sections']),flush=True)
  (OUT/'genus3_hyperelliptic_checkpoint.json').write_text(json.dumps({'completed':index,'total':len(cases)}))
 assert len(rows)==79
 assert sum(r['order']==r['positive_order'] for r in rows)==18
 mixed=[r for r in rows if r['order']!=r['positive_order']]
 assert len(mixed)==61
 for filename,records in [('type_3_0_hyperelliptic_catalogue.csv',rows),('type_3_0_hyperelliptic_mixed_catalogue.csv',mixed)]:
  with (OUT/filename).open('w',newline='') as f:
   w=csv.DictWriter(f,fieldnames=list(records[0]));w.writeheader();w.writerows(records)
 (OUT/'type_3_0_hyperelliptic_sections.json').write_text(json.dumps(details,indent=2)+'\n')
 summary={'scope':'all finite actions containing a hyperelliptic involution',
  'classes':79,'positive_classes':18,'mixed_classes':61,
  'mixed_by_order':dict(sorted(Counter(r['order'] for r in mixed).items())),
  'mixed_by_Phi_orbits':dict(sorted(Counter(r['Gamma_orbits_on_Phi'] for r in mixed).items()))}
 (OUT/'catalogue_genus3_hyperelliptic_output.json').write_text(json.dumps(summary,indent=2)+'\n')
 print('FINAL',json.dumps(summary),flush=True)
if __name__=='__main__':main()
