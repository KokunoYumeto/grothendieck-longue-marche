"""Independent finite/coordinate audit of GT A.C2--C17; no source-image claim."""
from itertools import product
from collections import Counter
from pathlib import Path
import json
import sympy as sp

I=(1,0,0,1)
U=(1,1,0,1)
L=(1,0,-1,1)
R=(0,-1,1,1)
def mm(a,b,m):
 return ((a[0]*b[0]+a[1]*b[2])%m,(a[0]*b[1]+a[1]*b[3])%m,(a[2]*b[0]+a[3]*b[2])%m,(a[2]*b[1]+a[3]*b[3])%m)
def red(a,m):return tuple(x%m for x in a)
def det(a,m):return (a[0]*a[3]-a[1]*a[2])%m
def inv(a,m):
 d=pow(det(a,m),-1,m)
 return tuple(d*x%m for x in (a[3],-a[1],-a[2],a[0]))
def pw(a,n,m):
 if n<0:return pw(inv(a,m),-n,m)
 ans=I
 while n:
  if n%2:ans=mm(ans,a,m)
  a=mm(a,a,m);n//=2
 return ans
def conj(a,b,m):return mm(mm(a,b,m),inv(a,m),m)
def mv(a,v,m):return ((a[0]*v[0]+a[1]*v[1])%m,(a[2]*v[0]+a[3]*v[1])%m)
def crt34(a,b):return tuple(next(c for c in range(12) if c%3==x and c%4==y) for x,y in zip(a,b))
S=mm(mm(U,L,12),U,12);Rp=mm(U,L,12);R0=tuple(-x%12 for x in Rp)
sl3=[a for a in product(range(3),repeat=4) if det(a,3)==1]
gl3=[a for a in product(range(3),repeat=4) if det(a,3)]
ct=[a for a in sl3 if mm(a,R0,3)==mm(R0,a,3)]
cw=[a for a in sl3 if mm(a,S,3)==mm(S,a,3)]
assert len(sl3)==24 and len(gl3)==48 and len(ct)==6 and len(cw)==4
assert set(ct)=={pw(Rp,j,3) for j in range(6)}
assert set(cw)=={pw(S,j,3) for j in range(4)}
def bt(a):
 v=mv(a,(1,-1),3)
 assert v in {(1,2),(2,1)}
 return int(v==(2,1))
def bw(a):return next(j%2 for j in range(4) if a==pw(S,j,3))
counts=Counter((bt(a),bw(b)) for a in ct for b in cw)
assert set(counts.values())=={6}
normalizers={}
for name,C,bit in [('T',ct,bt),('W',cw,bw)]:
 normal=[g for g in gl3 if {conj(g,c,3) for c in C}==set(C)]
 assert all(bit(conj(g,c,3))==bit(c) for g in normal for c in C)
 normalizers[name]=len(normal)
for rho in range(12):
 V=pw(U,8*rho,12)
 f=(1,(-8*rho)%12,(-8*rho)%12,(1+64*rho*rho)%12)
 assert conj(V,S,12)==mm(S,f,12)
 assert conj(V,R0,12)==mm(inv(f,12),R0,12)
# Actual mod-four image of the signed pure subgroup.
pure4={I};todo=[I]
while todo:
 a=todo.pop()
 for g in [pw(U,2,4),pw(L,2,4)]:
  b=mm(a,g,4)
  if b not in pure4:pure4.add(b);todo.append(b)
assert len(pure4)==4 and red((-1,0,0,-1),4) not in pure4
assert [a for a in pure4 if mm(a,R0,4)==mm(R0,a,4)]==[I]
# Both integral choices CR=Rplus^epsilon C, retaining determinant.
Cs={}
for eps in [-1,1]:
 for a in product(range(-1,2),repeat=4):
  if abs(a[0]*a[3]-a[1]*a[2])!=1:continue
  am=sp.Matrix(2,2,a);rm=sp.Matrix(2,2,R);rpm=sp.Matrix(2,2,Rp)
  # Rp above is reduced mod 12; use the integral positive matrix.
  rpm=sp.Matrix([[0,1],[-1,1]])
  if am*rm==rpm**eps*am:
   Cs[eps]=a;break
 assert eps in Cs
# For every signed T,W and permitted j, a common exponent exists iff bits agree.
# We enumerate the entire allowable M3 centralizer, not actual gentle elements.
M3=[a for a in sl3 if mm(a,R,3)==mm(R,a,3) and mv(a,(1,1),3)==(1,1)]
assert len(M3)==3
rows=[]
for eps,C in Cs.items():
 for t,w,j in product(ct,cw,[0,2,4]):
  T=crt34(t,I)
  M4=pw(R,j+3*bw(w),4)
  possibilities=[]
  for m3 in M3:
   M=crt34(m3,M4)
   for k in range(6):
    if mm(T,C,12)==mm(mm(pw(Rp,k,12),C,12),M,12):
     possibilities.append((k,m3))
  assert len(possibilities)==(1 if bt(t)==bw(w) else 0)
  rows.append({'epsilon':eps,'T':t,'W':w,'j':j,'solutions':len(possibilities)})
# Explicit bad witness: T=5I, W=I.
assert bt((2,0,0,2))==1 and bw(I)==0

z,u,x,t,a,b,Z,Y,r=sp.symbols('z u x t a b Z Y r')
phi=(z-1)/(z+1)
assert sp.factor(phi**2+phi**-2-2*((z*z+z**-2)+6)/((z*z+z**-2)-2))==0
mob=2*(u+6)/(u-2)
assert sp.limit(mob,u,sp.oo)==2 and sp.limit(mob,u,2)==sp.oo and mob.subs(u,-2)==-2
D=4*a**3+27*b**2
X=(t+x*x+a)/2
Zf=X-a/3;Yf=X*x+b/2
res=sp.together(Yf**2-Zf**3-D/108)
num,den=sp.fraction(res)
quartic=t*t-x**4-2*a*x*x-4*b*x+a*a/3
assert sp.rem(num,quartic,t)==0
xi=(Y-b/2)/(Z+a/3)
ti=2*(Z+a/3)-xi*xi-a
back=sp.factor(ti*ti-xi**4-2*a*xi*xi-4*b*xi+a*a/3)
num,den=sp.fraction(back)
assert sp.rem(num,Y*Y-Z**3-D/108,Y)==0
assert sp.factor(((ti+xi*xi+a)/2-a/3)-Z)==0
assert sp.factor(((ti+xi*xi+a)/2)*xi+b/2-Y)==0
# Division fields: r^4=3/4. All expressions are checked in that exact algebra.
def rem_r(expr):
 num,den=sp.fraction(sp.cancel(expr));return sp.factor(sp.rem(num,r**4-sp.Rational(3,4),r))
sqrt3=2*r*r
aa=(1/r+2*r)/2
bb=(1/r-2*r)/(2*sp.I)
assert rem_r(sqrt3**2-3)==0
assert rem_r(3*aa**4-6*aa**2-1)==0
assert rem_r(3*bb**4-6*bb**2-1)==0
assert rem_r(sqrt3*aa*bb-sp.I)==0
assert sp.simplify(aa+sp.I*bb-1/r)==0
xp=-1+sqrt3
yp=sqrt3*(sqrt3-1)*r
assert rem_r(yp*yp-xp**3-1)==0
# Its doubling is (-1,0) on y²=x³+1.
slope=3*xp*xp/(2*yp)
xd=sp.cancel(slope*slope-2*xp)
yd=sp.cancel(slope*(xp-xd)-yp)
assert rem_r(xd+1)==0 and rem_r(yd)==0
out={
 'SL2_F3_order':len(sl3),'GL2_F3_order':len(gl3),'T_cartan_order':len(ct),'W_cartan_order':len(cw),
 'pairs_by_bits':{str(k):v for k,v in counts.items()},'normalizer_orders':normalizers,
 'finite_covariances_checked':12,'signed_pure_mod4':sorted(pure4),
 'integral_comparison_matrices':{str(k):v for k,v in Cs.items()},
 'common_exponent_cases':len(rows),'common_exponent_cases_with_solution':sum(x['solutions'] for x in rows),
 'unequal_bits_have_no_common_exponent':True,'bad_witness_T':'5I mod 12','bad_witness_W':'I',
 'crossratio_and_quartic_identities':True,'division_point_and_field_coordinate_identities':True,
 'scope':'Finite necessary matrices and algebraic identities only; no full gentle source enumeration or GT vanishing certified.'}
path=Path(__file__).with_suffix('.json');path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
