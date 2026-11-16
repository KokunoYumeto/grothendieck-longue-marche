"""Exact certificates for class203: no theta3/5; scalar Frobenius; semilinear norm."""
import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'code'))
from finite_jacobian import BinaryField,PolynomialRing,Jacobian
F=BinaryField(7);R=PolynomialRing(F);a=2;b=3;x=(0,1);one=(1,)
add=R.add;mul=R.mul;sq=R.sq;scale=R.scale
counts=[]
for modulus in (7,19):
 E=BinaryField(modulus);PR=PolynomialRing(E);alpha=E.embed_f4();beta=alpha^1
 hh=(alpha,1,1)
 ff=PR.mul(hh,PR.add(PR.mul((0,1),hh),PR.scale((1,1),beta)))
 J=Jacobian(E,hh,ff)
 counts.append([E.q,len(J.points())])
assert counts==[[4,7],[16,15]]
# theta3 equations reduce to r^2+r=0 and r^3+alpha*r+1=0.
r3eq=(0,1,1);r3end=(1,a,0,1)
g3,u3,v3=R.xgcd(r3eq,r3end)
assert g3==(1,)
assert add(mul(u3,r3eq),mul(v3,r3end))==(1,)
# theta5: R5=r^5+r^4+beta, S=d^2=alpha*(r^4+r+1), Td=U.
r5eq=(b,0,0,0,1,1)
S=(a,a,0,0,a)
T=add(S,x)
U=add(add(add(add(sq(x),mul(add(x,one),S)),sq(S)),scale(x,b)),one)
ob=add(sq(U),mul(S,sq(T)))
g5,u5,v5=R.xgcd(r5eq,ob)
assert g5==(1,)
assert add(mul(u5,r5eq),mul(v5,ob))==(1,)
obrem=R.mod(ob,r5eq)
g5r,u5r,v5r=R.xgcd(r5eq,obrem)
assert g5r==(1,) and add(mul(u5r,r5eq),mul(v5r,obrem))==(1,)
# Frobenius characteristic polynomial in ascending order.
P=[16,8,1,2,1]
def pmul(f,g,p):
 out=[0]*(len(f)+len(g)-1)
 for i,v in enumerate(f):
  for j,w in enumerate(g):out[i+j]=(out[i+j]+v*w)%p
 for i in range(len(out)-1,3,-1):
  c=out[i]
  for j in range(5):out[i-4+j]=(out[i-4+j]-c*P[j])%p
 return (out+[0]*4)[:4]
def power(n,p):
 v=[1,0,0,0];x=[0,1,0,0]
 while n:
  if n&1:v=pmul(v,x,p)
  n>>=1;x=pmul(x,x,p)
 return v
assert power(5,3)==[2,0,0,0]
assert power(13,5)==[2,0,0,0]
assert power(10,3)==[1,0,0,0]
assert power(52,5)==[1,0,0,0]
# Every eigenvalue has exact indicated order: gcd(P,X^m-1)=1 for proper m dividingorder.
def igcd(f,g,p):
 while g:
  h=f[:]
  while len(h)>=len(g):
   c=h[-1]*pow(g[-1],-1,p)%p;d=len(h)-len(g)
   for j,w in enumerate(g):h[d+j]=(h[d+j]-c*w)%p
   while h and not h[-1]:h.pop()
  f,g=g,h
 if not f:return[]
 inv=pow(f[-1],-1,p);return[v*inv%p for v in f]
orders={}
for p,n in [(3,10),(5,52)]:
 checks=[]
 for m in range(1,n+1):
  if n%m:continue
  poly=[p-1]+[0]*(m-1)+[1]
  g=igcd([v%p for v in P],poly,p)
  checks.append([m,g])
  assert len(g)==(5 if m==n else 1)
 orders[p]=checks
# All semilinear maps x -> c*x^2 on F4 andF16 have fthpoweridentity.
sem=[]
for mod,f in [(7,2),(19,4)]:
 E=BinaryField(mod)
 for c in range(1,E.q):
  for x0 in range(E.q):
   z=x0
   for _ in range(f):z=E.mul(c,E.mul(z,z))
   assert z==x0
 sem.append({'field_size':E.q,'scalar_choices':E.q-1,'vectors':E.q,'iterations':f})
print(json.dumps({'curve':'v^2+v=z+(alpha+1)*(z+1)/(z^2+z+alpha), alpha^2+alpha+1=0','encoding':'F4 elements0,1,alpha=2,alpha+1=3; coefficient lists ascending','theta3':{'r_equation':r3eq,'other_equation':r3end,'bezout_u':u3,'bezout_v':v3,'gcd':g3},'theta5':{'r_equation':r5eq,'S':S,'T':T,'U':U,'obstruction':ob,'obstruction_mod_R5':obrem,'reduced_bezout_u':u5r,'reduced_bezout_v':v5r,'bezout_u':u5,'bezout_v':v5,'gcd':g5},'point_counts':counts,'Frobenius_polynomial':P,'pi5_mod3':power(5,3),'pi13_mod5':power(13,5),'exact_eigenvalue_orders':orders,'semilinear_checks':sem},indent=2))
