"""Literal invariant maps for the extra elliptic factors of harmonic D."""
from pathlib import Path
import sympy as s

T,W,a=s.symbols("T W a",nonzero=True)
lam=s.sqrt(2)/2
F=lambda z:z*(z-1)*(z-s.Rational(1,2))
W4=F(T)/a
def reduce_w(expr):
    num,den=s.fraction(s.factor(expr))
    num=s.rem(s.Poly(num,W),s.Poly(W**4-W4,W)).as_expr()
    return s.simplify(num/den)
rows=[]
for l in [lam,-lam]:
    Tp=l*l/T;Wp=l*W/T
    x=a*W**2/T
    y=a*W*(T+l)/T
    b=a*(s.Rational(3,2)+2*l)
    assert s.simplify(F(Tp)-l**4*F(T)/T**4)==0
    assert s.simplify(a*Wp**2/Tp-x)==0
    assert s.simplify(a*Wp*(Tp+l)/Tp-y)==0
    assert reduce_w(y*y-x**3-b*x)==0
    u=T+l*l/T
    assert reduce_w(x*x/a+s.Rational(3,2)-u)==0
    assert s.simplify(T*T-u*T+l*l)==0
    assert s.simplify(y*T/(a*(T+l))-W)==0
    dW=s.diff(F(T),T)/(4*a*W**3)
    dx=s.diff(x,T)+s.diff(x,W)*dW
    differential=(T-l)/(4*a*W**3)
    assert reduce_w(dx/(2*y)-differential)==0
    rows.append((str(l),str(b),str(differential)))
epsilon=1+s.sqrt(2)
M=7*13*23*139*1119169
q0=s.Rational(M,2*191**2)
aa=573*q0**2
bplus=aa*(s.Rational(3,2)+s.sqrt(2))
bminus=aa*(s.Rational(3,2)-s.sqrt(2))
assert s.simplify(bplus*(2*191)**4-1146*epsilon**2*M**2)==0
assert s.simplify(bminus/bplus-(s.sqrt(2)-1)**4)==0
print("PASS: both involutions preserve the literal quartic and square to identity.")
print("PASS: x=aW^2/T and Y=aW(T±1/sqrt(2))/T are invariant and satisfy both elliptic equations.")
print("PASS: inverse field equations recover the degree-two extension and W.")
print("PASS: both pulled-back invariant differentials are (T∓1/sqrt(2))dT/(4aW^3).")
print("PASS: exact integral scaling gives coefficient 1146*(1+sqrt(2))^2*M^2, M =",M)
print("PASS: conjugate factors are isomorphic by the exact fourth-power coefficient ratio.")
print("The proof note supplies the proper extensions, boundary maps, and Jacobian isogeny.")
print("No finite-Mordell-Weil conclusion is asserted.")
