"""Exact verification of the Fermat-septic map and a positive L-value bound.

No table of ranks or L-values is read.  The analytic formula uses the
identification of the target with X_0(49) proved in Elkies, sections 2.1, 4.2.
"""
from fractions import Fraction as F
from math import factorial
import sympy as s

a,b,c=s.symbols('a b c')
X,Y,Z=a**3*c,b**3*a,c**3*b
K=X**3*Y+Y**3*Z+Z**3*X
assert s.expand(K-a**3*b**3*c**3*(a**7+b**7+c**7))==0
x,y,z=s.symbols('x y z')
e1=x+y+z; e2=x*y+y*z+z*x; e3=x*y*z
K0=x**3*y+y**3*z+z**3*x
K1=x**3*z+z**3*y+y**3*x
assert s.expand(e2**4+e3*(e1**5-5*e1**3*e2+e1*e2**2+7*e1**2*e3)-K0*K1)==0
den=e1*e3
xx=-e2**2/den
yy=(2*e1**2*e2-5*e2**2)/den
num=s.factor(s.together(yy**2-4*xx**3-21*xx**2-28*xx)*den**3)
assert s.expand(num-4*e2**2*K0*K1)==0
u,v=s.symbols('u v')
assert s.expand((2*v+u)**2-(4*(u-2)**3+21*(u-2)**2+28*(u-2))-4*(v*v+u*v-u**3+u*u+2*u+1))==0
print('Fermat septic -> Klein quartic identity: PASS')
print('Klein quartic -> y^2=4x^3+21x^2+28x identity: PASS')
print('Minimal equation v^2+uv=u^3-u^2-2u-1: PASS')

# Exact local certificates for the two 2-isogeny descents.
sq={n*n%16 for n in range(16)}
for title,form in [
 ('E: excluded squareclass 2',lambda U,V:2*U**4+21*U*U*V*V+56*V**4),
 ('E dual: excluded squareclass -1',lambda U,V:-U**4-42*U*U*V*V+7*V**4)]:
 vals=sorted({form(U,V)%16 for U in range(16) for V in range(16) if U%2 or V%2})
 assert not sq.intersection(vals)
 print(title, 'primitive residues', vals, '; square residues',sorted(sq),': PASS')

# Fourier coefficients from exact point counts of the minimal equation.
M=30
aps={}
for p in list(s.primerange(2,M+1)):
 count=1+sum((V*V+U*V-U**3+U*U+2*U+1)%p==0 for U in range(p) for V in range(p))
 aps[p]=int(p+1-count)
assert aps[7]==0
def coeff(n):
 out=1
 for p,k in s.factorint(n).items():
  p=int(p); k=int(k)
  if p==7:
   ak=0
  else:
   aa,bb=1,aps[p]
   for j in range(2,k+1): aa,bb=bb,aps[p]*bb-p*aa
   ak=bb
  out*=ak
 return out
an=[coeff(n) for n in range(1,M+1)]

# 333/106 < pi < 355/113.  Alternating series bounds for exp(-t), 0<t<1.
def expneg_bounds(t):
 lo=sum((-t)**k/F(factorial(k)) for k in range(60)) # last exponent 59
 hi=lo+t**60/F(factorial(60))
 return lo,hi
rlo=expneg_bounds(F(2,7)*F(355,113))[0]
rhi=expneg_bounds(F(2,7)*F(333,106))[1]
lo=F(0);hi=F(0)
for n,aa in enumerate(an,1):
 if aa>=0: lo+=2*F(aa,n)*rlo**n; hi+=2*F(aa,n)*rhi**n
 else: lo+=2*F(aa,n)*rhi**n; hi+=2*F(aa,n)*rlo**n
# |a_n| <= d(n)*sqrt(n) <= 2n, so both omitted tails <= this quantity.
tail=4*rhi**(M+1)/(1-rhi)
lo-=tail; hi+=tail
assert lo>F(1,10) and hi<F(12,10)
print('a_1,...,a_30 =',an)
print('Rigorous L(E,1) rational interval is contained in [1/10, 6/5].')
print('For display only, outward-rounded interval: [%.9f, %.9f]'%(float(lo)-1e-9,float(hi)+1e-9))
print('Tail bound <',float(tail))
print('Certified nonvanishing: PASS')
