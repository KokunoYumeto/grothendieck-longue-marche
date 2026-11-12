# check_psl27.py -- own check for B.f5/B.f7 of the LM2 return (Claude, Fable 5.2, 12 Nov 2026; none of the return's code was run).
# Generating pairs (x, y) of PSL_2(F_7) modulo Aut = PGL_2(F_7): their number, and their distribution over the
# types (order x, order y, order xy). A Galois element acts on these classes through the type-preserving permutations
# after the cyclotomic twist, so the types with more than one class are where the arithmetic image is not determined
# by the branch-cycle argument.
import itertools, collections
p = 7
def norm(m):
    a, b, c, d = m; n = tuple((-v) % p for v in m)
    return min(m, n)
def mul(m, n):
    a, b, c, d = m; e, f, g, h = n
    return norm(((a*e + b*g) % p, (a*f + b*h) % p, (c*e + d*g) % p, (c*f + d*h) % p))
G = sorted({norm((a, b, c, d)) for a in range(p) for b in range(p) for c in range(p) for d in range(p) if (a*d - b*c) % p == 1})
I = norm((1, 0, 0, 1))
def order(m):
    n, x = 1, m
    while x != I: x = mul(x, m); n += 1
    return n
ORD = {g: order(g) for g in G}
GL = [(a, b, c, d) for a in range(p) for b in range(p) for c in range(p) for d in range(p) if (a*d - b*c) % p]
def conj(g, m):
    a, b, c, d = g; det = (a*d - b*c) % p; di = pow(det, -1, p)
    gi = ((d*di) % p, (-b*di) % p, (-c*di) % p, (a*di) % p)
    def mm(u, v): return ((u[0]*v[0] + u[1]*v[2]) % p, (u[0]*v[1] + u[1]*v[3]) % p, (u[2]*v[0] + u[3]*v[2]) % p, (u[2]*v[1] + u[3]*v[3]) % p)
    return norm(mm(mm(g, m), gi))
# PGL_2 representatives
PGL = sorted({min(tuple((k*v) % p for v in g) for k in range(1, p)) for g in GL})
def generated(x, y):
    S = {I}; fr = [I]
    while fr:
        nw = []
        for g in fr:
            for h in (x, y):
                k = mul(g, h)
                if k not in S: S.add(k); nw.append(k)
        fr = nw
        if len(S) > 24: pass
    return len(S)
lines = []
def P(*a):
    s = " ".join(str(x) for x in a); lines.append(s); print(s)
P("|PSL_2(F_7)| =", len(G), " |PGL_2(F_7)| =", len(PGL))
seen = set(); classes = []
for x in G:
    for y in G:
        if (x, y) in seen: continue
        orb = {(conj(g, x), conj(g, y)) for g in PGL}
        seen |= orb
        if generated(x, y) == len(G): classes.append((x, y, len(orb)))
P("generating pairs modulo Aut:", len(classes), " (all orbits free:", all(c[2] == len(PGL) for c in classes), ")")
types = collections.Counter((ORD[x], ORD[y], ORD[mul(x, y)]) for x, y, _ in classes)
P("types (order x, order y, order xy) with the number of classes:")
for t in sorted(types): P("  ", t, types[t])
uns = collections.Counter(tuple(sorted(t)) for t in types.elements())
P("unordered types:", dict(sorted(uns.items())))
P("types with exactly one class:", sum(1 for t in types if types[t] == 1), "of", len(types), "; classes in types with more than one class:", sum(v for v in types.values() if v > 1))
open(__file__.replace(".py", ".out"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
