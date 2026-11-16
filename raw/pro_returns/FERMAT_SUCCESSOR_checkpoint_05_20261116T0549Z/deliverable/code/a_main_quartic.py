"""Exact quartic quotient, 2-isogeny descent, and eta-series checks."""
from fractions import Fraction
import sympy as s
u,v,a=s.symbols('u v a')
x=2*(v+1)/u**2;y=4*(v+1)/u**3
num=s.factor((y*y-x**3+4*a*x)*u**6)
assert s.rem(num,s.Poly(v*v-1-a*u**4,v),v)==0
print('quartic map x=2(v+1)/u^2, y=4(v+1)/u^3 verified')
for B in [-4,4,16,-16]:
 print('E_B, B=',B)
 for p in [3,5,7,11]:
  count=1+sum((yy*yy-xx**3-B*xx)%p==0 for xx in range(p) for yy in range(p))
  print(' #E(F_%d)='%p,count)
for B,d in [(16,2),(-16,2),(-16,-2)]:
 residues=sorted({(d*m**4+(B//d)*e**4)%16 for m in range(16) for e in range(16) if (m%2 or e%2)})
 squares={z*z%16 for z in range(16)}
 assert not (set(residues)&squares)
 print('quartic descent obstruction B=%d d=%d: primitive RHS residues %s, squares %s'%(B,d,residues,sorted(squares)))

def mul(A,B,n):
 C=[0]*(n+1)
 for i,a in enumerate(A):
  for j,b in enumerate(B):
   if i+j<=n:C[i+j]+=a*b
 return C
def eta_product(exponents,n):
 shift=sum(k*r for k,r in exponents.items())//24
 A=[1]+[0]*n
 for delta,r in exponents.items():
  for k in range(1,n//delta+1):
   m=delta*k
   P=[0]*(n+1)
   for j in range(n//m+1):
    P[j*m]=int(s.binomial(r,j))*(-1)**j
   A=mul(A,P,n)
 return [0]*shift+A[:n+1-shift]
for N,B,exponents in [(32,4,{4:2,8:2}),(64,-4,{4:-2,8:8,16:-2})]:
 bound=N*3//2//6
 q=eta_product(exponents,bound)
 ap={p:p+1-(1+sum((yy*yy-xx**3-B*xx)%p==0 for xx in range(p) for yy in range(p))) for p in list(s.primerange(3,bound+1))}
 def an(n):
  if n==1:return 1
  prod=1
  for p,e in s.factorint(n).items():
   if p==2:return 0
   aa,bb=1,ap[p]
   for i in range(2,e+1):aa,bb=bb,ap[p]*bb-p*aa
   prod*=bb
  return prod
 coeffs=[0]+[an(i) for i in range(1,bound+1)]
 assert q==coeffs
 print('eta coefficients equal elliptic local-factor coefficients through bound',bound,'at level',N,':',q)
 orders=[]
 for c in s.divisors(N):
  order=Fraction(N,24*s.gcd(c*c,N))*sum(Fraction(r*int(s.gcd(c,d))**2,d) for d,r in exponents.items())
  assert order>0
  orders.append((c,str(order)))
 print('positive eta cusp orders:',orders)
 print('eta congruences:',sum(d*r for d,r in exponents.items())%24,sum((N//d)*r for d,r in exponents.items())%24)
print('All exact quartic checks passed. The whole-L-function modular identifications are supplied independently by Martin–Ono (1997), Theorem 2, opened primary author PDF.')
