#!/usr/bin/env python3
"""Final approved scan079 count correction; preserve the full original record."""
import copy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'reviewed' / '147_scan079.json'
ARCHIVE = ROOT / 'workflow' / 'substantive_count_reclassification_079_final.json'
BASIS = ("This row counts only H's omission of that separately recorded prefix group. "
         "It does not count a resolved reading of du or a resolved singular/plural distinction.")


def counts(record):
    return {'rows': len(record['changes']),
            'against_C': sum(bool(row['against_C']) for row in record['changes']),
            'against_H': sum(bool(row['against_H']) for row in record['changes'])}


def transform(before):
    after = copy.deepcopy(before)
    rows = {row['id']: row for row in after['changes']}
    if ('079-08' not in rows or '079-29' not in rows
            or not before.get('audit_complete')):
        raise SystemExit('Expected finalized original comparisons are missing')
    if rows['079-08']['against_C'] or not rows['079-08']['against_H']:
        raise SystemExit('Unexpected 079-08 witness flags')
    target = rows['079-29']
    if target['against_C'] or not target['against_H'] or 'separate' not in target['evidence']:
        raise SystemExit('Unexpected 079-29 counting basis')
    target['kind'] = 'omission'
    target['error_sheet_kind'] = 'omissions'
    target['evidence'] = target['evidence'].rstrip() + ' ' + BASIS
    after['changes'] = [row for row in after['changes'] if row['id'] != '079-08']
    total = counts(after)
    note = (f"Current substantive comparison counts after the final classification review: "
            f"{total['rows']} rows, {total['against_C']} against C and "
            f"{total['against_H']} against H; a row may differ from both witnesses. "
            "Unresolved comparisons 079-01, 079-08 and 079-37 are excluded from these counts. "
            "079-29 remains counted against H only for omission of the separate prefix group, "
            "without resolving du or the singular/plural ending. Complete earlier records and "
            "excluded comparisons are preserved in workflow/substantive_count_reclassification_078_079.json "
            "and workflow/substantive_count_reclassification_079_final.json. Earlier review totals "
            "describe their historical classification; these are the current counts. "
            "No page reading, doubt or adjudication was changed by this counting review.")
    indices = [i for i, value in enumerate(after['notes'])
               if value.startswith('Current substantive comparison counts after the final classification review:')]
    if len(indices) != 1:
        raise SystemExit('Expected one existing current-count note')
    after['notes'][indices[0]] = note
    if any(before.get(key) != after.get(key) for key in set(before) | set(after)
           if key not in {'changes', 'notes'}):
        raise SystemExit('Unexpected modification outside approved metadata fields')
    return after


def main():
    if ARCHIVE.exists():
        archive = json.loads(ARCHIVE.read_text())
        before = archive['pre_repair_record']
    else:
        source = PATH.read_text()
        before = json.loads(source)
        after = transform(before)
        original_rows = {row['id']: row for row in before['changes']
                         if row['id'] in {'079-08', '079-29'}}
        archive = {
            'created_utc': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
            'source_sha256': hashlib.sha256(source.encode()).hexdigest(),
            'operations': {'remove': ['079-08'], 'clarify_omission_basis': ['079-29']},
            'pre_repair_record': before,
            'original_comparison_records': original_rows,
            'counts_before': counts(before),
            'counts_after': counts(after),
        }
        with ARCHIVE.open('x') as handle:
            json.dump(archive, handle, ensure_ascii=False, indent=2)
            handle.write('\n')
    after = transform(before)
    # Fresh read immediately before writing; do not overwrite any concurrent edit.
    current = json.loads(PATH.read_text())
    if current == after:
        state = 'already current'
    elif current == before:
        PATH.write_text(json.dumps(after, ensure_ascii=False, indent=2) + '\n')
        state = 'updated'
    else:
        raise SystemExit('Current scan079 changed since archive; refusing overwrite')
    print(json.dumps({'scan': 79, 'state': state, **counts(after),
                      'removed': '079-08',
                      'clarified': '079-29 evidence/kind/error_sheet_kind',
                      'archive': str(ARCHIVE)}, indent=2))


if __name__ == '__main__':
    main()

