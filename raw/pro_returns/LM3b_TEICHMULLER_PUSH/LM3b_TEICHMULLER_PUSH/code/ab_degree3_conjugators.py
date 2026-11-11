#!/usr/bin/env python3
"""Integral degree-three spherical conjugators, as group-commutator lift recipes."""
from ab_lie import *

def tree(w):
 if len(w)==1:return w[0]
 for j in range(1,len(w)):
  if is_lyndon(w[j:]):return [tree(w[:j]),tree(w[j:])]

def get_a(p,i):
 bas=[expand(w) for w in lyndon(3,3)]
 cols=[coords(bracket(a,gen(i)),3,4) for a in bas]
 M=sp.zeros(len(lyndon(3,4)),len(bas))
 for j,c in enumerate(cols):
  for k,v in c.items():M[k,j]=v
 b=sp.zeros(M.rows,1)
 for k,v in coords(p,3,4).items():b[k]=v
 sol=M.gauss_jordan_solve(b)[0]
 return sol

out=[]
for D in special(3,3):
 aa=[get_a(p,i) for i,p in enumerate(D)]
 den=sp.ilcm(*[sp.denom(v) for a in aa for v in a])
 row=[]
 for a in aa:
  row.append([dict(coefficient=int(c*den),lyndon_word=list(w),tree=tree(w)) for c,w in zip(a,lyndon(3,3)) if c])
 out.append(row)
with open(Path(__file__).with_name('ab_degree3_conjugators.json'),'w') as f:json.dump(out,f,indent=2)
print('Six integral solutions; each array lists a_x,a_y,a_z.')
print('Lift tree [s,t] as group commutator s t s^-1 t^-1, multiply indicated powers.')
print('Conjugate each generator by its A_i; relation product is exact modulo gamma_5.')
print(json.dumps(out,indent=2))
