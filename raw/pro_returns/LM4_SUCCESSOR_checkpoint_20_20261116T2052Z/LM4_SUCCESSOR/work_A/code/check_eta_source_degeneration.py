#!/usr/bin/env python3
"""Exact new eta-pencil identities; eta is not the old product coordinate q=vw."""
import sympy as s
v,w,eta,u=s.symbols('v w eta u')
e=(v*w-1)/(w-1)**2
assert s.cancel(e+1-w*(v+w-2)/(w-1)**2)==0
assert s.cancel(s.diff(e,v)-w/(w-1)**2)==0
pol=eta*w**2+(-2*eta-u)*w+(eta+1)
assert s.expand(pol- (eta*(w-1)**2-u*w+1))==0
assert s.expand(pol.subs(eta,-1)-w*(2-u-w))==0
assert s.expand(s.discriminant(pol,w)-(u**2+4*eta*(u-1)))==0
assert s.expand(s.discriminant(pol,w).subs(eta,-1)-(u-2)**2)==0
print('PASS eta+1 = w(v+w-2)/(w-1)^2')
print('PASS d eta/dv = w/(w-1)^2, a unit everywhere on actual Y')
print('PASS v=u fiber equation eta*w^2+(-2eta-u)*w+(eta+1)=0')
print('PASS at eta=-1 it is w*(2-u-w), with roots 0 and 2-u')
print('PASS discriminant u^2+4eta(u-1), specializing to (u-2)^2')
print('Conclusion: the actual source fiber is smooth but boundary-atypical; one constant puncture escapes to removed w=0.')
print('No relative kernel-surjectivity or monodromy identity is asserted.')
