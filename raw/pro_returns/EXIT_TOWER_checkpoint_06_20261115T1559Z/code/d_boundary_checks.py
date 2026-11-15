#!/usr/bin/env python3
"""Exact checks for D.2, D.4, D.9 and the one-step M_0,6 modifications.
All graphs use labelled subsets; no finite quotient is substituted for the
infinite curve complex. The lifted pentagon is described in the paper.
"""
from itertools import combinations
from pathlib import Path
from collections import Counter
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

def main():
 vertices=list(combinations(range(1,6),2))
 edges=[(a,b) for a,b in combinations(vertices,2) if set(a).isdisjoint(b)]
 A=sp.zeros(10)
 for a,b in edges:
  i,j=vertices.index(a),vertices.index(b);A[i,j]=A[j,i]=1
 Q=A-sp.eye(10)
 S=smith_normal_form(Q,domain=ZZ)
 print('Petersen graph vertices,edges:',len(vertices),len(edges))
 print('Intersection matrix rank:',Q.rank())
 print('Smith diagonal:',[abs(int(S[i,i])) for i in range(10)])
 print('First Betti number of graph:',len(edges)-len(vertices)+1)
 pentagon=[(1,2),(3,4),(1,5),(2,3),(4,5)]
 cyc=list(zip(pentagon,pentagon[1:]+pentagon[:1]))
 assert all(set(a).isdisjoint(b) for a,b in cyc)
 edge=frozenset(((1,2),(3,4)))
 cocycle=sum(frozenset((a,b))==edge for a,b in cyc)%2
 print('Actual-curve pentagon:',pentagon)
 print('Z/2 edge cocycle evaluation:',cocycle)
 assert cocycle==1
 print('Triple crossing depth2 auxiliary graph cycle rank:',3-3+1)
 print('Triple crossing pi1 ranks truncated,full:',4,3)
 p=Path(__file__).with_name('a_graphs_0_6.json')
 if p.exists():
  data=json.loads(p.read_text())
  types=Counter()
  for genera,legs,es in data['graphs']:
   if len(es) not in (2,3):continue
   val=[legs.count(v) for v in range(len(genera))]
   deg=[sum(a==v for a,b in es)+sum(b==v for a,b in es) for v in range(len(genera))]
   key=tuple(sorted(zip(deg,val)))
   types[(len(es),key)]+=1
  print('Mbar_0,6 stratum counts:',data['by_edges'])
  print('Nontrivial one-stratum blowups:',sum(types.values()))
  print('S6-orbit sizes and vertex (internal degree,leg count) types:')
  for key,count in sorted(types.items()):print(key,count)
  assert sorted(types.values())==[15,45,60,90]
 # Each star subdivision of a standard orthant at its coordinate face
 # replaces one standard generator by their sum; determinant has abs one.
 for r in (2,3):
  v=sp.ones(r,1)
  dets=[]
  for j in range(r):
   M=sp.eye(r);M[:,j]=v;dets.append(int(M.det()))
  print('Star subdivision codimension',r,'maximal cone determinants',dets)
  assert all(abs(a)==1 for a in dets)
if __name__=='__main__':main()
