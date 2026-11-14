#!/usr/bin/env python3
"""Finite genus-two actions with one or two punctures, including reflections.
Decorate intrinsic K-fixed strata of each closed action from B.28, and divide
by the exact hyperelliptic normalizer permutations proved in B.29.
"""
from collections import defaultdict,Counter,deque
from itertools import product,permutations
from pathlib import Path
from fractions import Fraction
import csv,json
from catalogue_spheres import orbifolds,pmul,pinv,ppow
from catalogue_genus2_extended import make_group,char_values
from genus2_characters import expanded,character_orbits
from catalogue_tori import permutation_closure
OUT=Path(__file__).resolve().parent

class Decorated:
 def __init__(self,o,p,model,whole,k,values,bits,pgens):
  self.o,self.p,self.m,self.w,self.k=o,p,model,whole,k
  self.values,self.bits,self.pgens=values,bits,pgens
  self.ids=model.ids;self.elements=model.elements
  self.kids={self.ids[g] for g in k}
  self.z=pgens['z'];self.full=values is None
  old=whole['nodes'];self.old=old;self.oldbyid={n['id']:n for n in old}
  key={(tuple(n['stratum']),frozenset(n['coset_elements'])):n['id'] for n in old}
  self.acts={}
  for g in model.group:
   self.acts[g]={n['id']:key[(tuple(n['stratum']),frozenset(self.ids[pmul(g,self.elements[j])] for j in n['coset_elements']))] for n in old}
  self.stabs={n['id']:frozenset(self.elements[i] for i in n['stabilizer_elements']) for n in old}
  self.graph={};self.edges=[]
  # One midpoint in every edge permits removal of any two old sample points
  # without losing the interval between adjacent punctures.
  for j,(a,b) in enumerate(whole['mirror_graph_edges'],len(old)):
   self.edges.append((a,b,j));self.graph.setdefault(a,set()).add(j);self.graph.setdefault(b,set()).add(j)
   self.graph[j]={a,b};self.stabs[j]=self.stabs[a]&self.stabs[b]
  emap={frozenset((a,b)):j for a,b,j in self.edges}
  for g in model.group:
   for a,b,j in self.edges:
    aa,bb=self.acts[g][a],self.acts[g][b]
    self.acts[g][j]=emap[frozenset((aa,bb))]
    if self.acts[g][j]==j:assert (aa,bb)==(a,b)
  self.critical=frozenset(n['id'] for n in old if any(g!=model.identity and model.orientation[g]==1 for g in self.stabs[n['id']]&k))
  left=set(self.critical);self.vorbs=[]
  while left:
   x=min(left);orb=frozenset(self.acts[g][x] for g in k);left-=orb;self.vorbs.append(orb)
  self.vorbs.sort(key=lambda x:sorted(x))
  self.reflections=[g for g in k if model.orientation[g]==-1 and model.elem_order(g)==2]
  self.ref_comps={};mirrors=[]
  for r in self.reflections:
   fixed={n for n in self.graph if self.acts[r][n]==n}
   assert all(len(self.graph[n]&fixed)==2 for n in fixed)
   comps=self.components(fixed,self.critical)
   self.ref_comps[r]=self.components(fixed,frozenset())
   mirrors.extend(c for kind,c in comps)
  assert len(mirrors)==len(set(mirrors))
  left=set(mirrors);self.morbs=[]
  while left:
   c=min(left,key=lambda x:sorted(x));orb=frozenset(frozenset(self.acts[g][x] for x in c) for g in k)
   assert orb<=set(mirrors);left-=orb;self.morbs.append(orb)
  self.morbs.sort(key=lambda x:sorted(sorted(c) for c in x))
  self.strata=[('vertex',v) for v in self.vorbs]+[('mirror',frozenset().union(*cs)) for cs in self.morbs]
  self.node_stratum={n:i for i,(kind,s) in enumerate(self.strata) for n in s}
  self.desc_to_stratum={};self.stratum_desc={}
  for n in old:
   idx=n['id'];tag=tuple(n['stratum'])
   if idx not in self.node_stratum:continue
   kind,j=tag[:2]
   if kind not in ('cone','corner','edge'):continue
   if kind=='edge' and tag[2]!='segment':continue
   loc=self.stabs[idx]
   sheet=None
   if not self.full and all(values[g]==0 for g in loc):
    sheet=values[self.elements[min(n['coset_elements'])]]
   d=(kind,j,sheet)
   si=self.node_stratum[idx]
   if d in self.desc_to_stratum:assert self.desc_to_stratum[d]==si
   self.desc_to_stratum[d]=si
   self.stratum_desc.setdefault(si,d)
  assert len(self.stratum_desc)==len(self.strata)
  self.weights=[len(v) for v in self.vorbs]+[len(k)//2 for _ in self.morbs]
  self.perms=self.normalizers()
 def components(self,fixed,deleted):
  left=set(fixed)-set(deleted);out=[]
  while left:
   x=min(left);seen=set();todo=[x]
   while todo:
    y=todo.pop()
    if y in seen:continue
    seen.add(y);todo.extend((self.graph[y]&fixed)-set(deleted)-seen)
   left-=seen
   kind='line' if any(self.graph[y]&fixed&set(deleted) for y in seen) else 'oval'
   out.append((kind,frozenset(seen)))
  return out
 def perm_from_descriptors(self,fn):
  ans=[]
  for i in range(len(self.strata)):
   d=self.stratum_desc[i];dd=fn(d)
   assert dd in self.desc_to_stratum,(self.o.name,self.p,self.bits,d,dd,self.desc_to_stratum)
   ans.append(self.desc_to_stratum[dd])
  assert sorted(ans)==list(range(len(ans)))
  return tuple(ans)
 def normalizers(self):
  n=len(self.strata);gens={tuple(range(n))}
  # Deck involution and, equivalently, every nontrivial coset of K in E.
  gens.add(tuple(self.node_stratum[self.acts[self.z][min(s)]] for kind,s in self.strata))
  cs,ks,es,a=self.p
  colors=[('old_cone',m,d) for m,d in zip(self.o.cone_orders,cs)]+[('regular_branch',1,1)]*a
  if not self.full:
   colors=[color+(self.values[x],) for color,x in zip(colors,self.m.cones)]
  for j in range(len(colors)):
   for l in range(j):
    if colors[j]!=colors[l]:continue
    def fn(d,j=j,l=l):
     kind,i,b=d
     return (kind,l if i==j else j if i==l else i,b) if kind=='cone' else d
    gens.add(self.perm_from_descriptors(fn))
  if not self.full:
   for j,x in enumerate(self.m.cones):
    if self.values[x] or ('cone',j,0) not in self.desc_to_stratum:continue
    if self.o.kind=='sphere' or (self.o.kind=='disc' and a>0):
     def fn(d,j=j):
      kind,i,b=d
      return (kind,i,1-b) if kind=='cone' and i==j and b is not None else d
     gens.add(self.perm_from_descriptors(fn))
  if self.o.kind=='disc':
   co=expanded(self.o,self.p);L=len(co)
   ebit=0 if self.full else self.values[self.pgens['e']]
   rbits=None if self.full else [self.values[self.pgens[f'r{i}']] for i in range(max(1,L))]
   if L:
    for sign in (1,-1):
     for s in range(L):
      cp=[(s+j)%L if sign==1 else (s-j-1)%L for j in range(L)]
      if any(co[j]!=co[cp[j]] for j in range(L)):continue
      if rbits is not None and any(rbits[j]!=rbits[(s+sign*j)%L] for j in range(L)):continue
      def fn(d,s=s,sign=sign):
       kind,j,b=d
       if kind=='cone':return d
       k=s+j if sign==1 else s-j-(1 if kind=='corner' else 0)
       q,jj=divmod(k,L)
       return kind,jj,None if b is None else b^(q*ebit%2)
      gens.add(self.perm_from_descriptors(fn))
  return permutation_closure(gens,n)
 def patterns(self,nu):
  limits=[1]*len(self.vorbs)+[nu//(len(self.k)//2) for _ in self.morbs]
  out=set()
  for v in product(*(range(l+1) for l in limits)):
   rem=nu-sum(x*w for x,w in zip(v,self.weights))
   if rem<0 or rem%len(self.k):continue
   a=rem//len(self.k)
   out.add(min(tuple(v[p[i]] for i in range(len(v))) for p in self.perms)+(a,))
  return sorted(out)
 def realize(self,pat):
  nv=len(self.vorbs);removed=set()
  for b,v in zip(pat[:nv],self.vorbs):
   if b:removed|=v
  for b,orbs in zip(pat[nv:-1],self.morbs):
   component=min(orbs,key=lambda x:sorted(x));count=0
   for x in sorted(component & set(self.oldbyid)):
    if count==b:break
    if x in removed:continue
    orb={self.acts[g][x] for g in self.k}
    assert len(orb)==len(self.k)//2
    removed|=orb;count+=1
   assert count==b
  assert len(removed)==sum(b*w for b,w in zip(pat[:-1],self.weights))
  return frozenset(removed)
 def puncture_mu(self,p,g):
  if g==self.m.identity:return '0'
  if self.m.orientation[g]==-1:return '1/2'
  for s in self.w['sections']:
   if s['fixed_component_kind']=='point' and p in s['fixed_component_nodes'] and self.ids[g] in s['image_elements']:
    return s['mu_by_element_id'][str(self.ids[g])]
  raise AssertionError(('missing puncture rotation',p,g))
 def sections(self,removed,cid):
  sections=[]
  # Exact positive local sections of E restrict to K.
  for s in self.w['sections']:
   if s['fixed_component_kind']!='point' or not set(s['image_elements'])<=self.kids:continue
   if set(s['fixed_component_nodes'])&removed:continue
   sections.append((frozenset(s['image_elements']),'point',frozenset(s['fixed_component_nodes']),s['mu_by_element_id']))
  for r,closed in self.ref_comps.items():
   for _,c in closed:
    for kind,d in self.components(set(c),removed):
     h=frozenset({self.ids[self.m.identity],self.ids[r]})
     sections.append((h,kind,d,{str(self.ids[self.m.identity]):'0',str(self.ids[r]):'1/2'}))
  sections.sort(key=lambda c:(len(c[0]),sorted(c[0]),c[1],sorted(c[2])))
  key=lambda c:(c[0],c[1],c[2]);index={key(c):i for i,c in enumerate(sections)}
  def incl(c,d):return c[0]<d[0] and d[2]<=c[2]
  maxima={i for i,c in enumerate(sections) if not any(incl(c,d) for d in sections)}
  def actsec(g,c):
   h=frozenset(self.ids[self.m.conj(g,self.elements[j])] for j in c[0])
   nodes=frozenset(self.acts[g][j] for j in c[2])
   return index[(h,c[1],nodes)]
  left=set(maxima);orbs=[]
  while left:
   i=min(left);orb={actsec(g,sections[i]) for g in self.k};assert orb<=maxima
   left-=orb;orbs.append(sorted(orb))
  records=[]
  for i,c in enumerate(sections):
   ext=[j for j,d in enumerate(sections) if incl(c,d)]
   maxover=sorted(({i}|set(ext))&maxima)
   if c[1]=='point':assert len(maxover)==1
   records.append({'section_id':i,'image_elements':sorted(c[0]),'kind':c[1],
    'fixed_component_nodes':sorted(c[2]),'centralizer':'Z' if c[1]=='oval' else '1',
    'mu':c[3],'strict_extensions':ext,'maximal':i in maxima,'maximal_overgroups':maxover,
    'Gamma_stabilizer_elements':sorted(self.ids[g] for g in self.k if actsec(g,c)==i)})
  row={'class_id':cid,'order':len(self.k),'positive_order':sum(self.m.orientation[g]==1 for g in self.k),
   'full_splitting_classes':1 if len(self.k)==1 else sum(c[0]==self.kids for c in sections),
   'nontrivial_partial_splitting_classes':len(sections),'maximal_partial_classes_Phi':len(maxima),
   'Gamma_orbits_on_Phi':len(orbs),'oval_section_classes':sum(c[1]=='oval' for c in sections),
   'line_section_classes':sum(c[1]=='line' for c in sections)}
  data={'class_id':cid,'group_elements':sorted(self.kids),'puncture_nodes':sorted(removed),
   'puncture_stabilizers':[{'node':p,'elements':sorted(self.ids[g] for g in self.k&self.stabs[p]),'local_mu':{self.ids[g]:self.puncture_mu(p,g) for g in self.k&self.stabs[p]}} for p in sorted(removed)],
   'sections':records,'Phi_orbits':orbs}
  return row,data

def main():
 base=json.loads((OUT/'type_2_0_extended_sections.json').read_text())
 wholes=base['hyperelliptic_extensions']
 cases=[(o,p) for o in orbifolds() for p in o.patterns(6)]
 cases.sort(key=lambda z:(z[0].order,z[0].name,z[1]))
 rows={1:[],2:[]};details={1:[],2:[]};closed=0
 for i,((o,p),whole) in enumerate(zip(cases,wholes),1):
  model,pgens,colors,pres=make_group(o,p,i)
  reps,chardata=character_orbits(o,p)
  groups=[(model.group,None,None)]
  for b in reps:
   values,_=char_values(o,p,b,model,pgens)
   groups.append((frozenset(g for g,v in values.items() if not v),values,b))
  for k,values,b in groups:
   closed+=1;d=Decorated(o,p,model,whole,k,values,b,pgens)
   for nu in (1,2):
    for pat in d.patterns(nu):
     cid=f'G2N{nu}_{len(rows[nu])+1:03}';removed=d.realize(pat)
     row,data=d.sections(removed,cid)
     row.update({'type':f'(2,{nu})','closed_class':f'G2_{closed:03}',
      'extension_id':f'E{i:03}','decoration':str(pat),'regular_puncture_orbits':pat[-1]})
     data.update({'closed_class':f'G2_{closed:03}','extension_id':f'E{i:03}',
      'decoration':pat,'stratum_weights':d.weights,
      'strata':[{'kind':kind,'nodes':sorted(s)} for kind,s in d.strata],
      'normalizer_permutations':sorted(d.perms),'regular_puncture_orbits':pat[-1],
      'additional_mirror_midpoints':[{'node':j,'endpoints':[a,b]} for a,b,j in d.edges],
      'regular_puncture_orbit_models':[{'orbit':j,'points_indexed_by_group_elements':sorted(d.kids),'stabilizer_elements':[model.ids[model.identity]],'local_mu':{model.ids[model.identity]:'0'}} for j in range(pat[-1])]})
     rows[nu].append(row);details[nu].append(data)
   print('closed',closed,'E',i,'strata',len(d.strata),'normperms',len(d.perms),
         'totals',{n:len(rows[n]) for n in rows},flush=True)
 for nu in (1,2):
  with (OUT/f'type_2_{nu}_extended_catalogue.csv').open('w',newline='') as f:
   w=csv.DictWriter(f,fieldnames=list(rows[nu][0]));w.writeheader();w.writerows(rows[nu])
  (OUT/f'type_2_{nu}_extended_sections.json').write_text(json.dumps({'type':f'(2,{nu})','catalogue':details[nu]},indent=2)+'\n')
 summary={'counts':{f'(2,{nu})':len(rows[nu]) for nu in rows},
          'positive_counts':{f'(2,{nu})':sum(r['order']==r['positive_order'] for r in rows[nu]) for nu in rows}}
 # Independent primary-source oriented catalogues supplied by the other calculation.
 primary=OUT/'oriented_higher_genus_catalogue_input.csv'
 if not primary.exists():
  common=OUT.parent if (OUT.parent/'root').is_dir() else OUT.parents[1]
  source=common/'root'/'higher_genus_output'/'oriented_higher_genus_catalogue.csv'
  primary.write_bytes(source.read_bytes())
 old=list(csv.DictReader(primary.open()));checks=[]
 for nu in (1,2):
  a=Counter(tuple(int(r[k]) for k in ('order','full_sections','nontrivial_partial_sections','phi_points','phi_orbits'))
      for r in old if r['genus']=='2' and int(r['punctures'])==nu)
  b=Counter(tuple(r[k] for k in ('order','full_splitting_classes','nontrivial_partial_splitting_classes','maximal_partial_classes_Phi','Gamma_orbits_on_Phi'))
      for r in rows[nu] if r['order']==r['positive_order'])
  checks.append({'nu':nu,'matches':a==b,'missing':list((a-b).items()),'extra':list((b-a).items())})
 summary['independent_oriented_checks']=checks
 (OUT/'catalogue_genus2_punctures_output.json').write_text(json.dumps(summary,indent=2)+'\n')
 print('FINAL',json.dumps(summary),flush=True)
 assert all(c['matches'] for c in checks)
if __name__=='__main__':main()
