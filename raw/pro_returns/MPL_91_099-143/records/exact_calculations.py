"""Exact checks of the finite examples in the research notes; no scan processing."""
from pathlib import Path
from datetime import datetime, timezone
import sympy as s

root = Path(__file__).resolve().parents[1]
t, e = s.symbols("t epsilon")
a0, a1, a2, b0, b1, b2 = s.symbols("a0 a1 a2 a0prime a1prime a2prime")
f = a0 + a1*t + a2*t**2
composite = s.Poly(s.expand(b0+b1*f+b2*f**2), t)
coeffs = [b0+b1*a0+b2*a0**2, b1*a1+2*b2*a0*a1,
          b1*a2+b2*(a1**2+2*a0*a2), 2*b2*a1*a2, b2*a2**2]
assert all(s.expand(composite.nth(i)-v)==0 for i,v in enumerate(coeffs))

# Reduction modulo epsilon^2 in Q(t)[epsilon].
product = s.expand((1+e/t)*(1-e/t))
laurent_product = s.rem(product,e**2,e)
assert laurent_product == 1

# Quotient Q[epsilon,t]/(epsilon^3,t^3), via its monomial basis.
translated = s.Poly(s.expand((t+e)**3),e,t)
remainder = sum(c*e**i*t**j for (i,j),c in translated.terms() if i<3 and j<3)
assert s.expand(remainder-(3*e*t**2+3*e**2*t))==0
assert remainder != 0

a,b,c,d=s.symbols("a b c d")
A=s.Matrix([[0,1],[-1,0]])
X=s.Matrix([[a,b],[c,d]])
matrix=X.T*A+A*X
assert matrix==(a+d)*A
basis=[s.Matrix([[1,0],[0,-1]]),s.Matrix([[0,1],[0,0]]),s.Matrix([[0,0],[1,0]])]
assert all(B.T*A+A*B==s.zeros(2) for B in basis)
assert X.subs(d,-a)==a*basis[0]+b*basis[1]+c*basis[2]

x1,x2,y1,y2=s.symbols("X1 X2 Y1 Y2")
second=s.Poly((x2+y2*(1+x1**2))-(y2+x2*(1+y1**2)),
              x1,x2,y1,y2,modulus=2)
assert second==s.Poly(x1**2*y2+y1**2*x2,x1,x2,y1,y2,modulus=2)
assert not second.is_zero
quadratic=sum(coef*s.prod(v**k for v,k in zip((x1,x2,y1,y2),powers))
              for powers,coef in second.terms() if sum(powers)<3)
assert quadratic==0
first=s.expand((x1+y1+x1*y1)-(y1+x1+y1*x1))
assert first==0

lines=[
    "# Exact calculation checks",
    "",
    "Checked "+datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")+
    "; exact symbolic arithmetic with SymPy "+s.__version__+".",
    "",
    "These checks concern the explicit examples in the research notes. They do not alter or complete the frozen transcription.",
    "",
    "1. RN142-02: quadratic substitution coefficients, degrees 0 through 4: "+
      "; ".join(str(s.expand(v)) for v in coeffs)+". PASS.",
    "2. RN135-03: (1+epsilon/t)(1-epsilon/t) reduced modulo epsilon^2 is 1. PASS.",
    "3. RN142-04: (t+epsilon)^3 modulo (epsilon^3,t^3) is "+
      str(s.expand(remainder))+", a nonzero basis expression. PASS.",
    "4. RN139-03: transpose(X) A + A X = (a+d) A; the three displayed kernel basis matrices vanish under this map and parametrize X with d=-a. PASS.",
    "5. RN139-02: in characteristic 2, the second-coordinate difference is "+
      str(second.as_expr())+"; it is nonzero and has zero image modulo total degree >=3. The first-coordinate difference is zero. PASS.",
    "",
    "Direct proof checks recorded in the notes: RN135-02 gives the equality-stage map and its identical inverse; RN142-03 uses the coefficient equation 2 h_1 = 1 in Z. No floating-point or statistical calculation is used.",
]
(root/"records/exact_calculations.md").write_text("\n".join(lines)+"\n")
print("Five exact calculation checks passed.")
