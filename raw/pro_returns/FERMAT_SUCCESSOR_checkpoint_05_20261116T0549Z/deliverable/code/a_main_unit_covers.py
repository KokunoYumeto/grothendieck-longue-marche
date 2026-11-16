#!/usr/bin/env python3
"""Exact supplementary two-cover calculations for A.65.

This certifies the necessary cover reduction and its positive-rank diagnostic.
The theorem itself is proved by rational-unit rigidity and a Faltings argument;
no finite-abelian-descent excellence of the positive-rank curves is asserted.
"""
from pathlib import Path
import csv
import math
import sympy as s

d,c,u,V,w,x,y,B=s.symbols('d c u V w x y B')
z=(d-1)/2

def rd(f):
    num,den=s.fraction(s.cancel(f))
    assert not den.has(d)
    return s.cancel(s.rem(s.expand(num),d*d+3,d)/den)

def re(f):
    num,den=s.fraction(s.cancel(f))
    num=s.rem(s.expand(num),x**3-y*y-y-1,x)
    num=s.rem(s.expand(num),d*d+3,d)
    return s.cancel(num/den)

def add(P,Q):
    xp,yp=P; xq,yq=Q
    m=3*xp*xp/(2*yp+1) if P==Q else (yq-yp)/(xq-xp)
    xr=s.cancel(m*m-xp-xq)
    yr=s.cancel(-yp-1+m*(xp-xr))
    return xr,yr

P=(s.Integer(1),s.Integer(0))
P2=add(P,P); P3=add(P2,P)
assert P2==(7,-19)
assert P3==(s.Rational(73,36),s.Rational(487,216))
assert rd(z*z+z+1)==0
print('E: y^2+y=x^3-1, P=(1,0).')
print('2P =',P2,'; 3P =',P3)
print('At every rational prime q>=5, reduction of 3P is not O.')
print('A unit profinite scalar preserves membership in E[3] in every finite reduction.')

F=y*y+y-x**3+1
res=rd(F.subs({x:u*w,y:z-c*w*w}))
base=c*c*w*w-u**3*w-d*c
assert s.expand(res-w*w*base)==0
vexpr=2*c*c*w-u**3
D=4*d*c**3
assert s.expand(vexpr*vexpr-u**6-D-4*c*c*base)==0
print('w^2=(zeta_3-y)/c gives u=x/w, V=2c^2 w-u^3,')
print('  C_c: V^2=u^6+D, D=4*sqrt(-3)*c^3.')
print('Inverse: w=(V+u^3)/(2c^2), x=u*w, y=zeta_3-c*w^2.')

X1=u*u; Y1=V
X2=D/u**2; Y2=D*V/u**3
assert s.cancel(Y1**2-X1**3-D)==V**2-u**6-D
assert s.cancel(Y2**2-X2**3-D**2-D**2*(V**2-u**6-D)/u**6)==0
assert s.cancel(s.diff(X1,u)/(2*Y1)-u/V)==0
assert s.cancel(s.diff(X2,u)/(2*Y2)+1/V)==0
assert rd(D**2+48*c**6)==0
print('Degree-two targets: E_D and E_(D^2); differential coefficients (u,-1).')
print('D^2=-48*c^6, so the second target is the fixed E9 short model.')

f=z-y
xp=d*f/x**2
yp=z*z+d*f*f/x**3
m=(y-z)/x
assert re(m*m-x-xp)==0
assert re(-y-1+m*(x-xp)-yp)==0
assert rd(8*z*z+4+4*d)==0
print('After scaling the second quotient to E9, it is Q -> Q+(0,zeta_3).')
assert re((z-y)*(z*z-y)-x**3)==0
print('Norm identity: (zeta_3-y)*(zeta_3^2-y)=x^3.')

rows=[]
for label,cc in [('1',1),('-1',-1),('2',2),('-2',-2),
                 ('delta',d),('-delta',-d),('2delta',2*d),('-2delta',-2*d)]:
    dd=rd(D.subs(c,cc))
    norm=rd(cc*s.sympify(cc).subs(d,-d))
    rows.append((label,dd,norm))
print('The eight K({2,3},2) classes and their Prym coefficients:')
for label,dd,norm in rows:
    print(' ',label,'D=',dd,'Norm(c)=',norm)

XP=rd(z*z); YP=2+d
assert rd(YP*YP-XP**3-4*d)==0
assert rd((2-d)**2-z**3+4*d)==0
print('For c=1, E_(4delta)(K) contains (zeta_3^2,2+delta).')
print('For c=-1, its conjugate contains (zeta_3,2-delta).')
counts=[]
for q in (7,13):
    for dr in range(q):
        if (dr*dr+3)%q: continue
        br=4*dr%q
        count=1+sum(1 for xx in range(q) for yy in range(q)
                    if (yy*yy-xx**3-br)%q==0)
        counts.append((q,dr,br,count))
        print('  q,delta_mod_q,B_mod_q,#E(F_q) =',counts[-1])
assert (7,5,6,4) in counts
assert (13,6,11,19) in counts
assert math.gcd(4,19)==1
print('The good reductions with orders4 and19 force K-rational torsion to be trivial.')
print('Hence both displayed points are nontorsion; both Pryms have rank at least2 over K.')

census=Path(__file__).with_name('a_main_sextic_census.csv')
with census.open() as fobj:
    saved={int(r['coefficient']):r for r in csv.DictReader(fobj)}
print('Previously certified rational Prym cases (not fresh numerical rank estimates):')
for bb,expected in [(36,1),(-36,0),(288,1),(-288,1)]:
    r=saved[bb]; twist=saved[-27*bb]
    assert int(r['analytic_rank'])==expected
    assert int(twist['analytic_rank'])==expected
    print('  B=',bb,'N=',r['conductor'],'rank_Q=',expected,
          'rank_K=',2*expected,'certificate=',r['arb_interval'])

# The rational 3-isogeny explains equality with the quadratic (-3)-twist.
tx=(x**3+4*B)/x**2
ty=y*(x**3-8*B)/x**3
num=s.fraction(s.cancel(ty*ty-tx**3+27*B))[0]
assert s.rem(num,y*y-x**3-B,y)==0
print('The exact 3-isogeny E_B -> E_(-27B) identity is verified.')
bb=s.symbols('b')
Cnorm=V*V-4*bb**3*u**6+3
assert s.expand(F.subs({x:bb*u*u,y:(V-1)/2})-Cnorm/4)==0
XA=4*bb**3*u*u; YA=4*bb**3*V
XB=-3/u**2; YB=-3*V/u**3
assert s.cancel(YA*YA-XA**3+48*bb**6-16*bb**6*Cnorm)==0
assert s.cancel(YB*YB-XB**3-36*bb**3-9*Cnorm/u**6)==0
assert s.cancel(s.diff(XA,u)/(2*YA)-u/V)==0
assert s.cancel(s.diff(XB,u)/(2*YB)+1/V)==0
print('The Q norm cover w^2=x/b is C_b: V^2=4b^3*w^6-3.')
print('Its two targets are fixed E9 and E_(36*b^3), with independent differentials.')
print('Norm(c) is square class1 for c=+/-1,+/-2 and class3 for the other four.')
r=saved[972]
assert int(r['analytic_rank'])==0
print('For b=3 the Prym E972 has certified L(1)=',r['arb_interval'])
tc=[]
for q in (5,7,13):
    count=1+sum(1 for xx in range(q) for yy in range(q)
                if (yy*yy-xx**3-972)%q==0)
    tc.append(count)
    print('  E972 reduction q,#E(F_q)=',q,count)
assert tc==[6,4,9]
assert math.gcd(*tc)==1
print('These reductions force E972(Q)_tors=0; rank0 gives E972(Q)={O}.')
print('The inverse fibre of O on C_3 is w=0,V^2=-3, so C_3(Q) is empty.')
print('Stoll finite-support descent therefore makes C_3(A_Q)^(f-ab) empty.')
print('Hence norm class b=3, and all four delta-containing c classes, are excluded.')
print('No rank assertion is made for c=+/-2; positive-rank obstructions already occur at c=+/-1.')
print('All exact unit-cover reduction checks passed.')
