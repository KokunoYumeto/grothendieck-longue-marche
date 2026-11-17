#!/usr/bin/env python3
"""Exact Schreier/Fox columns of the stored actual nodal words.

Works in the common far Artin marking. It does not replace that marking
by the paired involution basis, assert a full infinite matrix, or test a
Tate obstruction. Every two-chain boundary is checked independently.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib,sys
ROOT=Path(__file__).resolve().parent.parent
P=ROOT/'next_symmetric_nodes'
inp=P/(sys.argv[1] if len(sys.argv)>1 else 'symmetric_node_words.json')
D=json.loads(inp.read_text());initial=D['initial_order'];labels=D['labels']
def red(w):
 s=[]
 for x in w:
  if s and s[-1]==-x:s.pop()
  else:s.append(x)
 return tuple(s)
def inv(w):return tuple(-x for x in reversed(w))
def mul(*ws):return red(x for w in ws for x in w)
retained=[0,1,2,19,20]
old_to_head={initial.index(p)+1:i+1 for i,p in enumerate(retained)}
head_to_old={v:k for k,v in old_to_head.items()}
basis={};meta={}
def bid(head,physical):
 key=(head,physical)
 if key not in basis:
  j=len(basis)+1;basis[key]=j
  meta[j]={'head_word':head,'physical_label':physical,'component':labels[physical]}
 return basis[key]
def rewrite(w):
 head=();out=[]
 for x in w:
  j=abs(x);sgn=1 if x>0 else -1
  if j in old_to_head:head=red(head+(sgn*old_to_head[j],))
  else:out.append(sgn*bid(head,initial[j-1]))
 assert not head,('word not in actual filling kernel',head)
 return red(out)
def expand(w):
 terms=[]
 for x in w:
  m=meta[abs(x)];g=tuple((1 if y>0 else -1)*head_to_old[abs(y)] for y in m['head_word'])
  d=(initial.index(m['physical_label'])+1,)
  v=mul(g,d,inv(g))
  terms.append(v if x>0 else inv(v))
 return mul(*terms)
def family(j):return meta[abs(j)]['component']['kind']
def project(w,fam):return red(x for x in w if family(x)==fam)
def add(d,k,v):
 d[k]+=v
 if not d[k]:del d[k]
def edge_cycle(w):
 a=b=();out=defaultdict(int)
 for x in w:
  if family(x)=='A':
   aa=red(a+(x,));apos=a if x>0 else aa
   add(out,('A',apos,b,abs(x)),1 if x>0 else -1);a=aa
  else:
   bb=red(b+(x,));bpos=b if x>0 else bb
   add(out,('B',a,bpos,abs(x)),1 if x>0 else -1);b=bb
 assert not a and not b
 return dict(out)
def fill(w):
 # Combing every A edge to the B=1 axis gives a finite product-tree
 # rectangle. The independent edge boundary below verifies all signs.
 a=b=();out=defaultdict(int)
 for x in w:
  if family(x)=='A':
   aa=red(a+(x,));apos=a if x>0 else aa;sx=1 if x>0 else -1
   bp=()
   for y in b:
    bn=red(bp+(y,));bpos=bp if y>0 else bn;sy=1 if y>0 else -1
    add(out,(apos,bpos,abs(x),abs(y)),-sx*sy);bp=bn
   a=aa
  else:b=red(b+(x,))
 assert not a and not b
 return dict(out)
def boundary(cells):
 out=defaultdict(int)
 for (a,b,i,j),n in cells.items():
  assert family(i)=='A' and family(j)=='B'
  add(out,('A',a,b,i),n)
  add(out,('A',a,red(b+(j,)),i),-n)
  add(out,('B',red(a+(i,)),b,j),n)
  add(out,('B',a,b,j),-n)
 return dict(out)
def ab(w):
 out=defaultdict(int)
 for x in w:add(out,abs(x),1 if x>0 else -1)
 return dict(out)
rows=[]
for loop in D['loops']:
 for ni,node in enumerate(loop['nodes']):
  ma,mb=(rewrite(w) for w in node['meridians'])
  rr=rewrite(node['commutator'])
  assert expand(ma)==tuple(node['meridians'][0]) and expand(mb)==tuple(node['meridians'][1])
  assert expand(rr)==tuple(node['commutator'])
  assert rr==mul(ma,mb,inv(ma),inv(mb))
  fa=labels[node['physical_labels'][0]]['kind'];fb=labels[node['physical_labels'][1]]['kind']
  assert {fa,fb}=={'A','B'}
  assert not project(ma,fb) and not project(mb,fa)
  assert not project(rr,'A') and not project(rr,'B')
  aba,abb=ab(ma),ab(mb)
  assert len(aba)==len(abb)==1 and list(aba.values())==list(abb.values())==[1]
  ia,ib=next(iter(aba)),next(iter(abb))
  if fa=='B':ia,ib=ib,ia
  cells=fill(rr);edges=edge_cycle(rr)
  assert boundary(cells)==edges
  aug=defaultdict(int)
  for (_,_,i,j),n in cells.items():add(aug,(i,j),n)
  assert dict(aug)=={(ia,ib):1 if fa=='A' else -1}
  rows.append({'loop_index':loop['index'],'local_node_index':ni,
   'physical_labels':node['physical_labels'],'schreier_meridians':[ma,mb],
   'schreier_relator':rr,'component_basis_pair':[ia,ib],
   'augmented_orientation':1 if fa=='A' else -1,
   'fox_cells':[{'A_vertex':a,'B_vertex':b,'A_generator':i,'B_generator':j,'coefficient':v}
     for (a,b,i,j),v in sorted(cells.items())],
   'edge_boundary_terms':len(edges),'two_chain_terms':len(cells)})
  print('PASS exact Fox column',loop['index'],ni,'letters',len(rr),'squares',len(cells),'boundary',len(edges),flush=True)
out={'scope':__doc__,'input':str(inp.relative_to(ROOT.parent)),
 'input_sha256':hashlib.sha256(inp.read_bytes()).hexdigest(),
 'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'retained_physical_labels':retained,'old_to_head_basis':old_to_head,
 'finite_used_schreier_basis':meta,'node_columns':rows,
 'total_columns':len(rows),'total_two_chain_terms':sum(r['two_chain_terms'] for r in rows),
 'full_matrix_claim':False,'paired_involution_basis_converted':False,
 'old_base_action_translates_included':False,
 'actual_finite_claim':'These exact transported local node columns and their actual filling-kernel words, in one common far marking.'}
outpath=P/(inp.stem+'_fox_columns.json')
outpath.write_text(json.dumps(out,indent=2)+'\n')
print('PASS',len(rows),'exact transported columns;',len(meta),'used Schreier generators;',out['total_two_chain_terms'],'nonzero square terms.',flush=True)
