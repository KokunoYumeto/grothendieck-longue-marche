#!/usr/bin/env python3
"""Exact algebraic certificates for research notes A01--A09 and L90--L92.

Requires SymPy. Reads no manuscript/context files and changes no files.
These polynomial checks support, but do not replace, the commutative-algebra
proofs in arithmetic_evidence.md. Assertions are over Q, Z, or F_2 as stated.
"""
import itertools
import sympy as s


def zero(expression):
    assert s.cancel(expression) == 0, expression


def emit(label, value):
    print(f'{label}: {value}')


r, u, v, z = s.symbols('r u v z')
a1 = -(r+u+v)
a2 = r*u+r*v+u*v
a3 = -r*u*v
f = z**3+a1*z**2+a2*z+a3
radical = (r-u)*(r-v)
b = u*v-r*(u+v)
zero(f-(z-r)*(z-u)*(z-v))
zero(s.diff(f,z).subs(z,r)-radical)
zero(-(a1*r**2+2*a2*r+3*a3)/r-radical)
zero(r**2-a2+2*u*v-radical)
bad_radical = -(a1*r+2*a2+3*u*v)
zero(bad_radical-radical+6*u*v)
bad_fixed_rhs = 2*r*z-(a2+2*u*v)
correct_fixed_rhs = 2*r*z-a2+2*u*v
zero(bad_fixed_rhs-correct_fixed_rhs+4*u*v)
M=s.Matrix([[r,b],[1,-r]])
assert (M*M-radical*s.eye(2)).applyfunc(s.expand) == s.zeros(2)
emit('L90 radical identity', s.factor(radical))
emit('L90 bracket error (literal minus correct)', s.factor(bad_radical-radical))
emit('L90 marginal constant error (literal minus correct)', s.factor(bad_fixed_rhs-correct_fixed_rhs))
for point in [{r:1,u:2,v:3},{r:0,u:1,v:2}]:
    emit(f'L90/L91 example {point}', {'correct':radical.subs(point),'literal bracket':bad_radical.subs(point)})
zero(radical.subs(r,0)-u*v)
emit('L91 zero-root extension', 'radical = u*v; involution z -> u*v/z')

# Scan 117/118 determinant and scan 123/125/126 basis formulas.
z1,z2,z3,w1,w2,w3=s.symbols('z1 z2 z3 w1 w2 w3')
det=s.Matrix([[1,z1,w1],[1,z2,w2],[1,z3,w3]]).det()
zero(det-((z2*w3-z3*w2)+(z3*w1-z1*w3)+(z1*w2-z2*w1)))
D=(r-u)*(u-v)*(v-r)
f1=s.Matrix([u-v,v-r,r-u])/D
f2=-s.Matrix([r*(u-v),u*(v-r),v*(r-u)])/D
e=s.eye(3)
roots=[r,u,v]
for i,j,k in [(0,1,2),(1,2,0),(2,0,1)]:
    difference=roots[i]*f1+f2-(e[:,j]-e[:,k])/(roots[j]-roots[k])
    for entry in difference: zero(entry)
zero(sum(f1));zero(sum(f2))
kernel_vector=s.Matrix([u-v,v-r,r-u])
assert (s.Matrix([[1,1,1],[r,u,v]])*kernel_vector).applyfunc(s.expand)==s.zeros(2,1)
emit('L92 basis and kernel identities','all exact rational identities passed; D != 0 required')

# Quadratic orders, discriminants, and the integral generator.
S,R,H,U,T,X,m,P=s.symbols('S R H U T X m P')
normal_equation=U**2-R*U-H
zero((2*U-R)**2-(R**2+4*H)-4*normal_equation)
zero(s.discriminant(normal_equation,U)-(R**2+4*H))
zero((2*S)**2-4*P-4*(S**2-P))
emit('A06 normalization identity','(2U-R)^2-(R^2+4H)=4(U^2-RU-H)')
affine_equation=U**2-T*U+m*T
zero((2*U-T)**2-(T**2-4*m*T)-4*affine_equation)
infinity_equation=U**2-U+m*X
zero((2*U-1)**2-(1-4*m*X)-4*infinity_equation)
zero(s.discriminant(infinity_equation,U)-(1-4*m*X))
zero(affine_equation.subs(U,T*U)/T**2-infinity_equation.subs(X,1/T))
emit('A08 affine/projective models','U_aff^2-T*U_aff+m*T and u^2-u+m*x; x=1/T, U_aff=T*u')
emit('A08 corrected discriminant',1-4*m*X)
assert s.Poly(s.diff(infinity_equation,U),U,X,m,modulus=2).as_expr()==1
bad_special=s.Poly(S**2+1,S,modulus=2)
assert bad_special==s.Poly((S+1)**2,S,modulus=2)
emit('A08 literal opposite-sign special fibre','S^2+1=(S+1)^2 over F_2 at x=0; not etale')

# Modulo-four certificate. Any square root has prescribed reduction mod two;
# replacing a lift R by R+2H does not change its square modulo four.
zero((R+2*H)**2-R**2-4*(R*H+H**2))
possibilities=[]
for sign in [1,-1]:
    for lam in range(4):
        witnesses=[]
        for c0,c1 in itertools.product(range(4),repeat=2):
            candidate=(c0+c1*T)**2-sign*T*(T-lam)
            if all(int(c)%4==0 for c in s.Poly(candidate,T).all_coeffs()):
                witnesses.append((c0,c1))
        if witnesses: possibilities.append((sign,lam,witnesses))
assert [(a,b) for a,b,_ in possibilities]==[(1,0)]
emit('A07 square modulo-four cases (sign, lambda mod4, lifts)',possibilities)
assert s.Poly(T*(T-2)-T**2,T,modulus=2).is_zero
assert any(int(c)%4 for c in s.Poly(T*(T-2)-T**2,T).all_coeffs())
emit('A07 modulo-two counterexample','lambda=2 gives T(T-2)=T^2 mod2, but 4 does not divide lambda')
assert {n*n%4 for n in range(4)}=={0,1}
emit('A05 signed-radicand warning','Q=1 is square mod4 but P=3 or P=-1 is not')

# Tangent cones. In the ramified mixed-characteristic DVR with pi^2=2,
# a=5 and alpha=1 give T^2+pi^2*T-pi^4.
pi,c,w=s.symbols('pi c w')
ramified_polynomial=s.Poly(T**2+pi**2*T-pi**4,T,pi,modulus=2)
degree=min(sum(monomial) for monomial,coefficient in ramified_polynomial.terms())
tangent=sum(coefficient*T**monomial[0]*pi**monomial[1]
            for monomial,coefficient in ramified_polynomial.terms()
            if sum(monomial)==degree)
assert tangent==T**2
unramified_tangent=T**2+pi*T+c*pi**2
assert s.Poly(s.diff(unramified_tangent,T),T,pi,c,modulus=2).as_expr()==pi
assert s.Poly(s.diff(unramified_tangent,pi),T,pi,c,modulus=2).as_expr()==T
assert s.Poly((T**2+pi**3).subs({T:w**3,pi:w**2}),w,modulus=2).is_zero
emit('A03 ramified tangent cone',tangent)
emit('A03 unramified tangent polar derivatives','d/dT = pi; d/dpi = T over F_2')
emit('A03 equal-characteristic cusp parametrization','pi=w^2, T=w^3 gives T^2+pi^3=0 over F_2')
emit('SymPy version',s.__version__)
emit('RESULT','PASS; polynomial certificates only, not a formal proof of normality/completion statements')
