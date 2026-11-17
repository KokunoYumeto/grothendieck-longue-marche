"""Exact transported half-twist equations and free-subgroup comparisons."""
from pathlib import Path
import json,itertools,hashlib
ROOT=Path(__file__).resolve().parents[2];CE=ROOT/'work_CE'
P=ROOT/'work_DE/next_marginal_source/remaining_pencil_braids.json';D=json.loads(P.read_text())
B=json.loads((CE/'four_triple_normality_gap.json').read_text())
def red(w):
 o=[]
 for x in w:
  if o and o[-1]==-x:o.pop()
  else:o.append(x)
 return tuple(o)
def iv(w):return tuple(-x for x in w[::-1])
def mul(*ws):return red(itertools.chain.from_iterable(ws))
def sub(w,A):return mul(*(A[x] if x>0 else iv(A[-x]) for x in w))
def cj(h,w):return mul(h,w,iv(h))
def art(w):
 A={i:(i,) for i in range(1,21)}
 for x in w:
  i=abs(x);a,b=A[i],A[i+1]
  A[i],A[i+1]=(mul(a,b,iv(a)),a) if x>0 else (b,mul(iv(b),a,b))
 return A
def cy(w):
 j=0
 while len(w)-2*j>1 and w[j]==-w[-j-1]:j+=1
 return w[:j],w[j:len(w)-j]
class Stallings:
 def __init__(self,words):
  E=[];n=1
  for w in words:
   v=0
   for j,l in enumerate(w):
    q=0 if j==len(w)-1 else n
    if q:n+=1
    E.extend([(v,l,q),(q,-l,v)]);v=q
  p=list(range(n))
  def root(a):
   while p[a]!=a:p[a]=p[p[a]];a=p[a]
   return a
  while True:
   T={};changed=False
   for a,l,b in E:
    a,b=root(a),root(b)
    if (a,l) in T:
     c=root(T[a,l])
     if b!=c:p[max(b,c)]=min(b,c);changed=True
    else:T[a,l]=b
   if not changed:break
  self.base=root(0);self.T={(root(a),l):root(b) for a,l,b in E}
  vs={self.base}|{a for a,l in self.T}|set(self.T.values())
  self.vertices=len(vs);self.edges=len(self.T)//2;self.rank=self.edges-self.vertices+1
  assert all(self.T.get((b,-l))==a for (a,l),b in self.T.items())
  assert all(self.contains(w) for w in words)
 def contains(self,w):
  v=self.base
  for l in w:
   if (v,l) not in self.T:return False
   v=self.T[v,l]
  return v==self.base
 def record(self):return {'vertices':self.vertices,'edges':self.edges,'rank':self.rank,'base':self.base,'edges_directed':[[a,l,b] for (a,l),b in sorted(self.T.items())]}
new={i:(i,) for i in range(1,21)};new[10]=(10,-11)
rows=[]
for row in D['loops']:
 if not row['name'].startswith('discriminant_'):continue
 local=mul(*(v['word'] for v in row['forward_segments'][1:]));prefix,core=cy(local)
 assert len(core)==1 and core[0]>0
 assert art(local)==art(mul(prefix,core,iv(prefix)))
 A=art(mul(row['forward_segments'][0]['word'],prefix));pos=[core[0],core[0]+1]
 ms=[sub(A[i],new) for i in pos];hs=[cy(m) for m in ms]
 assert all(len(core)==1 for h,core in hs)
 k=mul(iv(hs[0][0]),hs[1][0]);bs=[i for i,x in enumerate(k) if abs(x)==11];assert len(bs)==1
 j=bs[0];left,right=k[:j],k[j+1:];eps=k[j]//11
 if eps==1: V=cj(right,hs[1][1]);W=cj(iv(left),hs[0][1])
 else: V=cj(iv(left),hs[0][1]);W=cj(right,hs[1][1])
 assert all(abs(x)!=11 for x in V+W)
 rows.append({'name':row['name'],'local_positions':pos,'meridians':ms,'core_generators':[x[1][0] for x in hs],
              'arc':k,'b_sign':eps,'domain_V':V,'range_W':W})
phi={int(k):tuple(v) for k,v in B['nielsen_basis'].items()}
Avec=[(10,)]+[phi[i] for i in [6,12,1,19,20,2,15,9]]
Vs=[r['domain_V'] for r in rows];Ws=[r['range_W'] for r in rows]
GV=Stallings(Avec+Vs);GW=Stallings(Avec+Ws)
GVall=Stallings(Avec+Vs+[(7,),(14,)]);GWall=Stallings(Avec+Ws+[(7,),(14,)])
res={'scope':'Exact eight transported half-twist equations b V_i b^-1=W_i; free-group comparisons before other global relations.',
 'input_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'rows':rows,
 'domain':GV.record(),'range':GW.record(),
 'domain_contains_range':[GV.contains(w) for w in Ws],'range_contains_domain':[GW.contains(v) for v in Vs],
 'domain_plus_zero_generators':GVall.record(),'range_plus_zero_generators':GWall.record()}
(CE/'discriminant_partial_hnn.json').write_text(json.dumps(res,indent=2)+'\n')
for r in rows: print(r['name'],'cores',r['core_generators'],'arc length',len(r['arc']),'single b sign',r['b_sign'],'V/W lengths',len(r['domain_V']),len(r['range_W']))
for n,g in [('domain',GV),('range',GW),('domain+zeros',GVall),('range+zeros',GWall)]:print(n,'vertices',g.vertices,'edges',g.edges,'rank',g.rank)
print('domain contains range:',res['domain_contains_range'])
print('range contains domain:',res['range_contains_domain'])
print('PASS: literal half-twist actions, unique-b arc factorization, folded inverse graphs and all input memberships.')
