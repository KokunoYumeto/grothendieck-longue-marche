#!/usr/bin/env python3
"""Read-only archive-size preflight; this does not create a checkpoint."""
from pathlib import Path
import hashlib
import json
import zlib

root = Path(__file__).resolve().parents[1]
plan = json.loads((root / 'notes/checkpoint13_storage_plan.json').read_text())
new = json.loads((root / 'code/pbc_quotient86_standard2_replay_transform.json').read_text())
transforms = plan['transforms'] + [new]
skipped = {e['original_path'] for e in transforms}
skipped.update(e['original_path'] for key in ('exact_prefix_reconstructions',
                                           'superseded_compression_wrappers')
               for e in plan.get(key, []))
payloads = {}
for entry in transforms + plan.get('exact_prefix_reconstructions', []):
    if 'local_encoded_file' in entry:
        payloads[entry['stored_path']] = Path(entry['local_encoded_file'])
    for extra in entry.get('additional_payloads', []):
        payloads[extra['path']] = Path(extra['local_file'])
for extra in plan.get('additional_payloads', []):
    payloads[extra['path']] = Path(extra['local_file'])
excluded = ('build/tex-cache/', '__pycache__/', 'background/', 'inputs/')
metadata = {'PACKAGE_MANIFEST.json', 'CHECKPOINT_COMPRESSION_MAP.json',
            'ORIGINAL_PACKAGE_MANIFEST.json', 'RESTORE_LARGE_LOGS.py'}
seen = {}
rows = []
for path in sorted(root.rglob('*'), key=lambda p: (
        p.relative_to(root).as_posix().startswith('checkpoint_history/'),
        p.relative_to(root).as_posix())):
    if not path.is_file():
        continue
    name = path.relative_to(root).as_posix()
    if (name in skipped or name in payloads or name in metadata
            or path.suffix == '.pyc'
            or any(name.startswith(s) or '/' + s in name for s in excluded)):
        continue
    size = path.stat().st_size
    h = hashlib.sha256()
    compressed = 0
    store = name.endswith(('.xz', '.gz'))
    compressor = None if store else zlib.compressobj(9, zlib.DEFLATED, -15)
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
            compressed += len(block) if store else len(compressor.compress(block))
    if compressor:
        compressed += len(compressor.flush())
    digest = h.hexdigest()
    if (size >= 1_000_000 or name.startswith('checkpoint_history/objects/')) and digest in seen:
        continue
    seen.setdefault(digest, name)
    rows.append({'path': name, 'bytes': size, 'zip_payload_bytes': compressed})
for name, path in payloads.items():
    data = path.read_bytes()
    size = len(data)
    if name.endswith(('.xz', '.gz')):
        compressed = size
    else:
        compressor = zlib.compressobj(9, zlib.DEFLATED, -15)
        compressed = len(compressor.compress(data)) + len(compressor.flush())
    rows.append({'path': name, 'bytes': size, 'zip_payload_bytes': compressed})
total = sum(r['zip_payload_bytes'] for r in rows)
result = {
    'scope': 'Read-only conservative preflight before final build and QA; no archive created.',
    'estimated_payload_bytes': total,
    'with_2MiB_metadata_allowance': total + (2 << 20),
    'remaining_before_512MiB_cap': 536870912 - total - (2 << 20),
    'entries': len(rows),
    'largest_payloads': sorted(rows, key=lambda r: r['zip_payload_bytes'], reverse=True)[:30],
    'notes': 'Historical duplicates of explicit encoded payloads are not removed, so this slightly overestimates current packing. New paper/QA growth remains to be added.',
}
(root / 'notes/checkpoint14_size_preflight.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
