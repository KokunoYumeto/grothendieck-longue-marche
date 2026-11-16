#!/usr/bin/env python3
"""Conservative read-only size forecast; this never creates a ZIP.

Keep every byte of checkpoint14, then add compressed current content whose
hash is absent from its literal manifest, using checkpoint15's complete set of transformed/skipped paths. This intentionally overcounts
obsolete paths and some metadata. A final-PDF reserve is stated separately.
"""
from pathlib import Path
import hashlib
import json
import zipfile
import zlib

root = Path(__file__).resolve().parents[1]
archive = root.parent / 'LM8_PUSH_checkpoint_14.zip'
plan = json.loads((root / 'notes/checkpoint15_storage_plan.json').read_text())
with zipfile.ZipFile(archive) as z:
    manifest = json.loads(z.read('PACKAGE_MANIFEST.json'))
known = {e['sha256'] for e in manifest['files']}
skipped = {e['original_path'] for key in ('transforms', 'exact_prefix_reconstructions',
                                        'superseded_compression_wrappers')
           for e in plan.get(key, [])}
excluded = ('build/tex-cache/', '__pycache__/', 'background/', 'inputs/')
metadata = {'PACKAGE_MANIFEST.json', 'CHECKPOINT_COMPRESSION_MAP.json',
            'ORIGINAL_PACKAGE_MANIFEST.json', 'RESTORE_LARGE_LOGS.py'}
rows = []
for p in sorted(root.rglob('*')):
    if not p.is_file():
        continue
    rel = p.relative_to(root).as_posix()
    if (rel in skipped or rel in metadata or p.suffix == '.pyc'
            or any(rel.startswith(x) or '/' + x in rel for x in excluded)):
        continue
    data = p.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest in known:
        continue
    known.add(digest)
    if rel.endswith(('.xz', '.gz')):
        compressed = len(data)
    else:
        c = zlib.compressobj(9, zlib.DEFLATED, -15)
        compressed = len(c.compress(data)) + len(c.flush())
    rows.append({'path': rel, 'bytes': len(data), 'compressed_bytes': compressed,
                 'sha256': digest})
extra = sum(x['compressed_bytes'] + 2*len(x['path']) + 100 for x in rows)
reserve = 8 << 20
total = archive.stat().st_size + extra + reserve
result = {'scope': 'Read-only conservative forecast; no checkpoint ZIP created.',
          'previous_archive_bytes': archive.stat().st_size,
          'new_unique_compressed_bytes_with_header_allowance': extra,
          'future_build_QA_metadata_reserve': reserve,
          'upper_bound_with_reserve': total,
          'headroom_below_512MiB': 536870912-total,
          'new_unique_files': len(rows),
          'largest_additions': sorted(rows, key=lambda x:x['compressed_bytes'], reverse=True)[:25]}
(root / 'notes/checkpoint15_size_preflight.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
