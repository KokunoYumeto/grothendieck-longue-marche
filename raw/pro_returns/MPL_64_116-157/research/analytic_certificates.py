#!/usr/bin/env python3
"""Exact checks of formulas in the frozen cote64 transcription.

No image reading or OCR; no changes to the transcription. The free-word
calculation proves identities in F(x,y), not a theorem about profinite GT.
Run: python3 research/analytic_certificates.py
"""
import itertools
import json
import sympy as s

x, y = s.symbols('x y', real=True, nonzero=True)
a, b, c, d, A, B, C, D, t, m, n = s.symbols('a b c d A B C D t m n')
g, h = s.Matrix([[a,b],[c,d]]), s.Matrix([[A,B],[C,D]])
I = s.eye(2)
swap = s.Matrix([[0,1],[1,0]])
delta = s.diag(1,-1)
J = s.Matrix([[-x/y,(x*x+y*y)/y],[-1/y,x/y]])
assert s.simplify(J*J + I) == s.zeros(2)
orientation = s.det(s.Matrix.hstack(s.Matrix([1,0]), J*s.Matrix([1,0])))
assert orientation == -1/y

def mob(k,z):
    return (k[0,0]*z+k[0,1])/(k[1,0]*z+k[1,1])

def j(k,z):
    return k[1,0]*z+k[1,1]

def sigma(k):
    return delta*k.adjugate()*delta

assert sigma(g*h) == sigma(h)*sigma(g)
assert s.simplify(mob(g,mob(h,t))-mob(g*h,t)) == 0
assert s.simplify(j(g,mob(h,t))*j(h,t)-j(g*h,t)) == 0
rho = delta*g*delta
assert delta*(g*h)*delta == (delta*g*delta)*(delta*h*delta)
mp, np = rho*s.Matrix([m,n])
translation_residual = s.factor((mp+np*mob(g,t))*j(g,t)-(m+n*t))
assert s.factor(translation_residual-(a*d-b*c-1)*(m+n*t)) == 0
R = lambda k: swap*k*swap
assert R(g*h) == R(g)*R(h)
assert R(-I) == -I

invchar = {'x':'X','X':'x','y':'Y','Y':'y'}
def reduce(w):
    r=[]
    for q in w:
        if r and invchar[q] == r[-1]:
            r.pop()
        else:
            r.append(q)
    return ''.join(r)

def inverse(w):
    return ''.join(invchar[q] for q in w[::-1])

def apply(f,w):
    images = {**f, 'X':inverse(f['x']), 'Y':inverse(f['y'])}
    return reduce(''.join(images[q] for q in w))

def compose(f,k):
    return {q:apply(f,k[q]) for q in ('x','y')}

def power(f,r):
    z={'x':'x','y':'y'}
    for _ in range(r): z=compose(f,z)
    return z

identity={'x':'x','y':'y'}
S={'x':'y','y':'X'}
T={'x':'x','y':'xy'}
Ti={'x':'x','y':'Xy'}
assert compose(T,Ti)==compose(Ti,T)==identity
assert power(S,4)==identity
comm='xyXY'
assert apply(T,comm)==reduce('x'+comm+'X')
assert apply(S,comm)==reduce('X'+comm+'x')
ST3 = power(compose(S,T),3)
S2 = power(S,2)
# The two sides of the SL2(Z) relation differ by this inner automorphism.
conjugator=None
for length in range(8):
    for letters in itertools.product('xXyY', repeat=length):
        w=''.join(letters)
        if reduce(w)!=w: continue
        if all(ST3[q]==reduce(w+S2[q]+inverse(w)) for q in ('x','y')):
            conjugator=w
            break
    if conjugator is not None: break
assert conjugator is not None

def abelianize(w):
    return [w.count('x')-w.count('X'),w.count('y')-w.count('Y')]
Sm=s.Matrix.hstack(*[s.Matrix(abelianize(S[q])) for q in ('x','y')])
Tm=s.Matrix.hstack(*[s.Matrix(abelianize(T[q])) for q in ('x','y')])
assert Sm==s.Matrix([[0,-1],[1,0]])
assert Tm==s.Matrix([[1,1],[0,1]])
assert Sm**2==(Sm*Tm)**3==-I

report = {
    'sympy_version':s.__version__,
    'arithmetic':'exact rational functions and reduced free words',
    'complex_structure_J':str(J),
    'J_squared':'-I (exact)',
    'orientation_determinant':str(orientation),
    'sigma_anti_homomorphism':'exact for all 2x2 matrices using adjugate; on SL2 this is delta*g^-1*delta',
    'mobius_and_automorphy_cocycle':'exact',
    'translation_rho':str(rho),
    'translation_residual_before_det1':str(translation_residual),
    'period_action_R':str(R(g)),
    'period_action_R_homomorphism':'exact',
    'S_images':S,
    'T_images':T,
    'S_boundary_image':apply(S,comm),
    'T_boundary_image':apply(T,comm),
    'S_fourth':'identity exactly',
    'ST_cubed':ST3,
    'S_squared':S2,
    'ST_cubed_equals_inner_w_times_S_squared':conjugator,
    'S_abelianization':str(Sm),
    'T_abelianization':str(Tm),
    'scope_limit':'Does not prove Nielsen injectivity, uniformization, any profinite congruence statement, or GT arithmeticity.'
}
print(json.dumps(report,ensure_ascii=False,indent=2))
