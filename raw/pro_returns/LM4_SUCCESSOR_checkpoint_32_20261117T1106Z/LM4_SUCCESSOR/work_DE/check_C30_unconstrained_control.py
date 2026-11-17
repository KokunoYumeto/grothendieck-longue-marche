"""Independent exact scope control for the C29/C30 invertibility audit.

With lambda=1 and f=[x,y]^-1, the unconstrained substitution can
have proper finite image.  This is not a counterexample to C29 or
C30: it fails the third-cusp condition already in S3.
"""
from itertools import permutations

I=(0,1,2)
def mul(a,b):return tuple(a[b[j]] for j in range(3))
def inv(a):return tuple(a.index(j) for j in range(3))
def comm(a,b):return mul(mul(mul(a,b),inv(a)),inv(b))
def conj(a,b):return mul(mul(a,b),inv(a))
def generated(gens):
    seen={I};todo=[I]
    while todo:
        a=todo.pop()
        for b in gens:
            v=mul(a,b)
            if v not in seen:seen.add(v);todo.append(v)
    return seen

x=(1,0,2);y=(0,2,1)
f=inv(comm(x,y))
image_y=conj(inv(f),y)
assert len(generated([x,y]))==6
assert image_y==x and len(generated([x,image_y]))==2
assert mul(x,image_y)==I and mul(x,y)!=I
print('Finite convention: permutations act right to left on {0,1,2}.')
print('x=(01), y=(12) generate S3: order',len(generated([x,y])))
print('f=[x,y]^-1 has tuple',f)
print('x maps to',x,'; f^-1 y f maps to',image_y)
print('Substitution image has order',len(generated([x,image_y])))
print('Third-cusp product maps to identity whereas xy has order3: PASS')
print('PASS: unconstrained substitution need not be an automorphism; C29/C30 hypotheses are essential.')
