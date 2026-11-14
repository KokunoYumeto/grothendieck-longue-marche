#!/usr/bin/env python3
"""Independent exact checks for D.50's finite scalar covers and coefficients.

Only the Python standard library is used.  The group tables, quaternionic
representation, group-algebra products, and subgroup enumeration are constructed
here rather than imported from the manuscript's other certificates.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
import hashlib
import json
from pathlib import Path
import time


class Group:
    def __init__(self, n, mul):
        self.n = n
        self.tab = [[mul(a, b) for b in range(n)] for a in range(n)]
        self.inv = [next(b for b in range(n)
                         if self.tab[a][b] == self.tab[b][a] == 0)
                    for a in range(n)]
        assert all(self.tab[0][a] == self.tab[a][0] == a for a in range(n))
        assert all(self.tab[self.tab[a][b]][c] == self.tab[a][self.tab[b][c]]
                   for a, b, c in product(range(n), repeat=3))

    def mul(self, a, b):
        return self.tab[a][b]

    def comm(self, a, b):
        return self.mul(self.mul(self.mul(a, b), self.inv[a]), self.inv[b])

    def conj(self, a, b):
        return self.mul(self.mul(a, b), self.inv[a])

    def pow(self, a, n):
        r = 0
        for _ in range(n):
            r = self.mul(r, a)
        return r

    def order(self, a):
        return next(n for n in range(1, self.n + 1) if self.pow(a, n) == 0)

    def closure(self, generators):
        gs = tuple(generators)
        seen, queue = {0}, [0]
        for a in queue:
            for g in gs:
                b = self.mul(a, g)
                if b not in seen:
                    seen.add(b)
                    queue.append(b)
        return frozenset(seen)

    def subgroups(self):
        found, queue = {frozenset({0})}, [frozenset({0})]
        for H in queue:
            for a in range(self.n):
                if a in H:
                    continue
                K = self.closure((*H, a))
                if K not in found:
                    found.add(K)
                    queue.append(K)
        return sorted(found, key=lambda H: (len(H), sorted(H)))


# Quaternion units: index a = basis index (1,i,j,k) + 4 * negative sign.
UNIT_BASIS = ((0, 1, 2, 3), (1, 0, 3, 2),
              (2, 3, 0, 1), (3, 2, 1, 0))
UNIT_SIGN = ((0, 0, 0, 0), (0, 1, 0, 1),
             (0, 1, 1, 0), (0, 0, 1, 1))


def q8mul(a, b):
    u, v = a % 4, b % 4
    return UNIT_BASIS[u][v] + 4 * ((a // 4) ^ (b // 4) ^ UNIT_SIGN[u][v])


Q8 = Group(8, q8mul)


def hist_mul(G, a, b):
    out = Counter()
    for x, nx in a.items():
        for y, ny in b.items():
            out[G.mul(x, y)] += nx * ny
    return Counter({x: nx for x, nx in out.items() if nx})


def surface_count(G, subgroup, quotient, handles, boundaries):
    h = Counter({0: 1})
    for a, b in handles:
        A = [x for x in subgroup if quotient(x) == a]
        B = [x for x in subgroup if quotient(x) == b]
        P = Counter(G.comm(x, y) for x in A for y in B)
        h = hist_mul(G, h, P)
    for C in boundaries:
        h = hist_mul(G, h, Counter(C))
    return h[0]


def gauss_i(k):
    return ((1, 0), (0, 1), (-1, 0), (0, -1))[k % 4]


def gauss_mul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


# Q8 / {+1,-1}: actual nontrivial scalar cover Q=(Q8 x mu4)/graph(sign).
def phase_mul(a, b):
    u, k = a
    v, l = b
    w = q8mul(u, v)
    return (w % 4, (k + l + 2 * (w // 4)) % 4)


PHASE = tuple(product(range(4), repeat=2))
PHASE_INV = {a: next(b for b in PHASE
                     if phase_mul(a, b) == phase_mul(b, a) == (0, 0))
             for a in PHASE}


def phase_comm(a, b):
    return phase_mul(phase_mul(phase_mul(a, b), PHASE_INV[a]), PHASE_INV[b])


def q8_phase_case(handles, first_boundaries, last_quotient, signs):
    # The omitted boundary is fixed by the actual surface relation in Q.
    R = (0, 0)
    for a, b in handles:
        R = phase_mul(R, phase_comm((a, 0), (b, 0)))
    boundary_R = [(a, 0) for a in first_boundaries]
    for a in boundary_R:
        R = phase_mul(R, a)
    boundary_R.append(PHASE_INV[R])
    qs = tuple(first_boundaries) + (last_quotient,)
    assert tuple(a[0] for a in boundary_R) == qs
    classes = [(a + 4 * s,) for a, s in zip(qs, signs)]
    direct = surface_count(Q8, range(8), lambda a: a % 4, handles, classes)
    value = (1, 0)
    for C, (a, k) in zip(classes, boundary_R):
        g = C[0]
        assert g % 4 == a
        value = gauss_mul(value, gauss_i(k - 2 * (g // 4)))
    assert value[1] == 0
    trace_formula = Q(2) ** (2 * len(handles) - 1) * (1 + value[0])
    assert trace_formula.denominator == 1 and direct == trace_formula
    return direct, value[0]


def q8_phase_tests():
    assert all(phase_mul(phase_mul(a, b), c) == phase_mul(a, phase_mul(b, c))
               for a, b, c in product(PHASE, repeat=3))
    # Exact pair-to-quotient map and pullback bijection, including its graph.
    def qmap(g, k):
        return (g % 4, (k + 2 * (g // 4)) % 4)
    pairs = tuple(product(range(8), range(4)))
    assert all(qmap(q8mul(g, h), (k + l) % 4)
               == phase_mul(qmap(g, k), qmap(h, l))
               for (g, k), (h, l) in product(pairs, repeat=2))
    assert {(g, k) for g, k in pairs if qmap(g, k) == (0, 0)} == {(0, 0), (4, 2)}
    assert len({(g, qmap(g, k)) for g, k in pairs}) == 32
    totals, phases = Counter(), Counter()
    independent = [(a, b) for a in range(1, 4) for b in range(1, 4) if a != b]
    for a, b in independent:
        for signs in product(range(2), repeat=3):
            count, phase = q8_phase_case([], [a, b], a ^ b, signs)
            totals["genus0_boundaries3"] += 1
            phases[str(phase)] += 1
        for signs in product(range(2), repeat=1):
            count, phase = q8_phase_case([(a, b)], [], 0, signs)
            totals["genus1_boundaries1"] += 1
            phases[str(phase)] += 1
        for c, d in product(range(4), repeat=2):
            for signs in product(range(2), repeat=1):
                count, phase = q8_phase_case([(a, b), (c, d)], [], 0, signs)
                totals["genus2_boundaries1"] += 1
                phases[str(phase)] += 1
    for a, b, c in product(range(4), repeat=3):
        nonzero = {x for x in (a, b, c) if x}
        if len(nonzero) < 2:
            continue
        for signs in product(range(2), repeat=2):
            count, phase = q8_phase_case([(a, b)], [c], c, signs)
            totals["genus1_boundaries2"] += 1
            phases[str(phase)] += 1
    return {"group_order": 8, "normal_kernel_order": 2,
            "scalar_cover_order": 16, "pair_group_order": 32,
            "surface_cases": dict(totals), "scalar_phase_counts": dict(phases)}


# Independent rational Hamilton algebra, embedded into M_2(C) by
# i=diag(i,-i), j=[[0,1],[-1,0]], k=ij.  Trace is twice the scalar part.
def quat(a, b=0, c=0, d=0):
    return tuple(map(Q, (a, b, c, d)))


ONE = quat(1)
ZERO = quat(0)


def qm(a, b):
    x, y, z, w = a
    X, Y, Z, W = b
    return (x * X - y * Y - z * Z - w * W,
            x * Y + y * X + z * W - w * Z,
            x * Z - y * W + z * X + w * Y,
            x * W + y * Z - z * Y + w * X)


def qi(a):
    norm = sum(x * x for x in a)
    return (a[0] / norm, -a[1] / norm, -a[2] / norm, -a[3] / norm)


def qa(a, b):
    return tuple(x + y for x, y in zip(a, b))


def qc(a, b):
    return qm(qm(qm(a, b), qi(a)), qi(b))


QUNITS = [tuple(Q((-1 if k >= 4 else 1) if j == k % 4 else 0)
                for j in range(4)) for k in range(8)]
R = quat(Q(-1, 2), Q(-1, 2), Q(-1, 2), Q(-1, 2))
RPOW = [ONE, R, qm(R, R)]
assert qm(RPOW[2], R) == ONE
assert all(qm(QUNITS[a], QUNITS[b]) == QUNITS[q8mul(a, b)]
           for a, b in product(range(8), repeat=2))


def alpha(a, k=1):
    for _ in range(k % 3):
        a = (0, 2, 3, 1)[a % 4] + 4 * (a // 4)
    return a


assert all(qm(qm(R, QUNITS[a]), qi(R)) == QUNITS[alpha(a)] for a in range(8))


def tetmul(a, b):
    m, k = a % 8, a // 8
    n, l = b % 8, b // 8
    return q8mul(m, alpha(n, k)) + 8 * ((k + l) % 3)


TET = Group(24, tetmul)
REP = [qm(QUNITS[g % 8], RPOW[g // 8]) for g in range(24)]
assert all(qm(REP[a], REP[b]) == REP[TET.mul(a, b)]
           for a, b in product(range(24), repeat=2))
assert all(sum(t * t for t in a) == 1 for a in REP)  # exact determinant 1
TRACE = [2 * a[0] for a in REP]


def mclasses():
    ans = {}
    for k in range(3):
        found = set()
        for a in range(8 * k, 8 * k + 8):
            found.add(frozenset(TET.conj(m, a) for m in range(8)))
        ans[k] = sorted(found, key=lambda C: (len(C), sorted(C)))
    return ans


CLASSES = mclasses()


def tet_formula(g, boundaries):
    trivial = 1
    degree2 = Q(2) ** (2 - 2 * g - len(boundaries))
    for C in boundaries:
        trivial *= len(C)
        degree2 *= sum(TRACE[a] for a in C)
    return Q(8) ** (2 * g - 1) * (trivial + degree2)


def tet_surface_tests():
    totals, values = Counter(), Counter()
    def check(handles, boundary_cosets, label):
        for boundaries in product(*(CLASSES[h] for h in boundary_cosets)):
            direct = surface_count(TET, range(24), lambda a: a // 8,
                                   handles, boundaries)
            f = tet_formula(len(handles), boundaries)
            assert f.denominator == 1 and direct == f, (handles, boundaries, direct, f)
            totals[label] += 1
            values[str(direct)] += 1
    for a, b in product(range(3), repeat=2):
        if a or b:
            check([], [a, b, (-a - b) % 3], "genus0_boundaries3")
            check([(a, b)], [0], "genus1_boundaries1")
        for c in range(3):
            if a or b or c:
                check([(a, b)], [c, -c % 3], "genus1_boundaries2")
    for a, b, c, d in product(range(3), repeat=4):
        if a or b or c or d:
            check([(a, b), (c, d)], [0], "genus2_boundaries1")
    # Matrix handle factors for all outer pairs, not just traces.
    for a, b in product(range(3), repeat=2):
        total = ZERO
        for x in range(8 * a, 8 * a + 8):
            for y in range(8 * b, 8 * b + 8):
                total = qa(total, qc(REP[x], REP[y]))
        assert total == quat(16)
    # The noncentral normal-kernel action and the three moving linear blocks.
    assert TET.conj(8, 1) == 2 and TET.conj(8, 2) == 3
    # Since rho extends to J with determinant one, write every actual pair as
    # (g,zeta_24^k rho_J(g)).  The determinant condition is exactly zeta_24^2k
    # in mu_12.  The quotient is the literal map (g,k) -> (g mod M,k).
    pairs = tuple(product(range(24), range(24)))
    pair_graph = {(m, 0) for m in range(8)}
    scalar_kernel = {(0, k) for k in range(24)}
    qmap = lambda g, k: (g // 8, k)
    assert pair_graph & scalar_kernel == {(0, 0)}
    assert {(g, k) for g, k in pairs if qmap(g, k) == (0, 0)} == pair_graph
    assert all(qmap(TET.mul(g, h), (k + l) % 24)
               == ((g // 8 + h // 8) % 3, (k + l) % 24)
               for (g, k), (h, l) in product(pairs, repeat=2))
    assert len({(g, qmap(g, k)) for g, k in pairs}) == 576
    assert all(TET.conj(g, m) < 8 for g in range(24) for m in range(8))
    vanish_boundaries = vanish_handles = 0
    for u, v in ((1, 0), (0, 1), (1, 1)):
        char = [(1, (-1) ** u, (-1) ** v, (-1) ** (u + v))[m % 4]
                for m in range(8)]
        E = Counter({m: char[m] for m in range(8)})
        for k in (1, 2):
            for C in CLASSES[k]:
                assert not hist_mul(TET, E, Counter(C))
                vanish_boundaries += 1
        for a, b in product(range(3), repeat=2):
            if not (a or b):
                continue
            P = Counter(TET.comm(x, y)
                        for x in range(8 * a, 8 * a + 8)
                        for y in range(8 * b, 8 * b + 8))
            assert all(x < 8 for x in P)
            assert sum(char[x] * nx for x, nx in P.items()) == 0
            vanish_handles += 1
    return {"group_order": 24, "normal_kernel_order": 8,
            "normal_kernel_is_noncentral": True,
            "representation_dimensions": [1, 2],
            "exp_J": 12, "degree2_scalar_kernel_order": 24,
            "degree2_pair_group_order": 576, "degree2_cover_order": 72,
            "pair_group_quotient_product_checks": 576 ** 2,
            "pair_graph_scalar_intersection_order": 1,
            "surface_cases": dict(totals), "count_distribution": dict(values),
            "matrix_handle_cases": 9, "moving_boundary_blocks": vanish_boundaries,
            "moving_handle_blocks": vanish_handles}


def proper_subgroup_tests():
    subs = TET.subgroups()
    onto = [H for H in subs if {a // 8 for a in H} == {0, 1, 2}]
    full = frozenset(range(24))
    mu = {full: 1}
    for H in reversed(subs[:-1]):
        mu[H] = -sum(mu[K] for K in subs if H < K)
    profiles = Counter((len(H), len(H & frozenset(range(8)))) for H in onto)
    assert profiles == Counter({(3, 1): 4, (6, 2): 4, (24, 8): 1})
    # Actual extensions of all invariant M characters for every proper J.
    traces = {}
    for H in onto:
        M = H & frozenset(range(8))
        if len(M) == 1:
            traces[H] = [(1, {a: Q(1) for a in H})]
        elif len(M) == 2:
            q = next(a for a in H if a // 8 == 1 and TET.order(a) == 3)
            sign = {}
            for k, s in product(range(3), range(2)):
                a = TET.mul(4 * s, TET.pow(q, k))
                sign[a] = Q((-1) ** s)
            assert set(sign) == set(H)
            assert all(sign[TET.mul(a, b)] == sign[a] * sign[b] for a, b in product(H, repeat=2))
            traces[H] = [(1, {a: Q(1) for a in H}), (1, sign)]
        else:
            traces[H] = [(1, {a: Q(1) for a in H}), (2, {a: TRACE[a] for a in H})]
    cases = proper_cases = nonzero_proper = 0
    cache = {}
    epi_values = Counter()
    for a, b in product(range(3), repeat=2):
        if not (a or b):
            continue
        for boundaries in product(CLASSES[a], CLASSES[b], CLASSES[(-a - b) % 3]):
            weak = {}
            for H in onto:
                parts = [C & H for C in boundaries]
                direct = surface_count(TET, H, lambda x: x // 8, [], parts)
                M = H & frozenset(range(8))
                val = Q(0)
                for d, tr in traces[H]:
                    term = Q(1, d)
                    for C in parts:
                        term *= sum(tr[x] for x in C)
                    val += term
                val /= len(M)
                assert val.denominator == 1 and direct == val
                weak[H] = direct
                if H != full:
                    proper_cases += 1
                    nonzero_proper += direct != 0
            inverse_count = sum(mu[H] * weak[H] for H in onto)
            direct_epi = sum(TET.inv[TET.mul(x, y)] in boundaries[2]
                             and TET.closure((x, y)) == full
                             for x in boundaries[0] for y in boundaries[1])
            assert inverse_count == direct_epi
            key = tuple(tuple(sorted(C)) for C in boundaries)
            cache[key] = (tuple(weak[H] for H in onto), direct_epi)
            epi_values[str(direct_epi)] += 1
            cases += 1
    # All actual base-conjugator choices: each h_i in C3, independently.
    transports = 0
    for key, value in cache.items():
        for h in product(range(3), repeat=3):
            changed = tuple(tuple(sorted(TET.conj(8 * k, x) for x in C))
                            for C, k in zip(key, h))
            assert cache[changed] == value
            transports += 1
    return {"all_subgroups": len(subs), "onto_base_subgroups": len(onto),
            "onto_profiles_J_M": [{"J": j, "M": m, "number": n}
                                    for (j, m), n in sorted(profiles.items())],
            "pants_patterns": cases, "proper_subgroup_formula_cases": proper_cases,
            "nonzero_proper_subgroup_counts": nonzero_proper,
            "ordinary_mobius_epi_cases": cases,
            "epi_count_distribution": dict(epi_values),
            "all_literal_boundary_transports": transports,
            "subgroup_records": [{"elements": sorted(H), "M": sorted(H & frozenset(range(8))),
                                   "mu_to_E": mu[H]} for H in onto]}


def nonfaithful_d8_tests():
    def mul(a, b):
        i, j = a % 4, a // 4
        k, l = b % 4, b // 4
        return (i + (-1) ** j * k) % 4 + 4 * ((j + l) % 2)
    G = Group(8, mul)
    pairs = tuple(product(range(8), range(4)))
    def qmap(a, k):
        return ((k - 2 * (a % 4)) % 4, a // 4)
    def qmul(x, y):
        return ((x[0] + y[0]) % 4, (x[1] + y[1]) % 2)
    assert all(qmap(G.mul(a, b), (k + l) % 4) == qmul(qmap(a, k), qmap(b, l))
               for (a, k), (b, l) in product(pairs, repeat=2))
    graph = {(a, 2 * a % 4) for a in range(4)}
    scalar = {(0, k) for k in range(4)}
    kernel = {(a, k) for a, k in pairs if qmap(a, k) == (0, 0)}
    assert kernel == graph and graph & scalar == {(0, 0)}
    assert (2, 0) in graph  # nontrivial kernel of rho remains in first coordinate
    assert len({qmap(a, k) for a, k in pairs}) == 8
    pullback = {(a, (z, a // 4)) for a in range(8) for z in range(4)}
    assert {(a, qmap(a, k)) for a, k in pairs} == pullback
    # The B coordinate is exactly i^(z+2a), not an unspecified scalar.
    assert all(gauss_i(k) == gauss_i(qmap(a, k)[0] + 2 * (a % 4)) for a, k in pairs)
    return {"J_order": 8, "M_order": 4, "rho_kernel_order": 2,
            "determinant_bound": 4, "scalar_kernel_order": 4,
            "pair_group_order": 32, "graph_order": 4,
            "graph_scalar_intersection_order": 1,
            "quotient": "C4 x C2", "quotient_order": 8,
            "homomorphism_product_checks": 1024, "pullback_elements": 32}


def main():
    started = time.monotonic()
    result = {"status": "PASS", "scope": "D50 independent finite scalar-cover identities",
              "q8_projective_phase": q8_phase_tests(),
              "binary_tetrahedral": tet_surface_tests(),
              "proper_subgroups_and_mobius": proper_subgroup_tests(),
              "nonfaithful_d8": nonfaithful_d8_tests()}
    path = Path(__file__)
    result["source_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    path.with_suffix('.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps(result, indent=2, sort_keys=True))
    print(f"Elapsed seconds: {time.monotonic() - started:.3f}")


if __name__ == '__main__':
    main()
