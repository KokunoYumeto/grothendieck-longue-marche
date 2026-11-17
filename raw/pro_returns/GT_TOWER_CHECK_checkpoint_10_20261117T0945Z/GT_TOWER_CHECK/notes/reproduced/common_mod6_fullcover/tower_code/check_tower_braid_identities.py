#!/usr/bin/env python3
"""Exact checks of discrete words used in EXIT_TOWER E9, E28, E31, E43.
Artin free-group action is faithful. No finite shadow is inferred to lift to GT.
"""
from fractions import Fraction
from functools import lru_cache

def red(w):
 out=[]
 for x in w:
  if out and out[-1]==-x: out.pop()
  else: out.append(x)
 return tuple(out)
def inv(w): return tuple(-x for x in reversed(w))
def mul(*words): return red(x for w in words for x in w)
def power(w,n): return mul(*([w if n>=0 else inv(w)]*abs(n)))
def subst(w,images): return mul(*(images[x-1] if x>0 else inv(images[-x-1]) for x in w))
def compose(f,g): return tuple(subst(w,g) for w in f)
def sigma(n,i):
 j=abs(i); im=[(k,) for k in range(1,n+1)]
 if i>0: im[j-1]=(j,j+1,-j); im[j]=(j,)
 else: im[j-1]=(j+1,); im[j]=(-(j+1),j,j+1)
 return tuple(im)
@lru_cache(None)
def artin(n,w):
 im=tuple((k,) for k in range(1,n+1))
 for i in w: im=compose(im,sigma(n,i))
 return im

def eq(label,n,lhs,rhs):
 assert artin(n,tuple(lhs))==artin(n,tuple(rhs)),label
 print('PASS',label)

def A(i,j):return tuple(range(j-1,i,-1))+(i,i)+tuple(-k for k in range(i+1,j))

def comm(x,y):return mul(x,y,inv(x),inv(y))

a,b,d=(1,),(2,),(3,)
X,Y,Z=power(a,2),power(b,2),power(d,2)
U=mul(d,b,power(a,2),inv(b),inv(d))
V=power(mul(a,b,a),2)
W=power(mul(d,b,d),2)
omega=power(mul(a,b,d),4)
e2=mul(d,b,a,inv(b),inv(d))
for i in (1,2):eq('Artin braid relation '+str(i),4,(i,i+1,i),(i+1,i,i+1))
eq('E94 row a,W',4,power(mul(a,W),2),mul(omega,Z))
eq('E94 row e2,W',4,power(mul(e2,W),2),mul(omega,Y))
eq('E94 row e2,V',4,power(mul(e2,V),2),mul(omega,Y))
eq('E94 row d,V',4,power(mul(d,V),2),mul(omega,X))
eq('E94 UWV',4,mul(U,W,V),mul(omega,Y))
for name,p,q in [('X,Z',X,Z),('Y,U',Y,U),('Y,V',Y,V),('Y,W',Y,W),('V,X',V,X),('V,Y',V,Y),('W,Y',W,Y),('W,Z',W,Z)]:eq('E96 commutation '+name,4,comm(p,q),())
eq('E98 V=X*x13*Y',4,V,mul(X,A(1,3),Y))
eq('E98 W=Y*x24*Z',4,W,mul(Y,A(2,4),Z))
eq('E202 (uw²)²=(uw)³',3,power((1,2,2),2),power((1,2),3))
# First-strand doubling g: sigma1² -> sigma2 sigma1² sigma2;
# sigma_j -> sigma_{j+1} for j >=2.
g_x14=(4,3,2,1,1,2,-3,-4)
eq('E28 g(x14)=x15*x25',5,g_x14,mul(A(1,5),A(2,5)))
eq('E28 g(x24)=x35',5,(4,3,3,-4),A(3,5))
eq('E28 g(x34)=x45',5,(4,4),A(4,5))
# Free product D4=* C2: reduced words use four positive symbols.
def invol_red(w):
 out=[]
 for x in w:
  if out and out[-1]==x:out.pop()
  else:out.append(x)
 return tuple(out)
def invol_sub(w,ims):return invol_red(x for i in w for x in ims[i-1])
def artin_invol(w):
 im=tuple((j,) for j in range(1,5))
 for i in w:
  sig=[(j,) for j in range(1,5)]
  sig[i-1]=(i+1,);sig[i]=(i+1,i,i+1)
  im=tuple(invol_sub(x,sig) for x in im)
 return im
c=(1,2,3,4)
# The right action convention reverses the displayed conjugation convention;
# determine and report exactly which conjugation occurs.
full=artin_invol((1,2,3)*4)
plus=tuple(invol_red(c+(j,)+tuple(reversed(c))) for j in range(1,5))
minus=tuple(invol_red(tuple(reversed(c))+(j,)+c) for j in range(1,5))
assert full in (plus,minus)
print('PASS E9 full twist is inner by', 'c' if full==plus else 'c^-1','in the declared right action convention')
# Cyclotomic finite correction: Q[z]/(z^4+1).
def cyc_red(w):
 out=[0]*4
 for e,coeff in enumerate(w):
  q,r=divmod(e,4);out[r]+=coeff*(-1)**q
 return tuple(out)
def cyc_mul(x,y):
 raw=[0]*7
 for i,a0 in enumerate(x):
  for j,b0 in enumerate(y):raw[i+j]+=a0*b0
 return cyc_red(raw)
def zpow(k):
 k%=8;q,r=divmod(k,4);v=[0]*4;v[r]=(-1)**q;return tuple(v)
def add(x,y):return tuple(a0+b0 for a0,b0 in zip(x,y))
sqrt2=add(zpow(1),zpow(-1))
assert cyc_mul(sqrt2,sqrt2)==(2,0,0,0)
print('PASS (z+z^-1)^2=2 in Q[z]/(z^4+1)')
for lam in (1,3,5,7):
 val=add(zpow(lam),zpow(-lam))
 sign=1 if val==sqrt2 else -1
 assert val==tuple(sign*a0 for a0 in sqrt2)
 assert sign==(-1)**((lam*lam-1)//8)
 print('Kummer compatibility chi mod8=',lam,'forces rho2 mod2=',(0 if sign==1 else 1))
print('All exact checks passed. No assertion of a full GT lift is inferred from these computations.')
