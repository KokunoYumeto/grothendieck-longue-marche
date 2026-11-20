#!/usr/bin/env python3
"""Check a prepared proposal; --apply installs it with a retained audit transaction."""
from __future__ import annotations
import argparse
import datetime as dt
import fcntl
import hashlib
import json
import os
from pathlib import Path
import shutil

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PROPOSAL = HERE / 'proposal'
EXPECTED = [
    'deliverable/scripts/other_error_aliases.py',
    'deliverable/audit/OTHER_ERROR_ALIASES.json',
    'deliverable/other_errors.tsv',
    'deliverable/scripts/reconcile.py',
]


def sha(content):
    return hashlib.sha256(content).hexdigest()


def atomic(path, content):
    temporary = path.with_name(path.name + '.alias-normalization.tmp')
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary.write_bytes(content)
    if path.exists():
        temporary.chmod(path.stat().st_mode & 0o777)
    os.replace(temporary, path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    with (ROOT / 'work/reconcile.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        manifest_bytes = (PROPOSAL / 'manifest.json').read_bytes()
        manifest = json.loads(manifest_bytes)
        if manifest['schema_version'] != 1 or manifest['install_order'] != EXPECTED or set(manifest['files']) != set(EXPECTED):
            raise ValueError('Unexpected transaction targets')
        after = {}
        for relative in EXPECTED:
            record = manifest['files'][relative]
            path = ROOT / relative
            current = sha(path.read_bytes()) if path.exists() else None
            if current != record['before_sha256']:
                raise ValueError(f'Before-state changed; do not apply this stale proposal: {relative}')
            if current is not None and sha((PROPOSAL / 'before' / relative).read_bytes()) != current:
                raise ValueError(f'Corrupt before snapshot: {relative}')
            after[relative] = (PROPOSAL / 'after' / relative).read_bytes()
            if sha(after[relative]) != record['after_sha256']:
                raise ValueError(f'Corrupt after snapshot: {relative}')
        for relative, expected in manifest['protected_sha256'].items():
            if sha((ROOT / relative).read_bytes()) != expected:
                raise ValueError(f'Protected audit/history changed; refresh the proposal: {relative}')
        if sha((PROPOSAL / 'CORRECTION.md').read_bytes()) != manifest['correction_sha256']:
            raise ValueError('Corrupt correction addendum')
        for relative in EXPECTED:
            if relative.endswith('.py'):
                compile(after[relative], relative, 'exec')
        if not args.apply:
            print(json.dumps({'valid_proposal': True, 'applied': False,
                              'before_rows': manifest['before_rows'], 'after_rows': manifest['after_rows']}))
            return
        transaction_id = manifest['transaction_id']
        if not transaction_id or Path(transaction_id).name != transaction_id:
            raise ValueError('Invalid transaction ID')
        audit = ROOT / 'deliverable/audit/other_error_normalizations' / transaction_id
        if audit.exists():
            raise ValueError('Audit transaction already exists; inspect its application status before any retry')
        audit.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(PROPOSAL, audit)
        application = {'status': 'prepared', 'proposal_manifest_sha256': sha(manifest_bytes),
                       'started_utc': dt.datetime.now(dt.timezone.utc).isoformat()}
        atomic(audit / 'application.json', (json.dumps(application, indent=2) + '\n').encode())
        # All four replacements are under reconcile.lock. The complete before
        # snapshots already exist in the audit if a write is interrupted.
        for relative in EXPECTED:
            atomic(ROOT / relative, after[relative])
        for relative in EXPECTED:
            if sha((ROOT / relative).read_bytes()) != manifest['files'][relative]['after_sha256']:
                raise ValueError(f'Installed content mismatch: {relative}')
        for relative, expected in manifest['protected_sha256'].items():
            if sha((ROOT / relative).read_bytes()) != expected:
                raise ValueError(f'Protected audit/history changed during application: {relative}')
        application.update(status='completed', completed_utc=dt.datetime.now(dt.timezone.utc).isoformat())
        atomic(audit / 'application.json', (json.dumps(application, indent=2) + '\n').encode())
        print(json.dumps({'applied': True, 'audit_transaction': str(audit),
                          'before_rows': manifest['before_rows'], 'after_rows': manifest['after_rows']}))


if __name__ == '__main__':
    main()
