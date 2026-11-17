"""Finite witnesses for the projective pro-odd-kernel model.

These quotients are witnesses for the expressly abstract model in C.2;
they are not claimed to be quotients of a torus involution extension.
"""
from itertools import product


def closure(gens, mul, identity):
    seen = {identity}
    queue = [identity]
    while queue:
        u = queue.pop()
        for v in gens:
            w = mul(u, v)
            if w not in seen:
                seen.add(w)
                queue.append(w)
    return seen


def model(n, m):
    q, e = 3**n, 2**m
    elems = list(product(range(q), range(q), range(e)))
    one = (0, 0, 0)

    def mul(a, b):
        return ((a[0] + b[0]) % q,
                (a[1] + (-1)**a[2] * b[1]) % q,
                (a[2] + b[2]) % e)

    def inv(a):
        return (-a[0] % q, -((-1)**a[2])*a[1] % q, -a[2] % e)

    a, y = (1, 0, 1), (0, 1, 0)
    generated = closure([a, y], mul, one)
    A = closure([a], mul, one)
    kernel = {g for g in elems if g[0] == 0 and g[2] == 0}
    commutators = [mul(mul(mul(g, h), inv(g)), inv(h))
                   for g in elems for h in [a, y]]
    derived = closure(commutators, mul, one)
    assert len(generated) == len(elems)
    assert len(A) == q * e
    assert derived == kernel
    assert len(kernel) == q
    assert A & kernel == {one}
    assert y not in A
    for g in elems:
        assert mul(g, inv(g)) == one
        for h in elems:
            gh = mul(g, h)
            assert gh[0] == (g[0] + h[0]) % q
            assert gh[2] == (g[2] + h[2]) % e

    # The identity coset A is fixed by A and moved by y.  Hence its
    # F_2-basis vector is A-invariant but is not B-invariant.
    cosets, unused = [], set(elems)
    while unused:
        g = next(iter(unused))
        coset = frozenset(mul(g, h) for h in A)
        cosets.append(coset)
        unused -= coset
    identity_coset = frozenset(A)
    assert identity_coset in cosets
    assert all(frozenset(mul(h, k) for k in A) == identity_coset for h in A)
    assert frozenset(mul(y, k) for k in A) != identity_coset
    print(f"n={n}, m={m}: |B|={len(elems)}, |<a,y>|={len(generated)}, "
          f"|A|={len(A)}, |ker chi|=|B'|={len(kernel)}, [B:A]={len(cosets)}; "
          "invariant-surjectivity witness PASS")


if __name__ == "__main__":
    for parameters in [(1, 1), (1, 2), (2, 2)]:
        model(*parameters)
    print("All finite checks passed. Projectivity and all-open-subgroup claims are proved in C.2.")
