"""Finite S3 base of the full pentagon: exact pure braid presentation.
Artin action is Cohen2010 Example1.1. Products act rightmost first.
"""
from itertools import permutations,product
P=list(permutations(range(3)));E=tuple(range(3))
def mul(a,b):return tuple(a[b[i]] for i in range(3))
def inv(a):return tuple(a.index(i) for i in range(3))
def pw(a,n):
 z=E
 for _ in range(n):z=mul(z,a)
 return z
def conj(a,b):return mul(mul(a,b),inv(a))
def comm(a,b):return mul(mul(mul(a,b),inv(a)),inv(b))
def cyc(*c):
 z=list(range(3))
 for a,b in zip(c,c[1:]+c[:1]):z[a]=b
 return tuple(z)
c=cyc(0,1,2);t=cyc(0,1);t2=cyc(1,2)
canonical=[(t,c),(c,t),(t,t2)]
C=[E,c,pw(c,2)]
# A basis for all commutator-word evaluations at epimorphic S3 pairs.
evalvec={}
for a,b in product(P,repeat=2):
 if mul(a,b)==mul(b,a):evalvec[a,b]=(0,0,0);continue
 found=[]
 for i,(aa,bb) in enumerate(canonical):
  for h in P:
   if conj(h,aa)==a and conj(h,bb)==b:
    vec=[0,0,0];vec[i]=C.index(conj(h,c));found.append(tuple(vec))
 assert len(set(found))==1,(a,b,found)
 evalvec[a,b]=found[0]
def add(v,w,s=1):return tuple((v[i]+s*w[i])%3 for i in range(3))
def value(a,b,k):return C[sum(x*y for x,y in zip(evalvec[a,b],k))%3]
keys=[(1,2),(1,3),(2,3),(1,4),(2,4),(3,4)]
def pure_ok(q):
 for j in (3,4):
  for r in range(1,j):
   for s in range(r+1,j):
    g=q[r,s]
    for i in range(1,j):
     v=q[i,j]
     if i<r or s<i: rhs=v
     elif s==i:rhs=conj(q[r,j],v)
     elif r==i:rhs=conj(mul(q[r,j],q[s,j]),v)
     else:rhs=conj(comm(q[r,j],q[s,j]),v)
     if conj(inv(g),v)!=rhs:return False
 return True
relations=set();n=0
for vals in product(P,repeat=6):
 q=dict(zip(keys,vals))
 if not pure_ok(q):continue
 n+=1
 a,b,c3,d,e,f=(q[k] for k in keys)
 # x12=a,x13=b,x23=c3,x24=e,x34=f
 terms=[(a,mul(c3,e),1),(mul(b,c3),f,1),(c3,f,-1),(mul(a,b),mul(e,f),-1),(a,c3,-1)]
 row=(0,0,0)
 for v,w,s in terms:row=add(row,evalvec[v,w],s)
 relations.add(row)
solutions=[k for k in product(range(3),repeat=3) if all(sum(x*y for x,y in zip(r,k))%3==0 for r in relations)]
print('Hom(P4,S3) count:',n)
print('Distinct linear pentagon constraints:',sorted(relations))
print('All solution coordinate triples:',solutions)
for k in solutions:
 allowed=[]
 for mu in (1,5,7,11):
  m=(mu-1)//2;ok=True
  for x,y in product(P,repeat=2):
   z=inv(mul(x,y));f1=value(x,y,k);f2=value(z,x,k);f3=value(y,z,k)
   h=E
   for term in (f1,pw(x,m%6),f2,pw(z,m%6),f3,pw(y,m%6)):h=mul(h,term)
   if h!=E:ok=False;break
  if ok:allowed.append(mu)
 print('coords',k,'full S3 hexagon roots mu mod12:',allowed)
