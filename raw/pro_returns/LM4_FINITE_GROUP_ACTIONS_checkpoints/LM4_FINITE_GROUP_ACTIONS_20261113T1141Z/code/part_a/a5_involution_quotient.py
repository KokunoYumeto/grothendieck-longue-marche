#!/usr/bin/env python3
"""Exact exploration of the characteristic universal A5 quotient of Fhat_2.

Only finite equations are computed. Surviving tuples are never asserted
to lift to an element of the full pure or Grothendieck--Teichmueller group.
"""
from itertools import permutations, product
from collections import deque, Counter, defaultdict
from math import prod
from pathlib import Path
import json

S5 = list(permutations(range(5)))
ONE = tuple(range(5))


def multiply(a, b):
    return tuple(a[b[i]] for i in range(5))


def inverse(a):
    return tuple(a.index(i) for i in range(5))


def parity(a):
    return sum(a[i] > a[j] for i in range(5) for j in range(i + 1, 5)) % 2


def cycles(g):
    seen, out = set(), []
    for i in range(5):
        if i in seen:
            continue
        cyc, j = [], i
        while j not in seen:
            seen.add(j)
            cyc.append(j + 1)
            j = g[j]
        if len(cyc) > 1:
            out.append("(" + " ".join(map(str, cyc)) + ")")
    return "".join(out) or "()"


A5 = [g for g in S5 if parity(g) == 0]
INDEX = {g: i for i, g in enumerate(A5)}
ID = INDEX[ONE]
MUL = [[INDEX[multiply(a, b)] for b in A5] for a in A5]
INV = [INDEX[inverse(a)] for a in A5]
CONJ = [[INDEX[multiply(multiply(g, a), inverse(g))] for a in A5]
        for g in S5]


def power(a, n):
    ans = ID
    for _ in range(n % 30):
        ans = MUL[ans][a]
    return ans


def order(a):
    for n in range(1, 31):
        if power(a, n) == ID:
            return n
    raise AssertionError


def generated(a, b):
    seen, queue = {ID}, [ID]
    for s in queue:
        for t in (a, b):
            u = MUL[s][t]
            if u not in seen:
                seen.add(u)
                queue.append(u)
    return len(seen)


def tuple_mul(a, b):
    return tuple(MUL[x][y] for x, y in zip(a, b))


def tuple_inv(a):
    return tuple(INV[x] for x in a)


def main():
    reps, lookup = [], {}
    for a in range(60):
        for b in range(60):
            if (a, b) in lookup or generated(a, b) != 60:
                continue
            j = len(reps)
            reps.append((a, b))
            for gi, conj in enumerate(CONJ):
                pair = conj[a], conj[b]
                assert pair not in lookup
                lookup[pair] = j, gi
    assert len(reps) == 19 and len(lookup) == 2280
    X = tuple(a for a, _ in reps)
    Y = tuple(b for _, b in reps)
    Z = tuple(INV[MUL[a][b]] for a, b in reps)
    O = (ID,) * 19

    classes, cl = [], {}
    for a in range(60):
        if a in cl:
            continue
        c = {CONJ[i][a] for i, g in enumerate(S5) if parity(g) == 0}
        j = len(classes)
        classes.append(c)
        for b in c:
            cl[b] = j
    oddi = next(i for i, g in enumerate(S5) if parity(g))
    flip = {cl[a]: cl[CONJ[oddi][a]] for a in range(60)}
    passport_blocks = defaultdict(list)
    for i in range(19):
        v = (cl[X[i]], cl[Y[i]], cl[Z[i]])
        passport_blocks[min(v, tuple(flip[j] for j in v))].append(i)
    assert all(len(b) == 1 for b in passport_blocks.values())
    assert all(5 in (order(X[i]), order(Y[i]), order(Z[i])) for i in range(19))

    actions = {}
    for name, fn in [
        ("theta", lambda a, b: (b, a)),
        ("omega", lambda a, b: (b, INV[MUL[a][b]])),
        ("delta", lambda a, b: (INV[a], INV[b])),
    ]:
        actions[name] = [lookup[fn(a, b)] for a, b in reps]

    def act(name, values):
        return tuple(CONJ[gi][values[j]] for j, gi in actions[name])

    assert act("theta", act("theta", X)) == X
    assert act("omega", act("omega", act("omega", X))) == X
    assert act("omega", act("omega", act("omega", Y))) == Y
    delta_t = tuple(INDEX[S5[gi]] for j, gi in actions["delta"])
    assert all(j == i for i, (j, gi) in enumerate(actions["delta"]))
    assert all(MUL[t][t] == ID for t in delta_t)

    # For alpha=Inn(t), the normalized lambda=-1 equations reduce to:
    # t^2=1, t X t^-1=X^-1, omega(t)=Y^-1 theta(t).
    allowed = [
        {t for t in range(60)
         if MUL[t][t] == ID and MUL[MUL[t][X[i]]][INV[t]] == INV[X[i]]}
        for i in range(19)
    ]
    graph = defaultdict(list)
    for i in range(19):
        j, w = actions["omega"][i]
        k, th = actions["theta"][i]
        forward = {}
        inv_w = inverse(S5[w])
        for t in range(60):
            rhs = MUL[INV[Y[i]]][CONJ[th][t]]
            value = INDEX[multiply(multiply(inv_w, A5[rhs]), S5[w])]
            forward[t] = value
        backward = {v: u for u, v in forward.items()}
        assert len(backward) == 60
        graph[k].append((j, forward))
        graph[j].append((k, backward))

    components, component_solutions, used = [], [], set()
    for root in range(19):
        if root in used:
            continue
        comp, queue = {root}, [root]
        for v in queue:
            for w, _ in graph[v]:
                if w not in comp:
                    comp.add(w)
                    queue.append(w)
        used.update(comp)
        solutions = []
        for value in sorted(allowed[root]):
            assignment, pending, good = {root: value}, [root], True
            for v in pending:
                for w, transform in graph[v]:
                    z = transform[assignment[v]]
                    if z not in allowed[w] or (w in assignment and assignment[w] != z):
                        good = False
                        break
                    if w not in assignment:
                        assignment[w] = z
                        pending.append(w)
                if not good:
                    break
            if good:
                assert set(assignment) == comp
                solutions.append(assignment)
        components.append(sorted(comp))
        component_solutions.append(solutions)
    total = prod(len(s) for s in component_solutions)

    def full_t(choices):
        t = [None] * 19
        for assignment in choices:
            for j, value in assignment.items():
                t[j] = value
        assert all(v is not None for v in t)
        return tuple(t)

    units = [1, 7, 11, 13, 17, 19, 23, 29]
    conjugacy_allowed = {}
    for mu in units:
        sign = 0 if mu % 5 in (1, 4) else 1
        conjugacy_allowed[mu] = [
            {CONJ[gi][delta_t[i]] for gi, g in enumerate(S5)
             if parity(g) == sign and CONJ[gi][X[i]] == power(X[i], mu)}
            for i in range(19)
        ]

    # Every defining condition is confined to one listed component.
    # Enumerate all component assignments, then count their Cartesian product.
    # This computes all 10,125,000 tuples without a redundant global loop.
    triangle_sets = [
        {j for j, assignment in enumerate(solutions)
         if all(value not in (ID, X[i]) for i, value in assignment.items())}
        for solutions in component_solutions
    ]
    conjugacy_patterns = []
    for mu in units:
        pattern = tuple(frozenset(
            j for j, assignment in enumerate(solutions)
            if all(value in conjugacy_allowed[mu][i]
                   for i, value in assignment.items()))
            for solutions in component_solutions)
        if pattern not in conjugacy_patterns:
            conjugacy_patterns.append(pattern)
    def union_size(patterns):
        ans = 0
        for mask in range(1, 1 << len(patterns)):
            active = [patterns[j] for j in range(len(patterns)) if mask >> j & 1]
            cardinality = prod(len(set.intersection(*[set(p[i]) for p in active]))
                               for i in range(len(components)))
            ans += cardinality if len(active) % 2 else -cardinality
        return ans
    conjugate_total = union_size(conjugacy_patterns)
    triangle_total = prod(len(s) for s in triangle_sets)
    assert all(set(pattern[i]) <= triangle_sets[i]
               for pattern in conjugacy_patterns for i in range(len(components)))
    counts = Counter(finite_solutions=total, passes_triangle=triangle_total,
                     conjugate_by_finite_pure_automorphism=conjugate_total,
                     passes_triangle_but_not_conjugate=triangle_total-conjugate_total)
    # Exhaustively verify the defining constraints on every component assignment;
    # the displayed algebra reduces I/II to these same constraints globally.
    baseline = [solutions[0] for solutions in component_solutions]
    checked = 0
    representatives = []
    first_bad = None
    for ci, solutions in enumerate(component_solutions):
        for assignment in solutions:
            choices = baseline.copy()
            choices[ci] = assignment
            t = full_t(choices)
            f = tuple_mul(act("theta", t), tuple_inv(t))
            assert tuple_mul(act("theta", f), f) == O
            ii = tuple_mul(
                tuple_mul(tuple_mul(tuple_mul(tuple_mul(
                    act("omega", act("omega", f)), tuple_inv(Z)),
                    act("omega", f)), tuple_inv(Y)), f), tuple_inv(X))
            assert ii == O
            assert tuple_mul(t, t) == O
            assert tuple_mul(tuple_mul(t, X), tuple_inv(t)) == tuple_inv(X)
            assert tuple_mul(tuple_mul(t, Y), tuple_inv(t)) == tuple_mul(
                tuple_mul(tuple_inv(f), tuple_inv(Y)), f)
            alpha_f = tuple_mul(tuple_mul(t, f), tuple_inv(t))
            assert tuple_mul(f, alpha_f) == O
            assert act("omega", t) == tuple_mul(tuple_inv(Y), act("theta", t))
            no_central = all(value not in (ID, X[i]) for i, value in enumerate(t))
            direct = all(ID not in (t[i], MUL[X[i]][t[i]],
                          MUL[MUL[Y[i]][f[i]]][t[i]]) for i in range(19))
            assert direct == no_central
            mus = [mu for mu in units if all(
                t[i] in conjugacy_allowed[mu][i] for i in range(19))]
            checked += 1
            if first_bad is None and not no_central:
                first_bad = {"t": [cycles(A5[v]) for v in t],
                             "f": [cycles(A5[v]) for v in f]}
            if len(representatives) < 3:
                representatives.append({"t": [cycles(A5[v]) for v in t],
                    "conjugator_units": mus, "passes_triangle": no_central})
    data = {
        "group": "Q_A5 = A5^19, the quotient by the intersection of all kernels of epimorphisms Fhat_2 -> A5",
        "generating_pairs": len(lookup),
        "Aut_A5_orbits": len(reps),
        "representative_pairs": [[cycles(A5[a]), cycles(A5[b])] for a, b in reps],
        "standard_inversion_inner_tuple": [cycles(A5[v]) for v in delta_t],
        "theta_component_maps": actions["theta"],
        "omega_component_maps": actions["omega"],
        "passport_blocks": [v for v in passport_blocks.values()],
        "passports_orders": [[order(X[i]), order(Y[i]), order(Z[i])] for i in range(19)],
        "components": components,
        "component_solution_counts": [len(s) for s in component_solutions],
        "predicted_total": total,
        "triangle_component_counts": [len(s) for s in triangle_sets],
        "conjugacy_pattern_component_counts": [[len(s) for s in p] for p in conjugacy_patterns],
        "component_assignments_directly_checked": checked,
        "counts": dict(counts),
        "first_rejected_by_triangle": first_bad,
        "first_representatives": representatives,
        "scope": "All computed tuples satisfy finite normalized I, II, involutivity and invertibility on Q_A5. No surviving tuple is asserted to lift to full GT_0."
    }
    Path(__file__).with_name("a5_involution_quotient_output.json").write_text(
        json.dumps(data, indent=2) + "\n")
    print(json.dumps({key: data[key] for key in [
        "generating_pairs", "Aut_A5_orbits", "passports_orders", "components",
        "component_solution_counts", "triangle_component_counts",
        "conjugacy_pattern_component_counts", "component_assignments_directly_checked",
        "predicted_total", "counts", "scope"]}, indent=2))


if __name__ == "__main__":
    main()
