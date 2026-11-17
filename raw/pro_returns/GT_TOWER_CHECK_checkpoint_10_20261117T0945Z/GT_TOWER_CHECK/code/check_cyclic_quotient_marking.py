#!/usr/bin/env python3
"""Exact word and rational checks for the cyclic/equianharmonic comparison."""
from pathlib import Path
import runpy
from sympy import symbols,sqrt,simplify,limit,oo
ns=runpy.run_path(str(Path(__file__).with_name('check_harmonic_marking.py')))
mul,inv,pow_,conj=map(ns.get,('fp_mul','fp_inv','fp_pow','fp_conj'))
s,r,tau,x,y,z=map(ns.get,('s','r','tau','x','y','z'))
a=inv(tau);b=conj(s,a)
assert mul(a,b)==r
assert mul(mul(a,b),a)==s
assert mul(mul(a,b),a)==mul(mul(b,a),b)
assert pow_(a,2)==x
assert pow_(mul(x,r),3)==()
assert conj(r,x)==y and conj(r,y)==z and conj(r,z)==x
assert inv(mul(a,s))==r
print('Exact positive braid dictionary: ab=r, aba=s, a=tau^-1, a^2=x, (xr)^3=1.')
print('Adjoint r cycles x,y,z; the physical third peripheral (as)^-1 equals r.')
t=symbols('t');rho=(1+sqrt(-3))/2;omega=simplify(rho**2)
w=lambda t:simplify((t-rho)/(t-1/rho))
h=1/(1-t)
assert simplify(w(h)-omega*w(t))==0
assert simplify(w(0)-omega)==0
assert simplify(w(1)-omega**2)==0
assert limit(w(t),t,oo)==1
assert simplify(w(rho))==0
assert simplify(((t-rho)/(t-1/rho))**3-((h-rho)/(h-1/rho))**3)==0
print('Exact rational marking: w(h(t))=omega*w(t); w(0)=omega, w(1)=omega^2, w(infinity)=1.')
print('u=w^3 is invariant; fixed points map to 0,infinity; the regular cusp maps to 1.')
print('ALL CHECKS PASSED; topology and profinite automorphism claims are proved in the LaTeX contribution.')
