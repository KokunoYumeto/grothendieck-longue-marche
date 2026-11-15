#!/usr/bin/env python3
"""Exact certificate for the 15 codimension-two meridian lattices of Mbar_0,5."""
from itertools import combinations
from math import gcd
import json
V={
 '12':(-1,-1,-1,-1,-1),
 '13':(0,1,0,1,1),
 '14':(1,0,0,0,0),
 '15':(0,0,1,0,0),
 '23':(1,0,1,0,1),
 '24':(0,1,0,0,0),
 '25':(0,0,0,1,0),
 '34':(-1,-1,0,0,-1),
 '35':(0,0,-1,-1,-1),
 '45':(0,0,0,0,1),
}
print('Basis: dlog(x), dlog(x-1), dlog(y), dlog(y-1), dlog(x-y)')
print('Boundary meridian columns:')
for a in sorted(V): print(a, V[a])
rows=[]
for a,b in combinations(sorted(V),2):
 if set(a)&set(b): continue
 v,w=V[a],V[b]; ds=[]; chosen=None
 for i,j in combinations(range(5),2):
  d=v[i]*w[j]-v[j]*w[i];ds.append(d)
  if chosen is None and abs(d)==1: chosen=(i,j,d)
 assert gcd(*ds)==1 and chosen
 i,j,d=chosen
 L=[[0]*5 for _ in range(2)]
 L[0][i]=w[j]//d;L[0][j]=-w[i]//d
 L[1][i]=-v[j]//d;L[1][j]=v[i]//d
 product=[[sum(L[r][k]*c[k] for k in range(5)) for c in (v,w)] for r in range(2)]
 assert product==[[1,0],[0,1]]
 rows.append({'node_pair':[a,b],'left_inverse':L,'product':product})
 print(f'{a},{b}: minor rows {i+1},{j+1}, determinant {d}; left inverse {L}; product {product}')
assert len(rows)==15
print('All 15 compatible meridian pairs are primitive rank-two direct summands.')
print('Singletons primitive:',all(gcd(*v)==1 for v in V.values()))
with open('EXIT_TOWER_work/code/E_meridian_pairs.json','w') as f:json.dump(rows,f,indent=2)
