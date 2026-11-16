"""Find and exactly certify a relative-unit repair from local PARI output.

The computer algebra output is used only to supply candidate elements.  Every
unit, relative norm, residue and final positive identity is checked here.
No completeness of the computed unit or class group is asserted.
"""
from pathlib import Path
from fractions import Fraction as F
from math import lcm,gcd
import json,re,itertools,sys
sys.set_int_max_str_digits(0)
import sympy as sp
import mpmath as mp

base=Path(__file__).resolve().parent
d=649;rad=3*d**6

def add(x,y):return [a+b for a,b in zip(x,y)]
def scale(x,c):return [a*c for a in x]
def mul(x,y,a):
 n=len(x);z=[F(0)]*(2*n-1)
 for i,v in enumerate(x):
  for j,w in enumerate(y):z[i+j]+=v*w
 for k in range(2*n-2,n-1,-1):z[k-n]+=a*z[k]
 return z[:n]
def power(x,k,a):
 assert k>=0
 z=[F(1)]+[F(0)]*(len(x)-1)
 while k:
  if k&1:z=mul(z,x,a)
  x=mul(x,x,a);k//=2
 return z

def matrix(x,a):
 n=len(x);cols=[]
 for i in range(n):
  e=[F(0)]*n;e[i]=F(1);cols.append(mul(x,e,a))
 return sp.Matrix([[sp.Rational(cols[j][i].numerator,cols[j][i].denominator) for j in range(n)]for i in range(n)])
def normrel(x):
 A,B,C=[[x[j+3*k]*d**(2*k) for k in range(3)]for j in range(3)]
 w=[F(0),F(d*d),F(0)]
 return add(add(power(A,3,3),mul(w,power(B,3,3),3)),add(mul(power(w,2,3),power(C,3,3),3),scale(mul(w,mul(mul(A,B,3),C,3),3),-3)))
def embed(x):
 z=[F(0)]*9
 for i,v in enumerate(x):z[3*i]=v/F(d**(2*i))
 return z
U=[F(-2),F(0),F(1)];Ui=[F(4),F(3),F(2)]
assert mul(U,Ui,3)==[1,0,0]
def upower(k):return power(U,k,3)if k>=0 else power(Ui,-k,3)
def uexponent(x):
 digits=max(len(str(abs(v.numerator)))+len(str(v.denominator)) for v in x)
 mp.mp.dps=3*digits+120
 alpha=mp.root(3,3)
 z=sum(mp.mpf(v.numerator)/v.denominator*alpha**i for i,v in enumerate(x))
 assert z>0
 k=int(mp.nint(mp.log(z)/mp.log(alpha**2-2)))
 assert upower(k)==x,(k,x)
 return k

def finite(q):
 root=next(r for r in range(q)if r**3%q==3)
 def times(x,y):
  a,b=x;c,e=y
  return ((a*c-root*root*b*e)%q,(a*e+b*c-root*b*e)%q)
 def pw(x,k):
  z=(1,0)
  while k:
   if k&1:z=times(z,x)
   x=times(x,x);k//=2
  return z
 def ev(poly):
  z=(0,0)
  for v in reversed(poly):
   assert v.denominator%q
   z=times(z,(0,1));z=((z[0]+v.numerator*pow(v.denominator,-1,q))%q,z[1])
  return z
 def residue(x):
  parts=[[x[j+3*k]*d**(2*k)for k in range(3)]for j in range(3)]
  # The three ramification valuation classes are different: 0,2,1 mod3.
  for row in parts[:2]:assert all(v.denominator%q for v in row)
  for v in parts[2]:assert (v.denominator//gcd(v.denominator,q))%q
  return ev(parts[0])
 return times,pw,residue

raw=(base/'two_inert_relative_units_pari_output.txt').read_text()
found=re.findall(r'^UNIT (\d+) (\[.*\])$',raw,re.M)
assert found,raw[-500:]
rows=[]
for index,txt in found:
 u=[F(x.strip())for x in txt.strip('[]').split(',')]
 u += [F(0)]*(9-len(u));assert len(u)==9
 ch=matrix(u,rad).charpoly().all_coeffs()
 assert all(v.q==1 for v in ch)and abs(ch[-1])==1
 norm=-int(ch[-1])
 if norm==-1:
  u=scale(u,-1)
  ch=[v*(-1)**j for j,v in enumerate(ch)]
 assert ch[-1]==-1
 rel=normrel(u);k=uexponent(rel)
 assert k%3==0
 v=mul(u,embed(upower(-k//3)),rad)
 assert normrel(v)==[1,0,0]
 chars=[];residues=[]
 for q in (11,59):
  times,pw,res=finite(q);r=res(v)
  assert pw(r,3)==(1,0)
  chi=pw(r,(q*q-1)//3)
  omega=(10,6)if q==11 else(58,6)
  j=next(j for j in range(3)if pw(omega,j)==chi)
  chars.append(j);residues.append(r)
 rows.append({'index':int(index),'normalizing_sign':norm,'candidate':[str(x)for x in u], 'unit_charpoly':[int(v)for v in ch], 'relative_norm_U_exponent':k,'relative_norm_one_unit':[str(x)for x in v], 'quadratic_residues':residues,'character_column':chars})
 print('UNIT',index,'relative exponent',k,'normalized character column',chars,flush=True)
solution=next((e for e in itertools.product(range(3),repeat=len(rows))if all(sum(e[i]*rows[i]['character_column'][j]for i in range(len(rows)))%3==2 for j in range(2))),None)
print('REPAIR EXPONENTS',solution,flush=True)
result={'d':d,'radicand':rad,'units':rows,'repair_exponents':solution}
if solution is not None:
 v=[F(1)]+[F(0)]*8
 for e,row in zip(solution,rows):v=mul(v,power([F(x)for x in row['relative_norm_one_unit']],e,rad),rad)
 assert normrel(v)==[1,0,0]
 old=json.loads((base/'two_inert_norm2_generator_certificate_data.json').read_text())
 beta=[-F(x,old['generator_common_denominator'])for x in old['generator_numerators']]
 repaired=mul(beta,v,rad)
 assert normrel(repaired)==[1,-1,0]
 for q in (11,59):
  times,pw,res=finite(q)
  assert pw(res(repaired),(q*q-1)//3)==(1,0)
 result['repair_unit']=[str(x)for x in v]
 result['repaired_beta2']=[str(x)for x in repaired]
 print('PASS: explicit integral relative norm-one unit repairs both stable cubic residue characters.')
else:
 print('NO POSITIVE REPAIR among these explicit units; no completeness or impossibility conclusion.')
(base/'two_inert_relative_unit_repair_certificate_data.json').write_text(json.dumps(result,indent=2)+'\n')
