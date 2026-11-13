from fractions import Fraction as F
from pathlib import Path
import json
import sympy as s

x=s.Symbol('x')
ZERO=(F(0),)*4
ONE=(F(1),F(0),F(0),F(0))
Z=(F(0),F(1),F(0),F(0))

def add(a,b):return tuple(u+v for u,v in zip(a,b))
def neg(a):return tuple(-u for u in a)
def sub(a,b):return add(a,neg(b))
def sc(a,t):return tuple(F(t)*u for u in a)
def mul(a,b):
 c=[F(0)]*7
 for i,u in enumerate(a):
  for j,v in enumerate(b):c[i+j]+=u*v
 for k in range(6,3,-1):c[k-4]-=c[k]
 return tuple(c[:4])
def inv(a):
 p=sum(s.Rational(u.numerator,u.denominator)*x**i for i,u in enumerate(a))
 q=s.Poly(s.invert(p,x**4+1),x)
 return tuple(F(q.nth(i)) for i in range(4))
def div(a,b):return mul(a,inv(b))
def power(a,n):
 if n<0:return power(inv(a),-n)
 r=ONE
 while n:
  if n&1:r=mul(r,a)
  a=mul(a,a);n//=2
 return r

SQRT2=sub(Z,power(Z,3))
assert mul(SQRT2,SQRT2)==sc(ONE,2)
table={mul(power(Z,k),power(SQRT2,n)):(k,n) for k in range(8) for n in range(-24,25)}

points=[]
for name in ('A','B','C'):
 for i in range(4):
  a=power(Z,1+2*i)
  P=(ZERO,a,ONE) if name=='A' else ((a,ZERO,ONE) if name=='B' else (a,ONE,ZERO))
  line=(ZERO,ONE,neg(a)) if name=='A' else ((ONE,ZERO,neg(a)) if name=='B' else (ONE,neg(a),ZERO))
  points.append({'name':name+str(i),'a':a,'point':P,'line':line,'kind':name})
origin=next(i for i,P in enumerate(points) if P['name']=='B0')
other=[i for i in range(12) if i!=origin]

def line_lead(i,j):
 # local parameter at A=x/z, B=y/z, C=z/y, always with tangent one.
 P=points[j];line=points[i]['line']
 if i==j:return 4,sc(P['a'],F(1,4))
 v=ZERO
 for a,b in zip(line,P['point']):v=add(v,mul(a,b))
 assert v!=ZERO
 return 0,v

def f_lead(i,j):
 n,a=line_lead(i,j);m,b=line_lead(origin,j)
 return n-m,div(a,b)

frames={}; exponents=[]
for d in other:
 _,den=f_lead(d,origin)
 row=[]; vals={}
 for q in other:
  order,value=f_lead(d,q)
  value=div(value,den)
  k,n=table[value]
  vals[points[q]['name']]={'zeta8_exponent':k,'sqrt2_exponent':n,'field_coefficients':[str(t) for t in value],'f_order':order}
  row.append(n)
 frames[points[d]['name']]=vals;exponents.append(row)
N=s.Matrix(exponents).T
print('peripheral order',[points[i]['name'] for i in other])
print('sqrt2 exponents with columns d and rows q')
print(N)
print('symmetric?',N==N.T)
orbit=[i for i in other if points[i]['kind']=='B']
v=sum((N[:,other.index(i)] for i in orbit),s.zeros(11,1))/32
print('origin v=sum v_B/4=',list(v))
out={'origin':points[origin]['name'],'peripheral_order':[points[i]['name'] for i in other],
     'frames':frames,'sqrt2_exponent_matrix':[[int(v) for v in row] for row in N.tolist()],
     'path_vectors_matrix':[[str(F(v,8)) for v in row] for row in N.tolist()],
     'averaged_origin_vector':[str(vv) for vv in v], 'symmetric':N==N.T}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
