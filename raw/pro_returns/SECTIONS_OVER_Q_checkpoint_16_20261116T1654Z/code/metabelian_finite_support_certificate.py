#!/usr/bin/env python3
"""Exact finite checks for A.178.

The graph is the actual (Z/n)^2 cover of the tripod spine.  Boundary
columns trace x^n, y^n, and (xy)^(-n).  Smith form checks the integral
boundary module, not only its rational rank.  The other checks verify
the displayed surface-cover and literal Fermat transition identities.
They do not compute an infinite section set or replace the cited
finite-descent theorem.
"""
from pathlib import Path
from collections import deque
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

HERE = Path(__file__).resolve().parent
graph_rows = []
for n in range(2, 10):
    vertices = [(i, j) for i in range(n) for j in range(n)]
    index = {v: k for k, v in enumerate(vertices)}
    edges = [(v, a) for v in vertices for a in (0, 1)]
    eindex = {e: k for k, e in enumerate(edges)}

    def step(v, a):
        return ((v[0] + (a == 0)) % n,
                (v[1] + (a == 1)) % n)

    seen, todo = {(0, 0)}, deque([(0, 0)])
    while todo:
        v = todo.popleft()
        for a in (0, 1):
            w = step(v, a)
            if w not in seen:
                seen.add(w)
                todo.append(w)
    assert len(seen) == n*n

    incidence = sp.zeros(n*n, 2*n*n)
    for k, (v, a) in enumerate(edges):
        incidence[index[v], k] -= 1
        incidence[index[step(v, a)], k] += 1

    columns = []
    for j in range(n):
        v, chain = (0, j), [0]*(2*n*n)
        for _ in range(n):
            chain[eindex[(v, 0)]] += 1
            v = step(v, 0)
        assert v == (0, j)
        columns.append(chain)
    for i in range(n):
        v, chain = (i, 0), [0]*(2*n*n)
        for _ in range(n):
            chain[eindex[(v, 1)]] += 1
            v = step(v, 1)
        assert v == (i, 0)
        columns.append(chain)
    # The n diagonal orbits represent the n infinity branches.
    # Negating the closed positive (xy)^n path gives the homology
    # class of the actual meridian (xy)^(-n).
    for i in range(n):
        v, chain = (i, 0), [0]*(2*n*n)
        for _ in range(n):
            for a in (0, 1):
                chain[eindex[(v, a)]] -= 1
                v = step(v, a)
        assert v == (i, 0)
        columns.append(chain)

    boundary = sp.Matrix(2*n*n, 3*n,
                         lambda i, j: columns[j][i])
    assert incidence*boundary == sp.zeros(n*n, 3*n)
    assert boundary*sp.ones(3*n, 1) == sp.zeros(2*n*n, 1)
    assert incidence.rank() == n*n-1
    snf = smith_normal_form(boundary, domain=ZZ)
    factors = [abs(int(snf[i, i]))
               for i in range(min(snf.shape)) if snf[i, i]]
    assert factors == [1]*(3*n-1)
    affine_rank = 2*n*n - (n*n-1)
    compact_rank = affine_rank - len(factors)
    assert compact_rank == (n-1)*(n-2)
    graph_rows.append({
        "n": n, "vertices": n*n, "directed_generator_edges": 2*n*n,
        "boundary_points": 3*n,
        "affine_homology_rank": affine_rank,
        "nonzero_boundary_smith_factors": factors,
        "compact_homology_rank": compact_rank,
        "proper_genus": compact_rank//2,
    })

surface_rows = []
for g in range(7):
    for r in range(10):
        if 2*g-2+r <= 0:
            continue
        for n in (3, 6, 12, 30):
            d = 2*g if r <= 1 else 2*g+r-1
            degree = n**d
            if r == 0:
                boundary_count = 0
                rh = degree*(2*g-2)
                inertia_order = None
            elif r == 1:
                boundary_count = degree
                rh = degree*(2*g-2)
                inertia_order = 1
            else:
                boundary_count = r*(degree//n)
                rh = degree*(2*g-2) + r*(degree//n)*(n-1)
                inertia_order = n
            assert rh % 2 == 0
            genus = 1 + rh//2
            assert genus >= 1
            assert not r or boundary_count >= 2
            assert 2*genus-2+boundary_count == degree*(2*g-2+r)
            surface_rows.append({
                "g": g, "r": r, "n": n, "degree": degree,
                "inertia_order": inertia_order,
                "boundary_count": boundary_count, "proper_genus": genus,
            })

A, B, c, d, e, f, u, v = sp.symbols("A B c d e f u v")
transition_count = 0
for n in range(2, 10):
    for ratio in range(1, 6):
        m = n*ratio
        larger = A*c**n*u**m + B*d**n*v**m - 1
        smaller_pulled_back = A*(c*u**ratio)**n + B*(d*v**ratio)**n - 1
        assert sp.expand(larger-smaller_pulled_back) == 0
        # All three actual tripod boundary functions commute with the map.
        assert sp.cancel(A*(c*u**ratio)**n/(A*c**n*u**m)) == 1
        assert sp.cancel(B*(d*v**ratio)**n/(B*d**n*v**m)) == 1
        assert sp.cancel((1/(A*(c*u**ratio)**n))/
                         (1/(A*c**n*u**m))) == 1
        transition_count += 1

composition_count = 0
for n in range(2, 8):
    for mn in range(1, 5):
        for lm in range(1, 5):
            m, ell = n*mn, n*mn*lm
            composed_u = c*(e*u**lm)**mn
            direct_u = c*e**mn*u**(ell//n)
            composed_v = d*(f*v**lm)**mn
            direct_v = d*f**mn*v**(ell//n)
            assert sp.expand(composed_u-direct_u) == 0
            assert sp.expand(composed_v-direct_v) == 0
            assert sp.expand((A*c**n)*e**m
                             - A*(c*e**mn)**n) == 0
            assert sp.expand((B*d**n)*f**m
                             - B*(d*f**mn)**n) == 0
            composition_count += 1

out = {
    "tripod_graphs": graph_rows,
    "surface_cover_cases": surface_rows,
    "literal_fermat_transition_cases": transition_count,
    "literal_transition_compositions": composition_count,
    "scope": (
        "Exact finite cover graphs, integral boundary lattices, genus counts "
        "and polynomial maps. The all-field section theorem uses the written "
        "descent, cohomology and profinite compactness proof."
    ),
}
(HERE/"metabelian_finite_support_certificate_data.json").write_text(
    json.dumps(out, indent=2)+"\n")
print("PASS:", len(graph_rows),
      "actual tripod cover graphs and primitive integral boundary lattices")
print("PASS:", len(surface_rows),
      "exact hyperbolic surface degree/genus/boundary cases")
print("PASS:", transition_count,
      "literal Fermat cover maps, including all three boundary functions")
print("PASS:", composition_count,
      "compatible root-function and coefficient transition compositions")
print("PASS: n=3 tripod ranks (affine,boundary,proper) = (10,8,2)")
