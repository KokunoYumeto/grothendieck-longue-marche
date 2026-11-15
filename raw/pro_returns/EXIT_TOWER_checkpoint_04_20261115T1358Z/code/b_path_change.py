"""Executed S5-equivariant path-change certificate for the 542-object model.
Changes only the 120 free f_Qa arrows by inserting the full q=0 meridian
in the same four-point-cover family. Endpoint germs and every listed
fractional-twist arrow remain fixed. This is a comparison of specified
path data; no unrecorded marked-gommage identity is assumed.
"""
from pathlib import Path
import json,itertools
P=Path(__file__).resolve().parent
X={'__file__':str(P/'b_third_tier.py')}
exec((P/'b_third_tier.py').read_text().split('\nvertices={')[0],X)
S,r,I,eps=[X[k] for k in ('S','r','I','eps')]
Q,Z,zero,one=[X[k] for k in ('Q','Z','zero','one')]
red,inv,comb,expand,aux=[X[k] for k in ('red','inv','comb','expand','aux')]
D=X['D'];G=X['G'];C=X['C'];T=X['T']
full=json.loads((P/'b_third_tier.json').read_text());arrows=full['arrows'];tree=set(full['tree_edges']);paths={int(k):tuple(v) for k,v in full['tree_paths'].items()}
base=X['base'];vertices={int(v):tuple(Z(S.sympify(z)) for z in zs) for v,zs in T['vertices'].items()}
parts=[];certs=[]
for u,v in zip((1,I,-1,-I),(I,-1,-I,1)):
 q=eps*((1-r)*u+r*v)
 hom=((S.Integer(1),S.Integer(0)),(-I*q,S.Integer(1)),(I*q,S.Integer(1)),(-S.Integer(1),S.Integer(1)),(S.Integer(1),S.Integer(1)))
 poly,cert=X['universal_polygon'](hom);parts.append(poly);certs.append(cert)
print('Universal q=0 square-loop certificate intervals:',[len(x) for x in certs],flush=True)
loops={}
for j,e in enumerate(D['arrows']):
 perm=tuple(e['representative']);poly=[]
 for part in parts:
  p=[X['normalized_homogeneous'](z,perm) for z in part]
  if poly:assert poly[-1]==p[0];poly.extend(p[1:])
  else:poly.extend(p)
 v=122+j;assert poly[0]==poly[-1]==vertices[v]
 for den in (37,41,43,47,53,59,61,67,71,73,79,83):
  eta=Q(S.Rational(1,den));bridge=X['braid_polygon'](X['bridge'](vertices[v],base),eta);raw=X['braid_polygon'](poly,eta)
  if bridge is not None and raw is not None:break
 else:raise AssertionError('projection list exhausted')
 w=red(bridge+raw+inv(bridge));assert aux['permutation'](4,w)==(1,2,3,4) and aux['link12'](4,w)==0
 nf=comb(4,w);assert aux['eq'](4,w,expand(nf))
 homology=[sum(e for i,j,e in nf if (i,j)==pair) for pair in ((1,3),(2,3),(1,4),(2,4),(3,4))]
 assert any(homology)
 loops[v]=dict(braid=w,pure=nf,homology=homology,projection_denominator=den)
print('All60 source meridians computed; every image has nonzero H1.',flush=True)
def edge_expand(w,images=None):
 images=images or [tuple(a['braid']) for a in arrows]
 return red(x for a in w for x in (images[a-1] if a>0 else inv(images[-a-1])))
core_basis=[tuple(l['edge_word']) for l in C['loops']];std=[tuple(w) for w in G['standard_words_in_11_loops']]
lookup={(1,3):1,(2,3):2,(1,4):3,(2,4):4,(3,4):5}
def coreword(braid):
 nf=comb(4,braid);w=tuple(lookup[i,j]*e for i,j,e in nf)
 result=red(aux['subst'](red(aux['subst'](w,std)),core_basis))
 assert aux['eq'](4,edge_expand(result),braid)
 return result
maps={};inverse={};changed=[];newimages=[tuple(a['braid']) for a in arrows]
for i,e in enumerate(arrows):
 if e['name']!='f_Qa':continue
 assert i not in tree
 s=e['source'];ts=paths[s];loop=tuple(loops[s]['braid']);bt=edge_expand(ts)
 delta=red(bt+loop+inv(bt));kappa=coreword(delta)
 correction=red(inv(ts)+kappa+ts)
 assert all(abs(k)-1 in tree or abs(k)<=60 for k in correction)
 maps[i+1]=red(correction+(i+1,));inverse[i+1]=red(inv(correction)+(i+1,))
 newimages[i]=red(loop+tuple(e['braid']))
 assert aux['eq'](4,edge_expand(maps[i+1]),newimages[i])
 changed.append(dict(edge=i+1,source=s,target=e['target'],delta_core_word=kappa,correction=correction,forward=maps[i+1],inverse=inverse[i+1],new_braid=newimages[i]))
assert len(changed)==120

def substitute(word,table):
 return red(x for e in word for x in (table.get(e,(e,)) if e>0 else inv(table.get(-e,(-e,)))))
for i in range(1,len(arrows)+1):
 assert substitute(maps.get(i,(i,)),inverse)==(i,)
 assert substitute(inverse.get(i,(i,)),maps)==(i,)
newrels=[]
for rel in full['relators']:
 w=substitute(tuple(rel),inverse);assert substitute(w,maps)==red(rel);newrels.append(w)
assert len(newrels)==1080
print('120 forward/inverse Nielsen arrow changes verified; all1620 generators invert exactly.',flush=True)
print('All1080 kernel relators transported and checked by exact inverse substitution.',flush=True)
out=dict(scope=__doc__,counts=full['counts'],fixed_core_edges=60,fixed_tree_edges=len(tree),changed_arrow_count=len(changed),universal_certificates=certs,source_meridians=loops,changes=changed,transported_relators=newrels,relator_count=1080)
(P/'b_path_change.json').write_text(json.dumps(out,indent=2)+'\n')
