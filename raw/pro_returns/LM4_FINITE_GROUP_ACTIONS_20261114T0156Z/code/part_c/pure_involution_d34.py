#!/usr/bin/env python3
"""Exact incidence, norm-orbit and cyclic-cover certificates for D.34."""
from collections import Counter
from itertools import product
import json
from pathlib import Path

from three_cusp_rank_d32 import cycles, inverse, rref


def crt(values, moduli):
    modulus = 1
    for m in moduli:
        modulus *= m
    answer = 0
    for a, m in zip(values, moduli):
        cofactor = modulus//m
        answer += a*cofactor*pow(cofactor, -1, m)
    return answer % modulus


def local_normalizer_checks():
    moduli = (8, 9, 5)
    modulus = 360
    e2 = crt((1, 0, 0), moduli)
    records = []
    for signs in product((-1, 1), repeat=2):
        lam = crt((-1,)+signs, moduli)
        image = {(1-lam)*v % modulus for v in range(modulus)}
        choices = [range(m) if sign == 1 else (0,)
                   for sign, m in zip((-1,)+signs, moduli)]
        tests = 0
        for coords in product(*choices):
            v = crt(coords, moduli)
            assert (lam-1)*v % modulus == 0
            roots = {u for u in range(modulus) if ((1+lam)*u+v) % modulus == 0}
            assert roots
            orbits = []
            remaining = set(roots)
            while remaining:
                u = min(remaining)
                orbit = {(u+w) % modulus for w in image}
                assert orbit <= roots
                orbits.append(orbit)
                remaining -= orbit
            assert len(orbits) == 2
            representative = min(roots)
            assert (representative+e2) % modulus in roots
            assert not any(representative in orbit and (representative+e2) % modulus in orbit
                           for orbit in orbits)
            tests += 1
        records.append({"prime_coordinates": [2, 3, 5],
                        "signs": [-1]+list(signs), "modulus": modulus,
                        "lambda_modulus": lam, "admissible_square_parameters": tests,
                        "section_orbits_for_each": 2})
    return records


def unique_cusp_relations():
    checks = []
    for n in range(3, 13):
        vectors = [1 << i for i in range(n-1)] + [(1 << (n-1))-1]
        zero_subsets = []
        for subset in range(1 << n):
            total = 0
            for i, vector in enumerate(vectors):
                if subset >> i & 1:
                    total ^= vector
            if total == 0:
                zero_subsets.append(subset)
        assert zero_subsets == [0, (1 << n)-1]
        matrix = [[(v >> j) & 1 for j in range(n-1)] for v in vectors]
        assert len(rref(matrix, 2)[1]) == n-1
        # A standard n-cycle realizes exactly these edge differences.
        vertices = [0]
        for vector in vectors[:-1]:
            vertices.append(vertices[-1] ^ vector)
        assert len(set(vertices)) == n
        assert all((vertices[i] ^ vertices[(i+1) % n]) == vectors[i]
                   for i in range(n))
        checks.append({"cusp_count": n, "homology_rank": n-1,
                       "zero_subsets": ["empty", "all"],
                       "cycle_vertex_vectors": vertices})
    return checks


def cycle_type(perm):
    return sorted(len(c) for c in cycles(perm))


def cyclic_cover_checks():
    checks = []
    for q in (3, 5, 7, 11, 13, 17, 19):
        x = tuple((i+1) % q for i in range(q))
        y = tuple(range(q))
        z = inverse(x)
        boundaries = ([{"cusp": "x", "vertices": c, "degree": len(c)} for c in cycles(x)]
                      +[{"cusp": "z", "vertices": c, "degree": len(c)} for c in cycles(z)]
                      +[{"cusp": "y", "vertices": c, "degree": len(c)} for c in cycles(y)])
        n = len(boundaries)
        assert n == q+2 and (q+2-n)//2 == 0
        deck = [0, 1]+[2+(i+1) % q for i in range(q)]
        assert cycle_type(deck) == [1, 1, q]
        # Exact automorphisms of the n-cycle, on its edge set.
        automorphisms = set()
        for shift in range(n):
            automorphisms.add(tuple((i+shift) % n for i in range(n)))
            automorphisms.add(tuple((shift-i) % n for i in range(n)))
        assert len(automorphisms) == 2*n
        assert (2*n) % q != 0
        assert all(cycle_type(a) != [1, 1, q] for a in automorphisms)
        # In the normalized quotient, f has x-character0 and lambda1,
        # so alpha fixes every index of the q y-boundary lifts.
        alpha_on_y_lifts = [(1*i-0) % q for i in range(q)]
        assert alpha_on_y_lifts == list(range(q))
        checks.append({"prime": q, "cover_degree": q,
                       "boundary_count": n, "genus": 0,
                       "boundaries": boundaries,
                       "deck_edge_permutation": deck,
                       "deck_cycle_type": [1, 1, q],
                       "cycle_automorphism_group_order": 2*n,
                       "compatible_cycle_automorphisms": 0,
                       "alpha_on_y_lifts_under_hypothetical_plus_sign": alpha_on_y_lifts})
    return checks


def main():
    result = {
        "claim": "D.34", "status": "passed",
        "normalizer_section_orbits": local_normalizer_checks(),
        "unique_binary_cusp_relations": unique_cusp_relations(),
        "cyclic_cover_obstructions": cyclic_cover_checks(),
        "triangle_section_vectors": {"s": [0, 0, 1],
                                      "x_e2_s": [1, 0, 1],
                                      "y_e2_f_s": [0, 1, 1],
                                      "f_s": [0, 0, 1]},
        "logical_limit": "Finite norm calculations use square parameters allowed by the full-coordinate proof; they do not promote spurious finite-coordinate 2-torsion. The all-prime exclusion and graph classification are proved in d34.tex.",
    }
    destination = Path(__file__).with_name("pure_involution_d34_output.json")
    destination.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "passed",
                      "normalizer_parameter_checks": sum(r["admissible_square_parameters"]
                                                         for r in result["normalizer_section_orbits"]),
                      "cusp_relation_sizes": [r["cusp_count"] for r in result["unique_binary_cusp_relations"]],
                      "cyclic_cover_primes": [r["prime"] for r in result["cyclic_cover_obstructions"]],
                      "output": str(destination)}, indent=2))


if __name__ == "__main__":
    main()
