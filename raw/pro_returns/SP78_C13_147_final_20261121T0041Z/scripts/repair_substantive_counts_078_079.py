#!/usr/bin/env python3
"""Apply the four approved final count exclusions on scans078 and079."""
import copy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / 'workflow' / 'substantive_count_reclassification_078_079.json'
REMOVE = {78: ['078-04', '078-29'], 79: ['079-01', '079-37']}


def counts(record):
    return {'rows': len(record['changes']),
            'against_C': sum(bool(row['against_C']) for row in record['changes']),
            'against_H': sum(bool(row['against_H']) for row in record['changes'])}


def transform(scan, before):
    after = copy.deepcopy(before)
    ids = REMOVE[scan]
    found = [row['id'] for row in before['changes'] if row['id'] in ids]
    if sorted(found) != sorted(ids) or not before.get('audit_complete'):
        raise SystemExit(f'{scan}: expected finalized original rows are missing')
    after['changes'] = [row for row in after['changes'] if row['id'] not in ids]
    total = counts(after)
    note = (f"Current substantive comparison counts after the final classification review: "
            f"{total['rows']} rows, {total['against_C']} against C and "
            f"{total['against_H']} against H; a row may differ from both witnesses. "
            f"Unresolved comparisons {', '.join(ids)} are excluded from these counts. ")
    if scan == 78:
        note += ("The independently established geometry and omissions remain counted in "
                 "078-02; the unresolved roof does not create another substantive error. ")
    note += ("Complete earlier records and excluded comparisons are preserved separately in "
             "workflow/substantive_count_reclassification_078_079.json. Earlier review totals "
             "describe their historical classification; these are the current counts. "
             "No page reading, doubt or adjudication was changed by this counting review.")
    after.setdefault('notes', []).append(note)
    if any(before.get(key) != after.get(key) for key in set(before) | set(after)
           if key not in {'changes', 'notes'}):
        raise SystemExit(f'{scan}: unexpected field modification')
    return after


def main():
    if ARCHIVE.exists():
        archive = json.loads(ARCHIVE.read_text())
        if archive['remove'] != {str(k): v for k, v in REMOVE.items()}:
            raise SystemExit('Existing archive has a different repair plan')
    else:
        snapshots = {}
        excluded = []
        for scan, ids in REMOVE.items():
            name = f'147_scan{scan:03}.json'
            source = (ROOT / 'reviewed' / name).read_text()
            before = json.loads(source)
            after = transform(scan, before)
            snapshots[name] = {
                'source_sha256': hashlib.sha256(source.encode()).hexdigest(),
                'record': before,
                'counts_before': counts(before),
                'counts_after': counts(after),
            }
            for row in before['changes']:
                if row['id'] in ids:
                    excluded.append({'scan': scan, 'id': row['id'],
                                     'counted_after': False, 'original_record': row})
        archive = {
            'created_utc': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
            'purpose': 'Immutable pre-repair history of four approved unresolved comparisons',
            'remove': {str(k): v for k, v in REMOVE.items()},
            'pre_repair_records': snapshots,
            'excluded_comparisons': excluded,
        }
        ARCHIVE.parent.mkdir(exist_ok=True)
        with ARCHIVE.open('x') as handle:
            json.dump(archive, handle, ensure_ascii=False, indent=2)
            handle.write('\n')
    results = []
    for scan in REMOVE:
        name = f'147_scan{scan:03}.json'
        path = ROOT / 'reviewed' / name
        before = archive['pre_repair_records'][name]['record']
        after = transform(scan, before)
        # Read current content immediately before writing; preserve concurrent work.
        current = json.loads(path.read_text())
        if current == after:
            state = 'already current'
        elif current == before:
            path.write_text(json.dumps(after, ensure_ascii=False, indent=2) + '\n')
            state = 'updated'
        else:
            raise SystemExit(f'{name}: changed since archival snapshot; refusing overwrite')
        results.append({'scan': scan, 'state': state, **counts(after)})
    print(json.dumps({'archive': str(ARCHIVE), 'pages': results}, indent=2))


if __name__ == '__main__':
    main()

