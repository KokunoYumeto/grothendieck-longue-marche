#!/usr/bin/env python3
"""Evaluate the actual q=4 local class-three obstruction in Hall coordinates."""
from fractions import Fraction as Q
from pathlib import Path
from random import Random
import json
import sympy as s
import a_class3_frobenius as mag

def choose2(a):return a*(a-1)/2
def mult(g,h):
    a,b,n,r,t=g;A,B,N,R,T=h
    return (a+A,b+B,n+N-A*b,
            r+R+b*A*(A+1)/2-A*n,
            t+T+A*b*(b+1)/2-B*n+A*b*B)
def inv(g):
    a,b,n,r,t=g
    return (-a,-b,-n-a*b,-r-b*choose2(a)-a*n,-t-a*choose2(b)-b*n)
identity=(Q(0),)*5
def power(g,n):
    if n<0:return power(inv(g),-n)
    out=identity
    for _ in range(n):out=mult(out,g)
    return out
def frob4(g):
    a,b,n,r,t=g
    return (4*a,4*b,4*b+16*n,40*n+64*r,
            24*n+64*t-16*choose2(b)-Q(15,2)*b)
def simplify(g):return tuple(s.expand(a) for a in g)

a,b,n,A,B,N=s.symbols('a b n A B N')
inertia=(a,b,n,s.Integer(0),s.Integer(0))
fr=(A,B,N,s.Integer(0),s.Integer(0))
err=simplify(mult(mult(mult(fr,frob4(inertia)),inv(fr)),power(inertia,-4)))
assert err[:2]==(0,0)
lower=4*b+12*n+4*(A*b-B*a)+6*a*b
assert s.expand(err[2]-lower)==0
R=s.factor(err[3]);S=s.factor(err[4])
print('Exact lower relation:',lower)
print('Exact d-obstruction:',R)
print('Exact e-obstruction:',S)

# Every Hall formula is independently tested in the integral Magnus model.
rng=Random(540054)
hall_checks=0
for _ in range(100):
    g=tuple(Q(rng.randrange(-5,6)) for _ in range(5))
    h=tuple(Q(rng.randrange(-5,6)) for _ in range(5))
    assert mag.normal(*mult(g,h))==mag.mul(mag.normal(*g),mag.normal(*h))
    assert mag.normal(*inv(g))==mag.inv(mag.normal(*g))
    X,Y=mag.action(Q(4),Q(1))
    assert mag.normal(*frob4(g))==mag.evaluate(mag.normal(*g),X,Y)
    hall_checks+=1

def mod3(x):
    x=Q(x)
    assert x.denominator%3
    return x.numerator*pow(x.denominator,-1,3)%3

# Actual lower tame sections are specified by the exact class-two relation.
# Their class-three obstruction is read in (Z/3)^2, since64-4=60.
samples=[]
witness=None
for aa in range(-2,3):
    for bb in range(-2,3):
        for AA in range(-2,3):
            for BB in range(-2,3):
                cc=Q(-4*bb-4*(AA*bb-BB*aa)-6*aa*bb,12)
                if cc.denominator%3==0:continue
                for NN in range(-1,2):
                    ng=(Q(aa),Q(bb),cc,Q(0),Q(0))
                    fg=(Q(AA),Q(BB),Q(NN),Q(0),Q(0))
                    er=mult(mult(mult(fg,frob4(ng)),inv(fg)),power(ng,-4))
                    assert er[:3]==(0,0,0)
                    obs=[mod3(er[3]),mod3(er[4])]
                    # Twisting inertia in either central coordinate changes
                    # exactly by60, with the sign of the correction verified.
                    for j in [3,4]:
                        nn=list(ng);nn[j]+=1
                        e2=mult(mult(mult(fg,frob4(tuple(nn))),inv(fg)),power(tuple(nn),-4))
                        expected=list(er);expected[j]+=60
                        assert e2==tuple(expected)
                    rec={'inertia':[str(v) for v in ng[:3]],
                         'Frobenius':[str(v) for v in fg[:3]],
                         'error':[str(v) for v in er[3:]],'mod3':obs}
                    samples.append(rec)
                    if witness is None and any(obs):witness=rec
assert witness
# A particularly small genuine lower tame section has n=y and F=x^-1.
# Varying the central Frobenius coordinate gives error e^(5/2-4N).
simple=[]
for NN in range(6):
    ng=(Q(0),Q(1),Q(0),Q(0),Q(0))
    fg=(Q(-1),Q(0),Q(NN),Q(0),Q(0))
    er=mult(mult(mult(fg,frob4(ng)),inv(fg)),power(ng,-4))
    assert er==(0,0,0,0,Q(5,2)-4*NN)
    assert (mod3(er[4])==0)==(NN%3==1)
    simple.append({'Frobenius_c_exponent':NN,'e_error':str(er[4]),
                   'lifts_to_class3':NN%3==1})
ng=(Q(0),Q(1),Q(0),Q(0),Q(1,40))
fg=(Q(-1),Q(0),Q(1),Q(0),Q(0))
assert mult(mult(mult(fg,frob4(ng)),inv(fg)),power(ng,-4))==identity
assert 60==3*20 and 63==9*7
print('PASS:',hall_checks,'independent Hall/Magnus comparisons.')
print('PASS:',len(samples),'exact lower sections and their central correction signs.')
print('One obstructed lower section:',witness)

result={'statement':'E.54','status':'PASS',
        'coordinate_order':'x^a y^b c^n d^r e^s',
        'lower_tame_relation':str(lower),
        'central_d_error':str(R),'central_e_error':str(S),
        'central_correction_multiplier':60,
        'local_obstruction_group':'(Z/3)^2',
        'nonempty_local_fiber_group':'(Z/9)^2',
        'Hall_Magnus_checks':hall_checks,
        'lower_section_samples':len(samples),
        'obstructed_sample':witness,
        'simple_family':simple,
        'positive_exact_lift':{'inertia':['0','1','0','0','1/40'],
                               'Frobenius':['-1','0','1','0','0']},
        'samples':samples}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS: exact local obstruction formula and arithmetic Hall model saved.')
