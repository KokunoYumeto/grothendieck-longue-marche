#!/usr/bin/env python3
"""Verify a captured compact archive, its exact history, and all restore inputs."""
from pathlib import Path
import argparse
import csv
import hashlib
import io
import json
import zipfile
import fitz

ROOT = Path(__file__).resolve().parents[1]
ap = argparse.ArgumentParser()
ap.add_argument('serial', type=int)
ap.add_argument('--final', action='store_true')
args = ap.parse_args()
serial = f'{args.serial:02d}'
path = ROOT.parent / ('LM8_PUSH.zip' if args.final else f'LM8_PUSH_checkpoint_{serial}.zip')
with zipfile.ZipFile(path) as archive:
    names = archive.namelist()
    assert len(names) == len(set(names))
    assert archive.testzip() is None
    manifest = json.loads(archive.read('PACKAGE_MANIFEST.json'))
    original = json.loads(archive.read('ORIGINAL_PACKAGE_MANIFEST.json'))
    mapping = json.loads(archive.read('CHECKPOINT_COMPRESSION_MAP.json'))
    entries = {e['path']: e for e in manifest['files']}
    assert set(names) == set(entries) | {'PACKAGE_MANIFEST.json'}
    for name, entry in entries.items():
        data = archive.read(name)
        assert len(data) == entry['bytes']
        assert hashlib.sha256(data).hexdigest() == entry['sha256'], name
    transformed = {e['original_path']: e for e in mapping['transforms']}
    prefixed = {e['original_path']: e for e in mapping.get('exact_prefix_reconstructions', [])}
    wrappers = {e['original_path']: e for e in mapping.get('superseded_compression_wrappers', [])}
    copies = {e['original_path']: e for e in mapping.get('exact_file_copies', [])}

    def exact_entry(name, expected_hash, expected_bytes=None):
        if name in copies:
            copy = copies[name]
            assert copy['sha256'] == expected_hash
            if expected_bytes is not None:
                assert copy['bytes'] == expected_bytes
            name = copy['source_path']
        assert name in entries, name
        assert entries[name]['sha256'] == expected_hash, name
        if expected_bytes is not None:
            assert entries[name]['bytes'] == expected_bytes

    for item in original['files']:
        name = item['path']
        if name in transformed or name in prefixed or name in wrappers:
            entry = transformed.get(name) or prefixed.get(name) or wrappers[name]
            assert item['sha256'] == entry.get('original_sha256', entry.get('original_valid_gzip_sha256'))
        else:
            exact_entry(name, item['sha256'], item['bytes'])
    for entry in transformed.values():
        assert entry['kind'] in ('raw_bytes', 'gzip_payload'), entry['original_path']
        assert entry['stored_path'] in entries
        expected = entry.get('encoded_xz_sha256', entry.get('stored_sha256'))
        assert entries[entry['stored_path']]['sha256'] == expected
        assert entry['entire_decoded_byte_hash_verified']
        for arg in entry.get('restore_command', []):
            if arg.startswith('{archive}/'):
                assert arg[len('{archive}/'):] in entries, arg
        if entry['codec'].startswith('PBC_') and entry['stored_path'].endswith('.json'):
            recipe = json.loads(archive.read(entry['stored_path']))
            assert recipe['decoded_sha256'] == entry['decoded_sha256']
            assert recipe['decoded_bytes'] == entry['decoded_bytes']
            for path_key, hash_key in [
                ('leaf_payload_path', 'leaf_payload_sha256'),
                ('source_dat', 'source_dat_sha256'),
                ('identity_rows_path', 'identity_rows_sha256'),
                ('replay_source', 'replay_source_sha256'),
                ('replay_executable', 'replay_executable_sha256'),
            ]:
                if path_key in recipe:
                    assert recipe[path_key] in entries, ('Nonliteral replay dependency', recipe[path_key])
                    assert entries[recipe[path_key]]['sha256'] == recipe[hash_key]
            for dependency in recipe.get('build_dependencies', []):
                assert entries[dependency['path']]['sha256'] == dependency['sha256']
    for entry in prefixed.values():
        if entry.get('stored_path'):
            assert entries[entry['stored_path']]['sha256'] == entry['stored_sha256']
            assert entry['source_path'] in transformed
        else:
            assert entry['stored_source_path'] in entries
            assert 'code/' + entry['retained_source_payload'] in transformed
    qa = json.loads(archive.read('qa/reconstruction_manifest.json'))
    for name, entry in qa['images'].items():
        assert entry['pdf_path'] in entries, ('Nonliteral PNG dependency', entry['pdf_path'])
        assert entries[entry['pdf_path']]['sha256'] == entry['pdf_sha256']
        assert transformed[name]['decoded_sha256'] == entry['sha256']

    history = json.loads(archive.read('checkpoint_history/HISTORY_INDEX.json'))
    assert history['status'] == 'MATERIALIZED_VERIFIED_HISTORY'
    for obj in history['objects']:
        exact_entry(obj['path'], obj['sha256'], obj['bytes'])
    for name, item in history['exact_current_restoration_dependencies'].items():
        if name in transformed:
            assert transformed[name]['kind'] == 'raw_bytes'
            assert transformed[name]['decoded_sha256'] == item['sha256']
            assert transformed[name]['decoded_bytes'] == item['bytes']
        else:
            exact_entry(name, item['sha256'], item['bytes'])
    history_count = 0
    for snapshot in history['snapshots']:
        assert snapshot['entry_count'] == len(snapshot['entries'])
        history_count += len(snapshot['entries'])
        for item in snapshot['entries']:
            rep = item['representation']
            if rep == 'history_object':
                exact_entry(item['object_path'], item['sha256'], item['bytes'])
            elif rep == 'current_restored_exact':
                expected = history['exact_current_restoration_dependencies'][item['source_path']]
                assert expected == {k: item[k] for k in ('bytes', 'sha256')}
            else:
                assert rep == 'superseded_encoding'
                payload = item['retained_payload']
                current = transformed[payload['source_path']]
                assert payload['decoded_bytes'] <= current['decoded_bytes']
                if payload['decoded_bytes'] == current['decoded_bytes']:
                    assert payload['decoded_sha256'] == current['decoded_sha256']
                else:
                    matches = [c for c in history['verified_prefix_checks']
                               if c['source_path'] == payload['source_path']
                               and c['decoded_prefix_bytes'] == payload['decoded_bytes']
                               and c['expected_sha256'] == payload['decoded_sha256']]
                    assert len(matches) == 1 and matches[0]['passed']
                    assert matches[0]['observed_sha256'] == payload['decoded_sha256']
    assert history_count == history['historical_entries']

    frozen = json.loads(archive.read(f'notes/checkpoint{serial}_frozen_source_hashes.json'))
    for name, digest in frozen.items():
        exact_entry(name, digest)
    state = json.loads(archive.read(f'notes/checkpoint{serial}_frozen_state.json'))
    pdf = archive.read('LM8_PUSH_paper.pdf')
    pdf_hash = hashlib.sha256(pdf).hexdigest()
    assert pdf_hash == state['pdf_sha256']
    with fitz.open(stream=pdf, filetype='pdf') as doc:
        assert len(doc) == state['paper_pages']
    rows = list(csv.DictReader(io.StringIO(archive.read('LM8_PUSH_results.csv').decode())))
    assert len(rows) == len({r['id'] for r in rows}) == state['paper_statements']
    assert {s: sum(r['status'] == s for r in rows) for s in ['Proved', 'Refuted', 'Known', 'Open']} == state['status_counts']
    rendered = json.loads(archive.read(f'qa/checkpoint{serial}/rendered_pages.json'))
    reviewed = json.loads(archive.read(f'notes/checkpoint{serial}_visual_review.json'))
    assert sorted(rendered['rendered_pages']) == reviewed['rendered_and_actually_viewed_pages']
    assert reviewed['reviewed_page_count'] == len(rendered['rendered_pages'])
    assert reviewed['pdf_sha256'] == pdf_hash
    assert not any(name.startswith(('background/', 'inputs/')) for name in names)
h = hashlib.sha256()
with path.open('rb') as stream:
    for block in iter(lambda: stream.read(1 << 20), b''):
        h.update(block)
result = {
    'status': 'PASS', 'archive': str(path), 'bytes': path.stat().st_size,
    'sha256': h.hexdigest(), 'zip_entries': len(names), 'manifest_entries': len(entries),
    'original_files_accounted_for': len(original['files']), 'transforms': len(transformed),
    'prefixes': len(prefixed), 'exact_duplicate_copies': len(copies),
    'all_crc_and_manifest_hashes_checked': True,
    'all_restore_dependencies_present_and_hashed': True,
    'historical_entries_accounted_for': history_count,
    'historical_content_objects': len(history['objects']),
    'frozen_source_hashes_checked': len(frozen),
    'paper_pages': state['paper_pages'], 'paper_statements': len(rows),
    'actually_reviewed_pages': reviewed['reviewed_page_count'],
    'below_upload_limit': path.stat().st_size <= 536870912,
}
assert result['below_upload_limit']
print(json.dumps(result, indent=2))
