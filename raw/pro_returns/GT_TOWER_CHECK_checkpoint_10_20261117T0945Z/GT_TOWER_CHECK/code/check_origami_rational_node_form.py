#!/usr/bin/env python3
"""Exact coordinate comparison for the origami's rational nodal form.

This checks the stated quadratic isomorphism and local leading equations.
It does not identify these local coordinates with the HLS quilt parameters.
"""
import sympy as s
x,u,v,w,t,r,X,Y=s.symbols('x u v w t r X Y')
P=4*x*(x-1)
original=(P**2-(1-t))*(P-1)
new=(u*u-1)*(4*u**4-4*u*u+t)
assert s.expand(original.subs(x,(1+s.sqrt(2)*u)/2)/2-new)==0
print('PASS: x=(1+sqrt(2)*u)/2, y=sqrt(2)*v gives v^2=(u^2-1)(4u^4-4u^2+t).')
assert s.expand(new.subs(t,0)-4*u*u*(u*u-1)**2)==0
print('PASS: at t=0 the two rational components are v=+/-2u(u^2-1), with nodes -1,0,1.')
assert s.simplify((1-(1+s.sqrt(2)*u)/2 - (1+s.sqrt(2)*(-u))/2))==0
print('PASS: sqrt(2) Galois conjugation corresponds on the original model to (x,y)->(1-x,-y).')
g=u*(u*u-1)
local=w*w-g*g-t*(u*u-1)/4
for a in [-1,0,1]:
    series=s.Poly(s.expand(local.subs(u,a+r)),r,w,t)
    quadratic=sum(c*r**i*w**j*t**k for (i,j,k),c in series.terms() if i+j+k<=2)
    if a==0:
        assert s.expand(quadratic-(w*w-r*r+t/4))==0
        print('Node0 exact quadratic truncation:',quadratic)
    else:
        expected=w*w-4*r*r-a*t*r/2
        assert s.expand(quadratic-expected)==0
        print('Node',a,'exact total-degree-two truncation:',quadratic)
        completed=s.expand((w-2*a*r-t/8)*(w+2*a*r+t/8)+t*t/64)
        assert s.expand(completed-expected)==0
        print('PASS completed-square leading smoothing term -t^2/64.')
# In the normalized branch coordinate z=(u+1)/(1-u), the derivatives
# of z at0 and 1/z at1 are 2 and -1/2; at -1, dz/du=1/2.
z=(u+1)/(1-u)
assert s.diff(z,u).subs(u,0)==2
assert s.diff(z,u).subs(u,-1)==s.Rational(1,2)
assert s.diff(1/z,u).subs(u,1)==-s.Rational(1,2)
print('PASS normalized branch-coordinate derivatives: node0=2; node-1=1/2; node1=-1/2.')
print('SCOPE: these explicit coordinate data still require a comparison to the published quilt deformation parameters.')
