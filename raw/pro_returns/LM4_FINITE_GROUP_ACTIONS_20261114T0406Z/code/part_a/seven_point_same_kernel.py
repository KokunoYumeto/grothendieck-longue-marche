#!/usr/bin/env python3
"""Exact A4 relabelling certificate for the twelve F.7 seven-point maps.

No numerical braid computation is used.  The geometric identity is
f_(hI) = r_h o f_I in M_0,7, because all coordinates acquire the same
Mobius transformation h.  This program certifies the finite label data.
"""
import contextlib
import io
import json
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    import a5_centralizer_permutations as a


I = min(a.seven_point_sets, key=lambda s: sorted(s))
labels = sorted(I)
rows = []
seen = set()
for h in sorted(a.A4):
    action = a.vertex_action(h)
    J = frozenset(action[i] for i in I)
    target = sorted(J)
    assert J in a.seven_point_sets
    assert J not in seen
    seen.add(J)
    reindex = [target.index(action[i]) for i in labels]
    assert sorted(reindex) == list(range(7))
    for i in labels:
        assert a.group_labels[action[i]] == a.mul(h, a.group_labels[i])
    rows.append({
        'left_multiplier': list(h),
        'target_subset': target,
        'source_to_target_positions': reindex,
    })
assert seen == a.seven_point_sets

V4 = {g for g in a.A4 if g == a.one or a.mul(g, g) == a.one}
assert len(V4) == 4
cosets = sorted({frozenset(a.label_vertices[a.mul(g, v)] for v in V4)
                 for g in a.A4}, key=lambda c: sorted(c))
coset_rows = [{'coset': sorted(c), 'retained': sorted(c & I)} for c in cosets]
assert sorted(len(c & I) for c in cosets) == [2, 2, 3]
assert all(not c <= J for c in cosets for J in a.seven_point_sets)

twist_rows = []
for J in sorted(a.seven_point_sets, key=lambda s: sorted(s)):
    for j, partition in enumerate(a.partitions):
        essential = sorted((c & J for c in partition if len(c & J) >= 2),
                           key=lambda c: sorted(c))
        assert essential
        disk = essential[0]
        e = len(a.cyclic_subgroups[j])
        assert 2 <= len(disk) <= e <= 3
        assert len(J - disk) >= 4
        inside = sorted(disk)[:2]
        outside = sorted(J - disk)[:2]
        four = frozenset(inside + outside)
        survivors = [c & four for c in partition if len(c & four) == 2]
        # On S_0,4 each surviving boundary cuts the same two-two partition.
        assert all(c == frozenset(inside) or c == frozenset(outside)
                   for c in survivors)
        assert len(survivors) in (1, 2)
        twist_rows.append({'seven_labels': sorted(J), 'inertia_order': e,
                           'stabilizer_index': j, 'four_retained_labels': sorted(four),
                           'twist_character_on_primitive_source_cusp': len(survivors)})
assert len(twist_rows) == 12 * 7

output = {
    'base_subset': labels,
    'A4_order': len(a.A4),
    'seven_point_subsets': len(a.seven_point_sets),
    'A4_left_orbit_size': len(seen),
    'base_subset_stabilizer_order': 1,
    'relabelled_maps': rows,
    'V4_cosets': coset_rows,
    'V4_coset_intersection_sizes': [2, 2, 3],
    'contains_full_V4_coset': False,
    'twist_partition_checks': len(twist_rows),
    'four_point_twist_detection': twist_rows,
    'proved_map_identity': 'f_(hI) = r_h o f_I in M_0,7; common Mobius h is removed.',
    'proved_kernel_identity': 'All twelve discrete kernels coincide, and all twelve completed kernels coincide.',
    'profinite_cusp_detection': 'Every primitive source cusp maps, after the named four-point forget map and a twist character, to 1 or 2 in Zhat; all full cusp groups and their conjugates embed.',
    'scope': 'This proves equality of the kernels and detects all full source cusp groups. It neither proves injectivity nor produces a nontrivial seven-point kernel word.',
}
path = Path(__file__).with_name('seven_point_same_kernel_output.json')
path.write_text(json.dumps(output, indent=2) + '\n')
print(json.dumps(output, indent=2))
