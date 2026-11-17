"""Exact integral Q6 cusp/action certificate reconstructed after recovery.

Loads only the restored pre-affine prefix of the actual Q6 graph module.
Checks GR(4,3) monomial identities, literal c action, integral cusp rank,
and all 7^4 admissible translated s-frame heads. No full norm or central
layer is inferred from enumeration; the action-square theorem is proved
in research_A57_integral_norm.txt.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
from itertools import product
src=Path(__file__).resolve().parents[2]/'work_A/check_Q6_forced_frame.py'
s=src.read_text();marker='if frank(RES)==8:'
assert s.count(marker)==1
G={'__file__':str(src),'__name__':'_integral_q6_source'}
with redirect_stdout(StringIO()):exec(compile(s.split(marker)[0],str(src),'exec'),G)
# O=Z4[X]/(X^3+X+1), coefficients in base4.
def coeff(a):return[a&3,(a>>2)&3,(a>>4)&3]
def enc(a):return sum((x%4)<<(2*i)for i,x in enumerate(a))
def add(a,b):return enc([x+y for x,y in zip(coeff(a),coeff(b))])
def neg(a):return enc([-x for x in coeff(a)])
def mult(a,b):
 aa,bb=coeff(a),coeff(b);v=[0]*5
 for i,x in enumerate(aa):
  for j,y in enumerate(bb):v[i+j]+=x*y
 for j in (4,3):v[j-3]-=v[j];v[j-2]-=v[j]
 return enc(v[:3])
ADD=[[add(a,b)for b in range(64)]for a in range(64)]
MUL=[[mult(a,b)for b in range(64)]for a in range(64)]
NEG=[neg(a)for a in range(64)]
def power(a,n):
 v=1
 while n:
  if n&1:v=MUL[v][a]
  a=MUL[a][a];n//=2
 return v
def red(a):return sum((v&1)<<i for i,v in enumerate(coeff(a)))
zeta=power(4,8)
assert power(zeta,7)==1 and zeta!=1
TEICH={0:0}
for j in range(7):TEICH[G['zz'][j]]=power(zeta,j)
assert len(TEICH)==8 and all(red(v)==k for k,v in TEICH.items())
assert all(MUL[TEICH[a]][TEICH[b]]==TEICH[G['fm'](a,b)]for a in range(8)for b in range(8))
INV={a:power(a,13)for a in range(64)if red(a)}
assert all(MUL[a][b]==1 for a,b in INV.items())
def mon(cs):
 pp=[];ww=[]
 for col in cs:
  nz=[i for i,a in enumerate(col)if a];assert len(nz)==1
  i=nz[0];pp.append(i);ww.append(TEICH[col[i]])
 return tuple(pp),tuple(ww)
def compose(A,B):
 pa,wa=A;pb,wb=B
 return tuple(pa[j]for j in pb),tuple(MUL[wa[pb[i]]][wb[i]]for i in range(36))
ID=(tuple(range(36)),(1,)*36)
def mpow(A,n):
 out=ID
 while n:
  if n&1:out=compose(out,A)
  A=compose(A,A);n//=2
 return out
S,R,T,C,BETA=[mon(G[n])for n in ('S','R','T','CV','BETA')]
assert compose(S,S)==ID and mpow(R,3)==ID and compose(C,C)==ID
assert compose(C,compose(S,C))==S
assert compose(C,compose(R,C))==compose(S,compose(mpow(R,2),S))
assert T==compose(S,R) and compose(C,compose(T,C))==mpow(T,41)
assert mpow(T,42)==ID

def vec(i,n=36):return tuple(int(j==i)for j in range(n))
VB=[vec(i)for i in range(36)];ZERO=(0,)*36
def vadd(a,b):return tuple(ADD[x][y]for x,y in zip(a,b))
def vneg(a):return tuple(NEG[x]for x in a)
def vsub(a,b):return vadd(a,vneg(b))
def scale(a,v):return tuple(MUL[a][x]for x in v)
def apply(A,v):
 p,w=A;out=[0]*36
 for i,a in enumerate(v):out[p[i]]=MUL[w[i]][a]
 return tuple(out)
def orbit_data(A):
 p,w=A;seen=set();out=[]
 for start in range(36):
  if start in seen:continue
  o=[];j=start;phase=1
  while j not in o:o.append(j);phase=MUL[phase][w[j]];j=p[j]
  assert j==start;seen.update(o);out.append((o,phase))
 return out
so=orbit_data(S);assert sum(len(o)==1 for o,p in so)==4 and sum(len(o)==2 for o,p in so)==16
assert all(p==1 for o,p in so)
to=orbit_data(T);good=[o for o,p in to if p==1]
assert len(good)==4

def fixed_vector(A,o):
 p,w=A;v=[0]*36;v[o[0]]=1
 for j in o[:-1]:v[p[j]]=MUL[w[j]][v[j]]
 assert apply(A,tuple(v))==tuple(v)
 return tuple(v)
def coinvariant_functional(A,o):
 p,w=A;l=[0]*36;l[o[0]]=1
 for j in o[:-1]:l[p[j]]=MUL[INV[w[j]]][l[j]]
 assert MUL[w[o[-1]]][l[p[o[-1]]]]==l[o[-1]]
 return tuple(l)
TF=[fixed_vector(T,o)for o in good]
TL=[coinvariant_functional(T,o)for o in good]
def dot(a,b):
 z=0
 for x,y in zip(a,b):z=ADD[z][MUL[x][y]]
 return z
def cusp(v):return tuple(dot(l,v)for l in TL)
assert all(apply(C,v)==v for v in TF)
assert all(cusp(apply(C,vec(o[0])))==vec(i,4)for i,o in enumerate(good))
assert all(cusp(apply(T,v))==cusp(v)for v in VB)

# Integral normalized cocycles: s-value0, r-value in the order-three norm kernel.
R2=mpow(R,2)
def rproj(v):return vsub(v,scale(3,vadd(vadd(v,apply(R,v)),apply(R2,v))))
RC=[]
for v in VB:
 w=rproj(v)
 if G['frank']([tuple(red(x)for x in a)for a in RC+[w]])>len(RC):RC.append(w)
assert len(RC)==24
SF=[fixed_vector(S,o)for o,p in so]
DC=[vsub(v,apply(R,v))for v in SF]
assert len(SF)==20 and G['frank']([tuple(red(x)for x in v)for v in DC])==20
assert all(cusp(apply(S,v))==(0,)*4 for v in DC)
EF=[];EFc=[]
for v in RC:
 cv=cusp(apply(S,v))
 if G['frank']([tuple(red(x)for x in a)for a in EFc+[cv]])>len(EFc):EF.append(v);EFc.append(cv)
assert len(EF)==4
assert G['frank']([tuple(red(x)for x in a)for a in DC+EF])==24

def solve(cols,target):
 # Full column rank modulo2; every pivot used is a unit.
 rows=[list(row)+[t]for row,t in zip(zip(*cols),target)];n=len(cols);pivs=[];k=0
 for j in range(n):
  ii=next((i for i in range(k,len(rows))if red(rows[i][j])),None)
  assert ii is not None
  rows[k],rows[ii]=rows[ii],rows[k];rows[k]=list(scale(INV[rows[k][j]],rows[k]))
  for i in range(len(rows)):
   if i!=k and rows[i][j]:rows[i]=list(vsub(rows[i],scale(rows[i][j],rows[k])))
  pivs.append(j);k+=1
 assert all(not any(row[:-1]) and row[-1]==0 for row in rows[k:])
 out=tuple(rows[i][-1]for i in range(n));v=(0,)*len(target)
 for a,col in zip(out,cols):v=vadd(v,scale(a,col))
 assert v==target
 return out
# c action on normalized cocycle r-values is -C S R^-1.
for v in EF:
 cv=vneg(apply(C,apply(S,apply(R2,v))))
 solve(DC,vadd(cv,v))
 assert cusp(apply(S,cv))==tuple(NEG[x]for x in cusp(apply(S,v)))

# All admissible translated s-frame heads, using the actual four-dimensional
# F7 space and the actual character action. This checks the monomial2-group
# stabilizer argument; it does not solve the extra central extension.
nb=G['allowed_translations'];assert len(nb)==4
beta_perm=BETA[0];tested=0;orbit_counts=set()
for aa in product(range(7),repeat=4):
 nn=tuple(sum(aa[j]*nb[j][i]for j in range(4))%7 for i in range(13))
 ww=[]
 for j in range(36):
  k=beta_perm[j];ex=sum(x*y for x,y in zip(G['chars'][k],nn))%7
  ww.append(power(zeta,ex))
 BH=(beta_perm,tuple(ww));D=compose(BH,C)
 assert compose(D,D)==ID and compose(S,D)==compose(D,S)
 group=[ID,S,D,compose(S,D)]
 # Every point stabilizer scalar is literally1, as required for an
 # integral orbitwise permutation basis and invariant reduction.
 assert all(A[1][j]==1 for A in group for j in range(36)if A[0][j]==j)
 seen=set();orbs=[]
 for j in range(36):
  if j in seen:continue
  o={A[0][j]for A in group};seen|=o;orbs.append(o)
 orbit_counts.add(len(orbs));tested+=1
assert tested==2401
print('GR(4,3) Teichmuller generator:',coeff(zeta),'order7; all field scalars lift multiplicatively: PASS')
print('Actual integral S2=R3=C2=1, C R C=S R^-1 S, and C T C=T^-1: PASS')
print('s orbits:4 fixed lines and16 pairs; invariant free rank20')
print('tau cycles (length,phase):',[(len(o),coeff(p))for o,p in to])
print('tau admissible cycles4; invariant and coinvariant free rank4')
print('Literal integral C identity on all4 cusp invariant/coinvariant lines: PASS')
print('Normalized r-cocycles rank24, s-fixed coboundaries rank20, cusp determinant a unit: PASS')
print('Actual coefficient-twisted c acts as MINUS identity on integral free cusp cohomology: PASS')
print('All',tested,'admissible translated beta heads have commuting monomial involutions with trivial stabilizer scalars; orbit counts',sorted(orbit_counts))
print('Integral joint-invariant reduction for the s-frame head: PASS')
print('Scope: coefficient/head certificate; full square proof is separate; no new central-layer norm asserted.')
