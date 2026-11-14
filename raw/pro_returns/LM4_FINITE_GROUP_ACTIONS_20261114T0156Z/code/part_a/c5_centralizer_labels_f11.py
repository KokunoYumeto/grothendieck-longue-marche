#!/usr/bin/env python3
"""Exact icosahedral labels and D10 transports for the C5 kernel in F.11.

Uses the same based coset labels as modular_a5_gt0_f7.py and exact
Q(theta,i) arithmetic from c5_seven_kernel_exact.py.
"""
from itertools import permutations
from pathlib import Path
import json
import modular_a5_gt0_f7 as mod
import c5_seven_kernel_exact as alg


R, C, ZETA, THETA = alg.R, alg.C, alg.ZETA, alg.THETA


def cinverse(value):
    value = C(value)
    norm = (value*value.conjugate()).re
    assert norm != R(0)
    result = C(value.re/norm, -value.im/norm)
    assert value*result == C(1)
    return result


def canonical(matrix):
    scale = cinverse(next(x for x in matrix if x != C(0)))
    return tuple(x*scale for x in matrix)


def mm(left, right):
    a, b, c, d = left
    e, f, g, h = right
    return canonical((a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h))


def mi(matrix):
    a, b, c, d = matrix
    return canonical((d, -b, -c, a))


IDENTITY = canonical((C(1), C(0), C(0), C(1)))


def maps_point(matrix, source, target):
    a, b, c, d = matrix
    num, den = (a, c) if source is None else (a*source+b, c*source+d)
    assert num != C(0) or den != C(0)
    if target is None:
        return den == C(0)
    return num == target*den


def cycles(perm):
    unseen, answer = set(range(len(perm))), []
    while unseen:
        current = start = min(unseen)
        cycle = []
        while current in unseen:
            unseen.remove(current)
            cycle.append(current)
            current = perm[current]
        assert current == start
        answer.append(cycle)
    return answer


def main():
    G = {p for p in permutations(range(5)) if mod.parity(p) == 0}
    a, b = (1, 0, 3, 2, 4), (2, 1, 4, 3, 0)
    one = tuple(range(5))
    d = mod.multiply(a, b)
    D = mod.generated([d], 5)
    words, queue = mod.quotient_transversal(G, a, b)
    cosets, representatives = [], []
    for g in queue:
        coset = frozenset(mod.multiply(g, h) for h in D)
        if coset not in cosets:
            cosets.append(coset)
            representatives.append(g)
    index = {c: i for i, c in enumerate(cosets)}
    action = {g: tuple(index[frozenset(mod.multiply(g, h) for h in c)]
                       for c in cosets) for g in G}
    assert len(cosets) == 12 and len(set(action.values())) == 60
    assert cycles(action[d]) == [[0], [1, 3, 5, 6, 2],
                                 [4, 7, 9, 11, 8], [10]]
    A_labels, B_labels = [1, 3, 5, 6, 2], [4, 7, 9, 11, 8]
    N = {g for g in G if {mod.conjugate(g, h) for h in D} == D}
    assert len(N) == 10
    candidates = [g for g in N if mod.order(g) == 2 and action[g][1] == 4]
    assert len(candidates) == 1
    tau = candidates[0]
    assert mod.conjugate(tau, d) == mod.inverse(d)
    for j in range(5):
        assert action[tau][A_labels[j]] == B_labels[(-j) % 5]
        assert action[tau][B_labels[j]] == A_labels[(-j) % 5]
    assert action[tau][0] == 10 and action[tau][10] == 0

    # The actual marked icosahedral configuration, with this same coset
    # labelling. k=-phi^2 and t0=k*zeta^2, so t0*zeta^3=k.
    k = C(1-THETA**2)
    t0 = k*(ZETA**2)
    assert (t0.re-2).sign() > 0
    points = {0: C(0), 10: None}
    for j in range(5):
        points[A_labels[j]] = ZETA**j
        points[B_labels[j]] = t0*(ZETA**j)
    assert len(set(points.values())) == 12
    # a(z)=(1-z)/(1-z/k); b=a o d; d(z)=zeta*z.
    ma = canonical((-k, k, C(-1), k))
    md = canonical((ZETA, C(0), C(0), C(1)))
    mb = mm(ma, md)
    mtau = canonical((C(0), t0, C(1), C(0)))
    assert mm(ma, ma) == IDENTITY
    assert mm(mm(mb, mb), mb) == IDENTITY
    assert mm(ma, mb) == md
    assert mm(mtau, mtau) == IDENTITY
    assert mm(mm(mtau, md), mtau) == mi(md)
    generator_matrices = {1: ma, 2: mb, -2: mi(mb)}
    matrices = {}
    point_checks = 0
    for g in G:
        matrix = IDENTITY
        for letter in words[g]:
            matrix = mm(matrix, generator_matrices[letter])
        matrices[g] = matrix
        for label in range(12):
            assert maps_point(matrix, points[label], points[action[g][label]])
            point_checks += 1
    assert matrices[tau] == mtau
    assert len(set(matrices.values())) == 60
    product_checks = 0
    for g in G:
        for h in (a, b):
            assert mm(matrices[g], matrices[h]) == matrices[mod.multiply(g, h)]
            product_checks += 1

    # Every C5 pole-plus-orbit set is enumerated in the actual A5 action.
    C5s = sorted({frozenset(mod.generated([g], 5)) for g in G if mod.order(g) == 5},
                 key=lambda H: sorted(H))
    assert len(C5s) == 6
    seven_sets, six_sets, set_details = set(), set(), []
    for H in C5s:
        generator = min(H-{one})
        cc = cycles(action[generator])
        poles = sorted(c[0] for c in cc if len(c) == 1)
        orbits = sorted([c for c in cc if len(c) == 5], key=sorted)
        assert len(poles) == 2 and len(orbits) == 2
        for orbit in orbits:
            seven = frozenset(poles+orbit)
            six = [frozenset([pole]+orbit) for pole in poles]
            seven_sets.add(seven)
            six_sets.update(six)
            assert all(J < seven for J in six)
            set_details.append({"cyclic_subgroup": sorted(H),
                                "poles": poles, "five_cycle": sorted(orbit),
                                "seven_set": sorted(seven),
                                "contained_six_sets": [sorted(J) for J in six]})
    assert len(seven_sets) == 12 and len(six_sets) == 24
    constant_sets = {frozenset([0, 10]+A_labels), frozenset([0, 10]+B_labels)}
    nonconstant_sets = seven_sets-constant_sets
    representative = frozenset([1, 2, 4, 5, 7, 8, 10])
    assert representative in nonconstant_sets
    orbit = {frozenset(action[g][i] for i in representative) for g in N}
    assert orbit == nonconstant_sets and len(orbit) == 10
    d_powers = [one]
    for _ in range(4):
        d_powers.append(mod.multiply(d_powers[-1], d))
    transports = []
    for power in range(5):
        for eps in (0, 1):
            transporter = mod.multiply(d_powers[power], tau) if eps else d_powers[power]
            target = frozenset(action[transporter][i] for i in representative)
            transports.append({"d_exponent": power, "tau_exponent": eps,
                               "permutation_on_five_letters": transporter,
                               "word_in_a_b": words[transporter],
                               "permutation_on_twelve_labels": action[transporter],
                               "target_seven_set": sorted(target)})
    assert len({tuple(row["target_seven_set"]) for row in transports}) == 10
    fixed = sorted(j for j in range(5) if A_labels[j] in representative)
    moving = sorted(j for j in range(5) if B_labels[j] in representative)
    assert fixed == [0, 2, 4] and moving == [0, 1, 4]
    assert representative.intersection({0, 10}) == {10}

    result = {
        "status": "PASS",
        "abstract_generators": {"a": a, "b": b, "d": d, "tau": tau},
        "generator_actions": {"a": action[a], "b": action[b], "d": action[d], "tau": action[tau]},
        "label_coordinates": {str(i): ("infinity" if points[i] is None else points[i].encoded())
                              for i in range(12)},
        "A_labels_in_zeta_order": A_labels,
        "B_labels_in_zeta_order": B_labels,
        "actual_base_parameter": t0.encoded(),
        "actual_base_parameter_formula": "(1-theta^2)*zeta^2",
        "transport_to_braid_base": "straight segment from t0 to 2+2i, entirely Re(t)>=2",
        "normalizer_order": len(N),
        "tau_word_in_a_b": words[tau],
        "exact_icosahedral_point_action_checks": point_checks,
        "exact_Mobius_generator_product_checks": product_checks,
        "actual_Mobius_matrices": {name: [c.encoded() for c in matrix]
                                  for name, matrix in (("a", ma), ("b", mb), ("d", md), ("tau", mtau))},
        "seven_sets": [sorted(J) for J in sorted(seven_sets, key=sorted)],
        "six_sets": [sorted(J) for J in sorted(six_sets, key=sorted)],
        "constant_seven_sets": [sorted(J) for J in sorted(constant_sets, key=sorted)],
        "representative_seven_set": sorted(representative),
        "representative_configuration": ["infinity", "1", "zeta^2", "zeta^4", "t", "t*zeta", "t*zeta^4"],
        "normalizer_transports": transports,
        "six_point_factorizations": set_details,
        "scope": "Exact common A5 coset/icosahedral labelling, D10 transport of the ten nonconstant seven-point maps, and all 24 literal six-point subset factorizations. Group-completion and kernel statements are proved in the accompanying F.11 text."
    }
    target = Path(__file__).with_name("c5_centralizer_labels_f11_output.json")
    target.write_text(json.dumps(result, indent=2)+"\n")
    concise = {key: result[key] for key in (
        "status", "abstract_generators", "generator_actions",
        "A_labels_in_zeta_order", "B_labels_in_zeta_order",
        "actual_base_parameter_formula", "transport_to_braid_base",
        "normalizer_order", "tau_word_in_a_b",
        "exact_icosahedral_point_action_checks", "exact_Mobius_generator_product_checks",
        "constant_seven_sets", "representative_seven_set", "normalizer_transports")}
    print(json.dumps(concise, indent=2))


if __name__ == "__main__":
    main()
