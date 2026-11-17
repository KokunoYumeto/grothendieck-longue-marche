#!/usr/bin/env python3
"""Exact maps for the pointed H3 cover and its elliptic compactifications."""
import sympy as s

u,v,x,y=s.symbols('u v x y')
C=3*u**3-2*v**3-1
den=3*u*(u-1)-2*v*(v-1)
xe=18*(u*v-1)/den
ye=-27*(3*u*(u+1)+2*v*(v+1))/den
def zero_mod(expr, relation, variables):
    num=s.fraction(s.cancel(expr))[0]
    return s.rem(s.Poly(num,*variables),s.Poly(relation,*variables)).is_zero
assert zero_mod(ye**2-xe**3+243,C,(u,v))
print('PASS: the explicit pointed cubic-to-Mordell map lands on y^2=x^3-243')
assert xe.subs({u:s.Rational(-1,5),v:s.Rational(-4,5)})==7
assert ye.subs({u:s.Rational(-1,5),v:s.Rational(-4,5)})==-10
assert zero_mod((3*(3*u**3+2*v**3))**2-(6*u*v)**3-9,C,(u,v))
print('PASS: the cubic degree-three map lands on y^2=x^3+9')

phix=(x**3+36)/x**2
phiy=y*(x**3-72)/x**3
psix=(x**3-972)/(9*x**2)
psiy=y*(x**3+1944)/(27*x**3)
assert zero_mod(phiy**2-phix**3+243,y*y-x**3-9,(y,x))
assert zero_mod(psiy**2-psix**3-9,y*y-x**3+243,(y,x))
print('PASS: both degree-three isogeny formulas land on their stated curves')

f=x**3-243
x2=s.cancel(9*x**4/(4*f)-2*x)
r2=s.cancel(-1+3*x*x*(x-x2)/(2*f))
k3=s.cancel((r2-1)/(x2-x))
x3=s.cancel(f*k3*k3-x-x2)
r3=s.cancel(-1+k3*(x-x3))
comp_x=s.cancel((psix**3+36)/psix**2)
comp_y_factor=s.cancel((x**3+1944)/(27*x**3)*(psix**3-72)/psix**3)
assert s.cancel(comp_x-x3)==0 and s.cancel(comp_y_factor-r3)==0
print('PASS: phi composed with psi is exactly multiplication by3 on y^2=x^3-243')

R=(y-27)/(3*x); S=(y+27)/(3*x)
X=psix; Y=psiy
k=(Y-15)/(X-6)
Xf=k*k-X-6
ui=s.cancel(Xf*S/(6*(k-3)))
vi=s.cancel(Xf*R/(6*(k-2)))
assert zero_mod(3*ui**3-2*vi**3-1,y*y-x**3+243,(y,x))
print('PASS: the explicit inverse lands on 3u^3-2v^3=1')
Yf=-Y+k*(X-Xf)
assert zero_mod(6*ui*vi-Xf,y*y-x**3+243,(y,x))
assert zero_mod(3*(3*ui**3+2*vi**3)-Yf,y*y-x**3+243,(y,x))
print('PASS: g0 composed with iota inverse is psi plus the point(6,15)')
di=3*ui*(ui-1)-2*vi*(vi-1)
assert zero_mod(18*(ui*vi-1)-x*di,y*y-x**3+243,(y,x))
assert zero_mod(-27*(3*ui*(ui+1)+2*vi*(vi+1))-y*di,y*y-x**3+243,(y,x))
print('PASS: composing the inverse with the cubic-to-Mordell map is the identity')
assert s.cancel(x2-x+3*x*(x**3-972)/(4*f))==0
assert any(exponent%3 for exponent in s.factorint(972).values())
print('PASS: division polynomial for E is 3*x*(x^3-972); 972 is not a rational cube')
