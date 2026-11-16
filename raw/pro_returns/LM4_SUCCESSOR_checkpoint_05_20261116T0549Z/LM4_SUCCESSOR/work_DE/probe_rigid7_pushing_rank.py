"""Exploratory Stallings ranks in the seven-point pushing fibre.
Depends on numerically discovered braids; no topological certification yet.
"""
from pathlib import Path
import json,itertools,importlib.util,numpy as np
p=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('probe',p/'probe_rigid7_pushing.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
d=json.loads((p/'rigid7_pushing_probe.json').read_text());loops=d['loops'];braids=[x['braid'] for x in loops]
base=complex(*d['base']);order=list(np.argsort(m.config(base).real));local=m.S[1:].index(2);x=order.index(local)+1
print('Finite labels:',[a+1 for a in m.S[1:]],'x-sorted local indices:',order,'deleted label3 free-generator index',x)

def delx(w):return m.reduce(a if abs(a)<x else (a-1 if a>0 else a+1) for a in w if abs(a)!=x)
def fibre(w):
 a=m.action(w)
 assert [delx(v) for i,v in enumerate(a,1) if i!=x]==[(j,) for j in range(1,6)],'not in fibre'
 v=a[x-1];c=[]
 while len(v)>1 and v[0]==-v[-1]:c.append(v[0]);v=v[1:-1]
 assert v==(x,)
 return delx(c)

def rank(words):
 # Fold a bouquet of word loops, using union-find and repeated deterministic edge folding.
 edges=[];vertex=1
 for w in words:
  at=0
  for k,c in enumerate(w):
   to=0 if k==len(w)-1 else vertex
   if to:vertex+=1
   edges.append((at,c,to));edges.append((to,-c,at));at=to
 parent=list(range(vertex))
 def find(v):
  while parent[v]!=v:parent[v]=parent[parent[v]];v=parent[v]
  return v
 changed=True
 while changed:
  changed=False;table={}
  for a,c,b in edges:
   a,b=find(a),find(b);key=(a,c)
   if key in table:
    old=find(table[key])
    if old!=b:parent[b]=old;changed=True
   else:table[key]=b
 E={(find(a),c,find(b)) for a,c,b in edges}
 V={find(i) for i in range(vertex)}
 return len(E)//2-len(V)+1,len(V),len(E)//2

par=[i for i,a in enumerate(loops) if abs(complex(*a['root']))==1 and abs(complex(*a['root']).imag)<1e-8]
assert par==[4,10],par
other=[i for i in range(13) if i not in par]
words=[];names=[]
for g in [()]+[(i+1,) for i in other]+[(-i-1,) for i in other]:
 gb=tuple(braids[g[0]-1]) if g and g[0]>0 else (m.inverse(braids[-g[0]-1]) if g else ())
 for a in par:
  b=m.mul(gb,braids[a],m.inverse(gb));w=fibre(b)
  words.append(w);names.append((g,a+1))
  print('conjugate',g,a+1,'push length',len(w),flush=True)
  if len(words) in [2,24,46]:print('rank',len(words),rank(words),flush=True)
print('FREE DOMAIN BASIS SIZE',len(words),'FIBRE IMAGE RANK',rank(words))
(p/'rigid7_pushing_rank_probe.json').write_text(json.dumps({'warning':__doc__,'deleted_label':3,'free_generator':int(x),'names':names,'words':words,'rank':rank(words)},indent=2)+'\n')
