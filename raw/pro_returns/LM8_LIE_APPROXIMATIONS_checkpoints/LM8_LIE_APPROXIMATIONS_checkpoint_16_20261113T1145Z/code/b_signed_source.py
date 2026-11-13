#!/usr/bin/env python3
"""Exact certificates for the actual signed source and its first image.

The integral cocycle input is the executed B.24a model, not a table of
assumed automorphisms.  Every displayed finite automorphism is checked
on the full group and all generator edges.  The finite images are
reductions of the proved profinite image; this does not enumerate all
solutions of isolated equations on a finite quotient.
"""
from collections import deque
from itertools import product
from math import gcd
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
source = HERE / "g_signed_fermat2_model.json"
raw = source.read_bytes()
data = json.loads(raw)
reps = data["minimal_representatives"]
acts = data["minimal_actions"]
hmul = data["minimal_multiplication"]
coc = data["minimal_cocycle"]
hi = reps.index([])
hr, hs = reps.index([1]), reps.index([2])
hinv = [next(j for j in range(12) if hmul[i][j] == hi)
        for i in range(12)]


def mv(a, v):
    return tuple(sum(x*y for x, y in zip(row, v)) for row in a)


def finite_model(n):
    one = (hi, 0, 0)
    rho, sigma = (hr, 0, 0), (hs, 0, 0)

    def mul(g, h):
        q, r = g[0], h[0]
        v = mv(acts[q], h[1:])
        return (hmul[q][r], (g[1]+v[0]+coc[q][r][0]) % n,
                (g[2]+v[1]+coc[q][r][1]) % n)

    def inv(g):
        q = g[0]
        v = mv(acts[hinv[q]], (-g[1]-coc[q][hinv[q]][0],
                                  -g[2]-coc[q][hinv[q]][1]))
        ans = (hinv[q], v[0] % n, v[1] % n)
        assert mul(g, ans) == mul(ans, g) == one
        return ans

    def power(g, k):
        if k < 0:
            return power(inv(g), -k)
        ans = one
        while k:
            if k & 1:
                ans = mul(ans, g)
            g = mul(g, g)
            k //= 2
        return ans

    def word(w, r=rho, s=sigma):
        images = {1:r, 2:s, -1:inv(r), -2:inv(s)}
        ans = one
        for letter in w:
            ans = mul(ans, images[letter])
        return ans

    omega = power(rho, 3)
    e0, e1 = mul(sigma, rho), mul(rho, sigma)
    a, b = inv(e0), inv(e1)
    x, y = mul(omega, power(e0, 2)), mul(omega, power(e1, 2))
    assert x == (hi, 1 % n, 0) and y == (hi, 0, 1 % n)
    assert mul(mul(a,b),a) == mul(mul(b,a),b)
    assert mul(a,b) == rho and inv(mul(mul(a,b),a)) == sigma
    elements = [(h, u, v) for h in range(12)
                for u in range(n) for v in range(n)]
    index = {g:i for i,g in enumerate(elements)}
    generators = (rho, sigma, inv(rho), inv(sigma))
    # Verify that the displayed coordinates are the whole generated group.
    found, queue = {one}, deque([one])
    while queue:
        g = queue.popleft()
        for h in generators[:2]:
            gh = mul(g,h)
            if gh not in found:
                found.add(gh)
                queue.append(gh)
    assert found == set(elements)
    order_e0 = next(k for k in range(1,4*n+1) if power(e0,k) == one)
    assert order_e0 == (2*n if n % 2 == 0 else 4*n)
    units = [u for u in range(order_e0) if gcd(u,order_e0) == 1]
    autos = {}
    edge_checks = 0
    for mu in units:
        ap, bp = power(a,mu), power(b,mu)
        rp, sp = mul(ap,bp), inv(mul(mul(ap,bp),ap))
        wp = power(rp,3)
        xp = mul(wp,power(mul(sp,rp),2))
        yp = mul(wp,power(mul(rp,sp),2))
        assert xp == power(x,mu) and yp == power(y,mu)
        rep_images = [word(w,rp,sp) for w in reps]
        images = [mul(mul(power(xp,g[1]),power(yp,g[2])),rep_images[g[0]])
                  for g in elements]
        smu = {g:h for g,h in zip(elements,images)}
        assert len(set(images)) == len(elements)
        for g in elements:
            for h in generators:
                assert smu[mul(g,h)] == mul(smu[g],smu[h])
                edge_checks += 1
        assert smu[e0] == power(e0,mu)
        for r in range(2*n):
            er = power(e0,r)
            eri = inv(er)
            perm = tuple(index[mul(mul(er,smu[g]),eri)] for g in elements)
            autos[r,mu] = perm
    assert len(set(autos.values())) == len(autos) == 2*n*len(units)
    ir, iss = index[rho], index[sigma]
    law_checks = 0
    for (r,mu), p in autos.items():
        for (s,nu), q in autos.items():
            target = autos[(r+mu*s) % (2*n), (mu*nu) % order_e0]
            assert (p[q[ir]],p[q[iss]]) == (target[ir],target[iss])
            law_checks += 1
    # The direct integral cocycle argument can also be exhausted here.
    R, S = ((0,-1),(1,-1)), ((0,1),(1,0))
    cocycles = []
    for A in product(range(n),repeat=2):
        B = tuple((-v) % n for v in mv(S,A))
        if all((v+w) % n == 0 for v,w in zip(B,mv(S,B))):
            assert A == B == (A[0], -A[0] % n)
            cocycles.append((A,B))
    assert len(cocycles) == n
    return {"n":n,"group_order":len(elements),"loop_order":order_e0,
            "loop_inner_order":2*n,"multiplier_image_order":len(units),
            "actual_source_image_order":len(autos),
            "complete_generator_edge_checks":edge_checks,
            "affine_group_law_checks":law_checks,
            "normalized_identity_cocycles":len(cocycles)}


finite_rows = [finite_model(n) for n in range(1,9)]


def pmul(a,b):
    return tuple(a[b[i]] for i in range(len(a)))


def pinv(a):
    return tuple(a.index(i) for i in range(len(a)))


def closure(generators):
    one = tuple(range(len(generators[0])))
    seen, queue = {one}, deque([one])
    while queue:
        a = queue.popleft()
        for b in generators:
            c = pmul(a,b)
            if c not in seen:
                seen.add(c)
                queue.append(c)
    return seen


a5 = closure([(1,2,3,4,0),(1,2,0,3,4)])
assert len(a5) == 60
commutators = {pmul(pmul(pmul(a,b),pinv(a)),pinv(b))
               for a,b in product(a5,repeat=2)}
derived = closure(list(commutators))
center = [a for a in a5 if all(pmul(a,b)==pmul(b,a) for b in a5)]
assert derived == a5 and len(center) == 1

hensel = [{"n":1,"modulus":5,"root":1}]
root, modulus = 1, 5
for k in range(2,13):
    root = next(root+t*modulus for t in range(5)
                if ((root+t*modulus)**2-6) % (5*modulus) == 0)
    modulus *= 5
    assert root % 5 == 1 and (root*root-6) % modulus == 0
    hensel.append({"n":k,"modulus":modulus,"root":root})

result = {
    "status":"PASS",
    "integral_model_input":source.name,
    "integral_model_sha256":hashlib.sha256(raw).hexdigest(),
    "finite_reductions_of_actual_signed_image":finite_rows,
    "A5_formation_counterexample":{
        "degree":5,"generator_images_zero_based":[[1,2,3,4,0],[1,2,0,3,4]],
        "order":60,"derived_order":len(derived),"center_order":len(center),
        "derived_group_nilpotent":False},
    "sqrt6_fifth_adic_Hensel_lifts":hensel,
    "exact_profinite_image":"Zhat semidirect Zhat^times, (r,mu)(s,nu)=(r+mu*s,mu*nu)",
    "scope":["All elements and generator edges checked for each displayed finite reduction.",
             "This is not an enumeration of all isolated finite signed solutions.",
             "Irrationality of sqrt6 and the all-level action assertions are proved in the paper."]}
(HERE/"b_signed_source.json").write_text(json.dumps(result,indent=2)+"\n")
lines = ["PASS: exact reductions of the actual signed-source image.",
         " n | quotient order | loop order | image order | generator edges"]
lines += [f"{r['n']:2} | {r['group_order']:14} | {r['loop_order']:10} | "
          f"{r['actual_source_image_order']:11} | {r['complete_generator_edge_checks']}"
          for r in finite_rows]
lines += ["PASS: all affine composition laws and normalized cocycle fibres.",
          "PASS: A5 order60, derived order60, trivial centre; not nilpotent-by-abelian.",
          "PASS: compatible sqrt6 lifts through modulus5^12, each congruent1 mod5."]
out = "\n".join(lines)+"\n"
(HERE/"b_signed_source.out").write_text(out)
print(out,end="")
