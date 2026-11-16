#!/usr/bin/env python3
from itertools import permutations
import json

def mul(p,q):return tuple(p[q[i]] for i in range(len(p)))
def inv(p):return tuple(p.index(i) for i in range(len(p)))
def pw(p,k):
 r=tuple(range(len(p)))
 for _ in range(k):r=mul(r,p)
 return r
def sign(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def normalizer(G,H):
 return [g for g in G if {mul(mul(g,h),inv(g)) for h in H}==set(H)]
S3=list(permutations(range(3)))
A4=[p for p in permutations(range(4)) if sign(p)==1]
C2=[pw((1,0,2),k) for k in range(2)]
C3=[pw((1,2,0,3),k) for k in range(3)]
N2=normalizer(S3,C2);N3=normalizer(A4,C3)
assert set(N2)==set(C2) and set(N3)==set(C3)
print(json.dumps({'S3_order':len(S3),'A4_order':len(A4),'normalizer_C2_in_S3':N2,'normalizer_C3_in_A4':N3,'product_group_order':72,'product_subgroup_order':6,'product_normalizer_order':len(N2)*len(N3)},indent=2))
# A crossed map need not be a homomorphism.
c={0:0,1:1}
for x in (0,1):
 for y in (0,1):assert c[(x+y)%2]==(((-1)**x)*c[y]+c[x])%3
assert (c[1]+c[1])%3!=c[0]
print('C2 inversion cocycle into C3 verified; it is not an ordinary homomorphism.')
