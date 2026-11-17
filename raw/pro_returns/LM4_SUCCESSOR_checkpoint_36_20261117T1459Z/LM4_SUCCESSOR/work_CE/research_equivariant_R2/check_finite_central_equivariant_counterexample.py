"""Actual source-central quotient of C2*C2*C2, order13824.
This checks all group elements and generator edges, not a sampled table.
Normal forms x^a y^b w^d c^e, w=[x,y], a,b mod24,d mod12,e mod2.
"""
from itertools import product
from pathlib import Path
import json
P=Path(__file__).resolve().parent
one=(0,0,0,0);x=(1,0,0,0);y=(0,1,0,0);w=(0,0,1,0);c=(0,0,0,1)
def mul(g,h):
 a,b,d,e=g;u,v,k,f=h;s=1 if e==0 else -1
 return((a+s*u)%24,(b+s*v)%24,(d+k-b*s*u)%12,e^f)
def inv(g):
 a,b,d,e=g;s=1 if e==0 else -1
 return((-s*a)%24,(-s*b)%24,(-d-a*b)%12,e)
def power(g,n):
 if n<0:return power(inv(g),-n)
 out=one
 while n:
  if n&1:out=mul(out,g)
  g=mul(g,g);n>>=1
 return out
def conj(g,h):return mul(mul(g,h),inv(g))
def theta(g):return((7*g[0])%24,(7*g[1])%24,g[2],g[3])
def q(g):return(g[0]%12,g[1]%12,g[3])
def qm(g,h):
 a,b,e=g;u,v,f=h;s=1 if e==0 else -1
 return((a+s*u)%12,(b+s*v)%12,e^f)
G=list(product(range(24),range(24),range(12),range(2)))
gs=(x,y,c,inv(x),inv(y));found={one};todo=[one]
for a in todo:
 for b in gs:
  ab=mul(a,b)
  if ab not in found:found.add(ab);todo.append(ab)
assert len(found)==len(G)==13824
K={g for g in G if q(g)==(0,0,0)}
assert len(K)==48
assert mul(mul(mul(x,y),inv(x)),inv(y))==w
assert power(x,24)==power(y,24)==power(w,12)==power(c,2)==one
assert conj(c,x)==inv(x)and conj(c,y)==inv(y)and conj(c,w)==w
for a in G:
 assert mul(a,inv(a))==mul(inv(a),a)==one
 assert theta(theta(a))==a
 for b in gs:
  assert theta(mul(a,b))==mul(theta(a),theta(b))
  assert q(mul(a,b))==qm(q(a),q(b))
for a in K:
 assert theta(a)==a
 assert all(mul(a,b)==mul(b,a)for b in gs)
t0=c;t1=mul(x,c);t2=mul(inv(y),c)
assert all(power(t,2)==one for t in (t0,t1,t2))
assert mul(t1,t0)==x and mul(t0,t2)==y and mul(t1,t2)==mul(x,y)
for t,a in zip((t0,t1,t2),(one,power(x,3),power(y,-3))):
 assert theta(t)==conj(a,t)
z=inv(mul(x,y))
assert theta(x)==power(x,7)and theta(y)==power(y,7)
assert theta(z)==conj(power(x,3),power(z,7))
assert theta(mul(x,y))==conj(power(x,3),power(mul(x,y),7))
# Independent tiny finite certificate excluding the normalized full lift.
def cyc(n,*entries):
 p=list(range(n))
 for a,b in zip(entries,entries[1:]+entries[:1]):p[a]=b
 return tuple(p)
def pm(a,b):return tuple(a[b[i]]for i in range(len(a)))
def pp(a,n):
 out=tuple(range(len(a)))
 for _ in range(n):out=pm(out,a)
 return out
def po(a):
 b=a;n=1
 while b!=tuple(range(len(a))):b=pm(b,a);n+=1
 return n
X=cyc(4,1,2,3);Y=cyc(4,0,1,2,3)
actual=pm(pp(X,7),pp(Y,7));required=pp(pm(X,Y),7)
assert po(actual)==2 and po(required)==4
print('Exact source-central normal-form group:',len(G),'orientation subgroup:',len(G)//2)
print('Kernel over (Z/12)^2 semidirect C2:',len(K),'= C2^2 x C12, central and theta-fixed')
print('All13824 elements and generator edges: group, quotient and involutory automorphism checks PASS')
print('Three named reflection classes and all three pair-product cusp classes: PASS')
print('Theta fixes external c and uses common unit residue7mod24.')
print('Full c-equivariant lift would be literal powering; S4 orders2 versus4 exclude it.')
out=dict(scope='Actual finite source-central data without a full reflection-equivariant peripheral lift; mixed-multiplier scope',order=len(G),orientation_order=len(G)//2,central_kernel_order=len(K),source='E0=C2*C2*C2=F2 semidirect c',normal_subgroup='N=ker(F2 ->(Z/12)^2)',central_quotient='E0/[N,E0]',normal_form='x^a y^b w^d c^e; a,b mod24,d mod12,e mod2',theta='(a,b,d,e)->(7a,7b,d,e)',reflection_generators=[t0,t1,t2],reflection_conjugators=[one,power(x,3),power(y,-3)],cusp_conjugators=[one,one,power(x,3)],all_element_checks='PASS',S4_X=X,S4_Y=Y,S4_actual=actual,S4_required=required,S4_orders=[po(actual),po(required)],remaining_scope='Does not refute multiplier-one same-action equivariant lifting.')
(P/'finite_central_equivariant_counterexample.json').write_text(json.dumps(out,indent=2)+'\n')
