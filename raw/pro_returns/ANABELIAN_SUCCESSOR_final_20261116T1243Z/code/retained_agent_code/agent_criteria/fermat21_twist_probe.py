"""An unsuccessful smaller-degree comparison: exact Fermat21 Jacobi data.
The commuting projective cubic diagonal twist cannot remove the exponent8
obstruction, because bad unit roots already occur on its invariant part.
"""
import sys,math,json
from pathlib import Path
from collections import Counter
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'code'))
from finite_jacobian import BinaryField
import sympy as s
F=BinaryField(67);q=64;n=21;x=s.Symbol('x');ph=s.Poly(s.cyclotomic_poly(n,x),x);cf=[int(ph.nth(i)) for i in range(ph.degree()+1)];degree=len(cf)-1
pairs=Counter((F.log[x]%n,F.log[x^1]%n) for x in range(2,q))
def red(a):
 a=list(a)
 while len(a)>degree:
  z=a.pop();d=len(a)-degree
  if z:
   for i in range(degree):a[d+i]-=z*cf[i]
 while a and not a[-1]:a.pop()
 return tuple(a)
def sig(a,j):
 c=[0]*n
 for i,z in enumerate(a):c[(i*j)%n]+=z
 return red(c)
def add(a,b):return red([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def v2(x):
 a=0
 while x%2==0:a+=1;x//=2
 return a
S=Counter();twist=Counter();bad=[]
for a in range(1,n):
 for b in range(1,n):
  if (a+b)%n==0:continue
  z=[0]*n
  for (i,j),r in pairs.items():z[(a*i+b*j)%n]-=r
  z=red(z);assert sig(z,2)==z
  t=add(z,sig(z,-1));assert len(t)==1
  tr=t[0];S[(n//math.gcd(a,b,n),tr,v2(q+1-tr) if tr%2 else 0)]+=1
  if tr%2:
   twist[(tr,(a-b)%3)]+=1
   if tr==9 and(a-b)%3==0:bad.append((a,b))
out={'q':64,'degree':21,'genus':190,'free_nonabelian_group_order':21,'quotient_genus':10,
 'classification':[dict(conductor=c,trace=t,unit_v2=e,count=v) for(c,t,e),v in sorted(S.items())],
 'ordinary_characters_by_trace_and_cubic_twist_weight':[dict(trace=t,weight=w,count=v) for(t,w),v in sorted(twist.items())],
 'invariant_bad_characters':bad,'exponent':8,'criterion_holds':21>(8-1)**2}
print(json.dumps(out,indent=2))
