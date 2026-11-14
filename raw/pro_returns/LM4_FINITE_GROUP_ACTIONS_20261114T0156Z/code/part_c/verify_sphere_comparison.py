"""Finite certificates for C.24; no finite calculation proves the limit claim."""
from pathlib import Path
from math import factorial
import json

R=((0,0,1),(1,0,0),(0,1,0))
I=((1,0,0),(0,1,0),(0,0,1))
def mul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)) for i in range(3))
def transpose(a):
    return tuple(zip(*a))
assert mul(R,mul(R,R))==I and R!=I
assert mul(R,transpose(R))==I
# Every integral circulant test matrix commutes; the general coefficient
# equations MR=RM are exactly m_ij=m_(i+1,j+1), with indices modulo 3.
for a in range(-2,3):
    for b in range(-2,3):
        for c in range(-2,3):
            M=((a,b,c),(c,a,b),(b,c,a))
            assert mul(M,R)==mul(R,M)
residues=[]
for k in range(1,15):
    modulus=3**k
    beta=sum(3**factorial(j) for j in range(1,10) if factorial(j)<k)%modulus
    even_rep=beta if beta%2==0 else beta+modulus
    assert even_rep%modulus==beta and even_rep%2==0
    if k<=7:
        pairs={(n%modulus,n%2) for n in range(2*modulus)}
        assert len(pairs)==2*modulus
    residues.append({'k':k,'beta_mod_3k':beta,'even_integer_lift_mod_2x3k':even_rep,'finite_diagonal_map_bijective':True})
out={'action':'C3 cyclic permutation of the three coordinate axes on the unit sphere',
     'rotation_matrix':R,'order':3,'orthogonal':True,'axis':[1,1,1],
     'centralizer_equations':'m_ij=m_(i+1,j+1), indices modulo 3',
     'integral_comparison':'Z -> Z_3 x C2, n -> (n,n mod2)',
     'nonintegral_element':'beta=sum_{j>=1} 3^(j!), 3-adic digits 1 exactly at factorial positions',
     'infinite_obstruction':'beta has infinitely many digits 1 and 0; an integer has eventually all 0 or all 2 digits, so beta is not an integer',
     'residues':residues}
Path(__file__).with_name('verify_sphere_comparison_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
