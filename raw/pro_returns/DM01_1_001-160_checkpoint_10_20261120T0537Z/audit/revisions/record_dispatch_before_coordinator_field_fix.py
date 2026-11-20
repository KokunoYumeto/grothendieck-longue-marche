#!/usr/bin/env python3
"""Record actual root-dispatched readers, without assigning or reading ink."""
import argparse
import csv
import datetime as dt
import fcntl
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser()
parser.add_argument('scan', type=int)
parser.add_argument('agents', nargs='+')
args = parser.parse_args()
if not 1 <= len(args.agents) <= 3 or not all(a.startswith('/root/') for a in args.agents):
    parser.error('Supply one to three actual canonical reader names')
with (ROOT / 'work/reconcile.lock').open('a') as lock:
    fcntl.flock(lock, fcntl.LOCK_EX)
    allocation = json.loads(subprocess.check_output(
        [sys.executable, str(ROOT / 'deliverable/scripts/next_assignment.py'),
         '--readers', str(len(args.agents))], cwd=ROOT, text=True))
    if allocation.get('scan') != args.scan:
        raise ValueError('Dispatch must match the next uncommitted page')
    rows = list(csv.DictReader((ROOT / 'deliverable/decisions.tsv').open(), delimiter='\t'))
    events = list(csv.DictReader((ROOT / 'deliverable/CHECK_EVENTS.tsv').open(), delimiter='\t'))
    receipts = sorted((ROOT / 'deliverable/audit/receipts').glob('scan*.json'))
    assignments = []
    for part, agent in zip(allocation['parts'], args.agents):
        suffix = '_' + part['suffix'] if part['suffix'] else ''
        assignments.append({'part': part['suffix'], 'agent': agent, 'ids': part['ids'],
                            'report': f'work/scan{args.scan:03}{suffix}.json', 'status': 'running'})
    state = {'schema_version': 1, 'mode': 'staged_coordination_root_dispatch',
             'phase': 'awaiting_primaries', 'current_scan': args.scan,
             'updated_utc': dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
             'last_committed_scan': int(receipts[-1].stem.removeprefix('scan')) if receipts else None,
             'completed_pages': len(receipts), 'completed_marks': len(rows),
             'decision_counts': dict(Counter(row['decision'] for row in rows)),
             'check_events': len(events), 'root': '/root', 'coordinator': '/root/audit_tools',
             'primary_assignments': assignments,
             'expected_primary_reports': [a['report'] for a in assignments],
             'peer_assignments': [], 'expected_peer_reports': [], 'pending_revisions': [],
             'pending_third_assignment': None,
             'next_trigger': 'Review after all current primary reports and any selected peer reports are complete.',
             'checkpoint_owner': '/root',
             'checkpoint_service': 'deliverable/scripts/checkpoint_service.py; work/checkpoint_service.json',
             'allocation_note': 'Default: 3 readers at >=18 marks, 2 at >=6, otherwise 1; recorded names are actual root dispatches.'}
    try:
        service = json.loads((ROOT / 'work/checkpoint_service.json').read_text())
        heartbeat = next(service[k] for k in ('heartbeat_utc', 'at_utc', 'confirmed_utc', 'started_utc') if service.get(k))
        heartbeat_time = dt.datetime.strptime(heartbeat, '%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=dt.timezone.utc)
        age = round((dt.datetime.now(dt.timezone.utc) - heartbeat_time).total_seconds())
        health = {'phase': service.get('phase'), 'heartbeat_age_seconds': age,
                  'next_due_utc': service.get('next_due_utc'),
                  'needs_attention': age > 90 or service.get('phase') in ('error', 'stopped')}
    except (OSError, ValueError, StopIteration):
        health = {'needs_attention': True, 'reason': 'No readable checkpoint-service heartbeat'}
    state['checkpoint_service_health'] = health
    path = ROOT / 'deliverable/audit/COORDINATION.json'
    path.write_text(json.dumps(state, indent=2) + '\n')
    print(json.dumps({'scan': args.scan, 'phase': state['phase'], 'readers': args.agents,
                      'marks': allocation['count'], 'checkpoint_service_health': health}))
