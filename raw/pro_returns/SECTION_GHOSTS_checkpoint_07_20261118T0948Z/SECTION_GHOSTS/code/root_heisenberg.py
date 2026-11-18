"""Exhaustive small Heisenberg certificates and Riemann--Hurwitz data.

The proof in the paper is symbolic for every odd prime.  This program
independently enumerates the exceptional group at two and small examples.
No external data or packages are required.
"""
from itertools import product
from collections import Counter, deque


def check(p):
    elements = list(product(range(p), repeat=3))
    identity = (0, 0, 0)
    x, y = (1, 0, 0), (0, 1, 0)

    def mul(u, v):
        a, b, c = u
        d, e, f = v
        return ((a+d) % p, (b+e) % p, (c+f+a*e) % p)

    def inv(u):
        a, b, c = u
        return ((-a) % p, (-b) % p, (-c+a*b) % p)

    def order(u):
        z = identity
        for n in range(1, p*p+1):
            z = mul(z, u)
            if z == identity:
                return n
        raise AssertionError("order bound exceeded")

    seen, todo = {identity}, deque([identity])
    while todo:
        z = todo.popleft()
        for generator in (x, y):
            nxt = mul(z, generator)
            if nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
    assert len(seen) == p**3
    for u in elements:
        assert mul(u, inv(u)) == identity
    center = [u for u in elements if all(mul(u, v) == mul(v, u) for v in (x, y))]
    assert center == [(0, 0, c) for c in range(p)]
    commutator = mul(mul(mul(x, y), inv(x)), inv(y))
    assert commutator == (0, 0, 1)
    branches = (x, y, inv(mul(x, y)))
    branch_orders = tuple(order(u) for u in branches)
    cycle_counts = tuple(len(elements)//n for n in branch_orders)
    twice_genus = 2+len(elements)-sum(cycle_counts)
    assert twice_genus % 2 == 0
    genus = twice_genus//2
    expected = 0 if p == 2 else 1+p*p*(p-3)//2
    assert genus == expected
    orders = dict(sorted(Counter(order(u) for u in elements).items()))
    print(f"p={p}: order={len(elements)}, center={len(center)}, element orders={orders}, "
          f"branch orders={branch_orders}, boundary={sum(cycle_counts)}, genus={genus}")


if __name__ == "__main__":
    for p in (2, 3, 5, 7, 11):
        check(p)
    print("All exhaustive group, inertia, and genus assertions passed.")
