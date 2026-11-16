#!/usr/bin/env python3
"""Exact nonstable C8 quotient, invariant and cusp-divisor certificate.

Independent rational transvectant implementation; normalization references:
Sage invariants.py (normalized transvectants and Clebsch conversion),
Dabrowski--Sadek, equation (3), and Liu 1993, Theorem 1(V*),(V).
This certificate checks finite identities; the all-degree fixed-group
conclusion additionally uses the proved A.41--A.42 geometric criterion.
"""
from pathlib import Path
import json
import sympy as s

x,z,w,v,T,q=s.symbols('x z w v T q')
fc=w**16-6*w**8+1
fb=(T+2)*(T**4-4*T**2-4)
rel=v*v-fc
tb=w*w+w**-2
wb=(w+w**-1)*v/w**4
def reduce_curve(expr):
    return s.rem(s.fraction(s.cancel(expr))[0],rel,v)
assert reduce_curve(wb*wb-fb.subs(T,tb))==0
assert s.discriminant(fb,T)==-1048576
assert s.expand(fc-((w*w)**8-6*(w*w)**4+1))==0
# Pullbacks of the two actual genus-two holomorphic differentials.
d1=s.cancel(s.diff(tb,w)/((w+w**-1)/w**4))
d2=s.expand(tb*d1)
assert d1==2*w**4-2*w**2
assert d2==2*w**6-2*w**4+2*w**2-2
# Seven actual differential pullbacks span H^0(C,Omega).
def col(poly):return s.Matrix([s.expand(poly).coeff(w,j-1) for j in range(1,8)])
old=[col(w**j) for j in (1,3,5)]
bs=[col(d1),col(d2)]
rot=s.diag(*[q**j for j in range(1,8)])
M=s.Matrix.hstack(*(old+bs+[rot*b for b in bs]))
det=s.rem(s.expand(M.det()),q**4+1,q)
assert det!=0

def transvectant(f,g,k):
    if f==0 or g==0:return s.Integer(0)
    m=s.Poly(f,x,z).total_degree(); n=s.Poly(g,x,z).total_degree()
    if k>min(m,n):return s.Integer(0)
    c=s.factorial(m-k)*s.factorial(n-k)/(s.factorial(m)*s.factorial(n))
    return s.expand(c*sum((-1)**j*s.binomial(k,j)
       *s.diff(f,x,k-j,z,j)*s.diff(g,x,j,z,k-j)
       for j in range(k+1)))
def invariants(f):
    f=s.Poly(f,x)
    F=s.expand(sum(co*x**mon[0]*z**(6-mon[0]) for mon,co in f.terms()))
    ii=transvectant(F,F,4); dd=transvectant(ii,ii,2)
    A=transvectant(F,F,6); B=transvectant(ii,ii,4); C=transvectant(ii,dd,4)
    I2=-120*A; I4=-720*A*A+6750*B
    I6=8640*A**3-108000*A*B+202500*C
    I10=s.discriminant(f.as_expr(),x)
    if f.degree()==5:I10*=f.LC()**2
    J2=I2/8; J4=(4*J2**2-I4)/96
    J6=(8*J2**3-160*J2*J4-I6)/576
    J8=(J2*J6-J4**2)/4; J10=I10/s.Integer(4096)
    return [s.factor(a) for a in (I2,I4,I6,I10)], [s.factor(a) for a in (J2,J4,J6,J8,J10)]
IC,J=invariants(fb.subs(T,x))
assert IC==[192,4608,-516096,-1048576]
assert J==[24,-24,1248,7344,-256]
# Official PARI example computes invariants of 4P rather than P.
_,test=invariants(x**5+3*x**2-4)
pari=[a*4**d for a,d in zip(test,(2,4,6,8,10))]
assert pari==[0,9600,20736,-23040000,177926144]
J2,J4,J6,J8,J10=J
L4=J2**2-24*J4
L12=-8*J4**3+9*J2*J4*J6-27*J6**2-J2**2*J8
assert L4==1152 and L12==-52641792
def val2(a):
    a=s.Rational(a); n,d=map(abs,(int(a.p),int(a.q)))
    def v(n):
        r=0
        while n and n%2==0:r+=1;n//=2
        return r
    return v(n)-v(d)
ratios=[L4**4/J8**2,J10**4/J8**5,L12**4/J8**6,
        L4**12/(J10**4*J8),L12**4/(J10**4*J8)]
vals=[val2(r) for r in ratios]
assert vals==[20,12,32,48,20]
# Exact products prove no additional zeros or poles; local leading terms
# determine the four divisors, each supported at the two stated cusps.
F1=v-w**8+1; F2=v+w**8-1
F3=v-w**8-1; F4=v+w**8+1
assert reduce_curve(F1*F2+4*w**8)==0
assert reduce_curve(F3*F4+8*w**8)==0
u=s.symbols('u')
root=s.series(s.sqrt(1-6*u**8+u**16),u,0,17).removeO()
assert root==1-3*u**8-4*u**16
def order_at(poly,sign,infinity=False):
    ev=poly.subs({w:1/u if infinity else u,
                 v:sign*root/u**8 if infinity else sign*root},simultaneous=True)
    ev=s.expand(ev)
    return min(int(term.as_powers_dict().get(u,0)) for term in s.Add.make_args(ev) if term!=0)
orders=[[order_at(f,sg,inf) for inf,sg in ((False,1),(False,-1),(True,1),(True,-1))]
        for f in (F1,F2,F3,F4)]
assert orders==[[0,8,0,-8],[8,0,-8,0],[8,0,0,-8],[0,8,-8,0]]
out={'status':'PASS','curve':'v^2=w^16-6w^8+1','genus':7,
 'actual_genus_two_map':[str(tb),str(wb)],'genus_two_equation':str(s.expand(fb)),
 'differential_pullbacks':[str(d1),str(d2)],'seven_differential_determinant_mod_Phi8':str(det),
 'jacobian_isogeny':'J_C ~ J_C4 x J_B^2, from three actual maps',
 'igusa_clebsch':[str(a) for a in IC],'igusa_J':[str(a) for a in J],
 'pari_official_normalization_example':[str(a) for a in pari],
 'liu_auxiliary_I4':str(L4),'liu_auxiliary_I12':str(L12),
 'liu_theorem1_Vstar_V_valuations':vals,
 'liu_consequence':'two smooth elliptic components, both j=0 in characteristic2',
 'cusp_order_columns':['P0+','P0-','Pinf+','Pinf-'],'cusp_divisor_orders':orders,
 'cusp_differences_annihilated_by':8,
 'scope':'Exact finite algebra and primary-criterion inputs; full proof uses A37 and A41--42.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: actual quotient identities; seven independent holomorphic pullbacks; exact Igusa normalization cross-check; all five Liu valuations; four cusp divisors.')
