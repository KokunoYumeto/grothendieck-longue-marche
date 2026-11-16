"""Independent exact field and valuation check for A.170's anti-unit source.

This reads no candidate data and uses Q[p]/(p^6+3).  It verifies the
literal identities used in the proof; it does not compute a class group.
"""
import json
from pathlib import Path
import sympy as sp

p = sp.Symbol('p')
f = p**6 + 3
def red(x):
    a,b = sp.fraction(sp.cancel(x))
    return sp.rem(a * sp.invert(b,f),f,p).expand()
def inv(x):
    return sp.invert(red(x),f,p)
def val3(q):
    q=sp.Rational(q)
    if not q: return 10**9
    a,b=abs(int(q.p)),int(q.q)
    z=0
    while a%3==0: a//=3; z+=1
    while b%3==0: b//=3; z-=1
    return z
def depth(x):
    z=sp.Poly(red(x),p)
    return min(6*val3(c)+i[0] for i,c in z.terms())
zeta=-(1+p**3)/2
alpha=(p**2+p**5)/2
taup=(p+p**4)/2
def tau(x): return red(red(x).subs(p,taup))
assert red(alpha**3)==3
assert red(zeta**2+zeta+1)==0
assert tau(alpha)==alpha
assert tau(zeta)==red(zeta**2)
assert tau(taup)==p
v=red((1+p)*inv(1+p**2))
epsilon=red(v*inv(tau(v)))
U=red(alpha**2-2)
assert red(v*tau(v))==U
assert red(epsilon*tau(epsilon))==1
assert sp.resultant(f,1+p,p)==4
assert sp.resultant(f,1+p**2,p)==4
u11=red((2+zeta*alpha)*inv(2+zeta**2*alpha))
u59=red((2+2*zeta*alpha-zeta**2*alpha**2)*inv(2+2*zeta**2*alpha-zeta*alpha**2))
u=red(u11*u59)
assert u==red((1+6*zeta*alpha)*inv(1+6*zeta**2*alpha))
b=1+p-p**2
assert red(zeta-b**3)==-sp.Rational(9,2)-3*p+sp.Rational(9,2)*p**3-3*p**5
depths={
    'epsilon':depth(epsilon-1),
    'u11':depth(u11-1),
    'u59':depth(u59-1),
    'product':depth(u-1),
    'improved_zeta':depth(red(zeta*inv(b**3))-1),
}
assert depths=={'epsilon':1,'u11':5,'u59':5,'product':11,'improved_zeta':7}
assert depth((u-1)/3)==5
assert depth(red(3*((u-1)/3)**2+((u-1)/3)**3))==15
data={'identities':'PASS','depths':depths,'unit_numerator_norm':4,'unit_denominator_norm':4}
out=Path(__file__).with_name('two_inert_anti_unit_independent_audit_data.json')
out.write_text(json.dumps(data,indent=2)+'\n')
print('PASS: literal degree-six involution, alpha/zeta maps, global unit norm and anti-unit norm')
print('PASS: both exact rational norms equal 4; common support is proved by the printed residue table')
print('PASS: exact local depths',depths,'and Hensel residual depth 15')
print('This certificate does not infer class-group completeness or balanced-class detection.')
