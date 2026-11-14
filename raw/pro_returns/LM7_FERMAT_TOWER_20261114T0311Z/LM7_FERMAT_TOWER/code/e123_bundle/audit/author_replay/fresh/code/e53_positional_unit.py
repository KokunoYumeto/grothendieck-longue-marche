#!/usr/bin/env python3
"""Literal horizontal norm of E122 root20 and its positive tame character.

No number-field executable or author code is imported.  Rational arithmetic
uses Q[b,z]/(b^9-53*z^3,z^6+z^3+1).  The output gives an actual polynomial
in the positional generator b, its vertical norm, and exact support bounds.
"""
from pathlib import Path
from fractions import Fraction as Q
from functools import reduce,lru_cache
from math import gcd,lcm
import hashlib,json

R=Path(__file__).resolve().parents[1]
P=R/'inputs/e122_literal_unit_witnesses.json'
D=json.loads(P.read_text())
@lru_cache(None)
def reduce_z(k):
    k%=9
    return ((k,1),) if k<6 else ((k-3,-1),(k-6,-1))
products={}
for a in range(54):
    i,j=divmod(a,6)
    for c in range(54):
        k,l=divmod(c,6); q,r=divmod(i+k,9)
        products[a,c]=tuple((6*r+t,53**q*v) for t,v in reduce_z(j+l+3*q))

class Ring:
    def __init__(self,a,den=1):
        a=tuple(map(int,a));den=int(den)
        if den<0:a=tuple(-v for v in a);den=-den
        g=reduce(gcd,a,den)
        self.a=tuple(v//g for v in a);self.den=den//g
    @classmethod
    def rational(cls,x):
        x=Q(x);return cls([x.numerator]+[0]*53,x.denominator)
    @classmethod
    def coeff(cls,a):
        a=list(map(Q,a));den=lcm(*(v.denominator for v in a))
        return cls([v.numerator*(den//v.denominator) for v in a],den)
    def __add__(self,o):return Ring([x*o.den+y*self.den for x,y in zip(self.a,o.a)],self.den*o.den)
    def __neg__(self):return Ring([-x for x in self.a],self.den)
    def __sub__(self,o):return self+-o
    def __mul__(self,o):
        out=[0]*54
        for i,x in enumerate(self.a):
            if x:
                for j,y in enumerate(o.a):
                    if y:
                        for k,c in products[i,j]:out[k]+=x*y*c
        return Ring(out,self.den*o.den)
    def __pow__(self,n):
        assert n>=0;out=ONE;base=self
        while n:
            if n&1:out=out*base
            n//=2
            if n:base=base*base
        return out
    def __eq__(self,o):return self.a==o.a and self.den==o.den
    def automorphism(self,bshift=0,zpower=1):
        out=[0]*54
        for a,v in enumerate(self.a):
            i,j=divmod(a,6)
            for k,c in reduce_z(zpower*j+bshift*i):out[6*i+k]+=v*c
        return Ring(out,self.den)
    def positional(self):
        assert self.automorphism(zpower=4)==self
        out=[Q(0)]*18
        for i in range(9):
            assert all(self.a[6*i+j]==0 for j in (1,2,4,5))
            out[i]=Q(self.a[6*i],self.den)
            out[i+9]=Q(self.a[6*i+3],53*self.den)
        assert polynomial(out,b)==self
        return out

def mono(i,j):
    a=[0]*54;a[6*i+j]=1;return Ring(a)
ONE=Ring.rational(1);ZERO=Ring.rational(0);b=mono(1,0);z=mono(0,1)
def polynomial(co,x):
    y=ZERO
    for a in reversed(co):y=y*x+Ring.rational(a)
    return y
assert z**6+z**3+ONE==ZERO and b**9==Ring.rational(53)*z**3
ell=z-b**3*z**8
lower=[polynomial(v,ell) for v in D['lower_units']]
candidates=[polynomial(v,b*z**j) for v in D['upper_candidates'] for j in range(3)]
v=Ring.coeff(D['roots'][19]);ex=D['root_exponents'][19]
left=v**3;right=ONE
for a,e in zip(lower+candidates,ex):
    if e<0:left=left*a**(-e)
    if e>0:right=right*a**e
assert left==right
h1=v.automorphism(zpower=4);h2=v.automorphism(zpower=7)
assert h1.automorphism(zpower=4)==h2 and h2.automorphism(zpower=4)==v
w=v*h1*h2
assert w.automorphism(zpower=4)==w
wc=w.positional()
vertical=w*w.automorphism(bshift=3)*w.automorphism(bshift=6)
vc=vertical.positional()
assert all(vc[i]==0 for i in range(18) if i%3)
vc=[vc[3*i] for i in range(6)]
assert polynomial(vc,b**3)==vertical
relative=ONE
for k in range(9):relative=relative*w.automorphism(bshift=k)
assert all(relative.a[i]==0 for i in range(54) if i not in (0,3))
aa,bb=Q(relative.a[0],relative.den),Q(relative.a[3],relative.den)
absolute=aa*aa-aa*bb+bb*bb

def valuation(n,p):
    n=Q(n)
    if not n:return 10**9
    a,c=abs(n.numerator),n.denominator;e=0
    while a%p==0:a//=p;e+=1
    while c%p==0:c//=p;e-=1
    return e
def support(q):
    q=Q(q);e3,e53=valuation(q,3),valuation(q,53)
    rest=q/(Q(3)**e3*Q(53)**e53)
    return e3,e53,rest
den=lcm(*(x.denominator for x in wc))
ds=support(den);ns=support(absolute)
assert ds[2]==1 and ns[2]==1

# The unique prime over53 has residue F_53[zeta], zeta^2+zeta+1=0.
def fm(x,y):
    a,c=x;d,e=y
    return ((a*d-c*e)%53,(a*e+c*d-c*e)%53)
def fp(x,n):
    y=(1,0)
    while n:
        if n&1:y=fm(y,x)
        n//=2
        if n:x=fm(x,x)
    return y
def residue(q):
    q=Q(q);assert q.denominator%53
    return q.numerator*pow(q.denominator,-1,53)%53
terms=[]
for i in range(9):
    a,c=wc[i],53*wc[i+9]
    k=min(valuation(a,53),valuation(c,53))
    if k==10**9:continue
    unit=(residue(a/Q(53)**k),residue(c/Q(53)**k))
    unit=fm(unit,fp((0,1),(-k)%3))
    terms.append((i+9*k,unit))
v53=min(a for a,_ in terms)
least=[u for a,u in terms if a==v53];assert len(least)==1
res=least[0];power=fp(res,(53**2-1)//3)
logs={fp((0,1),i):i for i in range(3)}
chi53=(-logs[power])%3
chi3=(-chi53)%3
assert (chi3,chi53)==(2,1)
assert ns[1]==2*v53

result={
 'status':'PASS',
 'field_relations':['b^9=53*z^3','z^6+z^3+1=0'],
 'source_root_index':20,
 'source_cube_identity_rechecked':True,
 'horizontal_norm_definition':'w=v20(b,z)*v20(b,z^4)*v20(b,z^7)',
 'horizontal_norm_coefficients_in_b':[str(x) for x in wc],
 'horizontal_norm_fixed_by_h':True,
 'vertical_norm_coefficients_in_beta1':[str(x) for x in vc],
 'norm_to_K_coefficients':[str(aa),str(bb)],
 'absolute_norm':str(absolute),
 'absolute_norm_exponents_3_53':list(ns[:2]),
 'power_basis_denominator':str(den),
 'denominator_exponents_3_53':list(ds[:2]),
 'independent_S_support_proof':'Power-basis denominators and absolute norm both have support only3,53; b is integral.',
 'valuation_at53':v53,
 'unit_residue_at53':list(res),
 'residue_power936':list(power),
 'positive_characters_3_53':[chi3,chi53],
 'comparison_to_B2_character':[sum([2,2,1])%3,sum([2,1,1])%3],
 'input_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),
 'scope':'Literal positional S-unit and its actual positive cubic character; no new BNF or class-number estimate.'
}
(R/'code/e53_positional_unit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
