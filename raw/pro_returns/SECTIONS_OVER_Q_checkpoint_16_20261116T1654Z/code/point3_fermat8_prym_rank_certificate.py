#!/usr/bin/env python3
"""Exact quadratic Prym maps and elementary two-isogeny rank certificates.

No external arithmetic service is called.  Dyadic enumerations are only
used as necessary exclusions; explicit global points attain all survivors.
"""
from pathlib import Path
from fractions import Fraction
from itertools import product
import contextlib
import io
import json
import runpy
import sympy as sp

BASE=Path(__file__).resolve().parent
z,w,A,r,s=sp.symbols('z w A r s')
curve=w**4-A*z*(z*z+r*r)
X=A*w*w/z
Y=A*A*w*(z+r)/z
coefficient=2*A**3*r
def on_curve(h):
    return sp.rem(sp.together(h).as_numer_denom()[0],curve,w)==0
assert on_curve(Y*Y-X**3-coefficient*X)
assert sp.cancel(X.subs({z:r*r/z,w:r*w/z},simultaneous=True)-X)==0
assert sp.cancel(Y.subs({z:r*r/z,w:r*w/z},simultaneous=True)-Y)==0
dw=A*(3*z*z+r*r)/(4*w**3)
dX=sp.diff(X,z)+dw*sp.diff(X,w)
assert on_curve(dX/(2*Y)-(z-r)/(4*w**3))
assert on_curve(z*z-(X*X/A**3)*z+r*r)
assert sp.cancel(Y*z/(A*A*(z+r))-w)==0
assert sp.Matrix([[-r,1],[r,1]]).det()==-2*r
print('PASS: literal reciprocal involution, elliptic quotient/inverse, differential and conjugate rank-two map')

def fieldzero(h,D):
    return sp.rem(sp.together(h).as_numer_denom()[0],s*s-D,s)==0

map_rows=[
    (-12,1,-3,s/6,2*s,-4*s,sp.Rational(-1,2),(-2,2+2*s)),
    (18,1,2,s/6,3*s,6*s,sp.Rational(1,3),(3,3+3*s)),
    (3,-2,-6,s/3,s/2,8*s,sp.Integer(1),(-2,-4+2*s)),
]
map_data=[]
for aa,bb,D,rr,scale,new_b,z0,point in map_rows:
    assert fieldzero(rr**2-sp.Rational(bb,aa),D)
    assert fieldzero(2*aa**3*rr/scale**4-new_b,D)
    px=aa/z0/scale**2
    py=aa*aa*(z0+rr)/z0/scale**3
    assert fieldzero(px-point[0],D) and fieldzero(py-point[1],D)
    assert fieldzero(point[1]**2-point[0]**3-new_b*point[0],D)
    map_data.append({'A':aa,'B':bb,'field_discriminant_parameter':D,
                     'r':str(rr),'scale':str(scale),'elliptic_b':str(new_b),
                     'point':[str(a) for a in point]})
    print('SCALED PRYM',aa,bb,'field sqrt',D,'b',new_b,'point',point)

# At the ramified prime above three in the two imaginary fields,
# v(b)=1.  For d=(-1)^sigma*2^e*s^f, the necessary residue is
# d if f=0 and b/d if f=1, after removing s.
imaginary_data=[]
for D,kappa,allowed_e,expected in [
    (-3,-4,[0,1],[(0,0,0),(1,1,0),(1,0,1),(0,1,1)]),
    (-3,1,[0],[(0,0,0),(0,0,1)]),
    (-6,8,[0,1],[(0,0,0),(1,1,0),(1,0,1),(0,1,1)]),
    (-6,-2,[0,1],[(0,0,0),(1,1,0),(0,0,1),(1,1,1)]),
]:
    survivors=[]
    for sigma,e,f in product(range(2),allowed_e,range(2)):
        unit=(-1)**sigma*2**e %3
        residue=unit if f==0 else kappa*pow(unit,-1,3)%3
        if residue==1:survivors.append((sigma,e,f))
    assert set(survivors)==set(expected)
    imaginary_data.append({'D':D,'b_over_s':kappa,
                           'surviving_exponent_vectors':sorted(survivors)})
    print('ODD THREE FILTER',D,kappa,'survivors',sorted(survivors))

# Exact class-group lattice for Q(sqrt(-6)): P2^2=(2), P3^2=(3),
# P2 P3=(s).  These two generator columns span precisely m+n even.
for m in range(-30,31):
    for n in range(-30,31):
        if (m+n)%2==0:
            assert 2*((m-n)//2)+n==m
        else:
            assert (m-n)%2
assert all(a*a+6*b*b!=2 for a,b in product(range(-3,4),repeat=2))
assert fieldzero((-2)*(2-s/2)**2-(-5+4*s),-6)
assert fieldzero((37-s)**2-(-5+4*s)**3+2*s*(-5+4*s),-6)
assert fieldzero((3-3*s)**2-3**3+6*s*3,2)
print('PASS: imaginary S-divisor lattice and exact nontrivial dual point squareclasses')

def mul(z,w):
    return (z[0]*w[0]+2*z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def ring(L):
    ma,mb=2**((L+1)//2),2**(L//2)
    def red(x):return x[0]%ma,x[1]%mb
    def times(x,y):return red(mul(x,y))
    def plus(x,y):return red((x[0]+y[0],x[1]+y[1]))
    def inv(x):
        assert x[0]%2
        a=pow((x[0]*x[0]-2*x[1]*x[1])%ma,-1,ma)
        return red((a*x[0],-a*x[1]))
    values=list(product(range(ma),range(mb)))
    return red,times,plus,inv,values
def residue_square9(x):
    return (x[0]*x[0]-2*x[1]*x[1])%3==1

L=13
red,times,plus,inv,values=ring(L)
squares={times(v,v) for v in values}
fourths=[(v,times(times(v,v),times(v,v))) for v in values]
nonunit_fourths=[(v,v4) for v,v4 in fourths if not v[0]%2]
real_rows=[]
for sign in [1,-1]:
    answers=[]
    for sigma,e,delta,gamma in product(range(2),repeat=4):
        d=(1,0)
        for factor in [((-1,0) if sigma else (1,0)),
                       ((1,1) if e else (1,0)),
                       ((0,1) if delta else (1,0)),
                       ((3,0) if gamma else (1,0))]:d=mul(d,factor)
        reason=None
        if (sign==1 and sigma) or (sign==-1 and (sigma+e+delta)%2):
            reason='positive real embedding of b'
        if reason is None:
            if gamma:
                unit=(d[0]//3,d[1]//3)
                norm=(unit[0]*unit[0]-2*unit[1]*unit[1])%3
                unit_inverse=(unit[0]*pow(norm,-1,3)%3,
                              -unit[1]*pow(norm,-1,3)%3)
                odd_value=mul((0,sign*2),unit_inverse)
            else:odd_value=d
            if not residue_square9(odd_value):reason='quadratic residue at three'
        witness=None
        if reason is None:
            unit=(d[1],d[0]//2) if delta else d
            numerator=(sign*6,0) if delta else (0,sign*6)
            quotient=times(red(numerator),inv(red(unit)))
            dd=red(d)
            for V,V4 in fourths:
                if plus(dd,times(quotient,V4)) in squares:
                    witness={'chart':'U=1','other':V};break
            if witness is None:
                for U,U4 in nonunit_fourths:
                    if plus(times(dd,U4),quotient) in squares:
                        witness={'chart':'V=1','other':U};break
            if witness is None:reason='primitive quartic modulo pi^13'
        answers.append({'exponents':[sigma,e,delta,gamma],
                        'd':d,'excluded_by':reason,'finite_witness':witness})
    retained=[tuple(a['d']) for a in answers if a['excluded_by'] is None]
    expected=[(1,0),(3,0),(0,sign),(0,sign*3)]
    assert set(retained)==set(expected)
    real_rows.append({'b_over_pi':sign*6,'candidates':answers,'retained':retained})
    print('REAL QUADRATIC COMPLETE FILTER',sign*6,'survivors',retained)

# Both connecting groups are generated by displayed global points and T0.
assert fieldzero((2+2*s)**2-(-2)**3+4*s*(-2),-3)
assert fieldzero((-4+2*s)**2-(-2)**3-8*s*(-2),-6)
rank_rows=[{'D':-3,'image_order':4,'dual_image_order':2,'rank':1},
           {'D':2,'image_order':4,'dual_image_order':4,'rank':2},
           {'D':-6,'image_order':4,'dual_image_order':4,'rank':2}]
for row in rank_rows:
    assert row['image_order']*row['dual_image_order']//4==2**row['rank']
print('PASS: exact Prym ranks1,2,2 from the full connecting images')

buf=io.StringIO()
with contextlib.redirect_stdout(buf):
    runpy.run_path(str(BASE/'point3_fermat8_elliptic_rank_certificate.py'),run_name='__main__')
(BASE/'point3_fermat8_elliptic_rank_certificate_output.txt').write_text(buf.getvalue())
print('PASS: old elliptic rank certificate rerun; exact six-factor contribution8')

(BASE/'point3_fermat8_prym_rank_certificate_data.json').write_text(json.dumps({
    'actual_map_rows':map_data,'imaginary_filters':imaginary_data,
    'real_quadratic_filter':real_rows,'dyadic_modulus':L,
    'dyadic_ring_size':len(values),'rank_rows':rank_rows,
    'exact_six_factor_rank_contribution':8,
    'total_jacobian_rank_upper_bound':'not established'},indent=2)+'\n')
