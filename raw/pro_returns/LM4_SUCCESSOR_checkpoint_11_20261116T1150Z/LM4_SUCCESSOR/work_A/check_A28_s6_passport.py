#!/usr/bin/env python3
"""A finite negative peripheral action with no reflection triangle of its passport.
All arithmetic is exact permutation arithmetic.  This does not assert a full
profinite order-two lift of the finite automorphism.
"""
from itertools import permutations, product
from collections import Counter

n=6
one=tuple(range(n))
def mul(a,b): return tuple(a[b[i]] for i in range(n))
def inv(a): return tuple(a.index(i) for i in range(n))
def parity(a): return sum(a[i]>a[j] for i in range(n) for j in range(i+1,n))%2
def ctype(a):
    seen=set();ans=[]
    for i in range(n):
        if i not in seen:
            j=i;k=0
            while j not in seen:
                seen.add(j);k+=1;j=a[j]
            ans.append(k)
    return tuple(sorted(ans))
def generated(gens):
    gens=tuple(gens)+tuple(map(inv,gens));seen={one};queue=[one]
    for a in queue:
        for g in gens:
            b=mul(a,g)
            if b not in seen:seen.add(b);queue.append(b)
    return frozenset(seen)
def cyc(*cs):
    a=list(one)
    for c in cs:
        for u,v in zip(c,c[1:]+c[:1]):a[u-1]=v-1
    return tuple(a)
def notation(a):
    seen=set();ans=[]
    for i in range(n):
        if i not in seen:
            j=i;c=[]
            while j not in seen:seen.add(j);c.append(j+1);j=a[j]
            if len(c)>1:ans.append('('+','.join(map(str,c))+')')
    return ''.join(ans) or '()'

S=tuple(permutations(range(n)))
A=tuple(g for g in S if not parity(g))
I=tuple(g for g in S if parity(g) and mul(g,g)==one)
C=tuple(g for g in A if ctype(g)==(2,4))
x=cyc((1,2,3,4),(5,6))
for y in C:
    z=inv(mul(x,y))
    if z in C and len(generated((x,y)))==360:break
else:raise AssertionError('No generating (4,4,4) passport')
t=cyc((2,4))
assert mul(mul(t,x),t)==inv(x)
assert len(generated((x,y,t)))==720
# Actual involutory automorphism alpha = Ad(t) preserves each inverse A6 class.
frames=[]
for a in (x,y,z):
    aa=mul(mul(t,a),t)
    frame=next(g for g in A if mul(mul(g,inv(a)),inv(g))==aa)
    frames.append(frame)
# Every cusp is separately inverted by an odd involution.
reversers=[next(u for u in I if mul(mul(u,a),u)==inv(a)) for a in (x,y,z)]
assert all(mul(u,u)==one for u in reversers)
# A6's perfectness, and uniqueness of the nonsplit (4,2) class.
conj={mul(mul(g,x),inv(g)) for g in A}
assert conj==set(C)
comms=[mul(mul(mul(a,b),inv(a)),inv(b)) for a in (x,y) for b in A]
assert len(generated(comms))==360
hist=Counter(ctype(u) for u in I)
# A product of two odd involutions lies in C iff their involution types differ.
# The converse is not claimed; only necessity is used in the two-colour proof.
assert all(ctype(u)!=ctype(v) for u,v in product(I,repeat=2) if mul(u,v) in C)
triangles=[(u,v,w) for u,v,w in product(I,repeat=3)
           if mul(u,v) in C and mul(v,w) in C and mul(w,u) in C]
assert not triangles
rot=cyc((3,4,6))
assert all(mul(mul(rot,u),inv(rot))==v for u,v in ((x,y),(y,z),(z,x)))
print('cyclic conjugator (3,4,6) verified')
print('|S6|=',len(S),'|A6|=',len(A),'|C_(4,2)|=',len(C))
print('x=',notation(x),'y=',notation(y),'z=',notation(z))
print('xyz=1:',mul(mul(x,y),z)==one,'generated orientation subgroup=',len(generated((x,y))))
print('t=',notation(t),'alpha=Ad(t), alpha^2=1')
print('pure inverse-class conjugators=',[notation(g) for g in frames])
print('separate odd involution reversers=',[notation(g) for g in reversers])
print('odd involution types=',dict(sorted(hist.items())))
print('reflection triangles with all products in C_(4,2)=',len(triangles))
print('|[A6,A6]|=',len(generated(comms)))
print('This is a finite-level obstruction only; no full profinite lift is asserted.')
