"""Independent raw attainment and exact Frobenius-cyclic stem projection.

f_ijk=z_ij*b_k^4+a_i^2*w_jk^4, with raw values in F8^64.
Only the actual triple-commutator image is computed here; the full
central-refinement upper bound and norm are separate arguments.
"""
from pathlib import Path
import itertools,json
HERE=Path(__file__).resolve().parent
def mul(a,b):
 r=0
 while b:
  if b&1:r^=a
  b>>=1;a<<=1
  if a&8:a^=11
 return r
def pw(a,n):
 r=1
 for _ in range(n):r=mul(r,a)
 return r
def proj(a):return pw(a,2)^pw(a,4)
ix=list(itertools.product(range(4),repeat=3))
AB=[tuple(v if j==i else 0 for j in range(4))for i in range(4)for v in(1,2,4)]
def tr(a,b,c):
 return tuple(mul(mul(pw(a[i],2),b[j])^mul(pw(b[i],2),a[j]),pw(c[k],4))^
                   mul(pw(c[i],2),pw(mul(pw(a[j],2),b[k])^mul(pw(b[j],2),a[k]),4))
              for i,j,k in ix)
def pack(v):
 return sum(x<<(3*i)for i,x in enumerate(v))
idx={v:i for i,v in enumerate(ix)}
def sigma(v):
 # Push t at(i,j,k) to t^2 at(j,k,i).
 return tuple(pw(v[idx[k,i,j]],2)for i,j,k in ix)
def va(a,b):return tuple(x^y for x,y in zip(a,b))
def norm(v):return va(va(v,sigma(v)),sigma(sigma(v)))
def projection(v):return va(sigma(v),sigma(sigma(v)))
def insert(piv,x):
 while x:
  q=x.bit_length()-1
  if q not in piv:piv[q]=x;return True
  x^=piv[q]
 return False
piv={};naive={};basis=[];labels=[]
for i,a in enumerate(AB):
 for j,b in enumerate(AB):
  for k,c in enumerate(AB):
   v=tr(a,b,c);assert norm(v)==(0,)*64
   x=pack(v);orig=x
   if insert(piv,x):basis.append(orig);labels.append((i,j,k))
   insert(naive,pack(tuple(proj(x)for x in v)))
print('Raw generalized64 scalar coordinates; triple-image binary rank:',len(piv))
assert len(piv)==128
assert len(naive)==88
print('Rejected coordinatewise trace-zero projection loses40 directions: rank88.')
npiv={};qpiv={}
for i in range(64):
 for a in(1,2,4):
  v=tuple(a if j==i else 0 for j in range(64))
  assert sigma(sigma(sigma(v)))==v
  assert norm(norm(v))==norm(v)
  assert projection(projection(v))==projection(v)
  assert norm(projection(v))==(0,)*64
  insert(npiv,pack(norm(v)));insert(qpiv,pack(projection(v)))
assert len(npiv)==64 and len(qpiv)==128
print('Cyclic-Frobenius fixed complement rank64 and canonical stem projection rank128: PASS')
print('All128 stem scalar directions attained by actual third commutators: PASS')
# The defining cocycle identity follows by cancellation of the common
# monomial a_i^2*b_j*c_k^4.  Check its exact field identity on all triples.
for a,b,c in itertools.product(range(8),repeat=3):
 assert mul(mul(pw(a,2),b),pw(c,4))==mul(pw(a,2),pw(mul(pw(b,2),c),4))
print('Exact cocycle cancellation identity on all512 field triples: PASS')
out=dict(scope='Actual generalized-cocycle central quotient lower bound; full scalar upper bound separate',
 coefficient='F8^64 modulo Fix(sigma), sigma pushes t_(i,j,k) to t^2_(j,k,i)',
 scalar_coordinates=ix,binary_A_basis=AB,triple_image_rank=128,
 rejected_coordinatewise_projection_rank=88,
 fixed_complement_rank=64,canonical_projection_rank=128,
 attaining_triple_labels=labels,attaining_vectors=basis,
 cocycle_identity_checked=True)
(HERE.parent/'generalized_scalar_triple_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
