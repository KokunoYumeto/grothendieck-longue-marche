#!/usr/bin/env python3
"""Apply approved count exclusions without changing manuscript readings or audit history."""
import copy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / 'workflow' / 'substantive_count_reclassification.json'
PLAN = json.loads(r'''{
  "remove": [
    "054-06",
    "057-06",
    "057-08",
    "060-23",
    "060-25",
    "061-04",
    "062-17",
    "062-18",
    "062-19",
    "063-15",
    "063-26",
    "064-26",
    "065-12",
    "066-01",
    "066-05",
    "067-39",
    "071-29",
    "072-05",
    "073-10",
    "073-13",
    "073-16",
    "074-35",
    "074-49",
    "077-12"
  ],
  "clear": {
    "058-01": "against_C",
    "063-04": "against_C",
    "065-13": "against_C",
    "066-22": "against_C",
    "068-04": "against_C",
    "068-08": "against_C",
    "073-03": "against_H"
  }
}''')
SUMMARY_EDITS = json.loads(r'''[
  [
    61,
    [
      "notes",
      6
    ],
    "Completed 13 single crops, all viewed, and 16 substantive change rows against at least one witness.",
    "First-stage completion recorded 13 single crops, all viewed, and 16 comparison rows against at least one witness."
  ],
  [
    62,
    [
      "notes",
      7
    ],
    "three comparison rows record the preferred calligraphic representation against H, while no clear alphabet resolution or settled witness error is asserted.",
    "the three comparisons remain documented as unresolved, with no settled alphabet choice or substantive H error counted."
  ],
  [
    64,
    [
      "notes",
      6
    ],
    "The completed report has 29 substantive comparison rows, two MARKS decisions in source order, and 13 second-reading boxes.",
    "Before the final counting review, the report had 29 comparison rows, two MARKS decisions in source order, and 13 second-reading boxes."
  ],
  [
    65,
    [
      "notes",
      8
    ],
    "After the blind audit there are16 substantive comparison rows:6 against C and11 against H.",
    "Before the final counting review, the blind audit report listed 16 comparison rows: 6 against C and 11 against H."
  ],
  [
    67,
    [
      "notes",
      6
    ],
    "There are 41 substantive comparison rows and 13 second-reading boxes;",
    "The earlier classification had 41 comparison rows and 13 second-reading boxes;"
  ],
  [
    72,
    [
      "root_review_notes"
    ],
    "excluded from the 20 substantive changes.",
    "excluded from the 19 substantive changes."
  ],
  [
    74,
    [
      "notes",
      8
    ],
    "The comparison has fifty substantive rows;",
    "The earlier classification contained fifty comparison rows;"
  ],
  [
    74,
    [
      "witness_comparison"
    ],
    "Fifty substantive rows are recorded;",
    "The earlier classification recorded fifty comparison rows;"
  ],
  [
    77,
    [
      "notes",
      6
    ],
    "This report contains 36 substantive comparison rows,",
    "Before the final counting review, this report contained 36 comparison rows,"
  ]
]''')
SCANS = sorted({int(row_id[:3]) for row_id in PLAN['remove']} |
               {int(row_id[:3]) for row_id in PLAN['clear']})


def counts(record):
    rows = record['changes']
    return {'rows': len(rows),
            'against_C': sum(bool(row.get('against_C')) for row in rows),
            'against_H': sum(bool(row.get('against_H')) for row in rows)}


def transform(scan, before):
    after = copy.deepcopy(before)
    removals = [rid for rid in PLAN['remove'] if int(rid[:3]) == scan]
    clears = {rid: flag for rid, flag in PLAN['clear'].items() if int(rid[:3]) == scan}
    by_id = {row['id']: row for row in after['changes']}
    if len(by_id) != len(after['changes']):
        raise SystemExit(f'{scan}: duplicate row ID')
    for rid in removals:
        if rid not in by_id:
            raise SystemExit(f'{scan}: missing original removal row {rid}')
    for rid, flag in clears.items():
        if rid not in by_id or by_id[rid].get(flag) is not True:
            raise SystemExit(f'{scan}: unexpected original flag for {rid}.{flag}')
        by_id[rid][flag] = False
        other = 'against_H' if flag == 'against_C' else 'against_C'
        if by_id[rid].get(other) is not True:
            raise SystemExit(f'{scan}: mixed row {rid} would have no substantive difference')
    after['changes'] = [row for row in after['changes'] if row['id'] not in removals]
    for edit_scan, field_path, old, new in SUMMARY_EDITS:
        if edit_scan != scan:
            continue
        target = after
        for key in field_path[:-1]:
            target = target[key]
        key = field_path[-1]
        if target[key].count(old) != 1:
            raise SystemExit(f'{scan}: unexpected summary at {field_path}')
        target[key] = target[key].replace(old, new, 1)
    total = counts(after)
    note = (f"Current substantive comparison counts after the final classification review: "
            f"{total['rows']} rows, {total['against_C']} against C and "
            f"{total['against_H']} against H; a row may differ from both witnesses. ")
    if removals:
        note += ("Unresolved comparisons " + ', '.join(removals)
                 + " are excluded from these substantive counts. ")
    if clears:
        note += ("Rows " + ', '.join(f"{rid} ({flag}=false)" for rid, flag in clears.items())
                 + " retain only their independently supported witness differences. ")
    note += ("Complete earlier records and excluded comparisons are preserved separately in "
             "workflow/substantive_count_reclassification.json. Earlier first-stage or audit "
             "totals describe their historical classification; these are the current counts. "
             "No page reading, doubt or adjudication was changed by this counting review.")
    after.setdefault('notes', []).append(note)
    allowed = {'changes', 'notes', 'root_review_notes', 'witness_comparison'}
    if any(before.get(key) != after.get(key) for key in set(before) | set(after)
           if key not in allowed):
        raise SystemExit(f'{scan}: unexpected change outside approved metadata fields')
    return after


def main():
    if ARCHIVE.exists():
        archive = json.loads(ARCHIVE.read_text())
        if archive['operations'] != PLAN or archive['summary_edits'] != SUMMARY_EDITS:
            raise SystemExit('Existing archive belongs to a different repair plan')
    else:
        snapshots = {}
        excluded = []
        mixed = []
        for scan in SCANS:
            name = f'147_scan{scan:03}.json'
            source = (ROOT / 'reviewed' / name).read_text()
            record = json.loads(source)
            after = transform(scan, record)
            snapshots[name] = {
                'source_sha256': hashlib.sha256(source.encode()).hexdigest(),
                'record': record,
                'counts_before': counts(record),
                'counts_after': counts(after),
            }
            for row in record['changes']:
                rid = row['id']
                if rid in PLAN['remove']:
                    reason = ('The accent remains unresolved; the independent H delimiter/ellipsis '
                              'difference stays in 073-11.' if rid == '073-10' else
                              'Retained alternatives do not establish a substantive witness error.')
                    excluded.append({'scan': scan, 'id': rid, 'counted_after': False,
                                     'reason': reason, 'original_record': row})
                elif rid in PLAN['clear']:
                    mixed.append({'scan': scan, 'id': rid,
                                  'cleared_flag': PLAN['clear'][rid],
                                  'original_record': row})
        archive = {
            'created_utc': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
            'purpose': 'Immutable pre-repair record of approved substantive-count corrections',
            'operations': PLAN,
            'summary_edits': SUMMARY_EDITS,
            'pre_repair_records': snapshots,
            'excluded_comparisons': excluded,
            'mixed_flag_corrections': mixed,
        }
        ARCHIVE.parent.mkdir(exist_ok=True)
        with ARCHIVE.open('x') as handle:
            json.dump(archive, handle, ensure_ascii=False, indent=2)
            handle.write('\n')
    results = []
    for scan in SCANS:
        name = f'147_scan{scan:03}.json'
        path = ROOT / 'reviewed' / name
        before = archive['pre_repair_records'][name]['record']
        after = transform(scan, before)
        # Re-read immediately before deciding whether to write; never overwrite newer work.
        current = json.loads(path.read_text())
        if current == after:
            state = 'already current'
        elif current == before:
            path.write_text(json.dumps(after, ensure_ascii=False, indent=2) + '\n')
            state = 'updated'
        else:
            raise SystemExit(f'{name}: changed since archival snapshot; refusing overwrite')
        results.append({'scan': scan, 'state': state, **counts(after)})
    print(json.dumps({'removed_rows': len(PLAN['remove']),
                      'mixed_flags_cleared': len(PLAN['clear']),
                      'archive': str(ARCHIVE), 'pages': results}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()

