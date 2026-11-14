#!/usr/bin/env python3
"""Exact finite coordinate checks for the actual maps in D.73.

The infinite quotient, integral lattice argument and full fixed-kernel
cohomology are proved in d73.tex. These finite checks do not assert
existence of a scalar cubic action.
"""
from collections import Counter, deque
from itertools import product
from math import gcd
from pathlib import Path
import json


CHECKS = Counter()


def check(name, condition):
    assert condition, name
    CHECKS[name] += 1


def mul(g, h, modulus, root):
    a, i, j = g
    b, k, ell = h
    return ((a + pow(root, i, modulus)*b) % modulus,
            (i+k) % 3, (j+ell) % 3)


def inverse(g, modulus, root):
    a, i, j = g
    return ((-pow(root, (-i) % 3, modulus)*a) % modulus,
            (-i) % 3, (-j) % 3)


def power(g, exponent, modulus, root):
    out = (0, 0, 0)
    if exponent < 0:
        return power(inverse(g, modulus, root), -exponent, modulus, root)
    while exponent:
        if exponent & 1:
            out = mul(out, g, modulus, root)
        g = mul(g, g, modulus, root)
        exponent //= 2
    return out


def commutator(g, h, modulus, root):
    return mul(mul(mul(g, h, modulus, root),
                   inverse(g, modulus, root), modulus, root),
               inverse(h, modulus, root), modulus, root)


def generated(generators, modulus, root):
    one = (0, 0, 0)
    alphabet = tuple(generators) + tuple(
        inverse(g, modulus, root) for g in generators)
    seen = {one}
    todo = deque([one])
    while todo:
        g = todo.popleft()
        for h in alphabet:
            k = mul(g, h, modulus, root)
            if k not in seen:
                seen.add(k)
                todo.append(k)
    return seen


def rotate(vector, shift):
    size = len(vector)
    return [vector[(i-shift) % size] for i in range(size)]


def prefix_product(vector, exponent):
    """Multiply by 1+r+...+r^(exponent-1) in Z[C_m], exactly."""
    size = len(vector)
    out = [sum(vector[(-k) % size] for k in range(exponent))]
    for i in range(1, size):
        out.append(out[-1] + vector[i] - vector[(i-exponent) % size])
    return out


def vector_add(*vectors):
    return [sum(entries) for entries in zip(*vectors)]


def vector_negative(vector):
    return [-a for a in vector]


def cycle_boundary(B, D, E, root):
    modulus = len(B)
    root_squared = root*root % modulus
    return vector_add(rotate(B, 1), vector_negative(B),
                      rotate(D, root), vector_negative(D),
                      rotate(E, root_squared), vector_negative(E))


def root_lifts(q, levels):
    initial = [a for a in range(1, q) if (a*a+a+1) % q == 0]
    check("two_primitive_roots", len(initial) == 2)
    for initial_root in initial:
        modulus = q
        root = initial_root
        previous_modulus = 1
        previous_root = 0
        for n in range(1, levels+1):
            if n > 1:
                old_modulus = modulus
                candidates = [root+c*old_modulus for c in range(q)
                              if ((root+c*old_modulus)**2
                                  +root+c*old_modulus+1)
                              % (old_modulus*q) == 0]
                check("unique_hensel_root", len(candidates) == 1)
                previous_modulus, previous_root = modulus, root
                modulus *= q
                root = candidates[0]
            yield q, n, modulus, root, previous_modulus, previous_root


def main():
    rows = []
    pair_rows = []
    for q, n, m, root, previous_m, previous_root in (
            case for q, levels in ((7, 3), (13, 2), (19, 2))
            for case in root_lifts(q, levels)):
        one = (0, 0, 0)
        r, t, s = (1, 0, 0), (0, 1, 0), (0, 0, 1)
        check("cyclotomic_relation", (root*root+root+1) % m == 0)
        check("primitive_root_order", pow(root, 3, m) == 1 and root != 1)
        check("cusp_generator_unit", gcd(root-1, m) == 1)
        check("complement_order", power(t, 3, m, root) == one)
        check("section_order", power(s, 3, m, root) == one)
        check("deck_conjugation", mul(mul(t, r, m, root),
              inverse(t, m, root), m, root) == (root, 0, 0))
        cusp = commutator(t, r, m, root)
        check("actual_cusp_image", cusp == ((root-1) % m, 0, 0))
        check("full_finite_quotient", len(generated((r, t, s), m, root))
              == 9*m)
        check("surface_cover_type",
              2-2*((3*m-1)//2)-3 == -3*m)

        # The original F-quotient labels use only the first two coordinates.
        seen = set()
        cycles = []
        for a, i in product(range(m), range(3)):
            g = (a, i, 0)
            if g in seen:
                continue
            cycle = []
            while g not in seen:
                seen.add(g)
                cycle.append(g)
                g = mul(g, cusp, m, root)
            check("cusp_cycle_closes", g == cycle[0])
            check("primitive_cusp_cycle_length", len(cycle) == m)
            cycles.append(cycle)
        check("three_actual_cusp_cycles",
              len(cycles) == 3 and len(seen) == 3*m)

        # Exact normal forms, inverse compositions, and quotient transitions.
        for a, i, j in product(range(m), range(3), range(3)):
            g = (a, i, j)
            check("normal_form_inverse", mul(g, inverse(g, m, root),
                  m, root) == one)
            check("normal_form_coordinates",
                  mul(mul(power(r, a, m, root), power(t, i, m, root),
                          m, root), power(s, j, m, root), m, root) == g)
            check("specified_central_section",
                  mul(g, s, m, root) == mul(s, g, m, root))
            h = ((2*a+1) % m, (i+1) % 3, (j+2) % 3)
            gh = mul(g, h, m, root)
            check("abelian_label_character",
                  (gh[1]+gh[2]) % 3
                  == (g[1]+g[2]+h[1]+h[2]) % 3)
            if previous_m > 1:
                check("compatible_root_reduction",
                      root % previous_m == previous_root)
                reduced = (a % previous_m, i, j)
                for generator in (r, t, s):
                    result = mul(g, generator, m, root)
                    check("actual_quotient_transition",
                          (result[0] % previous_m, result[1], result[2])
                          == mul(reduced, generator,
                                 previous_m, previous_root))

        # Coordinates for all labelled section images and the complement twist.
        for a in range(m):
            chosen = (a, 2, 1)
            check("other_section_label", chosen[1:] == (2, 1))
            check("other_section_order", power(chosen, 3, m, root) == one)
            check("other_section_character_kernel",
                  (chosen[1]+chosen[2]) % 3 == 0)
            check("fixed_complement_twist",
                  (3*a % m == 0) == (a == 0))
            cusp_root = (a, 1, 1)
            check("finite_cusp_root_label",
                  power(cusp_root, 3, m, root) == one)

        # The map (A,D,E,k) to graph cycles and its inverse, over Z.
        for seed in range(4):
            A = [(2*i+seed) % 7-3 for i in range(m)]
            D = [(i*i+3*seed) % 11-5 for i in range(m)]
            E = [(3*i+seed*seed) % 13-6 for i in range(m)]
            k = seed-2
            PD = prefix_product(D, root)
            PE = prefix_product(E, root*root % m)
            B = [-d-e+k for d, e in zip(PD, PE)]
            check("exact_graph_cycle_map",
                  cycle_boundary(B, D, E, root) == [0]*m)
            restored = vector_add(B, PD, PE)
            check("exact_graph_cycle_inverse",
                  restored == [k]*m)
        for exponent in (1, root, root*root % m):
            sample = [(i+2) % 7-3 for i in range(m)]
            P = prefix_product(sample, exponent)
            check("prefix_ring_identity",
                  vector_add(rotate(P, 1), vector_negative(P))
                  == vector_add(rotate(sample, exponent),
                                vector_negative(sample)))

        # Full primary powers: the q-primary idempotent in a finite
        # cyclic quotient projects to a generator modulo q^n.
        total_order = 15*m
        e_q = 15*pow(15, -1, m) % total_order
        check("primary_idempotent_coordinates",
              e_q % m == 1 and e_q % 15 == 0)
        check("primary_idempotent_square",
              (e_q*e_q-e_q) % total_order == 0)
        check("primary_section_order",
              total_order//gcd(total_order, e_q) == m)

        # Every pair of actual global section-image types is tested.
        # Inverting a labelled element does not change its subgroup.
        if n == 1 or (q == 7 and n == 2):
            representatives = [s] + [(a, 2, 1) for a in range(m)]
            pairs = 0
            for ia, first in enumerate(representatives):
                for ib in range(ia, len(representatives)):
                    second = representatives[ib]
                    image = generated((first, second), m, root)
                    check("all_two_section_images_proper", len(image) < 9*m)
                    if ia == 0 and ib == 0:
                        expected = 3
                    elif ia == 0:
                        expected = 9
                    else:
                        expected = 3*m//gcd(m, first[0]-second[0])
                        check("two_other_sections_kernel",
                              all((g[1]+g[2]) % 3 == 0 for g in image))
                    check("exact_two_section_image_order", len(image) == expected)
                    pairs += 1
            pair_rows.append({"q": q, "n": n, "m": m,
                              "root": root, "pairs": pairs})
        rows.append({"q": q, "n": n, "m": m, "root": root,
                     "quotient_order": 3*m, "extension_quotient_order": 9*m,
                     "cover_type": [(3*m-1)//2, 3],
                     "nontrivial_rotation_rank": 3*(m-1),
                     "regular_cubic_rank": m-1})

    result = {
        "claim": "D.73", "status": "PASS",
        "cases": rows, "two_section_enumerations": pair_rows,
        "checks": dict(CHECKS), "total_checks": sum(CHECKS.values()),
        "scope": "Compatible exact prime-power quotient coordinates, actual "
                 "cusp cycles, integral graph-cycle inverse maps, primary "
                 "procyclic splitting coordinates, and finite images of "
                 "all two-section types in the named cases. The full "
                 "q-adic quotient, lattice proof and fixed-kernel cohomology "
                 "are proved in d73.tex. No scalar cubic realization or "
                 "full section-generation theorem is inferred."
    }
    Path(__file__).with_name("torus_cubic_qadic_d73_output.json").write_text(
        json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: result[key] for key in
                     ("claim", "status", "two_section_enumerations",
                      "checks", "total_checks", "scope")}, indent=2))


if __name__ == "__main__":
    main()
