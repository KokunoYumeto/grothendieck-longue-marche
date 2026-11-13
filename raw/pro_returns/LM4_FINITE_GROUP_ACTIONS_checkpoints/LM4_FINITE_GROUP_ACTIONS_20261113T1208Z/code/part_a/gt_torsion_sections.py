#!/usr/bin/env python3
"""Finite arithmetic and dihedral certificates for the D.28 section argument."""
from itertools import product
from pathlib import Path
import json


def crt_pair(a, m, b, n):
    assert __import__('math').gcd(m,n) == 1
    return (a + m*((b-a)*pow(m,-1,n) % n)) % (m*n)


def root3(level):
    root, modulus = 2, 7
    for _ in range(1,level):
        root = next(root+modulus*t for t in range(7)
                    if pow(root+modulus*t,3,7*modulus)==1)
        modulus *= 7
    return root, modulus


def norm_checks():
    rows=[]
    for k,j in product((1,2,3),(1,2)):
        root, qmod = root3(j)
        pmod = 2*3**k
        modulus = pmod*qmod
        u=crt_pair(1,pmod,root,qmod)
        assert pow(u,3,modulus)==1
        norm=(1+u+u*u) % modulus
        norm_image={(norm*v) % modulus for v in range(modulus)}
        compatible={m for m in range(modulus)
                    if ((u-1)*m) % modulus==0 and m % 3==0}
        assert compatible == norm_image
        rows.append({'modulus':modulus,'u':u,'norm':norm,
            'fixed_exponents_divisible_by_3':len(compatible),
            'norm_image_size':len(norm_image),'sets_equal':True})
    return rows


def dihedral_certificate():
    n=7
    G=list(product(range(n),range(2)))
    one=(0,0)
    def mul(a,b):return ((a[0]+(-1)**a[1]*b[0]) % n,(a[1]+b[1]) % 2)
    def power(a,k):
        out=one
        for _ in range(k):out=mul(out,a)
        return out
    def inv(a):return next(b for b in G if mul(a,b)==one)
    r,s=(1,0),(0,1)
    x,y=s,mul(s,r)
    u=9
    actual=mul(power(x,u),power(y,u))
    expected=power(mul(x,y),u)
    conjugates=sorted({mul(mul(h,actual),inv(h)) for h in G})
    assert actual==r and expected==(2,0) and expected not in conjugates
    for a,b,c in product(G,repeat=3):
        assert mul(mul(a,b),c)==mul(a,mul(b,c))
    return {'group_order':14,'epsilon_mod_14':u,
        'x':x,'y':y,'x_to_u_y_to_u':actual,'xy_to_u':expected,
        'conjugates_of_actual':conjugates,'nonconjugate':True,
        'associativity_checks':14**3}


out={'norm_checks':norm_checks(),'third_cusp_failure':dihedral_certificate(),
     'scope':'The finite test certifies the failure of the diagonal-power candidate, not existence of GT0 torsion. The section-class and fixed-subgroup assertions are proved by profinite cohomology in D.28.'}
Path(__file__).with_name('gt_torsion_sections_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
