#!/usr/bin/env python3
"""Exact finite certificates for frozen MPL 64 scans 026--039.

No scan, transcription, or context file is modified.  The only input read is the
combined frozen fragment, as bytes, to bind the result to its SHA-256.  All
mathematics uses the Python standard library and exhaustive finite operations.

Usage: python3 records/group_checks.py [--output records/group_checks_results.json]

Matrices are row-major tuples acting on column vectors on the left.  A product
g*h means g after h.  Permutations are tuples of images, with the same convention.
The subgroup named A is the canonical two-dimensional summand of End(F2^2), not
a subalgebra.  D8 denotes the group of order eight.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools as it
import json
from collections import Counter
from pathlib import Path


E = (1, 0, 0, 1)
O = (0, 0, 0, 0)
J = ((1, 0), (0, 1), (1, 1))
FROZEN_SHA256 = 'f5b4a21fa7e2d5bcac3f2f42e655abe0cbd277b4c3442b07e9c0438abf5a7932'


def add(x, y, n=2):
    return tuple((a+b) % n for a, b in zip(x, y))


def mul(x, y, n=4):
    a, b, c, d = x
    e, f, g, h = y
    return ((a*e+b*g) % n, (a*f+b*h) % n,
            (c*e+d*g) % n, (c*f+d*h) % n)


def mv(x, v, n=4):
    return ((x[0]*v[0]+x[1]*v[1]) % n,
            (x[2]*v[0]+x[3]*v[1]) % n)


def det(x, n=4):
    return (x[0]*x[3]-x[1]*x[2]) % n


def tr(x):
    return (x[0]+x[3]) % 2


def inv(x, n=4):
    k = pow(det(x, n), -1, n)
    return tuple(k*a % n for a in (x[3], -x[1], -x[2], x[0]))


def mod2(x):
    return tuple(a % 2 for a in x)


def lift_kernel(x):
    return tuple((a+2*b) % 4 for a, b in zip(E, x))


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def parity(p):
    return sum(p[i] > p[j] for i in range(len(p))
               for j in range(i+1, len(p))) % 2


def closure(generators, identity=E, operation=mul):
    generators = set(generators)
    found, queue = {identity}, [identity]
    while queue:
        x = queue.pop()
        for g in generators:
            y = operation(x, g)
            if y not in found:
                found.add(y)
                queue.append(y)
    return frozenset(found)


def derived(group):
    return closure(mul(mul(mul(x, y), inv(x)), inv(y))
                   for x in group for y in group)


def center(group):
    return frozenset(x for x in group
                     if all(mul(x, y) == mul(y, x) for y in group))


def quotient_order_counts(group, normal):
    cosets = {frozenset(mul(x, n) for n in normal) for x in group}
    answer = Counter()
    for coset in cosets:
        x, y, k = min(coset), E, 0
        while True:
            y = mul(y, x)
            k += 1
            if y in normal:
                break
            assert k <= len(group)
        answer[k] += 1
    return dict(sorted(answer.items()))


def partition_orbits(points, group, action):
    return tuple(sorted({frozenset(action(g, p) for g in group)
                         for p in points}, key=lambda x: sorted(x)))


def quotient_action(orbits, group, action):
    owner = {p: i for i, orbit in enumerate(orbits) for p in orbit}
    result = {}
    for g in group:
        perm = []
        for orbit in orbits:
            images = {owner[action(g, p)] for p in orbit}
            assert len(images) == 1
            perm.append(images.pop())
        assert len(set(perm)) == len(orbits)
        result[g] = tuple(perm)
    return result, owner


def square_mul(x, y):
    # (translation first coordinate, translation second coordinate, swap bit)
    a, b, c = x
    d, e, f = y
    if c:
        d, e = e, d
    return (a ^ d, b ^ e, c ^ f)


def square_section(c, d):
    return (d, 0, c)


def run():
    R = {}
    End = tuple(it.product(range(2), repeat=4))
    V = tuple(it.product(range(2), repeat=2))
    G2 = tuple(x for x in End if det(x, 2) == 1)
    G = tuple(x for x in it.product(range(4), repeat=4) if det(x) % 2)
    SL = frozenset(x for x in G if det(x) == 1)
    Z = frozenset((E, (3, 0, 0, 3)))
    K = frozenset(lift_kernel(x) for x in End)
    assert len(G) == 96 and len(SL) == 48 and len(K) == 16
    assert K == frozenset(x for x in G if mod2(x) == E)
    assert all(mul(lift_kernel(a), lift_kernel(b)) == lift_kernel(add(a, b))
               for a in End for b in End)
    assert all(det(lift_kernel(a)) == (1+2*tr(a)) % 4 for a in End)

    # Canonical module summands: the three involutions and the two 3-cycles.
    sigma = {(0, 0): O}
    for v in J:
        candidates = [g for g in G2 if g != E and mv(g, v, 2) == v]
        assert len(candidates) == 1
        sigma[v] = candidates[0]
    A = frozenset(sigma.values())
    rhos = tuple(g for g in G2 if g != E and mul(mul(g, g, 2), g, 2) == E)
    assert len(rhos) == 2
    rho = (0, 1, 1, 1)
    rho2 = mul(rho, rho, 2)
    assert set(rhos) == {rho, rho2}
    W = frozenset((O, E, rho, rho2))
    assert len(A) == len(W) == 4 and A & W == {O}
    assert {add(a, w) for a in A for w in W} == set(End)
    assert all(sigma[add(u, v)] == add(sigma[u], sigma[v]) for u in V for v in V)
    assert all(sigma[mv(g, v, 2)] == mul(mul(g, sigma[v], 2), inv(g, 2), 2)
               for g in G2 for v in V)
    assert all(tr(mul(a, w, 2)) == 0 for a in A for w in W)
    sl = frozenset(a for a in End if tr(a) == 0)
    assert sl == {add(a, z) for a in A for z in (O, E)}
    assert W & sl == {O, E}
    eval_maps = {tuple(mv(a, v, 2) for v in J) for a in End}
    sum_zero_maps = {f for f in it.product(V, repeat=3)
                     if add(add(f[0], f[1]), f[2]) == (0, 0)}
    assert eval_maps == sum_zero_maps and len(eval_maps) == 16
    for g in G2:
        jp = tuple(J.index(mv(g, v, 2)) for v in J)
        rp = tuple(rhos.index(mul(mul(g, r, 2), inv(g, 2), 2)) for r in rhos)
        assert parity(jp) == parity(rp)

    # Four complements of scalars in sl2; one is invariant under the whole S3.
    scalar = {O, E}
    complements = set()
    for x, y in it.combinations(sl - {O}, 2):
        B = frozenset((O, x, y, add(x, y)))
        if len(B) == 4 and B & scalar == {O}:
            complements.add(B)
    invariant = [B for B in complements if all(
        {mul(mul(g, x, 2), inv(g, 2), 2) for x in B} == set(B) for g in G2)]
    assert len(complements) == 4 and invariant == [A]
    complement_orbits = {frozenset(frozenset(mul(mul(g, x, 2), inv(g, 2), 2)
                                           for x in B) for g in G2)
                         for B in complements}
    assert sorted(map(len, complement_orbits)) == [1, 3]
    # Explicit equivariant F2^J/diag -> V -> sl2/scalars.
    coeffs = tuple(it.product(range(2), repeat=3))
    def coeff_to_v(c):
        return tuple(sum(c[i]*J[i][k] for i in range(3)) % 2 for k in range(2))
    assert {c for c in coeffs if coeff_to_v(c) == (0, 0)} == {(0,0,0),(1,1,1)}
    for h in G2:
        hp = tuple(J.index(mv(h, v, 2)) for v in J)
        for c in coeffs:
            hc = [0]*3
            for i in range(3):
                hc[hp[i]] = c[i]
            assert coeff_to_v(hc) == mv(h, coeff_to_v(c), 2)
    # Recheck the pre-existing LM_P057 R17 formula against this certificate.
    def phi(t):
        return tuple((v[0]*mv(t,v,2)[1]-v[1]*mv(t,v,2)[0]) % 2 for v in J)
    assert all(sum(phi(t)) % 2 == 0 and coeff_to_v(phi(t)) == (t[1],t[2]) for t in sl)
    assert {t for t in sl if phi(t)==(0,0,0)} == scalar
    for h in G2:
        hi = inv(h,2)
        for t in sl:
            assert phi(mul(mul(h,t,2),hi,2)) == tuple(phi(t)[J.index(mv(hi,v,2))] for v in J)
    R['G01_module_decomposition'] = {
        'field': 'F2', 'dimension': 2, 'J_order': J,
        'sigma_by_v': {str(v): sigma[v] for v in J},
        'A': sorted(A), 'W': sorted(W), 'rho': rho, 'rho_inverse': rho2,
        'trace_zero': sorted(sl), 'evaluation_bijection_size': len(eval_maps),
        'scalar_complements': len(complements),
        'scalar_complement_orbit_sizes': [1, 3],
        'unique_invariant_complement': sorted(A),
        'equivariant_quotient_map': '[c_i] -> sum c_i v_i -> [sigma_(sum c_i v_i)]',
        'LM_P057_R17_determinant_function_formula_rechecked':True,
        'all_linearity_equivariance_trace_and_direct_sum_assertions': True,
    }

    # The sixteen sum-zero lift triples, and the canonical quotient torsors.
    fibres = [[p for p in it.product(range(4), repeat=2)
               if tuple(x % 2 for x in p) == v] for v in J]
    P = tuple(sorted(p for p in it.product(*fibres)
                     if add(add(p[0], p[1], 4), p[2], 4) == (0, 0)))
    assert len(P) == 16
    def act(g, p):
        out = [None]*3
        for i, v in enumerate(J):
            j = J.index(mv(mod2(g), v, 2))
            out[j] = mv(g, p[i])
        return tuple(out)
    assert all(act(g, p) in P for g in G for p in P)
    p0 = ((1, 0), (0, 1), (3, 3))
    assert p0 in P and {act(k, p0) for k in K} == set(P)
    assert all(act(lift_kernel(a), p) == tuple(add(p[i], tuple(2*x for x in mv(a, J[i], 2)), 4)
                                            for i in range(3)) for a in End for p in P)
    H = frozenset(g for g in G if act(g, p0) == p0)
    assert len(H) == 6 and {mod2(g) for g in H} == set(G2)
    assert H & K == {E} and {mul(h, k) for h in H for k in K} == set(G)
    h_r, h_s = (0, 3, 1, 3), (0, 1, 1, 0)
    assert h_r in H and h_s in H and closure((h_r, h_s)) == H
    assert mul(mul(h_s, h_r), h_s) == inv(h_r)
    KA, KW = frozenset(map(lift_kernel, A)), frozenset(map(lift_kernel, W))
    Iorbs = partition_orbits(P, KW, act)
    Sorbs = partition_orbits(P, KA, act)
    PI, Iowner = quotient_action(Iorbs, G, act)
    PS, Sowner = quotient_action(Sorbs, G, act)
    assert len(Iorbs) == len(Sorbs) == 4
    assert len(set(PI.values())) == 24 and len(set(PS.values())) == 8
    assert len({(PI[g], PS[g]) for g in G}) == 96
    PJ = {g: tuple(J.index(mv(mod2(g), v, 2)) for v in J) for g in G}
    sg = {g: parity(PJ[g]) for g in G}
    dt = {g: (det(g)-1)//2 for g in G}
    assert all(parity(PI[g]) == sg[g] for g in G)
    assert all(dt[h] == sg[h] for h in H)
    assert all(dt[mul(h, lift_kernel(a))] == (sg[h] ^ tr(a)) for h in H for a in End)

    # Give S=P/A its square graph via the distinguished W basis {rho,rho^-1}.
    bits = tuple(it.product(range(2), repeat=2))
    scoord = {}
    for x, y in bits:
        w = add(tuple(x*a for a in rho), tuple(y*a for a in rho2))
        scoord[(x, y)] = Sowner[act(lift_kernel(w), p0)]
    assert len(set(scoord.values())) == 4
    sinv = {i: c for c, i in scoord.items()}
    Q = {}
    for g in G:
        t = sinv[PS[g][scoord[(0, 0)]]]
        c = sg[g]
        for x, y in bits:
            u, v = (y, x) if c else (x, y)
            assert sinv[PS[g][scoord[(x, y)]]] == (u ^ t[0], v ^ t[1])
        Q[g] = (t[0], t[1], c)
    D8 = set(it.product(range(2), repeat=3))
    assert set(Q.values()) == D8
    assert all(Q[mul(g, h)] == square_mul(Q[g], Q[h]) for g in G for h in G)
    cchar = {g: Q[g][2] for g in G}
    dchar = {g: Q[g][0] ^ Q[g][1] for g in G}
    orchar = {g: Q[g][0] ^ Q[g][1] ^ Q[g][2] for g in G}
    assert all((cchar[g], dchar[g], orchar[g]) == (sg[g], sg[g] ^ dt[g], dt[g]) for g in G)
    S4 = set(it.permutations(range(4)))
    fibreproduct = {(s, q) for s in S4 for q in D8 if parity(s) == q[2]}
    assert {(PI[g], Q[g]) for g in G} == fibreproduct
    square_edges = {frozenset((b, add(b, e))) for b in bits for e in ((1,0),(0,1))}
    square_diagonals = {frozenset((b, add(b, (1,1)))) for b in bits}
    assert len(square_edges) == 4 and len(square_diagonals) == 2
    R['G02_torsor_and_square'] = {
        'P_size': len(P), 'P_basepoint_for_coordinates_only': p0,
        'P_points': P, 'I_P_mod_W_size': len(Iorbs), 'S_P_mod_A_size': len(Sorbs),
        'stabilizer_of_basepoint': sorted(H), 'stabilizer_generators': [h_r, h_s],
        'I_action_image_order': 24, 'square_action_image_order': 8,
        'combined_action_image_order': 96, 'fibre_product_order': len(fibreproduct),
        'square_coordinate_form': '(x,y) -> (t1,t2) + swap^c(x,y)',
        'codiagonal_character_c': 'sign(reduction)=sign(I)',
        'diagonal_character_d': 't1+t2=sign(reduction)+det_bit',
        'square_orientation_character': 't1+t2+c=det_bit',
        'det_bit_convention': 'det(g)=(-1)^det_bit in (Z/4)^*',
        'all_action_torsor_and_fibreproduct_assertions': True,
    }

    # Commutators, centers, exact abelianizations, and the five intersections.
    DSL, DG = derived(SL), derived(G)
    kerQ = frozenset(g for g in G if Q[g] == (0,0,0))
    assert DSL == kerQ and len(DSL) == 12
    assert {PI[g] for g in DSL} == {s for s in S4 if parity(s) == 0}
    assert len({PI[g] for g in DSL}) == len(DSL)
    assert DG == {mul(a, z) for a in DSL for z in Z} and len(DG) == 24
    assert DSL & Z == {E} and all(mul(a,z)==mul(z,a) for a in DSL for z in Z)
    assert center(G) == Z and center(SL) == Z
    # The cyclic abelianization transforms as the determinant line, not as a
    # trivial C4 under all of GL.  Fix the lower elementary transvection as the
    # generator corresponding to e1 wedge e2 in this coordinate convention.
    U = (1,0,1,1)
    U_powers = [E]
    for _ in range(3):
        U_powers.append(mul(U_powers[-1],U))
    assert len({frozenset(mul(u,a) for a in DSL) for u in U_powers}) == 4
    assert all(mul(mul(mul(g,U),inv(g)),inv(U_powers[det(g)])) in DSL for g in G)
    sl_involutions = {g for g in SL if mul(g,g)==E}
    assert sl_involutions <= K
    sl_orders = quotient_order_counts(SL, DSL)
    gl_orders = quotient_order_counts(G, DG)
    assert sl_orders == {1:1, 2:1, 4:2}
    assert gl_orders == {1:1, 2:3}
    assert {Q[g] for g in SL} == {q for q in D8 if q[0] ^ q[1] ^ q[2] == 0}
    S4section = frozenset(mul(k, h) for k in KA for h in H)
    assert len(S4section) == 24 and closure(S4section) == S4section
    assert len({PI[g] for g in S4section}) == 24
    assert S4section & KW == {E}
    assert {mul(s,w) for s in S4section for w in KW} == set(G)
    Hsg = frozenset(g for g in G if sg[g] == 0)
    Hsd = frozenset(g for g in G if sg[g] ^ dt[g] == 0)
    Ksl = K & SL
    assert Hsg == {mul(a,w) for a in DSL for w in KW}
    assert DSL & KW == {E} and all(mul(a,w)==mul(w,a) for a in DSL for w in KW)
    assert Hsd == {mul(s,z) for s in S4section for z in Z}
    assert S4section & Z == {E}
    squares = [
        ('GL', set(G), 'ker(sign)', Hsg, 'SL', SL, 'derived_GL', DG),
        ('ker(sign)', Hsg, 'K', K, 'derived_GL', DG, 'K_intersect_SL', Ksl),
        ('derived_GL', DG, 'K_intersect_SL', Ksl, 'derived_SL', DSL, 'KA', KA),
        ('K', K, 'KW', KW, 'K_intersect_SL', Ksl, 'Z', Z),
        ('K_intersect_SL', Ksl, 'Z', Z, 'KA', KA, '1', {E}),
    ]
    square_data = []
    for tn, top, ln, left, rn, right, bn, bottom in squares:
        assert left <= top and right <= top and set(left) & set(right) == set(bottom)
        square_data.append({'top':tn, 'left':ln, 'right':rn, 'bottom':bn,
                            'orders':[len(top),len(left),len(right),len(bottom)],
                            'edge_indices_top_left_top_right_left_bottom_right_bottom':[
                                len(top)//len(left),len(top)//len(right),
                                len(left)//len(bottom),len(right)//len(bottom)]})
    R['G03_derived_groups_and_lattice'] = {
        'GL_order':len(G), 'SL_order':len(SL), 'kernel_reduction_order':len(K),
        'derived_SL_order':len(DSL), 'derived_SL_is_A4_via_I':True,
        'derived_GL_order':len(DG), 'derived_GL_equals_derived_SL_times_Z':True,
        'SL_abelianization_element_order_counts':sl_orders,
        'GL_abelianization_element_order_counts':gl_orders,
        'SL_abelianization_generator_matrix':U,
        'GL_conjugation_on_SL_abelianization':'g.[U]=det(g)*[U] in additive C4',
        'SL_reduction_extension_splits':False,
        'SL_elements_with_square_one':len(sl_involutions),
        'center_GL':sorted(center(G)), 'center_SL':sorted(center(SL)),
        'chosen_S4_complement_order':len(S4section),
        'kernel_sign_det_is_chosen_S4_times_Z':True,
        'five_cartesian_subgroup_squares':square_data,
        'splittings_depend_on_P_basepoint':True,
    }

    # Octahedron vertices, faces, bifaces, and all of their characters.
    primitive = tuple(v for v in it.product(range(4), repeat=2) if any(x%2 for x in v))
    def cls(v):
        return min(v, tuple(-x % 4 for x in v))
    vertices = tuple(sorted({cls(v) for v in primitive}))
    vi = {v:i for i,v in enumerate(vertices)}
    pairs = tuple(tuple(i for i,v in enumerate(vertices) if tuple(x%2 for x in v)==j) for j in J)
    assert len(vertices) == 6 and all(len(p) == 2 for p in pairs)
    pairset = {frozenset(p) for p in pairs}
    ant = tuple(next(j for pair in pairs if i in pair for j in pair if j!=i) for i in range(6))
    PO = {g:tuple(vi[cls(mv(g,v))] for v in vertices) for g in G}
    Oct = set(PO.values())
    all_oct = {p for p in it.permutations(range(6))
               if {frozenset(p[i] for i in pair) for pair in pairs} == pairset}
    assert Oct == all_oct and len(Oct) == 48
    assert {g for g in G if PO[g] == tuple(range(6))} == set(Z)
    oct_center = {p for p in Oct if all(compose(p,q)==compose(q,p) for q in Oct)}
    assert oct_center == {tuple(range(6)),ant}
    faces = tuple(sorted(frozenset(f) for f in it.product(*pairs)))
    assert len(faces) == 8
    def pf(p):
        return frozenset(vi[cls(v)] for v in p)
    facefibres = {f:{p for p in P if pf(p)==f} for f in faces}
    assert all(len(fibre)==2 for fibre in facefibres.values())
    assert {frozenset(fibre) for fibre in facefibres.values()} == set(partition_orbits(P,Z,act))
    def anti_face(f):
        return frozenset(ant[i] for i in f)
    bifaces = {frozenset((f,anti_face(f))) for f in faces}
    assert len(bifaces) == 4
    assert {frozenset(pf(p) for p in orb) for orb in Iorbs} == bifaces
    def face_color(f):
        return sum(pair[1] in f for pair in pairs) % 2
    facechars = {}
    for g in G:
        differences = {face_color(f)^face_color(frozenset(PO[g][i] for i in f)) for f in faces}
        assert len(differences) == 1
        facechars[g] = differences.pop()
        assert facechars[g] == dchar[g]
        assert (sg[g] ^ facechars[g]) == dt[g]
        assert all(pf(act(g,p)) == frozenset(PO[g][i] for i in pf(p)) for p in P)
    rotations = {PO[g] for g in G if dt[g] == 0}
    assert len(rotations) == 24 and {PO[g] for g in SL} == rotations
    assert ant not in rotations
    assert {compose(p,a) for p in rotations for a in (tuple(range(6)),ant)} == Oct
    # PSL2(Z4) -> permutations of I is exactly S4, with kernel +/-I upstairs.
    assert {PI[g] for g in SL} == S4
    assert {g for g in SL if PI[g] == tuple(range(4))} == set(Z)
    assert {g for g in G if PO[g] in oct_center} == set(KW)
    oriented_twist = {g:compose(ant,PO[g]) if dt[g] else PO[g] for g in G}
    assert set(oriented_twist.values()) == rotations
    assert {g for g in G if oriented_twist[g]==tuple(range(6))} == set(KW)
    oct_edges = {frozenset((i,j)) for i in range(6) for j in range(i+1,6)
                 if not any(i in p and j in p for p in pairs)}
    assert len(oct_edges) == 12
    R['G04_octahedron'] = {
        'vertices_representatives':vertices, 'opposite_pairs_vertex_indices':pairs,
        'antipode_permutation':ant, 'vertices':6, 'edges':len(oct_edges), 'faces':len(faces),
        'bifaces':len(bifaces), 'GL_image_order':len(Oct), 'GL_action_kernel':sorted(Z),
        'SL_image_rotation_order':len(rotations), 'PSL2_Z4_equals_S4_via_I':True,
        'face_map_P_mod_Z_bijective':True, 'biface_map_I_bijective':True,
        'face_color_character':'det_bit + sign(reduction)',
        'octahedron_orientation_character':'det_bit',
        'biface_and_opposite_pair_orientation_character':'sign(reduction)',
        'center_preimage_in_GL':sorted(KW),
        'full_automorphism_group_is_rotations_times_antipode':True,
        'orientation_twist_action_image_order':24,
        'orientation_twist_action_kernel':sorted(KW),
    }

    # Exact extension cocycle: D8 -> (codiagonal bit c, diagonal bit d).
    zq = (1,1,0)
    for c,d,cp,dp in it.product(range(2), repeat=4):
        left = square_mul(square_section(c,d),square_section(cp,dp))
        right = square_section(c^cp,d^dp)
        if c*dp:
            right = square_mul(zq,right)
        assert left == right
    # Identify Aut(Oct) with S4(I) x C2(face colors), then choose the section
    # with square part (d,0,sign(s)).  Test every pair in the order-48 quotient.
    QH = {(PI[g],dchar[g]) for g in G}
    assert QH == {(s,d) for s in S4 for d in (0,1)}
    section = {}
    for s,d in QH:
        candidates = [g for g in G if PI[g]==s and Q[g]==square_section(parity(s),d)]
        assert len(candidates)==1
        section[(s,d)] = candidates[0]
    for (s,d),(sp,dp) in it.product(QH,repeat=2):
        target = section[(compose(s,sp),d^dp)]
        if parity(s)*dp:
            target = mul((3,0,0,3),target)
        assert mul(section[(s,d)],section[(sp,dp)]) == target
    # One explicit order-two quotient element with no order-two lift.
    odd_involutions = [s for s in S4 if parity(s)==1 and compose(s,s)==tuple(range(4))]
    s = min(odd_involutions)
    bad_g = section[(s,1)]
    assert mul(bad_g,bad_g) == (3,0,0,3)
    assert mul(mul((3,0,0,3),bad_g),mul((3,0,0,3),bad_g)) == (3,0,0,3)
    assert (3,0,0,3) in DG  # An independent obstruction to central splitting.
    R['G05_lifting_obstruction'] = {
        'D8_section':'q(c,d)=((d,0),c)', 'D8_cocycle':'c*d_prime mod 2',
        'D8_pair_checks':16, 'GL_quotient_pair_checks':len(QH)**2,
        'quotient_coordinates':'(s in S4(I), d=face_color_bit)',
        'GL_section_rule':'I_action=s and square_part=(d,0,sign(s))',
        'GL_cocycle':'sign(s)*d_prime mod 2, central generator -I',
        'central_extension_splits':False,
        'obstructed_C2_action_quotient_I_permutation':s,
        'obstructed_C2_action_face_color_bit':1,
        'obstructed_C2_action_lift_matrix':bad_g,
        'both_lifts_square_to_minus_I':True,
        'cohomological_inference':'[codiagonals] cup [diagonals] in H^2(base,C2)',
        'scope':'A locally constant torsor lifting problem; not nonexistence of an individual ordinary octahedron model.',
    }

    # Finite bridge only: the specified cusp generator convention modulo 4.
    U = (1,0,1,1)
    cycle = ((1,0),(1,1),(1,2),(1,3))
    fixed = ((0,1),(2,1))
    assert U in SL
    assert all(cls(mv(U,cycle[i])) == cycle[(i+1)%4] for i in range(4))
    assert all(cls(mv(U,v)) == v for v in fixed)
    assert mul(mul(U,U),mul(U,U)) == E and mul(U,U) != E
    R['G06_unipotent_bridge'] = {
        'matrix':U, 'convention':'left action on column vectors, representative=min(v,-v)',
        'cycle':cycle, 'fixed_representatives':fixed, 'order':4,
        'scope':'Finite level-4 permutation witness only; no cusp geometry or congruence invariance is inferred.',
    }
    return R


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('group_checks_results.json'))
    args = parser.parse_args()
    script = Path(__file__).resolve()
    combined = script.parent.parent / 'MPL_64_002-039_transcription.tex'
    frozen_hash = hashlib.sha256(combined.read_bytes()).hexdigest()
    assert frozen_hash == FROZEN_SHA256, 'Combined fragment differs from the frozen source binding.'
    result = {
        'schema':'MPL64 finite certificate 1',
        'agent':'GPT-6 Astra Pro /root/delivery_tooling',
        'arithmetic':'Exact integers reduced modulo 2 or 4; no external packages or database.',
        'script_sha256':hashlib.sha256(script.read_bytes()).hexdigest(),
        'frozen_transcription_sha256':frozen_hash,
        'checks':run(),
        'all_assertions_passed':True,
    }
    args.output.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({'all_assertions_passed':True,'output':str(args.output.resolve()),
                      'groups':{k:result['checks']['G03_derived_groups_and_lattice'][k]
                                for k in ('GL_order','SL_order','derived_GL_order','derived_SL_order')},
                      'central_extension_splits':False},ensure_ascii=False))


if __name__ == '__main__':
    main()
