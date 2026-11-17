#!/usr/bin/env python3
"""Rebuild the S5 coset graph and check EXIT_TOWER B21 graph cycles/algebra.
No unprovided path-word file is used.
"""
from itertools import permutations
from collections import deque
from pathlib import Path
import re,json
P=tuple(permutations(range(5)));one=tuple(range(5))
def mul(p,q):return tuple(p[q[i]] for i in range(5))
def cyc(*xs):
 p=list(one)
 for a,b in zip(xs,xs[1:]+xs[:1]):p[a]=b
 return tuple(p)
def generated(gs):
 H={one}; todo=[one]
 while todo:
  h=todo.pop()
  for g in gs:
   x=mul(h,g)
   if x not in H:H.add(x);todo.append(x)
 return H
H=generated([mul(cyc(1,2),cyc(3,4))])
HB=generated([cyc(0,1,2),mul(cyc(1,2),cyc(3,4))])
HQ=generated([cyc(1,3,2,4)])
def rep(p,G):return min(mul(p,h) for h in G)
E=sorted({rep(p,H) for p in P})
B=sorted({rep(p,HB) for p in P});Q=sorted({rep(p,HQ) for p in P})
assert (len(B),len(Q),len(E))==(20,30,60)
V=[('B',p) for p in B]+[('Q',p) for p in Q]
ends=[(('B',rep(p,HB)),('Q',rep(p,HQ))) for p in E]
adj={v:[] for v in V}
for i,(s,t) in enumerate(ends,1):adj[s].append((i,t));adj[t].append((-i,s))
tree=set();paths={V[0]:[]};todo=deque([V[0]])
while todo:
 v=todo.popleft()
 for i,w in sorted(adj[v],key=lambda e:abs(e[0])):
  if w not in paths:paths[w]=paths[v]+[i];tree.add(abs(i));todo.append(w)
assert len(paths)==50
non=[i for i in range(1,61) if i not in tree]
assert non==[2,3,6,8,9,13,19,22,42,45,48]
def inverse(w):return [-x for x in reversed(w)]
def red(w):
 s=[]
 for x in w:
  if s and s[-1]==-x:s.pop()
  else:s.append(x)
 return s
cycles=[red(paths[ends[i-1][0]]+[i]+inverse(paths[ends[i-1][1]])) for i in non]
source=Path(__file__).resolve().parents[2]/'background/exit_tower_cp28/sections/B.tex'
text=source.read_text()
# Parse the eleven printed B36 cycle words, to compare to the independent BFS.
chunk=text[text.index('g_1 &[1,-12'):text.index('\\tag{B.36}')]
printed=[]
for m in re.finditer(r'&\[([^\]]+)\]',chunk):printed.append([int(x) for x in m.group(1).split(',')])
assert cycles==printed,(cycles,printed)
print('PASS core graph: 20+30 vertices,60 edges,connected; vertex degree3/2')
print('PASS BFS tree49 edges; printed11 non-tree edges and all B36 cycles')
# Formal free-word checks, requiring no braid relation.
g={1:[1,2,4,5],2:[5],3:[1,2,5],4:[-5,-4,5],5:[1,3,5],6:[-5,-3,5],7:[-5,3,5],8:[-2,-5,-4],9:[-2,-1,-5,-4,-3],10:[1,2,3,4,5],11:[1]}
def evaluate(w):return red(z for x in w for z in (g[x] if x>0 else inverse(g[-x])))
relations={1:[3,-4],5:[11,2,-6],7:[-6],8:[2,-3,11,4,-2],9:[2,-3,4,6,-2],10:[3,-6,-4]}
for lhs,rhs in relations.items():assert evaluate([lhs])==evaluate(rhs)
for rhs,expected in [([11],[1]),([-11,3,-2],[2]),([2,-6,-2],[3]),([2,-4,-2],[4]),([2],[5])]:assert evaluate(rhs)==expected
print('PASS six B39 elimination relations as freely reduced words')
print('PASS B38 inverse images recover a,b,x,y,z exactly')
vertex_counts=[12,20,30,60,60,120,60,120,60]
arrow_counts=[60,120,60,120,60,60,120,120,120,120,120,360,120,60]
assert sum(vertex_counts)==542 and sum(arrow_counts)==1620
assert 1620-542+1==1079
assert 12+(1620-60)-(542-50)==1080
print('PASS declared full counts:542 vertices,1620 edges,1079 cycles')
print('PASS Tietze extension count:12+(1560−492)=1080 relators')
out={'core_vertices':50,'core_edges':60,'non_tree_edges':non,'core_cycles':cycles,'full_vertices':542,'full_edges':1620,'full_relator_count':1080,'scope':'Graph, printed core cycle words and algebraic eliminations only; geometric word table B37 not checked by this program.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['scope'])
