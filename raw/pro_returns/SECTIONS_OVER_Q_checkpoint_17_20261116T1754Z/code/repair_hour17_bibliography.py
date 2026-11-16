#!/usr/bin/env python3
"""Synchronize the audited checkpoint bibliography back into its source fragments."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

w = Path(__file__).resolve().parents[1]
def entries(text):
    starts = list(re.finditer(r'(?m)^@\w+\{([^,]+),', text))
    return {
        m.group(1): text[m.start():starts[i+1].start() if i+1 < len(starts) else len(text)].strip()
        for i, m in enumerate(starts)
    }

previous_path = w / 'notes/checkpoint16_references_snapshot.bib'
previous = entries(previous_path.read_text())
names = ['base_references.bib', 'root_references.bib', 'birational_references.bib',
         'legendre_references.bib', 'local_agent_references.bib', 'metabelian_references.bib']
paths = [w / 'notes' / name for name in names]
texts = {p: p.read_text() for p in paths}
where = {}
current = {}
for p in paths:
    for k, entry in entries(texts[p]).items():
        assert k not in where
        where[k] = p
        current[k] = entry
missing = sorted(previous.keys() - current.keys())
changed = sorted(k for k in previous.keys() & current.keys() if previous[k] != current[k])
restored = []
for k in missing:
    assert re.search(r'\bverified\b', previous[k], re.I), k
    texts[w / 'notes/root_references.bib'] += '\n' + previous[k] + '\n'
    restored.append(k)
updated = []
for k in changed:
    # This source fragment retains an additional, already verified A127 local
    # reciprocity passage absent from the parent checkpoint. Its other content
    # is identical; preserve the larger verified note.
    if k == 'BIR_KedlayaCFT':
        assert 'Theorem 4.1.2 and Example 4.1.4' in current[k]
        continue
    p = where[k]
    assert texts[p].count(current[k]) == 1
    texts[p] = texts[p].replace(current[k], previous[k], 1)
    updated.append(k)
for p in paths:
    if texts[p] != p.read_text():
        p.write_text(texts[p])
proc = subprocess.run(['python', str(w / 'code/build_bibliography.py')],
                      capture_output=True, text=True, check=True)
final = entries((w / 'SECTIONS_OVER_Q_references.bib').read_text())
assert set(previous) <= set(final)
assert len(final) == 107
assert final['BIR_Darmon1995'] == current['BIR_Darmon1995']
assert all(final[k] == previous[k] for k in previous if k != 'BIR_KedlayaCFT')
record = {
    'reason': 'The old fragment builder omitted later parent-only entries and verification notes; the hourly archive preserved their audited text.',
    'checkpoint16_count': len(previous),
    'temporary_fragment_build_count': len(current),
    'restored_missing_entries': restored,
    'restored_later_verification_notes': updated,
    'retained_larger_fragment_note': 'BIR_KedlayaCFT',
    'final_count': len(final),
    'final_sha256': hashlib.sha256((w / 'SECTIONS_OVER_Q_references.bib').read_bytes()).hexdigest(),
    'all_checkpoint16_entries_preserved': True,
    'current_new_entry': 'BIR_Darmon1995'
}
(w / 'notes/hour17_bibliography_reconciliation.json').write_text(json.dumps(record, indent=2) + '\n')
out = proc.stdout + json.dumps(record, indent=2) + '\n'
(w / 'code/repair_hour17_bibliography_output.txt').write_text(out)
print(out, end='')
