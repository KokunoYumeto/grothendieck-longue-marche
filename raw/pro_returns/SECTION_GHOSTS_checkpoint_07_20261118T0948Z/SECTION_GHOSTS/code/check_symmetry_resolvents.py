"""Independent exact checks for the typed-map comparison E.55.

This does not compute an unprovided full lift.  It verifies the branch
polynomial, rational markings, and permutation transport used in the proof.
"""
from itertools import permutations
from pathlib import Path
import json
import sympy as s

t = s.symbols('t')
j = t**3 * (t**2 + 5*t + 40)
assert s.expand(j - 1728 - (t-3)*(t*t+4*t+24)**2) == 0
assert s.discriminant(t*t+5*t+40,t) == -135
rp = (-5+3*s.sqrt(-15))/2
rm = (-5-3*s.sqrt(-15))/2
for r in (rp,rm):
    f = 1728*(t-r)/(3-r)
    assert s.simplify(f.subs(t,r)) == 0
    assert s.simplify(f.subs(t,3)) == 1728

def mult(a,b): return tuple(a[b[i]] for i in range(5))
def inv(a): return tuple(a.index(i) for i in range(5))
def power(a,n):
    e=tuple(range(5))
    for _ in range(n): e=mult(e,a)
    return e
def sign(a): return (-1)**sum(a[i]>a[k] for i in range(5) for k in range(i+1,5))
def conj(g,h): return mult(mult(g,h),inv(g))
three=(1,2,0,3,4)
five=(1,2,3,4,0)
normal3=[]
normal5=[]
for g in permutations(range(5)):
    for a in (1,2):
        if conj(g,three)==power(three,a):
            support_sign=1 if a==1 else -1
            fixed_sign=1 if g[3]==3 else -1
            assert sign(g)==support_sign*fixed_sign
            normal3.append((g,a))
    for a in (1,2,3,4):
        if conj(g,five)==power(five,a):
            assert sign(g)==(1 if a in (1,4) else -1)
            normal5.append((g,a))
assert len(normal3)==12 and len(normal5)==20
assert all(g[3:]==(3,4) for g in permutations(range(5)) if sign(g)==1 and conj(g,three)==three)
z=s.symbols('z')
cover=z**3/(z**3-1)
assert cover.subs(z,2)==s.Rational(8,7)
assert s.simplify(cover-1)==1/(z**3-1)
out={'quintic_identity':True,'quadratic_discriminant':-135,
     'geometric_affine_markings':True,'normalizer_three_size':len(normal3),
     'normalizer_five_size':len(normal5),'fixed_letter_transport':True,
     'root_stack_cover_degree':3,'rational_base_point':'z=2, t=8/7','all_checks':'PASS'}
path=Path(__file__).with_suffix('.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
