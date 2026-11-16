"""Retain and audit every distinct file version in all earlier checkpoint ZIPs.

Recovered implementation, 2026-11-16. The pre-outage implementation was not
archived. This program audits actual archive bytes; it does not assume that a
reconstructed source is identical to an inaccessible seventh-hour version.
"""
from pathlib import Path
import csv
import hashlib
import json
import zipfile
from datetime import datetime, timezone

root = Path(__file__).resolve().parents[1]
history = root / 'checkpoint_history'
history.mkdir(exist_ok=True)
archives = sorted(root.parent.glob('LM4_SUCCESSOR_checkpoint_[0-9][0-9].zip'))
assert archives, 'No prior checkpoint archives available'
rows = []
created = []
known_versions = {}
# These files are rewritten below. Their old bytes must have historical
# paths even when the current active file still equals a prior snapshot.
rewritten_paths = {
    'records/checkpoint_version_retention.csv',
    'records/checkpoint_version_retention_summary.json',
    'checkpoint_history/README.md',
}

def digest(data):
    return hashlib.sha256(data).hexdigest()

for archive in archives:
    number = int(archive.stem.rsplit('_', 1)[1])
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None, ('CRC failure', archive)
        for entry in z.infolist():
            if entry.is_dir():
                continue
            parts = Path(entry.filename).parts
            assert parts and parts[0] == 'LM4_SUCCESSOR', entry.filename
            assert '..' not in parts, entry.filename
            relative = Path(*parts[1:])
            data = z.read(entry)
            sha = digest(data)
            active = root / relative
            if str(relative) not in rewritten_paths and active.is_file() and active.read_bytes() == data:
                retained = active
                mode = 'active-identical'
            elif (str(relative), sha) in known_versions:
                retained = known_versions[(str(relative), sha)]
                assert retained.read_bytes() == data
                mode = 'history-identical'
            else:
                retained = history / f'checkpoint_{number:02d}' / relative
                retained.parent.mkdir(parents=True, exist_ok=True)
                if retained.exists():
                    assert retained.read_bytes() == data, ('Historical collision', retained)
                else:
                    retained.write_bytes(data)
                    created.append((str(retained.relative_to(root)), len(data)))
                mode = 'historical-copy'
            # Only historical paths may be reused after a future active edit.
            if history in retained.parents:
                known_versions[(str(relative), sha)] = retained
            assert retained.read_bytes() == data
            rows.append(dict(checkpoint=f'{number:02d}', archive=archive.name,
                             original_path=str(relative), bytes=len(data),
                             sha256=sha, retained_path=str(retained.relative_to(root)),
                             retention=mode, omission_reason=''))

records = root / 'records'
records.mkdir(exist_ok=True)
target = records / 'checkpoint_version_retention.csv'
with target.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['checkpoint','archive','original_path','bytes',
                                         'sha256','retained_path','retention','omission_reason'])
    writer.writeheader()
    writer.writerows(rows)
historical = [p for p in history.rglob('*') if p.is_file() and p != history / 'README.md']
summary = dict(recorded_at=datetime.now(timezone.utc).isoformat(),
               archives=len(archives), archive_entries=len(rows), omissions=0,
               new_historical_copies=len(created),
               new_historical_bytes=sum(n for _, n in created),
               total_historical_copies=len(historical),
               total_historical_bytes=sum(p.stat().st_size for p in historical),
               audit='Every archived file byte is retained at the indexed path.',
               scope='Prior durable checkpoints only; inaccessible unarchived versions are not certified.')
(records / 'checkpoint_version_retention_summary.json').write_text(json.dumps(summary, indent=2)+'\n')
(history / 'README.md').write_text('''# Exact prior checkpoint versions

This tree retains distinct earlier bytes when the active file differs.
The authoritative index is records/checkpoint_version_retention.csv.
Every earlier checkpoint entry is mapped to an identical active file or an
identical historical copy. No omission is authorized by this mechanism.

These historical sources are not inputs to the current paper or statement
register. They preserve prior proofs, reports, programs, outputs, and PDF
versions without conflating them with current assertions.

The audit concerns durable checkpoints. It cannot certify the contents of
unarchived files lost when the execution environment disappeared.
''')
print(json.dumps(summary, indent=2))
