"""Independent certificate checker using pure Python binary-field arithmetic.

It does not import the C++ field helper or the searcher's Cartier routine.
The tangent interpolation is recomputed from N(v)/u and h^{-1} mod u.
"""
from pathlib import Path
import sys,json,time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'code'))
from finite_jacobian import PolynomialRing,Jacobian
ROOT=Path(__file__).resolve().parents[1]/'code'
def red(a,b):
 while a.bit_length()>=b.bit_length():a^=b<<(a.bit_length()-b.bit_length())
 return a
def gcd(a,b):
 while b:a,b=b,red(a,b)
 return a
def square_poly(a):
 z=0;j=0
 while a:
  if a&1:z^=1<<(2*j)
  j+=1;a>>=1
 return z
def irreducible(f):
 n=f.bit_length()-1;pr=[];m=n;d=2
 while d*d<=m:
  if m%d==0:
   pr.append(d)
   while m%d==0:m//=d
  d+=1
 if m>1:pr.append(m)
 tests={n//p for p in pr};a=2
 for i in range(1,n+1):
  a=red(square_poly(a),f)
  if i in tests and gcd(a^2,f)!=1:return False
 return a==2
class PureField:
 def __init__(self,mod):
  assert irreducible(mod)
  self.modulus=mod;self.m=mod.bit_length()-1;self.q=1<<self.m
 def mul(self,a,b):
  z=0
  while b:
   if b&1:z^=a
   b>>=1;a<<=1
   if a&self.q:a^=self.modulus
  return z
 def sq(self,a):return red(square_poly(a),self.modulus)
 def inv(self,a):
  assert a
  u,v=a,self.modulus;g,h=1,0
  while u!=1:
   j=u.bit_length()-v.bit_length()
   if j<0:u,v=v,u;g,h=h,g;j=-j
   u^=v<<j;g^=h<<j
  return red(g,self.modulus)
 def div(self,a,b):return self.mul(a,self.inv(b))
 def power(self,a,n):
  out=1
  while n:
   if n&1:out=self.mul(out,a)
   a=self.sq(a);n>>=1
  return out
 def frob(self,a,n):
  for _ in range(n):a=self.sq(a)
  return a
 def sqrt(self,a):return self.frob(a,self.m-1)
def pair(x):return tuple(tuple(p) for p in x)
def independent_double(J,D):
 R,F=J.R,J.F;u,v=D;r=len(u)-1
 gg,hh,_=R.xgcd(J.h,u)
 if len(gg)==2:
  assert r==2
  out=J.add(D,D)
  return out,(J.h[2] if len(J.h)>2 else 0),'branch'
 assert gg==(1,)
 n0=R.add(R.add(R.sq(v),R.mul(J.h,v)),J.f)
 t=R.mod(R.mul(R.exact(n0,u),hh),u)
 vv=R.add(v,R.mul(u,t))
 nn=R.add(R.add(R.sq(vv),R.mul(J.h,vv)),J.f)
 uu=R.sq(u)
 assert not R.mod(nn,uu)
 if r==1:
  return (uu,vv),(J.h[1] if len(J.h)>1 else 0),'one_two'
 w=R.exact(nn,uu);uj=R.monic(w);vj=R.mod(R.add(J.h,vv),uj)
 if len(uj)==2:return (uj,vj),1,'two_one'
 assert len(uj)==3 and len(vv)==4
 return (uj,vj),F.mul(vv[3],uj[1]),'two_two'
def poly_linear_product(F,roots):
 c=[1]
 for a in roots:
  out=[0]*(len(c)+1)
  for j,v in enumerate(c):out[j]^=v;out[j+1]^=F.mul(v,a)
  c=out
 return c
def verify(name):
 start=time.time();o=json.loads((ROOT/name).read_text())
 F=PureField(o['field_modulus']);R=PolynomialRing(F)
 assert F.sq(o['alpha'])^o['alpha']^1==0
 J=Jacobian(F,o['h'],o['f']);ell=o['ell'];d=2*o['base_field_degree_over_F4']
 c=next(c for c in o['candidates'] if c.get('relative_class_number_mod2')==1)
 D=pair(c['torsion_divisor']);ds=[pair(x) for x in c['multiples']]
 assert D!=J.zero and ds[0]==J.zero and ds[1]==D
 assert len(set(ds))==ell
 for i in range(ell):
  assert J.valid(ds[i])
  assert J.add(ds[i],D)==ds[(i+1)%ell]
 assert J.scale(D,ell)==J.zero
 frob=tuple(tuple(F.frob(v,d) for v in p) for p in D)
 assert frob==J.scale(D,pow(2,d,ell))
 coeff=[0]*ell;cases={}
 for i in range(1,ell):
  out,a,case=independent_double(J,ds[i])
  assert out==ds[(2*i)%ell]
  assert a==c['doubling_coefficients'][i]
  coeff[i]=a;cases[case]=cases.get(case,0)+1
 As=[]
 for i in range(1,ell):
  a=1;j=i
  for _ in range(d):a=F.mul(F.sq(a),coeff[j]);j=2*j%ell
  assert j==pow(2,d,ell)*i%ell
  As.append(a)
 assert As==c['q_power_coefficients'] and all(a!=1 for a in As)
 for i in range(1,ell):
  assert As[2*i%ell-1]==F.sq(As[i-1])
  assert As[ell-i-1]==As[i-1]
 lambdas=[F.frob(a,F.m-d) for a in As]
 pol=poly_linear_product(F,lambdas)
 assert all(a in(0,1) for a in pol) and sum(pol)%2==1
 first=lambdas[0];orbit=[];a=first
 while a not in orbit:orbit.append(a);a=F.sq(a)
 assert a==first
 minrec=poly_linear_product(F,orbit)
 assert all(a in (0,1) for a in minrec)
 return {'file':name,'field_degree':F.m,'prime':ell,'base_degree_over_F4':d//2,
  'pure_Python_field_irreducibility':True,'exact_order_and_Frobenius_verified':True,
  'all_multiples_verified':ell,'independent_interpolation_cases':cases,
  'all_coefficients_recomputed':ell-1,'all_values_not_one':True,
  'linear_Frobenius_q_root_applied':True,'relative_zeta_mod2_exponents':[i for i,a in enumerate(pol) if a],
  'relative_class_number_mod2':1,'first_linear_scalar':first,
  'first_scalar_F2_degree':len(orbit),
  'first_scalar_reciprocal_minpoly_exponents':[i for i,a in enumerate(minrec) if a],
  'seconds':time.time()-start}
if __name__=='__main__':
 out=[verify(x) for x in ['bielliptic_mixed_ell11_F4pow60.json','bielliptic_mixed_ell113_F4pow16.json']]
 print(json.dumps(out,indent=2))

