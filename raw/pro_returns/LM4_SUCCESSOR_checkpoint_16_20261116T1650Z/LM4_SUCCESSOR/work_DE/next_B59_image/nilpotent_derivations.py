"""Exact integral Magnus expansions and graded Artin derivations.

For a pure braid, D1 and twiceD2 are the first two homogeneous parts
of the logarithm of its action on the completed free Lie algebra.
Integer Magnus coefficients through degree3 suffice for these data.
No faithful finite representation is assumed: all polynomial identities
are exact truncated identities of the Artin action.
"""
from collections import defaultdict
from fractions import Fraction
import itertools

def clean(p):return {w:c for w,c in p.items() if c}
def add(*ps):
 out=defaultdict(int)
 for p in ps:
  for w,c in p.items():out[w]+=c
 return clean(out)
def scale(p,c):return {w:c*x for w,x in p.items() if c*x}
def prefix(i,p):return {(i,)+w:c for w,c in p.items()}
def suffix(p,i):return {w+(i,):c for w,c in p.items()}
def deriv_add(*ds):return [add(*(d[i] for d in ds)) for i in range(len(ds[0]))]
def deriv_scale(d,c):return [scale(p,c) for p in d]
def deriv_zero(n):return [{} for _ in range(n)]
def apply(d,p):
 out=defaultdict(int)
 for w,c in p.items():
  for j,i in enumerate(w):
   for v,a in d[i].items():out[w[:j]+v+w[j+1:]]+=c*a
 return clean(out)
def bracket(d,e):return [add(apply(d,p),scale(apply(e,q),-1)) for p,q in zip(e,d)]

def magnus_artin(word,n):
 # Each image is represented by (its linear variable,M2,M3).
 images=[(i,{}, {}) for i in range(n)]
 def conjugate(a,b,negative=False):
  i,A2,A3=a;j,B2,B3=b
  comm={(i,j):1,(j,i):-1}
  if negative:
   two=add(B2,scale(comm,-1))
   three=add(B3,scale(prefix(i,B2),-1),scale(suffix(A2,j),-1),
             prefix(j,A2),suffix(B2,i),{(i,i,j):1,(i,j,i):-1})
  else:
   two=add(B2,comm)
   three=add(B3,prefix(i,B2),suffix(A2,j),scale(prefix(j,A2),-1),
             scale(suffix(B2,i),-1),{(j,i,i):1,(i,j,i):-1})
  return j,two,three
 for a in word:
  k=abs(a)-1;u,v=images[k:k+2]
  images[k:k+2]=[conjugate(u,v),u] if a>0 else [v,conjugate(v,u,True)]
 return images

def log_parts(word,n):
 im=magnus_artin(word,n)
 assert [a[0] for a in im]==list(range(n)),'braid must be pure'
 D1=[a[1] for a in im];twice=[]
 for i,(_,M2,M3) in enumerate(im):
  expansion=defaultdict(int)
  for (a,b),c in M2.items():
   expansion[(a,a,b)]+=c;expansion[(a,b,b)]+=c
  v=add(scale(M3,2),clean(expansion),scale(prefix(i,M2),-1),
        scale(suffix(M2,i),-1),scale(apply(D1,M2),-1))
  twice.append(v)
 return D1,twice

def pair_derivation(i,j,n):
 assert i!=j
 out=deriv_zero(n)
 c={(i,j):1,(j,i):-1}
 out[i]=scale(c,-1);out[j]=c
 return out

def product_log_parts(parts):
 n=len(parts[0][0]);one=deriv_zero(n);two=deriv_zero(n)
 for d,e in parts:
  two=deriv_add(two,e,bracket(one,d));one=deriv_add(one,d)
 return one,two

def commutator_parts(X,Y):
 x,x2=X;y,y2=Y
 c2=bracket(x,y)
 c3=deriv_add(bracket(x,y2),bracket(x2,y),bracket(deriv_add(x,y),c2))
 return c2,c3 # degree2, twice degree3

def poly_bracket(p,q):
 out=defaultdict(int)
 for a,x in p.items():
  for b,y in q.items():out[a+b]+=x*y;out[b+a]-=x*y
 return clean(out)

def lyndon_words(r,length):
 return [w for w in itertools.product(range(r),repeat=length)
         if all(w<w[i:]+w[:i] for i in range(1,length))]
def lyndon_bracket(w,gens,comm):
 if len(w)==1:return gens[w[0]]
 # Longest proper Lyndon suffix gives the standard bracketing.
 for i in range(1,len(w)):
  v=w[i:]
  if all(v<v[j:]+v[:j] for j in range(1,len(v))):
   return comm(lyndon_bracket(w[:i],gens,comm),lyndon_bracket(v,gens,comm))
 raise AssertionError(w)

def grade3_basis(n):
 data=[]
 for k in range(1,n):
  for w in lyndon_words(k,3):data.append((k,w))
 assert len(data)==sum((r**3-r)//3 for r in range(1,n))
 return data

def extract_grade3(d,n,basis=None,reconstruct=False):
 basis=grade3_basis(n) if basis is None else basis
 coefficients=[];blocks={}
 for k in range(1,n):
  blocks[k]={w[:3]:c for w,c in d[k].items() if len(w)==4 and w[-1]==k and all(a<k for a in w[:3])}
 polys={}
 for k,w in basis:
  p=blocks[k];c=p.get(w,0);coefficients.append(c)
  if c:
   pol=lyndon_bracket(w,[{(i,):1} for i in range(k)],poly_bracket)
   assert pol[w]==1 and min(pol)==w
   blocks[k]=add(p,scale(pol,-c))
 assert all(not p for p in blocks.values()),'degree3 vector not in the expected free Lie blocks'
 if reconstruct:
  out=deriv_zero(n)
  for (k,w),c in zip(basis,coefficients):
   if c:
    b=lyndon_bracket(w,[pair_derivation(i,k,n) for i in range(k)],bracket)
    out=deriv_add(out,deriv_scale(b,c))
  assert out==d,'full graded Artin derivation reconstruction failed'
 return coefficients

def encode_derivation(d):return [[[list(w),int(c)] for w,c in sorted(p.items())] for p in d]
def decode_derivation(d):return [{tuple(w):c for w,c in p} for p in d]

def self_test():
 for n in [3,4]:
  identity=magnus_artin([],n)
  for i in range(1,n):
   assert magnus_artin([i,-i],n)==identity
   assert magnus_artin([-i,i],n)==identity
  for i in range(1,n-1):assert magnus_artin([i,i+1,i],n)==magnus_artin([i+1,i,i+1],n)
  for i in range(1,n):
   for j in range(1,n):
    if abs(i-j)>1:assert magnus_artin([i,j],n)==magnus_artin([j,i],n)
 d,t=log_parts([1,1],3);assert d==pair_derivation(0,1,3)
 p=log_parts([2,2],3)
 both=log_parts([1,1,2,2],3)
 assert both==product_log_parts([(d,t),p])
 for n in range(3,7):
  basis=grade3_basis(n)
  for j,(k,w) in enumerate(basis):
   D=lyndon_bracket(w,[pair_derivation(i,k,n) for i in range(k)],bracket)
   got=extract_grade3(D,n,basis)
   assert got==[int(i==j) for i in range(len(basis))]
 print('PASS Artin braid relations/inverses, pair sign, BCH product, and graded basis extraction')

if __name__=='__main__':self_test()
