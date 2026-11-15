"""Exact finite parenthesized-pants to chamber-braid dictionaries."""
from pathlib import Path
from collections import deque
import itertools,json
P=Path(__file__).parent
H={};exec((P/'b_genus_zero.py').read_text().split('\ndata={}')[0],H)
red,inv=H['red'],H['inv']
ch=json.loads((P/'b_genus_zero.json').read_text())
def shapes(a,n):
 if n==1:return [a]
 return [(l,r) for k in range(1,n) for l in shapes(a,k) for r in shapes(a+k,n-k)]
def rotations(t):
 if isinstance(t,int):return []
 l,r=t;out=[]
 if not isinstance(l,int):out.append((l[0],(l[1],r)))
 out += [(v,r) for v in rotations(l)]
 out += [(l,v) for v in rotations(r)]
 return out
def cherries(t):
 if isinstance(t,int):return []
 l,r=t
 if isinstance(l,int) and isinstance(r,int):return [l+1]
 return cherries(l)+cherries(r)
def leftcomb(n):
 t=0
 for j in range(1,n):t=(t,j)
 return t
data={}
for m in (3,4):
 ts=shapes(0,m);ti={t:i for i,t in enumerate(ts)};root=ti[leftcomb(m)]
 ps=list(itertools.permutations(range(1,m+1)))
 objects=[(p,k) for p in ps for k in range(len(ts))];vid={v:i for i,v in enumerate(objects)}
 edges=[];Fedges={};Bedges={}
 def add(kind,p,k,q,l,sigma=0):
  eid=len(edges)+1;edges.append(dict(kind=kind,source=vid[p,k],target=vid[q,l],sigma=sigma))
  return eid
 for p in ps:
  for k,t in enumerate(ts):
   for s in rotations(t):Fedges[p,k,ti[s]]=add('F',p,k,p,ti[s])
 for p in ps:
  for k,t in enumerate(ts):
   for i in cherries(t):
    q=H['swap'](p,i);Bedges[p,k,i]=add('B',p,k,q,k,i)
 paths={};forest=set()
 for p in ps:
  adj={k:[] for k in range(len(ts))}
  for (q,k,l),eid in Fedges.items():
   if q==p:adj[k].append((l,eid));adj[l].append((k,-eid))
  paths[p,root]=();todo=deque([root])
  while todo:
   k=todo.popleft()
   for l,eid in adj[k]:
    if (p,l) not in paths:paths[p,l]=paths[p,k]+(eid,);forest.add(abs(eid));todo.append(l)
 dictionary={}
 for p in ps:
  for i in range(1,m):
   k=min(k for k,t in enumerate(ts) if i in cherries(t))
   dictionary[p,i]=paths[p,k]+(Bedges[p,k,i],)+inv(paths[H['swap'](p,i),k])
 relations=[];types=[]
 for (p,k,l),eid in Fedges.items():
  if eid not in forest:relations.append(paths[p,k]+(eid,)+inv(paths[p,l]));types.append('associativity')
 for (p,k,i),eid in Bedges.items():
  word=paths[p,k]+(eid,)+inv(paths[H['swap'](p,i),k])
  if word!=dictionary[p,i]:relations.append(red(word+inv(dictionary[p,i])));types.append('cut-change naturality')
 def lift(p,w):
  out=[]
  for i in w:out.extend(dictionary[p,i]);p=H['swap'](p,i)
  return tuple(out)
 for r in ch[str(m+1)]['relations']:
  p=tuple(r['source']);relations.append(red(lift(p,r['left'])+inv(lift(p,r['right']))));types.append(r['type'])
 relations.append(lift(tuple(range(1,m+1)),H['full'](m)));types.append('outer boundary capping')
 def braid(w):return red((1 if e>0 else -1)*edges[abs(e)-1]['sigma'] for e in w if edges[abs(e)-1]['sigma'])
 def endpoints(w):
  first=edges[abs(w[0])-1];start=first['source'] if w[0]>0 else first['target'];at=start
  for e in w:
   edge=edges[abs(e)-1];u,v=(edge['source'],edge['target']) if e>0 else (edge['target'],edge['source'])
   assert at==u;at=v
  return start,at
 for w,typ in zip(relations,types):
  assert endpoints(w)[0]==endpoints(w)[1]
  assert H['eq'](m,braid(w),H['full'](m) if typ=='outer boundary capping' else ())
 for (p,i),w in dictionary.items():assert braid(w)==(i,)
 counts=[len(objects),len(Fedges),len(Bedges),len(relations)]
 print('M0,%d:'%(m+1),'objects,F,B,relations=',counts,'all maps/relations verified')
 data[str(m+1)]=dict(shapes=ts,objects=objects,arrows=edges,relations=[dict(word=w,type=t) for w,t in zip(relations,types)],inverse_chamber_dictionary=[dict(source=p,sigma=i,word=w) for (p,i),w in dictionary.items()],counts=counts)
(P/'b_parenthesized.json').write_text(json.dumps(data,indent=2)+'\n')
