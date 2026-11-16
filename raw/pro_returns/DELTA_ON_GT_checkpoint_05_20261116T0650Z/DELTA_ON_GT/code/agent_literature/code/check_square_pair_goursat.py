"""Independent exact permutation check of the square-pair comparison.

This checks a joint word-evaluation quotient only. It asserts neither
gentle relations nor a lift satisfying the full profinite pentagon.
"""
from collections import deque
from itertools import permutations
import json

I = (0, 1, 2, 3)
p = (1, 2, 0, 3)  # (123)
t = (1, 2, 3, 0)  # (1234)

def mul(a, b):
    return tuple(a[b[i]] for i in range(4))

def inv(a):
    return tuple(a.index(i) for i in range(4))

def comm(a, b):
    return mul(mul(mul(a, b), inv(a)), inv(b))

def order(a):
    b = I
    for n in range(1, 25):
        b = mul(b, a)
        if b == I:
            return n
    raise AssertionError("Unexpected order")

def closure(gens, identity=I, multiply=mul):
    seen = {identity}
    queue = deque([identity])
    while queue:
        a = queue.popleft()
        for b in gens:
            c = multiply(a, b)
            if c not in seen:
                seen.add(c)
                queue.append(c)
    return seen

def derived(group):
    return closure({comm(a, b) for a in group for b in group})

t2 = mul(t, t)
S = closure((p, t))
A = closure((p, t2))
assert len(S) == 24 and len(A) == 12
assert (order(p), order(t), order(mul(p, t))) == (3, 4, 4)
assert (order(p), order(t2), order(mul(p, t2))) == (3, 2, 3)
pairmul = lambda a, b: (mul(a[0], b[0]), mul(a[1], b[1]))
pairinv = lambda a: (inv(a[0]), inv(a[1]))
paircomm = lambda a, b: pairmul(pairmul(pairmul(a, b), pairinv(a)), pairinv(b))
J = closure(((p, p), (t, t2)), (I, I), pairmul)
J1 = closure({paircomm(a, b) for a in J for b in J}, (I, I), pairmul)
J2 = closure({paircomm(a, b) for a in J1 for b in J1}, (I, I), pairmul)
assert len(J) == 288
assert J1 == {(a, b) for a in derived(S) for b in derived(A)}
assert len(J1) == 48
assert J2 == {(a, I) for a in derived(derived(S))}
assert len(J2) == 4
c1, c2 = comm(p, t), comm(p, t2)
w1 = comm(c1, mul(mul(p, c1), inv(p)))
w2 = comm(c2, mul(mul(p, c2), inv(p)))
assert w1 != I and w2 == I
print(json.dumps({
    "status": "PASS",
    "square_pair_orders": [3, 2, 3],
    "unsquared_pair_orders": [3, 4, 4],
    "individual_image_orders": [len(S), len(A)],
    "joint_derived_series_orders": [len(J), len(J1), len(J2), 1],
    "witness_word": "[[x,y], x[x,y]x^-1]",
    "witness_images_zero_based": [w1, w2],
    "scope": "Word-evaluation quotient only; no gentle or full-GT lift asserted."
}, indent=2))
