#!/usr/bin/env python3
"""Two exact branch-defect colors; no new group or relation-orbit search."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / 'records/root_coarse_corrections29.json'
data = json.loads(INPUT.read_text())
rows = {(r['section'], r['operator'], r['retained_generator']): r
        for r in data['rows']}

def chi_g(word):
    return sum((1 if z == 2 else -1 if z == -2 else 0) for z in word)

result = []
for section in ('old_c_section', 'local_C_section'):
    row = rows[section, 'v', 1]
    q = row['coarse_head_T']
    assert q == [3, 2, -3] and chi_g(q) == 1
    colors = {
        i: {tuple(t['retained_word_T']): t['coefficient']
            for t in row['module_coefficients'] if t['family_index_F11'] == i}
        for i in (2, 7)
    }
    assert colors[2] == {(): 1, (3, -2, -3): -1}
    assert colors[7] == {(3,): 1, (3, 2): -1}
    moments = {i: sum(chi_g(t) * n for t, n in colors[i].items())
               for i in (2, 7)}
    assert moments == {2: 1, 7: -1}
    assert {i: n % 3 for i, n in moments.items()} == {2: 1, 7: 2}
    record = {'section': section, 'q_T': q,
              'B_defect': [{'word_T': list(t), 'coefficient': n}
                           for t, n in sorted(colors[2].items())],
              'bar_B_defect': [{'word_T': list(t), 'coefficient': n}
                               for t, n in sorted(colors[7].items())],
              'forced_paired_augmentations': [moments[2], moments[7]],
              'forced_augmentations_mod3': [moments[2] % 3, moments[7] % 3]}
    result.append(record)
    print(section, 'PASS: entire two color defects; chi_g moments (1,-1); mod3 (1,2).')

out = {'status': 'PASS_EXACT_DELTA_FIXED_BRANCH_OBSTRUCTION_INPUT',
       'utc': datetime.now(timezone.utc).isoformat(),
       'input': str(INPUT.relative_to(ROOT)),
       'input_sha256': hashlib.sha256(INPUT.read_bytes()).hexdigest(),
       'results': result,
       'scope': 'Exact coefficient verification. The uniform moment identity, actual post-node descent, completed finite-target extension and section consequence are proved in the companion note.'}
target = ROOT / 'work_CE/next_symmetric_nodes/delta_fixed_branch_correction29.json'
assert not target.exists()
target.write_text(json.dumps(out, indent=2) + '\n')
print('PASS: delta-fixed classes have equal paired color augmentations, contradicting these required values.')
