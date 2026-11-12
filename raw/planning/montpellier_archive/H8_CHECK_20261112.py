import itertools
from math import comb
from collections import Counter

def basis(g, i):
    return [frozenset(c) for c in itertools.combinations(range(2 * g), i)]

def lef_matrix(g, i):
    # theta^[g-i] wedge - : Lambda^i(Z^2g) -> Lambda^(2g-i)(Z^2g), theta = sum e_j f_j, basis order e_1 f_1 e_2 f_2 ...
    k = g - i
    src = basis(g, i)
    tgt = basis(g, 2 * g - i)
    tidx = {b: n for n, b in enumerate(tgt)}
    M = [[0] * len(src) for _ in tgt]
    for col, b in enumerate(src):
        free = [j for j in range(g) if 2 * j not in b and 2 * j + 1 not in b]
        for J in itertools.combinations(free, k):
            nb = set(b)
            for j in J:
                nb.add(2 * j)
                nb.add(2 * j + 1)
            M[tidx[frozenset(nb)]][col] += 1
    return M

def diag_form(M):
    A = [row[:] for row in M]
    m = len(A)
    n = len(A[0]) if m else 0
    diag = []
    t = 0
    while t < min(m, n):
        best = None
        for i in range(t, m):
            Ai = A[i]
            for j in range(t, n):
                v = Ai[j]
                if v and (best is None or abs(v) < best[0]):
                    best = (abs(v), i, j)
                    if best[0] == 1:
                        break
            if best and best[0] == 1:
                break
        if best is None:
            break
        _, i0, j0 = best
        A[t], A[i0] = A[i0], A[t]
        for row in A:
            row[t], row[j0] = row[j0], row[t]
        while True:
            changed = False
            p = A[t][t]
            for i in range(t + 1, m):
                if A[i][t]:
                    q = A[i][t] // p
                    Ai = A[i]
                    At = A[t]
                    for j in range(t, n):
                        Ai[j] -= q * At[j]
                    if A[i][t]:
                        A[t], A[i] = A[i], A[t]
                        changed = True
                        break
            if changed:
                continue
            p = A[t][t]
            for j in range(t + 1, n):
                if A[t][j]:
                    q = A[t][j] // p
                    for i in range(t, m):
                        A[i][j] -= q * A[i][t]
                    if A[t][j]:
                        for row in A:
                            row[t], row[j] = row[j], row[t]
                        changed = True
                        break
            if not changed:
                break
        diag.append(abs(A[t][t]))
        t += 1
    return diag

def prime_powers(ds):
    out = Counter()
    for d in ds:
        x = d
        q = 2
        while x > 1:
            if x % q == 0:
                e = 0
                while x % q == 0:
                    x //= q
                    e += 1
                out[q ** e] += 1
            q += 1
    return out

def predicted(g, i):
    out = []
    for s in range(0, i + 1):
        if (i - s) % 2:
            continue
        p = (i - s) // 2
        if s + p > g:
            continue
        v = g - s
        k = p + (g - i)
        if k > v:
            continue
        mult_S = comb(g, s) * 2 ** s
        for j in range(0, p + 1):
            d = comb(k - j, p - j)
            mm = comb(v, j) - (comb(v, j - 1) if j >= 1 else 0)
            if d > 1 and mm > 0:
                out += [d] * (mm * mult_S)
    return out

for g in range(2, 7):
    for i in range(0, g + 1):
        if g == 6 and i >= 4:
            continue
        M = lef_matrix(g, i)
        d = diag_form(M)
        full_rank = len(d) == len(M) and all(d)
        got = prime_powers([x for x in d if x > 1])
        exp = prime_powers(predicted(g, i))
        order = 1
        for x in d:
            order *= x
        print(f"g={g} i={i} size={len(M)} full_rank_over_Q={full_rank} |coker|={order} "
              f"coker_prime_powers={dict(sorted(got.items()))} matches_Wilson_prediction={got == exp}")
