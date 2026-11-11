#!/usr/bin/env python3
"""Build and audit the statement, reading and condition registers.

This is a metadata consistency check, not a mathematical proof checker.
All input records are included in ledger_inputs/. Run from any directory.
"""
from pathlib import Path
import csv
import json
import re
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
INPUT = Path(__file__).resolve().parent / 'ledger_inputs'
PREFIX = 'LM2_LOOP_EQUATIONS'
FIELDS = ['id', 'statement', 'status', 'where_proved', 'depends_on',
          'manuscript_passages (section; folio; scan)',
          'depends_on_doubtful_reading (scan, alternatives)', 'notes']
READING_FIELDS = ['package', 'scan', 'the \\unsure or \\illegible place',
                  'what the mathematics supports', 'how strongly']

def expand(path):
    text = path.read_text()
    def sub(match):
        child = ROOT / (match.group(1) + '.tex')
        return expand(child)
    return re.sub(r'\\input\{([^}]+)\}', sub, text)

def write_csv(path, fields, rows):
    with path.open('w', newline='', encoding='utf-8') as out:
        writer = csv.DictWriter(out, fields, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)

def main():
    ordered_claims = re.findall(r'\\begin\{claim\}\{([^}]+)\}\{([^}]+)\}',
                               expand(ROOT / (PREFIX + '_paper.tex')))
    ids = [c[0] for c in ordered_claims]
    assert len(ids) == len(set(ids)), 'Duplicate paper identifier'
    records = []
    readings = []
    for owner in ['root', 'dictionary', 'arithmetic', 'graded']:
        records.extend(json.loads((INPUT / (owner+'_results.json')).read_text()))
        readings.extend(json.loads((INPUT / (owner+'_readings.json')).read_text()))
    assert len(records) == len({r['id'] for r in records}), 'Duplicate ledger identifier'
    lookup = {r['id']: r for r in records}
    assert set(ids) == set(lookup), {
        'missing_rows': sorted(set(ids)-set(lookup)),
        'extra_rows': sorted(set(lookup)-set(ids))}
    for ident, status in ordered_claims:
        assert lookup[ident]['status'] == status, (ident, status, lookup[ident]['status'])
        assert status in {'Proved', 'Known', 'Refuted', 'Open'}
        for key in FIELDS:
            assert key in lookup[ident], (ident, key)
    rows = [lookup[ident] for ident in ids]
    write_csv(ROOT / (PREFIX+'_results.csv'), FIELDS, rows)
    write_csv(ROOT / (PREFIX+'_readings.csv'), READING_FIELDS, readings)
    conditions = json.loads((INPUT/'new_conditions.json').read_text())
    write_csv(ROOT / (PREFIX+'_new_conditions.csv'), list(conditions[0]), conditions)
    inventory = json.loads((INPUT/'condition_inventory.json').read_text())
    write_csv(ROOT / (PREFIX+'_condition_inventory.csv'), list(inventory[0]), inventory)
    counts = dict(Counter(r['status'] for r in rows))
    summary = {'numbered_statements':len(rows), 'status_counts':counts,
               'readings':len(readings), 'new_condition_rows':len(conditions),
               'complete_inventory_rows':len(inventory),
               'all_statement_ids_match':True, 'all_statuses_match':True}
    (ROOT/'code'/'register_audit.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))

if __name__ == '__main__':
    main()
