#!/usr/bin/env python3
"""Exact arithmetic for A.102, including the search that selected its witness.

The program checks finite arithmetic, not existence of a full section.
The section of the named H-plus-abelian quotient is constructed in the proof.
"""

from math import comb
from sympy import factorint, primerange


def vp(a, p):
    if not a:
        return float("inf")
    a, v = abs(int(a)), 0
    while a % p == 0:
        a //= p
        v += 1
    return v


def first_log(a, p):
    return (((pow(int(a), p-1, p*p)-1)//p)
            * pow(p-1, -1, p)) % p


def first_ratio(a, b, p):
    if not a % p or not b % p:
        return None
    return a*pow(b, -1, p) % p


def square_unit(a, p):
    return a is not None and pow(a, (p-1)//2, p) == 1


selected = []
for p0 in primerange(5, 3000):
    p = int(p0)
    factors = factorint(2*p-1)
    q = int(max(factors))
    if q < 5 or factors[q] != 1:
        continue
    m = (2*p-1)//q
    ap = first_ratio(-6*first_log(2, p), -6*first_log(2, p)+2, p)
    bp = first_ratio(-first_log(m, p), first_log(q, p), p)
    aq = first_ratio(-first_log(2, q), first_log(p, q), q)
    bq = first_ratio(2*first_log(m, q)-8*first_log(2, q),
                     2*first_log(m, q)-8*first_log(2, q)-m, q)
    if all((square_unit(ap, p), square_unit(bp, p),
            square_unit(aq, q), square_unit(bq, q))):
        selected.append((2*p, p, q, m, ap, bp, aq, bq))
        if len(selected) == 10:
            break
assert selected[0] == (254, 127, 23, 11, 31, 49, 8, 4)


def mul(a, b, degree):
    out = [0]*(degree+1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i+j <= degree:
                out[i+j] += x*y
    return out


def inv(a, degree):
    assert a[0] == 1
    out = [1]+[0]*degree
    for k in range(1, degree+1):
        out[k] = -sum(a[i]*out[k-i] for i in range(1, k+1))
    return out


def evaluate(a, x, modulus):
    out = 0
    for c in reversed(a):
        out = (out*x+c) % modulus
    return out


def log_unit(a, p, precision):
    modulus = p**precision
    z = (pow(a, p-1, modulus)-1) % modulus
    if not z:
        return 0
    depth = vp(z, p)
    out = 0
    for n in range(1, p*precision+5):
        d = vp(n, p)
        if n*depth-d < precision:
            term = (z**n//p**d)*pow(n//p**d, -1, modulus)
            out = (out+(-1)**(n+1)*term) % modulus
    return out*pow(p-1, -1, modulus) % modulus


def ratio(a, b, p, precision):
    modulus = p**precision
    a, b = a % modulus, b % modulus
    depth = vp(a, p)
    assert depth == vp(b, p) == 1
    target_modulus = p**(precision-depth)
    return ((a//p**depth)*pow(b//p**depth, -1, target_modulus)
            % target_modulus, target_modulus)


def square_root(a, p, modulus):
    root = next(z for z in range(1, p) if z*z % p == a % p)
    for _ in range(10):
        root = (root+a*pow(root, -1, modulus))*pow(2, -1, modulus) % modulus
    assert root*root % modulus == a % modulus
    return root


degree, precision = 12, 7
e4 = [1]+[240*sum(d**3 for d in range(1, n+1) if n % d == 0)
          for n in range(1, degree+1)]
delta = [1]+[0]*degree
for n in range(1, degree+1):
    term = [0]*(degree+1)
    for k in range(min(24, degree//n)+1):
        term[n*k] = (-1)**k*comb(24, k)
    delta = mul(delta, term, degree)
phi = mul(mul(mul(e4, e4, degree), e4, degree), inv(delta, degree), degree)
assert phi[:5] == [1, 744, 196884, 21493760, 864299970]

nomes = {}
for p, w in ((127, 254), (23, -253)):
    modulus = p**(precision+2)
    j_num = 256*(w*w-w+1)**3
    j_den = w*w*(1-w)**2
    q = 0
    for _ in range(precision+4):
        q = j_den*evaluate(phi, q, modulus)*pow(j_num, -1, modulus) % modulus
    assert (j_num*q-j_den*evaluate(phi, q, modulus)) % modulus == 0
    assert vp(q, p) == 2
    unit_modulus = p**precision
    unit_q = q//(p*p)
    F = 256*unit_q*pow((w//p)**2, -1, unit_modulus) % unit_modulus
    LF = log_unit(F, p, precision)
    assert F % (p*p) == (1+w) % (p*p)
    assert LF % (p*p) == w % (p*p)
    nomes[p] = (q, F, log_unit(unit_q, p, precision), LF)

ap, mp = ratio(-6*log_unit(2, 127, precision), nomes[127][2], 127, precision)
bp, _ = ratio(-log_unit(11, 127, precision), log_unit(23, 127, precision), 127, precision)
aq, mq = ratio(-log_unit(2, 23, precision), log_unit(127, 23, precision), 23, precision)
bq, _ = ratio(2*log_unit(11, 23, precision)-8*log_unit(2, 23, precision),
               nomes[23][2], 23, precision)
assert (ap % 127, bp % 127, aq % 23, bq % 23) == (31, 49, 8, 4)
roots = {
    "alpha127": square_root(ap, 127, mp),
    "beta127": square_root(bp, 127, mp),
    "alpha23": square_root(aq, 23, mq),
    "beta23": square_root(bq, 23, mq),
}

# The four exact defining equalities are checked to their retained precision.
assert (ap*nomes[127][2]+6*log_unit(2, 127, precision)) % 127**precision == 0
assert (bp*log_unit(23, 127, precision)+log_unit(11, 127, precision)) % 127**precision == 0
assert (aq*log_unit(127, 23, precision)+log_unit(2, 23, precision)) % 23**precision == 0
assert (bq*nomes[23][2]-2*log_unit(11, 23, precision)
        +8*log_unit(2, 23, precision)) % 23**precision == 0

# Torsion at the bad places and the untouched common H^ab factors.
assert factorint(127-1) == {2: 1, 3: 2, 7: 1}
assert factorint(23-1) == {2: 1, 11: 1}
assert factorint(11-1) == {2: 1, 5: 1}
assert (127-1) % 23 and (23-1) % 127
assert all(10 % ell for ell in (23, 127))
assert 254 == 2*127 and 1-254 == -11*23
assert factorint(16*254**2*(1-254)**2) == {2: 6, 11: 2, 23: 2, 127: 2}
assert (-11*23) % 127 == 1 and (2*127) % 23 == 1

# Exact good-place failure in the finite abelian quotient at exponent46.
alpha46 = next(z for z in range(46) if z % 2 == 1 and z % 23 == 8)
beta46 = next(z for z in range(46) if z % 2 == 1 and z % 23 == 4)
assert (alpha46, beta46) == (31, 27)
A47, B47 = 2*pow(127, alpha46, 47) % 47, -11*pow(23, beta46, 47) % 47
assert (A47, B47) == (33, 33)
assert (A47+B47) % 47 == 19
assert B47 != 1 and A47 != 1 and (A47+B47) % 47 != 0
assert (first_log(2, 11), first_log(127, 11)) == (6, 6)
assert -first_log(2, 11)*pow(first_log(127, 11), -1, 11) % 11 == 10
assert not square_unit(10, 11)

print("A.102 bad-place fibre certificate: all checks passed.")
print("Search selecting the witness; tuples are (lambda,p,q,m,alpha_p,beta_p,alpha_q,beta_q):")
for row in selected:
    print(" ", row)
print("These residue tests select witnesses; they make no full-section recognition claim.")
for p in (127, 23):
    q, F, Lq, LF = nomes[p]
    print(f"p={p}: nome modulo p^9={q}; F modulo p^7={F}; log(nome/p^2) modulo p^7={Lq}.")
    print(f"  log(F) modulo p^2={LF % (p*p)}.")
print(f"alpha127={ap}, beta127={bp} modulo127^6={mp}.")
print(f"alpha23={aq}, beta23={bq} modulo23^6={mq}.")
print("Explicit unit square roots at these precisions:", roots)
print("Bad places are exactly2,11,23,127; the two modified primary factors are absent from the relevant other unit torsion groups.")
print("At47: exponents modulo46=(31,27), residues(A,B)=(33,33), sum=19, excluding ordinary points and all three cusps.")
print("Recognition addition: at11 the first logarithms of2 and127 are both6, so cusp1 would force the nonsquare alpha11=10.")
print("After11 is ordinary, the23 equations force the same exponents modulo46 for every remaining two-label configuration, independently of all other coefficients.")
print("The proof constructs only the actual full-H-plus-abelian quotient section and proves its local matching at all bad places.")
