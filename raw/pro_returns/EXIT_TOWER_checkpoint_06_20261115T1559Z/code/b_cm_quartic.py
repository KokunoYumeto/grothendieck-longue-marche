"""Exact algebra for the three-division-quartic CM comparison.

This program verifies algebraic identities, not the outstanding profinite
functoriality or the value of the CM character on GT.
"""
from pathlib import Path
import json
import sympy as S

a,b,x,t=S.symbols('a b x t')
D=4*a**3+27*b**2
psi=3*x**4+6*a*x**2+12*b*x-a**2
Q=t**2-psi/3
X=(t+x*x+a)/2
Z=X-a/3
Y=X*x+b/2
curve=S.expand(Y**2-Z**3-D/108)
quotient,remainder=S.div(curve,Q,t)
assert S.expand(remainder)==0
quartic_I=12*3*(-a*a)+(6*a)**2
quartic_J=72*3*(6*a)*(-a*a)-27*3*(12*b)**2-2*(6*a)**3
assert S.expand(quartic_I)==0
assert S.expand(quartic_J+432*D)==0
assert S.expand((-b/2)**2-(-a/3)**3-D/108)==0

# The inverse follows from X=Z+a/3 and Y=Xx+b/2.
z,y=S.symbols('z y')
xi=(y-b/2)/(z+a/3)
ti=2*(z+a/3)-xi**2-a
inverse_expr=S.together(ti**2-psi.subs(x,xi)/3)
num,den=S.fraction(inverse_expr)
iq,ir=S.div(S.expand(num),y*y-z**3-D/108,y)
assert S.expand(ir)==0

# At b=0 the pole difference is a nonzero two-torsion point.
assert (-b/2).subs(b,0)==0
# At a=0 it is a flex: the horizontal tangent meets the cubic triply.
assert S.expand(((-b/2)**2-z**3-D.subs(a,0)/108))==-z**3

# Original Weierstrass scaling (x,a,b,t)->(u²x,u⁴a,u⁶b,u⁴t)
# induces (Z,Y)->(u⁴Z,u⁶Y), which records the CM orientation.
u=S.symbols('u')
sub={x:u**2*x,a:u**4*a,b:u**6*b,t:u**4*t}
assert S.expand(Z.xreplace(sub)-u**4*Z)==0
assert S.expand(Y.xreplace(sub)-u**6*Y)==0

U=S.Matrix([[1,1],[0,1]])
L=S.Matrix([[1,0],[-1,1]])
delta=U*L*U
epsilon=U*U*L*U
assert delta**2==-S.eye(2)
assert epsilon==(U*L)**2
assert epsilon**3==S.eye(2)

data={
  'status':'Executed algebraic certificate; profinite comparison not asserted',
  'division_polynomial':str(psi),
  'binary_quartic_I':str(S.expand(quartic_I)),
  'binary_quartic_J':str(S.expand(quartic_J)),
  'quartic':str(Q)+' = 0',
  'map':{'Z':str(Z),'Y':str(Y)},
  'weierstrass':'Y^2 = Z^3 + (4*a^3+27*b^2)/108',
  'inverse':{'x':str(xi),'t':str(ti)},
  'pole_plus':'origin',
  'pole_minus':{'Z':'-a/3','Y':'-b/2'},
  'quartic_involution':'Q -> P-Q',
  'harmonic_b_zero':'P has order 2; the four branch points satisfy 2Q=P',
  'equianharmonic_a_zero':'P has order 3',
  'scaling':{'Z':'u^4 Z','Y':'u^6 Y'},
  'braid_fold':{'delta4_squared':[[int(e) for e in row] for row in (-S.eye(2)).tolist()],
                'epsilon4':[[int(e) for e in row] for row in epsilon.tolist()],
                'orientation_note':'The explicit CM scaling sends source zeta6 to target zeta3^2; a positive braid dictionary requires checking r versus epsilon4^-1.'}
}
out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
