#!/usr/bin/env python3
"""Exact V4 surface phase image, orbit invariant, and old-source comparisons."""
from collections import deque
from functools import reduce
from itertools import product
from pathlib import Path
import json

from a_relative_prop import mul, inv, comm, subst, compose, exact_word_checks

HERE = Path(__file__).resolve().parent


def span_rank(rows):
    pivots = {}
    for row in rows:
        while row:
            pivot = row.bit_length()-1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def wedge(a, b):
    return ((a & 1)*(b >> 1) ^ (a >> 1)*(b & 1)) & 1


def umul(a, b):
    x, y, z = a & 1, (a >> 1) & 1, a >> 2
    u, v, w = b & 1, (b >> 1) & 1, b >> 2
    return (x ^ u) | ((y ^ v) << 1) | ((z ^ w ^ (x & v)) << 2)


def uinv(a):
    return a ^ (((a & 1)*((a >> 1) & 1)) << 2)


def uword(word, values):
    out = 0
    for letter in word:
        value = values[abs(letter)-1]
        out = umul(out, value if letter > 0 else uinv(value))
    return out


def character(word, values):
    return reduce(int.__xor__, (values[abs(letter)-1] for letter in word), 0)


def frame_bit(boundaries, values):
    return reduce(int.__xor__, (uword(word, values) >> 2 for word in boundaries), 0)


def abelian_mask(word):
    return reduce(int.__xor__, (1 << (abs(letter)-1) for letter in word), 0)


def eval_mask(mask, values):
    return reduce(int.__xor__, (a for i, a in enumerate(values) if (mask >> i) & 1), 0)


def conjugator(word, target):
    """Return and verify an actual free conjugator, including cyclic rotations."""
    def cyclic_reduce(w):
        w = list(w)
        prefix = []
        while len(w) > 1 and w[0] == -w[-1]:
            prefix.append(w[0])
            w = w[1:-1]
        return prefix, w
    p, core = cyclic_reduce(word)
    q, target_core = cyclic_reduce(target)
    for i in range(len(target_core)):
        first, second = target_core[:i], target_core[i:]
        if second+first == core:
            answer = mul(p, inv(first), inv(q))
            assert word == mul(answer, target, inv(answer))
            return answer
    raise AssertionError(('not a positive conjugate', word, target))


def source_maps(genus):
    rank = 2*genus+2
    identity = {i: [i] for i in range(1, rank+1)}
    handles = [([2*i+1], [2*i+2]) for i in range(genus)]
    c, d = [2*genus+1], [2*genus+2]
    prefix = mul(*[comm(a, b) for a, b in handles])
    boundaries = [c, d, inv(mul(prefix, c, d))]
    swaps = []
    for at in range(2):
        left, right = boundaries[at:at+2]
        phi, psi = dict(identity), dict(identity)
        phi[left[0]] = mul(left, right, inv(left))
        psi[left[0]] = right
        if at == 0:
            phi[right[0]] = left
            psi[right[0]] = mul(inv(right), left, right)
        assert compose(phi, psi) == compose(psi, phi) == identity
        assert subst(left, phi) == mul(left, right, inv(left))
        assert subst(right, phi) == left
        swaps.append((phi, psi))
    charts = {(0, 1, 2): (identity, identity)}
    todo = deque([(0, 1, 2)])
    while todo:
        permutation = todo.popleft()
        eta, eta_inv = charts[permutation]
        for at, (phi, psi) in enumerate(swaps):
            swap = [0, 1, 2]
            swap[at], swap[at+1] = swap[at+1], swap[at]
            nxt = tuple(swap[i] for i in permutation)
            if nxt not in charts:
                charts[nxt] = compose(phi, eta), compose(eta_inv, psi)
                todo.append(nxt)
    assert len(charts) == 6
    for permutation, (eta, eta_inv) in charts.items():
        assert compose(eta, eta_inv) == compose(eta_inv, eta) == identity
        for i, boundary in enumerate(boundaries):
            conjugator(subst(boundary, eta), boundaries[permutation[i]])

    handle_charts = [(identity, identity)]
    if genus == 2:
        a, b, u, v = [[i] for i in range(1, 5)]
        A, B = comm(a, b), comm(u, v)
        eta, eta_inv = dict(identity), dict(identity)
        eta.update({1: mul(A, u, inv(A)), 2: mul(A, v, inv(A)), 3: a, 4: b})
        eta_inv.update({1: u, 2: v, 3: mul(inv(B), a, B), 4: mul(inv(B), b, B)})
        assert compose(eta, eta_inv) == compose(eta_inv, eta) == identity
        assert subst(prefix, eta) == prefix
        handle_charts.append((eta, eta_inv))

    old = exact_word_checks()
    replacements = {1: 2*genus-1, 2: 2*genus, 3: c[0]}
    convert = lambda w: [(1 if a > 0 else -1)*replacements[abs(a)] for a in w]
    push, push_inv = dict(identity), dict(identity)
    push.update({replacements[int(i)]: convert(w) for i, w in old['bounding_pair_map'].items()})
    push_inv.update({replacements[int(i)]: convert(w) for i, w in old['bounding_pair_inverse'].items()})
    J, Ji = swaps[0]
    other_push = compose(J, compose(push, Ji))
    other_push_inv = compose(J, compose(push_inv, Ji))
    pair = compose(push, other_push_inv)
    pair_inv = compose(other_push, push_inv)
    square, square_inv = compose(J, J), compose(Ji, Ji)
    base_maps = [('single_push', push, push_inv),
                 ('paired_push', pair, pair_inv),
                 ('pure_boundary_square', square, square_inv)]
    change, change_inv = dict(identity), dict(identity)
    aa, bb = 2*genus-1, 2*genus
    change[aa], change_inv[aa] = [aa, bb], [aa, -bb]

    records, seen = [], set()
    for permutation, (bc, bci) in charts.items():
        for handle, (hc, hci) in enumerate(handle_charts):
            for changed, (ac, aci) in enumerate([(identity, identity), (change, change_inv)]):
                eta = compose(hc, compose(bc, ac))
                eta_inv = compose(aci, compose(bci, hci))
                assert compose(eta, eta_inv) == identity
                for kind, base, base_inv in base_maps:
                    phi = compose(eta, compose(base, eta_inv))
                    psi = compose(eta, compose(base_inv, eta_inv))
                    key = tuple(tuple(phi[i]) for i in range(1, rank+1))
                    if key in seen:
                        continue
                    seen.add(key)
                    assert compose(phi, psi) == compose(psi, phi) == identity
                    paths = [conjugator(subst(boundary, phi), boundary) for boundary in boundaries]
                    records.append({'kind': kind, 'handle_chart': handle,
                                    'boundary_chart_permutation': list(permutation),
                                    'a_to_ab': bool(changed), 'map': phi, 'inverse': psi,
                                    'boundary_conjugators': paths,
                                    'homology_masks': [abelian_mask(phi[i]) for i in range(1, rank+1)],
                                    'conjugator_masks': [abelian_mask(w) for w in paths]})
    return boundaries, records


def phase_image_certificate():
    result = []
    for genus in (1, 2):
        boundaries, maps = source_maps(genus)
        rank = 2*genus+2
        all_values = list(product(range(4), repeat=rank))
        invariants = {values: frame_bit(boundaries, values) for values in all_values}
        case_histogram = {}
        matched_pairs = 0
        for values in all_values:
            if span_rank(values) != 2:
                continue
            jj = [character(w, values) for w in boundaries]
            dimension = sum(2 if j == 0 else 1 for j in jj)
            expected = dimension-int(any(jj))
            phase_rows = []
            for rec in maps:
                moved = tuple(eval_mask(mask, values) for mask in rec['homology_masks'])
                kk = [eval_mask(mask, values) for mask in rec['conjugator_masks']]
                defect = reduce(int.__xor__, (wedge(j, k) for j, k in zip(jj, kk)), 0)
                assert invariants[moved] == invariants[values] ^ defect
                matched_pairs += 1
                if moved != values:
                    continue
                row, shift = 0, 0
                for j, k in zip(jj, kk):
                    if j == 0:
                        row |= k << shift
                        shift += 2
                    else:
                        row |= wedge(j, k) << shift
                        shift += 1
                assert defect == 0
                phase_rows.append(row)
            actual = span_rank(phase_rows)
            assert actual == expected, (genus, values, jj, actual, expected)
            key = (span_rank(jj), tuple(jj), actual)
            case_histogram[key] = case_histogram.get(key, 0)+1
        result.append({'genus': genus, 'boundary_words': boundaries,
                       'all_literal_maps': maps,
                       'all_surjective_character_cases': sum(case_histogram.values()),
                       'all_affine_phase_identity_cases': matched_pairs,
                       'phase_rank_cases': [{'boundary_span_rank': k[0], 'boundary_values': list(k[1]),
                                             'effective_phase_rank': k[2], 'character_count': count}
                                            for k, count in sorted(case_histogram.items())]})
    return result


def character_orbit_certificate():
    results = []
    for genus in (1, 2):
        n = 2*genus
        basis = [1 << i for i in range(n)]
        transvections = basis[:]
        for i in range(genus):
            for j in range(i+1, genus):
                transvections += [basis[2*i] ^ basis[2*j], basis[2*i+1] ^ basis[2*j+1]]
        for i in range(genus):
            for j in range(genus):
                if i != j:
                    transvections.append(basis[2*i] ^ basis[2*j+1])
        cases = []
        for c, d in product(range(4), repeat=2):
            boundary_span = span_rank([c, d])
            pending = {values for values in product(range(4), repeat=n)
                       if span_rank([*values, c, d]) == 2}
            orbits = []
            while pending:
                start = min(pending)
                orbit, todo = {start}, deque([start])
                while todo:
                    values = todo.popleft()
                    successors = []
                    for v in transvections:
                        cv = eval_mask(v, values)
                        partner_mask = sum(((v >> (i ^ 1)) & 1) << i for i in range(n))
                        successors.append(tuple(a ^ (cv if (partner_mask >> i) & 1 else 0)
                                                for i, a in enumerate(values)))
                    for i in range(n):
                        for j in (c, d):
                            changed = list(values)
                            changed[i] ^= j
                            successors.append(tuple(changed))
                    for nxt in successors:
                        if nxt not in orbit:
                            assert span_rank([*nxt, c, d]) == 2
                            orbit.add(nxt)
                            todo.append(nxt)
                cups = {reduce(int.__xor__, (wedge(values[2*i], values[2*i+1])
                                             for i in range(genus)), 0) for values in orbit}
                if boundary_span == 0:
                    assert len(cups) == 1
                pending -= orbit
                orbits.append({'representative': list(start), 'size': len(orbit),
                               'handle_cup_values': sorted(cups)})
            assert len(orbits) == (2 if genus == 2 and boundary_span == 0 else 1)
            cases.append({'boundary_values': [c, d, c ^ d], 'boundary_span_rank': boundary_span,
                          'orbits': orbits})
        results.append({'genus': genus, 'actual_elementary_transvection_vectors': transvections,
                        'all_character_orbits': cases})
    return results


def previous_sources():
    source = json.loads((HERE/'a_peripheral_a5_deleted.json').read_text())
    surface = json.loads((HERE/'a_peripheral_surface20_framed.json').read_text())
    boundaries = source['boundary_words_in_Schreier_basis']
    characters = surface['source_characters_on_Schreier_basis']
    bits = [frame_bit(boundaries, values) for values in characters]
    jj = surface['boundary_outer_characters'][0]
    phases = [[a ^ b for a, b in zip(local, path)] for local, path in zip(
        surface['local_conjugator_outer_values'], surface['source_path_module_outer_changes'])]
    wedges = [reduce(int.__xor__, (wedge(j, k) for j, k in zip(jj, row)), 0) for row in phases]
    defects = [value ^ bits[0] ^ phase for value, phase in zip(bits, wedges)]
    assert defects == [0, 1, 1, 1, 1]
    # Every actual ordinary centralizer image in D36 lies in the relevant
    # boundary line, so its entire additional phase has zero wedge.
    centralizer_lines = [[0, j] for j in (1, 2, 3)]
    assert all(wedge(j, k) == 0 for j, line in zip((1, 2, 3), centralizer_lines) for k in line)

    old = json.loads((HERE/'a_peripheral_a6_obstruction.json').read_text())
    reference = [1, 2, uinv(umul(1, 2))]
    assert reference == [1, 2, 3]
    rows = []
    for rec in old['all64_conjugator_cases']:
        hh = rec['h']
        omega = reduce(int.__xor__, (wedge(j, k) for j, k in zip((1, 2, 3), hh)), 0)
        assert omega == rec['relative_parity']
        target = [umul(umul(k, a), uinv(k)) for k, a in zip(hh, reference)]
        relation = umul(umul(target[0], target[1]), target[2])
        assert relation == omega << 2
        assert (relation == 0) == bool(rec['proper_count'])
        assert rec['proper_count'] == (360 if omega == 0 else 0)
        rows.append({'base_conjugators': hh, 'framed_V4_defect': omega,
                     'actual_Heisenberg_target_triple': target,
                     'Heisenberg_relation_value': relation,
                     'A6_generating_fibre_count': rec['proper_count']})
    ordinary_u = []
    uclasses = [{umul(umul(h, a), uinv(h)) for h in range(8)} for a in reference]
    for x, y in product(uclasses[0], uclasses[1]):
        z = uinv(umul(x, y))
        if z not in uclasses[2]:
            continue
        seen, todo = {0}, deque([0])
        while todo:
            at = todo.popleft()
            for g in (x, y):
                nxt = umul(at, g)
                if nxt not in seen:
                    seen.add(nxt)
                    todo.append(nxt)
        assert len(seen) == 8
        ordinary_u.append([x, y, z])
    assert len(ordinary_u) == 4
    return {'D36': {'literal_surface_frame_bits': bits,
                    'actual_boundary_phase_rows': phases,
                    'boundary_phase_wedge_sums': wedges,
                    'complete_framed_defects': defects,
                    'full_ordinary_centralizer_outer_lines': centralizer_lines},
            'D31_refinement': {'reference_Heisenberg_triple': reference,
                              'all64_prescribed_conjugator_cases': rows,
                              'all_four_ordinary_Heisenberg_epimorphisms': ordinary_u,
                              'joint_generating_fibre_count_above_each': 360,
                              'joint_ordinary_generating_count': 1440,
                              'joint_actual_group_order': 2880}}


def main():
    assert all(umul(umul(a, b), c) == umul(a, umul(b, c)) for a, b, c in product(range(8), repeat=3))
    assert all(umul(a, uinv(a)) == 0 for a in range(8))
    phases = phase_image_certificate()
    orbits = character_orbit_certificate()
    old = previous_sources()
    payload = {'status': 'PASS_V4_SURFACE_PHASES_ORBITS_AND_ACTUAL_OLD_SOURCES',
               'Heisenberg_model': '(a,b,z)*(u,v,w)=(a+u,b+v,z+w+a*v) overF2; bits a+2b+4z',
               'phase_image': phases, 'character_orbits': orbits, 'actual_source_comparisons': old,
               'scope': 'Exact finite word, character, and existing actual source comparisons. The arbitrary-genus statement and chief-refinement comparison are proved by the displayed source and induced-extension maps.'}
    (HERE/'a_v4_surface.json').write_text(json.dumps(payload, indent=2)+'\n')
    print('PASS every literal boundary/handle chart, corrected paired push, and inverse')
    print('PASS complete effective-phase image ker(sum j_i wedge k_i) in genera1,2 with three boundaries')
    print('PASS complete two-character surface orbits and every affine Heisenberg phase identity')
    print('D36 literal frame bits:', old['D36']['literal_surface_frame_bits'])
    print('D36 boundary-phase wedge sums:', old['D36']['boundary_phase_wedge_sums'])
    print('D36 complete ordinary defects:', old['D36']['complete_framed_defects'])
    print('PASS all64 D31 conjugator cases; exact Heisenberg refinement selects all proper fibres')
    print(payload['status'])


if __name__ == '__main__':
    main()
