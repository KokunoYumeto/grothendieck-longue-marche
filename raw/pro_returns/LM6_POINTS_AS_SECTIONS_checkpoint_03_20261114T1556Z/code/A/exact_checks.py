"""Independent exact certificates for Part A of LM6.

No archived executable is imported.  All arithmetic is exact, in finite
groups, integer free-associative algebras, or rational matrices.  The finite
tests verify the stated certificates; they do not assert an infinite lifting
or anabelian theorem.
"""
import itertools
import json
from collections import deque
from pathlib import Path
import sympy as sp


def permutation_checks():
    S3 = list(itertools.permutations(range(3)))
    one = (0, 1, 2)
    mul = lambda a, b: tuple(a[b[i]] for i in range(3))
    inv = lambda a: tuple(a.index(i) for i in range(3))
    conj = lambda a, b: mul(mul(a, b), inv(a))
    mu = (1, 0, 2)
    # rho=f=f_i=id, a=1, mu_i=1.  The corrected a'=mu^{-1}.
    correct = all(conj(inv(mu), conj(mu, g)) == g for g in S3)
    printed = all(conj(one, conj(mu, g)) == g for g in S3)
    assert correct and not printed
    return {"group_order": 6, "corrected_naturality": correct,
            "printed_formula_naturality": printed,
            "mu": mu, "corrected_a_prime": inv(mu)}


def add(a, b):
    z = a.copy()
    for w, c in b.items():
        z[w] = z.get(w, 0) + c
        if not z[w]:
            del z[w]
    return z


def scale(a, n):
    return {w: n*c for w, c in a.items() if n*c}


def prod(a, b):
    z = {}
    for u, c in a.items():
        for v, d in b.items():
            z[u+v] = z.get(u+v, 0) + c*d
    return {w: c for w, c in z.items() if c}


def bracket(a, b):
    return add(prod(a, b), scale(prod(b, a), -1))


def derive(a, dx, dy):
    z = {}
    for w, c in a.items():
        for i, ch in enumerate(w):
            d = dx if ch == 'x' else dy
            z = add(z, {w[:i]+v+w[i+1:]: c*k for v, k in d.items()})
    return z


def lyndon(w):
    return all(w < w[i:] for i in range(1, len(w)))


def lyndon_bracket(w):
    if len(w) == 1:
        return {w: 1}
    for i in range(1, len(w)):
        if lyndon(w[i:]):
            return bracket(lyndon_bracket(w[:i]), lyndon_bracket(w[i:]))
    raise AssertionError(w)


def lie_checks():
    x, y = {'x': 1}, {'y': 1}
    ad = lambda v: bracket(x, v)
    v1 = ad(y)
    v2 = ad(v1)
    v3 = ad(v2)
    v4 = ad(v3)
    ex = v4
    ey = add(bracket(y, v3), scale(bracket(v1, v2), -1))
    tx = add(derive(ex, y, {}), scale(ey, -1))
    ty = derive(ey, y, {})
    target_x = add(scale(lyndon_bracket('xxxyy'), -2),
                   scale(lyndon_bracket('xxyxy'), -1))
    target_y = add(scale(lyndon_bracket('xxyyy'), 2),
                   scale(lyndon_bracket('xyxyy'), 3))
    assert tx == target_x and ty == target_y
    assert not derive(v1, tx, ty)
    source = [lyndon_bracket(''.join(w)) for w in itertools.product('xy', repeat=4)
              if ''.join(w).count('x') == 2 and lyndon(''.join(w))]
    columns = [bracket(x, a) for a in source]
    rows = sorted(set().union(*(set(a) for a in columns+[tx])))
    matrix = sp.Matrix([[a.get(w, 0) for a in columns] for w in rows])
    augmented = matrix.row_join(sp.Matrix([tx.get(w, 0) for w in rows]))
    assert matrix.rank() == 1 and augmented.rank() == 2
    kernels = []
    # An actual finite-degree audit, not a replacement for LM8 G.8.
    for n in range(1, 8):
        basis = [lyndon_bracket(''.join(w)) for w in itertools.product('xy', repeat=n)
                 if lyndon(''.join(w))]
        images = [derive(a, tx, ty) for a in basis]
        rows = sorted(set().union(*(set(a) for a in images)))
        m = sp.Matrix([[a.get(w, 0) for a in images] for w in rows])
        rank = m.rank() if rows else 0
        nullity = len(basis)-rank
        assert nullity == (1 if n == 2 else 0)
        kernels.append({"degree": n, "dimension": len(basis), "rank": rank,
                        "kernel_dimension": nullity})
    return {"T_x": tx, "T_y": ty, "T_boundary": {},
            "rank_ad_x_L_4_bidegree_3_2": matrix.rank(),
            "rank_after_adding_T_x": augmented.rank(), "kernel_checks": kernels}


# F_25 = F_5[z]/(z^2+z+1), represented by (a,b) = a+b*z.
F = list(itertools.product(range(5), repeat=2))
zero, one, zeta = (0, 0), (1, 0), (0, 1)


def fa(a, b):
    return ((a[0]+b[0]) % 5, (a[1]+b[1]) % 5)


def fn(a):
    return ((-a[0]) % 5, (-a[1]) % 5)


def fm(a, b):
    return ((a[0]*b[0]-a[1]*b[1]) % 5,
            (a[0]*b[1]+a[1]*b[0]-a[1]*b[1]) % 5)


Z = [one, zeta, fm(zeta, zeta)]
G = [(v, i) for v in F for i in range(3)]
identity = (zero, 0)


def gm(a, b):
    return (fa(a[0], fm(Z[a[1]], b[0])), (a[1]+b[1]) % 3)


def gi(a):
    return (fn(fm(Z[-a[1] % 3], a[0])), -a[1] % 3)


def gc(a, b):
    return gm(gm(a, b), gi(a))


def phi(a):
    return (fn(a[0]), a[1])


def metabelian_checks():
    assert all(gm(gm(a, b), c) == gm(a, gm(b, c))
               for a in G for b in G for c in G)
    assert all(gm(a, gi(a)) == identity == gm(gi(a), a) for a in G)
    assert all(phi(gm(a, b)) == gm(phi(a), phi(b)) for a in G for b in G)
    assert all(phi(phi(a)) == a for a in G)
    assert any(phi(a) != a for a in G)
    x, y = (zero, 1), (one, 1)
    generated = {identity}
    q = deque([identity])
    generators = [x, y, gi(x), gi(y)]
    while q:
        a = q.popleft()
        for b in generators:
            c = gm(a, b)
            if c not in generated:
                generated.add(c); q.append(c)
    assert len(generated) == 75
    c = gm(gm(gm(x, y), gi(x)), gi(y))
    r, s = (1, 1), zeta
    f, h = (fm(r, c[0]), 0), (fm(s, c[0]), 0)
    assert f == ((3, 4), 0) and h == ((4, 3), 0)
    assert phi(x) == x
    assert phi(y) == gc(gi(f), y)
    assert phi(gm(x, y)) == gc(gi(h), gm(x, y))
    assert gm(f, phi(f)) == identity == gm(h, phi(h))
    inners = [tuple(gc(a, b) for b in G) for a in G]
    assert tuple(phi(a) for a in G) not in inners
    # Every automorphism has a normalizer-of-C3 linear part (48 possibilities)
    # and a translation of a complement (25 possibilities).  Verify the 1200
    # explicit maps and their commutators with phi, up to inner automorphism.
    auto_count = 0
    for alpha in F:
        if alpha == zero:
            continue
        for epsilon in (1, -1):
            def linear(v):
                vv = v if epsilon == 1 else fm(fm(fm(fm(v, v), v), v), v)
                return fm(alpha, vv)
            for translation in F:
                t = (translation, 0)
                def autom(a):
                    return gc(t, (linear(a[0]), epsilon*a[1] % 3))
                vals = [autom(a) for a in G]
                assert len(set(vals)) == 75
                invvals = {b: a for a, b in zip(G, vals)}
                # phi a phi^{-1} a^{-1}
                comm = tuple(phi(autom(phi(invvals[a]))) for a in G)
                assert comm in inners
                auto_count += 1
    assert auto_count == 1200
    return {"order": 75, "associativity_triples": 75**3,
            "automorphism_pairs": 75**2, "generators_generate": len(generated),
            "c": c, "r": r, "s": s, "f": f, "h": h,
            "phi_order": 2, "phi_inner": False,
            "peripheral_conjugacy_and_norms": True,
            "automorphisms_outer_commuting_with_phi": auto_count}


def main():
    output = {"naturality": permutation_checks(), "lie": lie_checks(),
              "metabelian_order_75": metabelian_checks(),
              "scope": "Exact finite certificates and degree <= 7 Lie checks only."}
    dest = Path(__file__).with_name('exact_checks_output.json')
    dest.write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps({"written": str(dest), "all_assertions_passed": True,
                      "lie_degrees": 7, "finite_group_order": 75}))


if __name__ == '__main__':
    main()
