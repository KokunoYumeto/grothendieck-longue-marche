"""Rank-one C2 character calculation for P4, testing the proposed H_p ⋊ C2 bridge.
Exact Artin relations are the Cohen2010 Example1.1 presentation already used in
check_relative_s3_pentagon.py. No conclusion about full pentagon lifts follows.
"""
from itertools import product
from collections import Counter,defaultdict
keys=[(1,2),(1,3),(2,3),(1,4),(2,4),(3,4)]
def mul(a,b):return (a[0]+(-1)**a[1]*b[0],(a[1]+b[1])%2)
def inv(a):return (-(-1)**a[1]*a[0],a[1])
def conj(a,b):return mul(mul(a,b),inv(a))
def comm(a,b):return mul(mul(mul(a,b),inv(a)),inv(b))
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
     assert lhs[1]==rhs[1]
     out.append(lhs[0]-rhs[0])
 return out

def nullspace(mat,p):
 a=[[v%p for v in row] for row in mat];m=len(a);n=len(a[0]); piv=[];row=0
 for col in range(n):
  pivot=next((i for i in range(row,m) if a[i][col]),None)
  if pivot is None:continue
  a[row],a[pivot]=a[pivot],a[row]
  s=pow(a[row][col],-1,p);a[row]=[(v*s)%p for v in a[row]]
  for i in range(m):
   if i!=row and a[i][col]:
    s=a[i][col];a[i]=[(v-s*w)%p for v,w in zip(a[i],a[row])]
  piv.append(col);row+=1
 free=[j for j in range(n) if j not in piv];out=[]
 for f in free:
  v=[0]*n;v[f]=1
  for i,j in enumerate(piv):v[j]=-a[i][f]%p
  out.append(v)
 return out
for p in (3,5,7,11,13):
 counts=Counter();special=[]
 for eps in product(range(2),repeat=6):
  cols=[]
  for j in range(6):
   q={k:(int(i==j),eps[i]) for i,k in enumerate(keys)}
   cols.append(defects(q))
  mat=list(map(list,zip(*cols)));basis=nullspace(mat,p);d=len(basis)
  counts[d]+=1
  if any(eps) and d>=3:special.append((eps,basis))
 print('p=',p,'dimension counts',sorted(counts.items()),'nontrivial characters with dimension >=3',special)
 if p==7:
  for eps in product(range(2),repeat=6):
   cols=[defects({k:(int(i==j),eps[i]) for i,k in enumerate(keys)}) for j in range(6)]
   basis=nullspace(list(map(list,zip(*cols))),p)
   if any(eps) and len(basis)==2:print('  dim2',eps,'basis',basis)

# Exact integer certificate: every nonzero Smith invariant is 2, so the
# displayed dimensions hold over every field of odd characteristic.
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form
summary=Counter()
for eps in product(range(2),repeat=6):
 cols=[defects({k:(int(i==j),eps[i]) for i,k in enumerate(keys)}) for j in range(6)]
 M=Matrix(list(map(list,zip(*cols))));S=smith_normal_form(M,domain=ZZ)
 diag=tuple(abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i])
 summary[diag]+=1
 assert all(d==2 for d in diag)
print('EXACT INTEGER SMITH CERTIFICATE:',dict(summary))
assert summary=={():1,(2,2,2,2,2):48,(2,2,2,2):15}
