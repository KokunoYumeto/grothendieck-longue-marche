#!/usr/bin/env python3
"""Exact finite shadows of C3:573--582, independent of GT/Galois images.

Enumerate the full matrix group and all automorphisms from the images of
its two generators.  Every right Cayley edge is checked.  No automorphism
classification or source image assertion is used by the computation.
"""
from collections import deque, Counter
from itertools import product
from math import gcd
from pathlib import Path
import json

OUT = Path(__file__).resolve().parent


def model(n):
    mats = sorted(a for a in product(range(n), repeat=4)
                  if (a[0]*a[3]-a[1]*a[2]) % n == 1)
    ix = {a: i for i, a in enumerate(mats)}
    N = len(mats)

    def rawmul(a, b):
        return ((a[0]*b[0]+a[1]*b[2]) % n,
                (a[0]*b[1]+a[1]*b[3]) % n,
                (a[2]*b[0]+a[3]*b[2]) % n,
                (a[2]*b[1]+a[3]*b[3]) % n)

    m = [[ix[rawmul(a, b)] for b in mats] for a in mats]
    inv = [ix[(a[3], -a[1] % n, -a[2] % n, a[0])] for a in mats]
    one = ix[(1, 0, 0, 1)]
    omega = ix[((-1) % n, 0, 0, (-1) % n)]
    r = ix[(0, 1, n-1, 1)]
    s = ix[(0, n-1, 1, 0)]

    def power(a, k):
        b = one
        for _ in range(k):
            b = m[b][a]
        return b

    def cyclic(a):
        ans, b = {one}, a
        while b != one:
            ans.add(b)
            b = m[b][a]
        return frozenset(ans)

    def subgroup(gens):
        ans, todo = {one}, deque([one])
        while todo:
            a = todo.popleft()
            for b in gens:
                c = m[a][b]
                if c not in ans:
                    ans.add(c)
                    todo.append(c)
        return frozenset(ans)

    def conj(a, b):
        return m[m[a][b]][inv[a]]

    orders = [len(cyclic(a)) for a in range(N)]
    assert subgroup([r, s]) == frozenset(range(N))
    assert power(r, 3) == power(s, 2) == omega
    center = frozenset(a for a in range(N)
                       if all(m[a][b] == m[b][a] for b in range(N)))
    assert center == {one, omega}
    steps = (r, s, inv[r], inv[s])

    def cayley_map(rp, sp):
        images, todo = {one: one}, deque([one])
        targets = (rp, sp, inv[rp], inv[sp])
        while todo:
            a = todo.popleft()
            for g, h in zip(steps, targets):
                b, y = m[a][g], m[images[a]][h]
                if b in images:
                    if images[b] != y:
                        return None
                else:
                    images[b] = y
                    todo.append(b)
        assert len(images) == N
        if len(set(images.values())) != N:
            return None
        return tuple(images[a] for a in range(N))

    autos = sorted({a for rp in range(N) for sp in range(N)
                    if orders[rp] == orders[r] and orders[sp] == orders[s]
                    if (a := cayley_map(rp, sp)) is not None})
    theta = cayley_map(r, m[omega][s])
    if theta is not None:
        assert all(theta[theta[a]] == a for a in range(N))
    identity = tuple(range(N))
    # Canonical quotient by the actual central involution.
    zcoset = [min(a, m[omega][a]) for a in range(N)]
    qreps = sorted(set(zcoset))
    qix = {a: i for i, a in enumerate(qreps)}
    qimages = {tuple(qix[zcoset[u[a]]] for a in qreps) for u in autos}
    kernel = [u for u in autos if all(zcoset[u[a]] == zcoset[a]
                                     for a in range(N))]
    assert set(kernel) == ({identity, theta} if theta is not None else {identity})
    eps = m[s][r]
    L = cyclic(eps)
    square_L = cyclic(power(eps, 2))
    Lconj = {frozenset(conj(a, b) for b in L) for a in range(N)}
    peripheral_autos = [u for u in autos
                        if frozenset(u[b] for b in L) in Lconj]
    twisted_eps = m[omega][eps]
    theta_preserves_class = cyclic(twisted_eps) in Lconj
    if theta is not None:
        assert all(theta[b] == b for b in square_L)
    rec = dict(modulus=n, group_order=N, center_order=len(center),
               automorphisms=len(autos), quotient_order=len(qreps),
               central_quotient_automorphism_image_order=len(qimages),
               central_quotient_kernel_order=len(kernel),
               central_twist_descends_to_this_quotient=theta is not None,
               central_twist_proposed_generator_images=dict(r=mats[r],s=mats[m[omega][s]]),
               loop_matrix=mats[eps], loop_order=orders[eps],
               twisted_loop_matrix=mats[twisted_eps],
               twisted_loop_order=orders[twisted_eps],
               loop_conjugacy_preserving_automorphisms=len(peripheral_autos),
               central_twist_preserves_loop_subgroup_class=theta_preserves_class,
               square_loop_unaffected_by_central_sign=True,
               automorphism_generator_images=[dict(r=mats[u[r]],s=mats[u[s]]) for u in autos])
    if n == 4:
        Pi = frozenset(a for a, x in enumerate(mats)
                       if tuple(z % 2 for z in x) == (1, 0, 0, 1))
        l0 = m[omega][power(eps, 2)]
        l1 = m[omega][power(m[r][s], 2)]
        Pi0 = subgroup([l0, l1])
        assert len(Pi) == 8 and len(Pi0) == 4
        assert all(conj(a,b) in Pi0 for a in range(N) for b in Pi0)
        assert omega not in Pi0 and Pi == Pi0 | {m[omega][a] for a in Pi0}
        assert all(frozenset(u[a] for a in Pi) == Pi for u in autos)
        # S4 is exhibited by conjugation on the four cyclic order-3 subgroups.
        threes = sorted({cyclic(a) for a in range(N) if orders[a] == 3},
                        key=lambda x: tuple(sorted(x)))
        assert len(threes) == 4
        threes_ix = {a: i for i, a in enumerate(threes)}
        perms = [tuple(threes_ix[frozenset(conj(a,b) for b in H)]
                       for H in threes) for a in range(N)]
        assert len(set(perms)) == 24
        assert {a for a in range(N) if perms[a] == tuple(range(4))} == center
        # The four C3 subgroups also show Aut(S4)=Inn(S4): its induced
        # permutation action is faithful since these C3 subgroups generate.
        # The code only needs the exact 24 induced automorphisms above.
        tau = tuple(ix[(x[0], -x[1] % n, -x[2] % n, x[3])] for x in mats)
        assert tau in autos
        assert all(tau[tau[a]] == a for a in range(N))
        assert frozenset(tau[a] for a in Pi0) == Pi0
        classes = {a: {conj(b,a) for b in range(N)}
                   for a in (r, inv[r], s, inv[s])}
        units = [1,5,7,11]
        normalized = []
        Zpairs = []
        for ai,u in enumerate(autos):
            for mu in units:
                er = 1 if mu % 3 == 1 else -1
                es = 1 if mu % 4 == 1 else -1
                if (u[eps] == power(eps,mu)
                        and u[r] in classes[r if er == 1 else inv[r]]
                        and u[s] in classes[s if es == 1 else inv[s]]):
                    Zpairs.append((ai,mu))
                    acts_trivially_on_mod2 = all(
                        tuple(z % 2 for z in mats[u[a]]) ==
                        tuple(z % 2 for z in mats[a]) for a in range(N))
                    if not acts_trivially_on_mod2:
                        continue
                    alpha = [(a,t) for a in Pi0 for t in (0,1)
                             if conj(a, tau[r] if t else r) == u[r]]
                    beta = [b for b in Pi0
                            if (conj(b,s) if es == 1 else m[omega][conj(b,s)]) == u[s]]
                    normalized.append(dict(automorphism_index=ai,multiplier=mu,
                        alpha_solutions=[dict(matrix=mats[a],tau_power=t) for a,t in alpha],
                        beta_solutions=[mats[b] for b in beta],
                        required_tau_parity=0 if er == 1 else 1))
        assert len(normalized) == 8
        assert all(sum(a['tau_power'] == x['required_tau_parity']
                       for a in x['alpha_solutions']) == 1
                   and len(x['beta_solutions']) == 2 for x in normalized)
        witness = ix[(1,0,2,1)]
        assert conj(witness,eps) == m[omega][inv[eps]]
        h = ix[(1,2,2,1)]
        assert h != one and h in Pi0 and conj(h,s) == s
        rec.update(Pi_order=len(Pi),Pi0_order=len(Pi0),
                   Pi0_matrices=[mats[a] for a in sorted(Pi0)],
                   quotient_S4_certificate=dict(order3_subgroups=[
                       [mats[a] for a in sorted(H)] for H in threes],
                       r_permutation=perms[r],s_permutation=perms[s],
                       permutation_image_order=len(set(perms)),kernel_order=len(center)),
                   linked_numerical_pairs=len(Zpairs),
                   loop_conjugacy_witness=dict(matrix=mats[witness],
                       conjugated_loop=mats[conj(witness,eps)],
                       equals='minus_inverse_loop'),
                   identity_normalized_beta_ambiguity=[mats[one],mats[h]],
                   normalized_mod2_trivial_pairs=normalized,
                   normalized_alpha_count_after_prescribed_parity=1,
                   normalized_beta_count=2,
                   normalized_solution_multiplicities=dict(Counter(
                       f"alpha={len(x['alpha_solutions'])},beta={len(x['beta_solutions'])}"
                       for x in normalized)))
    return rec


records = [model(3), model(4)]
assert records[0]['loop_order'] == 3
assert records[0]['twisted_loop_order'] == 6
assert records[0]['central_twist_preserves_loop_subgroup_class'] is False
answer = dict(models=records,all_assertions_passed=True,
    scope="Complete automorphism enumerations for SL2(F3),SL2(Z/4); these are not assertions about an arithmetic or GT image.")
(OUT/'AB_modular_comparison.json').write_text(json.dumps(answer,indent=2)+'\n')
for r in records:
    compact={k:v for k,v in r.items() if k not in (
        'automorphism_generator_images','normalized_mod2_trivial_pairs')}
    print(json.dumps(compact,indent=2))
print('ALL MODULAR-COMPARISON ASSERTIONS PASSED')
