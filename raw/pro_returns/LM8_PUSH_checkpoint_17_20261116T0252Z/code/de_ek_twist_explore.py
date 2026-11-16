"""Exact modulo-25 EK derivative traces for the conductor-12 CM twist.
Exploratory certificate: arithmetic orbit and Rubin control audited separately.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json
MOD=25;d2=36

def pa(a,b):
 c=a.copy()
 for v,x in b.items():c[v]=c.get(v,Q(0))+x
 return {v:x for v,x in c.items() if x}
def ps(a,q):return {v:x*q for v,x in a.items() if x*q}
def pm(a,b):
 c={}
 for (ax,ay,az),x in a.items():
  for (bx,by,bz),y in b.items():
   v=(ax+bx,ay+by,az+bz);z=x*y
   if v[1]<2:c[v]=c.get(v,Q(0))+z
   else:
    assert v[1]==2
    for dx,e in ((3,4),(1,-4*d2)):
     w=(v[0]+dx,0,v[2]);c[w]=c.get(w,Q(0))+e*z
 return {v:x for v,x in c.items() if x}
def pd(a):
 c={}
 for (nx,ny,nz),x in a.items():
  if nx:c=pa(c,pm({(nx-1,ny,nz):nx*x},{(0,1,0):Q(1)}))
  if ny:c=pa(c,pm({(nx,0,nz):x},{(2,0,0):Q(6),(0,0,0):Q(-2*d2)}))
  if nz:c=pa(c,{(nx+1,ny,nz-1):-nz*x})
 return c
onep={(0,0,0):Q(1)};wp={(1,0,0):Q(1)}
c=[{}, {(0,0,1):Q(1)}]
for k in range(2,8):
 if k>2:wp=pd(wp)
 ck=ps(wp,-Q(1,factorial(k)))
 if k==4:ck=pa(ck,{(0,0,0):Q(d2,60)})
 c.append(ck)
e=[onep]
for n in range(1,8):
 p={}
 for k in range(1,n+1):p=pa(p,ps(pm(c[k],e[n-k]),Q(k,n)))
 e.append(p)
# Etale algebra Z/25[r,v]/(r^2-2,v^8-6v^4-3), rank16.
class F:
 def __init__(self,c=0):self.c=tuple([c%MOD]+[0]*15) if isinstance(c,int) else tuple(x%MOD for x in c)
 def __add__(a,b):
  if not isinstance(b,F):b=F(b)
  return F([x+y for x,y in zip(a.c,b.c)])
 __radd__=__add__
 def __neg__(a):return F([-x for x in a.c])
 def __sub__(a,b):return a+-b if isinstance(b,F) else a+(-b)
 def __rsub__(a,b):return -a+b
 def __mul__(a,b):
  if not isinstance(b,F):b=F(b)
  o=[0]*16
  for i,x in enumerate(a.c):
   if not x:continue
   for j,y in enumerate(b.c):
    if not y:continue
    ir,iv=divmod(i,8);jr,jv=divmod(j,8)
    z=x*y*(2 if ir+jr==2 else 1);rr=(ir+jr)%2;n=iv+jv
    stack=[(n,z)]
    while stack:
     n,z=stack.pop()
     if n<8:o[8*rr+n]+=z
     else:stack.extend([(n-4,6*z),(n-8,3*z)])
  return F(o)
 __rmul__=__mul__
 def __pow__(a,n):
  if n<0:return a.inverse()**(-n)
  z=F(1)
  while n:
   if n%2:z=z*a
   a=a*a;n//=2
  return z
 def inverse(a):
  mat=[]
  cols=[]
  for j in range(16):
   b=[0]*16;b[j]=1;cols.append((a*F(b)).c)
  mat=[[cols[j][i] for j in range(16)]+[int(i==0)] for i in range(16)]
  for j in range(16):
   k=next(k for k in range(j,16) if mat[k][j]%5)
   mat[j],mat[k]=mat[k],mat[j]
   v=pow(mat[j][j],-1,MOD);mat[j]=[x*v%MOD for x in mat[j]]
   for i in range(16):
    if i!=j:
     v=mat[i][j];mat[i]=[(x-v*y)%MOD for x,y in zip(mat[i],mat[j])]
  ans=F([mat[i][-1] for i in range(16)])
  assert a*ans==F(1)
  return ans
 def __truediv__(a,b):
  if not isinstance(b,F):b=F(b)
  return a*b.inverse()
 def __eq__(a,b):
  if not isinstance(b,F):b=F(b)
  return a.c==b.c
 def trace(a):return (16*a.c[0]+48*a.c[4])%MOD
v=F([0,1]+[0]*14);r=F([0]*8+[1]+[0]*7)
assert r*r==2 and v**8-6*v**4-3==0
s=(v**4-3)/2;u=v**2/s
assert s*s==3 and u*u==1+2*s/3
Q3=(6*u,12*v);Q4=(6*(1+r),12*s*(1+r))

def ecadd(A,B):
 if A is None:return B
 if B is None:return A
 x,y=A;xx,yy=B
 if x==xx and y==-yy:return None
 slope=(3*x*x-d2)/(2*y) if A==B else (yy-y)/(xx-x)
 z=slope*slope-x-xx;return z,slope*(x-z)-y

def ecneg(A):return A[0],-A[1]
def oncurve(A):return A is None or A[1]*A[1]==A[0]**3-d2*A[0]
assert oncurve(Q3) and oncurve(Q4)
assert ecadd(ecadd(Q3,Q3),Q3) is None
assert ecadd(Q4,Q4)==(F(6),F(0))
P=ecadd(ecneg(Q4),Q3);P2=ecadd(P,P);P3=ecadd(P2,P)
assert P3==Q4 and oncurve(P)
X,ystd=P;Y=2*ystd;X2,Y2=P2[0],2*P2[1];X3,Y3=P3[0],2*P3[1]
Z=(- (6*X3*X3-2*d2)/(4*Y3) - (6*X*X-2*d2)/(2*Y) - (Y2-Y)/(2*(X2-X)))/3
powers=[[F(1)] for _ in range(3)]
for i,a in enumerate((X,Y,Z)):
 for n in range(40):powers[i].append(powers[i][-1]*a)
rows=[]
for m in (1,3,5):
 for t in range((6-m)//2+1):
  A=19-t;B=m+t;p=ps(e[B+1],Q(factorial(B)))
  for _ in range(A):p=pd(p)
  assert all(z.denominator==1 for z in p.values())
  value=F(0)
  for (a,b,c),z in p.items():value=value+int(z)*powers[0][a]*powers[1][b]*powers[2][c]
  val=value.trace()
  pi=(-1+2*18)%25;barpi=(-1-2*18)%25
  # psi_6 at 5 equals psi_1 at 5.
  fac=(1-pow(pi,A,25)*pow(barpi,-B-1,25))*(1-pow(pi,B,25)*pow(barpi,-A-1,25))%25
  ans=val*fac%25
  row={'m':m,'t':t,'A':A,'B':B,'trace_derivative_mod25':val,'Euler_factor_mod25':fac,
       'trace_restricted_moment_without_unit_period_mod25':ans,
       'valuation_less_than_2':0 if ans%5 else (1 if ans else None)}
  rows.append(row);print(json.dumps(row))
result={'scope':'EK derivative traces in explicit rank16 etale algebra; ray-class identification and Rubin control separate',
 'checks':{'Q3_order3':True,'Q4_double_6_0':True,'3P_Q4':True,'all_derivative_polynomials_integral':True},
 'X':X.c,'Y':Y.c,'Z':Z.c,'rows':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
