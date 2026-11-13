#!/usr/bin/env python3
"""Exact checks for the prime-to-three genus-two separation in B14.

The checks enumerate finite fields directly.  The geometric argument,
Jacobian norm identity, and degree-(2,3) genus contradiction are proved
in sections/F7_test.tex; finite enumeration does not replace them.
"""
from pathlib import Path
import json
import sympy as sp

BASE = Path(__file__).resolve().parents[1]
checks = []

def check(name, actual, expected=True):
    ok = actual == expected
    checks.append({"name": name, "actual": actual, "expected": expected, "passed": ok})
    assert ok, (name, actual, expected)

u,t,Z = sp.symbols('u t Z')
poly = lambda f, var: sp.Poly(f,var,modulus=3)
F6 = poly(u*(u-1)*(u+1)*(u**3-u-1),u)
G4 = poly((u+1)*(u**3-u-1),u)
H8 = poly(1-t**2-t**4-t**8,t)
check('translation identity', poly((u**3-u+1)**2-1-F6.as_expr(),u).is_zero)
check('sextic square-free', sp.gcd(F6,F6.diff()).degree(), 0)
check('quartic square-free', sp.gcd(G4,G4.diff()).degree(), 0)
check('quadratic and quartic coprime', sp.gcd(poly(u*(u-1),u),G4).degree(), 0)
check('octic square-free', sp.gcd(H8,H8.diff()).degree(), 0)
b=1-t*t
transformed=poly(1+b+2*b*b+b**3+2*b**4,t)
check('conic parametrization gives octic', transformed==H8)
check('F27 defining cubic has no F3 root', [(a**3-a-1)%3 for a in range(3)], [2,2,2])
check('genus2 from sextic', (F6.degree()-2)//2, 2)
check('genus3 from octic', (H8.degree()-2)//2, 3)
check('unramified double-cover genus', 2*3-2, 2*(2*2-2))

e_affine=[]
for x in range(3):
    for y in range(3):
        if (y*y-int(G4.eval(x)))%3==0:
            e_affine.append([x,y])
check('elliptic affine points',e_affine,[[1,1],[1,2],[2,0]])
check('elliptic group order with two infinities',len(e_affine)+2,5)
labels=[('Pprime',1,2,2,2),('Qplus',1,1,1,1),('Qminus',2,2,1,2)]
for name,tt,WW,z_ratio,e_sign in labels:
    check(name+' lies on octic',(WW*WW-int(H8.eval(tt)))%3,0)
    check(name+' image signs',[tt*WW%3,WW],[z_ratio,e_sign])
check('only possible remaining divisor order',[d for d in (1,2,3,6) if d%3==0 and d!=3],[6])
check('degree-(2,3) arithmetic genus is below 3',(2-1)*(3-1)<3)

class Field:
    """F3[X]/(monic modulus), coefficients in ascending degree."""
    def __init__(self,modulus):
        self.mod=tuple(modulus)
        self.d=len(modulus)-1
        self.q=3**self.d
    def el(self,n):
        out=[]
        for _ in range(self.d):
            out.append(n%3)
            n//=3
        return tuple(out)
    def add(self,a,b):
        return tuple((x+y)%3 for x,y in zip(a,b))
    def neg(self,a):
        return tuple(-x%3 for x in a)
    def mul(self,a,b):
        c=[0]*(2*self.d-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):
                c[i+j]=(c[i+j]+x*y)%3
        for k in range(len(c)-1,self.d-1,-1):
            z=c[k]
            for j in range(self.d):
                c[k-self.d+j]=(c[k-self.d+j]-z*self.mod[j])%3
        return tuple(c[:self.d])
    def power(self,a,n):
        out=self.el(1)
        while n:
            if n&1:
                out=self.mul(out,a)
            a=self.mul(a,a)
            n//=2
        return out
    def count_octic(self):
        squares={self.mul(self.el(i),self.el(i)) for i in range(self.q)}
        affine=0
        for i in range(self.q):
            a=self.el(i)
            value=self.el(1)
            for exponent in (2,4,8):
                value=self.add(value,self.neg(self.power(a,exponent)))
            affine += 1 if value==self.el(0) else 2 if value in squares else 0
        # The degree is even, with leading coefficient -1=2.
        infinity=2 if self.el(2) in squares else 0
        return affine,infinity

counts=[]
point_counts={}
for modulus,expected in [((0,1),6),((1,0,1),10),((2,2,0,1),36)]:
    F=Field(modulus)
    check(f'F{F.q} nonzero multiplicative orders',
          all(F.power(F.el(a),F.q-1)==F.el(1) for a in range(1,F.q)))
    affine,infinity=F.count_octic()
    count=affine+infinity
    check(f'D(F{F.q}) count',count,expected)
    counts.append(count)
    point_counts[str(F.q)]={"affine":affine,"at_infinity":infinity,"total":count}

s1,s2,s3=[3**(i+1)+1-counts[i] for i in range(3)]
c1=-s1
check('second Newton numerator integral',(s1*s1-s2)%2,0)
check('third Newton numerator integral',(-s1**3+3*s1*s2-2*s3)%6,0)
c2=(s1*s1-s2)//2
c3=(-s1**3+3*s1*s2-2*s3)//6
frobenius=Z**6+c1*Z**5+c2*Z**4+c3*Z**3+3*c2*Z**2+9*c1*Z+27
check('Frobenius polynomial',str(frobenius),str(Z**6+2*Z**5+2*Z**4+4*Z**3+6*Z**2+18*Z+27))
j3=int(frobenius.subs(Z,1))
j27=int(sp.resultant(frobenius,Z**3-1,Z))
check('Jacobian over F3',j3,60)
check('Jacobian over F27',j27,25920)
check('Jacobian F27 factorization',{str(p):int(e) for p,e in sp.factorint(j27).items()}, {'2':6,'3':4,'5':1})
prime_to_three=j27
while prime_to_three%3==0:
    prime_to_three//=3
check('prime-to3 Lang quotient degree',prime_to_three,320)
check('composite finite etale cover degree',2*prime_to_three,640)

output={"result":"B14","all_passed":all(c['passed'] for c in checks),
        "check_count":len(checks),"elliptic_affine_points":e_affine,
        "elliptic_infinities":["e_plus","e_minus"],
        "point_counts":point_counts,"frobenius_polynomial":str(frobenius),
        "jacobian_F27":j27,"prime_to_three_Lang_degree":prime_to_three,
        "composite_cover_degree":2*prime_to_three,"checks":checks}
destination=BASE/'code/F7_test_output.json'
destination.write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({"output":str(destination),"checks":len(checks),
                  "all_passed":output['all_passed'],"cover_degree":640},indent=2))
