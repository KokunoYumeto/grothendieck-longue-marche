"""Exact rational test of the full pentagon in Heisenberg ⋊ C2^2.
All computations use the actual Cohen Artin presentation of P4 and the
rank-five Schreier basis of ker(F2 -> C2^2). This is a finite-dimensional
relative class-two calculation, not a construction of a full pentagon word.
"""
from itertools import product,combinations
from fractions import Fraction as Q
from collections import Counter
from pathlib import Path
import importlib.util
import sympy as S
keys=[(1,2),(1,3),(2,3),(1,4),(2,4),(3,4)]
# (X,Y,Z,epsilon_X,epsilon_Y); Heisenberg uses BCH coordinates.
E=(Q(0),Q(0),Q(0),0,0)
def mul(a,b):
 x,y,z,i,j=a;X,Y,Z,I,J=b
 sx=(-1)**i;sy=(-1)**j
 return (x+sx*X,y+sy*Y,z+sx*sy*Z+(x*sy*Y-y*sx*X)/2,(i+I)%2,(j+J)%2)
def inv(a):
 x,y,z,i,j=a;return(-(-1)**i*x,-(-1)**j*y,-(-1)**(i+j)*z,i,j)
def conj(a,b):return mul(mul(a,b),inv(a))
def comm(a,b):return mul(mul(mul(a,b),inv(a)),inv(b))
def word(*args):
 g=E
 for a in args:g=mul(g,a)
 return g

def defects(q):
 out=[]
 for j in (3,4):
  for r in range(1,j):
   for s in range(r+1,j):
    g=q[r,s]
    for i in range(1,j):
     v=q[i,j]
     if i<r or s<i:rhs=v
     elif s==i:rhs=conj(q[r,j],v)
     elif r==i:rhs=conj(mul(q[r,j],q[s,j]),v)
     else:rhs=conj(comm(q[r,j],q[s,j]),v)
     lhs=conj(inv(g),v)
     assert lhs[3:]==rhs[3:]
     out.append(tuple(lhs[k]-rhs[k] for k in range(3)))
 return out

def scalar_matrix(eps):
 cols=[]
 for j in range(6):
  vals=[(Q(int(i==j)),Q(0),Q(0),eps[i],0) for i in range(6)]
  cols.append([d[0] for d in defects(dict(zip(keys,vals)))])
 return S.Matrix(list(zip(*cols)))

def frac(x):return Q(int(S.numer(x)),int(S.denom(x)))
chars={};matrices={}
for eps in product(range(2),repeat=6):
 M=scalar_matrix(eps);matrices[eps]=M;basis=M.nullspace()
 if not any(eps):chars[eps]=[[frac(x) for x in v] for v in basis]
 else:
  cob=S.Matrix([int(e) for e in eps]);chosen=[];span=[cob]
  for v in basis:
   if S.Matrix.hstack(*(span+[v])).rank()>len(span):span.append(v);chosen.append([frac(x) for x in v])
  if chosen:chars[eps]=chosen
print('Characters contributing H1:',len(chars),'total dimension:',sum(map(len,chars.values())))

pairs=list(combinations(range(5),2));mons=list(combinations(range(3),2))
quad=[(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]
width=19

def uvalue(a,b):
 aa=inv(a);bb=inv(b)
 basis=[word(a,a),word(b,a,bb,aa),word(b,b),word(a,b,a,bb),word(a,b,b,aa)]
 assert all(g[3:]==(0,0) for g in basis)
 vx=[basis[0][0]-basis[3][0],basis[1][0],basis[2][0]-basis[4][0]]
 vy=[basis[0][1]-basis[3][1],basis[1][1],basis[2][1]-basis[4][1]]
 z=[basis[0][2]-basis[3][2],basis[1][2],basis[2][2]-basis[4][2]]
 z += [basis[i][0]*basis[j][1]-basis[i][1]*basis[j][0] for i,j in pairs]
 return vx,vy,z

def detpoly(a,b):
 ax,ay=a;bx,by=b;out=[Q(0)]*6
 for i in range(3):
  for j in range(3):out[quad.index(tuple(sorted((i,j))))]+=ax[i]*by[j]-ay[i]*bx[j]
 return out

def pentagon_rows(vals):
 a,b,c,d,e,f=vals
 us=[uvalue(a,mul(c,e)),uvalue(mul(b,c),f),uvalue(c,f),uvalue(mul(a,b),mul(e,f)),uvalue(a,c)]
 seq=[(us[0],1),(us[1],1),(us[4],-1),(us[3],-1),(us[2],-1)]
 vx=[Q(0)]*3;vy=[Q(0)]*3;z=[Q(0)]*13;zz=[Q(0)]*6
 for (x,y,t),sign in seq:
  xx=[sign*v for v in x];yy=[sign*v for v in y]
  dxy=detpoly((vx,vy),(xx,yy));zz=[u+v/2 for u,v in zip(zz,dxy)]
  vx=[u+v for u,v in zip(vx,xx)];vy=[u+v for u,v in zip(vy,yy)];z=[u+sign*v for u,v in zip(z,t)]
 return [vx+[Q(0)]*16,vy+[Q(0)]*16,z+zz]

rows=[];data=[];counts=Counter();maxden=1
for eps,rb in chars.items():
 for eta,sb in chars.items():
  epz=tuple((a+b)%2 for a,b in zip(eps,eta));M=matrices[epz]
  for rr in rb:
   for ss in sb:
    vals=[(rr[i],ss[i],Q(0),eps[i],eta[i]) for i in range(6)]
    ds=defects(dict(zip(keys,vals)))
    assert all(dx==dy==0 for dx,dy,dz in ds)
    rhs=S.Matrix([-dz for dx,dy,dz in ds])
    try:sol,params=M.gauss_jordan_solve(rhs)
    except ValueError:counts['obstructed']+=1;continue
    sol=sol.subs({t:0 for t in params});zs=[frac(z) for z in sol]
    vals=[(rr[i],ss[i],zs[i],eps[i],eta[i]) for i in range(6)]
    assert all(d==(0,0,0) for d in defects(dict(zip(keys,vals))))
    ps=pentagon_rows(vals)
    nz=[row for row in ps if any(row)]
    for row in nz:
     maxden=max(maxden,*[x.denominator for x in row]);rows.append(row);data.append((eps,eta,rr,ss,zs))
    counts['valid']+=1
    counts['valid_both_nontrivial' if any(eps) and any(eta) else 'valid_some_trivial']+=1
    if any(eps) and any(eta) and eps!=eta:counts['valid_distinct_nontrivial']+=1
    if nz:counts['nonzero_rows']+=len(nz)

# Complete the mixed trivial/nontrivial character families by solving their
# bilinear obstruction as a linear system in the six trivial-character
# coordinates. Also vary every central cocycle in the nontrivial families.
for side in (0,1):
 for eps1,basis1 in chars.items():
  if not any(eps1):continue
  fixed=basis1[0];eps=eps1 if side==0 else (0,)*6;eta=(0,)*6 if side==0 else eps1
  epz=eps1;M=matrices[epz];dcols=[]
  for j in range(6):
   variable=[Q(int(i==j)) for i in range(6)]
   rr,ss=(fixed,variable) if side==0 else (variable,fixed)
   vals=[(rr[i],ss[i],Q(0),eps[i],eta[i]) for i in range(6)]
   dcols.append([d[2] for d in defects(dict(zip(keys,vals)))])
  block=S.Matrix.hstack(S.Matrix(list(zip(*dcols))),M)
  for v in block.nullspace():
   variable=[frac(x) for x in v[:6]];zs=[frac(x) for x in v[6:]]
   rr,ss=(fixed,variable) if side==0 else (variable,fixed)
   vals=[(rr[i],ss[i],zs[i],eps[i],eta[i]) for i in range(6)]
   assert all(d==(0,0,0) for d in defects(dict(zip(keys,vals))))
   for row in pentagon_rows(vals):
    if any(row):rows.append(row);data.append(('mixed_complete',eps,eta,rr,ss,zs))
   counts['mixed_complete_representatives']+=1
# Central-cocycle changes alter the polynomial linearly; their separate
# zero-vector representations suffice to supply every such difference.
for eps in product(range(2),repeat=6):
 for zvec in matrices[eps].nullspace():
  zs=[frac(x) for x in zvec]
  vals=[(Q(0),Q(0),zs[i],eps[i],0) for i in range(6)]
  assert all(d==(0,0,0) for d in defects(dict(zip(keys,vals))))
  for row in pentagon_rows(vals):
   if any(row):rows.append(row);data.append(('central_cocycle',eps,zs))
  counts['central_cocycle_representatives']+=1

print('Representation counts:',dict(counts),'maximum row denominator:',maxden)
M=S.Matrix(rows) if rows else S.zeros(0,width)
print('Constraint matrix shape',M.shape,'rank',M.rank())
rref,pivs=M.rref();rrrows=[list(rref[i,:]) for i in range(len(pivs))]
labels=['r','s','t']+[f'w{i+1}{j+1}' for i,j in pairs]+['r2','rs','rt','s2','st','t2']
for row in rrrows:
 print('RELATION:', ' '.join(f'({v})*{labels[j]}' for j,v in enumerate(row) if v))
# c2=r-s-2t+4(w13+w15-w34+w45); d=1-4(r+s).
c=[Q(1),Q(-1),Q(-2)]+[Q(4 if ij in [(0,2),(0,4),(3,4)] else -4 if ij==(2,3) else 0) for ij in pairs]+[Q(0)]*6
wanted=[3*v for v in c];wanted[0]+=1;wanted[1]+=1
wanted[13]-=2;wanted[14]-=4;wanted[16]-=2
print('Desired row:',list(zip(labels,wanted)))
contained=M.col_join(S.Matrix([wanted])).rank()==M.rank()
print('Desired dihedral/c2 equality follows from these tests:',contained)
if contained:
 solution,parameters=M.T.gauss_jordan_solve(S.Matrix(wanted));solution=solution.subs({t:0 for t in parameters})
 cert=[(i,str(v),str(data[i])) for i,v in enumerate(solution) if v]
 print('Exact certificate terms:',len(cert))
 for term in cert:print(term)

# The invariant central direction has ordinary c2=1, dihedral k=0. Its
# nonzero bracket coordinates are X_+ wedge Y_+, with X_+=(A+B+D)/4,
# Y_+=(C+E)/4. It is anti-invariant under swapping the free generators.
v0=[Q(0)]*3+[Q(0),Q(1,16),Q(0),Q(1,16),Q(1,16),Q(0),Q(1,16),Q(-1,16),Q(0),Q(1,16)]+[Q(0)]*6
assert all(sum(a*b for a,b in zip(row,v0))==0 for row in rows)
assert sum(a*b for a,b in zip(c,v0))==1
print('Invariant central test datum has c2=1,k=0 and passes every row:',True)
