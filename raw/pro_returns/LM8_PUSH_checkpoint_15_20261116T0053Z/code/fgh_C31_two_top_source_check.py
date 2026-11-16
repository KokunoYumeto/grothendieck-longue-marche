#!/usr/bin/env python3
"""Literal source checks supporting the independently audited top-two kernel.

This is the exact source of the initial executed inline check, retained as a
standalone program. It leaves every original pc/proof file unchanged.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent.parent
s = json.loads((ROOT / 'code/pbc_iterated_shortcut_v2_original_source.json').read_text())
r = json.loads((ROOT / 'code/pbc_two_top_module.json').read_text())
C = {(i, j): w for i, j, w in s['conjugates']}


def trunc(w, n):
    out = []
    for k, e in zip(w[::2], w[1::2]):
        if k <= n:
            out.extend((k, e))
    return out


assert all(s['relative_orders'][i - 1] == 2 and not s['powers'][i - 1]
           for i in range(105, 177))
assert all(C[i, j] == [i, 1]
           for i in range(105, 177) for j in range(105, i))
assert all(all(k >= 105 for k in C[i, j][::2])
           for i in range(105, 177) for j in range(1, i))
assert all(s['relative_orders'][i - 1] == 3 and not trunc(s['powers'][i - 1], 104)
           for i in range(87, 105))
assert all(trunc(C[i, j], 104) == [i, 1]
           for i in range(87, 105) for j in range(87, i))
assert all(all(k >= 87 for k in trunc(C[i, j], 104)[::2])
           for i in range(87, 105) for j in range(1, i))
assert s['s'] == [2, 1] and s['relative_orders'][1] == 2 and s['powers'][1] == []
S = {w[0] - 105 for w in s['s_centralizers']
     if len(w) == 2 and w[1] == 1 and w[0] >= 105}
assert len(S) == 36
M = [int(x, 16) for x in r['all_action_matrices_hex']['2']]
mask = sum(1 << i for i in S)
assert all((M[i] ^ (1 << i)) & ~mask == 0 for i in range(72))
out = {
    'status': 'PASS',
    'A_elementary_2_dimension': 72,
    'N_elementary_3_dimension': 18,
    'normal_suffix_comparisons_checked': True,
    'actual_involution_g2_verified': True,
    'norm_support_retained_centralizer_dimension': 36,
    'source_sha256': hashlib.sha256(
        (ROOT / 'code/pbc_iterated_shortcut_v2_original_source.json').read_bytes()
    ).hexdigest(),
}
(ROOT / 'notes/fgh_C31_two_top_source_check.json').write_text(
    json.dumps(out, indent=2) + '\n'
)
print(json.dumps(out))
