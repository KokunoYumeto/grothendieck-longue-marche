#!/usr/bin/env python3
"""One exact finite subgroup intersection for the actual contact-block gate."""
from pathlib import Path
import sys,json,hashlib
from collections import deque
ROOT=Path(__file__).resolve().parents[2];DE=ROOT/'work_DE/next_marginal_source';P=ROOT/'work_CE/next_symmetric_nodes'
sys.path.insert(0,str(DE));from weighted_stallings import WeightedFold,reduce_word as red,inverse as inv,substitute as sub
src=DE/'annular_neck_reflection23.json';E=json.loads(src.read_text());eta={int(k):tuple(v)for k,v in E['eta_adapted_K_basis_a_barb_d_e_f'].items()}
Lwords=[(1,),(3,),(4,),(-5,2,5)]
Qwords=[eta[1],eta[3],eta[4]]
L=WeightedFold(Lwords);Q=WeightedFold(Qwords)
def graph(F):
 roots={F.find(i)[0]for i in range(len(F.parent))};g={}
 for r in roots:
  g[r]={}
  for x,e in F.adj[r].items():
   u,c,v,t=F.edge_weight(e);assert u==r and c==x;g[r][x]=v
 for u,row in g.items():
  for x,v in row.items():assert g[v][-x]==u
 return F.find(0)[0],g
lr,lg=graph(L);qr,qg=graph(Q);base=(lr,qr)
queue=deque([base]);ids={base:0};pg={};path={base:()};tree=set()
while queue:
 u=queue.popleft();pg[u]={}
 for x in sorted(set(lg[u[0]])&set(qg[u[1]])):
  v=(lg[u[0]][x],qg[u[1]][x]);pg[u][x]=v
  if v not in ids:
   ids[v]=len(ids);path[v]=red(path[u]+(x,));queue.append(v)
   tree.add((u,x,v));tree.add((v,-x,u))
assert sum(len(d)for d in pg.values())%2==0
loops=[]
for u,row in pg.items():
 for x,v in row.items():
  if x<0 or (u,x,v)in tree:continue
  w=red(path[u]+(x,)+inv(path[v]));assert w
  wl=L.rewrite(w);wq=Q.rewrite(w);assert wl is not None and wq is not None
  assert sub(wl,L.words)==w and sub(wq,Q.words)==w
  #preimage under eta in actual <a,d,e> coordinates
  uneta=sub(w,{i:eta[i]for i in range(1,6)})
  expected=sub(wq,{1:(1,),2:(3,),3:(4,)})
  assert uneta==expected
  loops.append({'word_common_K':w,'word_L_basis':wl,'word_eta_adE_basis':wq,'eta_inverse_word_adE':uneta})
rank=sum(len(d)for d in pg.values())//2-len(pg)+1;assert rank==len(loops)
#Retain the entire connected fiber-product automaton, including finite tails;
#its complete fundamental-group basis decides the exact intersection.
out={'status':'PASS_EXACT_INTERSECTION','input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
 'common_K_labels':['a','B=bar_b','d','e','f'],'L_basis':Lwords,'Q_basis_eta_adE':Qwords,
 'left_vertices':len(lg),'right_vertices':len(qg),'product_vertices':len(pg),'product_edges':sum(len(r)for r in pg.values())//2,'intersection_rank':rank,
 'product_graph':{str(ids[u]):{str(x):ids[v]for x,v in row.items()}for u,row in pg.items()},
 'base_vertex':0,'spanning_tree_paths':{str(ids[u]):path[u]for u in pg},'intersection_free_basis':loops,
 'scope':'Entire finite Stallings fiber product computes <a,d,e,f^-1 B f> intersect eta(<a,d,e>) exactly. Its application uses A\'s separate exact C_R(k) intersection theorem and the full a,d,e cross-family diagonal block; no broader subgroup or quotient conclusion.'}
(P/'annular_contact_intersection23.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS exact full finite subgroup fiber product')
print('vertices L,Q,product:',len(lg),len(qg),len(pg),'rank:',rank)
for row in loops:print('common word',row['word_common_K'],'L witness',row['word_L_basis'],'outer a,d,e witness',row['eta_inverse_word_adE'])
print('Scope: this one exact intersection; no orbit-depth or finite-group search')
