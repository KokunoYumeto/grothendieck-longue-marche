"""Exact identities and all-depth tame congruences for A162."""
from pathlib import Path
from fractions import Fraction as F
import json,sys
import sympy as sp
sys.set_int_max_str_digits(0)
base=Path(__file__).resolve().parent
d=649;rad=3*d**6

def add(x,y):return[a+b for a,b in zip(x,y)]
def scale(x,c):return[a*c for a in x]
def mul(x,y,a):
 n=len(x);z=[F(0)]*(2*n-1)
 for i,v in enumerate(x):
  for j,w in enumerate(y):z[i+j]+=v*w
 for k in range(2*n-2,n-1,-1):z[k-n]+=a*z[k]
 return z[:n]
def pw(x,k,a):
 z=[F(1)]+[F(0)]*(len(x)-1)
 while k:
  if k&1:z=mul(z,x,a)
  x=mul(x,x,a);k//=2
 return z

def inv(x,a):
 n=len(x);X=sp.symbols('X');pol=sum(sp.Rational(v.numerator,v.denominator)*X**i for i,v in enumerate(x))
 z=sp.Poly(sp.invert(pol,X**n-a),X)
 return[F(z.nth(i))for i in range(n)]
def embed(x):
 z=[F(0)]*9
 for i,v in enumerate(x):z[3*i]=v/F(d**(2*i))
 return z

def normrel(x):
 A,B,C=[[x[j+3*k]*d**(2*k)for k in range(3)]for j in range(3)]
 w=[F(0),F(d*d),F(0)]
 return add(add(pw(A,3,3),mul(w,pw(B,3,3),3)),add(mul(pw(w,2,3),pw(C,3,3),3),scale(mul(w,mul(mul(A,B,3),C,3),3),-3)))
def norm3(x):
 a,b,c=x;return a**3+3*b**3+9*c**3-9*a*b*c

gamma={11:[F(2),F(1),F(0)],59:[F(2),F(2),F(-1)]}
h={}
for q,g in gamma.items():
 assert norm3(g)==q
 h[q]=scale(pw(inv(g,3),3,3),q)
 assert norm3(h[q])==1
old=json.loads((base/'two_inert_norm2_generator_certificate_data.json').read_text())
beta2=[-F(x,old['generator_common_denominator'])for x in old['generator_numerators']]
beta1=[F(1),F(-1),F(0)]
f=mul(h[11],pw(h[59],2,3),3)
b2=mul(beta2,embed(f),rad)
b1=mul(beta1,pw(f,3,3),3)
assert normrel(beta2)==beta1
assert normrel(b2)==b1 and norm3(b1)==-2
rows=[]
for q,exponent in [(11,1),(59,2)]:
 r=next(x for x in range(q)if x**3%q==3)
 def times(x,y):
  a,b=x;c,e=y
  return((a*c-r*r*b*e)%q,(a*e+b*c-r*b*e)%q)
 def power(x,k):
  k%=q*q-1;z=(1,0)
  while k:
   if k&1:z=times(z,x)
   x=times(x,x);k//=2
  return z
 def eval3(x):
  z=(0,0)
  for v in reversed(x):
   z=times(z,(0,1));z=((z[0]+v.numerator*pow(v.denominator,-1,q))%q,z[1])
  return z
 omega=(10,6)if q==11 else(58,6)
 beta_res=(6,3)if q==11 else(23,57)
 alpha=(0,1);m=(q*q-1)//3;assert m%3
 dp=d//q
 rad_unit=times((pow(dp,-8,q),0),power(alpha,-5))
 h_unit=times(times((pow(dp,-4,q),0),power(alpha,-2)),power(eval3(gamma[q]),-3))
 other=59 if q==11 else 11
 other_res=eval3(h[other]);assert power(other_res,m)==(1,0)
 unit_res=times(times(beta_res,power(h_unit,exponent)),power(other_res,2 if other==59 else 1))
 val=3*exponent
 assert power(unit_res,m)==(1,0)
 for depth in range(1,13):
  e=3**depth;A=pow(8,-1,e);B=(1-8*A)//e
  assert 8*A+e*B==1
  test=times(power(unit_res,m),power(power(rad_unit,m),-A*val))
  assert test==(1,0)
  assert sp.gcd(e,q*q-1)==3
 print('q',q,'quadratic valuation',val,'normalized unit residue',unit_res,'cube character1 at all tested depths1..12')
 rows.append({'q':q,'valuation':val,'normalized_unit_residue':unit_res,'radicand_unit_residue':rad_unit,'h_exponent':exponent})
 # Exact absolute norm-zero divisor contribution.
 assert -6*exponent+2*(3*exponent)==0
out={'d':d,'h11':[str(x)for x in h[11]],'h59':[str(x)for x in h[59]],'changed_beta1':[str(x)for x in b1],'changed_beta2':[str(x)for x in b2],'norm_relative':[str(x)for x in normrel(b2)],'norm_absolute':-2,'local_rows':rows}
(base/'two_inert_changed_seed_certificate_data.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: literal gamma norms11/59; h norms1; N(beta2*)=beta1*; N(beta1*)=-2.')
print('PASS: exact q-divisor norms, both stable characters, 24 explicit Bezout/depth checks.')
