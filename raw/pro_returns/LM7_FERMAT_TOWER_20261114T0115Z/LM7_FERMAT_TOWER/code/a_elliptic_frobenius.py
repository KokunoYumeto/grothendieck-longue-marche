#!/usr/bin/env python3
"""Exact truncated Magnus arithmetic for the based elliptic Frobenius at two."""
from fractions import Fraction as Q
from pathlib import Path
import json

# The rational Weierstrass map retains the actual cubic tangent.
import sympy as sp
s0=sp.Symbol('s')
q=(1+s0**3)**sp.Rational(1,3)
t=sp.Rational(2,3)*s0/(1+q)
assert sp.limit(t/s0,s0,0)==sp.Rational(1,3)
xx,yy=sp.symbols('xx yy')
assert sp.expand((9+yy)**3+(9-yy)**3+(-6*xx)**3)==54*(27+yy**2-4*xx**3)
points2=[(a,b) for a in range(2) for b in range(2) if (b*b+b-a**3+7)%2==0]
assert len(points2)+1==3

DEG=3
one={():Q(1)}
x={():Q(1),(0,):Q(1)}
y={():Q(1),(1,):Q(1)}
def add(*ps):
    out={}
    for p in ps:
        for w,a in p.items():out[w]=out.get(w,Q(0))+a
    return {w:a for w,a in out.items() if a}
def scale(p,a):return {w:a*b for w,b in p.items() if a*b}
def mul(p,q):
    out={}
    for w,a in p.items():
        for v,b in q.items():
            if len(w+v)<=DEG:out[w+v]=out.get(w+v,Q(0))+a*b
    return {w:a for w,a in out.items() if a}
def power(p,a):
    a=Q(a);u=add(p,scale(one,-1));term=one;out=one;coef=Q(1)
    for k in range(1,DEG+1):
        term=mul(term,u);coef*=Q(a-k+1,k);out=add(out,scale(term,coef))
    return out
def prod(*ps):
    out=one
    for p in ps:out=mul(out,p)
    return out
def inv(p):return power(p,-1)
def comm(p,q):return prod(p,q,inv(p),inv(q))
c=comm(x,y);d=comm(x,c);e=comm(y,c);z=inv(c)
def evaluate(p,X,Y):
    us=[add(X,scale(one,-1)),add(Y,scale(one,-1))];out={}
    for w,a in p.items():
        out=add(out,scale(prod(*(us[i] for i in w)),a))
    return out
def compose(a,b):return tuple(evaluate(v,*a) for v in b)
identity=(x,y)
def normal(a,b,n,r,s):
    return prod(power(x,a),power(y,b),power(c,n),power(d,r),power(e,s))
def hall(p):
    a=p.get((0,),Q(0));b=p.get((1,),Q(0))
    q=prod(inv(normal(a,b,0,0,0)),p)
    n=q.get((0,1),Q(0));q=prod(power(c,-n),q)
    r=q.get((0,0,1),Q(0));q=prod(power(d,-r),q)
    s=-q.get((0,1,1),Q(0));q=prod(power(e,-s),q)
    assert q==one
    ans=(a,b,n,r,s);assert normal(*ans)==p
    return ans
def inner(q):return prod(q,x,inv(q)),prod(q,y,inv(q))
def T1(a):return mul(x,power(y,-Q(a))),y
def T2(a):return x,mul(y,power(x,Q(a)))
def word(actions):
    out=identity
    for a in actions:out=compose(out,a)
    return out
def Apower(a,n):
    out=identity
    for _ in range(n):out=compose(out,a)
    return out

# Proposition5.7.3: these are the actual Weierstrass-section Dehn twists.
assert word([T1(1),T2(1),T1(1)])==word([T2(1),T1(1),T2(1)])
central=Apower(word([T1(1),T2(1)]),6)
assert central==inner(inv(c))

# Theorem5.2.4 with its exact z=[x,y]^-1 convention.  The leading Ihara
# coefficient is (chi^2-1)/24; higher terms cannot survive this substitution.
def tate(chi):
    chi=Q(chi);b=(chi*chi-1)/24
    fplus=power(comm(prod(x,y,inv(x)),z),b)
    fminus=power(comm(inv(y),z),b)
    out=(prod(power(z,(1-chi)/2),fplus,x,inv(fminus)),
         prod(fminus,power(y,chi),inv(fminus)))
    assert evaluate(c,*out)==power(c,chi)
    return out

# A diagonal SL2 lift, whose discriminant winding is -(2u+u^-1-3).
def diagonal(u):
    u=Q(u)
    out=word([T2(u),T1(1/u),T2(u-1),T1(-1),T2(-1)])
    assert hall(out[0])[:2]==(u,0)
    assert hall(out[1])[:2]==(0,1/u)
    assert evaluate(c,*out)==c
    return out

base=compose(diagonal(-2),tate(4))
base_delta=Q(15,2)
assert hall(base[0])[:2]==(-2,0) and hall(base[1])[:2]==(0,-2)

# Theorem6.10.3 on the Tate kernel: an increment kappa_Delta corresponds
# in ambient class three to Ad(c^(kappa_Delta/12)).
def frobenius(delta):
    return compose(inner(power(c,(Q(delta)-base_delta)/12)),base)
local=frobenius(0)
principal=frobenius(Q(3,2))
assert principal==compose(inner(power(c,Q(1,8))),local)

# A path change by T1(1/2) supplies the coherent discriminant-root
# coboundary.  We retain and test both orientations instead of assigning
# the sign from notation alone.
path_forward=word([T1(Q(-1,2)),local,T1(Q(1,2))])
path_reverse=word([T1(Q(1,2)),local,T1(Q(-1,2))])
path_forward_ok=path_forward==principal
path_reverse_ok=path_reverse==principal
assert path_forward_ok != path_reverse_ok

# The actual degree-nine elliptic cover subgroup maps to the lattice
# P=<x^3,y^3,c,d,e> inside the ambient class-three group.
P=[power(x,3),power(y,3),c,d,e]
def Pcoords(p):
    a,b,n,r,s=hall(p);ans=(a/3,b/3,n,r,s)
    assert all(q.denominator%3 for q in ans)
    return ans
images={name:list(map(str,Pcoords(evaluate(p,*principal))))
        for name,p in zip(['x^3','y^3','c','d','e'],P)}
for action in [local,principal]:
    assert evaluate(c,*action)==power(c,4)
    assert evaluate(d,*action)==power(d,-8)
    assert evaluate(e,*action)==power(e,-8)
    for p in action:
        assert all(q.denominator%3 for q in p.values())

root_checks=[]
for n in range(1,13):
    q=3**n;k=(q+1)//2
    assert (2*k-1)%q==0
    if n>1:assert k%(q//3)==root_checks[-1]['ratio_exponent']
    assert (4*k-k)%q==(3*pow(2,-1,q))%q
    root_checks.append({'n':n,'ratio_exponent':k,'discriminant_Kummer_value_mod_3n':(3*k)%q})

out={'status':'PASS','statement':'E.58',
     'good_reduction_points_F2':points2,'trace_Frobenius2':0,
     'Weierstrass_tangent_leading_coefficient':'1/3 before [3], 1 after [3]',
     'Hall_order':'x^a y^b c^n d^r e^s; c=[x,y], d=[x,c], e=[y,c]',
     'central_braid':'(T1 T2)^6 = Ad(c^-1)',
     'Tate4_images':[list(map(str,hall(p))) for p in tate(4)],
     'diagonal_minus2_images':[list(map(str,hall(p))) for p in diagonal(-2)],
     'reference_delta':str(base_delta),
     'reference_images':[list(map(str,hall(p))) for p in base],
     'Q2_discriminant_images':[list(map(str,hall(p))) for p in local],
     'principal_discriminant_images':[list(map(str,hall(p))) for p in principal],
     'relative_inner_correction':'principal = Ad(c^(1/8)) Q2',
     'path_transport':('T1(-1/2) Q2 T1(1/2)' if path_forward_ok else 'T1(1/2) Q2 T1(-1/2)'),
     'P_generator_images':images,'root_ratio_checks':root_checks}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
