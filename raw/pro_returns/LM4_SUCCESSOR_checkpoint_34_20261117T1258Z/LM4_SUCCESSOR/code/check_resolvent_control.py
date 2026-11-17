"""Exact finite control quotient for the two B.53 resolvents.

This computes the induced degree-30 permutation representations of
C2*C3 from the index-five C2*C3*C3 subgroup after killing one C3
factor and then quotienting the surviving C2*C3 by S3. It is a
finite control calculation, not a proof of a profinite lift or P5.
"""
from itertools import permutations
from sympy.combinatorics import Permutation, PermutationGroup
from sympy import factorint
S3=list(permutations(range(3)))
I3=tuple(range(3));I5=tuple(range(5));idx={g:i for i,g in enumerate(S3)}
def mul(a,b):return tuple(a[b[i]] for i in range(len(a)))
qs=(1,0,3,2,4);qr=(2,1,4,3,0)
S=(1,0,2);R=(1,2,0)
def induced(base,local):
 return Permutation([6*base[i]+idx[mul(local.get(i,I3),g)] for i in range(5) for g in S3])
s=induced(qs,{4:S})
rplus=induced(qr,{1:R})
rminus=induced(qr,{3:R})
assert s.order()==2 and rplus.order()==rminus.order()==3
base=PermutationGroup(Permutation(list(qs)),Permutation(list(qr)))
assert base.order()==60
for name,r in [('plus',rplus),('minus',rminus)]:
 G=PermutationGroup(s,r);order=int(G.order())
 tau=s*r
 assert G.is_transitive()
 assert tau.order()==10
 assert order%6==0
 cusps=order//int(tau.order())
 genus=1+order//12-cusps//2
 print(name,'degree',G.degree,'order',order,'factorization',factorint(order))
 print(name,'cusp order',tau.order(),'free rank',1+order//6,'cusps',cusps,'compact genus',genus)
 print(name,'s cycles',s.cyclic_form)
 print(name,'r cycles',r.cyclic_form)
# The simultaneous representation is the diagonal action on two disjoint blocks.
def join(a,b):return Permutation(list(a.array_form)+[30+x for x in b.array_form])
Sboth=join(s,s);Rboth=join(rplus,rminus)
Gboth=PermutationGroup(Sboth,Rboth);order=int(Gboth.order());tau=Sboth*Rboth
print('both','degree',Gboth.degree,'order',order,'factorization',factorint(order))
print('both','cusp order',tau.order(),'free rank',1+order//6,'cusps',order//int(tau.order()),'compact genus',1+order//12-order//(2*int(tau.order())))
assert 7 not in factorint(order)
print('PASS: ell=7 is coprime to both finite resolvent control quotients.')
