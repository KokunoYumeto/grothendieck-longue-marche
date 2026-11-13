#!/usr/bin/env python3
"""All good (p,n), p<=50, 3<=n<=12: Jacobi sums over F_{p^ord_n(p)}.
Finite fields are exhaustively enumerated unless p^(f/2)=-1 mod n; then the
proved quadratic-extension Gauss-sum formula gives J(a,b)=p^(f/2).
Checks exact norm J*barJ=q and independent point counts whenever enumerated.
No pretend Frobenius scalar is assigned at bad reduction p|n.
"""
from pathlib import Path
from itertools import product
import subprocess,json,random,time
import sympy as s
OUT=Path(__file__).resolve().parent
z=s.symbols('z')

def mul(a,b,c,p):
 f=len(c);t=[0]*(2*f-1)
 for i,u in enumerate(a):
  for j,v in enumerate(b):t[i+j]=(t[i+j]+u*v)%p
 for k in range(2*f-2,f-1,-1):
  for j in range(f):t[k-f+j]=(t[k-f+j]-t[k]*c[j])%p
 return tuple(t[:f])
def pw(a,k,c,p):
 r=(1,)+(0,)*(len(c)-1)
 while k:
  if k&1:r=mul(r,a,c,p)
  a=mul(a,a,c,p);k//=2
 return r
def primitive_poly(p,f):
 if f==1:return [(-int(s.primitive_root(p)))%p]
 q=p**f;fac=list(s.factorint(q-1));one=(1,)+(0,)*(f-1);t=(0,1)+(0,)*(f-2)
 rng=random.Random(100*p+f)
 for tries in range(100000):
  c=[rng.randrange(1,p)]+[rng.randrange(p) for _ in range(f-1)]
  if pw(t,q-1,c,p)!=one:continue
  if any(pw(t,(q-1)//a,c,p)==one for a in fac):continue
  return c
 raise RuntimeError((p,f))
def reduce_poly(v,n):
 expr=sum(a*z**i for i,a in enumerate(v));r=s.Poly(expr,z,domain=s.ZZ).rem(s.Poly(s.cyclotomic_poly(n,z),z))
 return [int(r.nth(i)) for i in range(s.totient(n))]
def product_reduce(a,b,n):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return reduce_poly(c,n)
def conjugate(a,n):
 c=[0]*n
 for i,x in enumerate(a):c[-i%n]+=x
 return reduce_poly(c,n)
def main():
 subprocess.run(['g++','-O3','-std=c++17',str(OUT/'d_jacobi_field.cpp'),'-o',str(OUT/'d_jacobi_field')],check=True)
 rows=[];allvals={};fieldcert={};checks=0
 for p in s.primerange(2,51):
  for n in range(3,13):
   if n%p==0:
    rows.append({'p':p,'n':n,'status':'bad reduction p divides n'});continue
   f=int(s.n_order(p,n));q=int(p)**f;sem=f%2==0 and pow(int(p),f//2,n)==n-1
   # Small semiprimitive fields are also enumerated to audit the formula.
   direct=(not sem) or q<=100000
   vals={};t0=time.time();c=None;cnt=None
   if direct:
    key=f'{p}^{f}'
    if key not in fieldcert:fieldcert[key]=primitive_poly(int(p),f)
    c=fieldcert[key]
    r=subprocess.run([str(OUT/'d_jacobi_field'),str(p),str(f),str(n),*map(str,c)],check=True,capture_output=True,text=True)
    cnt=[list(map(int,line.split())) for line in r.stdout.strip().splitlines()]
    assert len(cnt)==n and all(len(a)==n for a in cnt)
    assert sum(map(sum,cnt))==q-2
   for a in range(1,n):
    for b in range(1,n):
     if (a+b)%n==0:continue
     if direct:
      coeff=[0]*n
      for i in range(n):
       for j in range(n):coeff[(a*i+b*j)%n]-=cnt[i][j]
      v=reduce_poly(coeff,n)
      if sem:assert v==[-int(p)**(f//2)]+[0]*(int(s.totient(n))-1),(p,n,a,b,v)
     else:v=[-int(p)**(f//2)]+[0]*(int(s.totient(n))-1)
     assert product_reduce(v,conjugate(v,n),n)==[q]+[0]*(int(s.totient(n))-1)
     vals[f'{a},{b}']=v;checks+=1
   twist_e=0 if p==2 else ((q-1)//2)%n
   vals_plus={k:[((-1 if twist_e else 1)**sum(map(int,k.split(','))))*c for c in v] for k,v in vals.items()}
   trace_plus=[sum(v[i] for v in vals_plus.values()) for i in range(int(s.totient(n)))]
   assert not any(trace_plus[1:]);points_plus=q+1-trace_plus[0]
   trace=[sum(v[i] for v in vals.values()) for i in range(int(s.totient(n)))]
   assert not any(trace[1:]);points=q+1-trace[0]
   if direct:
    inf=n if p==2 or (q-1)//n%2==0 else 0
    assert points==n*n*cnt[0][0]+2*n+inf,(p,n,points,cnt[0][0])
    assert points_plus==n*n*cnt[twist_e][twist_e]+(3*n if twist_e==0 else 0),(p,n,points_plus,twist_e)
   row={'p':int(p),'n':n,'f':f,'q':q,'semiprimitive':sem,'direct_enumeration':direct,'H1_dimension':(n-1)*(n-2),'trace_Frob_q':trace[0],'point_count_Fq':points,'plus_curve_twist_exponent':twist_e,'plus_curve_trace_Frob_q':trace_plus[0],'plus_curve_point_count_Fq':points_plus,'seconds':round(time.time()-t0,3)}
   rows.append(row);allvals[f'{p},{n}']={'Frob_convention':'j(a,b)=-sum chi^a(x)chi^b(1-x); arithmetic action on etale homology as in Otsubo Thm8.1','j_values_basis_1_z_to_phi_minus1':vals,'manuscript_plus_curve_j_values':vals_plus,'cyclotomic_counts':cnt}
   print(row,flush=True)
   (OUT/'d_jacobi.json').write_text(json.dumps({'coverage':rows,'values':allvals,'primitive_polynomials_low_to_high_without_monic':fieldcert,'scalar_norm_checks':checks},indent=2))
 print('Complete coverage for p<=50 and levels3..12. Levels1,2 have H1(projective)=0; no nondegenerate character pairs. Bad reduction rows explicitly retained.')
if __name__=='__main__':main()
