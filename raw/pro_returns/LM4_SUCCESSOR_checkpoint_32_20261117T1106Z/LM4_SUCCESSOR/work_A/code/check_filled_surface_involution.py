#!/usr/bin/env python3
"""Exact rational identities for the actual Y_b fixed-subgroup proof."""
import sympy as s
v,w,q,u,r,c=s.symbols('v w q u r c')
V=v*(w-1)/(1-v);W=w*(v-1)/(1-w)
assert s.cancel(V*W-v*w)==0
assert s.cancel(V.subs({v:V,w:W},simultaneous=True)-v)==0
assert s.cancel(W.subs({v:V,w:W},simultaneous=True)-w)==0
assert s.cancel(V.subs(w,2-v)-v)==0
assert s.cancel(W.subs(w,2-v)-(2-v))==0
assert s.cancel(V.subs(w,q/v)-(v-q)/(v-1))==0
M=s.Matrix([[1,-q],[1,-1]])
assert M*M==(1-q)*s.eye(2)
f=(v-q)/(v-1)
assert s.cancel(f.subs(v,0)-q)==0
assert s.cancel(f.subs(v,q))==0
assert s.cancel(f.subs({v:r,q:r*r})+r)==0
assert s.cancel(f.subs({v:-r,q:r*r})-r)==0
assert s.cancel((f-1).subs(v,u+1)-(1-q)/u)==0
inv=u+c/u
assert s.cancel(inv.subs(u,c/u)-inv)==0
assert s.cancel(inv.subs({u:-1,c:1-q})-(q-2))==0
assert s.cancel(inv.subs({u:r-1,c:1-r*r})+2)==0
P={v:s.Rational(399,200),w:s.Rational(1,200)}
assert s.cancel(V.subs(P)-P[v])==0
assert s.cancel(W.subs(P)-P[w])==0
assert P[v]*P[w]==s.Rational(399,40000)
source=w*w-2*w+q
assert s.discriminant(source,w)==4*(1-q)
assert s.expand(source.subs(q,w*(2-w)))==0
print('PASS actual F is involutory, fixes the literal base point, preserves q=vw and fixes the source')
print('PASS fiber matrix squares to (1-q)I and exchanges all three puncture pairs')
print('PASS u -> (1-q)/u; quotient u+(1-q)/u has deleted values infinity,-2,q-2')
print('PASS source cover w^2-2w+q=0 has discriminant4(1-q), with q*=399/40000')
print('Group conclusions use the actual bundle and full profinite centralizer theorem, not numerical sampling.')
