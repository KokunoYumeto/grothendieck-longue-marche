#!/usr/bin/env python3
"""Restore one complete historical file tree from the retained version index."""
from pathlib import Path
import argparse
import gzip
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parents[1]
ap = argparse.ArgumentParser()
ap.add_argument('--checkpoint', type=int, required=True)
ap.add_argument('--destination', type=Path, required=True)
ap.add_argument('--materialized-root', type=Path, default=ROOT)
args = ap.parse_args()
dest = args.destination.resolve()
if dest.exists():
    raise SystemExit('Refusing to overwrite existing historical destination: ' + str(dest))
index = json.loads((ROOT / 'checkpoint_history/HISTORY_INDEX.json').read_text())
snapshots = [s for s in index['snapshots'] if s['serial'] == args.checkpoint]
assert len(snapshots) == 1, 'Checkpoint is not covered by this index'
snapshot = snapshots[0]
mapping_path = ROOT / 'CHECKPOINT_COMPRESSION_MAP.json'
mapping = json.loads(mapping_path.read_text()) if mapping_path.exists() else {}
aliases = {e['original_path']: e['source_path'] for e in mapping.get('exact_file_copies', [])}

def safe(root, relative):
    target = (root / relative).resolve()
    assert target.is_relative_to(root.resolve()), relative
    return target

def source_path(relative):
    seen = set()
    while True:
        assert relative not in seen, 'Copy-recipe cycle'
        seen.add(relative)
        for base in (args.materialized_root, ROOT):
            path = safe(base, relative)
            if path.is_file():
                return path
        if relative not in aliases:
            raise SystemExit('Missing exact restoration dependency: ' + relative +
                             '; run the outer RESTORE_LARGE_LOGS.py first')
        relative = aliases[relative]

def copy_exact(row, source, target):
    h = hashlib.sha256()
    count = 0
    target.parent.mkdir(parents=True, exist_ok=True)
    with source.open('rb') as inp, target.open('xb') as out:
        for block in iter(lambda: inp.read(1 << 20), b''):
            out.write(block)
            h.update(block)
            count += len(block)
    assert count == row['bytes'] and h.hexdigest() == row['sha256'], row['path']

# Check dependency availability before creating any output directory.
for row in snapshot['entries']:
    if row['representation'] == 'history_object':
        source_path(row['object_path'])
    elif row['representation'] == 'current_restored_exact':
        source_path(row['source_path'])
    else:
        source_path(row['retained_payload']['source_path'])
dest.mkdir(parents=True)
superseded = []
exact = 0
for row in snapshot['entries']:
    rep = row['representation']
    if rep != 'superseded_encoding':
        relative = row['object_path'] if rep == 'history_object' else row['source_path']
        copy_exact(row, source_path(relative), safe(dest, row['path']))
        exact += 1
        continue
    payload = row['retained_payload']
    source = source_path(payload['source_path'])
    target = safe(dest, payload['source_path'])
    assert not target.exists(), 'Historical decoded replacement conflicts with an exact entry'
    target.parent.mkdir(parents=True, exist_ok=True)
    opener = gzip.open if payload['kind'] == 'gzip_payload' else open
    h = hashlib.sha256()
    remaining = payload['decoded_bytes']
    with opener(source, 'rb') as inp, target.open('xb') as raw:
        out = gzip.GzipFile(filename='', mode='wb', fileobj=raw, compresslevel=1, mtime=0) if payload['kind'] == 'gzip_payload' else raw
        while remaining:
            block = inp.read(min(1 << 20, remaining))
            assert block, 'Truncated retained historical payload'
            out.write(block)
            h.update(block)
            remaining -= len(block)
        if out is not raw:
            out.close()
    assert h.hexdigest() == payload['decoded_sha256'], row['path']
    superseded.append(row)
result = {'status': 'PASS', 'checkpoint': args.checkpoint,
          'source_archive_sha256': snapshot['archive_sha256'],
          'exact_historical_entries_restored': exact,
          'superseded_encodings': superseded,
          'old_zip_wrapper_recreated': False}
(dest / 'HISTORICAL_RESTORATION_ACCOUNTING.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k != 'superseded_encodings'}, indent=2))
