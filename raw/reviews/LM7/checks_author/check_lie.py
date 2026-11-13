# Review checks for LM7_FERMAT_TOWER: free Lie algebra computations (D.11, D.21, E.3, E.4).
# Author: Claude Fable 5.2 (effort max), 13 Nov 2026. Own code; the return's code was not run.
# Elements of degree n of Q<x,y> are integer arrays of length 2^n (x=0, y=1, first letter most significant).
# Ranks are computed modulo two primes (a rank mod p never exceeds the rational rank; equality of both
# with the return's value and with the nullity counts is reported).
# Run: python -I -B check_lie.py > check_lie.out
import numpy as np, sys
from math import comb

PRIMES = (2147483629, 2147483587)

def tens(a, b, P=None):
    c = np.multiply.outer(a, b).ravel()
    return c % P if P else c
def br(a, b, P=None):
    c = tens(a, b) - tens(b, a)
    return c % P if P else c
X1 = np.array([1, 0], dtype=np.int64); Y1 = np.array([0, 1], dtype=np.int64)

def lyndon_words(n):
    # Duval: all Lyndon words over {0,1} of length <= n
    out = []; w = [-1]
    while w:
        w[-1] += 1
        out.append(tuple(w))
        m = len(w)
        while len(w) < n: w.append(w[len(w) - m])
        while w and w[-1] == 1: w.pop()
    return out
def std_fact(w, lyn):
    for i in range(1, len(w)):
        if w[i:] in lyn: return w[:i], w[i:]
def lie_bases(nmax, P):
    lw = lyndon_words(nmax); lyn = set(lw); val = {}
    for w in sorted(lw, key=len):
        if len(w) == 1: val[w] = (X1 if w[0] == 0 else Y1).copy()
        else:
            u, v = std_fact(w, lyn); val[w] = br(val[u], val[v], P)
    return {n: [val[w] for w in lw if len(w) == n] for n in range(1, nmax + 1)}

def left_null(M, P):
    # rows of M: vectors; returns basis of {c : c M = 0} mod P and the rank
    M = M.copy() % P; r, cols = M.shape
    T = np.eye(r, dtype=np.int64); piv = 0; used = []
    for c in range(cols):
        if piv == r: break
        nz = np.nonzero(M[piv:, c])[0]
        if len(nz) == 0: continue
        k = piv + nz[0]
        if k != piv:
            M[[piv, k]] = M[[k, piv]]; T[[piv, k]] = T[[k, piv]]
        inv = pow(int(M[piv, c]), -1, P)
        M[piv] = (M[piv] * inv) % P; T[piv] = (T[piv] * inv) % P
        f = M[:, c].copy(); f[piv] = 0
        idx = np.nonzero(f)[0]
        if len(idx):
            M[idx] = (M[idx] - np.multiply.outer(f[idx], M[piv]) % P) % P
            T[idx] = (T[idx] - np.multiply.outer(f[idx], T[piv]) % P) % P
        piv += 1
    return T[piv:], piv
def rank(M, P):
    if M.shape[0] == 0: return 0
    return left_null(M, P)[1]

def lincomb(coefs, B, P):
    # sum of coefs[i]*B[i] mod P, reduced at every step (no int64 overflow)
    out = np.zeros_like(B[0])
    for i, c in enumerate(coefs):
        if c: out = (out + (int(c) * B[i]) % P) % P
    return out
def swap(a): return a[::-1].copy()
def subst(a, n, P):
    # x -> -x-y, y -> y on every tensor factor
    t = a.reshape((2,) * n)
    for ax in range(n):
        t = np.moveaxis(t, ax, 0)
        t = np.stack([(-t[0]) % P, (t[1] - t[0]) % P])
        t = np.moveaxis(t, 0, ax)
    return t.reshape(-1)
def meta(f, n, P):
    # ab(f_y): words ending in y, last letter stripped, as a polynomial in X,Y of degree n-1; index = power of Y
    out = np.zeros(n, dtype=np.int64)
    for i in np.nonzero(f)[0]:
        if i & 1: out[bin(int(i) >> 1).count("1")] += f[i]
    return out % P

NMAX = 10
table = {}
for P in PRIMES:
    L = lie_bases(NMAX, P)
    XY = (X1 + Y1) % P
    rows = []
    for n in range(1, NMAX + 1):
        B = L[n]; d = len(B)
        # special: [f,y] - [g,x+y] = 0
        M = np.array([br(b, Y1, P) for b in B] + [(-br(b, XY, P)) % P for b in B], dtype=np.int64)
        null, _ = left_null(M, P)
        fs = [lincomb(v[:d], B, P) for v in null]
        coef = np.array([v[:d] for v in null], dtype=np.int64) if len(null) else np.zeros((0, d), dtype=np.int64)
        if n == 1:   # weight 1: f=x gives the inner derivation ad(x)-type solution g: remove inner ones
            sp = 0; spm = 0; fs = []
        else:
            sp = rank(coef, P)
            spm = rank(np.array([meta(f, n, P) for f in fs], dtype=np.int64), P) if fs else 0
        # S3-invariant: f(x,y)+f(y,x)=0 and [x,f]-[x+y,f(-x-y,y)]=0
        Mi = np.array([np.concatenate([(b + swap(b)) % P, (br(X1, b, P) - br(XY, subst(b, n, P), P)) % P]) for b in B], dtype=np.int64)
        nulli, _ = left_null(Mi, P)
        fi = [lincomb(v, B, P) for v in nulli]
        inv = len(nulli)
        if n == 1: inv = 0; fi = []   # weight 1: only the inner derivation
        invm = rank(np.array([meta(f, n, P) for f in fi], dtype=np.int64), P) if fi else 0
        # is the invariant space inside the special space?
        inside = (rank(np.vstack([coef, nulli]), P) == sp) if (inv and n > 1) else True
        extra = {}
        if n >= 3 and n % 2 == 1 and fi:
            # gamma line: X*p with p=((X+Y)^n-X^n-Y^n)/(XY): coefficient of X^(n-1-k) Y^k is C(n,k+1), k=0..n-2
            g = np.array([comb(n, k + 1) % P for k in range(n - 1)] + [0], dtype=np.int64)
            Mm = np.array([meta(f, n, P) for f in fi], dtype=np.int64)
            extra["gamma_in_inv_image"] = rank(np.vstack([Mm, g]), P) == invm
            if n == 9:
                # X * X^2 Y^2 (X+Y)^3 = X^3 Y^2 (X+Y)^3: coefficient of Y^(2+j) is C(3,j)
                e = np.zeros(n, dtype=np.int64)
                for j in range(4): e[2 + j] = comb(3, j)
                extra["X2Y2(X+Y)^3_in_inv_image"] = rank(np.vstack([Mm, e]), P) == invm
                extra["independent_of_gamma"] = rank(np.vstack([g, e]), P) == 2
        if n >= 3 and fs:
            # special metabelian image inside (X+Y)*poly: X*p vanishes at Y=-X
            ev = [int(sum(int(c) * (-1) ** k for k, c in enumerate(meta(f, n, P)))) % P for f in fs]
            extra["special_image_divisible_by_X+Y"] = all(x == 0 for x in ev)
        rows.append((n, d, sp, spm, inv, invm, inside, extra))
    table[P] = rows
print("weight n | dim L_n | special outer | its metabelian image | S3-invariant | its metabelian image | invariant inside special | extra")
for a, b in zip(table[PRIMES[0]], table[PRIMES[1]]):
    assert a[:6] == b[:6], (a, b)
    print(a)
print("return D.11:   special 0,0,1,0,3,0,6,4,13,12 ; image 0,0,1,0,3,0,5,0,7,0 ; invariant 0,0,1,0,1,0,2,1,4,2 ; image 0,0,1,0,1,0,1,0,2,0")
print("mine:          special", ",".join(str(r[2]) for r in table[PRIMES[0]]), "; image", ",".join(str(r[3]) for r in table[PRIMES[0]]),
      "; invariant", ",".join(str(r[4]) for r in table[PRIMES[0]]), "; image", ",".join(str(r[5]) for r in table[PRIMES[0]]))

print()
print("== E.3 / E.4: Ihara bracket of depth-one generators, exact integers")
def adx(k):
    a = Y1.copy()
    for _ in range(k): a = br(X1, a)
    return a
def unit(n, idx):
    u = np.zeros(2 ** n, dtype=np.int64) if n else np.array([0], dtype=np.int64)
    if n == 0: return np.array([1], dtype=np.int64)
    u[idx] = 1; return u
def D(f, g, ng):
    # derivation D_f: x -> 0, y -> [y,f], applied to g (every word of g has exactly one y)
    yf = br(Y1, f); out = None
    for i in np.nonzero(g)[0]:
        bits = [(int(i) >> (ng - 1 - k)) & 1 for k in range(ng)]
        pos = bits.index(1); assert sum(bits) == 1
        t = tens(tens(unit(pos, 0), yf), unit(ng - 1 - pos, 0)) * int(g[i])
        out = t if out is None else out + t
    return out
def ihara(kf, kg):
    f, g = adx(kf), adx(kg)
    return br(f, g) + D(f, g, kg + 1) - D(g, f, kf + 1)
rel = ihara(2, 8) - 3 * ihara(4, 6)
print("{s3,s9} - 3{s5,s7} == 0 exactly:", not rel.any())
print("{s3,s5} != 0:", bool(ihara(2, 4).any()), "; {s3,s7} != 0:", bool(ihara(2, 6).any()))
P = PRIMES[0]
for w, pairs in ((8, [(2, 4)]), (10, [(2, 6)]), (12, [(2, 8), (4, 6)]), (14, [(2, 10), (4, 8)])):
    M = np.array([ihara(a, b) % P for a, b in pairs], dtype=np.int64)
    print("weight %d: pairs %s, rank of depth-two brackets = %d" % (w, [(a + 1, b + 1) for a, b in pairs], rank(M, P)))
