"""Check the fixed-ring indices and all three scalar-sign formulas."""
import math,json
import sympy as sp
rows=[]
for ell in sp.primerange(3,2000):
 f=int(sp.n_order(2,ell))
 for r in range(1,25):
  for sign in (1,-1):
   s=sign*pow(2,r,ell)%ell;m=int(sp.n_order(s,ell));d=f//math.gcd(f,m)
   predicted=math.gcd(f,r if sign==1 or f%2 else r+f//2)
   assert d==predicted
   H={pow(s,i,ell) for i in range(m)}
   assert (d==1)==(2 in H)
   if ell in (7,11,13) and r==2 and sign==-1:
    rows.append(dict(ell=ell,s=s,f=f,m=m,d=d,fixed_ring_field_size=2**d,
      fixed_ring_factor_count=(ell-1)//math.lcm(f,m)))
print(json.dumps({'all_odd_primes_below':2000,'scalar_exponents_checked':'1 through24, bothsigns',
 'all_formulas_pass':True,'C0_over_F16_cases':rows},indent=2))
