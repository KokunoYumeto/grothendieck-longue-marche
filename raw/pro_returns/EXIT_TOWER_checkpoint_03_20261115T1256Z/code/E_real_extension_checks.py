"""Exact finite checks for E.18 and E.19, without a group-theory package."""
import json
from pathlib import Path


def mul(x, y):
    # (i,e) means r^i t^e in D_8, with trt=r^{-1}.
    i, e = x
    j, f = y
    return ((i + (-1) ** e * j) % 4, (e + f) % 2)


elts = [(i, e) for i in range(4) for e in range(2)]
unit = (0, 0)
inverse = {x: next(y for y in elts if mul(x, y) == unit) for x in elts}
P = [(i, 0) for i in range(4)]
K = [(0, 0), (2, 0)]
tau = (0, 1)


def conj(g, x):
    return mul(mul(g, x), inverse[g])


alpha = {g: conj(tau, g) for g in P}
cocycles = [k for k in K if mul(k, alpha[k]) == unit]
classes = [sorted({mul(mul(b, k), inverse[alpha[b]]) for b in K})
           for k in cocycles]
classes = sorted({tuple(c) for c in classes})
action_r = [mul(mul((1, 0), k), inverse[alpha[(1, 0)]]) for k in cocycles]
centralizer = [g for g in P if conj(g, tau) == tau]
assert classes == [((0, 0),), ((2, 0),)]
assert action_r == [(2, 0), (0, 0)]
assert centralizer == K


def mm(a, b, p):
    return tuple(sum(a[2*i+k] * b[2*k+j] for k in range(2)) % p
                 for i in range(2) for j in range(2))


def inv(a, p):
    return (a[3] % p, -a[1] % p, -a[2] % p, a[0] % p)


def sl(p):
    return [(a, b, c, d) for a in range(p) for b in range(p)
            for c in range(p) for d in range(p) if (a*d-b*c) % p == 1]


p = 5
A = (1, 1, 0, 1)
Ainv = inv(A, p)
same_conjugacy = [g for g in sl(p) if mm(mm(g, A, p), inv(g, p), p) == Ainv]
# -1 is a square mod 5, so this particular quotient does not distinguish
# positive and inverse transvections. Mod 3 does.
p = 3
positive_vs_inverse = [g for g in sl(p)
    if mm(mm(g, A, p), inv(g, p), p) == inv(A, p)]
assert not positive_vs_inverse

out = {
    'D8': {'P_order': len(P), 'K_order': len(K),
           'H1_classes': classes, 'r_action_on_representatives': action_r,
           'centralizer_in_P': centralizer, 'centralizer_image_in_Q_order': 1},
    'SL2_F3_positive_twist_not_conjugate_to_inverse': not positive_vs_inverse,
    'SL2_F5_warning_conjugators_exist': len(same_conjugacy),
}
print(json.dumps(out, indent=2))
Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2) + '\n')
