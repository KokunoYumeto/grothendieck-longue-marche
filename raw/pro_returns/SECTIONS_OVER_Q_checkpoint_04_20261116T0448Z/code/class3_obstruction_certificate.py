"""Exact truncated Magnus check for the actual class-three Galois action.

The calculation is over Q[A,B,H,A1,B1,H1,L,F] with noncommuting
Magnus variables X,Y, truncated after degree three.  It checks integral
group words; displayed binomial coefficients extend to profinite
exponents.  This is a symbolic certificate, not a finite-level substitute
for any continuous-cohomology assertion.
"""
from collections import defaultdict
import sympy as s

A, B, H, A1, B1, H1, L, F = s.symbols("A B H A1 B1 H1 L F")


def clean(p):
    return {w: s.expand(c) for w, c in p.items() if s.expand(c) != 0}


def add(*polys):
    out = defaultdict(lambda: s.Integer(0))
    for p in polys:
        for w, c in p.items():
            out[w] += c
    return clean(out)


def scale(p, a):
    return clean({w: a * c for w, c in p.items()})


def mul(*polys):
    out = {(): s.Integer(1)}
    for p in polys:
        nxt = defaultdict(lambda: s.Integer(0))
        for w, c in out.items():
            for v, d in p.items():
                if len(w) + len(v) <= 3:
                    nxt[w + v] += c * d
        out = clean(nxt)
    return out


one = {(): s.Integer(1)}


def power(p, n):
    n = s.sympify(n)
    u = add(p, scale(one, -1))
    return add(one, scale(u, n), scale(mul(u, u), n*(n-1)/2),
               scale(mul(u, u, u), n*(n-1)*(n-2)/6))


def comm(p, q):
    return mul(p, q, power(p, -1), power(q, -1))


x = {(): s.Integer(1), ("X",): s.Integer(1)}
y = {(): s.Integer(1), ("Y",): s.Integer(1)}
c = comm(x, y)
d = comm(c, x)
e = comm(c, y)


def section(a, b, h):
    return mul(power(y, b), power(x, a), power(c, h))


gx = power(x, L)
gy = mul(power(c, -F), power(y, L), power(c, F))
gc = comm(gx, gy)
assert gy == mul(power(y, L), power(e, -L*F))
assert gc == mul(power(c, L**2), power(d, -L**2*(L-1)/2),
                power(e, -L**2*(L-1)/2))
assert comm(gc, gx) == power(d, L**3)
assert comm(gc, gy) == power(e, L**3)
gw1 = mul(power(gy, B1), power(gx, A1), power(gc, H1))
A01, B01, H01 = A + L*A1, B + L*B1, H + L**2*H1 + A*L*B1
defect = mul(section(A, B, H), gw1, power(section(A01, B01, H01), -1))
assert all(len(w) == 3 or w == () for w in defect)
raw_x = -defect.get(("X", "X", "Y"), 0)
raw_y = defect.get(("X", "Y", "Y"), 0)
assert defect == mul(power(d, raw_x), power(e, raw_y))

epsilon = (L-1)/2
wick_x = -(A+epsilon)*L**2*H1 - A*(A-1)/2*L*B1
wick_y = (B+epsilon)*L**2*(A1*B1-H1) + B*(B-1)/2*L*A1 - F*L*B1


def differential(p):
    return s.expand(p + L**3*p.subs({A:A1, B:B1, H:H1}, simultaneous=True)
                    - p.subs({A:A01, B:B01, H:H01}, simultaneous=True))


assert s.expand(raw_x - wick_x + differential(H*A)) == 0
print("Raw x obstruction = Wickelgren x representative - delta(H*A).")
assert s.expand(raw_y - wick_y - differential(A*B*(B-1)/2-B*H)) == 0
print("Raw y obstruction = Wickelgren y representative + delta(A*binom(B,2)-B*H).")
print("Raw y minus Wickelgren y:", s.factor(raw_y - wick_y))

monomials = [A**3, A**2*B, A*B**2, B**3, A*H, B*H,
             A**2, A*B, B**2, H, A, B, s.Integer(1)]
coeffs = s.symbols("z0:" + str(len(monomials)))
candidate = sum(z*m for z,m in zip(coeffs, monomials))
equation = s.Poly(s.expand(raw_y - wick_y - differential(candidate)),
                  A,B,H,A1,B1,H1,L,F)
solution = s.linsolve(equation.coeffs(), coeffs)
print("Coboundary coefficient solutions for raw y minus Wickelgren y:", solution)

# Exact weight-three tame residue of a weight-one cocycle cup an
# unramified weight-two cocycle.  This is the strict psi from A.27,
# whose differential becomes q^2-1 in coefficient weight three.
q, alpha, inertia, z = s.symbols("q alpha inertia z")
c_F_tau = 0
c_Ftau_Finv = -(alpha + q*inertia)*z
c_F_Finv = -alpha*z
residue = s.cancel((c_F_tau+c_Ftau_Finv-c_F_Finv)/q)
assert residue == -inertia*z
print("Weight-three tame residue of A cup z_unram = -A(tau)*z(F).")

# The two explicit point x=3 tests detect all twenty-four twists.
seen = set()
for k in range(24):
    test = (k * pow(8, -1, 3) % 3, k * pow(3, -1, 8) % 8)
    assert test not in seen
    seen.add(test)
    assert (test == (0, 0)) == (k == 0)
print("The (2,3) and (3,2) point-section tests detect all 24 twist classes.")
