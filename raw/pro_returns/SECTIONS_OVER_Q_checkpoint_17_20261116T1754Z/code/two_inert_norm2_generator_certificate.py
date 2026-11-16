"""Exact rational-arithmetic certificate extracted from a relation search.

No class-group completeness or analytic estimate is used here.
"""
from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
import json,re
import sympy as sp

base=Path(__file__).resolve().parent
raw=(base/'two_inert_balanced_level2_magma_v3_output.txt').read_text()
raw=re.sub(r'\\\s*\n\s*','',raw)
s=re.search(r'GENERATOR POWER BASIS \[ (.*?) \]\s*GENERATOR NORM',raw,re.S).group(1)
gamma=[F(z.strip()) for z in s.split(',')]
assert len(gamma)==9
d=649;a=3*d**6

def add(x,y):return [u+v for u,v in zip(x,y)]
def scale(x,c):return [c*u for u in x]
def mul(x,y,rad):
    n=len(x);z=[F(0)]*(2*n-1)
    for i,u in enumerate(x):
        for j,v in enumerate(y):z[i+j]+=u*v
    for k in range(2*n-2,n-1,-1):z[k-n]+=rad*z[k]
    return z[:n]
def pw(x,k,rad):
    assert k>=0
    z=[F(1)]+[F(0)]*(len(x)-1)
    while k:
        if k&1:z=mul(z,x,rad)
        x=mul(x,x,rad);k//=2
    return z
def relative_norm(g):
    # t^3=d^2*alpha, alpha^3=3.
    parts=[[g[j+3*k]*d**(2*k) for k in range(3)] for j in range(3)]
    A,B,C=parts;w=[F(0),F(d*d),F(0)]
    return add(add(pw(A,3,3),mul(w,pw(B,3,3),3)),
               add(mul(pw(w,2,3),pw(C,3,3),3),
                   scale(mul(w,mul(mul(A,B,3),C,3),3),-3)))
def multiplication_matrix(g,rad):
    n=len(g);cols=[]
    for j in range(n):
        e=[F(0)]*n;e[j]=F(1)
        cols.append(mul(g,e,rad))
    return sp.Matrix([[sp.Rational(cols[j][i].numerator,cols[j][i].denominator)
                       for j in range(n)] for i in range(n)])

rel=relative_norm(gamma)
# Norm(alpha-1)=2; its inverse is (alpha^2+alpha+1)/2.
ratio=mul(rel,[F(1,2)]*3,3)
U=[F(-2),F(0),F(1)]
Uinv=[F(4),F(3),F(2)]
assert mul(U,Uinv,3)==[1,0,0]
exponent=None
for k in range(1001):
    if pw(U,k,3)==ratio:exponent=k;break
    if pw(Uinv,k,3)==ratio:exponent=-k;break
assert exponent is not None
q,rem=divmod(exponent,3)
correction=pw(Uinv,q,3) if q>=0 else pw(U,-q,3)
embedded=[F(0)]*9
for k,c in enumerate(correction):embedded[3*k]=c/F(d**(2*k))
reduced=mul(gamma,embedded,a)
rel_reduced=relative_norm(reduced)
assert rel_reduced==mul([F(-1),F(1),F(0)],pw(U,rem,3),3)

matrix=multiplication_matrix(reduced,a)
char=matrix.charpoly().all_coeffs()
assert all(x.q==1 for x in char)
det=matrix.det(method='domain-ge')
assert det==2 and char[-1]==-2
relmatrix=multiplication_matrix(rel_reduced,3)
assert relmatrix.det(method='domain-ge')==2
common=lcm(*(x.denominator for x in reduced))
numerators=[int(x*common) for x in reduced]
assert gcd(common,gcd(*numerators))==1
integer_matrix=matrix*common
assert all(x.q==1 for x in integer_matrix)
integer_char=integer_matrix.charpoly().all_coeffs()
for j,c in enumerate(integer_char):
    assert int(c)%(common**j)==0
    assert int(c)//(common**j)==int(char[j])
assert integer_matrix.det(method='domain-ge')==2*common**9
# A monic Z-polynomial annihilating gamma proves integrality directly.
value=[F(0)]*9
for c in char:value=add(mul(value,reduced,a),[F(int(c))]+[F(0)]*8)
assert value==[0]*9
assert a==224176165072750803
assert (d*d)**9*a==3*d**24
assert (d*d)**3*3==3*d**6

data={
 'field_polynomial':'T^9 - 224176165072750803',
 'd':d,'radicand':a,
 'original_coefficients':[str(x) for x in gamma],
 'original_relative_norm':[str(x) for x in rel],
 'original_unit_exponent':exponent,
 'scalar_unit_correction_exponent':-q,
 'reduced_unit_exponent':rem,
 'generator_common_denominator':common,
 'generator_numerators':numerators,
 'characteristic_polynomial_coefficients':[int(x) for x in char],
 'integer_characteristic_polynomial_coefficients':[int(x) for x in integer_char],
 'absolute_norm':int(det),
 'relative_norm_coefficients':[str(x) for x in rel_reduced],
 'root_field_map':'rho_2=649^2*T; alpha=T^3/649^2',
 'integrality_proof':'The displayed monic integral characteristic polynomial annihilates the displayed element exactly.'
}
(base/'two_inert_norm2_generator_certificate_data.json').write_text(json.dumps(data,indent=2)+'\n')
print('Original relative norm = (alpha-1)*(alpha^2-2)^k, k=',exponent)
print('Scalar unit correction exponent:',-q,'; retained exponent:',rem)
print('COMMON DENOMINATOR',common)
print('NUMERATORS',numerators)
print('CHARACTERISTIC POLYNOMIAL COEFFICIENTS',[int(x) for x in char])
print('RELATIVE NORM',rel_reduced)
print('PASS: exact monic integral characteristic polynomial and zero remainder')
print('PASS: all ten integer characteristic-coefficient divisibilities by D^j')
print('PASS: exact multiplication determinant = 2; relative norm determinant = 2')
print('PASS: literal old and new radicand embeddings')
