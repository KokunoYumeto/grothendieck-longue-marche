#!/usr/bin/env python3
"""Joint cycle residues for the six signed SL2(F3) evaluations.
Necessary finite conditions only. Full profinite liftability is not asserted.
"""
from itertools import permutations
from pathlib import Path
import json
m=3;I=(1,0,0,1)
def mm(a,b):return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%m for i in range(2) for j in range(2))
def inv(a):return (a[3],-a[1]%m,-a[2]%m,a[0])
M=[(a,b,c,d) for a in range(3) for b in range(3) for c in range(3) for d in range(3) if (a*d-b*c)%3==1]
ind={a:i for i,a in enumerate(M)};mul=[[ind[mm(a,b)] for b in M] for a in M];iv=[ind[inv(a)] for a in M]
S=(0,1,2,0);tau=(1,2,0,1);z=inv(mm(S,tau));pairs=list(permutations((S,tau,z),2))
X=bytes(ind[a] for a,b in pairs);Y=bytes(ind[b] for a,b in pairs);ID=bytes([ind[I]]*6)
def tm(a,b):return bytes(mul[i][j] for i,j in zip(a,b))
def ti(a):return bytes(iv[i] for i in a)
def cj(a,b):return tm(tm(a,b),ti(a))
def closure(gens):
 seen={ID};todo=[ID]
 for a in todo:
  for b in gens:
   c=tm(a,b)
   if c not in seen:seen.add(c);todo.append(c)
 return seen
G=[ID];index={ID:0};parent=[-1];letter=[-1]
for a in G:
 i=index[a]
 for j,b in enumerate((X,Y)):
  c=tm(a,b)
  if c not in index:index[c]=len(G);G.append(c);parent.append(i);letter.append(j)
print('group order',len(G),flush=True)
Z=ti(tm(X,Y))
def subst(a,b,check=True):
 vals=[ID]*len(G)
 for i in range(1,len(G)):vals[i]=tm(vals[parent[i]],(a,b)[letter[i]])
 if check:
  for i,g in enumerate(G):
   for old,new in ((X,a),(Y,b)):
    if vals[index[tm(g,old)]]!=tm(vals[i],new):return None
 return vals
th=subst(Y,X);ro=subst(Y,Z);assert th is not None and ro is not None
basic=tm(tm(X,Y),tm(ti(X),ti(Y)));derived=closure(list({cj(g,basic) for g in G}));print('derived order',len(derived),flush=True)
rows=[];cycle_count=0
for f in sorted(derived):
 i=index[f]
 if tm(f,th[i])!=ID:continue
 rf=ro[i];r2f=ro[index[rf]]
 if tm(tm(r2f,rf),f)!=ID:continue
 cycle_count+=1
 ay=cj(ti(f),Y)
 vals=subst(X,ay)
 if vals is None or len(set(vals))!=len(G):continue
 v=M[f[0]];h=M[tm(rf,f)[0]]
 rows.append(dict(f=list(f),v=v,h=h))
out=dict(order=len(G),derived_order=len(derived),cycles=cycle_count,cycle_automorphisms=len(rows),pairs=pairs,rows=rows,scope='Necessary finite cycle-automorphism locus only; no full profinite lift asserted')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
