"""Serialize the main reader's explicit crop decisions; never decide a reading.

Before calling this script, the main reader visually inspects every differing
box, writes review/<page>_audit_decisions.json keyed by box ID, and applies any
approved text/report edits. Original first/second readings remain untouched.
"""
from pathlib import Path
import csv
import json
import sys
import finish_audit

WORK = Path('/workspace/scratch/b8c6ff258063/SP87_C13_149_work')

def adjudicate(scan):
    page = f'149_scan{scan:03d}'
    second = WORK/'second'
    comparisons = list(csv.DictReader((second/f'{page}_comparison.tsv').open(), delimiter='\t'))
    explicit = json.loads((WORK/'review'/f'{page}_audit_decisions.json').read_text())
    if set(explicit) != {r['box'] for r in comparisons}:
        raise ValueError('An explicit main-reader decision is required for every differing box')
    target = second/f'{page}_adjudications.tsv'
    if target.exists():
        raise ValueError('Adjudications already saved; do not replace the evidence record')
    rows = []
    for c in comparisons:
        d = explicit[c['box']]
        if not d.get('evidence') or d.get('changed') not in [True, False]:
            raise ValueError('Evidence and a boolean changed outcome are mandatory')
        rows.append({
            'box': c['box'], 'first': c['first'], 'second': c['second'],
            'final': d.get('final', c['first']),
            'decision': d.get('decision', 'main-reader crop adjudication'),
            'evidence': d['evidence'],
            'crop': f'crops/second_{page}_{c["box"]}.png',
            'changed': 'yes' if d['changed'] else 'no',
        })
    with target.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['box','first','second','final','decision','evidence','crop','changed'], delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)
    finish_audit.finish(scan)

if __name__ == '__main__':
    adjudicate(int(sys.argv[1]))
