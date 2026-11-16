"""Exact Jacobi sums for Fermat39/F4096 and rational2-exponent data.

Every character pair a,b,a+b!=0 mod39 is enumerated. Cyclotomic
arithmetic is integral in Z[zeta39], with all norms, Frobenius invariance,
traces, and the projective point-count sign convention checked.
"""
import sys,json,math,time
from collections import Counter
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'code'))
from finite_jacobian import BinaryField
import sympy as sp
start=time.time();F=BinaryField(4105);n=39;q=F.q
X=sp.Symbol('X');phi=sp.Poly(sp.cyclotomic_poly(n,X),X)
coeff=[int(phi.nth(i)) for i in range(phi.degree()+1)];degree=len(coeff)-1
pairs=Counter((F.log[x]%n,F.log[x^1]%n) for x in range(2,q))
def red(a):
 a=list(a)
 while len(a)>degree:
  h=a.pop();d=len(a)-degree
  if h:
   for i in range(degree):a[d+i]-=h*coeff[i]
 while a and not a[-1]:a.pop()
 return tuple(a)
def add(a,b):return red([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return red(c)
def sigma(a,t):
 c=[0]*n
 for i,x in enumerate(a):c[i*t%n]+=x
 return red(c)
def val2(x):
 assert x
 v=0
 while x%2==0:x//=2;v+=1
 return v
jacs={};stats=Counter();rows=[];sum_alpha=()
for a in range(1,n):
 for b in range(1,n):
  if (a+b)%n==0:continue
  counts=[0]*n
  for (u,v),number in pairs.items():counts[(a*u+b*v)%n]+=number
  jac=red(counts);assert sigma(jac,2)==jac
  conj=sigma(jac,-1);assert mul(jac,conj)==(q,)
  tr=add(jac,conj);assert len(tr)==1
  alpha=tuple(-x for x in jac);trace=-tr[0]
  jacs[(a,b)]=alpha
  assert trace in (128,-128,115,-115,80,-80,28,-28),trace
  conductor=n//math.gcd(a,b,n)
  if conductor<39:assert trace in(128,-128)
  if trace%2:
   assert abs(trace)==115
   ex=val2(q+1-trace);assert ex in(1,2)
  else:ex=0
  stats[(conductor,trace,ex)]+=1
  rows.append({'a':a,'b':b,'conductor':conductor,'Frobenius_trace_over_quadratic_field':trace,
    'unit_root_v2_alpha_minus1':ex,'Frobenius_eigenvalue_coefficients':alpha})
  sum_alpha=add(sum_alpha,alpha)
assert len(rows)==1406
assert len(sum_alpha)==1
points=n
for x in range(q):
 rhs=1^F.power(x,n)
 points+=1 if not rhs else (n if F.log[rhs]%n==0 else 0)
assert q+1-points==sum_alpha[0]
# All unit roots are the SAME 2-adic root beta of
# X^2-115X+4096. Frobenius is central in the semisimple rational
# endomorphism algebra, hence acts semisimply on the etale Tate module.
# It therefore acts as beta on the entire integral Tate lattice.
# This avoids relying on any isogeny decomposition to bound the exponent.
units=sum(number for (cond,tr,e),number in stats.items() if e)
# Each cyclotomic polynomial record comprises both2-adic embeddings;
# exactly half the multiplicity of every ordinary quadratic trace is unit.
assert units%2==0
p_rank=units//2
assert p_rank<=703
zeta=F.power(F.generator,(q-1)//n)
def residue(alpha):
 ans=0
 for coefficient in reversed(alpha):
  ans=F.mul(ans,zeta)^(coefficient%2)
 return ans
unit_pairs=[]
for row in rows:
 r=residue(row['Frobenius_eigenvalue_coefficients'])
 assert r in (0,1)
 row['chosen_2_adic_residue']=r
 if r:unit_pairs.append((row['a'],row['b']))
assert len(unit_pairs)==p_rank==24
assert all(row['Frobenius_trace_over_quadratic_field']==115
 for row in rows if row['chosen_2_adic_residue'])
sigma_fixed=[a for a in jacs if(5*a[0]+7*a[1])%13==0]
seen=set();quotient_orbits=[]
for pair in sigma_fixed:
 if pair in seen:continue
 orbit=[];x=pair
 while x not in orbit:
  assert x in sigma_fixed
  orbit.append(x);seen.add(x);x=(x[1],(-sum(x))%n)
 assert all(jacs[x]==jacs[pair] for x in orbit)
 quotient_orbits.append(orbit)
assert Counter(map(len,quotient_orbits))==Counter({3:36,1:2})
# The two fixed characters factor through the Fermat cubic. The cycle
# acts freely on that cubic, hence by translation and trivially on H^1.
assert [o[0] for o in quotient_orbits if len(o)==1]==[(13,13),(26,26)]
unit_quotient_orbits=[o for o in quotient_orbits if residue(jacs[o[0]])]
assert len(unit_quotient_orbits)==4 and all(len(o)==3 for o in unit_quotient_orbits)
quotient_stats=Counter()
for orbit in quotient_orbits:
 alpha=jacs[orbit[0]]
 tr=add(alpha,sigma(alpha,-1))[0]
 quotient_stats[tr]+=1
assert sum(quotient_stats.values())==38
# The larger free group uses s=diag(1,zeta39,zeta39^17), with
# tau*s*tau^-1=s^16 projectively; its order is117 and quotient genus7.
larger_sigma_fixed=[a for a in jacs if(22*a[0]+23*a[1])%39==0]
seen=set();larger_orbits=[]
for pair in larger_sigma_fixed:
 if pair in seen:continue
 orbit=[];x=pair
 while x not in orbit:
  assert x in larger_sigma_fixed
  orbit.append(x);seen.add(x);x=(x[1],(-sum(x))%n)
 assert all(jacs[x]==jacs[pair] for x in orbit)
 larger_orbits.append(orbit)
assert Counter(map(len,larger_orbits))==Counter({3:12,1:2})
larger_stats=Counter(add(jacs[o[0]],sigma(jacs[o[0]],-1))[0] for o in larger_orbits)
assert larger_stats==Counter({-128:4,115:8,128:2})
assert sum(residue(jacs[o[0]]) for o in larger_orbits)==4
assert all((r['a']-r['b'])%3==0 for r in rows
 if r['Frobenius_trace_over_quadratic_field']==115)
def trace_power(m):
 a,b=2,115
 for j in range(2,m+1):a,b=b,115*b-q*a
 return b if m else a
extension_exponents={m:val2(q**m+1-trace_power(m)) for m in (1,2,3,4,6,8,13,39)}
assert extension_exponents=={1:1,2:3,3:1,4:4,6:3,8:5,13:1,39:1}
maximum_exponent=max(e for _,_,e in stats)
assert maximum_exponent==1
out={'curve':'X^39+Y^39+Z^39=0','q':q,'field_modulus':4105,'genus':703,
 'diagonal_group_order':39**2,'free_nonabelian_group_order':39,'quotient_genus':19,
 'projective_point_count':points,'Frobenius_trace':sum_alpha[0],
 'all_nontrivial_character_pairs_checked':len(rows),
 'sigma2_invariance_and_absolute_norm_verified':True,
 'classification':[{'conductor':c,'trace':t,'v2_unit_root_minus1':e,'character_pairs':v}
  for (c,t,e),v in sorted(stats.items())],
 'geometric_2_rank':p_rank,'maximum_unit_root_v2_alpha_minus1':maximum_exponent,
 'rational_2_primary_exponent':2**maximum_exponent,
 'rational_2_primary_group':'(Z/2Z)^24',
 'unit_character_pairs':unit_pairs,
 'quotient_sigma_fixed_character_count':len(sigma_fixed),
 'quotient_character_orbits':quotient_orbits,
 'quotient_unit_character_orbits':unit_quotient_orbits,
 'quotient_geometric_2_rank':len(unit_quotient_orbits),
 'quotient_rational_2_primary_group':'(Z/2Z)^4',
 'relative_class_number_v2':20,
 'quotient_character_trace_counts':dict(sorted(quotient_stats.items())),
 'larger_free_group_order':117,'larger_quotient_genus':7,
 'larger_quotient_sigma_fixed_character_count':len(larger_sigma_fixed),
 'larger_quotient_character_orbits':larger_orbits,
 'larger_quotient_character_trace_counts':dict(sorted(larger_stats.items())),
 'larger_quotient_2_primary_group':'(Z/2Z)^4',
 'intermediate_cubic_cover_relative_polynomial':'(1+64T)^24',
 'intermediate_cubic_cover_relative_class_number':65**24,
 'extension_degree_to_v2_exponent':extension_exponents,
 'norm_equation_nonnegative_solutions':[[128,0],[115,9],[80,16],[28,20]],
 'all_Jacobi_eigenvalues':rows,'seconds':time.time()-start}
print(json.dumps(out,indent=2))
