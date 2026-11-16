"""Minimal independent certificate for C.35.
Only 2x2 arithmetic over F3, the quaternion subgroup, and four projective
pair orbits are used. No pentagon enumeration or imported script is used.
"""
from itertools import product

def mul(a,b):
 return ((a[0]*b[0]+a[1]*b[2])%3,(a[0]*b[1]+a[1]*b[3])%3,
         (a[2]*b[0]+a[3]*b[2])%3,(a[2]*b[1]+a[3]*b[3])%3)
def det(a):return(a[0]*a[3]-a[1]*a[2])%3
def inv(a):
 t=pow(det(a),-1,3);return(a[3]*t%3,-a[1]*t%3,-a[2]*t%3,a[0]*t%3)
def neg(a):return tuple(-v%3 for v in a)
def con(a,b):return mul(mul(a,b),inv(a))
E=(1,0,0,1);I=(0,1,2,0);J=(1,1,1,2);K=mul(I,J)
A=(1,1,0,1);B=(0,1,2,1);D=(0,1,2,2)
S=(1,0,2,2);T=(1,2,0,2);R=(1,1,2,1)
Q={E,I,J,K,neg(E),neg(I),neg(J),neg(K)}
assert K==(1,2,2,2) and len(Q)==8
assert all(mul(g,g)==neg(E) for g in (I,J,K))
assert all(mul(a,b) in Q for a,b in product(Q,repeat=2))
assert (con(S,A),con(S,B))==(neg(B),neg(A))
assert (con(S,I),con(S,J),con(S,K))==(neg(J),neg(I),neg(K))
assert (con(J,A),con(J,D))==(D,A)
assert (con(J,I),con(J,J),con(J,K))==(neg(I),J,neg(K))
assert (con(T,A),con(T,B))==(inv(A),inv(B))
assert (con(T,I),con(T,J),con(T,K))==(J,I,neg(K))
assert (con(R,I),con(R,J),con(R,K))==(I,K,neg(J))
assert inv(mul(A,B))==J
assert con(A,I)==neg(J) and con(S,I)==neg(J)
assert mul(B,S)==neg(R)
dual1={g for g in Q if mul(g,con(S,g))==E}
dual2={g for g in Q if mul(g,con(J,g))==E}
assert dual1=={E,neg(E),K,neg(K)}
assert dual2==Q-{J,neg(J)}
hexvalues={mul(inv(con(R,g)),g) for g in Q}
assert hexvalues=={E,I} and hexvalues&dual1=={E}
assert {g for g in dual1 if con(T,g)==g}=={E,neg(E)}
print('Every displayed conjugation and negative-hexagon identity: PASS')
print('Duality solutions at(A,B): ±1,±K; at(A,D): ±1,±I,±K')
print('Negative hexagon forces f(A,B)=1; canonical norm forces u(A,B)=±1')

points=[(1,0),(0,1),(1,1),(2,1)]
def project(a):
 out=[]
 for x,y in points:
  X=(a[0]*x+a[1]*y)%3;Y=(a[2]*x+a[3]*y)%3
  v=(1,0) if not Y else(X*pow(Y,-1,3)%3,1)
  out.append(points.index(v))
 return tuple(out)
def pmul(a,b):return tuple(a[b[i]] for i in range(4))
def pinv(a):return tuple(a.index(i) for i in range(4))
def pcon(a,b):return pmul(pmul(a,b),pinv(a))
pe=tuple(range(4))
def generated(a,b):
 h={pe};todo=[pe]
 while todo:
  g=todo.pop()
  for t in (a,b):
   q=pmul(g,t)
   if q not in h:h.add(q);todo.append(q)
 return h
def order(a):
 q=pe
 for n in range(1,13):
  q=pmul(q,a)
  if q==pe:return n
SL=[a for a in product(range(3),repeat=4) if det(a)==1]
GL=[a for a in product(range(3),repeat=4) if det(a)]
assert Q=={E,neg(E)}|{g for g in SL if (g[0]+g[3])%3==0}
assert all(con(g,h) in Q for g in SL for h in Q)
ci=mul(con(A,I),inv(I));assert ci==neg(K)
comm_orbit=[ci,con(A,ci),con(mul(A,A),ci)]
sub={E};todo=[E]
while todo:
 g=todo.pop()
 for h in comm_orbit:
  v=mul(g,h)
  if v not in sub:sub.add(v);todo.append(v)
assert sub==Q
print('Q is normal, L/Q has order3, and [A,I] with its A-conjugates generates Q: PASS')
G={project(a) for a in SL};Aut={project(a) for a in GL}
assert len(SL)==24 and len(G)==12 and len(Aut)==24
pairs=[(A,I),(A,B),(A,D),(I,A)];orbits=[]
for a,b in pairs:
 pa,pb=project(a),project(b)
 assert len(generated(pa,pb))==12
 orbit={(pcon(h,pa),pcon(h,pb)) for h in Aut}
 assert len(orbit)==24
 orbits.append(orbit)
 print('Projective passport:',(order(pa),order(pb),order(pmul(pa,pb))))
assert len(set.union(*orbits))==96
assert set.union(*orbits)=={(a,b) for a,b in product(G,repeat=2) if len(generated(a,b))==12}
counts=[len(generated(project(A),project(con(inv(g),D)))) for g in (E,I,J,K)]
assert counts==[12,12,3,12]
print('All96 generating A4 pairs covered by four orbits: PASS')
print('Generation orders after conjugating D by1,I,J,K:',counts)
print('All A4 generation conclusions of C.35: PASS')

# Finite third-cusp corollary C.36, with every unit residue modulo6.
def ppow(a,n):
 q=pe
 for _ in range(n):q=pmul(q,a)
 return q
for (a,b),allowed in zip(pairs,[Q,{E,neg(E)},Q-{J,neg(J)},Q]):
 for u in allowed:
  for mu in (1,5):
   left=pmul(ppow(project(a),mu),pcon(pinv(project(u)),ppow(project(b),mu)))
   right=ppow(pmul(project(a),project(b)),mu)
   assert left in {pcon(h,right) for h in G}
print('C.36 finite A4 third-cusp tests for every unit residue: PASS')
