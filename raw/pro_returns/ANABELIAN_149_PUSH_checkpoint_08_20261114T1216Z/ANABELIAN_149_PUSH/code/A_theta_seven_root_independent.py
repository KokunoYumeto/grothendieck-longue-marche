#!/usr/bin/env python3
"""Root's independent symbolic and brute-force checks of A.C2.13.

Uses SymPy quotient-polynomial arithmetic rather than the candidate's bit
multiplication and Artin-Schreier trace count. Does not assert geometric proofs.
"""
from pathlib import Path
import json
import sympy as s
x, alpha, z = s.symbols('x alpha z')
u=x*(x+1)
a=x+alpha**2
b=x**2+alpha**2
F=x**3+x**2+x+alpha
G=s.groebner([alpha**2+alpha+1],alpha,x,modulus=2)
assert G.reduce(s.expand(u*(a*a+a*b)+b*b*(F+alpha*u)-(x+alpha**2)**7))[1]==0

def field_table(degree, modulus):
    q=2**degree
    elements=[s.Poly(sum(((i>>j)&1)*z**j for j in range(degree)),z,modulus=2) for i in range(q)]
    mod=s.Poly(modulus,z,modulus=2)
    product=[]
    for f in elements:
        row=[]
        for g in elements:
            h=(f*g).rem(mod)
            row.append(sum((int(h.nth(j))%2)<<j for j in range(degree)))
        product.append(row)
    return product

counts=[]
for degree, modulus, al in [(2,z*z+z+1,2),(4,z**4+z+1,6)]:
    q=2**degree
    m=field_table(degree,modulus)
    assert m[al][al]^al==1
    inverses={i:next(j for j in range(1,q) if m[i][j]==1) for i in range(1,q)}
    affine=[]
    for xv in range(2,q):
        rhs=xv ^ m[al][inverses[xv]] ^ m[m[al][al]][inverses[xv^1]]
        for yv in range(q):
            if m[yv][yv]^yv==rhs: affine.append([xv,yv])
    counts.append({'field_size':q,'alpha_encoding':al,'affine_points':affine,'total_with_three_branch_points':len(affine)+3})
assert [c['total_with_three_branch_points'] for c in counts]==[3,15]
P=x**4-2*x**3+x*x-8*x+16
A=-207*x**3-57*x*x+248*x+856
B=-207*x**4-471*x**3-487*x*x-1303*x-2575
assert s.expand((x**5-1)*A-40344-P*B)==0
assert s.rem(x**5-1,P,x)==3*x**3+6*x*x-33
assert s.factorint(40344)[3]==1
result={'status':'PASS','norm_remainder':0,'field_counts':counts,
        'frobenius_characteristic_polynomial':str(P),
        'bezout_remainder':0,'annihilator_factorization':{str(k):v for k,v in s.factorint(40344).items()},
        'method':'Independent SymPy quotient polynomials, enumeration of every affine (x,y), exact integer polynomial division.',
        'scope':'Checks the algebra and point counts; root/independent mathematical reviews supply divisor, character, and section arguments.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
