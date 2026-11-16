"""NOTES §36, main session (Claude Opus 5.5 at effort max), 16 Nov 2026. Independent check of S2COUNT's six-arrow monoid
M = {1, x00, x01, x10, x11, y}: x_ij x_kl = x_il, y x_ij = x_0j, x_ij y = x_i0, y^2 = x00. (1) associativity and unit;
(2) H_n(BM) from the normalized bar complex C_n = Z[(M - 1)^n], n <= 4, by ranks mod several primes (equal ranks for all
primes = no torsion there). Claim to test: H_0 = Z, H_1 = 0, H_n = Z for n >= 2 (BM ~ wedge of S^n, n >= 2)."""
import itertools
E = ["1", "x00", "x01", "x10", "x11", "y"]
def mul(a, b):
    if a == "1": return b
    if b == "1": return a
    if a == "y" and b == "y": return "x00"
    if a == "y": return "x0" + b[2]          # y x_ij = x_0j
    if b == "y": return "x" + a[1] + "0"     # x_ij y = x_i0
    return "x" + a[1] + b[2]                 # x_ij x_kl = x_il
assert all(mul(mul(a, b), c) == mul(a, mul(b, c)) for a in E for b in E for c in E), "not associative"
print("associative, unit 1: ok")
N = [e for e in E if e != "1"]
def basis(n): return list(itertools.product(N, repeat=n))
def boundary(n):
    """d: C_n -> C_{n-1} as {col: {row: coeff}} (normalized: faces with an entry 1 vanish)."""
    rows = {b: i for i, b in enumerate(basis(n - 1))}
    cols = []
    for s in basis(n):
        v = {}
        def add(t, c):
            if "1" in t: return
            v[rows[t]] = v.get(rows[t], 0) + c
        add(s[1:], 1)
        for i in range(n - 1):
            add(s[:i] + (mul(s[i], s[i + 1]),) + s[i + 2:], (-1) ** (i + 1))
        add(s[:-1], (-1) ** n)
        cols.append({k: c for k, c in v.items() if c})
    return cols, len(rows)
def rank_mod(cols, p):
    pivots = {}  # pivot row -> reduced vector
    r = 0
    for col in cols:
        v = {k: c % p for k, c in col.items() if c % p}
        while v:
            k = max(v)
            if k in pivots:
                w = pivots[k]; f = v[k] * pow(w[k], -1, p) % p
                for kk, cc in w.items():
                    v[kk] = (v.get(kk, 0) - f * cc) % p
                    if v[kk] == 0: del v[kk]
            else:
                pivots[k] = v; r += 1; break
    return r
ranks = {}
for n in range(1, 6):
    cols, _ = boundary(n)
    ranks[n] = {p: rank_mod(cols, p) for p in (2, 3, 5, 1000003)}
    print(f"rank d_{n} (C_{n} -> C_{n-1}, {len(cols)} columns):", ranks[n])
dims = {n: 5 ** n for n in range(0, 6)}
for n in range(0, 5):
    for p in (2, 3, 5, 1000003):
        rk_out = ranks[n][p] if n >= 1 else 0
        b = dims[n] - rk_out - ranks[n + 1][p]
        print(f"H_{n} mod {p}: dim {b}", end="; ")
    print()
