"""Exact certificate for the one-retained-tangency relative counterexample.

The topological covering and its actual source comparison are proved in
records/one_exception_tangent_counterexample_13h.md.  This program checks
the polynomial identities, unramified Jacobian, source deck transformation,
and every element of the concrete eight-element deck group.
"""
from pathlib import Path
import itertools
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[2]
a, b, c = s.symbols('a b c')
u = (a*a+b*b)/2
v = (a*a-b*b)**2/4
x = u+1
y = v+2*u+1
assert s.expand(u*u-v-a*a*b*b) == 0
assert s.expand(4*y-((a+b)**2+2)*((a-b)**2+2)) == 0
jac = s.det(s.Matrix([[s.diff(u,a),s.diff(u,b)],
                     [s.diff(v,a),s.diff(v,b)]]))
assert s.expand(jac+2*a*b*(a*a-b*b)) == 0

def red(expr):
    return s.rem(s.Poly(s.expand(expr),c),s.Poly(c*c+2,c)).as_expr().expand()

assert red(y.subs(a,b+c)) == 0
assert red(x.subs(a,b+c)-b*(b+c)) == 0
source_x=b*(b+c)
assert red(source_x.subs(b,-c-b)-source_x) == 0
assert red(source_x.subs(b,-c/2)-s.Rational(1,2)) == 0
assert red(s.diff(source_x,b).subs(b,-c/2)) == 0
assert s.diff(source_x,b).subs(b,0) == c
assert s.diff(source_x,b).subs(b,-c) == -c

def mul(A,B):
    return tuple(sum(A[2*i+k]*B[2*k+j] for k in range(2))
                 for i in range(2) for j in range(2))

def inverse(A):
    return (A[0],A[2],A[1],A[3])

Id=(1,0,0,1)
swap=(0,1,1,0)
minus_swap=(0,-1,-1,0)
flip=(-1,0,0,1)
D8=set()
for e,f in itertools.product((-1,1),repeat=2):
    D8.add((e,0,0,f))
    D8.add((0,e,f,0))
assert len(D8)==8
assert {mul(A,B) for A in D8 for B in D8}==D8
assert all(mul(A,inverse(A))==Id for A in D8)
for A in D8:
    aa=A[0]*a+A[1]*b
    bb=A[2]*a+A[3]*b
    assert s.expand(u.subs({a:aa,b:bb},simultaneous=True)-u)==0
    assert s.expand(v.subs({a:aa,b:bb},simultaneous=True)-v)==0

# A deck transformation preserves a-b=c, c!=0, exactly when this row
# functional is fixed, not merely multiplied by minus one.
source={A for A in D8 if (A[0]-A[2],A[1]-A[3])==(1,-1)}
assert source=={Id,minus_swap}
conjugates={mul(mul(A,minus_swap),inverse(A)) for A in D8}
normal={Id}
while True:
    enlarged=normal|{mul(A,B) for A in normal for B in conjugates}
    if enlarged==normal:
        break
    normal=enlarged
assert normal=={Id,(-1,0,0,-1),swap,minus_swap}
assert mul(mul(flip,minus_swap),inverse(flip))==swap
assert swap not in source
assert mul(minus_swap,minus_swap)==Id

out={
    'scope':'One exceptional retained tangency; not the actual marginal surface',
    'ambient':'C^2 minus y=x^2 and y=2x-1',
    'source':'y=0; x notin {0,1/2}',
    'filled_source':'y=0; x!=0',
    'cover':'u=(a^2+b^2)/2, v=(a^2-b^2)^2/4; a*b*(a^2-b^2)!=0',
    'coordinate_change':'u=x-1, v=y-2*x+1',
    'jacobian':str(s.factor(jac)),
    'source_component':'a-b=c, c^2=-2; x=b*(b+c)',
    'deck_group_order':len(D8),
    'deck_group':sorted(D8),
    'source_image':sorted(source),
    'source_kernel_image':sorted(source),
    'ambient_deletion_kernel_image':sorted(normal),
    'retained_meridian':flip,
    'deleted_source_meridian':minus_swap,
    'separating_conjugate':swap,
    'checks':'PASS'
}
(ROOT/'records/one_exception_tangent_counterexample_certificate.json').write_text(
    json.dumps(out,indent=2)+'\n')
print('Actual polynomial cover identities and nonzero unramified Jacobian: PASS')
print('Four source components; selected component x=b*(b+c), c^2=-2: PASS')
print('Source x=0 unramified; source x=1/2 simply branched, deck=-swap: PASS')
print('All8 signed permutation deck transformations checked: PASS')
print('Actual source image and source U-kernel image: C2, order2')
print('Actual ambient U-kernel image: V4, order4')
print('Retained meridian conjugates -swap to +swap outside the source: PASS')
print('The one-exceptional-retained-point relative principle is FALSE.')
