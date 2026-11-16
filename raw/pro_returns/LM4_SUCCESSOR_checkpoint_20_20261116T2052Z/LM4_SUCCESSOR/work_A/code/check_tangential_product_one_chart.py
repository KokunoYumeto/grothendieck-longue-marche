"""Exact rational chart/source identities; no finite-group census."""
import sympy as s
t,q=s.symbols('t q')
w=1+t
v=(1+q*t*t)/(1+t)
W=s.cancel((w**5-1)/t)
V=s.cancel(((1+q*t*t)**5-(1+t)**5)/t)
D=-2+(q-1)*t
P=s.cancel(((1+q*t*t)**5-1)/(q*t*t))
for f in (W,V,D,P):
    assert s.denom(f)==1
assert s.cancel(w**5-1-t*W)==0
assert s.cancel(v**5-1-t*V/(1+t)**5)==0
assert s.cancel(v-w-t*D/(1+t))==0
assert s.cancel((v*w)**5-1-q*t*t*P)==0
assert s.cancel(v*w-1-q*t*t)==0
assert s.cancel(v-1-t*(q*t-1)/(1+t))==0
F=s.expand((1+t)*(1+q*t*t)*W*V*D*P)
assert F.subs(t,0)==250
assert s.cancel(v.subs(q,-1)-(1-t))==0
assert s.cancel((v+w-2)-t*t*(q+1)/(1+t))==0
print('PASS all exact deleted-boundary factor identities')
print('PASS F(0,q)=250: the exceptional open section is all Gm_q')
print('PASS actual source is exactly q=-1; v=1-t and w=1+t')
print('PASS strict v=1 is qt=1; strict diagonal is qt=2+t; product1 is q=0')
print('Scope: rational chart identities only; actual based q-loop has separate DE certificate')
