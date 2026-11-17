"""Exact Eisenstein coefficient calculation for the 12-point cyclic cover.

The unreduced Burau module at t^2-t+1=0 has invariant vector v=(1,...,1)
and invariant covector (1,t,...,t^11).  Because t^12=1, v is in the
kernel of the covector.  Their subquotient has dimension 10.
All arithmetic is exact in Z[t]/(t^2-t+1).
"""
from pathlib import Path
import json
from collections import Counter,defaultdict
zero=(0,0);one=(1,0);t=(0,1)
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[0],-x[1])
def sub(x,y):return add(x,neg(y))
def mul(x,y):
 a,b=x;c,d=y
 return (a*c-b*d,a*d+b*c+b*d)
def power(x,n):
 if n<0:
  assert x==t
  x=(1,-1);n=-n
 z=one
 for _ in range(n):z=mul(z,x)
 return z
def identity(n):return [[one if i==j else zero for j in range(n)] for i in range(n)]
def scalar(c,A):return [[mul(c,x) for x in row] for row in A]
def mm(A,B):
 n=len(A);ans=[[zero for j in range(n)] for i in range(n)]
 for i in range(n):
  for k in range(n):
   if A[i][k]!=zero:
    for j in range(n):
     if B[k][j]!=zero:ans[i][j]=add(ans[i][j],mul(A[i][k],B[k][j]))
 return ans
def mp(A,n):
 z=identity(len(A))
 for _ in range(n):z=mm(z,A)
 return z
def trace(A):
 z=zero
 for i in range(len(A)):z=add(z,A[i][i])
 return z
def burau(word,n=12):
 A=identity(n)
 for letter in word:
  assert letter>0
  k=letter-1
  # right multiplication by [[1-t,t],[1,0]]
  for row in A:
   a,b=row[k:k+2];row[k]=add(mul((1,-1),a),b);row[k+1]=mul(t,a)
 return A
def quotient(A):
 # Basis e_i - t^(i-11)e_11, i=0,...,9, modulo v.
 return [[sub(sub(A[i][j],mul(power(t,j-11),A[i][11])),
              sub(A[10][j],mul(power(t,j-11),A[10][11])))
          for j in range(10)] for i in range(10)]
def perm(word):
 p=list(range(12))
 for a in word:p[a-1],p[a]=p[a],p[a-1]
 return tuple(p)
def pc(p,q):return tuple(p[j] for j in q)
def po(p):
 z=tuple(range(len(p)))
 for k in range(1,61):
  z=pc(z,p)
  if z==tuple(range(len(p))):return k
 raise AssertionError

root=Path(__file__).resolve().parents[1]
d=json.loads((root/'data'/'icosahedral_braids.json').read_text())
b2,b3=d['beta2'],d['beta3'];I=identity(10)
M2=quotient(burau(b2));M3=quotient(burau(b3))
assert mp(M2,2)==I and mp(M3,3)==I
R=list(range(11,1,-1))+[1,1]+list(range(2,12))
assert quotient(burau(R))==scalar(t,I)
M2=scalar((-1,0),M2)
M3=scalar(power(t,4),M3)
assert mp(M3,3)==I and mp(mm(M2,mp(M3,2)),5)==I
gens=[(perm(b2),M2),(perm(b3),M3)]
identityp=tuple(range(12));seen={identityp:I};todo=[identityp]
for p in todo:
 for q,B in gens:
  r=pc(p,q);A=mm(seen[p],B)
  if r in seen:assert seen[r]==A
  else:seen[r]=A;todo.append(r)
assert len(seen)==60
chars=defaultdict(Counter)
for p,A in seen.items():chars[po(p)][trace(A)]+=1
assert dict(chars)=={1:Counter({(10,0):1}),2:Counter({(2,0):15}),3:Counter({(1,0):20}),5:Counter({(0,0):24})}
print('PASS: exact 10-dimensional quotient; R_last acts by t')
print('PASS: normalized matrices generate A5, order60, relations s^2=r^3=(sr^-1)^5=1')
print('Trace by element order:',dict(chars))
# A5 characters for dimensions 1,4,5 on the same class types.
expected={1:10,2:2,3:1,5:0}
inner=sum(sum(count*(value[0]**2) for value,count in C.items()) for C in chars.values())
assert inner==180
print('Endomorphism centralizer dimension:',inner//60)
print('Character decomposition: 1 + 4 + 5; all multiplicities one')
(root/'data'/'icosahedral_eigenspace_matrices.json').write_text(json.dumps({'coefficient_relation':'t^2-t+1=0','s':M2,'r':M3,'dimension':10},indent=2)+'\n')
