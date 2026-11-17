#!/usr/bin/env python3
"""Independent DAG/input/telescoping audit, without the large expansion."""
from pathlib import Path
from collections import defaultdict
import json,hashlib,time
H=Path(__file__).resolve().parent;ROOT=H.parents[1];P=ROOT/'work_CE/next_symmetric_nodes'
f=P/'geometric_stabilizer_factored_chain.json';j=json.loads(f.read_text())
d=json.loads((P/'symmetric_paired_fox_data.json').read_text())
raw=json.loads((P/'geometric_stabilizer_column.json').read_text());start=time.monotonic()
def red(w):
 s=[]
 for x in w:
  if s and s[-1]==-x:s.pop()
  else:s.append(x)
 return tuple(s)
def inv(w):return tuple(-x for x in w[::-1])
def sub(w,A):return red(y for x in w for y in(A[abs(x)] if x>0 else inv(A[-x])))
def mp(m):return {int(k):tuple(v) for k,v in m.items()}
def add(m,k,n):
 m[k]+=n
 if not m[k]:del m[k]
for rel,h in j['input_sha256'].items():assert hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==h
node=next(x for x in d['node_columns'] if (x['loop_index'],x['local_node_index'])==(8,0))
a,b=map(tuple,node['paired_meridians']);original=red(a+b+inv(a)+inv(b))
assert original==tuple(node['paired_relator'])
for x in(6,2,-6,-2):
 op=mp(d['old_actions'][abs(x)-1]['geometric_push_paired' if x>0 else 'based_pullback_paired'])
 a,b=sub(a,op),sub(b,op)
large=red(a+b+inv(a)+inv(b))
assert list(large)==raw['transformed_relator_F21']
assert list(a)==raw['transformed_meridians_F21'][0] and list(b)==raw['transformed_meridians_F21'][1]
print('PASS literal four-action input:',len(large),'letters',flush=True)
T=[tuple(x) for x in j['retained_word_DAG']];R=[tuple(x) for x in j['R_word_DAG']]
G=[None]+[tuple(x) for x in j['common_R_generators'][1:]]
assert j['common_R_generators'][0] is None
def validate(nodes,bound):
 assert nodes[0]==(0,0,0);index={}
 for k,(p,x,n) in enumerate(nodes[1:],1):
  assert 0<=p<k and 0<abs(x)<bound and n==nodes[p][2]+1
  assert not p or nodes[p][1]!=-x
  assert (p,x) not in index;index[p,x]=k
 return index
TI=validate(T,6);RI=validate(R,len(G));GI={}
for k,g in enumerate(G[1:],1):
 assert 0<=g[0]<len(T) and g[1] in(2,3,5,6,7,8,10,11)
 assert g not in GI;GI[g]=k
def step(nodes,index,p,x):return nodes[p][0] if p and nodes[p][1]==-x else index[p,x]
def tstep(p,x):return step(T,TI,p,x)
def rstep(p,x):return step(R,RI,p,x)
def read(nodes,p):
 out=[]
 while p:p,x,n=nodes[p];out.append(x)
 return tuple(reversed(out))
def locate(nodes,index,word):
 p=0
 for x in word:p=step(nodes,index,p,x)
 return p
ret={x:i+1 for i,x in enumerate(d['retained_paired_indices'])};beta=mp(d['retained_involution'])
assert all(len(v)==1 for v in beta.values());results=[]
for circuit,w in zip(j['circuits'],(original,large)):
 assert tuple(circuit['literal_F21_word'])==w and len(w)==circuit['input_length']
 h=bh=a=b=0;Ae=defaultdict(int);Be=defaultdict(int);cost=deleted=0
 for letter in w:
  x=abs(letter);sg=1 if letter>0 else -1
  if x in ret:
   k=ret[x];h=tstep(h,sg*k);bh=tstep(bh,sg*beta[k][0]);continue
  deleted+=1
  if x<12:
   g=GI[h,x];an=rstep(a,sg*g);add(Ae,(an,b),1);add(Ae,(a,b),-1);a=an
  else:
   g=GI[bh,x-10];bn=rstep(b,sg*g);bv=b if sg>0 else bn
   add(Be,(a,bv,g),sg);cost+=R[a][2];b=bn
 assert h==bh==a==b==0
 Ab=defaultdict(int);Bb=defaultdict(int);keys=set()
 for term in circuit['rectangles']:
  a=term['A_endpoint'];v=term['B_edge_start'];g=term['B_generator'];n=term['coefficient']
  assert 0<a<len(R) and 0<=v<len(R) and 0<g<len(G) and isinstance(n,int) and n
  assert (a,v,g) not in keys;keys.add((a,v,g));vg=rstep(v,g)
  add(Ab,(a,v),n);add(Ab,(a,vg),-n)
  add(Bb,(a,v,g),n);add(Bb,(0,v,g),-n)
 assert {k:n for k,n in Ab.items() if k[0]}=={k:n for k,n in Ae.items() if k[0]}
 assert Bb==Be
 assert cost==circuit['uncollected_expansion_cost'] and deleted==circuit['deleted_letter_count']
 assert len(keys)==circuit['factored_term_count']
 results.append({'name':circuit['name'],'letters':len(w),'factored_terms':len(keys),'uncollected_cost':cost,'exact_boundary':True})
 print('PASS independent complete boundary:',circuit['name'],len(keys),'terms, cost',cost,flush=True)
expanded=defaultdict(int)
for term in j['circuits'][0]['rectangles']:
 at=0
 for x in read(R,term['A_endpoint']):
  nxt=rstep(at,x);u=at if x>0 else nxt
  add(expanded,(u,term['B_edge_start'],abs(x),term['B_generator']),term['coefficient']*(1 if x>0 else -1));at=nxt
old={}
for k,v in d['finite_used_common_R_basis'].items():old[int(k)]=GI[locate(T,TI,v['retained_word']),v['paired_slot']]
def cv(w):return locate(R,RI,((1 if x>0 else -1)*old[abs(x)] for x in w))
want=defaultdict(int)
for c in node['fox_cells']:add(want,(cv(c['A_vertex']),cv(c['B_vertex']),old[c['A_generator']],old[c['B_generator']]),c['coefficient'])
assert expanded==want and len(want)==117
assert results[1]['factored_terms']>2*results[0]['factored_terms']
out={'input_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'actual_input_reconstructed':True,'retained_DAG_nodes':len(T),'R_DAG_nodes':len(R),'common_generators':len(G)-1,
 'all_DAG_nodes_canonical_freely_reduced':True,'circuits':results,'all117_original_coefficients_match':True,
 'not_a_single_G_unit_multiple_by_support':True,'elapsed_seconds':time.monotonic()-start,
 'scope':'Exact full-chain root-path normal forms; no large rectangle expansion, collected G-row support or whole-block overlap claim.'}
(H/'factored_product_tree_chain_independent_review.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all DAGs,117 calibration,and33162>2*42 unit obstruction; seconds',round(out['elapsed_seconds'],3),flush=True)
