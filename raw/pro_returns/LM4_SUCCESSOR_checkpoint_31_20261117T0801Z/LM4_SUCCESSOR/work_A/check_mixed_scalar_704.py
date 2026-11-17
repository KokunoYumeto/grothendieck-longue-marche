"""Exact cubic stem count for48 ordinary slots with at least one cusp row.

This is the commutator/attainment certificate for a proposed actual scalar
refinement. It does not assert the peripheral action or frame norms on
that new refinement. The old128 free-cusp block is retained explicitly.
"""
from pathlib import Path
import itertools,json
HERE=Path(__file__).resolve().parent
F=range(4);B=range(4,8);rows=range(8)
slots=[(i,j)for i in rows for j in rows if i<4 or j<4]
slotset=set(slots)
closed=[(i,j,k)for i in rows for j in rows for k in rows if sum(x<4 for x in(i,j,k))>=2]
single=[(i,j,k)for i in B for j in F for k in B]
indices=closed+single;index={t:i for i,t in enumerate(indices)}
assert len(slots)==48 and len(closed)==256 and len(single)==64
assert set(indices)=={(i,j,k)for i in rows for j in rows for k in rows if(i,j)in slotset and(j,k)in slotset}
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
def project_term(t,v):
 if t not in index or not v:return 0
 i,j,k=t
 if t in closedset:
  return(pw(v,4)<<(3*index[k,i,j]))^(pw(v,2)<<(3*index[j,k,i]))
 return v<<(3*index[t])
closedset=set(closed)
def projection(x):
 y=0
 for j,t in enumerate(indices):y^=project_term(t,(x>>(3*j))&7)
 return y
def rank(cols):
 piv={}
 for x in cols:
  while x:
   j=x.bit_length()-1
   if j not in piv:piv[j]=x;break
   x^=piv[j]
 return len(piv),piv
pc=[project_term(t,a)for t in indices for a in(1,2,4)]
assert all(projection(x)==x for x in pc)
rp,_=rank(pc);assert rp==704
basis=list(itertools.product(rows,(1,2,4)))
columns=[]
for(ra,a),(rb,b),(rc,c)in itertools.product(basis,repeat=3):
 v=0
 for t,x in [((ra,rb,rc),mul(mul(pw(a,2),b),pw(c,4))),
             ((rb,ra,rc),mul(mul(pw(b,2),a),pw(c,4))),
             ((rc,ra,rb),mul(mul(pw(c,2),a),pw(b,4))),
             ((rc,rb,ra),mul(mul(pw(c,2),b),pw(a,4)))]:
  v^=project_term(t,x)
 columns.append(v)
r,piv=rank(columns);assert r==704
oldmask=sum(7<<(3*index[t])for t in closed if all(i<4 for i in t))
ro,_=rank([x&oldmask for x in columns]);rn,_=rank([x&~oldmask for x in columns])
assert(ro,rn)==(128,576)
# The literal local cocycle cancellation used for every valid index.
for a,b,c in itertools.product(range(8),repeat=3):
 assert mul(mul(pw(a,2),b),pw(c,4))==mul(pw(a,2),pw(mul(pw(b,2),c),4))
print('Allowed ordinary slots48; cyclic-closed triple slots256; centered-one-cusp slots64: PASS')
print('Raw center960 binary bits; exact projected center704; projection idempotent: PASS')
print('All24^3 binary-basis triple commutators span704 dimensions: PASS')
print('Retained all-free scalar block128; new mixed scalar directions576: PASS')
print('All512 field cocycle cancellation identities: PASS')
out=dict(scope='Exact actual commutator target for the proposed mixed scalar cover; action/frame and source-refinement upper bound require separate proofs',
 ordinary_slots=slots,cyclic_closed_triples=closed,centered_single_cusp_triples=single,
 raw_binary_dimension=960,stem_dimension=704,old_free_dimension=128,new_mixed_dimension=576,
 tested_binary_triples=len(columns),triple_columns=columns,projection_columns=pc,
 old_free_coordinate_mask=oldmask)
(HERE/'mixed_scalar_704_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
