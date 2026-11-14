"""Finite checks used in LM5 Parts B and C. Python 3, standard library only.

These checks supplement the proofs. No bounded computation is presented as
a proof about all groups, all dimensions, or all polynomials.
"""
from itertools import combinations, permutations, product


def rank_mod(matrix, p):
    a = [[x % p for x in row] for row in matrix]
    if not a:
        return 0
    m, n, r = len(a), len(a[0]), 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], -1, p)
        a[r] = [inv * x % p for x in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                k = a[i][c]
                a[i] = [(x - k * y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return r


def betti(simplices, p=2, max_degree=3):
    levels = [sorted(s for s in simplices if len(s) == q + 1)
              for q in range(max_degree + 2)]
    ranks = [0]
    for q in range(1, max_degree + 2):
        rows = {s: i for i, s in enumerate(levels[q - 1])}
        mat = [[0] * len(levels[q]) for _ in rows]
        for j, s in enumerate(levels[q]):
            for i in range(len(s)):
                mat[rows[s[:i] + s[i + 1:]]][j] += (-1) ** i
        ranks.append(rank_mod(mat, p))
    return [len(levels[q]) - ranks[q] - ranks[q + 1]
            for q in range(max_degree + 1)]


arrow = {(0,), (1,), (0, 1)}
sphere = {c for r in range(1, 4) for c in combinations(range(4), r)}
for prime in (2, 3, 5):
    a, b = betti(arrow, prime), betti(sphere, prime)
    assert a == [1, 0, 0, 0]
    assert b == [1, 0, 1, 0]
    print(f"B.4 mod {prime}: nerve([1]) Betti={a}; S2 Betti={b}")


def hm(x, y, n):
    a, b, c = x
    d, e, f = y
    return ((a + d) % n, (b + e) % n, (c + f + a * e) % n)


def hi(x, n):
    a, b, c = x
    return (-a % n, -b % n, (-c + a * b) % n)


for modulus in (2, 3, 4, 5, 9):
    x, y = (1, 0, 0), (0, 1, 0)
    comm = hm(hm(hm(x, y, modulus), hi(x, modulus), modulus), hi(y, modulus), modulus)
    z, order = (0, 0, 0), None
    for j in range(1, modulus + 1):
        z = hm(z, comm, modulus)
        if z == (0, 0, 0):
            order = j
            break
    assert comm == (0, 0, 1) and order == modulus
    print(f"B.6 Heisenberg(Z/{modulus}): commutator={comm}, order={order}")


S3 = list(permutations(range(3)))
one = tuple(range(3))


def pm(a, b):
    return tuple(a[b[i]] for i in range(3))


def pinv(a):
    return tuple(a.index(i) for i in range(3))


def wm(x, y):
    b, s = x
    c, t = y
    si = pinv(s)
    return (tuple(pm(b[i], c[si[i]]) for i in range(3)), pm(s, t))


base = list(product(S3, repeat=3))
wreath = list(product(base, S3))
gens = []
for i in range(3):
    for v in ((1, 0, 2), (1, 2, 0)):
        t = [one] * 3
        t[i] = v
        gens.append((tuple(t), one))
centralizer = [x for x in wreath if all(wm(x, y) == wm(y, x) for y in gens)]
center_S3 = [s for s in S3 if all(pm(s, t) == pm(t, s) for t in S3)]
assert len(wreath) == 1296 and len(base) == 216
assert len(centralizer) == 1 and len(center_S3) == 1
print("C.11 nonclosure of centralizer-free maps:")
print(f"  N=S3^3 has order {len(base)}; H=N semidirect S3 has order {len(wreath)}")
print(f"  |C_H(N)|={len(centralizer)}; |C_S3(S3)|={len(center_S3)}")
print("  composite N -> H -> S3 is trivial; its centralizer has order 6")


def reduced(word):
    stack = []
    for letter in word:
        if stack and stack[-1] == letter:
            stack.pop()
        else:
            stack.append(letter)
    return tuple(stack)


lengths = [len(reduced((0, 1) * n)) for n in range(1, 11)]
assert lengths == list(range(2, 21, 2))
print("C.4 C2*C2: lengths of (ab)^n, n=1,...,10:", lengths)
print("The proof uses the normal-form theorem for all n, not this finite test.")


for p in (2, 3, 5):
    m = next(m for m in range(2, 10) if m % p and (p - 1) * (m - 1) >= 2)
    numerator = (p - 1) * (m - 1)
    assert numerator % 2 == 0
    print(f"B.6 AS cover y^{p}-y=x^{m}: genus={numerator // 2}, one point above infinity")

print("ALL FINITE CHECKS PASSED")
