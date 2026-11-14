#!/usr/bin/env python3
"""Exact finite GT_0 shadow checks; Python standard library only.

The finite groups are the dihedral GT-shadows of Bortnovskyi--Dolgushev--
Holikov--Pashkovskyi, arXiv:2405.11725v3, Proposition 4.5. No assertion that a
finite-order shadow lifts to finite-order GT_0 is made. The refinement
calculation explicitly imposes the order bound at the deeper level.
"""
from collections import Counter, deque
from itertools import product
from math import gcd
import json
from pathlib import Path
import csv


def nu(u):
    return (u - 1) // 4 if u % 4 == 1 else (u + 1) // 4


def shadows(n):
    assert n >= 4 and n % 2 == 0
    return [(k, u) for k in range(n // 2) for u in range(2 * n)
            if gcd(u, 2 * n) == 1 and
            (n % 4 != 0 or (k - nu(u)) % 2 == 0)]


def mul(n, a, b):
    return ((a[0] + a[1] * b[0]) % (n // 2), a[1] * b[1] % (2 * n))


def inv(n, a):
    v = pow(a[1], -1, 2 * n)
    return ((-v * a[0]) % (n // 2), v)


def power(n, a, d):
    result = (0, 1)
    while d:
        if d & 1:
            result = mul(n, result, a)
        a = mul(n, a, a)
        d //= 2
    return result


def reduce_to(n, a):
    return (a[0] % (n // 2), a[1] % (2 * n))


def conjugacy_classes(n, subset):
    group = shadows(n)
    remaining = set(subset)
    answer = []
    while remaining:
        a = min(remaining)
        orbit = {mul(n, mul(n, h, a), inv(n, h)) for h in group}
        assert orbit <= remaining
        answer.append({"representative": a, "size": len(orbit)})
        remaining -= orbit
    return answer


def refine(n, q, d):
    assert q % n == 0
    lower = shadows(n)
    upper = shadows(q)
    lower_roots = {a for a in lower if power(n, a, d) == (0, 1)}
    upper_roots = [a for a in upper if power(q, a, d) == (0, 1)]
    fibers = Counter(reduce_to(n, a) for a in upper_roots)
    assert set(fibers) <= lower_roots
    assert {reduce_to(n, a) for a in upper} == set(lower)
    return {"n": n, "q": q, "order_bound": d,
            "lower_group_order": len(lower), "upper_group_order": len(upper),
            "lower_nonidentity_roots": len(lower_roots) - 1,
            "upper_nonidentity_roots": len(upper_roots) - 1,
            "lower_nonidentity_roots_with_bounded_order_lift":
                sum(1 for a in lower_roots if a != (0, 1) and fibers[a]),
            "bounded_order_fiber_size_histogram": dict(sorted(Counter(
                fibers[a] for a in lower_roots if a != (0, 1)).items())),
            "eliminated_nonidentity_elements": sorted(a for a in lower_roots
                if a != (0, 1) and not fibers[a])}


class DihedralCube:
    """Three copies of D_n; coordinate r^a s^b is (a,b)."""
    def __init__(self, n):
        self.n = n
        self.one = ((0, 0),) * 3
        self.x = ((1, 0), (0, 1), (0, 1))
        self.y = ((1, 1), (1, 0), (1, 1))
        self.z = self.inv(self.mul(self.x, self.y))

    def mul(self, a, b):
        return tuple(((x + (-1 if e else 1) * y) % self.n, (e + f) % 2)
                     for (x, e), (y, f) in zip(a, b))

    def inv(self, a):
        return tuple((((1 if e else -1) * x) % self.n, e) for x, e in a)

    def power(self, a, d):
        if d < 0:
            a, d = self.inv(a), -d
        r = self.one
        while d:
            if d & 1:
                r = self.mul(r, a)
            a = self.mul(a, a)
            d //= 2
        return r

    def generated(self, generators):
        seen = {self.one}
        queue = deque([self.one])
        while queue:
            a = queue.popleft()
            for g in generators:
                b = self.mul(a, g)
                if b not in seen:
                    seen.add(b)
                    queue.append(b)
        return seen

    def generator_map(self, generator_images):
        """Prove descent by every labelled Cayley edge, and prove bijectivity."""
        original = (self.x, self.y)
        mapping = {self.one: self.one}
        queue = deque([self.one])
        while queue:
            a = queue.popleft()
            for g, image in zip(original, generator_images):
                b = self.mul(a, g)
                image_b = self.mul(mapping[a], image)
                if b in mapping:
                    assert mapping[b] == image_b
                else:
                    mapping[b] = image_b
                    queue.append(b)
        assert len(set(mapping.values())) == len(mapping)
        return mapping


def direct_check(n):
    cube = DihedralCube(n)
    theta = cube.generator_map((cube.y, cube.x))
    tau = cube.generator_map((cube.y, cube.z))
    group = set(theta)
    # Normal closure of [x,y] is the commutator subgroup of this two-generator G.
    comm = cube.mul(cube.mul(cube.mul(cube.x, cube.y), cube.inv(cube.x)),
                    cube.inv(cube.y))
    conjugates = [cube.mul(cube.mul(g, comm), cube.inv(g)) for g in group]
    derived = cube.generated(set(conjugates))
    checked = 0
    direct_pairs = set()
    # Exhaust all m and the commutator subgroup, then test both cycle relations.
    # Their equivalence to the two braid hexagons is DG Proposition 3.4.
    for m in range(n):
        if gcd(2 * m + 1, n) != 1:
            continue
        for f in derived:
            if cube.mul(theta[f], f) != cube.one:
                continue
            h = cube.mul(cube.power(cube.y, m), f)
            if cube.mul(cube.mul(tau[tau[h]], tau[h]), h) != cube.one:
                continue
            automorphism = cube.generator_map((cube.power(cube.x, 2 * m + 1),
                cube.mul(cube.mul(cube.inv(f), cube.power(cube.y, 2 * m + 1)), f)))
            assert len(automorphism) == len(group)
            direct_pairs.add((m, f))
            checked += 1
    formula_pairs = set()
    for k, u in shadows(n):
        m = (u - 1) // 2
        kappa = m + 1 if m % 2 else -m
        f = ((2*k % n, 0), (-2*k % n, 0), (kappa % n, 0))
        formula_pairs.add((m, f))
    assert direct_pairs == formula_pairs
    # Exhibit nonnilpotence when n/2 has an odd factor: projection to D_(n/2).
    # The output records a direct noncommutation in D_odd, between Sylow parts.
    odd = n
    while odd % 2 == 0:
        odd //= 2
    witness = None if odd == 1 else {"quotient": f"D_{odd}",
        "rotation_order": odd, "reflection_order": 2,
        "s_r_s_inverse_rotation_exponent": (-1) % odd,
        "r_rotation_exponent": 1}
    return {"n": n, "F2_quotient_order": len(group),
            "derived_subgroup_order": len(derived),
            "shadow_order_from_exhaustive_relations": checked,
            "cycle_equations_and_all_Cayley_edges_checked": True,
            "matches_affine_formula": True, "nonnilpotence_witness": witness}


def algebra_check(n):
    group = shadows(n)
    lookup = set(group)
    for a in group:
        assert mul(n, a, inv(n, a)) == (0, 1)
        assert inv(n, a) in lookup
        for b in group:
            assert mul(n, a, b) in lookup
    if len(group) <= 32:
        for a, b, c in product(group, repeat=3):
            assert mul(n, mul(n, a, b), c) == mul(n, a, mul(n, b, c))
    return {"n": n, "order": len(group), "closure_and_inverse_checked": True,
            "associativity_exhaustive": len(group) <= 32,
            "associativity_general_proof": "(k+u*l+u*v*t,u*v*w) on both sides"}


def alternating_quotient_check():
    """An explicit F2 quotient outside the metabelian dihedral family."""
    one = tuple(range(5))
    a = (1, 2, 3, 4, 0)
    b = (1, 2, 0, 3, 4)
    def compose(p, q):
        return tuple(p[q[i]] for i in range(5))
    def inverse(p):
        q = [0] * 5
        for i, j in enumerate(p):
            q[j] = i
        return tuple(q)
    def generated(gens):
        seen = {one}
        queue = deque([one])
        while queue:
            p = queue.popleft()
            for q in gens:
                r = compose(p, q)
                if r not in seen:
                    seen.add(r)
                    queue.append(r)
        return seen
    group = generated((a, b))
    commutators = {compose(compose(compose(p, q), inverse(p)), inverse(q))
                   for p in group for q in group}
    derived = generated(commutators)
    assert len(group) == 60 and derived == group
    return {"x_image": "(1 2 3 4 5)", "y_image": "(1 2 3)",
            "image_order": len(group), "derived_subgroup_order": len(derived),
            "perfect_nontrivial": True,
            "conclusion": "No metabelian dihedral F2 quotient can surject onto this image."}


def main():
    out = {
        "description": "Exact bounded-order refinements in isolated dihedral GT_0 shadows",
        "source": "arXiv:2405.11725v3, Theorem 4.3 and Proposition 4.5",
        "direct_quotient_checks": [direct_check(n) for n in (4, 6, 8, 12, 14)],
        "affine_group_checks": [algebra_check(n) for n in (4, 6, 8, 12, 14, 18, 32)],
        "bounded_order_refinements": [refine(n, q, d)
            for n, q in ((6, 18), (18, 54), (54, 162),
                         (14, 98), (4, 8), (8, 16), (16, 32), (32, 64))
            for d in (2, 3)],
        "small_involution_conjugacy": {
            str(n): conjugacy_classes(n, [a for a in shadows(n)
                if a != (0, 1) and power(n, a, 2) == (0, 1)])
            for n in (4, 8, 16, 32)},
        "noncofinality_quotient": alternating_quotient_check(),
        "logical_scope": [
            "A surviving finite shadow has not been proved to lift to finite-order GT_0.",
            "Every lift of an eliminated shadow has order not dividing the tested bound.",
            "The dihedral family is not cofinal among all isolated finite shadows.",
            "Order-bounded lifting over all isolated refinements is required for full GT_0 torsion."
        ]
    }
    path = Path(__file__).with_name("gt_shadow_refinement_output.json")
    path.write_text(json.dumps(out, indent=2) + "\n")
    csv_path = Path(__file__).with_name("gt_shadow_refinement_table.csv")
    fields = ["n", "q", "order_bound", "lower_group_order", "upper_group_order",
              "lower_nonidentity_roots", "upper_nonidentity_roots",
              "lower_nonidentity_roots_with_bounded_order_lift"]
    with csv_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(out["bounded_order_refinements"])
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
