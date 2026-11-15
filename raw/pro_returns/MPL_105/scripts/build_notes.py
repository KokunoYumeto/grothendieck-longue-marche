#!/usr/bin/env python3
"""Assemble root-authored notes and attach supplied register locators.

This script does not interpret manuscript or context content. Root authored all
assessment text; the inputs contain bibliographic locators, not source scans.
"""
from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
sources = json.loads((root / 'records/comparison_source_locators.json').read_text())
annotations = {}
for number, line in enumerate((root / 'records/dossier_annotations.tsv').read_text().splitlines(), 1):
    if not line.strip() or line.startswith('#'):
        continue
    fields = line.split(' || ')
    if len(fields) != 5:
        raise ValueError(f'Annotation line {number}: expected 5 fields')
    ident, title, location, kind, body = fields
    if ident in annotations:
        raise ValueError(f'Duplicate root annotation: {ident}')
    annotations[ident] = (title, location, kind, body)
expected = {r['id'] for r in sources}
if set(annotations) - expected:
    raise ValueError(f'Unexpected IDs: {sorted(set(annotations) - expected)}')

output = ['## Individual comparison of every dossier statement\n',
          'Each heading identifies exactly one row of the supplied '
          '`DOSSIER_STATEMENTS_WITH_STATUS.md`. The register status is quoted '
          'as a claim, including when its label says “Proved” or “Known”; '
          'no independent review is inferred from that label. Source-line '
          'numbers locate the supplied Markdown register, while manuscript '
          'references are reproduced from its locator cell.\n']
current_group = None
for row in sources:
    ident = row['id']
    if ident not in annotations:
        continue
    group = ident.split()[0]
    if group != current_group:
        output.append(f'## Dossier family: {group}\n')
        current_group = group
    title, location, kind, body = annotations[ident]
    refs = row['refs'] or 'No manuscript-page locator supplied in this row'
    output.extend([
        f'### {ident} — {title}\n',
        f'**Location:** {location}. **Kind:** {kind}. '
        f'**Context:** *DOSSIER_STATEMENTS_WITH_STATUS* (n.d.), '
        f'`DOSSIER_STATEMENTS_WITH_STATUS.md`, {ident}, source line '
        f'{row["source_line"]}; {refs}. **Register status:** {row["status"]}.\n',
        body + '\n'
    ])
part = root / 'records/notes_parts/04_dossier.md'
part.write_text('\n'.join(output))
parts = sorted((root / 'records/notes_parts').glob('*.md'))
final = root / 'MPL_105_notes.md'
final.write_text('\n'.join(p.read_text().rstrip() + '\n' for p in parts))
print(json.dumps({'dossier_entries_written': len(annotations),
                  'dossier_entries_expected': len(sources),
                  'missing': [r['id'] for r in sources if r['id'] not in annotations],
                  'notes_bytes': final.stat().st_size,
                  'notes_words': len(final.read_text().split())}, ensure_ascii=False))
