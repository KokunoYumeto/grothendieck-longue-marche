"""Exact finite algebra for the two Jarden--Ritter local-field examples.
The p-adic field and conductor-discriminant theorems are used in A.tex;
this certificate checks their polynomial and S3 character inputs only.
"""
from itertools import permutations
import json

def val(n,p):
    r=0
    while n and n%p==0:n//=p;r+=1
    return r

def disc_cubic(a,b,c,d):
    return b*b*c*c-4*a*c*c*c-4*b*b*b*d-27*a*a*d*d+18*a*b*c*d

polys=[(1,0,0,-3),(1,3,3,-3)]
for a,b,c,d in polys:
    assert a%3 and all(z%3==0 for z in (b,c,d)) and d%9
D=[disc_cubic(*x) for x in polys]
assert D==[-243,-432]
assert [val(x,3) for x in D]==[5,3]
# disc / (-3) is a rational square, and -3 is nonsquare in Q_3.
assert D[0]//(-3)==9**2 and D[1]//(-3)==12**2
G=list(permutations(range(3)))
def sign(g):return (-1)**sum(g[i]>g[j] for i in range(3) for j in range(i+1,3))
chars=[[1 for g in G],[sign(g) for g in G],[sum(g[i]==i for i in range(3))-1 for g in G]]
for i in range(3):
    for j in range(3):assert sum(x*y for x,y in zip(chars[i],chars[j]))==6*(i==j)
reg=[6 if g==(0,1,2) else 0 for g in G]
assert reg==[chars[0][i]+chars[1][i]+2*chars[2][i] for i in range(6)]
output={'eisenstein_at_3':[True,True], 'polynomials':polys,
        'cubic_discriminants':D,'cubic_discriminant_exponents':[5,3],
        'discriminant_square_class':'-3','s3_character_orthogonality':True,
        'regular_character_decomposition':[1,1,2],
        'quadratic_conductor':1,'splitting_field_discriminant_exponents':[11,7],
        'certificate_scope':'polynomial identities and finite S3 character calculation; not an independent computation of infinite Galois groups'}
print(json.dumps(output,indent=2))
