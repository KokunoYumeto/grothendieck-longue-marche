#!/usr/bin/env python3
"""Independent complete replay of actual21 Fox data and forest comparison."""
from pathlib import Path
from collections import defaultdict
import json,hashlib,time
H=Path(__file__).resolve().parent;ROOT=H.parents[1];P=ROOT/'work_CE/next_symmetric_nodes'
fp=P/'actual_full21_Fox.json';d=json.loads(fp.read_text());started=time.monotonic()
paired=json.loads((P/'symmetric_paired_fox_data.json').read_text())
source=json.loads((P/'symmetric_full_source_data.json').read_text())
own=json.loads((H/'boundary16_and_Tate_certificate.json').read_text())
def red(w):
 a=[]
 for x in w:
  if a and a[-1]==-x:a.pop()
  else:a.append(x)
 return tuple(a)
def inv(w):return tuple(-x for x in w[::-1])
def sub(w,A):return red(y for x in w for y in(A[abs(x)] if x>0 else inv(A[-x])))
def mp(x):return {int(k):tuple(v) for k,v in x.items()}
def add(m,k,n):
 m[k]+=n
 if not m[k]:del m[k]
for name,h in d['input_sha256'].items():assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==h
T=[tuple(x) for x in d['retained_word_DAG']];R=[tuple(x) for x in d['R_word_DAG']]
gens=[None]+[tuple(x) for x in d['common_R_generators'][1:]]
GG=[tuple(x) for x in d['group_elements']]
def valid(nodes,bound):
 assert nodes[0]==(0,0,0);idx={}
 for n,(p,x,l) in enumerate(nodes[1:],1):
  assert 0<=p<n and 0<abs(x)<bound and l==nodes[p][2]+1
  assert not p or nodes[p][1]!=-x
  assert (p,x) not in idx;idx[p,x]=n
 return idx
TI=valid(T,6);RI=valid(R,len(gens));GI={}
slots=(2,3,5,6,7,8,10,11)
for i,g in enumerate(gens[1:],1):
 assert 0<=g[0]<len(T) and g[1] in slots and g not in GI;GI[g]=i
Gidx={g:i for i,g in enumerate(GG)};assert len(Gidx)==len(GG) and GG[0]==(0,0,0)
for a,b,t in GG:assert 0<=a<len(R) and 0<=b<len(R) and 0<=t<len(T)
def append(nodes,idx,p,x):return nodes[p][0] if p and nodes[p][1]==-x else idx[p,x]
def locate(nodes,idx,w):
 p=0
 for x in w:p=append(nodes,idx,p,x)
 return p
def read(nodes,p):
 w=[]
 while p:p,x,l=nodes[p];w.append(x)
 return tuple(reversed(w))
ret={j:i+1 for i,j in enumerate(paired['retained_paired_indices'])};beta=mp(paired['retained_involution'])
beta_cache={0:0}
def betaid(t):
 if t not in beta_cache:beta_cache[t]=locate(T,TI,sub(read(T,t),beta))
 return beta_cache[t]
def advance(gid,x):
 a,b,t=GG[gid];j=abs(x);s=1 if x>0 else -1
 if j in ret:t=append(T,TI,t,s*ret[j])
 elif j<12:a=append(R,RI,a,s*GI[t,j])
 else:b=append(R,RI,b,s*GI[betaid(t),j-10])
 return Gidx[a,b,t]
def fox(w):
 v=defaultdict(int);p=0
 for x in w:
  q=advance(p,x)
  add(v,(abs(x),p if x>0 else q),1 if x>0 else -1);p=q
 return dict(v),p
def boundary(v):
 b=defaultdict(int)
 for (j,g),n in v.items():add(b,advance(g,j),n);add(b,g,-n)
 return dict(b)
def decode(rows):
 out={}
 for j,g,n in rows:
  assert 1<=j<=21 and 0<=g<len(GG) and isinstance(n,int) and n and (j,g) not in out
  out[j,g]=n
 return out
expected={}
for a in paired['old_actions']:
 expected['old',a['name'],'push']=mp(a['geometric_push_paired'])
 expected['old',a['name'],'pull']=mp(a['based_pullback_paired'])
for a in source['old_source_generators']:
 expected['source',a['name'],'push']=mp(a['source_push_F21'])
 expected['source',a['name'],'pull']=mp(a['source_pullback_F21'])
F=mp(paired['paired_involution']);assert all(len(w)==1 for w in F.values())
expected['involution','F','self_inverse']=F
checks=[];letters=terms=source_F=0
for m in d['matrices']:
 key=(m['family'],m['name'],m['direction']);A=expected[key]
 assert len(m['columns'])==len(m['literal_F21_images'])==21
 for j in range(1,22):
  w=tuple(m['literal_F21_images'][j-1]);assert w==A[j]
  v,p=fox(w);assert v==decode(m['columns'][j-1]) and p==m['generator_images_G'][j-1]
  b=defaultdict(int);add(b,p,1);add(b,0,-1);assert boundary(v)==dict(b)
  if j not in ret:
   core=w
   while len(core)>1 and core[0]==-core[-1]:core=core[1:-1]
   target=F[j][0] if m['family']=='involution' else j
   assert core==(target,),('actual peripheral conjugacy',key,j,core)
  if m['family']=='source':
   assert sub(w,F)==sub(F[j],A);source_F+=1
  letters+=len(w);terms+=len(v)
 checks.append({'family':key[0],'name':key[1],'direction':key[2],
                'all21_exact_derivatives_and_boundaries':True,'deleted_peripheral_conjugacies':True})
 print('PASS complete independent Fox matrix',*key,flush=True)
assert len(checks)==35 and letters==703187 and terms==695738 and source_F==462
# Direct literal inverse/chain-rule calibrations, without expanding huge
# products of matrices. The general chain rule is proved algebraically.
inverse_checks=0
for family,name in [('old','0'),('source','branch_square')]:
 A=expected[family,name,'push'];B=expected[family,name,'pull']
 for j in range(1,22):
  assert sub(A[j],B)==sub(B[j],A)==(j,);inverse_checks+=2
for j in range(1,22):assert sub(F[j],F)==(j,)
ids={int(k):GI[locate(T,TI,v['retained_word']),v['paired_slot']] for k,v in own['common_R_basis'].items()}
def convert_R(w):return locate(R,RI,((1 if x>0 else -1)*ids[abs(x)] for x in w))
own_nodes={tuple(n['node_index']):n for n in own['columns']}
original={(n['loop_index'],n['local_node_index']):n for n in paired['node_columns']}
node_checks=[]
for n in d['node_cycles']:
 key=tuple(n['node_index']);assert n['literal_F21_word']==original[key]['paired_relator']
 v,p=fox(n['literal_F21_word']);assert p==0 and not boundary(v)
 assert v==decode(n['full21_cycle'])
 drop={k:c for k,c in v.items() if k[0] not in ret};assert drop==decode(n['collapsed16_cycle'])
 want={}
 for r in own_nodes[key]['boundary_terms']:
  g=r['G_coefficient'];gid=Gidx[convert_R(g['A_word']),convert_R(g['B_word']),locate(T,TI,g['retained_word'])]
  row=r['slot']+(0 if r['side']=='A' else 10);assert (row,gid) not in want;want[row,gid]=r['coefficient']
 assert drop==want
 node_checks.append({'node_index':key,'full_terms':len(v),'collapsed_terms':len(drop),'entire_independent_cycle_equal':True})
print('PASS all64 exact full21/own16 comparisons and retained forest projection.',flush=True)
out={'input_sha256':hashlib.sha256(fp.read_bytes()).hexdigest(),'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'all_DAGs_canonical':True,'DAG_counts':[len(T),len(R),len(gens)-1,len(GG)],'matrix_checks':checks,
 'literal_letters':letters,'matrix_terms':terms,'actual_source_F_commutations':source_F,
 'direct_small_inverse_compositions':inverse_checks,'node_checks':node_checks,
 'composition_scope':'All735 literal evaluated derivatives independently checked. Semilinear composition follows from the proved Fox chain rule; only the specified small inverse calibrations are expanded, not huge matrix products.',
 'claims_excluded':['ordinary linear composition','old operators on arbitrary16 edges','whole-orbit syzygy conclusion'],
 'elapsed_seconds':time.monotonic()-started}
(H/'actual_full21_Fox_independent_review.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS735 columns,462 source/F words,84 small inverse compositions; seconds',round(out['elapsed_seconds'],3),flush=True)
