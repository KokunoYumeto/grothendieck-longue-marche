#!/usr/bin/env python3
"""Small-factor verification of a research-only fixed-lifting countermodel.
The group A5^6 is never enumerated. Fixed-coordinate equations reduce the
centralizer image exactly to a subgroup of S3.
"""
from itertools import permutations,product
from pathlib import Path
import json,hashlib

def mul(p,q):return tuple(p[q[i]] for i in range(len(p)))
def inv(p):
 o=[0]*len(p)
 for i,j in enumerate(p):o[j]=i
 return tuple(o)
def conj(g,x):return mul(mul(inv(g),x),g)
def comm(p,q):return mul(mul(mul(p,q),inv(p)),inv(q))
def even(p):return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2==0
def generated(gens,identity):
 seen={identity};todo=[identity]
 while todo:
  x=todo.pop()
  for g in gens:
   y=mul(x,g)
   if y not in seen:seen.add(y);todo.append(y)
 return seen
R=list(permutations(range(3)));er=(0,1,2);A=[p for p in permutations(range(5)) if even(p)];ea=tuple(range(5))
t=(1,0,2);u=(1,0,3,2,4)
assert len(R)==6 and len(A)==60 and mul(t,t)==er and mul(u,u)==ea and u!=ea
C={comm(a,b) for a,b in product(A,repeat=2)}
assert generated(C,ea)==set(A)
assert generated([conj(r,t) for r in R],er)==set(R)
# The left/right index action, and inversion implementing the swap.
def act(a,b,x):return mul(mul(a,x),inv(b))
for a,b,c,d,x in product(R,repeat=5):
 assert act(a,b,act(c,d,x))==act(mul(a,c),mul(b,d),x)
 assert inv(act(a,b,x))==act(b,a,inv(x))
fixed=[x for x in R if inv(x)==x];pairs=[];used=set(fixed)
for x in R:
 if x not in used:pairs.append((x,inv(x)));used.add(x);used.add(inv(x))
assert len(fixed)==4 and len(pairs)==1
m={x:(u if x==t else ea) for x in R}
assert all(m[x]==m[inv(x)] and mul(m[x],m[x])==ea for x in R)
# n=(f,(r,r)) centralizes sigma=m*sigma0 iff
# f_x*m_(r^-1 x r)=m_x*f_(x^-1) at all6 coordinates.
rows=[];image=[]
for r in R:
 local=[];count=1
 for x in fixed:
  y=conj(r,x)
  sols=[f for f in A if mul(f,m[y])==mul(m[x],f)]
  local.append({'index':x,'transported_index':y,'number_of_solutions':len(sols)})
  count*=len(sols)
 for x,y in pairs:
  # All active m coordinates are fixed points, so these two equations
  # identify f_x=f_y and have exactly |A| solutions.
  assert m[x]==m[y]==m[conj(r,x)]==m[conj(r,y)]==ea
  count*=len(A)
 expected=conj(r,t)==t
 assert (count>0)==expected
 if expected:
  image.append(r)
  # Pure diagonal representative is an actual fixed lift.
  assert all(m[conj(r,x)]==m[x] for x in R)
 rows.append({'diagonal_head':r,'fixed_coordinate_checks':local,'full_fiber_solution_count':count,'has_fixed_lift':expected})
assert len(image)==2 and not all(conj(r,x) in image for r in R for x in image)
# Coordinate kernels in R x R intersect trivially and commute. Their
# inverse images in N intersect in M; their mutual commutator contains
# [M,M]=M, proved factorwise above, and is contained in M.
KA={(a,er) for a in R};KB={(er,b) for b in R}
assert KA&KB=={(er,er)}
for a in R:
 for b in R:assert (mul(a,er),mul(er,b))==(mul(er,a),mul(b,er))
out={'scope':'Research-only finite algebraic countermodel; not an actual surface quotient',
     'R':'S3','M':'A5^R','N':'M semidirect (R x R)',
     'N_order':60**6*36,'M_order':60**6,
     'twist_support':t,'A5_involution':u,
     'action':'(a,b):x->a*x*b^-1; sigma0 swaps(a,b),x->x^-1',
     'sigma_square':'identity because sigma0(m)=m and m^2=1',
     'A5_derived_order':len(generated(C,ea)),
     'intersection':'N_A intersect N_B=M=[N_A,N_B]',
     'first_relative_module':'M/[M,N]=1 because M is perfect',
     'fixed_diagonal_image':image,'fixed_diagonal_image_order':len(image),
     'normal_closure_in_R_order':len(generated([conj(r,t) for r in R],er)),
     'centralizer_total_order':sum(x['full_fiber_solution_count'] for x in rows),
     'exact_small_factor_checks':rows,
     'enumerated_groups':['S3 (6 elements)','A5 (60 elements)'],
     'not_enumerated':'A5^6 or N',
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path('work_CE/perfect_kernel_fixed_lifting_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS A5 perfect; support involution and swap action exactly verified.')
print('PASS N_A intersect N_B=M=[N_A,N_B], by coordinate quotient and factorwise perfectness.')
print('PASS all6 diagonal heads: fixed-lift image exactly C_S3(t), order2; its normal closure is all S3.')
print('PASS relative first module M/[M,N] is trivial, yet fixed lifting is not onto.')
print('Only groups of orders6 and60 enumerated; no actual-surface conclusion.')
