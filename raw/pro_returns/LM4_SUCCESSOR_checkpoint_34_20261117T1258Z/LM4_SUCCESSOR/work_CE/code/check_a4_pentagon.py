"""Complete finite A4 pentagon test, with genuine P4 Artin relations.
Every proper subgroup of A4 is abelian. A commutator word therefore vanishes
on nongenerating pairs. Four Aut(A4)=S4 orbits of generating pairs carry eight
F2 coordinates. We impose every P4->A4 pentagon relation, without claiming
that an admissible evaluation tuple lifts to a full pentagon word.
"""
from itertools import permutations,product
from collections import Counter
P=list(permutations(range(4)));identity=tuple(range(4))
def compose(a,b):return tuple(a[b[i]] for i in range(4))
def inverse(a):return tuple(a.index(i) for i in range(4))
def parity(a):return sum(a[i]>a[j] for i in range(4) for j in range(i+1,4))%2
def cyc(*cs):
 a=identity
 for cc in cs:
  b=list(identity)
  for i,j in zip(cc,cc[1:]+cc[:1]):b[i-1]=j-1
  a=compose(a,tuple(b))
 return a
G=[g for g in P if not parity(g)];ix={g:i for i,g in enumerate(G)};one=ix[identity]
mul=[[ix[compose(a,b)] for b in G] for a in G];inv=[ix[inverse(a)] for a in G]
con=[[mul[mul[a][b]][inv[a]] for b in range(12)] for a in range(12)]
comm=[[mul[mul[mul[a][b]][inv[a]]][inv[b]] for b in range(12)] for a in range(12)]
V=[one,ix[cyc((1,2),(3,4))],ix[cyc((1,3),(2,4))],ix[cyc((1,4),(2,3))]]
# V[3]=V[1]*V[2], so its list index is its two-bit coordinate.
assert mul[V[1]][V[2]]==V[3]
vcoord={g:i for i,g in enumerate(V)}
autos=[[ix[compose(compose(h,g),inverse(h))] for g in G] for h in P]
def gen(a,b):
 h={one};todo=[one]
 while todo:
  q=todo.pop()
  for t in (a,b):
   v=mul[q][t]
   if v not in h:h.add(v);todo.append(v)
 return len(h)
canonical=[];evalmap={}
for a,b in product(range(12),repeat=2):
 if (a,b) in evalmap:continue
 if gen(a,b)<12:
  assert comm[a][b]==one
  evalmap[a,b]=(0,0);continue
 j=len(canonical);canonical.append((a,b))
 for au in autos:
  pair=(au[a],au[b]);outs=[vcoord[au[V[1]]],vcoord[au[V[2]]]]
  # rows express each of the two output bits in the 8 input bits.
  rows=[sum(((outs[t]>>bit)&1)<<(2*j+t) for t in range(2)) for bit in range(2)]
  if pair in evalmap:assert evalmap[pair]==tuple(rows)
  evalmap[pair]=tuple(rows)
assert len(canonical)==4 and len(evalmap)==144
print('Canonical generating-pair orbits (permutations in one-line notation):')
for j,(a,b) in enumerate(canonical):print(j,G[a],G[b])
relations=set();count=0;representations=[]
# P3 relations first, then the nine F3 action relations.
for a,b,c in product(range(12),repeat=3):
 if con[inv[a]][b]!=con[mul[b][c]][b] or con[inv[a]][c]!=con[b][c]:continue
 for d,e,f in product(range(12),repeat=3):
  if con[inv[a]][f]!=f or con[inv[c]][d]!=d:continue
  if con[inv[a]][d]!=con[mul[d][e]][d] or con[inv[a]][e]!=con[d][e]:continue
  if con[inv[b]][d]!=con[mul[d][f]][d] or con[inv[b]][f]!=con[d][f]:continue
  if con[inv[b]][e]!=con[comm[d][f]][e]:continue
  if con[inv[c]][e]!=con[mul[e][f]][e] or con[inv[c]][f]!=con[e][f]:continue
  count+=1;representations.append((a,b,c,d,e,f))
  terms=[(a,mul[c][e]),(mul[b][c],f),(c,f),(mul[a][b],mul[e][f]),(a,c)]
  row=[0,0]
  for pair in terms:
   rr=evalmap[pair];row[0]^=rr[0];row[1]^=rr[1]
  relations.update(row)
print('Hom(P4,A4) count:',count)
relations.discard(0)
solutions=[v for v in range(256) if all((r&v).bit_count()%2==0 for r in relations)]
print('Nonzero relation masks:',sorted(relations))
print('Number of pentagon-admissible coordinate assignments:',len(solutions))
def eval_u(a,b,v):
 rr=evalmap[a,b];bits=sum(((rr[i]&v).bit_count()%2)<<i for i in range(2));return V[bits]
x=ix[cyc((2,3,4))];y=ix[cyc((1,2,4))];u=ix[cyc((1,3),(2,4))];sig=cyc((2,4))
assert gen(x,y)==12 and con[inv[u]][y]==x
assert compose(compose(sig,G[x]),sig)==G[inv[x]]
assert compose(compose(sig,G[y]),sig)==G[inv[y]]
assert compose(sig,G[u])==compose(G[u],sig)
allowed=Counter(eval_u(x,y,v) for v in solutions)
print('Possible u(x,y) at the specified collapse pair:',[(G[g],n) for g,n in allowed.items()])
bad=[v for v in solutions if eval_u(x,y,v)==u]
print('Specified collapsing u is allowed:',bool(bad),'assignments:',bad)
# Independently impose the full two-cycle at every pair.
dual=[v for v in solutions if all(mul[eval_u(a,b,v)][eval_u(b,a,v)]==one for a,b in product(range(12),repeat=2))]
print('Pentagon plus duality assignments:',len(dual),'collapsing assignments:',[v for v in dual if eval_u(x,y,v)==u])
print('Generating substituted pairs for every A4 pair:',[v for v in solutions if all(gen(a,con[inv[eval_u(a,b,v)]][b])==12 for a,b in product(range(12),repeat=2) if gen(a,b)==12)])

# Verify that all eight coordinates are attained by actual commutator words:
# conjugates of [x,y] by x^i y^j span the entire evaluation module.
def coord_tuple(vals):return sum(vcoord[g]<<(2*j) for j,g in enumerate(vals))
orbit=[]
for i,j in product(range(3),repeat=2):
 vals=[]
 for a,b in canonical:
  h=one
  for _ in range(i):h=mul[h][a]
  for _ in range(j):h=mul[h][b]
  vals.append(con[h][comm[a][b]])
 orbit.append(coord_tuple(vals))
span={0}
for v in orbit:span|={u^v for u in list(span)}
print('Actual F-prime evaluation image size:',len(span));assert len(span)==256

# Exact finite versions of the extra equations satisfied by the given alpha:
# f pentagon+duality+negative hexagon; alpha an involution; u=f alpha(u).
def alpha_pair(a,b,vf):
 ff=eval_u(a,b,vf)
 return inv[a],con[inv[ff]][inv[b]]
def negative_hex(vf):
 for a,b in product(range(12),repeat=2):
  z=inv[mul[a][b]];g=one
  for h in (eval_u(a,b,vf),inv[a],eval_u(z,a,vf),inv[z],eval_u(b,z,vf),inv[b]):g=mul[g][h]
  if g!=one:return False
 return True
fallowed=[]
for vf in dual:
 if not negative_hex(vf):continue
 if not all(gen(*alpha_pair(a,b,vf))==12 for a,b in canonical):continue
 if not all(mul[eval_u(a,b,vf)][eval_u(*alpha_pair(a,b,vf),vf)]==one for a,b in canonical):continue
 fallowed.append(vf)
print('Negative involution parameter assignments f:',fallowed)
fullfinite=[]
for vf,vu in product(fallowed,dual):
 if all(eval_u(a,b,vu)==mul[eval_u(a,b,vf)][eval_u(*alpha_pair(a,b,vf),vu)] for a,b in canonical):fullfinite.append((vf,vu))
print('Pairs (f,u) satisfying all finite equations:',len(fullfinite))
print('Such pairs with specified collapsing u(x,y):',[(vf,vu) for vf,vu in fullfinite if eval_u(x,y,vu)==u])
