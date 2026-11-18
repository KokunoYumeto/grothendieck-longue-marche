#!/usr/bin/env python3
"""Exact coverage of the historical list in task E2, not proof certification."""
from pathlib import Path
import csv
import re

root = Path(__file__).resolve().parents[1]
historical = {r['historical_id']: r for r in csv.DictReader(
    (root / 'notes/historical_audit.csv').open())}
required = ['SECTIONS_OVER_Q A.' + str(n) for n in
            (25, 32, 42, 44, 48, 50, 51, 52, 59, 65, 72,
             137, 139, 196, 207, 209)]
required += [f'GT_TOWER_CHECK C.{part}.{n}'
             for part, last in ((1, 21), (2, 18), (3, 11))
             for n in range(1, last + 1)]
main = (root / 'SECTION_GHOSTS_paper.tex').read_text()
inputs = [root / (name + '.tex')
          for name in re.findall(r'\\input\{([^}]+)\}', main)]
integrated = set()
for source in inputs:
    integrated.update(re.findall(r'\\begin\{result\}\s*\{([^}]+)\}',
                                 source.read_text()))
assert len(required) == len(set(required)) == 66
for identifier in required:
    row = historical[identifier]
    assert row['audit_status'] == 'confirmed', (identifier, row['audit_status'])
    proofs = row['current_proof_files'].split('; ')
    for proof in proofs:
        assert (root / proof).is_file(), (identifier, proof)
    statements = row['current_statements'].split('; ')
    assert statements and all(s in integrated for s in statements), (identifier, statements)
    print(identifier, 'confirmed', '; '.join(statements), sep='\t')
pending = [i for i, r in historical.items() if r['audit_status'] == 'pending']
assert not set(pending).intersection(required)
print('PASS: all16 specified SQ statements and all50 specified GT C statements are confirmed and have integrated proof references.')
print('Additional pending E1/L5 claims:', '; '.join(pending))
print('Coverage is a finite accounting check; the full mathematical proofs and actual independent reviews are separate.')
