"""Exact actual source-central quotient for the dyadic bad-frame test.

F=<x,y>, c inverts x,y, w=[x,y], u=[w,x], v=[w,y].
Q has class two and x^4=y^4=w^4=1.  N=ker(F->Q).
The mathematical proof identifies E/[N,E] with the following order2048
group, rather than inferring universality merely from its finite order.
All paths written by this checker stay in work_CE.
"""
from itertools import product
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
I=(0,0,0,0,0)
X=(1,0,0,0,0);Y=(0,1,0,0,0)
W=(0,0,1,0,0);U=(0,0,0,1,0);V=(0,0,0,0,1)

def choose2(a):return a*(a-1)//2
def mul0(g,h):
 a,b,d,r,s=g;A,B,D,R,S=h
 return ((a+A)%8,(b+B)%8,(d+D-b*A)%4,
         (r+R+d*A-b*choose2(A+1))%2,
         (s+S-A*choose2(b+1)+B*(d-b*A))%2)
def ca(g):
 a,b,d,r,s=g
 return((-a)%8,(-b)%8,d,(r+d)%2,(s+d)%2)
def inv0(g):
 a,b,d,r,s=g
 A=-a;B=-b;D=-d+b*A
 R=-r-d*A+b*choose2(A+1)
 S=-s+A*choose2(b+1)-B*(d-b*A)
 return(A%8,B%8,D%4,R%2,S%2)
def mul(g,h):
 a,e=g;b,f=h
 return(mul0(a,ca(b)if e else b),e^f)
def inv(g):
 a,e=g;ia=inv0(a)
 return(ca(ia)if e else ia,e)
one=(I,0);x=(X,0);y=(Y,0);w=(W,0);u=(U,0);v=(V,0);c=(I,1)
def powr(g,n):
 if n<0:return powr(inv(g),-n)
 a=one
 while n:
  if n&1:a=mul(a,g)
  g=mul(g,g);n>>=1
 return a
def con(g,h):return mul(mul(g,h),inv(g))
def comm(g,h):return mul(mul(mul(g,h),inv(g)),inv(h))
def q(g):
 (a,b,d,r,s),e=g
 return(a%4,b%4,d,e)
def qm(g,h):
 a,b,d,e=g;A,B,D,f=h;sg=1 if e==0 else -1
 return((a+sg*A)%4,(b+sg*B)%4,(d+D-b*sg*A)%4,e^f)

F=list(product(range(8),range(8),range(4),range(2),range(2)))
G=list(product(F,range(2)))
gens=(x,y,c,inv(x),inv(y))
assert len(F)==1024 and len(G)==2048
seen={one};todo=[one]
for a in todo:
 for b in gens:
  ab=mul(a,b)
  if ab not in seen:seen.add(ab);todo.append(ab)
assert len(seen)==2048
assert comm(x,y)==w and comm(w,x)==u and comm(w,y)==v
assert all(powr(g,n)==one for g,n in[(x,8),(y,8),(w,4),(u,2),(v,2),(c,2)])
assert con(c,x)==inv(x)and con(c,y)==inv(y)
assert con(c,w)==mul(mul(w,u),v)
assert con(c,u)==u and con(c,v)==v
for a in F:
 assert ca(ca(a))==a
 assert mul0(a,inv0(a))==mul0(inv0(a),a)==I
 for b in (X,Y,W,U,V):
  assert ca(mul0(a,b))==mul0(ca(a),ca(b))
# Associativity for all pairs and each generator of the orientation group.
# This also tests every coefficient/carry in the collection polynomial.
for a in F:
 for b in F:
  ab=mul0(a,b)
  for t in (X,Y):
   assert mul0(ab,t)==mul0(a,mul0(b,t))
K={g for g in G if q(g)==(0,0,0,0)}
assert len(K)==16
for a in G:
 assert mul(a,inv(a))==mul(inv(a),a)==one
 for b in gens:
  assert q(mul(a,b))==qm(q(a),q(b))
for a in K:assert all(mul(a,b)==mul(b,a)for b in gens)
Kgens=(powr(x,4),powr(y,4),u,v)
assert all(powr(k,2)==one for k in Kgens)
assert {mul(mul(powr(Kgens[0],a),powr(Kgens[1],b)),
                 mul(powr(Kgens[2],d),powr(Kgens[3],e)))
        for a,b,d,e in product(range(2),repeat=4)}==K

beta=powr(w,2)
assert beta!=one and powr(beta,2)==one and con(c,beta)==beta
assert all(mul(beta,g)==mul(g,beta)for g in gens)
assert mul(beta,con(c,beta))==one
z=inv(mul(x,y));t=(c,mul(x,c),mul(inv(y),c))
assert all(powr(a,2)==one for a in t)
# The actual quotient action is the identity.  The named x and xc frames
# can nevertheless be chosen beta, while all other frames are one.
assert con(beta,x)==x and con(beta,t[1])==t[1]
assert all(con(one,a)==a for a in (y,z,t[0],t[2]))
qbeta=q(beta)
qxpowers={q(powr(x,i))for i in range(8)}
assert qbeta not in qxpowers
print('Actual source-central quotient normal forms: order2048; orientation1024; base128.')
print('All orientation pairs and x/y associativity checks, all inverses, c and quotient edges: PASS')
print('Central source kernel: C2^4, order16.  Quotient retains w^2 nontrivially.')
print('Identity action; named reflection/cusp frame beta=w^2: class and c-norm equations PASS')
print('beta has order2 and q(beta) is not in <q(x)>: PASS')
print('Scope: prescribed-frame lifting fails; frames allowed to vary admit the identity lift.')
out=dict(order=len(G),orientation_order=len(F),base_order=128,
 source_central_kernel_order=len(K),source_central_kernel='C2^4',
 normal_forms='x^a y^b w^d u^r v^s c^e, a,b mod8,d mod4,r,s,e mod2',
 generators=dict(x=x,y=y,w=w,u=u,v=v,c=c),bad_frame=beta,
 base_bad_frame=qbeta,identity_action=True,frame_norm=True,
 all_checks='PASS',scope='Only prescribed frames, including their quotient involutory norms; no obstruction when frames may vary.')
(HERE/'dyadic_bad_frame_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
