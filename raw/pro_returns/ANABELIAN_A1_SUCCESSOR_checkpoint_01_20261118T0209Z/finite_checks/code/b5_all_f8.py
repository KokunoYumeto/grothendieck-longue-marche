"""Extend the cyclic-seven search to every F8-rational branch pattern.
The last two branch counts are reduced by PGL2(F8). Functional equations
recover the high coefficients from a nonzero matched pair, reducing the
required finite-field sums. All computed counts and recovery data are saved.
"""
import csv,json,time,itertools,gzip
from pathlib import Path
import numpy as np
from flint import fmpq_poly
r=Path(__file__).resolve().parent;start=time.time();Phi=fmpq_poly([1]*7)
mods={3:11,6:67,9:529,12:4179,15:32771,18:(1<<18)|(1<<7)|1,21:(1<<21)|(1<<2)|1}
zero=(0,)*6;one=(1,0,0,0,0,0)
def red(v):
 a=[0]*7
 for i,x in enumerate(v):a[i%7]+=x
 return tuple(a[i]-a[6] for i in range(6))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(a,n):return tuple(x*n for x in a)
def product(a,b):
 v=[0]*11
 for i,x in enumerate(a):
  for j,y in enumerate(b):v[i+j]+=x*y
 return red(v)
def conjugate(a):
 v=[0]*7
 for i,x in enumerate(a):v[(-i)%7]+=x
 return red(v)
def divide(a,b):
 g,s,t=fmpq_poly(list(b)).xgcd(Phi);assert g==1
 v=(fmpq_poly(list(a))*s)%Phi
 assert all(v[i].denominator==1 for i in range(6))
 return tuple(int(v[i]) for i in range(6))
matrices={};fields=[]
def matrix(m):
 if m in matrices:return matrices[m]
 n=3*m;q=1<<n;mod=mods[n];lg=[-1]*q;ex=[];x=1
 for i in range(q-1):
  assert lg[x]<0,('nonprimitive modulus',n,mod,i)
  lg[x]=i;ex.append(x);x<<=1
  if x&q:x^=mod
 assert x==1
 kk=next(j for j in range(1,7) if ex[(3*j*((q-1)//7))%(q-1)]^ex[j*((q-1)//7)]^1==0)
 alpha=ex[kk*((q-1)//7)];alpha2=ex[(2*kk*((q-1)//7))%(q-1)]
 bs=[(j&1)^((alpha if j&2 else 0))^((alpha2 if j&4 else 0)) for j in range(8)]
 xs=np.array([j for j in range(q) if j not in bs],dtype=np.int32);logs=np.array(lg,dtype=np.int32)
 M=np.column_stack([logs[xs^b]*pow(kk,-1,7)%7 for b in bs]).astype(np.int16)
 fields.append({'m':m,'modulus':mod,'alpha':alpha,'embedded_F8':bs})
 matrices[m]=M;print('field ready',m,q,flush=True);return M
spec=json.loads((r/'b5_cyclic7_complete.json').read_text());templates=spec['templates'];records=[];found=[];hist={}
with (r/'b5_all_f8_orbits.csv').open() as f:rows=list(csv.DictReader(f))
for num,row in enumerate(rows):
 es=tuple(int(row['e'+str(j)]) for j in range(9));d=int(row['branches'])-2
 a=[one];sums=[];counts=[];recovery=None
 while len(a)<=d:
  k=len(a);cc=np.bincount(matrix(k)@np.array(es[:8],dtype=np.int16)%7,minlength=7).tolist()
  if es[8]==0:cc[0]+=1
  counts.append(cc);sums.append(red(cc));v=zero
  for j in range(1,k+1):v=add(v,product(sums[j-1],a[k-j]))
  assert all(x%k==0 for x in v);a.append(tuple(x//k for x in v))
  if k==d:break
  j=next((j for j in range(min(k,d//2),0,-1) if d-j<=k and a[j]!=zero),None)
  if j is not None:
   lead=divide(scale(a[d-j],8**j),conjugate(a[j]));recovery={'pair':j,'last_direct_coefficient':k}
   while len(a)<=d:a.append(None)
   a[d]=lead
   for j in range(1,d+1):
    if a[d-j] is not None:
     val=product(lead,conjugate(a[d-j]));den=8**(d-j)
     assert all(v%den==0 for v in val);val=tuple(v//den for v in val)
     if a[j] is None:a[j]=val
     else:assert a[j]==val
   assert all(v is not None for v in a);break
 hist[len(counts)]=hist.get(len(counts),0)+1
 hits=[]
 for tp in templates:
  deg=len(tp)-1
  if deg>d:continue
  for phase in range(7):
   pp=[red([0]*((phase*j)%7)+[c]) for j,c in enumerate(tp)];quo=[]
   for k in range(d+1-deg):
    v=a[k]
    for j in range(1,min(k,deg)+1):v=add(v,scale(product(pp[j],quo[k-j]),-1))
    quo.append(v)
   if all(a[k]==tuple(sum(product(pp[j],quo[k-j])[h] for j in range(max(0,k-len(quo)+1),min(k,deg)+1)) for h in range(6)) for k in range(d+1-deg,d+1)):
    hits.append({'template':tp,'phase':phase,'quotient':quo})
 rec={'branches':d+2,'orbit_size':int(row['orbit_size']),'exponents':es,'character_coefficients':a,'power_sum_residue_counts':counts,'functional_equation_recovery':recovery,'hits':hits};records.append(rec)
 if hits:found.append(rec);print('FOUND',es,hits,flush=True)
 if (num+1)%100==0:print('checked',num+1,'found',len(found),'seconds',time.time()-start,flush=True)
with gzip.open(r/'b5_all_f8_polynomials.json.gz','wt') as f:json.dump(records,f,separators=(',',':'))
out={'checked_orbits':len(rows),'found':found,'direct_sum_degree_histogram':hist,'fields':fields,'seconds':time.time()-start}
(r/'b5_all_f8.json').write_text(json.dumps(out,indent=2)+'\n');print('DONE',len(rows),'found',len(found),'histogram',hist,'seconds',time.time()-start,flush=True)
