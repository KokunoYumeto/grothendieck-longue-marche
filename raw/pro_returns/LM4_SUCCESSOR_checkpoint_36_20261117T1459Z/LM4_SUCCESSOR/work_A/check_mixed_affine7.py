"""Exploratory exact mixed-head quotient, not an order-two lifting result."""
from collections import deque
n=7;I=tuple(range(n));V=[v for v in range(1<<n) if v.bit_count()%2==0]
def mul(a,b):return tuple(a[b[i]] for i in range(n))
def act(a,v):return sum(1<<a[i] for i in range(n) if v>>i&1)
def norm(a,v,m):
 q=0
 for _ in range(m):q^=v;v=act(a,v)
 return q
def support(v):return [i for i in range(n) if v>>i&1]
def prod(a,b):return(a[0]^act(a[1],b[0]),mul(a[1],b[1]))
def power(a,k):
 b=(0,I)
 for _ in range(k):b=prod(b,a)
 return b
s=tuple(-i%7 for i in range(7));r=tuple((2*i+1)%7 for i in range(7));tau=mul(s,r)
cob={(v^act(s,v),v^act(r,v)) for v in V}
sol=[(v,w) for v in V for w in V if norm(s,v,2)==0 and norm(r,w,3)==0]
assert len(cob)==64 and len(sol)==128
vx,vy=next(pair for pair in sol if pair not in cob)
S=(vx,s);R=(vy,r);T=prod(S,R)
assert power(S,2)==power(R,3)==(0,I)
seen={(0,I)};todo=deque([(0,I)])
while todo:
 a=todo.popleft()
 for b in(S,R):
  c=prod(a,b)
  if c not in seen:seen.add(c);todo.append(c)
assert len(seen)==64*42
print('H generators: s(x)=-x, r(x)=2x+1, tau(x)=5x+6, on F7.')
print('Lift vector supports:',support(vx),support(vy))
print('Order2/order3 lift equations:',len(sol),'solutions; coboundaries:',len(cob))
print('Generated affine group size:',len(seen),'=2^6*42: PASS')
print('Cusp sixth power translation:',support(power(T,6)[0]))
print('Cusp twelfth power identity:',power(T,12)==(0,I))
# Every nonzero H-submodule is V: exact orbit-span rank.
def rank(vs):
 piv={}
 for v in vs:
  while v:
   i=v.bit_length()-1
   if i in piv:v^=piv[i]
   else:piv[i]=v;break
 return len(piv)
heads={g for v,g in seen}
assert len(heads)==42
assert all(rank([act(g,v) for g in heads])==6 for v in V if v)
print('Every nonzero vector has H-orbit span of dimension6: irreducibility PASS')
print('This is a finite quotient certificate only; no central/norm lifting assertion.')
