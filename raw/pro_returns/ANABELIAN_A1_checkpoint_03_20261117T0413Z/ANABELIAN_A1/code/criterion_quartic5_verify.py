"""Independent verifier for quartic_cyclic5.json; imports no producer code.

Checks all elliptic kernels, the rational isogeny and pullback identities,
the complete regular-differential basis, every Cartier coefficient, its
eighth semilinear iterate by a direct ordered product, and characteristic
polynomials using a division-free recursive adjugate calculation rather
than the producer's Bareiss determinant.  Small base-curve counts use a
separate elementary polynomial-field implementation.
"""
from pathlib import Path
from hashlib import sha256
import json

from flint import fq_default_ctx, fq_default_poly_ctx, fmpz_mod_poly_ctx

ROOT = Path(__file__).resolve().parent
source = ROOT / "quartic_cyclic5.json"
raw = source.read_bytes()
data = json.loads(raw)
assert data["field"]["p"] == 3 and data["field"]["degree"] == 8
assert data["ell"] == 5 and data["constant_degree"] == 8
P = fmpz_mod_poly_ctx(3)
modulus = P(data["field"]["modulus"])
z = P.gen()
assert z.pow_mod(3**8, modulus) == z
assert (z.pow_mod(3**4, modulus)-z).gcd(modulus) == 1
k = fq_default_ctx(modulus=modulus, var="z", fq_type="FQ_NMOD")
R = fq_default_poly_ctx(k)
x = R.gen()
zero, one = k.zero(), k.one()
f = x**3-x


def decode(n):
    assert isinstance(n, int) and 0 <= n < 3**8
    return k([(n//3**j) % 3 for j in range(8)])


def encode(a):
    return sum(int(c)*3**i for i, c in enumerate(a.to_list()))


def polynomial(values):
    return R([decode(n) for n in values])


def matrix(values):
    return [[decode(n) for n in row] for row in values]


def ec_add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    a, b = P
    c, d = Q
    if a == c and b+d == 0:
        return None
    slope = (d-b)/(c-a) if a != c else (-one)/(2*b)
    X = slope*slope-a-c
    Y = -b+slope*(a-X)
    assert Y*Y == X**3-X
    return X, Y


def ec_mul(n, point):
    # A repeated-addition path suffices for the small orders checked here.
    ans = None
    for i in range(n):
        ans = ec_add(ans, point)
    return ans


def matmul(A, B):
    return [[sum((A[i][h]*B[h][j] for h in range(len(B))), zero)
             for j in range(len(B[0]))] for i in range(len(A))]


def eye(n):
    return [[one if i == j else zero for j in range(n)] for i in range(n)]


def rank(A):
    A = [row[:] for row in A]
    r = 0
    for j in range(len(A[0])):
        candidates = [i for i in range(r, len(A)) if A[i][j] != 0]
        if not candidates:
            continue
        i = candidates[0]
        A[i], A[r] = A[r], A[i]
        pivot = A[r][j]
        A[r] = [a/pivot for a in A[r]]
        for i in range(len(A)):
            if i != r and A[i][j] != 0:
                ratio = A[i][j]
                A[i] = [a-ratio*b for a, b in zip(A[i], A[r])]
        r += 1
    return r


def characteristic(A):
    """det(X-A) by block adjugates, without divisions in characteristic 3."""
    n = len(A)
    if n == 0:
        return R.one()
    a = A[0][0]
    B = [row[1:] for row in A[1:]]
    cp = characteristic(B)
    out = (x-a)*cp
    if n == 1:
        return out
    row = A[0][1:]
    v = [A[i][0] for i in range(1, n)]
    moments = []
    for j in range(n-1):
        moments.append(sum((b*c for b, c in zip(row, v)), zero))
        v = [sum((b*c for b, c in zip(br, v)), zero) for br in B]
    # cp=X^m+c1 X^(m-1)+...; adjugate coefficient is
    # B^j+c1 B^(j-1)+...+cj I.
    m = n-1
    for j in range(m):
        coeff = sum((cp[m-h]*moments[j-h] for h in range(j+1)), zero)
        out -= R([zero]*(m-1-j)+[coeff])
    return out


def cartier_independent(F, factors, basis):
    n = len(basis)
    result = [[zero for j in range(n)] for i in range(n)]
    for column, (s, j) in enumerate(basis):
        target = next(t for t in (1, 2, 3) if (3*t-s) % 4 == 0)
        exponent = (3*target-s)//4
        numerator = factors[s]*x**j*F**exponent
        terms = []
        for degree in range(numerator.degree()+1):
            if degree % 3 == 2:
                terms.append(numerator[degree]**(3**7))
        extracted = R(terms)
        quotient, remainder = divmod(extracted, factors[target])
        assert remainder == 0
        for i, (tt, degree) in enumerate(basis):
            if tt == target:
                result[i][column] = quotient[degree]
        rebuilt = sum((R([result[i][column]])*x**degree
                       for i, (tt, degree) in enumerate(basis) if tt == target), R.zero())
        assert rebuilt == quotient
    return result


def elementary_count(n, modulus_coeffs):
    """Independent, small finite-field arithmetic; no FLINT use here."""
    q = 3**n
    def digits(a):
        return [(a//3**i) % 3 for i in range(n)]
    def add(a, b):
        return sum(((x+y) % 3)*3**i for i, (x, y) in enumerate(zip(digits(a), digits(b))))
    def neg(a):
        return sum((-x % 3)*3**i for i, x in enumerate(digits(a)))
    def mul(a, b):
        aa, bb = digits(a), digits(b)
        out = [0]*(2*n-1)
        for i in range(n):
            for j in range(n):
                out[i+j] = (out[i+j]+aa[i]*bb[j]) % 3
        for j in range(2*n-2, n-1, -1):
            c = out[j]
            for i in range(n):
                out[j-n+i] = (out[j-n+i]-c*modulus_coeffs[i]) % 3
        return sum(out[i]*3**i for i in range(n))
    fourth = [0]*q
    for w in range(q):
        w2 = mul(w, w)
        fourth[mul(w2, w2)] += 1
    count = 1
    for X in range(q):
        rhs = add(mul(mul(X, X), X), neg(X))
        count += fourth[rhs]
    return count


counts = [elementary_count(n, mod) for n, mod in
          [(1, [0, 1]), (2, [1, 0, 1]), (3, [2, 2, 0, 1])]]
assert counts == [4, 4, 28]
trace1, trace2, trace3 = [3**i+1-counts[i-1] for i in (1, 2, 3)]
a1 = -trace1
a2 = -(trace2+a1*trace1)//2
a3 = -(trace3+a1*trace2+a2*trace1)//3
assert (a1, a2, a3) == (0, -3, 0)
base_weil_polynomial = [27, 0, -9, 0, -3, 0, 1]
# (X^2+3)(X^2-3)^2; each root modulo5 has fourth power -1,
# hence exact order8.  This necessary period statement does not
# require a semisimplicity assertion for the repeated factor.
assert pow(2, 2, 5) == pow(3, 2, 5) == 4

base_basis = [(2, 0), (3, 0), (3, 1)]
base_C = cartier_independent(f, {s:R.one() for s in (1, 2, 3)}, base_basis)
assert base_C == matrix(data["base_Cartier_matrix"])
assert all(a == 0 for row in base_C for a in row)

E_basis = [tuple(decode(n) for n in point) for point in data["E5_basis"]]
for point in E_basis:
    assert point[1]**2 == point[0]**3-point[0]
    assert ec_mul(5, point) is None and point is not None
assert E_basis[1] not in [ec_mul(i, E_basis[0]) for i in range(5)]
all_torsion = {None}
for i in range(5):
    for j in range(5):
        point = ec_add(ec_mul(i, E_basis[0]), ec_mul(j, E_basis[1]))
        all_torsion.add(None if point is None else tuple(map(encode, point)))
assert len(all_torsion) == 25

checked, lines = [], set()
for record in data["covers"]:
    point = tuple(map(decode, record["kernel_generator"]))
    second = tuple(map(decode, record["kernel_second"]))
    assert ec_mul(2, point) == second and ec_mul(5, point) is None
    line = frozenset(tuple(map(encode, ec_mul(i, point))) for i in range(1, 5))
    assert len(line) == 4 and line not in lines
    lines.add(line)
    h, N, g = [polynomial(record[name]) for name in ("h", "N", "g")]
    assert h == (x-point[0])*(x-second[0])
    expected_N = x*h*h
    for a, b in (point, second):
        lin = x-a
        q1, r1 = divmod(h*h, lin)
        q2, r2 = divmod(h*h, lin*lin)
        assert r1 == r2 == 0
        expected_N += q1+b*b*q2
    assert N == expected_N and N.gcd(h) == 1
    assert g == N.derivative()*h-2*N*h.derivative()
    aa, bb = map(decode, record["target_E_coefficients"])
    assert f*g*g == N**3+aa*N*h**4+bb*h**6
    scale, shift = decode(record["scale"]), decode(record["shift"])
    assert scale**4 == -aa and shift**3+aa*shift+bb == 0
    F = polynomial(record["cover_polynomial_F"])
    assert F == f*g*g*h*h/(scale**6)
    # Direct verification of W^4=X^3-X after clearing h^8.
    assert F == ((N-shift*h*h)**3*h*h-scale**4*(N-shift*h*h)*h**6)/(scale**6)
    assert (f.degree(), g.degree(), h.degree(), F.degree()) == (3, 6, 2, 19)
    assert all(a.is_squarefree() for a in (f, g, h))
    assert f.gcd(g) == f.gcd(h) == g.gcd(h) == 1
    basis = [tuple(entry) for entry in record["basis"]]
    expected_basis = []
    for s in (1, 2, 3):
        hf_degree = 0 if s == 1 else 8
        j = 0
        while 19*s-4*hf_degree-4*j-5 >= 0:
            expected_basis.append((s, j))
            j += 1
    assert basis == expected_basis and len(basis) == 11
    M = cartier_independent(F, {1:R.one(), 2:g*h, 3:g*h}, basis)
    assert M == matrix(record["Cartier_matrix"])
    A = eye(11)
    for j in range(8):
        conjugated = [[a**(3**((-j) % 8)) for a in row] for row in M]
        A = matmul(A, conjugated)
    assert A == matrix(record["Cartier_eighth_power"])
    cp = characteristic(A)
    assert cp == polynomial(record["Frobenius_characteristic_polynomial_mod_3"])
    assert cp == x**3*(x+1)**8
    assert cp(one) == 1
    assert rank(A) == rank(matmul(A, A)) == 8
    assert record["power_ranks"] == [8]*12
    assert record["p_rank"] == 8 and record["relative_class_number_prime_to_3"] is True
    checked.append({
        "kernel_generator": record["kernel_generator"],
        "checked_Cartier_entries": 121,
        "characteristic_polynomial": [encode(a) for a in cp],
        "det_one_minus_Cartier_eighth_power": encode(cp(one)),
        "stable_rank": 8,
        "all_even_extensions_bad_all_odd_extensions_good": True,
    })
assert len(lines) == 6
assert set().union(*lines) == all_torsion-{None}

out = {
    "source_sha256": sha256(raw).hexdigest(),
    "field_modulus_irreducible": True,
    "base_point_counts_degrees_1_2_3": counts,
    "base_Frobenius_polynomial_ascending": base_weil_polynomial,
    "base_Frobenius_polynomial_factored": "(X^2+3)(X^2-3)^2",
    "every_degree5_constant_cover_requires_field_degree_multiple_of": 8,
    "base_Cartier_zero": True,
    "six_distinct_elliptic_kernel_lines_exhaust_E5": True,
    "verified_covers": checked,
    "conclusion": "all six genus11 P-split cyclic5 covers have 3-unit relative class number over F_(3^8)",
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2)+"\n")
print(json.dumps(out, indent=2))
