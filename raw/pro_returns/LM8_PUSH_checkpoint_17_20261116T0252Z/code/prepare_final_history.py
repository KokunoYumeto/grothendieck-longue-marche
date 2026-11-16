#!/usr/bin/env python3
"""Inventory every saved checkpoint entry without duplicating large encodings.

This creates a verified history plan, not a final archive. Every historical
entry is either retained exactly, points to equal current bytes, or is an
individually documented superseded encoding of a verified retained payload.
"""
from pathlib import Path
import argparse
import gzip
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ap = argparse.ArgumentParser()
ap.add_argument('through', type=int)
args = ap.parse_args()
catalog = json.loads((ROOT / 'notes/checkpoint_saved_paths.json').read_text())

def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()

def selected(serial):
    key = f'{serial:02d}'
    if key in catalog:
        return Path(catalog[key]['path'])
    assert serial < 9, 'Later checkpoints must be explicitly recorded as saved'
    return ROOT.parent / f'LM8_PUSH_checkpoint_{key}.zip'

base_path = selected(args.through)
with zipfile.ZipFile(base_path) as z:
    base_manifest = json.loads(z.read('PACKAGE_MANIFEST.json'))
    base_original = json.loads(z.read('ORIGINAL_PACKAGE_MANIFEST.json'))
    base_map = json.loads(z.read('CHECKPOINT_COMPRESSION_MAP.json'))
base_entries = {e['path']: e for e in base_manifest['files']}
base_by_hash = {e['sha256']: e['path'] for e in base_entries.values()}
base_originals = {e['path']: e for e in base_original['files']}
base_transforms = {e['original_path']: e for e in base_map['transforms']}

prefix_cache = {}
prefix_checks = []
def payload_is_available(old):
    name = old['original_path']
    current = base_transforms.get(name)
    if current is None:
        return None
    count, digest = old['decoded_bytes'], old['decoded_sha256']
    if count == current['decoded_bytes'] and digest == current['decoded_sha256']:
        return {'source_path': name, 'decoded_bytes': count,
                'decoded_sha256': digest, 'kind': current['kind'],
                'comparison': 'Identical fully verified decoded payload'}
    if count >= current['decoded_bytes']:
        return None
    cache_key = (name, count, digest)
    if cache_key not in prefix_cache:
        source = ROOT / name
        assert sha(source) == base_originals[name]['sha256'], name
        h = hashlib.sha256()
        remaining = count
        reader = gzip.open(source, 'rb') if current['kind'] == 'gzip_payload' else source.open('rb')
        with reader:
            while remaining:
                block = reader.read(min(1 << 20, remaining))
                assert block, name
                h.update(block)
                remaining -= len(block)
        prefix_cache[cache_key] = h.hexdigest() == digest
        prefix_checks.append({'source_path': name, 'source_original_sha256': base_originals[name]['sha256'],
                              'decoded_prefix_bytes': count, 'expected_sha256': digest,
                              'observed_sha256': h.hexdigest(), 'passed': prefix_cache[cache_key]})
    if not prefix_cache[cache_key]:
        return None
    return {'source_path': name, 'decoded_bytes': count,
            'decoded_sha256': digest, 'kind': current['kind'],
            'comparison': 'Every decoded prefix byte hashed; exact historical verified payload hash matches'}

snapshots = []
objects = {}
counts = {}
for serial in range(1, args.through + 1):
    path = selected(serial)
    digest = sha(path)
    if f'{serial:02d}' in catalog:
        assert digest == catalog[f'{serial:02d}']['sha256'], path
    with zipfile.ZipFile(path) as z:
        manifest = json.loads(z.read('PACKAGE_MANIFEST.json'))
        listed = {e['path']: e for e in manifest['files']}
        storage = json.loads(z.read('CHECKPOINT_COMPRESSION_MAP.json')) if 'CHECKPOINT_COMPRESSION_MAP.json' in z.namelist() else {}
        encoded = {}
        for entry in storage.get('transforms', []):
            encoded.setdefault(entry['stored_path'], []).append(entry)
        rows = []
        for info in z.infolist():
            if info.is_dir():
                continue
            name = info.filename
            if name in listed:
                entry = listed[name]
                assert entry['bytes'] == info.file_size
                entry_hash = entry['sha256']
            else:
                data = z.read(name)
                entry_hash = hashlib.sha256(data).hexdigest()
            row = {'path': name, 'bytes': info.file_size, 'sha256': entry_hash}
            if entry_hash in base_by_hash:
                row.update(representation='current_literal', source_path=base_by_hash[entry_hash])
            elif name in base_originals and base_originals[name]['sha256'] == entry_hash and base_transforms.get(name, {}).get('kind') == 'raw_bytes':
                row.update(representation='current_restored_exact', source_path=name)
            elif name in encoded and len(encoded[name]) == 1 and name.endswith('.xz'):
                payload = payload_is_available(encoded[name][0])
                if payload is not None:
                    row.update(representation='superseded_encoding', retained_payload=payload,
                               reason='The numerical compression representation is superseded by the current verified representation of exactly the same mathematical payload or its verified prefix. Its original count, hash, recipe and validation records remain in this history.')
            if 'representation' not in row:
                suffix = Path(name).suffix
                object_path = f'checkpoint_history/objects/{entry_hash}{suffix}'
                if entry_hash not in objects:
                    objects[entry_hash] = {'path': object_path, 'bytes': info.file_size,
                                          'sha256': entry_hash, 'source_checkpoint': serial,
                                          'source_archive': str(path), 'source_entry': name,
                                          'previous_compressed_bytes': info.compress_size}
                row.update(representation='history_object', object_path=objects[entry_hash]['path'])
            counts[row['representation']] = counts.get(row['representation'], 0) + 1
            rows.append(row)
        snapshots.append({'serial': serial, 'archive_path': str(path), 'archive_bytes': path.stat().st_size,
                          'archive_sha256': digest, 'entry_count': len(rows), 'entries': rows,
                          'container_policy': 'The old ZIP wrapper is unchanged at its saved location. The final archive will retain its complete file/version accounting through this index, with each superseded encoding individually identified.'})

result = {'status': 'VERIFIED_PLAN_NOT_FINAL_ARCHIVE', 'through_checkpoint': args.through,
          'base_checkpoint': str(base_path), 'base_checkpoint_sha256': sha(base_path),
          'snapshots': snapshots, 'objects': list(objects.values()), 'prefix_checks': prefix_checks,
          'representation_counts': counts,
          'historical_entries': sum(x['entry_count'] for x in snapshots),
          'unique_history_object_bytes': sum(x['bytes'] for x in objects.values()),
          'previous_compressed_object_bytes': sum(x['previous_compressed_bytes'] for x in objects.values()),
          'final_assembly_requirement': 'Recheck current_literal/current_restored_exact hashes against the final captured current files. If a current file changed after the base checkpoint, retain the historical snapshot entry as its own exact object. Verify all selected entry bytes again while building the final archive.'}
out = ROOT / 'notes/final_history_inventory.json'
out.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k not in {'snapshots', 'objects'}}, indent=2))
