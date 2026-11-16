#!/usr/bin/env python3
"""Finite checks for the uniform elementary proof in A.56.

The proof itself covers every ell >= 5.  This script independently enumerates
SL(2,F_ell), generates the normal closure of the indicated q-power element,
and checks that its order is the full group order for ell=5,7,11,13.
No simplicity/classification library is used.
"""

from collections import deque


def prime_divisors(n):
    out = []
    p = 2
    while p*p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.append(n)
    return out


for ell in (5, 7, 11, 13):
    I = (1, 0, 0, 1)

    def mul(a, b):
        return ((a[0]*b[0]+a[1]*b[2]) % ell,
                (a[0]*b[1]+a[1]*b[3]) % ell,
                (a[2]*b[0]+a[3]*b[2]) % ell,
                (a[2]*b[1]+a[3]*b[3]) % ell)

    def inv(a):
        return (a[3], -a[1] % ell, -a[2] % ell, a[0])

    def power(a, n):
        b = I
        while n:
            if n & 1:
                b = mul(b, a)
            a = mul(a, a)
            n //= 2
        return b

    def group_generated(gens):
        seen = {I}
        queue = deque([I])
        while queue:
            a = queue.popleft()
            for b in gens:
                c = mul(a, b)
                if c not in seen:
                    seen.add(c)
                    queue.append(c)
        return seen

    U = lambda t: (1, t % ell, 0, 1)
    L = lambda t: (1, 0, t % ell, 1)
    W = (0, -1 % ell, 1, 0)
    S = group_generated([U(1), L(1)])
    assert len(S) == ell*(ell*ell-1)
    assert all((a*d-b*c) % ell == 1 for a,b,c,d in S)
    D2 = (2, 0, 0, pow(2, -1, ell))
    for t in range(ell):
        assert mul(mul(mul(D2, U(t)), inv(D2)), inv(U(t))) == U(3*t)
        assert mul(mul(mul(D2, L(t)), inv(D2)), inv(L(t))) == L((pow(4,-1,ell)-1)*t)
    print(f"ell={ell}, group_order={len(S)}, perfectness identities: verified")
    for q in prime_divisors(len(S)):
        if q == 2:
            D, order, kind = W, 4, "W of order four"
        elif q == ell:
            D, order, kind = U(1), ell, "upper unipotent"
        elif (ell-1) % q == 0:
            a = next(a for a in range(2,ell) if pow(a,q,ell) == 1)
            D, order, kind = (a,0,0,pow(a,-1,ell)), q, "split Cartan"
        else:
            assert (ell+1) % q == 0
            D = next(mul(W,U(t)) for t in range(ell)
                     if power(mul(W,U(t)),q) == I and mul(W,U(t)) != I)
            order, kind = q, "nonsplit companion matrix"
        assert power(D,order) == I and D != I
        assert all(power(D,order//p) != I for p in prime_divisors(order))
        conjugates = {mul(mul(g,D),inv(g)) for g in S}
        normal_closure = group_generated(sorted(conjugates))
        assert normal_closure == S
        print(f"  q={q}, element={D}, order={order}, type={kind}, "
              f"normal_closure_order={len(normal_closure)}")
print("All finite group checks passed.")
