#!/usr/bin/env python3
"""Stage an exact before/after proposal in work/; never edit authoritative files."""
from __future__ import annotations
import csv
import datetime as dt
import hashlib
import io
import json
from pathlib import Path

from other_error_aliases import ErrorAliases, FIELDS, row_key

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PROPOSAL = HERE / 'proposal'
TRANSACTION_ID = 'OE0001_exact_aliases_042_044_046'


def sha(content):
    return hashlib.sha256(content).hexdigest()


def main():
    if PROPOSAL.exists():
        raise ValueError('Proposal already exists; retain it and choose a new proposal directory before refreshing')
    before_table = (ROOT / 'deliverable/other_errors.tsv').read_bytes()
    reader = csv.DictReader(io.StringIO(before_table.decode('utf-8'), newline=''), delimiter='\t')
    if reader.fieldnames != list(FIELDS):
        raise ValueError('Unexpected error-table header')
    rows = list(reader)
    registry = json.loads((HERE / 'OTHER_ERROR_ALIASES.json').read_bytes())
    aliases = ErrorAliases(registry)
    if len({row_key(row) for row in rows}) != len(rows):
        raise ValueError('Unexpected exact duplicates; this proposal is only for the reviewed aliases')
    for entry in registry['aliases']:
        if entry['alias'] not in rows or entry['canonical'] not in rows:
            raise ValueError('Both exact reviewed rows must already exist before this transaction')
    after_rows = aliases.normalize(rows)
    removed = [entry['alias'] for entry in registry['aliases']]
    if after_rows != [row for row in rows if row not in removed]:
        raise ValueError('Normalization would change more than the three reviewed alias rows')
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fieldnames=FIELDS, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(after_rows)
    outputs = {
        'deliverable/scripts/other_error_aliases.py': (HERE / 'other_error_aliases.py').read_bytes(),
        'deliverable/audit/OTHER_ERROR_ALIASES.json': (HERE / 'OTHER_ERROR_ALIASES.json').read_bytes(),
        'deliverable/other_errors.tsv': stream.getvalue().encode('utf-8'),
        'deliverable/scripts/reconcile.py': (HERE / 'reconcile.py').read_bytes(),
    }
    manifest = {
        'schema_version': 1,
        'transaction_id': TRANSACTION_ID,
        'prepared_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
        'status': 'proposal_only_not_applied',
        'reason': 'Root-reviewed exact full-row aliases; no handwriting reassessment or source edit.',
        'before_rows': len(rows), 'after_rows': len(after_rows),
        'removed_alias_ids': [entry['id'] for entry in registry['aliases']],
        'install_order': list(outputs),
        'files': {},
        'protected_sha256': {},
    }
    for relative, after in outputs.items():
        path = ROOT / relative
        before = path.read_bytes() if path.exists() else None
        manifest['files'][relative] = {'before_sha256': sha(before) if before is not None else None,
                                       'after_sha256': sha(after)}
        for stage, content in [('before', before), ('after', after)]:
            if content is not None:
                target = PROPOSAL / stage / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(content)
    # Hash existing text audit/history files; do not inspect or copy scan images.
    audit = ROOT / 'deliverable/audit'
    for path in sorted(audit.rglob('*')):
        if path.is_file() and path.suffix in {'.json', '.tsv', '.md', '.txt', '.log', '.py', '.tex'}:
            relative = path.relative_to(ROOT).as_posix()
            if relative not in outputs:
                manifest['protected_sha256'][relative] = sha(path.read_bytes())
    for relative in ['deliverable/decisions.tsv', 'deliverable/CHECK_EVENTS.tsv', 'deliverable/progress.log']:
        manifest['protected_sha256'][relative] = sha((ROOT / relative).read_bytes())
    for entry in registry['aliases']:
        for relative, expected in entry['source_reports'].items():
            if sha((ROOT / relative).read_bytes()) != expected:
                raise ValueError(f'Reviewed report changed: {relative}')
            manifest['protected_sha256'][relative] = expected
    correction = (HERE / 'CORRECTION.md').read_bytes()
    (PROPOSAL / 'CORRECTION.md').write_bytes(correction)
    manifest['correction_sha256'] = sha(correction)
    (PROPOSAL / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'proposal': str(PROPOSAL), 'before_rows': len(rows), 'after_rows': len(after_rows),
                      'protected_files': len(manifest['protected_sha256']), 'applied': False}))


if __name__ == '__main__':
    main()
