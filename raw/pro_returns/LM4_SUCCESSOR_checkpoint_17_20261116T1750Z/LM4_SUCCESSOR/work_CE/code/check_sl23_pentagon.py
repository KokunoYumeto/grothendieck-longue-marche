"""Exact binary-tetrahedral refinement of check_a4_pentagon.py.
Central changes of x,y do not change any commutator-word value. Hence only
four central lift bits, plus the Q8 c2 bit, are needed above each A4 tuple.
Every P4 representation is checked using the actual Artin relations.
"""
from itertools import product
from collections import Counter
import importlib.util,io,contextlib
from pathlib import Path
sp=importlib.util.spec_from_file_location('a4',Path(__file__).with_name('check_a4_pentagon.py'))
A=importlib.util.module_from_spec(sp)
with contextlib.redirect_stdout(io.StringIO()):sp.loader.exec_module(A)

def mm(a,b):
 return ((a[0]*b[0]+a[1]*b[2])%3,(a[0]*b[1]+a[1]*b[3])%3,(a[2]*b[0]+a[3]*b[2])%3,(a[2]*b[1]+a[3]*b[3])%3)
def determinant(a):return(a[0]*a[3]-a[1]*a[2])%3
def mi(a):
 q=pow(determinant(a),-1,3);return(a[3]*q%3,-a[1]*q%3,-a[2]*q%3,a[0]*q%3)
SL=[a for a in product(range(3),repeat=4) if determinant(a)==1];GL=[a for a in product(range(3),repeat=4) if determinant(a)]
ix={a:i for i,a in enumerate(SL)};one=ix[(1,0,0,1)];minus=ix[(2,0,0,2)]
mul=[[ix[mm(a,b)] for b in SL] for a in SL];inv=[ix[mi(a)] for a in SL]
con=[[mul[mul[a][b]][inv[a]] for b in range(24)] for a in range(24)]
comm=[[mul[mul[mul[a][b]][inv[a]]][inv[b]] for b in range(24)] for a in range(24)]
points=[(1,0),(0,1),(1,1),(2,1)]
def projmat(a):
 out=[]
 for x,y in points:
  X=(a[0]*x+a[1]*y)%3;Y=(a[2]*x+a[3]*y)%3
  v=(1,0) if not Y else(X*pow(Y,-1,3)%3,1)
  out.append(points.index(v))
 return A.ix[tuple(out)]
proj=[projmat(a) for a in SL];lift={g:next(i for i,q in enumerate(proj) if q==g) for g in range(12)}
assert all(proj[mul[i][j]]==A.mul[proj[i]][proj[j]] for i,j in product(range(24),repeat=2))
I=lift[A.V[1]];J=lift[A.V[2]];section=[one,I,J,mul[I][J]]
assert mul[I][I]==mul[J][J]==minus
assert all(proj[section[i]]==A.V[i] for i in range(4))
autbyproj={}
for h in GL:
 au=[ix[mm(mm(h,g),mi(h))] for g in SL]
 key=tuple(proj[au[lift[g]]] for g in range(12))
 if key in autbyproj:assert autbyproj[key]==au
 autbyproj[key]=au
assert len(autbyproj)==24
pairorbit={}
for j,(a,b) in enumerate(A.canonical):
 for au4 in A.autos:
  key=(au4[a],au4[b]);entry=(j,autbyproj[tuple(au4)])
  if key in pairorbit:assert pairorbit[key]==entry
  pairorbit[key]=entry
solutions=A.solutions
# For each SL pair: one unknown central bit and all32 constant values.
mask={};const={}
for a,b in product(range(24),repeat=2):
 pa,pb=proj[a],proj[b]
 if (pa,pb) in pairorbit:
  j,au=pairorbit[pa,pb];mask[a,b]=1<<j
  ca,cb=A.canonical[j]
  const[a,b]=[au[section[A.vcoord[A.eval_u(ca,cb,v)]]] for v in solutions]
 else:
  assert comm[a][b] in (one,minus)
  mask[a,b]=(1<<4) if comm[a][b]==minus else 0
  const[a,b]=[one]*len(solutions)

def uval(a,b,j,bits):
 g=const[a,b][j]
 return mul[minus][g] if (mask[a,b]&bits).bit_count()%2 else g

def pure_ok(v):
 a,b,c,d,e,f=v
 return (con[inv[a]][b]==con[mul[b][c]][b] and con[inv[a]][c]==con[b][c]
 and con[inv[a]][f]==f and con[inv[c]][d]==d
 and con[inv[a]][d]==con[mul[d][e]][d] and con[inv[a]][e]==con[d][e]
 and con[inv[b]][d]==con[mul[d][f]][d] and con[inv[b]][f]==con[d][f]
 and con[inv[b]][e]==con[comm[d][f]][e]
 and con[inv[c]][e]==con[mul[e][f]][e] and con[inv[c]][f]==con[e][f])

rows=[];lifts=0;rhsbyrow={};inconsistent=0
for v4 in A.representations:
 v=tuple(lift[g] for g in v4)
 if not pure_ok(v):continue
 lifts+=1;a,b,c,d,e,f=v
 ps=[(a,mul[c][e]),(mul[b][c],f),(c,f),(mul[a][b],mul[e][f]),(a,c)]
 row=0
 for pair in ps:row^=mask[pair]
 rhs=0
 for j in range(len(solutions)):
  g=one
  for n in (0,1,4,3,2):
   t=const[ps[n]][j];g=mul[g][t if n<2 else inv[t]]
  assert g in (one,minus)
  if g==minus:rhs|=1<<j
 if row in rhsbyrow:inconsistent|=rhsbyrow[row]^rhs
 else:rhsbyrow[row]=rhs
print('Projective P4 representations admitting SL2(F3) lifts:',lifts)
print('Total Hom(P4,SL2(F3)):',lifts*64)
print('Distinct central pentagon row masks:',sorted(rhsbyrow))
pent=[]
for j,v in enumerate(solutions):
 if inconsistent>>j&1:continue
 for bits in range(32):
  if all(((row&bits).bit_count()%2)==(rhs>>j&1) for row,rhs in rhsbyrow.items()):pent.append((j,bits))
print('Full binary-tetrahedral pentagon assignments:',len(pent))
print('Counts by projective coordinate assignment:',dict(Counter(solutions[j] for j,bits in pent)))
collapse=lambda j:A.eval_u(A.x,A.y,solutions[j])==A.u
print('Pentagon assignments with the specified A4 collapse:',sum(collapse(j) for j,bits in pent))

# Check duality, negative hexagon, involutivity, and the actual norm equation.
allpairs=list(product(range(24),repeat=2))
def dual_ok(j,bits):return all(mul[uval(a,b,j,bits)][uval(b,a,j,bits)]==one for a,b in allpairs)
pent=[(j,bits) for j,bits in pent if dual_ok(j,bits)]
print('After full duality:',len(pent))
def alpha_pair(a,b,j,bits):
 ff=uval(a,b,j,bits);return inv[a],con[inv[ff]][inv[b]]
def neg_hex(j,bits):
 for a,b in allpairs:
  z=inv[mul[a][b]];g=one
  for h in (uval(a,b,j,bits),inv[a],uval(z,a,j,bits),inv[z],uval(b,z,j,bits),inv[b]):g=mul[g][h]
  if g!=one:return False
 return True
fa=[]
for j,bits in pent:
 if bits&16:continue # full negative GT coefficient c2(f)=0
 if solutions[j] not in A.fallowed:continue
 if not neg_hex(j,bits):continue
 if not all(mul[uval(a,b,j,bits)][uval(*alpha_pair(a,b,j,bits),j,bits)]==one for a,b in allpairs):continue
 fa.append((j,bits))
print('Lifted negative involution f assignments:',[(solutions[j],bits) for j,bits in fa])
compatible=[]
for jf,bf in fa:
 for ju,bu in pent:
  if all(uval(a,b,ju,bu)==mul[uval(a,b,jf,bf)][uval(*alpha_pair(a,b,jf,bf),ju,bu)] for a,b in allpairs):compatible.append((jf,bf,ju,bu))
print('Joint finite (f,u) assignments satisfying every equation:',len(compatible))
bad=[(solutions[jf],bf,solutions[ju],bu) for jf,bf,ju,bu in compatible if collapse(ju)]
print('Such joint assignments retaining the specified A4 collapse:',len(bad),bad)

# Realizability of the raw relative word coordinates: enumerate the normal
# closure of the joint commutator in Q8^4 times the last Q8 central factor.
qx=[lift[a] for a,b in A.canonical]+[I];qy=[lift[b] for a,b in A.canonical]+[J]
c0=tuple(comm[a][b] for a,b in zip(qx,qy));orb={c0};todo=[c0]
while todo:
 g=todo.pop()
 for q in (qx,qy):
  h=tuple(con[a][b] for a,b in zip(q,g))
  if h not in orb:orb.add(h);todo.append(h)
identity=(one,)*5;sub={identity};todo=[identity]
while todo:
 g=todo.pop()
 for h in orb:
  v=tuple(mul[a][b] for a,b in zip(g,h))
  if v not in sub:sub.add(v);todo.append(v)
print('Actual commutator-word joint image size:',len(sub),'ambient maximum:',8**4*2)
assert len(sub)==8**4*2

def all_a4_generate(ju):
 vu=solutions[ju]
 return all(A.gen(a,A.con[A.inv[A.eval_u(a,b,vu)]][b])==12 for a,b in A.canonical)
print('Projective u assignments after joint equations:',sorted({solutions[ju] for jf,bf,ju,bu in compatible}))
otherbad=[(solutions[jf],bf,solutions[ju],bu) for jf,bf,ju,bu in compatible if not all_a4_generate(ju)]
print('Joint assignments failing some A4 generation test:',len(otherbad),otherbad[:16])
print('Pentagon-only assignments failing some A4 generation test:',sum(not all_a4_generate(j) for j,bits in pent))
# Extract a single exact P4 relation witnessing the specified collapsed data
# cannot lift, preferably a row0 relation independent of every central bit.
base_bad_indices=[j for j,v in enumerate(solutions) if collapse(j)]
for v4 in A.representations:
 v=tuple(lift[g] for g in v4)
 if not pure_ok(v):continue
 a,b,c,d,e,f=v;ps=[(a,mul[c][e]),(mul[b][c],f),(c,f),(mul[a][b],mul[e][f]),(a,c)]
 row=0
 for pair in ps:row^=mask[pair]
 if row:continue
 allbad=True;vals=[]
 for j in base_bad_indices:
  g=one
  for n in (0,1,4,3,2):g=mul[g][const[ps[n]][j] if n<2 else inv[const[ps[n]][j]]]
  vals.append(g)
  if g!=minus:allbad=False;break
 if allbad:
  print('Single P4 witness matrices A12,A13,A23,A14,A24,A34:',[SL[g] for g in v])
  print('Witness projective images:',[A.G[g] for g in v4])
  print('Witness pentagon argument orbit masks:',[mask[pair] for pair in ps])
  print('Every specified collapsing assignment gives central defect -I independently of lifts:',True)
  break
else:print('No one row0 witness covers all eight collapsing assignments.')

# Separate the genuinely GT0 input from the pentagon input: do not infer
# their equivalence without checking every commutator-word coordinate.
all_a4_dual=[v for v in range(256) if all(A.mul[A.eval_u(a,b,v)][A.eval_u(b,a,v)]==A.one for a,b in product(range(12),repeat=2))]
print('All A4 duality assignments without pentagon:',len(all_a4_dual),'equal pentagon list:',all_a4_dual==solutions)
all_sl_dual=[(j,bits) for j in range(len(solutions)) for bits in range(32) if dual_ok(j,bits)]
print('All binary-tetrahedral duality assignments without pentagon:',len(all_sl_dual),'equal pentagon list:',all_sl_dual==pent)
assert all_a4_dual==solutions and all_sl_dual==pent
print('Therefore the all-A4 generation deduction uses duality, negative hexagon, involutivity, and coboundary only; full pentagon is unnecessary at this quotient.',True)
