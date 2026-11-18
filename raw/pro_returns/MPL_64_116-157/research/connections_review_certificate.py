#!/usr/bin/env python3
"""Independent narrow review of connections_hua.md S03--S05.
No manuscript inputs. Uses a closed p-curvature expansion rather than C2's recurrence.
"""
import sympy as s
x,u=s.symbols('x u')
q=x*(x-1)*(x-u)
R=x*(x-1)/(2*(x-u))
derivative=lambda V:s.diff(V,x)-V*s.diff(q,x)/(2*q)
lhs=3*u*(1-u)/(4*(x-u)**2)+(1-2*u)/(2*(x-u))-s.Rational(1,4)
assert s.cancel(lhs-derivative(R))==0
P=(1-2*u)/(u*(1-u)); Q=-1/(4*u*(1-u))
schwarz=s.cancel(2*Q-s.diff(P,u)-P**2/2)
assert s.cancel(schwarz-(u**2-u+1)/(2*u**2*(u-1)**2))==0
print('S03 PASS: exact-differential sign and Schwarzian.')

# Independent de Rham basis reduction and gauge calculation.
alpha=-1/(2*(u-1)); beta=1/(2*u*(u-1))
assert s.cancel(1/(2*(x-u))-(alpha+beta*x)+derivative(x*(x-1))/(u*(u-1)))==0
G=s.Matrix([[alpha,alpha],[beta,1/(2*(u-1))]])
H=s.Matrix([[1,alpha],[0,beta]])
A=s.Matrix([[0,1],[1/(4*u*(1-u)),-P]])
assert (H.inv()*(G*H+H.diff(u))-A.T).applyfunc(s.cancel)==s.zeros(2)
print('S05 PASS: de Rham basis (omega, nabla omega) has coefficient connection d+A^T; dual companion d-A.')

# (d-A)^3 constant term: -A''+A'A+2AA'-A^3.
# Terms in d and d^2 have coefficients divisible by 3.
def red(f):
    # Explicit coefficient reduction is also required after specialization:
    # cancel(constant, modulus=3) alone leaves integer constants unchanged.
    numerator,denominator=s.fraction(s.cancel(f))
    numerator=s.Poly(numerator,u,modulus=3).as_expr()
    denominator=s.Poly(denominator,u,modulus=3).as_expr()
    assert denominator!=0
    return s.cancel(numerator/denominator,modulus=3)
def closed_curvature(M):
    return (-M.diff(u,2)+M.diff(u)*M+2*M*M.diff(u)-M**3).applyfunc(red)
psi=closed_curvature(A)
expected=s.Matrix([[-u-1,(u+1)**2],[-1,u+1]])/(u**2*(u-1)**2)
assert (psi-expected).applyfunc(red)==s.zeros(2)
assert (psi*psi).applyfunc(red)==s.zeros(2)
psi_dr=closed_curvature(-A.T)
assert (psi_dr+psi.T).applyfunc(red)==s.zeros(2)
special=psi.subs(u,-1).applyfunc(red)
special_dr=psi_dr.subs(u,-1).applyfunc(red)
assert special==s.Matrix([[0,0],[-1,0]])
assert special_dr==s.Matrix([[0,1],[0,0]])
h=s.Poly(q,x).coeff_monomial(x**2)
assert s.expand(h+1+u)==0
assert h.subs(u,-1)==0
v=s.Matrix([u+1,1])
assert (v.diff(u)-A*v).applyfunc(red)==s.zeros(2,1)
print('S05 PASS: independent closed expansion agrees with recurrence matrix.')
print('Companion specialization at u=-1:',special)
print('De Rham specialization at u=-1:',special_dr)
print('Hasse coefficient:',h,'; horizontal companion vector:',v.T)
print('PASS: nonzero, rank-one, square-zero at the supersingular parameter.')
print('This is the value of the base-connection p-curvature tensor, not a connection on an isolated fibre.')
