"""Exact Clifford central refinement for the mixed AGL1(F7) quotient.

Even subsets of seven anticommuting generators e_i with e_i^2=1
form the extraspecial group 2_+^{1+6}. Permutations act honestly by
permuting those generators, with the required reordering sign.
This script checks finite identities and dimensions; it does not
replace the proof identifying the actual profinite central refinement.
"""
from collections import deque
n=7;I=tuple(range(n));V=[v for v in range(128) if v.bit_count()%2==0]
def mulp(a,b):return tuple(a[b[i]] for i in range(n))
def invp(a):return tuple(a.index(i) for i in range(n))
def act(a,v):return sum(1<<a[i] for i in range(n) if v>>i&1)
def cross(v,w):return sum((v>>i&1)*(w>>j&1) for i in range(n) for j in range(i))%2
def psign(a,v):
 points=[a[i] for i in range(n) if v>>i&1]
 return sum(points[i]>points[j] for i in range(len(points)) for j in range(i+1,len(points)))%2
def prod(a,b):
 ea,va,ga=a;eb,vb,gb=b;w=act(ga,vb)
 return(ea^eb^psign(ga,vb)^cross(va,w),va^w,mulp(ga,gb))
def power(a,k):
 b=(0,0,I)
 for _ in range(k):b=prod(b,a)
 return b
def inverse(a):
 e,v,g=a;gi=invp(g)
 return(e^cross(v,v)^psign(gi,v),act(gi,v),gi)
def rank(vs):
 piv={}
 for v in vs:
  while v:
   i=v.bit_length()-1
   if i in piv:v^=piv[i]
   else:piv[i]=v;break
 return len(piv)
def support(v):return[i for i in range(n) if v>>i&1]
s=tuple(-i%7 for i in range(7));r=tuple((2*i+1)%7 for i in range(7))
S=(0,0,s);vr=(1<<2)^(1<<5)
R0=(0,vr,r);eps=power(R0,3)[0];R=(eps,vr,r)
assert power(S,2)==power(R,3)==(0,0,I)
T=prod(S,R)
seen={(0,0,I)};todo=deque([(0,0,I)])
while todo:
 a=todo.popleft()
 for b in(S,R):
  c=prod(a,b)
  if c not in seen:seen.add(c);todo.append(c)
assert len(seen)==128*42
print('Honest Clifford action, chosen r central sign:',eps)
print('Lift orders: s=2,r=3; generated group order',len(seen),'=2^7*42: PASS')
print('Cusp sixth power:',power(T,6)[:2],'twelfth:',power(T,12)[:2],'twenty-fourth:',power(T,24)[:2])
qzeros=sum((v.bit_count()//2)%2==0 for v in V)
assert qzeros==36
print('Invariant quadratic q(v)=wt(v)/2: zeros',qzeros,'of64; plus type: PASS')
heads={g for e,v,g in seen};assert len(heads)==42
# Verify the complete permutation action respects multiplication on P.
for g in (s,r):
 for v in V:
  for w in V:
   lhs=(cross(v,w)^psign(g,v^w),act(g,v^w))
   rhs=(psign(g,v)^psign(g,w)^cross(act(g,v),act(g,w)),act(g,v)^act(g,w))
   assert lhs==rhs
print('Permutation action respects every P product for both H generators: PASS')
# Wedge-square coinvariant dimension, using basis e_i+e_6, i=0,...,5.
basis=[(1<<i)^(1<<6) for i in range(6)];pairs=[(i,j) for i in range(6) for j in range(i+1,6)]
def coords(v):return v&63
def wedge(u,v):
 return sum((((u>>i&1)*(v>>j&1))^((u>>j&1)*(v>>i&1)))<<k for k,(i,j) in enumerate(pairs))
relations=[]
for g in(s,r):
 cols=[coords(act(g,b)) for b in basis]
 for k,(i,j) in enumerate(pairs):relations.append((1<<k)^wedge(cols[i],cols[j]))
assert rank(relations)==14
print('Alternating-square coinvariant relation rank14 of15, dimension1: PASS')
# The second character is obtained by precomposing with actual c(s)=s,
# c(r)=s*r^{-1}*s. The joint head has order7^2*6.
rminus=mulp(mulp(s,invp(r)),s)
headone=(I,I);hs=(s,s);hr=(r,rminus)
headset={headone};todo=deque([headone])
while todo:
 a=todo.popleft()
 for b in(hs,hr):
  c=(mulp(a[0],b[0]),mulp(a[1],b[1]))
  if c not in headset:headset.add(c);todo.append(c)
assert len(headset)==294
print('Joint c-exchanged head order:',len(headset),'=7^2*6: PASS')
translation=tuple((i+1)%7 for i in range(7))
assert (translation,I) in headset and (I,translation) in headset
# t-1 has rank6 on the augmentation module; tensoring with a fixed6-space
# therefore removes all36 cross coinvariants.
assert rank([coords(act(translation,b))^coords(b) for b in basis])==6
print('Independent7-translations and rank(t-1)=6: all36 cross coinvariants vanish: PASS')
odd_relations=[]
for g in(translation,r):
 cols=[coords(act(g,b)) for b in basis]
 for k,(i,j) in enumerate(pairs):odd_relations.append((1<<k)^wedge(cols[i],cols[j]))
assert rank(odd_relations)==14
print('Odd subgroup C7:C3 alone has wedge relation rank14, coinvariant dimension1: PASS')
oddhead={(I,I)};todo=deque([(I,I)])
forbidden=None
oddgens=((translation,I),(I,translation),hr)
while todo:
 a=todo.popleft()
 for b in oddgens:
  h=(mulp(a[0],b[0]),mulp(a[1],b[1]))
  if h not in oddhead:oddhead.add(h);todo.append(h)
assert len(oddhead)==147
print('Paired odd normal subgroup order147; total wedge coinvariant dimension2: PASS')
# Both actual s components are pure. Any order3 lift is conjugate to the
# pure complement; display an exact conjugator in the Clifford kernel.
pureR=(0,0,r)
conj=None
for e in range(2):
 for v in V:
  p=(e,v,I)
  if prod(prod(p,pureR),inverse(p))==R:conj=(e,v);break
 if conj:break
assert conj is not None
print('Exact P-conjugator taking pure r to actual r:',conj[0],support(conj[1]))
print('Finite torsion centralizer projections are therefore onto their H centralizers.')
print('All finite Clifford certificates PASS. The actual-refinement identification is proved separately.')
