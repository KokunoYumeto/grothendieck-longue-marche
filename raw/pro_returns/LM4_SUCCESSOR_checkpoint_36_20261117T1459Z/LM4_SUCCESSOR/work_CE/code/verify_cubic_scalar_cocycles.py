"""Independent exact check of the local cubic scalar cocycles.
No inference to a full peripheral involution is made here.
"""
import numpy as np
def mul(a,b):
 out=0
 while b:
  if b&1:out^=a
  b>>=1;a<<=1
  if a&8:a^=11
 return out
def power(a,n):
 out=1
 for _ in range(n):out=mul(out,a)
 return out
def tr(a):
 out=a^power(a,2)^power(a,4);assert out in(0,1);return out
els=[(a,z)for a in range(8)for z in range(8)]
def product(g,h):
 a,z=g;b,w=h;return(a^b,z^w^mul(mul(a,a),b))
index={g:i for i,g in enumerate(els)}
prod=np.array([[index[product(g,h)]for h in els]for g in els],dtype=np.int16)
def kap(q,g,h):
 a,z=g;b,w=h;d=q^mul(q,q)
 return tr(mul(d,mul(power(a,4),w))^mul(q,mul(power(a,6),b))^mul(mul(q,q),mul(power(a,4),power(b,3))))
for q in range(8):
 k=np.array([[kap(q,g,h)for h in els]for g in els],dtype=np.uint8)
 assert not np.any(k[0])and not np.any(k[:,0])
 for i in range(64):
  # rows j, columns l: k(j,l)+k(ij,l)+k(i,jl)+k(i,j)
  defect=k^k[prod[i],:]^k[i,prod]^k[i,:,None]
  assert not np.any(defect)
 for scalar in range(1,8):
  act=[index[(mul(scalar,a),mul(power(scalar,3),z))]for a,z in els]
  assert np.array_equal(k,k[np.ix_(act,act)])
 if q==1:
  f=np.array([tr(power(a,7))for a,z in els],dtype=np.uint8)
  assert np.array_equal(k,f[:,None]^f[None,:]^f[prod])
print('All eight normalized cubic cocycles: full64^3 cocycle equations PASS.')
print('All seven scalar actions preserve every cocycle: PASS.')
print('q=1 equals the coboundary of Tr(a^7): PASS.')
triples=set()
for a in range(8):
 for b in range(8):
  z=mul(mul(a,a),b)^mul(a,mul(b,b))
  for c in range(8):
   triples.add(tuple(tr(mul(q^mul(q,q),mul(power(c,4),z)))for q in(2,4)))
assert triples=={(0,0),(0,1),(1,0),(1,1)}
print('The two scalar directions q=2,4 are both attained by triple commutators: PASS.')
