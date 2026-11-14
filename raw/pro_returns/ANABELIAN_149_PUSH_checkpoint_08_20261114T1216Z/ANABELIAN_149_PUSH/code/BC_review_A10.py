"""Independent exact checks of the finite certificates in statement A.10.

Uses F4 directly, with a^2+a+1=0; no import from the A-series checks.
This certifies the small finite algebra. The all-geometric-points proof
is reviewed separately in audit/BC_review_A10.md.
"""
from itertools import product
from pathlib import Path
import json

def add(x,y):
    return x ^ y

def mul(x,y):
    ans=0
    while y:
        if y & 1:
            ans ^= x
        y >>= 1
        x <<= 1
        if x & 4:
            x ^= 7
    return ans

def power(x,n):
    ans=1
    while n:
        if n & 1:
            ans=mul(ans,x)
        x=mul(x,x)
        n >>= 1
    return ans

alpha=2
alpha_inv=3
assert mul(alpha,alpha_inv)==1
assert power(alpha,2)==3
assert power(alpha,2)^alpha^1==0

# Equation: w^3+(x^2+alpha)*w=x^2+x.
fibres={x:[w for w in range(4) if power(w,3)^mul(power(x,2)^alpha,w)^power(x,2)^x==0] for x in range(4)}
assert fibres=={0:[0,3],1:[0,2],2:[],3:[1,2,3]}
# At Z=0, W*(W+X)^2=0 gives O=[1:0:0], T=[1:1:0].
infinity_points=[(1,w,0) for w in range(4) if power(w,3)^w==0]
assert infinity_points==[(1,0,0),(1,1,0)]
assert sum(map(len,fibres.values()))+len(infinity_points)==9

# The matrix [[1,1],[alpha,alpha^-1]] has determinant 1.
assert alpha ^ alpha_inv == 1
linear_map=lambda z,v:(z^v,mul(alpha,z)^mul(alpha_inv,v))
assert len({linear_map(z,v) for z,v in product(range(4),repeat=2)})==16

# u=0: three points on each of the two unramified branches.
zero_branch=[linear_map(0,v) for v in (1,2,3)]
unit_branch=[linear_map(z,0) for z in (1,2,3)]
assert len(set(zero_branch+unit_branch))==6

# At infinity z/x=xi and v/x=xi^-1.
infinity_pairs=[]
for xi in (1,alpha,power(alpha,2)):
    xinv=power(xi,2)
    a,b=linear_map(xi,xinv)
    assert a in (0,1) and b in (0,1)
    infinity_pairs.append(['O' if a==0 else 'T','O' if b==0 else 'T'])
assert infinity_pairs==[['O','T'],['T','T'],['T','O']]

out={
    'passed':True,
    'field':'F2[a]/(a^2+a+1), coefficients represented by two-bit integers',
    'affine_fibres':fibres,
    'points_at_infinity':infinity_points,
    'E_F4_count':9,
    'frobenius_polynomial_coefficients_descending':[1,4,4],
    'matrix_determinant':1,
    'linear_map_is_bijective_on_F4_squared':True,
    'u_zero_branch_pairs':zero_branch,
    'u_unit_branch_pairs':unit_branch,
    'six_pairs_are_distinct':True,
    'infinity_image_pairs':infinity_pairs,
    'scope':'Independent finite algebra certificate only; the proof for all geometric points and the section argument are reviewed in audit/BC_review_A10.md.'
}
Path(__file__).with_name('BC_review_A10_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
