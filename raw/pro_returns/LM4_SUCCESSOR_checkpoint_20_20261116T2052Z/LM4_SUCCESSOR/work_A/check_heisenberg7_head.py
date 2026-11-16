"""Exploratory Heisenberg7:C6 head; no full lifting claim."""
from collections import deque
p=7;half=4;a=3
I=(0,0,0,0)
def mul(g,h):
 x,y,z,d=g;u,v,w,e=h
 u=u*pow(a,d,7)%7;v=v*pow(a,-d,7)%7
 return((x+u)%7,(y+v)%7,(z+w+half*(x*v-y*u))%7,(d+e)%6)
def pw(g,n):
 h=I
 for _ in range(n):h=mul(h,g)
 return h
s=(0,0,0,3);r=(1,1,2,2);tau=mul(s,r)
assert pw(s,2)==pw(r,3)==I
seen={I};todo=deque([I])
while todo:
 g=todo.popleft()
 for h in(s,r):
  q=mul(g,h)
  if q not in seen:seen.add(q);todo.append(q)
assert len(seen)==7**3*6
print('s=',s,'r=',r,'tau=',tau)
print('Generated head order:',len(seen),'=7^3*6: PASS')
print('tau^6=',pw(tau,6),'tau^42=',pw(tau,42))
cs=[g for g in seen if mul(g,s)==mul(s,g)]
assert len(cs)==42 and all(g[0]==g[1]==0 for g in cs)
print('C_H(s)=Z(Heis7) times C6, order',len(cs))
print('The actual cusp central character is nontrivial, so tau-1 is invertible in a nontrivial central-character module.')
