"""Independent Eisenstein--Kronecker derivative experiment for E1.

Computes d_z^A d_w^B Theta_{P,0}(0,0) algebraically, where
E:y^2=x^3-x, P=(i,1-i), 2P=(0,0), and
F_1(P)=zeta(P)-bar(P)/A=(1+i)/2.
This does not by itself assert a Rubin Selmer comparison.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json
# polynomials in X=wp(z+P), Y=wp'(z+P), Z=F_1(z+P), Y^2=4X^3-4X

def add(a,b):
 c=a.copy()
 for v,x in b.items():c[v]=c.get(v,Q(0))+x
 return {v:x for v,x in c.items() if x}
def scale(a,q):return {v:x*q for v,x in a.items() if x*q}
def mul(a,b):
 c={}
 for (ax,ay,az),x in a.items():
  for (bx,by,bz),y in b.items():
   v=(ax+bx,ay+by,az+bz);z=x*y
   if v[1]<2:c[v]=c.get(v,Q(0))+z
   else:
    assert v[1]==2
    for dx,e in ((3,4),(1,-4)):
     w=(v[0]+dx,0,v[2]);c[w]=c.get(w,Q(0))+e*z
 return {v:x for v,x in c.items() if x}
def deriv(a):
 c={}
 for (nx,ny,nz),x in a.items():
  if nx:c=add(c,mul({(nx-1,ny,nz):nx*x},{(0,1,0):Q(1)}))
  if ny:c=add(c,mul({(nx,0,nz):x},{(2,0,0):Q(6),(0,0,0):Q(-2)}))
  if nz:c=add(c,{(nx+1,ny,nz-1):-nz*x})
 return c
one={(0,0,0):Q(1)}
wp={(1,0,0):Q(1)}
c=[{}, {(0,0,1):Q(1)}]
for k in range(2,8):
 if k>2:wp=deriv(wp)
 ck=scale(wp,-Q(1,factorial(k)))
 if k==4:ck=add(ck,{(0,0,0):Q(1,60)})
 c.append(ck)
e=[one]
for n in range(1,8):
 p={}
 for k in range(1,n+1):p=add(p,scale(mul(c[k],e[n-k]),Q(k,n)))
 e.append(p)

def evmod(a,mod,iroot):
 # all denominators are dealt with at higher precision before reduction;
 # exact Gaussian rational evaluation avoids cancellation errors.
 def cmul(x,y):return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
 def cpow(x,n):
  z=(Q(1),Q(0))
  for _ in range(n):z=cmul(z,x)
  return z
 z=(Q(0),Q(0))
 for (a,b,c),v in a.items():
  w=cmul(cmul(cpow((Q(0),Q(1)),a),cpow((Q(2),Q(-2)),b)),cpow((Q(1,2),Q(1,2)),c))
  z=(z[0]+v*w[0],z[1]+v*w[1])
 assert all(v.denominator%5 for v in z),z
 return (int(z[0].numerator)*pow(int(z[0].denominator),-1,mod)+iroot*int(z[1].numerator)*pow(int(z[1].denominator),-1,mod))%mod,[str(v) for v in z]
rows=[]
for m in range(1,7):
 for t in range((6-m)//2+1):
  A=19-t;B=m+t
  p=scale(e[B+1],Q(factorial(B)))
  for _ in range(A):p=deriv(p)
  val,exact=evmod(p,25,18)
  # Both unit restrictions contribute Euler factors. Here the first is
  # 1 mod25 because A>=17; the second remains necessary when B=1.
  pi=(-1+2*18)%25;barpi=(-1-2*18)%25
  fac=(1-pow(pi,A,25)*pow(barpi,-B-1,25))*(1-pow(pi,B,25)*pow(barpi,-A-1,25))%25
  ans=val*fac%25
  r={'m':m,'t':t,'A':A,'B':B,'derivative_mod25':val,'Euler_factor_mod25':fac,
     'unit_restricted_moment_without_period_mod25':ans,'exact_derivative_real_imag':exact,
     'valuation_less_than_2':0 if ans%5 else (1 if ans else None)}
  rows.append(r);print(json.dumps(r))
result={'scope':'independent exact EK derivatives at P on E1; analytic interpolation and Rubin control not asserted',
        'rows':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
