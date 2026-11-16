"""An exact nonregular, orbit-one simple quotient of Pi=C2 amalg C3.

Permutation composition acts on the left. This certificate only establishes
the finite quotient; the actual central-refinement proof is in A.48.
"""
from collections import deque

def cycle(n,*xs):
 p=list(range(n))
 for a,b in zip(xs,xs[1:]+xs[:1]):p[a-1]=b-1
 return tuple(p)
def mul(a,b):return tuple(a[b[i]] for i in range(len(a)))
def power(a,n):
 b=tuple(range(len(a)))
 for _ in range(n):b=mul(b,a)
 return b
def types(a):
 seen=set();out=[]
 for i in range(len(a)):
  if i in seen:continue
  j=i;l=0
  while j not in seen:seen.add(j);l+=1;j=a[j]
  out.append(l)
 return sorted(out)
I=tuple(range(9))
s=mul(mul(cycle(9,1,2),cycle(9,3,4)),mul(cycle(9,5,6),cycle(9,7,8)))
r=mul(mul(cycle(9,1,3,8),cycle(9,2,4,9)),cycle(9,5,7,6))
tau=mul(s,r)
assert power(s,2)==power(r,3)==power(tau,15)==I
assert power(tau,3)!=I and power(tau,5)!=I
seen={I};todo=deque([I])
while todo:
 a=todo.popleft()
 for g in (s,r):
  b=mul(a,g)
  if b not in seen:seen.add(b);todo.append(b)
assert len(seen)==181440
print('s=(12)(34)(56)(78), r=(138)(249)(576)')
print('Orders: s=2, r=3, tau=sr=15; tau cycle type',types(tau))
print('Exact generated group order:',len(seen),'= |A9|: PASS')
print('Every K cusp maps to a conjugate of tau^5, of order3:',types(power(tau,5)))
print('K maps onto A9 because its image is normal and A9 is not a quotient of A5.')
print('Its K-kernel is normal in Pi, hence its A5 orbit has length1.')
print('This is not a regular tripod bundle: all12 cusp images are nontrivial.')
print('All finite checks PASS; no full order-two lift is inferred.')
