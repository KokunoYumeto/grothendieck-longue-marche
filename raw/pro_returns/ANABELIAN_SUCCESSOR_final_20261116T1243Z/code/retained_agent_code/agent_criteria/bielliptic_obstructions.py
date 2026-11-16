"""Exact certificates for c=alpha,alpha² in y²+y=x+c/(x²+x).

This verifies the elementary small-prime theta elimination, the complete
mod5 Frobenius-vector period cases, and elliptic-order gcds through degree16.
It does NOT claim existence of a witness at degree16 or refute A3.
"""
import sys,json,math
from pathlib import Path
from itertools import product
from collections import Counter
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'code'))
from finite_jacobian import BinaryField,PolynomialRing,Jacobian
F=BinaryField(7);R=PolynomialRing(F);x=(0,1);one=(1,)
certs=[]
for c in (2,3):
 h=(0,1,1);f=R.mul(h,R.add(R.mul(x,h),(c,)))
 J=Jacobian(F,h,f)
 N4=len(J.points());h4=len(J.enumerate())
 assert (N4,h4)==(7,32)
 elliptic_counts=[]
 for a in (3,2):
  number=2+sum(len(F.artin.get(F.mul(a,u)^F.div(c,u),[])) for u in range(1,4))
  elliptic_counts.append(number)
 assert sorted(elliptic_counts)==[4,8]
 # Order3 comparison r²+r=1 and r³=c forces c=1.
 q3=(1,1,1);last3=(c,0,0,1)
 assert R.xgcd(q3,last3)[0]==(1,)
 # Order5: Q=0 and U²+sE²=0; the remainder is (c+1)(r²+r).
 Q=(c^1,1,0,0,1)
 ss=R.scale((0,0,0,0,0,1),F.inv(c))
 E=R.add(ss,(1,1));B=(c^1,1)
 U=R.add(R.add(B,R.sq(E)),R.mul((1,1),ss))
 obstruction=R.add(R.sq(U),R.mul(ss,R.sq(E)))
 rem=R.mod(obstruction,Q)
 assert rem==(0,c^1,c^1)
 # cQ+(c+1)(r²+r+1)*rem=1.
 identity=R.add(R.scale(Q,c),R.mul(R.scale((1,1,1),c^1),rem))
 assert identity==(1,)
 certs.append({'c':c,'h':h,'f':f,'C_points4':N4,'C_J_order4':h4,
               'elliptic_points4':elliptic_counts,'theta3_gcd':[1],
               'theta5_Q':Q,'s':ss,'E':E,'B':B,'U':U,
               'obstruction':obstruction,'remainder':rem,'Bezout_result':identity})

periods=[]
for jordan in (0,1):
 def act(v):
  a,b,c,d=v
  return ((3*a+jordan*b)%5,3*b%5,d%5,(c+2*d)%5)
 hist=Counter();scalars=Counter()
 for v in product(range(5),repeat=4):
  if not any(v):continue
  z=act(v);m=1
  while z!=v:
   z=act(z);m+=1
   assert m<=60
  assert m in (4,12,20,60)
  d=m//4;z=v
  for _ in range(d):z=act(z)
  possible=[a for a in (2,3) if z==tuple(a*t%5 for t in v)]
  assert len(possible)==1
  hist[m]+=1;scalars[(m,possible[0])]+=1
 periods.append({'Jordan_nonzero':bool(jordan),'vectors_checked':624,
                 'period_histogram':dict(hist),
                 'period_scalar_counts':[[m,a,n] for (m,a),n in sorted(scalars.items())]})

periods7=[]
for jordan in (0,1):
 def act7(v):
  a,b,c,d=v
  return ((2*a+jordan*b)%7,2*b%7,3*d%7,(c+d)%7)
 hist=Counter()
 for v in product(range(7),repeat=4):
  if not any(v):continue
  z=act7(v);m=1
  while z!=v:
   z=act7(z);m+=1
   assert m<=168
  d={3:1,21:7,24:16,168:112}[m]
  z=v
  for _ in range(d):z=act7(z)
  assert z==tuple(2*a%7 for a in v)
  assert 3*d//m in (1,2) and 3*d%m==0
  hist[m]+=1
 for j in range(4):
  v=tuple(int(i==j) for i in range(4));z=v
  for _ in range(112):z=act7(z)
  assert z==tuple(2*a%7 for a in v)
 periods7.append({'Jordan_nonzero':bool(jordan),'vectors_checked':2400,
                  'period_histogram':dict(hist),'Frobenius112_scalar':2})

def order_mod(a,p):
 z=a%p;n=1
 while z!=1:z=z*a%p;n+=1
 return n
assert order_mod(3,11)==order_mod(5,11)==5
v=(1,0);z=(0,1);order11=1
while z!=v:z=(-4*z[1]%11,(z[0]+z[1])%11);order11+=1
assert order11==60

tr1=[2,-3];tr2=[2,1];table=[]
for n in range(2,17):
 tr1.append(-3*tr1[-1]-4*tr1[-2])
 tr2.append(tr2[-1]-4*tr2[-2])
for n in range(1,17):
 n1=4**n+1-tr1[n];n2=4**n+1-tr2[n]
 gcd=math.gcd(n1,n2);odd=gcd
 while odd%2==0:odd//=2
 table.append({'extension_degree_over_F4':n,'E1_order':n1,'E2_order':n2,
               'gcd':gcd,'odd_gcd':odd})
assert all(t['odd_gcd'] in (1,3,135) for t in table[:15])
assert [t['extension_degree_over_F4'] for t in table[:15] if t['odd_gcd']==135]==[12]
assert table[15]['odd_gcd']==3*113

def multiplicative_order(a,p):
 z=a%p;n=1
 while z!=1:z=z*a%p;n+=1
 return n
roots=[]
for trace in (-3,1):
 roots.append({'trace':trace,'roots_mod113':[[a,multiplicative_order(a,113)]
  for a in range(1,113) if (a*a-trace*a+4)%113==0]})
print(json.dumps({'curve':'y^2+y=x+c/(x^2+x), c=alpha oralpha² inF4',
                  'small_prime_certificates':certs,
                  'Frobenius_polynomial_ascending':[16,8,5,2,1],
                  'elliptic_Frobenius_factors_ascending':[[4,3,1],[4,-1,1]],
                  'mod5_complete_period_cases':periods,
                  'mod7_complete_period_cases':periods7,
                  'mod11_elliptic_eigenvalue_orders':[5,60],
                  'elliptic_order_gcd_table':table,
                  'first_remaining_mixed_prime_at_degree16':roots,
                  'proved_conclusions':['no nonconstant odd witness overF4 at infinity',
                   'no cubic orquintic witness over any extension at infinity',
                   'no constant odd witness overF4^m for1<=m<=15',
                   'at m16 theonlypossible prime is113'],
                  'unproved':'existence at degree16; universal A3; any global absence of prime witnesses'},indent=2))
