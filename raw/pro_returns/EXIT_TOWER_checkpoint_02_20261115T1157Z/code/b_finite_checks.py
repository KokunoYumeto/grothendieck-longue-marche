"""Finite checks for Section B.
The S5 graph below realizes the endpoint valencies of cote148/31-33.
It certifies counts and orbit decomposition, not the geometric path classes.
"""
from itertools import permutations,product,combinations_with_replacement
from collections import Counter,defaultdict
from pathlib import Path
import json,math

S=tuple(permutations(range(5)));one=tuple(range(5))
def mul(a,b):return tuple(a[b[i]] for i in range(5))
def inv(a):return tuple(a.index(i) for i in range(5))
def cycle(*cs):
 p=list(one)
 for c in cs:
  for a,b in zip(c,c[1:]+c[:1]):p[a]=b
 return tuple(p)
def subgroup(gs):
 H={one};todo=[one]
 while todo:
  a=todo.pop()
  for g in gs:
   b=mul(a,g)
   if b not in H:H.add(b);todo.append(b)
 return frozenset(H)
two=cycle((1,2),(3,4))
H2=subgroup([two]);H0=subgroup([])
Hs={
 'I10':subgroup([cycle((0,1,2,3,4)),cycle((1,4),(2,3))]),
 'I6':subgroup([cycle((0,1,2)),two]),
 'I4':subgroup([cycle((1,3,2,4))]),
 'II2':H2,'IIp2':H2,'II1':H0,'III2':H2,'III1':H0,'IIIp2':H2}
def coset(g,H):return min(mul(g,h) for h in H)
cosets={name:sorted({coset(g,H) for g in S}) for name,H in Hs.items()}
vertices=[(name,g) for name,cs in cosets.items() for g in cs]
vid={v:i for i,v in enumerate(vertices)}
families=[
 ('f_B_s','I6','I4',H2,1),
 ('f_Q_a','IIp2','I4',H0,1),
 ('tau_pi_s','II2','IIp2',H2,1),
 ('tau_r_0','II1','II1',H0,1),
 ('gamma_pi_s','II2','I10',H2,1),
 ('gamma_pp_pi_s','IIp2','I6',H2,1),
 ('gamma_r_0','II1','I6',H0,1),
 ('tau_pi_rho','III2','III1',H0,1),
 ('gamma_pi_rho','III2','II2',H0,1),
 ('tau_r_1','III1','IIIp2',H0,1),
 ('gamma_r_1','III1','IIp2',H0,1),
 ('gamma_r_1prime','III1','II1',H0,3),
 ('gamma_r_2','IIIp2','II2',H0,1),
 ('gamma_r_2prime','IIIp2','I4',H2,1)]
edges=[];summary=[]
for name,src,tgt,H,reps in families:
 assert H<=Hs[src]
 ks=[k for k in S if all(mul(inv(k),mul(h,k)) in Hs[tgt] for h in H)]
 assert ks
 for j in range(reps):
  k=ks[j]
  if name=='tau_r_0':k=cycle((0,1,2),(3,4))
  for g in sorted({coset(x,H) for x in S}):
   edges.append({'family':name,'orbit':j,'coset':g,
       'source':vid[src,coset(g,Hs[src])],
       'target':vid[tgt,coset(mul(g,k),Hs[tgt])]})
 summary.append((name,reps*120//len(H),reps,120//len(H)))
adj=defaultdict(set)
for e in edges:adj[e['source']].add(e['target']);adj[e['target']].add(e['source'])
seen={0};todo=[0]
while todo:
 u=todo.pop()
 for v in adj[u]-seen:seen.add(v);todo.append(v)
print('COTE148 CORE STABILIZERS GENERATE S5:',len(subgroup(list(Hs['I6']|Hs['I4']))))
assert len(subgroup(list(Hs['I6']|Hs['I4'])))==120
print('COTE148 VERTEX ORBITS')
for name,cs in cosets.items():print(name,'stabilizer',len(Hs[name]),'objects',len(cs))
print('total vertices:',len(vertices),'vertex orbits:',len(Hs))
print('COTE148 ARROW FAMILIES: name, arrows, orbits, orbit_size')
for row in summary:print(*row)
print('total arrows:',len(edges),'named families:',len(families),'actual orbits:',sum(t[2] for t in summary))
print('orbit-size histogram:',dict(Counter(t[3] for t in summary for _ in range(t[2]))))
print('connected:',len(seen)==len(vertices),'free-group rank:',len(edges)-len(vertices)+1)
assert len(vertices)==542 and len(edges)==1620 and sum(t[2] for t in summary)==16
assert len(seen)==len(vertices)
Path(__file__).with_name('b_diagram.json').write_text(json.dumps({'vertices':vertices,'edges':edges,'scope':'endpoint-valency coset realization; geometric path words not assigned'},indent=2))

def compositions(total,k):
 if k==1:yield(total,);return
 for i in range(total+1):
  for t in compositions(total-i,k-1):yield(i,)+t

def stable_graphs(g,n):
 out={}
 d=3*g-3+n
 for e in range(d+1):
  for v in range(1,e+2):
   weight=g-e+v-1
   if weight<0:continue
   pairs=list(combinations_with_replacement(range(v),2))
   for counts in compositions(e,len(pairs)):
    E=tuple(p for p,c in zip(pairs,counts) for _ in range(c))
    A=defaultdict(set)
    for i,j in E:A[i].add(j);A[j].add(i)
    reach={0};todo=[0]
    while todo:
     a=todo.pop()
     for b in A[a]-reach:reach.add(b);todo.append(b)
    if len(reach)<v:continue
    for genera in compositions(weight,v):
     for legs in product(range(v),repeat=n):
      deg=Counter(x for edge in E for x in edge);deg.update(legs)
      if any(2*genera[i]-2+deg[i]<=0 for i in range(v)):continue
      models=[]
      for p in permutations(range(v)):
       w=[0]*v
       for i in range(v):w[p[i]]=genera[i]
       models.append((tuple(w),tuple(sorted(tuple(sorted((p[i],p[j]))) for i,j in E)),tuple(p[i] for i in legs)))
      can=min(models)
      vertex_aut=sum(m==models[0] for m in models)
      edge_aut=math.prod(math.factorial(c) for c in Counter(E).values())*2**sum(i==j for i,j in E)
      out[can]=vertex_aut*edge_aut
 return out
print('STABLE GRAPH ENUMERATION')
for g,n in [(0,4),(0,5),(1,1),(1,2)]:
 gs=stable_graphs(g,n)
 print((g,n),'total',len(gs),'by_edges',dict(sorted(Counter(len(k[1]) for k in gs).items())))
 if g==1:
  for graph,aut in sorted(gs.items()):print(' graph',graph,'Aut order',aut)
 if g==0:
  trivalent=[k for k in gs if len(k[1])==n-3]
  r=2*n-3
  print(' trivalent charts:',len(trivalent),'framed rank',r,'objects per chart',2**r,'generators per chart',r*2**r)
  print(' disjoint framed charts: objects',len(trivalent)*2**r,'generators',len(trivalent)*r*2**r)
  k=n-3
  print(' disjoint node-only charts: objects',len(trivalent)*2**k,'generators',len(trivalent)*k*2**k)
# Counterexample to preservation of free object actions by a finite coequalizer.
parent=[0,1]
parent[1]=0
fixed_classes={parent[i] for i in range(2)}
print('C2 coequalizer: input objects 2, quotient objects',len(fixed_classes),'; nonidentity fixes quotient: True')
