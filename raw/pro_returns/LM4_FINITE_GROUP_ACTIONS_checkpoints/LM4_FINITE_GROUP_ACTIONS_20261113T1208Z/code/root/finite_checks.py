"""Exact finite certificates for LM4 Parts D/E/F. Python standard library only."""
import itertools,json,math
from fractions import Fraction
from pathlib import Path
out={}
# Matrix operations over the integers, with finite boxes used ONLY to find candidates;
# the paper proves that the displayed centralizers exhaust GL(2,Z).
def mul(A,B): return tuple(sum(A[2*i+k]*B[2*k+j] for k in range(2)) for i in range(2) for j in range(2))
def det(A):return A[0]*A[3]-A[1]*A[2]
I=(1,0,0,1)
def power(A,n):
 B=I
 for _ in range(n): B=mul(B,A)
 return B
def order(A,limit=24):
 for k in range(1,limit+1):
  if power(A,k)==I:return k
 return None
R4=(0,-1,1,0); R6=(0,-1,1,1)
for name,R,n in [('C4',R4,4),('C6',R6,6)]:
 mats=[A for A in itertools.product(range(-2,3),repeat=4) if abs(det(A))==1]
 central=[A for A in mats if mul(A,R)==mul(R,A)]
 inv=power(R,n-1)
 normal=[A for A in mats if mul(A,R) in [mul(R,A),mul(inv,A)]]
 assert len(central)==n and len(normal)==2*n
 assert set(central)=={power(R,k) for k in range(n)}
 def apply(A,v):return tuple(sum(A[2*i+j]*v[j] for j in range(2))%1 for i in range(2))
 # All exceptional points: unions of nonzero fixed sets of nonidentity powers.
 points=set()
 for k in range(1,n):
  M=power(R,k); d=abs(det((M[0]-1,M[1],M[2],M[3]-1)))
  if not d:continue
  for a,b in itertools.product(range(d),repeat=2):
   v=(Fraction(a,d),Fraction(b,d))
   if v!=(0,0) and apply(M,v)==v:points.add(v)
 kernel=[k for k in range(n) if all(apply(power(R,k),v)==v for v in points)]
 out[name]={'R':R,'centralizer_count':len(central),'normalizer_count':len(normal),'exceptional_points':[list(map(str,v)) for v in sorted(points)],'pointwise_kernel_powers':kernel}
assert out['C4']['pointwise_kernel_powers']==[0,2]
assert out['C6']['pointwise_kernel_powers']==[0]
# Heisenberg finite quotients certify normalized two-cycle and three-cycle equations.
# Coordinates x^a y^b z^c use matrix coordinates (a,b,c), multiplication below.
def heis(p):
 def m(u,v):return((u[0]+v[0])%p,(u[1]+v[1])%p,(u[2]+v[2]+u[0]*v[1])%p)
 def inv(u):return((-u[0])%p,(-u[1])%p,(-u[2]+u[0]*u[1])%p)
 def pw(u,k):
  v=(0,0,0)
  for _ in range(k%p):v=m(v,u)
  return v
 def comm(u,v):return m(m(m(u,v),inv(u)),inv(v))
 x=(1,0,0);y=(0,1,0);z=inv(m(x,y));zero=(0,0,0)
 rows=[]
 for lam in range(1,p):
  mm=(lam-1)*pow(2,-1,p)%p
  kk=(lam*lam-1)*pow(24,-1,p)%p
  f=lambda u,v:pw(comm(u,v),kk)
  two=m(f(y,x),f(x,y))
  three=zero
  for t in [f(z,x),pw(z,mm),f(y,z),pw(y,mm),f(x,y),pw(x,mm)]:three=m(three,t)
  assert two==zero and three==zero
  F=lambda v:(lam*v[0]%p,lam*v[1]%p,lam*lam*v[2]%p)
  elems=list(itertools.product(range(p),repeat=3))
  assert len({F(v) for v in elems})==p**3
  assert all(F(m(u,v))==m(F(u),F(v)) for u in elems for v in [x,y,z])
  o=next(j for j in range(1,p) if pow(lam,j,p)==1)
  rows.append({'lambda':lam,'m':mm,'commutator_exponent':kk,'automorphism_order':o,'two_cycle':two,'three_cycle':three})
 return rows
out['heisenberg']={str(p):heis(p) for p in [5,7,11]}
assert out['heisenberg']['5'][1]['automorphism_order']==4
# Character of the two lifts in the modular free product, visible on C6 abelianization.
out['C6_abelianization']=[{'lambda_mod6':u,'order2_generator_image':(3*u)%6,'order3_generator_image':(2*u)%6,'commuting_order3_lift':u%3==1} for u in [1,5]]
# Perfect finite group available as a quotient of F2 (warns against reconstructing full
# profinite elements from separate pro-p quotients).
def perm_mul(a,b):return tuple(a[b[i]] for i in range(len(a)))
def perm_inv(a):return tuple(a.index(i) for i in range(len(a)))
def perm_gen(gs):
 n=len(gs[0]);S={tuple(range(n))};queue=list(S)
 while queue:
  a=queue.pop()
  for b in gs:
   c=perm_mul(a,b)
   if c not in S:S.add(c);queue.append(c)
 return S
x=(1,2,3,4,0); y=(1,2,0,3,4)
A5=perm_gen([x,y]);assert len(A5)==60
comm=[perm_mul(perm_mul(perm_mul(a,b),perm_inv(a)),perm_inv(b)) for a in A5 for b in A5]
assert len(perm_gen(list(set(comm))))==60
out['A5']={'order':60,'derived_order':60,'consequence':'Each homomorphism A5 to a finite p-group is trivial; pro-p quotient tests alone do not test all finite quotients.'}
# Finite shadow of (Z_3 semidirect Z_2) x product_{ell != 2,3} Z_ell.
def mixed_mul(u,v):
 return ((u[0]+(-1 if u[1]%2 else 1)*v[0])%3,(u[1]+v[1])%4)
mixed=list(itertools.product(range(3),range(4)))
assert all(mixed_mul(mixed_mul(a,b),c)==mixed_mul(a,mixed_mul(b,c))
           for a in mixed for b in mixed for c in mixed)
L={u for u in mixed if u[1]%2==0}
v=(0,0); powers=[]
for k in range(6):
 powers.append(v);v=mixed_mul(v,(1,2))
assert set(powers)==L and v==(0,0)
assert mixed_mul((0,1),(1,0)) != mixed_mul((1,0),(0,1))
out['mixed_prime_normalizer']={
 'finite_quotient_order':len(mixed),'open_cyclic_subgroup_order':len(L),
 'cyclic_generator':[1,2],'cyclic_powers':powers,
 't_times_a':mixed_mul((0,1),(1,0)),
 'a_times_t':mixed_mul((1,0),(0,1)),
 'inverse_limit_torsion_free':'Proved in D.21 by projection to torsion-free Z_2 and remaining factors.'}
# Finite CRT prefixes of alpha_2=0, alpha_ell=1 at odd primes.
crt=[]
for k in range(1,6):
 two=2**k;odd=(3*5*7)**k;mod=two*odd
 a=(two*pow(two,-1,odd))%mod
 assert a%two==0 and a%odd==1
 crt.append({'k':k,'modulus':mod,'residue':a,
             'two_primary_residue':a%two,'odd_primary_residue':a%odd})
assert all(crt[k+1]['residue']%crt[k]['modulus']==crt[k]['residue']
           for k in range(len(crt)-1))
deck={'0':'0','infinity':'infinity','1':'-1','-1':'1'}
partition_a=[['0','1'],['infinity','-1']]
partition_b=[[deck[x] for x in pair] for pair in partition_a]
assert partition_b==[['0','-1'],['infinity','1']]
out['nonextending_discretization']={
 'alpha_crt_prefixes':crt,'curve_a_partition':partition_a,
 'deck_image_curve_b_partition':partition_b,
 'pure_abelianization':'(alpha,-alpha), nonintegral by D.15'}
text=json.dumps(out,indent=2)
Path(__file__).with_suffix('.json').write_text(text+'\n')
print(text)
