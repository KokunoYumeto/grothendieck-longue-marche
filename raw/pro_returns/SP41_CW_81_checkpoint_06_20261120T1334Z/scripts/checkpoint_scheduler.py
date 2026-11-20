"""Save the requested 45-minute checkpoints during this run, never between slots.

This scheduler performs no reading, transcription, collation or adjudication.
The stop marker is checked while waiting; no final checkpoint is created on exit.
"""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import csv, json, subprocess, sys, time, os

root = Path(__file__).resolve().parents[2]
w = root / 'work'
private = root / 'private'
private.mkdir(exist_ok=True)
start = datetime(2026, 11, 20, 8, 53, 22, tzinfo=timezone.utc)
stop = private / 'checkpoint_scheduler.stop'
state = private / 'checkpoint_scheduler_state.json'
register = w / 'validation/checkpoints.tsv'

def stamp():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def put_state(value):
    tmp = state.with_suffix('.tmp')
    tmp.write_text(json.dumps(value, indent=2))
    tmp.replace(state)

done = {int(r['number']) for r in csv.DictReader(register.open(), delimiter='\t')}
number = max(done, default=0) + 1
while not stop.exists():
    due = start + timedelta(minutes=45 * number)
    put_state({'pid': os.getpid(), 'next_number': number, 'due_utc': due.isoformat(), 'status': 'waiting'})
    while datetime.now(timezone.utc) < due and not stop.exists():
        time.sleep(min(20, max(.01, (due - datetime.now(timezone.utc)).total_seconds())))
    if stop.exists():
        break
    name = f'SP41_CW_81_checkpoint_{number:02d}.zip'
    created = stamp()
    with (w / 'progress.log').open('a') as f:
        f.write(f'checkpoint {number:02d} scheduled snapshot started {created}\n')
    put_state({'pid': os.getpid(), 'number': number, 'due_utc': due.isoformat(), 'status': 'packaging'})
    package = subprocess.run([sys.executable, str(w / 'scripts/package.py'), name], capture_output=True, text=True)
    (private / f'checkpoint{number:02d}_package_stdout.txt').write_text(package.stdout)
    (private / f'checkpoint{number:02d}_package_stderr.txt').write_text(package.stderr)
    if package.returncode:
        put_state({'pid': os.getpid(), 'number': number, 'status': 'package_failed', 'error': package.stderr})
        raise SystemExit(package.returncode)
    meta = json.loads(package.stdout)
    put_state({'pid': os.getpid(), 'number': number, 'status': 'uploading', 'archive': meta})
    payload = {'uploads': [{'local_path': meta['path'], 'purpose': 'create_library_file', 'library_artifact_type': 'other'}]}
    upload = subprocess.run([sys.executable, str(root / 'libhelpers/library_upload.py')], input=json.dumps(payload), capture_output=True, text=True)
    (private / f'checkpoint{number:02d}_upload_stdout.txt').write_text(upload.stdout)
    (private / f'checkpoint{number:02d}_upload_stderr.txt').write_text(upload.stderr)
    if upload.returncode:
        put_state({'pid': os.getpid(), 'number': number, 'status': 'upload_failed', 'archive': meta, 'error': upload.stderr})
        raise SystemExit(upload.returncode)
    # The helper emits one final JSON object. Preserve it in full and inspect success.
    result = json.loads(upload.stdout)
    rows = result.get('results', [])
    successful = [r for r in rows if r.get('status') == 'succeeded' and r.get('local_metadata_applied') is True]
    # Exact helper shapes can vary; never manufacture a remote identifier.
    def ids(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == 'library_file_id' and isinstance(v, str):
                    yield v
                else:
                    yield from ids(v)
        elif isinstance(obj, list):
            for v in obj:
                yield from ids(v)
    remote = list(dict.fromkeys(ids(result)))
    if len(remote) != 1 or len(rows) != 1 or len(successful) != 1:
        put_state({'pid': os.getpid(), 'number': number, 'status': 'upload_result_needs_review', 'archive': meta})
        raise SystemExit('Upload finished; inspect exact result before recording it.')
    with register.open('a', newline='') as f:
        csv.writer(f, delimiter='\t').writerow([number, name, created, remote[0], meta['bytes'], meta['sha256']])
    with (w / 'progress.log').open('a') as f:
        f.write(f'checkpoint {number:02d} saved {stamp()} {remote[0]} SHA256 {meta["sha256"]}\n')
    number += 1
put_state({'pid': os.getpid(), 'status': 'stopped', 'stopped_utc': stamp(), 'next_number': number})
