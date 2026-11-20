#!/usr/bin/env python3
"""Record a reviewed, committed page's actual coordination counts; never inspect ink."""
import argparse
import csv
import datetime as dt
import fcntl
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
p = argparse.ArgumentParser()
p.add_argument('scan', type=int)
p.add_argument('--notes', type=Path, help='JSON array of already-reviewed coordinator notes')
a = p.parse_args()
notes = json.loads((ROOT / a.notes).read_text()) if a.notes else []
if not isinstance(notes, list) or not all(isinstance(x, str) for x in notes):
    p.error('notes must be a JSON array of strings')
def table(path):
    with path.open() as stream:
        return list(csv.DictReader(stream, delimiter='\t'))
with (ROOT / 'work/reconcile.lock').open('a') as lock:
    fcntl.flock(lock, fcntl.LOCK_EX)
    path = ROOT / 'deliverable/audit/COORDINATION.json'
    state = json.loads(path.read_text())
    if state.get('current_scan') != a.scan:
        raise ValueError('Current coordination scan differs')
    receipts = sorted((ROOT / 'deliverable/audit/receipts').glob('scan*.json'))
    last = int(receipts[-1].stem.removeprefix('scan')) if receipts else None
    if last != a.scan:
        raise ValueError('The requested page must be the latest committed page')
    rows = table(ROOT / 'deliverable/decisions.tsv')
    events = table(ROOT / 'deliverable/CHECK_EVENTS.tsv')
    errors = table(ROOT / 'deliverable/other_errors.tsv')
    archive = ROOT / f'deliverable/audit/revisions/scan{a.scan:03}_coordination_final.json'
    if archive.exists():
        old = json.loads(archive.read_text())
        if old.get('completed_marks') != len(rows) or old.get('check_events') != len(events):
            raise ValueError('Existing final archive differs; do not overwrite history')
        print(json.dumps({'scan': a.scan, 'already_archived': True}))
    else:
        state.update(phase='committed', last_committed_scan=a.scan,
                     completed_pages=len(receipts), completed_marks=len(rows),
                     decision_counts=dict(Counter(r['decision'] for r in rows)),
                     check_events=len(events), unmarked_errors=len(errors),
                     updated_utc=dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
                     pending_revisions=[], pending_third_assignment=None,
                     next_trigger='Dispatch the next supplied page after this reviewed commit.')
        for assignment in state.get('primary_assignments', []) + state.get('peer_assignments', []):
            assignment['status'] = 'complete'
        state.setdefault('coordinator_notes', []).extend(notes)
        encoded = json.dumps(state, ensure_ascii=False, indent=2) + '\n'
        with archive.open('x') as stream:
            stream.write(encoded)
        path.write_text(encoded)
        print(json.dumps({'scan': a.scan, 'phase': 'committed', 'marks': len(rows),
                          'pages': len(receipts), 'events': len(events),
                          'archive': str(archive.relative_to(ROOT))}))
