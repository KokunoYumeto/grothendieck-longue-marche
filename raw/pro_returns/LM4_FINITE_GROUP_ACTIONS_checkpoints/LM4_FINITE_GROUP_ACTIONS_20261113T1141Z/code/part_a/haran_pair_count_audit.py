#!/usr/bin/env python3
"""Independent PSL2(11) peripheral-count audit using 12-point permutations.

The PSL group is generated on P1(F11), rather than enumerated as matrices.
Counts run through the allowed (l,t) images first and then the image of a.
"""
from collections import Counter
from pathlib import Path
import json

P = 11
INF = P
ONE = tuple(range(P + 1))


def compose(g, h):
    return tuple(g[h[i]] for i in range(P + 1))


def inverse(g):
    h = [None] * len(g)
    for i, v in enumerate(g):
        h[v] = i
    return tuple(h)


def mobius(a, b, c, d):
    out = []
    for x in range(P + 1):
        num, den = (a, c) if x == INF else ((a*x+b) % P, (c*x+d) % P)
        out.append(INF if den == 0 else num * pow(den, -1, P) % P)
    return tuple(out)


def main():
    s, t = mobius(0, -1, 1, 0), mobius(1, 1, 0, 1)
    group, seen = [ONE], {ONE}
    for g in group:
        for generator in (s, t):
            h = compose(g, generator)
            if h not in seen:
                seen.add(h)
                group.append(h)
    assert len(group) == 660
    ix = {g: i for i, g in enumerate(group)}
    mul = [[ix[compose(g, h)] for h in group] for g in group]
    inv = [ix[inverse(g)] for g in group]
    powers = []
    for g in range(len(group)):
        row, h = [0], g
        while h:
            row.append(h)
            h = mul[h][g]
        powers.append(row)

    def power(g, n):
        return powers[g][n % len(powers[g])]

    chosen = ix[mobius(0, 1, 10, 2)]
    cls = {mul[mul[g][chosen]][inv[g]] for g in range(len(group))}
    cls_inv = {inv[g] for g in cls}
    assert len(cls) == len(cls_inv) == 60
    assert cls.isdisjoint(cls_inv)
    assert all(len(powers[g]) == 11 for g in cls | cls_inv)
    # Exact CRT representatives for the group exponent 330.
    epsilon, kappa = 221, 165
    assert epsilon % 3 == 2 and epsilon % 110 == 1
    assert kappa % 2 == 1 and kappa % 165 == 0
    counts = [0, 0]
    by_l_order = [Counter(), Counter()]
    allowed_l_t = Counter()
    l_t_count = 0
    for l in range(len(group)):
        target, square = power(l, epsilon), power(l, kappa)
        allowed = [u for u in range(len(group))
                   if mul[u][u] == square and mul[mul[u][l]][inv[u]] == target]
        allowed_l_t[len(powers[l])] += len(allowed)
        l_t_count += len(allowed)
        for which, a_class in enumerate((cls, cls_inv)):
            # p=a^-1*l.  This chooses the image of a after the Nbad image.
            number_a = sum(mul[inv[a]][l] in cls for a in a_class)
            counts[which] += len(allowed) * number_a
            by_l_order[which][len(powers[l])] += len(allowed) * number_a
    assert counts == [10200, 4920]
    result = {
        "group": "PSL2(F11) in its independently generated action on P1(F11)",
        "group_order": len(group),
        "element_order_histogram": dict(sorted(Counter(map(len, powers)).items())),
        "class_matrix": [[0, 1], [10, 2]],
        "class_permutation": group[chosen],
        "class_size": len(cls),
        "inverse_class_size": len(cls_inv),
        "classes_disjoint": cls.isdisjoint(cls_inv),
        "epsilon_mod330": epsilon,
        "kappa_mod330": kappa,
        "Nbad_homomorphism_count": l_t_count,
        "Nbad_counts_by_l_order": dict(sorted(allowed_l_t.items())),
        "count_a_C_p_C": counts[0],
        "count_a_inverseC_p_C": counts[1],
        "first_count_by_l_order": dict(sorted(by_l_order[0].items())),
        "second_count_by_l_order": dict(sorted(by_l_order[1].items())),
        "proved_consequence": "No continuous automorphism of Nbad amalg Zhat(a), with p=a^-1*l, sends a to a conjugate of a^lambda and p to a conjugate of p: precomposition would biject the two finite Hom subsets, whose cardinalities differ.",
        "scope": "The implication from a proposed extra marked deck symmetry to the displayed automorphism is audited separately. No finite survivor is asserted to lift."
    }
    target = Path(__file__).with_name("haran_pair_count_audit_output.json")
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
