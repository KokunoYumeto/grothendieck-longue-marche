#!/usr/bin/env python3
"""Additional exact checks: Witt vectors, wound groups, and derived length."""
from math import comb
from itertools import product
import sympy as s
print('Witt-vector additive law: W_2(F_p).')
for p in [2,3,5]:
 def plus(a,b):
  return ((a[0]+b[0])%p,(a[1]+b[1]-sum((comb(p,i)//p)*a[0]**i*b[0]**(p-i) for i in range(1,p)))%p)
 allv=list(product(range(p),repeat=2))
 assert all(plus(plus(a,b),c)==plus(a,plus(b,c)) for a,b,c in product(allv,repeat=3))
 v=(0,0);atp=None;order=None
 for n in range(1,p*p+1):
  v=plus(v,(1,0))
  if n==p:atp=v
  if v==(0,0):order=n;break
 assert atp==(0,1) and order==p*p
 print('p=',p,'p*(1,0)=',atp,'order=',order,'associativity on',len(allv)**3,'triples: PASS')

print('\nWound one-dimensional group over F_p(t): y^p=x-t^(1-p)x^p; g=(t,0).')
t=s.symbols('t')
for p in [2,3,5]:
 assert s.expand(t-t**(1-p)*t**p)==0
 assert (1-p)%p!=0
 print('p=',p,'g lies on group: PASS; valuation of coefficient=',1-p,'not divisible by p: PASS')

print('\nDerived length of the order-48 quotient (Z/2)^2 semidirect Dic3.')
R=((0,1),(1,1));S=((0,1),(1,0));I=((1,0),(0,1))
def matmul(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))%2 for j in range(2)) for i in range(2))
def hm(a,b):return ((a[0]+(-1)**a[1]*b[0]+3*a[1]*b[1])%6,(a[1]+b[1])%2)
def power(A,n):
 C=I
 for _ in range(n):C=matmul(C,A)
 return C
act={(a,b):matmul(power(R,a),power(S,b)) for a,b in product(range(6),range(2))}
e=(0,0,0,0)
def mul(u,v):
 A=act[u[2:]];h=hm(u[2:],v[2:])
 return ((u[0]+A[0][0]*v[0]+A[0][1]*v[1])%2,(u[1]+A[1][0]*v[0]+A[1][1]*v[1])%2,*h)
G=list(product(range(2),range(2),range(6),range(2)))
inv={a:next(b for b in G if mul(a,b)==e) for a in G}
def subgroup(gens):
 seen={e};todo=[e]
 while todo:
  a=todo.pop()
  for b in gens:
   c=mul(a,b)
   if c not in seen:seen.add(c);todo.append(c)
 return seen
series=[set(G)]
while len(series[-1])>1:
 A=series[-1];comms={mul(mul(mul(a,b),inv[a]),inv[b]) for a,b in product(A,repeat=2)}
 series.append(subgroup(comms))
print('Derived subgroup orders:',[len(A) for A in series])
assert [len(A) for A in series]==[48,12,4,1]
print('Thus S is not metabelian in the modern derived-length-two sense.')

lower=[set(G)]
for _ in range(3):
 A=lower[-1]
 comms={mul(mul(mul(a,b),inv[a]),inv[b]) for a,b in product(G,A)}
 lower.append(subgroup(comms))
print('Lower central subgroup orders through gamma_4:',[len(A) for A in lower])
assert [len(A) for A in lower]==[48,12,12,12]

print('\nSmooth Ga deformations over every Z/p^2, checked at p=2,3,5.')
x,y,z,T=s.symbols('x y z T')
def reduce_poly(f,mod,*vars):
 return s.Poly(s.expand(f),*vars).trunc(mod).as_expr()
for p in [2,3,5]:
 C=sum((comb(p,i)//p)*x**i*y**(p-i) for i in range(1,p))
 def cp(a,b):return C.subs({x:a,y:b},simultaneous=True)
 def law(a,b,*vars):return reduce_poly(a+b+p*cp(a,b),p*p,*vars)
 assert s.expand(cp(x,y)+cp(x+y,z)-cp(y,z)-cp(x,y+z))==0
 assoc=reduce_poly(law(law(x,y,x,y),z,x,y,z)-law(x,law(y,z,y,z),x,y,z),p*p,x,y,z)
 assert assoc==0
 inverse=reduce_poly(-x-p*cp(x,-x),p*p,x)
 assert law(x,inverse,x)==0 and law(inverse,x,x)==0
 multiple=s.Integer(0)
 for _ in range(p):multiple=law(multiple,T,T)
 expected=reduce_poly(p*(T-T**p),p*p,T)
 assert s.expand(multiple-expected)==0
 assert int(multiple.subs(T,1))%(p*p)==0
 exponents=[];degree=1
 while degree<=12:exponents.append(degree);degree*=p
 candidates=0;survivors=[]
 for coeffs in product(range(p),repeat=len(exponents)):
  B=sum(c*T**d for c,d in zip(coeffs,exponents))
  if int(B.subs(T,1))%p!=1:continue
  candidates+=1
  condition=reduce_poly(B-B**p-coeffs[0]*T,p,T)
  if condition==0:survivors.append(coeffs)
 assert not survivors
 print('p=',p,'C_p=',C,'inverse=',inverse,'[p]_G(T)=',multiple,
       '; cocycle, associativity, inverse: PASS; normalized additive candidates degree<=12=',
       candidates,'survivors=',len(survivors))

print('\nCharacteristic-zero nilpotent base Q[epsilon]/(epsilon^2).')
eps,U=s.symbols('epsilon U')
def dual(f):return s.rem(s.Poly(s.expand(f),eps),s.Poly(eps**2,eps)).as_expr()
assert dual((1+eps*T)*(1+eps*U)-(1+eps*(T+U)))==0
g=s.Matrix([[1+eps,1],[0,1]])
N=g-s.eye(2)
X=(N-N*N/2).applyfunc(dual)
phi=(s.eye(2)+T*X+T*T*X*X/2).applyfunc(dual)
assert (phi.subs(T,T+U)-phi*phi.subs(T,U)).applyfunc(dual)==s.zeros(2)
assert (phi.subs(T,1)-g).applyfunc(dual)==s.zeros(2)
print('Scalar section 1+epsilon: phi(T)=1+epsilon*T; group law: PASS')
print('Matrix g=',g,'; log(g)=',X,'; phi(T)=',phi)
print('Matrix homomorphism law and value at 1: PASS')
print('\nALL ADDITIONAL ASSERTIONS PASSED.')
