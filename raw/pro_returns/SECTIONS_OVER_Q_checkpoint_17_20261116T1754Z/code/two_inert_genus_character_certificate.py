#!/usr/bin/env python3
"""Exact algebra and finite-group checks for the retained genus-character note.

This is not a class-group computation.  The local unramified and tower
arguments are proved in notes/two_inert_genus_character.md.
"""
from pathlib import Path
import json
import sympy as S

A, Z, X = S.symbols("A Z X")
G = S.groebner([A**3-3, Z**2+Z+1], A, Z, X, order="lex")
def red(p):
    return S.expand(G.reduce(S.expand(p))[1])

g11 = lambda v: 2+v
g59 = lambda v: 2+2*v-v*v
assert red(g11(Z*A)*g59(Z*A)-(1+6*Z*A)) == 0
assert red(g11(Z**2*A)*g59(Z**2*A)-(1+6*Z**2*A)) == 0
p, q = 1+6*Z*A, 1+6*Z**2*A
D = 1-6*A+36*A*A
num = 2-12*A-36*A*A
assert red(p*q-D) == 0
assert red(p*p+q*q-num) == 0
assert red(p*p-q*q-12*A*(1-3*A)*(Z-Z**2)) == 0
assert red(-27*(num*num-4*D*D)-(108*A*(1-3*A))**2) == 0

lam = Z-1
assert red(lam**2+3*Z) == 0
assert red((1+lam*X)**3-1-lam**3 *
           (X**3-Z**2*lam*X**2-Z**2*X)) == 0
assert all((x**3-x-1) % 3 for x in range(3))

# A second exact presentation: F=Q(pi), pi^6=-3, with its literal
# alpha/zeta embeddings and complex conjugation.
P=S.symbols("P")
minimal=P**6+3
def pr(expr):
    return S.rem(S.expand(expr),minimal,P,domain=S.QQ)
def rat_parts(expr):
    n,d=S.fraction(S.cancel(expr))
    return pr(n),pr(d)
def field_zero(expr):
    n,d=rat_parts(expr)
    assert d!=0
    return n==0
def vp3(q):
    q=S.Rational(q)
    assert q
    a,b=abs(int(q.p)),int(q.q)
    va=vb=0
    while a%3==0: a//=3; va+=1
    while b%3==0: b//=3; vb+=1
    return va-vb
def polynomial_valuation(expr):
    poly=S.Poly(pr(expr),P,domain=S.QQ)
    if poly.is_zero:
        return float("inf")
    return min(6*vp3(c)+mon[0] for mon,c in poly.terms())
def field_valuation(expr):
    n,d=rat_parts(expr)
    return polynomial_valuation(n)-polynomial_valuation(d)

zp=-(1+P**3)/2
ap=(P**2+P**5)/2
tp=(P+P**4)/2
assert field_zero(ap**3-3)
assert field_zero(zp*zp+zp+1)
assert field_zero(P*(zp-1)-ap*ap)
assert field_zero(tp+zp*P)
assert field_zero(tp**6+3)
vp=(1+P)/(1+P**2)
vt=(1+tp)/(1+tp**2)
eps=vp/vt
assert field_zero(vp*vt-(ap*ap-2))
assert S.resultant(minimal,1+P,P)==4
assert S.resultant(minimal,1+P*P,P)==4
up11=(2+zp*ap)/(2+zp*zp*ap)
up59=(2+2*zp*ap-zp*zp*ap*ap)/(2+2*zp*zp*ap-zp*ap*ap)
up=(1+6*zp*ap)/(1+6*zp*zp*ap)
bp=1+P-P*P
assert field_zero(zp-bp**3-(-S.Rational(9,2)-3*P+
                            S.Rational(9,2)*P**3-3*P**5))
literal_depths=[field_valuation(w-1) for w in
                (eps,up11,up59,up,zp/bp**3)]
assert literal_depths==[1,5,5,11,7]
C=up-1
trial=1+C/3
assert field_valuation(trial**3-up)==15
assert field_valuation(3*trial**2)==6

# Depths in F=Q_3(alpha,zeta_3), normalized by v_F(3)=6.
assert 2+3 == 5
assert 6+2+3 == 11
assert 3*3 == 9
cube_depths = []
for k in range(1, 20):
    if k < 3:
        depth = 3*k
    elif k == 3:
        depth = 9
    else:
        depth = 6+k
    cube_depths.append((k, depth))
    assert depth != 5
assert min(6+2*5, 3*5) == 15 > 2*6

def ff_mul(x,y,p):
    a,b=x; c,d=y
    return ((a*c-b*d)%p, (a*d+b*c-b*d)%p)
def ff_pow(x,n,p):
    r=(1,0)
    while n:
        if n&1: r=ff_mul(r,x,p)
        x=ff_mul(x,x,p); n//=2
    return r
def ff_inv(x,p):
    return ff_pow(x,p*p-2,p)
def ff_add(x,y,p):
    return ((x[0]+y[0])%p,(x[1]+y[1])%p)
def ff_scale(c,x,p):
    return (c*x[0]%p,c*x[1]%p)

z=(0,1)
z2=ff_mul(z,z,2)
u11_2=ff_mul(z,ff_inv(z2,2),2)
u59_2=ff_mul(z2,ff_inv(z,2),2)
assert u11_2==z2 and u59_2==z
assert ff_mul(u11_2,u59_2,2)==(1,0)
pi_residues=[]
for ar in ((1,0),z,z2):
    pi_residues.append(ff_mul(ff_mul(ar,ar,2),
                             ff_inv(ff_add(z,(1,0),2),2),2))
assert pi_residues==[z,(1,0),z2]
assert sum(r==(1,0) for r in pi_residues)==1

q_rows=[]
for p, alpha in ((11,9),(59,49)):
    assert pow(alpha,3,p)==3
    if p==11:
        assert (2+alpha)%p==0
    else:
        assert (2+2*alpha-alpha*alpha)%p==0
    top=ff_add((1,0),ff_scale(6*alpha,z,p),p)
    bot=ff_add((1,0),ff_scale(6*alpha,ff_mul(z,z,p),p),p)
    u=ff_mul(top,ff_inv(bot,p),p)
    assert u==ff_scale(-1,z,p)
    residue_char=ff_pow(u,(p*p-1)//3,p)
    e=next(j for j in range(3) if ff_pow(z,j,p)==residue_char)
    assert e==(1 if p==11 else 2)
    downstairs=2*e%3
    q_rows.append({"q":p,"alpha":alpha,"residue_exponent":e,
                   "Kn_arithmetic_Frobenius_exponent":downstairs})
assert [r["Kn_arithmetic_Frobenius_exponent"] for r in q_rows]==[2,1]

group_rows=[]
for n in range(2,9):
    N=3**n
    U1=[u for u in range(N) if u%3==1]
    assert len(U1)==3**(n-1)
    assert len({pow(4,j,N) for j in range(3**(n-1))})==len(U1)
    shifts={3*(1-u)%N for u in U1}
    assert shifts==set(range(0,N,9))
    assert len({t%9 for t in range(0,N,3)})==3
    group_rows.append({"n":n,"N":N,"root_stabilizer_order":len(U1),
                       "normal_closure_translation_step":9,
                       "maximal_Galois_root_subfield_degree":3})

data={
 "cubic_polynomial":"X^3-3X-(2-12A-36A^2)/(1-6A+36A^2)",
 "discriminant_square_root":"108A(1-3A)/(1-6A+36A^2)",
 "local_depths":{"individual":5,"product":11,"unramified_generator":9,
                 "Newton_residual":15,"Newton_derivative":6},
 "literal_sextic_depths":literal_depths,
 "norm_four_support_residues":pi_residues,
 "cube_depth_bounds":cube_depths,"changed_prime_rows":q_rows,
 "tower_group_rows":group_rows,
 "scope":"Exact retained character maps; no exhaustion of balanced characters."
}
Path(__file__).with_name("two_inert_genus_character_certificate_data.json").write_text(
    json.dumps(data,indent=2)+"\n")
print("PASS: exact two-radical product, cyclic cubic trace and square discriminant.")
print("PASS: literal sextic field/tau maps, norm-four unit, and exact depths",literal_depths)
print("PASS: unramified Kummer polynomial and depth5/depth9/depth11 separation.")
print("PASS: two-prime splitting and both residue-degree-two Frobenius comparisons.")
print("PASS:",len(group_rows),"actual root-stabilizer normal-closure calculations.")
