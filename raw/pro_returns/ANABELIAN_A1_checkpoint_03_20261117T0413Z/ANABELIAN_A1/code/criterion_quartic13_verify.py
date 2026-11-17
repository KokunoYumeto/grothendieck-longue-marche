"""Independent exact certificate for the F_125 cyclic-13 quartic witness.

This checker does not import the search producer. Polynomial arithmetic,
the degree-three field, the elliptic group law, and Cartier extraction
are implemented here over the prime field. SymPy supplies an independent
integer characteristic-polynomial calculation, reduced modulo five.
"""
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parent
source = json.loads((ROOT / "criterion_quartic_f5_ell13.json").read_text())
record = source["covers"][7]
p = 5


def trim(a):
    a = [int(v) % p for v in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a or [0]


def plus(a, b):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(a, c):
    return trim([c * v for v in a])


def times(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return trim(c)


def power(a, n):
    b = [1]
    while n:
        if n & 1:
            b = times(b, a)
        a = times(a, a)
        n >>= 1
    return b


def divide(a, b):
    a, b = trim(a), trim(b)
    assert b != [0]
    q = [0] * max(1, len(a) - len(b) + 1)
    while a != [0] and len(a) >= len(b):
        d = len(a) - len(b)
        c = a[-1] * pow(b[-1], -1, p) % p
        q[d] = c
        a = plus(a, [0] * d + scale(b, -c))
    return trim(q), a


def derivative(a):
    return trim([i * a[i] for i in range(1, len(a))])


def gcd(a, b):
    while b != [0]:
        a, b = b, divide(a, b)[1]
    return scale(a, pow(a[-1], -1, p))


def peval(a, x):
    y = 0
    for c in reversed(a):
        y = (y * x + c) % p
    return y


# F_125 = F_5[z]/(z^3+4z^2+3z+1), encoded in base five.
modulus = [1, 3, 4, 1]
assert all(peval(modulus, a) != 0 for a in range(p))


def digits(a):
    return [(a // p**i) % p for i in range(3)]


def encode(a):
    return sum((v % p) * p**i for i, v in enumerate(a))


def fa(a, b):
    return encode(plus(digits(a), digits(b)))


def fn(a):
    return encode(scale(digits(a), -1))


def fm(a, b):
    return encode(divide(times(digits(a), digits(b)), modulus)[1])


def fp(a, n):
    b = 1
    while n:
        if n & 1:
            b = fm(b, a)
        a = fm(a, a)
        n >>= 1
    return b


def fd(a, b):
    assert b != 0
    return fm(a, fp(b, 123))


assert all(fp(a, 125) == a for a in range(125))
assert all(fp(a, 124) == 1 for a in range(1, 125))


def add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    a, b = P
    c, d = Q
    if a == c and fa(b, d) == 0:
        return None
    slope = fd(fa(d, fn(b)), fa(c, fn(a))) if a != c else \
        fd(fa(fm(3, fm(a, a)), 4), fm(2, b))
    X = fa(fa(fm(slope, slope), fn(a)), fn(c))
    Y = fa(fn(b), fm(slope, fa(a, fn(X))))
    return X, Y


def mul(n, P):
    Q = None
    while n:
        if n & 1:
            Q = add(Q, P)
        P = add(P, P)
        n >>= 1
    return Q


def fpeval(a, u):
    y = 0
    for c in reversed(a):
        y = fa(fm(y, u), c)
    return y


h, N, g, F = (record[name] for name in ("h", "N", "g", "F"))
assert all(0 <= v < 5 for a in (h, N, g, F) for v in a)
assert h == [4, 0, 1, 0, 0, 0, 1]
assert g == plus(times(derivative(N), h), scale(times(N, derivative(h)), -2))
f = [0, 4, 0, 1]
assert times(f, power(g, 2)) == plus(power(N, 3), scale(times(N, power(h, 4)), -1))
assert F == scale(times(times(f, power(g, 2)), power(h, 2)), 4)
assert len(N) - 1 == 13 and len(g) - 1 == 18 and len(F) - 1 == 51
assert gcd(N, h) == [1]
assert all(gcd(a, derivative(a)) == [1] for a in (f, g, h))
assert all(gcd(a, b) == [1] for a, b in ((f, g), (f, h), (g, h)))

# A nonzero kernel point and its twelve translates prove constancy.
z = 5
rhs = fa(fp(z, 3), fn(z))
ys = [a for a in range(125) if fm(a, a) == rhs]
assert len(ys) == 2
K = (z, ys[0])
assert mul(13, K) is None
kernel = [mul(i, K) for i in range(13)]
assert len(set(kernel)) == 13
assert all(fpeval(h, T[0]) == 0 for T in kernel[1:])
assert len({T[0] for T in kernel[1:]}) == 6
assert all(fpeval(f, T[0]) == fm(T[1], T[1]) for T in kernel[1:])
assert not all(fp(a, 5) == a for a in K)

# Derive the entire differential matrix independently from its formula.
basis = [(1, j) for j in range(12)] + [(2, 0)] + [(3, j) for j in range(14)]
assert record["basis"] == [list(v) for v in basis]
gh = times(g, h)
factors = {1: [1], 2: gh, 3: gh}
M = [[0] * 27 for _ in range(27)]
for j, (s, a) in enumerate(basis):
    numerator = times([0] * a + factors[s], power(F, s))
    extracted = trim(numerator[4::5])
    quotient, remainder = divide(extracted, factors[s])
    assert remainder == [0]
    reconstructed = [0]
    for i, (t, b) in enumerate(basis):
        if t == s:
            M[i][j] = quotient[b] if b < len(quotient) else 0
            reconstructed = plus(reconstructed, [0] * b + [M[i][j]])
    assert reconstructed == quotient
assert M == record["Cartier_matrix"]


def mm(A, B):
    return [[sum(a * b for a, b in zip(row, col)) % 5 for col in zip(*B)]
            for row in A]


A = mm(mm(M, M), M)
old = [[3, 0, 0], [0, 0, 4], [0, 1, 0]]
assert old == source["base_Cartier_matrix"]
old3 = mm(mm(old, old), old)
T = sp.Symbol("T")


def charpoly(A):
    return sp.Poly(sp.Matrix(A).charpoly(T).as_expr(), T, modulus=5)


full_cp = charpoly(A)
old_cp = charpoly(old3)
new_cp = full_cp.exquo(old_cp)
assert charpoly(M) == sp.Poly((T-2)**5*(T+2)**6*(T*T-2*T-1)**4*(T*T+2*T-1)**4, T, modulus=5)
assert full_cp == sp.Poly((T - 2)**14 * (T + 2)**13, T, modulus=5)
assert old_cp == sp.Poly((T - 2)**2 * (T + 2), T, modulus=5)
assert new_cp == sp.Poly((T - 2)**12 * (T + 2)**12, T, modulus=5)
assert int(new_cp.eval(1)) % 5 == 1
assert sp.Matrix(A).det() % 5 != 0


def cp_list(f):
    return [int(v) % 5 for v in reversed(f.all_coeffs())]


def point_count(mod):
    degree = len(mod) - 1
    q = 5**degree
    def digs(a):
        return [(a // 5**i) % 5 for i in range(degree)]
    def enc(a):
        return sum((v % 5) * 5**i for i, v in enumerate(a))
    def multiplication(a, b):
        return enc(divide(times(digs(a), digs(b)), mod)[1])
    counts = {}
    for w in range(q):
        w2 = multiplication(w, w)
        w4 = multiplication(w2, w2)
        counts[w4] = counts.get(w4, 0) + 1
    result = 1
    for x in range(q):
        x3 = multiplication(multiplication(x, x), x)
        rhs = enc(plus(digs(x3), scale(digs(x), -1)))
        result += counts.get(rhs, 0)
    return result


point_counts = [point_count(m) for m in ([0, 1], [2, 0, 1], modulus)]
assert point_counts == [8, 44, 104]
H = sp.Poly((T*T + 2*T + 5)**2 * (T*T - 2*T + 5), T)
roots_power_sums = [5**n + 1 - point_counts[n-1] for n in (1, 2, 3)]
assert roots_power_sums == [-2, -18, 22]
newton = [1]
for n in (1, 2, 3):
    numerator = sum(newton[n-i] * roots_power_sums[i-1] for i in range(1, n+1))
    assert numerator % n == 0
    newton.append(-numerator // n)
assert H.all_coeffs() == newton + [5*newton[2], 25*newton[1], 125]
old_counts = []
for n in (1, 2, 3):
    factors = []
    for trace in (-2, 2):
        sums = [2, trace]
        for j in range(2, n+1):
            sums.append(trace*sums[-1] - 5*sums[-2])
        factors.append(5**n + 1 - sums[n])
    old_counts.append(factors[0]**2 * factors[1])
assert old_counts == [256, 32768, 104**2 * 148]
assert sp.factorint(old_counts[2]) == {2: 8, 13: 2, 37: 1}
X, Z = sp.symbols("X Z")
fermat_identity = sp.Poly((X+2*Z)**4-(X-2*Z)**4-(X**3*Z-X*Z**3), X, Z, modulus=5)
assert fermat_identity.is_zero
assert sp.Matrix([[1, 0, -2], [0, 1, 0], [1, 0, 2]]).det() % 5 != 0

certificate = {
    "verified": True,
    "method": "independent prime-field polynomial arithmetic and Cartier extraction; SymPy integer characteristic polynomials",
    "curve": "W^4=X^3Z-XZ^3 over F_5",
    "point": [1, 0, 0],
    "ell": 13,
    "constant_field": {"p": 5, "degree": 3, "modulus": modulus},
    "kernel_generator_base5": list(K),
    "kernel_base5": [list(P) if P else None for P in kernel],
    "E": "y^2=x^3-x",
    "h": h, "N": N, "g": g, "F": F,
    "cover_equation": "w^4=4*(x^3-x)*g(x)^2*h(x)^2",
    "map_to_C": "X=N/(4*h^2), W=w/h^2",
    "genus": 27,
    "basis": [list(a) for a in basis],
    "Cartier_matrix": M,
    "Cartier_cubed": A,
    "base_Cartier_matrix": old,
    "base_Cartier_cubed": old3,
    "full_charpoly_mod5": cp_list(full_cp),
    "base_charpoly_mod5": cp_list(old_cp),
    "new_charpoly_mod5": cp_list(new_cp),
    "relative_class_number_mod5": 1,
    "new_p_rank": 24,
    "further_extension_condition": "4 does not divide extension degree",
    "base_point_counts_degrees1to3": point_counts,
    "base_Weil_polynomial_descending": [int(v) for v in H.all_coeffs()],
    "base_Jacobian_orders_degrees1to3": old_counts,
    "least_constant_degree_for_any_odd_prime_witness": 3,
    "least_prime_at_constant_degree3": 13,
    "pointed_Fermat_isomorphism": "(X:W:Z) -> (X-2Z:W:X+2Z); U^4+V^4=R^4, infinity maps to (1:0:1)",
}
(ROOT / "criterion_quartic13_verify.json").write_text(json.dumps(certificate, indent=2) + "\n")
print(json.dumps({key: certificate[key] for key in (
    "verified", "ell", "constant_field", "kernel_generator_base5", "genus",
    "relative_class_number_mod5", "new_p_rank", "further_extension_condition",
    "base_point_counts_degrees1to3", "base_Jacobian_orders_degrees1to3",
    "least_constant_degree_for_any_odd_prime_witness", "least_prime_at_constant_degree3")}, indent=2))
print("Full Cartier^3: (T-2)^14 (T+2)^13; new factor: (T-2)^12 (T+2)^12")
