#!/usr/bin/env python3
"""Complete finite mapping-class subgroup catalogues in the four exceptional types,
with every injective realized lift and its extension-dependent section data.
Sphere antipodal comparison failure is recorded rather than suppressed.
"""
from pathlib import Path
from fractions import Fraction
from collections import Counter
from itertools import product
import json,csv
from catalogue_tori import Action,ID,I,closure,affine_classes,det,N as TORUS_N
OUT=Path(__file__).resolve().parent

N=8
AID=(1,1,0)
def amul(g,h):return (g[0]*h[0],g[1]*h[1],(g[2]+g[0]*h[2])%N)
def ainv(g):return (g[0],g[1],(-g[0]*g[2])%N)
def aconj(g,h):return amul(amul(g,h),ainv(g))
def aact(g,p):return ((g[0]*p[0]+g[2])%N,g[1]*p[1])
def asubgroups(g):
 hs={frozenset({AID})};front=hs.copy()
 while front:
  new={closure(set(h)|{x},amul,AID) for h in front for x in g-h}-hs
  hs|=new;front=new
 return hs
AGRID=frozenset(product(range(N),(-1,0,1)))
def afixed(h):
 if len(h)==1:return [('surface',AGRID)]
 pts=frozenset(p for p in AGRID if all(aact(g,p)==p for g in h))
 if not pts:return []
 if any(g[0]*g[1]==1 and g!=AID for g in h):return [('point',frozenset({p})) for p in sorted(pts)]
 assert len(h)==2
 g=next(g for g in h if g!=AID)
 if g[0]==1:return [('oval',pts)]
 return [('line',frozenset(p for p in pts if p[0]==x)) for x in sorted({p[0] for p in pts})]

def annulus(g,name,mcclass):
 elems=sorted(g);ids={x:i for i,x in enumerate(elems)}
 sections=[(h,kind,pts) for h in asubgroups(g) if len(h)>1 for kind,pts in afixed(h)]
 sections.sort(key=lambda c:(len(c[0]),sorted(c[0]),c[1],sorted(c[2])))
 index={c:i for i,c in enumerate(sections)}
 incl=lambda c,d:c[0]<d[0] and d[2]<=c[2]
 maxima=[c for c in sections if not any(incl(c,d) for d in sections)]
 def actsec(x,c):return(frozenset(aconj(x,y) for y in c[0]),c[1],frozenset(aact(x,p) for p in c[2]))
 left=set(maxima);orbs=[]
 while left:
  c=next(iter(left));orb={actsec(x,c) for x in g};assert orb<=set(maxima)
  left-=orb;orbs.append(sorted(index[d] for d in orb))
 records=[]
 for c in sections:
  h,kind,pts=c
  records.append({'section_id':index[c],'image_elements':[ids[x] for x in sorted(h)],
   'kind':kind,'fixed_component_samples':sorted(pts),'centralizer_in_pi':'Z' if kind=='oval' else '1',
   'mu':{ids[x]:'0' if x==AID else '1/2' for x in h},
   'maximal':c in maxima,'strict_extensions':[index[d] for d in sections if incl(c,d)],
   'maximal_overgroups':[index[d] for d in maxima if c==d or incl(c,d)],
   'Gamma_stabilizer':[ids[x] for x in g if actsec(x,c)==c]})
 cocycle=[[ (x[2]+x[0]*y[2]-amul(x,y)[2])//N for y in elems] for x in elems]
 assert all((x[2]+x[0]*y[2]-amul(x,y)[2])%N==0 for x in elems for y in elems)
 for x in elems:
  for y in elems:
   for z in elems:
    c=lambda a,b:cocycle[ids[a]][ids[b]]
    assert c(x,y)+c(amul(x,y),z)==x[0]*c(y,z)+c(x,amul(y,z))
 row={'type':'(0,2)','mapping_class_subgroup':mcclass,'action_class':name,'order':len(g),
  'positive_order':sum(e*h==1 for e,h,a in g),'full_splitting_classes':len(afixed(g)),
  'nontrivial_partial_splitting_classes':len(sections),'Phi':len(maxima),'Phi_orbits':len(orbs),
  'actual_fixed_components':len(afixed(g)),'note':'Extension cocycle retained; pi=Z.'}
 data={'action_class':name,'elements':[{'id':ids[x],'epsilon':x[0],'eta':x[1],'angle_numerator':x[2],'angle_denominator':N} for x in elems],
  'multiplication':[[ids[amul(x,y)] for y in elems] for x in elems],
  'extension_cocycle':cocycle,'extension_law':'(n,g)(m,h)=(n+epsilon_g*m+c(g,h),gh)',
  'sections':records,'Phi_orbits':orbs,'trivial_section_centralizer':'Z',
  'puncture_ends':[{'end':i,'stabilizer_elements':[ids[x] for x in elems if x[1]==1],
   'local_mu':{ids[x]:'0' if x==AID else '1/2' for x in elems if x[1]==1}} for i in (0,1)]}
 return row,data

def simply_connected(kind,action,negative,actual_fixed,fixed_kind):
 name=f'{kind}_{action}';order=2 if negative else 1
 row={'type':'(0,0)' if kind=='sphere' else '(0,1)',
  'mapping_class_subgroup':'C2_negative' if negative else 'trivial',
  'action_class':name,'order':order,'positive_order':1,
  'full_splitting_classes':1,'nontrivial_partial_splitting_classes':int(negative),
  'Phi':int(negative),'Phi_orbits':int(negative),'actual_fixed_components':actual_fixed,
  'note':'Antipodal: algebraic full section has no geometric fixed-point component.' if action=='antipodal' else 'pi=1; the lift extension is Gamma itself.'}
 section=[]
 if negative:
  section=[{'section_id':0,'image_elements':[0,1],'kind':'algebraic section',
   'geometric_fixed_component_kind':fixed_kind,'centralizer_in_pi':'1','maximal':True,
   'strict_extensions':[],'maximal_overgroups':[0],'Gamma_stabilizer':[0,1],
   'local_multiplier':None if action=='antipodal' else {'0':'0','1':'1/2'},
   'orientation_half_convention':{'0':'0','1':'1/2'}}]
 data={'action_class':name,'group':'C2' if negative else '1','pi':'1','extension':'E=Gamma',
  'sections':section,'Phi_orbits':[[0]] if negative else [],
  'geometric_model':{'sphere_reflection':'(x,y,z)->(x,y,-z)',
   'sphere_antipodal':'(x,y,z)->(-x,-y,-z)',
   'plane_reflection':'(x,y)->(x,-y)'}.get(name,'identity'),
  'trivial_section_centralizer':'1',
  'punctures':[{'point':'infinity','stabilizer_elements':list(range(order)),'local_mu':{'0':'0','1':'1/2'} if negative else {'0':'0'}}] if kind=='plane' else []}
 return row,data

def main():
 rows=[];details=[]
 # Exact antipodal counterexample: A=-I3 has A^2=I3, det(A)=-1,
 # and det(I3-A)=8, so no nonzero vector is fixed.
 matrix=tuple(tuple(-int(i==j) for j in range(3)) for i in range(3))
 identity=tuple(tuple(int(i==j) for j in range(3)) for i in range(3))
 square=tuple(tuple(sum(matrix[i][k]*matrix[k][j] for k in range(3)) for j in range(3)) for i in range(3))
 det3=lambda a:sum((1 if p in ((0,1,2),(1,2,0),(2,0,1)) else -1)*a[0][p[0]]*a[1][p[1]]*a[2][p[2]] for p in __import__('itertools').permutations(range(3)))
 difference=tuple(tuple(identity[i][j]-matrix[i][j] for j in range(3)) for i in range(3))
 antipodal={'A_squared_identity':square==identity,'determinant':det3(matrix),'det_I_minus_A':det3(difference)}
 assert antipodal=={'A_squared_identity':True,'determinant':-1,'det_I_minus_A':8}
 for arg in [('sphere','identity',False,1,'sphere'),('sphere','reflection',True,1,'circle'),
             ('sphere','antipodal',True,0,None),('plane','identity',False,1,'plane'),
             ('plane','reflection',True,1,'line')]:
  r,d=simply_connected(*arg);rows.append(r);details.append(d)
 a=(-1,1,0);b=(1,-1,0);bg=(1,-1,N//2);c=(-1,-1,0)
 cases=[([], 'identity','trivial'),([a],'angular_reflection','C2_angular'),
  ([b],'radial_reflection','C2_radial'),([bg],'radial_glide','C2_radial'),
  ([c],'positive_halfturn','C2_positive'),([a,b],'V4_split','V4'),([a,bg],'V4_glide','V4')]
 for gens,name,mc in cases:
  g=closure(gens,amul,AID);r,d=annulus(g,name,mc);rows.append(r);details.append(d)
 affine,stats=affine_classes();torus=[]
 for hi,g in affine:
  t=frozenset(x[1] for x in g if x[0]==I)
  if len(t)!=1:continue
  model=Action(hi,g);s=model.section_table(frozenset())
  name=f'torus_{len(torus)+1:02}'
  row={'type':'(1,0)','mapping_class_subgroup':f'GL2Z_{hi:02}',
   'action_class':name,'order':len(g),'positive_order':sum(det(a)==1 for a,t in g),
   'full_splitting_classes':s['full'],'nontrivial_partial_splitting_classes':s['partial'],
   'Phi':s['phi'],'Phi_orbits':s['phi_orbits'],'actual_fixed_components':s['full'],
   'note':'Exact affine extension with faithful linear part; pi=Z^2.'}
  data=model.data();data.update({'action_class':name,'pi':'Z^2','coordinate_denominator':TORUS_N,'sections':s['records'],
    'Phi_orbits':s['orbits'],'trivial_section_centralizer':'Z^2'})
  torus.append(row);rows.append(row);details.append(data)
  print(name,'linear',hi,'full',s['full'],'partial',s['partial'],flush=True)
 assert len(torus)==17 and len({r['mapping_class_subgroup'] for r in torus})==13
 expected={'(0,0)':(2,3),'(0,1)':(2,2),'(0,2)':(5,7),'(1,0)':(13,17)}
 summary={}
 for typ,(mc,ac) in expected.items():
  rs=[r for r in rows if r['type']==typ]
  assert len(rs)==ac and len({r['mapping_class_subgroup'] for r in rs})==mc
  summary[typ]={'finite_mapping_class_subgroup_classes':mc,'injectively_realized_action_classes':ac}
 with (OUT/'exceptional_finite_subgroups_and_lifts.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 (OUT/'exceptional_sections.json').write_text(json.dumps({'catalogue':details,'antipodal_matrix_check':antipodal},indent=2)+'\n')
 (OUT/'catalogue_exceptional_output.json').write_text(json.dumps(summary,indent=2)+'\n')
 print('FINAL',json.dumps(summary),flush=True)
if __name__=='__main__':main()
