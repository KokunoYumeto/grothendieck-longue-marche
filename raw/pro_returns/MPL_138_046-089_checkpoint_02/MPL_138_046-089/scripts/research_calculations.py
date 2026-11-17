#!/usr/bin/env python3
"""Post-freeze checks of mathematical interpretations, not transcription edits."""
from pathlib import Path
import datetime
import sympy as s

root = Path(__file__).resolve().parents[1]
x,y,z,t = s.symbols('x y z t')
xp = -x*(x*x-3*y*y)
yp = y*(y*y-3*x*x)
zp = z**3
res = s.factor(xp**2+yp**2+zp**2)
u = s.Rational(1,2)-s.Rational(1,4)*(t+1/t)
param = s.expand((1-t*t)**2+(2*t)**2-(1+t*t)**2)

def reduce_word(word):
    stack=[]
    for c in word:
        if stack and stack[-1] == -c: stack.pop()
        else: stack.append(c)
    return tuple(stack)
def inv(word): return tuple(-c for c in word[::-1])
def mul(*words): return reduce_word(sum((tuple(w) for w in words), ()))
def subst(word, images):
    return mul(*(images[c] if c>0 else inv(images[-c]) for c in word))
def fmt(word): return '1' if not word else ' '.join({1:'a',-1:'a^-1',2:'b',-2:'b^-1'}[c] for c in word)
a,b=(1,),(2,)
c=inv(mul(a,b))
q0=mul(a,b)
q1=b
written=mul(a,q0,c,inv(q0),b)
alternative=mul(a,q1,c,inv(q1),b)
tb=mul(q1,c,inv(q1))
t2b=subst(tb,{1:a,2:tb})
expected=mul(inv(a),b,a)
assert written == (1,-2,-1,2)
assert not alternative
assert t2b == expected
assert param == 0
assert s.rem(s.Poly(res,z),s.Poly(x*x+y*y+z*z,z)).as_expr()==0

stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
out=f'''# Post-freeze mathematical checks

UTC: {stamp}

These checks address interpretations in the notes, never alter a reading, and make no novelty claim.

## Scans 049/051/055: conic calculation

For x'=-x(x²-3y²), y'=y(y²-3x²), z'=z³:

    x'²+y'²+z'² = {res}

The remainder modulo x²+y²+z² is zero. The reduction of the sextic expression therefore uses the conic relation; it is not an identity between the two displayed polynomials on all of affine three-space.

The parametrization (1-t²,2t,1+t²) satisfies x²+y²-z²=0 (checked expression = {param}). Its all-plus expression is 2(1+t²)², so the two conic conventions require a coordinate change.

## Scan 047: rational dihedral map

    u(t) = {s.factor(u)}
    du/dt = {s.factor(s.diff(u,t))}
    u(t)-1 = {s.factor(u-1)}

These show double zero at t=1 and double preimage of 1 at t=-1; simple poles at 0 and infinity. Composing t=x_n^n adds the stated order-n ramification there in characteristic zero (or with the required prime-to-characteristic assumptions).

## Scan 085: conditional free-word check, nu=2

Set lambda0=a, lambda1=b, lambda2=(ab)^-1. Take the displayed q2 first as lambda0 lambda1, which is the frozen first reading of its uncertain initial subscript.

    product of images = {fmt(written)}

This is a nonempty reduced free word, hence disproves the relation for that reading. The same obstruction is flagged by Hua's modernized reading; this check is an independent elementary verification, conditional on the uncertain index.

If instead q2=lambda1:

    product of images = {fmt(alternative)}
    t(a)=a, t(b)={fmt(tb)}
    t²(b)={fmt(t2b)} = a^-1 b a

Thus this alternative repairs the product relation but yields t²=Int(a^-1), not the identity as an actual automorphism. It has order two in the outer group. Relation preservation alone does not establish the manuscript's asserted lift of a Z/2 action to the actual automorphism group.
'''
(root/'research_calculations.md').write_text(out)
print(out)
