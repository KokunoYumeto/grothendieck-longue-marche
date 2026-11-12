# Reviewer's independent checks of explicit Lie-algebra witnesses in LM3b (no code shared with the return).
# Elements of the free associative algebra over Z: dict word(tuple of letters) -> int.
from fractions import Fraction
import itertools

def add(*ps, coeffs=None):
    out = {}
    coeffs = coeffs or [1] * len(ps)
    for p, c in zip(ps, coeffs):
        for w, v in p.items():
            out[w] = out.get(w, 0) + c * v
    return {w: v for w, v in out.items() if v}

def scal(c, p): return {w: c * v for w, v in p.items() if c * v}
def mul(p, q):
    out = {}
    for u, a in p.items():
        for v, b in q.items():
            out[u + v] = out.get(u + v, 0) + a * b
    return {w: v for w, v in out.items() if v}
def br(p, q): return add(mul(p, q), mul(q, p), coeffs=[1, -1])
def g(c): return {(c,): 1}

def subst(p, imgs):
    """algebra endomorphism: letter -> imgs[letter] (a polynomial)"""
    out = {}
    for w, c in p.items():
        m = {(): 1}
        for l in w:
            m = mul(m, imgs[l])
        out = add(out, scal(c, m))
    return out

def der(D, p):
    """derivation D: letter -> polynomial, applied to p"""
    out = {}
    for w, c in p.items():
        for i, l in enumerate(w):
            left = {w[:i]: 1}; right = {w[i + 1:]: 1}
            out = add(out, scal(c, mul(mul(left, D[l]), right)))
    return out

def dbr(D, E, letters):
    return {l: add(der(D, E[l]), der(E, D[l]), coeffs=[1, -1]) for l in letters}

report = {}

# ---------- A.3: degree-5 tripod witness ----------
x, y = g('x'), g('y')
ax = add(br(x, br(x, br(br(x, y), y))), scal(-2, br(br(x, br(x, y)), br(x, y))))
ay = br(x, br(x, br(x, br(x, y))))
Dx, Dy = br(ax, x), br(ay, y)
report['A3 sum zero (D(z)=0 gauge)'] = add(Dx, Dy) == {}
tau = {'x': y, 'y': x}
TDx = subst(Dy, tau)   # (tau D tau^-1)(x) = tau(D(y))
TDy = subst(Dx, tau)
report['A3 transposition changes the gauge-fixed derivation'] = (TDx != Dx) or (TDy != Dy)
report['A3 D nonzero'] = Dx != {}
# 3-cycle x->y->z->x with z=-x-y, gauge D(z)=0 is preserved? compute sigma D sigma^-1 and renormalize
zz = add(x, y, coeffs=[-1, -1])
sig = {'x': y, 'y': zz}           # sigma(x)=y, sigma(y)=z
sig_inv = {'x': zz, 'y': x}       # sigma^-1(x)=z, sigma^-1(y)=x
Dfull = {'x': Dx, 'y': Dy}
def apply_der_full(D, p): return der(D, p)
# (sigma D sigma^-1)(x) = sigma(D(sigma^-1 x)) = sigma(D(z)) ; D(z) = -Dx-Dy = 0
SDx = subst(der(Dfull, sig_inv['x']), sig)
SDy = subst(der(Dfull, sig_inv['y']), sig)
report['A3 cycle image (x component) zero'] = SDx == {}

# ---------- B.3: degree-3 four-puncture witness ----------
X, Y, Z = g('x'), g('y'), g('z')
c = br(X, Y)
E = {'x': br(br(Y, c), X), 'y': scal(-1, br(br(X, c), Y)), 'z': {}}
report['B3 E(x+y+z)=0'] = add(E['x'], E['y'], E['z']) == {}
fillz = lambda p: {w: v for w, v in p.items() if 'z' not in w}
fillx = lambda p: {w: v for w, v in p.items() if 'x' not in w}
report['B3 filling x gives zero on y,z'] = fillx(E['y']) == {} and fillx(E['z']) == {}
report['B3 filling z gives nonzero'] = fillz(E['x']) != {}
u = {'x': br(Y, X), 'y': br(X, Y), 'z': {}}
v = {'x': br(Z, X), 'y': {}, 'z': br(X, Z)}
L3 = ['x', 'y', 'z']
Eu = dbr(E, u, L3); Ev = dbr(E, v, L3)
report['B3 [E,u]=0'] = all(not Eu[l] for l in L3)
report['B3 [E,v](z)=[E(x),z] and nonzero'] = Ev['z'] == br(E['x'], Z) and Ev['z'] != {}
# rank of E against point-pushing in degree 3: p_3 spanned by [u,[u,v]],[[u,v],v]
uv = dbr(u, v, L3)
p3 = [dbr(u, uv, L3), dbr(uv, v, L3)]
def vec(D):
    return {(l,) + w: c for l in L3 for w, c in D[l].items()}
import sympy as sp
def rank(Ds):
    keys = sorted({k for D in Ds for k in vec(D)})
    M = sp.Matrix([[vec(D).get(k, 0) for D in Ds] for k in keys])
    return M.rank()
report['B3 rank p3'] = rank(p3)
report['B3 rank p3 + E'] = rank(p3 + [E])
# degree-4: p4 and [E,v]
p4 = [dbr(u, dbr(u, uv, L3), L3), dbr(dbr(u, uv, L3), v, L3), dbr(dbr(uv, v, L3), v, L3)]
report['B3 rank p4'] = rank(p4)
report['B3 rank p4 + [E,v]'] = rank(p4 + [Ev])

# ---------- A.14: degree-7 elliptic witness ----------
a, b = g('a'), g('b')
r = [br(a, b)]
for j in range(4):
    r.append(br(r[-1], b))
Da = add(br(a, br(r[0], r[3])), br(a, br(r[1], r[2])), br(r[0], br(r[0], r[2])), br(br(r[0], r[1]), r[1]), coeffs=[-2, -3, 2, 1])
Db = add(br(r[0], r[4]), br(r[1], r[3]), coeffs=[2, 5])
report['A14 [D(a),b]+[a,D(b)]=0'] = add(br(Da, b), br(a, Db)) == {}
report['A14 D nonzero'] = Da != {} or Db != {}
report['A14 degrees'] = sorted({len(w) for w in Da} | {len(w) for w in Db})

# ---------- F.1: weight-4 polynomial ----------
def psi(X_, Y_):
    xy = br(X_, Y_)
    return add(br(X_, br(X_, xy)), br(X_, br(xy, Y_)), br(br(xy, Y_), Y_), coeffs=[1, -4, 1])
zf = add(x, y, coeffs=[-1, -1])
report['F1 antisymmetry'] = add(psi(x, y), psi(y, x)) == {}
report['F1 3-cycle'] = add(psi(x, y), psi(y, zf), psi(zf, x)) == {}
report['F1 cabling fails'] = add(br(x, psi(x, y)), br(add(x, y), psi(zf, y)), coeffs=[1, -1]) != {}

# ---------- C.5: degree-3 conjugators of the pro-2 witness ----------
ax5 = br(br(X, Y), Y); ay5 = br(X, br(X, Y))
report['C5 [a_x,X]+[a_y,Y]=0'] = add(br(ax5, X), br(ay5, Y)) == {}

for k, val in report.items():
    print(f'{k}: {val}')
