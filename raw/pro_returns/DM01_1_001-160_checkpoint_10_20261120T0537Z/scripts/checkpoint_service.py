#!/usr/bin/env python3
"""Save only due 45-minute checkpoint ZIPs; never infer manuscript readings.

Run in a yielding exec session. Create work/checkpoint_service.stop to stop
before final packaging. A failed or ambiguous upload stops for root review;
it is never automatically repeated and cannot silently create a duplicate.
"""
import csv
import datetime as dt
import fcntl
import json
import subprocess
import sys
import time
from pathlib import Path

import package

ROOT = Path(__file__).resolve().parents[2]
STOP = ROOT / 'work/checkpoint_service.stop'
STATE = ROOT / 'work/checkpoint_service.json'
HELPER = ROOT / 'work/library_helpers/library_upload.py'


def stamp():
    return dt.datetime.now(dt.timezone.utc).strftime(package.FMT)


def record(value, announce=True):
    tmp = STATE.with_suffix('.tmp')
    tmp.write_text(json.dumps(value, indent=2) + '\n')
    tmp.replace(STATE)
    if announce:
        print(json.dumps(value), flush=True)


def save(receipt):
    request = {'uploads': [{'local_path': receipt['file'], 'purpose': 'create_library_file'}]}
    proc = subprocess.run([sys.executable, str(HELPER)], input=json.dumps(request),
                          text=True, capture_output=True, cwd=ROOT)
    parsed = []
    for line in proc.stdout.splitlines():
        try:
            value = json.loads(line)
        except ValueError:
            continue
        if isinstance(value, dict) and 'results' in value:
            parsed.append(value)
    if len(parsed) != 1 or len(parsed[0]['results']) != 1:
        # Keep the original response locally for inspection, without retrying.
        (ROOT / f"work/checkpoint_{receipt['number']:02}_upload_response.txt").write_text(
            proc.stdout + '\n' + proc.stderr)
        raise RuntimeError('Upload response is ambiguous; root must inspect before any retry')
    result = parsed[0]['results'][0]
    if result.get('status') != 'succeeded' or not result.get('library_file_id'):
        (ROOT / f"work/checkpoint_{receipt['number']:02}_upload_response.txt").write_text(
            proc.stdout + '\n' + proc.stderr)
        raise RuntimeError('Persistent upload did not succeed; root must review the response')
    confirmed = stamp()
    safe_result = {k: result.get(k) for k in (
        'local_path', 'purpose', 'status', 'file_id', 'library_file_id',
        'file_name', 'local_metadata_applied', 'current_version_number')}
    with (ROOT / 'work/reconcile.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        history = ROOT / 'deliverable/audit/checkpoint_uploads.tsv'
        rows = list(csv.DictReader(history.open(), delimiter='\t')) if history.exists() else []
        if any(int(row['number']) == receipt['number'] for row in rows):
            raise RuntimeError('Checkpoint save already recorded; refusing duplicate history')
        fields = ['number', 'filename', 'library_file_id', 'confirmed_utc']
        with history.open('a', newline='') as stream:
            writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t', lineterminator='\n')
            if not rows:
                writer.writeheader()
            writer.writerow({'number': receipt['number'], 'filename': receipt['filename'],
                             'library_file_id': result['library_file_id'], 'confirmed_utc': confirmed})
        audit = ROOT / f"deliverable/audit/checkpoint_upload_{receipt['number']:02}.json"
        audit.write_text(json.dumps({'package': receipt, 'upload': safe_result,
                                    'confirmed_utc': confirmed}, indent=2) + '\n')
        with (ROOT / 'deliverable/WORKFLOW.md').open('a') as stream:
            stream.write(f"\n### {confirmed} — timed checkpoint {receipt['number']:02} confirmed\n\n"
                         f"The complete checkpoint ZIP was created at {receipt['created_utc']} "
                         f"and its persistent save was confirmed at {confirmed}. "
                         "It includes all deliverables and documentation then written, plus complete "
                         "pending submissions as uncommitted audit snapshots. Prior checkpoint ZIPs, "
                         "source attachments and inspection images are excluded. The next checkpoint "
                         "is due 45 minutes after this creation time.\n")
    return safe_result, confirmed


def main():
    with (ROOT / 'work/checkpoint_service.lock').open('a') as singleton:
        fcntl.flock(singleton, fcntl.LOCK_EX | fcntl.LOCK_NB)
        record({'phase': 'waiting', 'started_utc': stamp(), **package.status()})
        while not STOP.exists():
            remaining = (package.parse(package.status()['next_due_utc']) - package.now()).total_seconds()
            if remaining > 0:
                state = json.loads(STATE.read_text())
                state.update(package.status())
                state['heartbeat_utc'] = stamp()
                record(state, announce=False)
                time.sleep(min(30, remaining))
                continue
            with (ROOT / 'work/reconcile.lock').open('a') as lock:
                fcntl.flock(lock, fcntl.LOCK_EX)
                if STOP.exists():
                    break
                receipt = package.build(False)
            if 'file' not in receipt:
                continue
            record({'phase': 'uploading', 'at_utc': stamp(), 'package': receipt})
            result, confirmed = save(receipt)
            record({'phase': 'waiting', 'confirmed_utc': confirmed,
                    'last_package': receipt, 'last_upload': result, **package.status()})
        record({'phase': 'stopped', 'stopped_utc': stamp(), **package.status()})


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        record({'phase': 'error', 'at_utc': stamp(), 'error': str(exc)})
        raise
