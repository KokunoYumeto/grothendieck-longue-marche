"""Verify saved cyclic-seven polynomials and exclude every SS factor.
No producer imports. Newton identities are checked by independent cyclic
convolution. Nondivisibility is witnessed in finite fields at split primes,
using descending polynomial division, rather than the producer's integral
power-series division. A nonzero modular remainder proves nondivisibility
in Z[zeta7][T], since the tested leading coefficient is a unit modulo p.
"""
from pathlib import Path
import gzip,json,hashlib,itertools,time
r=Path(__file__).resolve().parent;start=time.time()
spec=json.loads((r/'b5_cyclic7_complete.json').read_text())
p=r/'b5_all_f8_polynomials.json.gz'
with gzip.open(p,'rt') as f:data=json.load(f)
zero=[0]*6;one=[1,0,0,0,0,0]
def product(a,b):
 v=[0]*7
 for i,x in enumerate(a):
  for j,y in enumerate(b):v[(i+j)%7]+=x*y
 return [v[i]-v[6] for i in range(6)]
def remainder(a,b,p):
 a=a[:];iv=pow(b[-1],-1,p)
 for j in range(len(a)-len(b),-1,-1):
  z=a[j+len(b)-1]*iv%p
  if z:
   for i,c in enumerate(b):a[j+i]=(a[j+i]-z*c)%p
 return a[:len(b)-1]
primes=[29,43,71,113,127,197,211,239,281]
roots={p:next(z for z in range(2,p) if pow(z,7,p)==1) for p in primes}
counts={p:0 for p in primes};seen=set();hist={};tests=0
for rec in data:
 es=tuple(rec['exponents']);a=rec['character_coefficients'];cs=rec['power_sum_residue_counts']
 assert es[0]==1 and len(es)==9 and sum(es)%7==0 and es not in seen
 seen.add(es);rank=sum(x!=0 for x in es)-2
 assert len(a)==rank+1 and a[0]==one and 3<=len(cs)<=rank
 hist[rank]=hist.get(rank,0)+1
 ss=[[v[i]-v[6] for i in range(6)] for v in cs]
 for k in range(1,len(cs)+1):
  out=[0]*6
  for j in range(1,k+1):
   term=product(ss[j-1],a[k-j]);out=[x+y for x,y in zip(out,term)]
  assert out==[k*x for x in a[k]]
 for j in range(rank+1):
  co=[0]*7
  for i,v in enumerate(a[j]):co[(-i)%7]+=v
  co=[co[i]-co[6] for i in range(6)]
  assert [8**j*v for v in a[rank-j]]==product(a[-1],co)
 # Evaluate at one split prime until a nonzero remainder is found. A true
 # characteristic-zero divisor must divide at every valid reduction.
 image={}
 for tp in spec['templates']:
  if len(tp)>len(a):continue
  for phase in range(7):
   for p in primes:
    z=roots[p]
    if p not in image:image[p]=[sum(v[i]*pow(z,i,p) for i in range(6))%p for v in a]
    b=[c*pow(z,phase*j,p)%p for j,c in enumerate(tp)]
    if any(remainder(image[p],b,p)):
     counts[p]+=1;tests+=1;break
   else:raise AssertionError(('need another split prime',es,tp,phase))
assert len(seen)==1256
out={'verified':True,'models':len(seen),'character_degree_histogram':hist,'nondivisibility_tests':tests,
     'modular_witness_counts':{p:n for p,n in counts.items() if n},'split_roots':roots,
     'method':'independent Newton and all functional-equation identities; descending division at split primes',
     'seconds':time.time()-start}
(r/'b5_all_f8_verify.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
