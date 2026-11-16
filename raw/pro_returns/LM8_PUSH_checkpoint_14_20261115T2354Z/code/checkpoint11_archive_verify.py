#!/usr/bin/env python3
"""Verify every archived entry and all reconstruction dependencies for checkpoint 11."""
from pathlib import Path
import csv
import hashlib
import io
import json
import re
import zipfile
import fitz

ROOT = Path(__file__).resolve().parents[1]
path = ROOT.parent / 'LM8_PUSH_checkpoint_11.zip'
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
    prefixed = {e['original_path']: e for e in mapping['exact_prefix_reconstructions']}
    wrappers = {e['original_path']: e for e in mapping['superseded_compression_wrappers']}
    copies = {e['original_path']: e for e in mapping['exact_file_copies']}
    for item in original['files']:
        name = item['path']
        if name in transformed or name in prefixed or name in wrappers:
            entry = transformed.get(name) or prefixed.get(name) or wrappers[name]
            assert item['sha256'] == entry.get('original_sha256', entry.get('original_valid_gzip_sha256'))
        elif name in copies:
            entry = copies[name]
            assert item['sha256'] == entry['sha256']
            assert entry['source_path'] in entries
            assert entries[entry['source_path']]['sha256'] == item['sha256']
        else:
            assert name in entries, name
            assert item['sha256'] == entries[name]['sha256'], name

    for entry in transformed.values():
        assert entry['stored_path'] in entries
        expected = entry.get('encoded_xz_sha256', entry.get('stored_sha256'))
        assert entries[entry['stored_path']]['sha256'] == expected
        assert entry['entire_decoded_byte_hash_verified']
        if entry['codec'] == 'PBC_REPLAY01':
            recipe = json.loads(archive.read(entry['stored_path']))
            for path_key, hash_key in [
                ('leaf_payload_path', 'leaf_payload_sha256'),
                ('source_dat', 'source_dat_sha256'),
                ('replay_source', 'replay_source_sha256'),
                ('replay_executable', 'replay_executable_sha256'),
            ]:
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
        assert entries[entry['pdf_path']]['sha256'] == entry['pdf_sha256']
        assert name in transformed and transformed[name]['decoded_sha256'] == entry['sha256']
    frozen = json.loads(archive.read('notes/checkpoint11_frozen_source_hashes.json'))
    for name, digest in frozen.items():
        assert entries[name]['sha256'] == digest
    pdf = archive.read('LM8_PUSH_paper.pdf')
    pdf_hash = hashlib.sha256(pdf).hexdigest()
    assert pdf_hash == '15f733bb00e2186831f48f5a106ebde353e14c23dd09dd646cf7c8082a2878de'
    with fitz.open(stream=pdf, filetype='pdf') as doc:
        assert len(doc) == 455
    rows = list(csv.DictReader(io.StringIO(archive.read('LM8_PUSH_results.csv').decode())))
    assert len(rows) == 258 and len({r['id'] for r in rows}) == 258
    assert {s: sum(r['status'] == s for r in rows) for s in ['Proved', 'Refuted', 'Known', 'Open']} == {
        'Proved': 210, 'Refuted': 8, 'Known': 10, 'Open': 30}
    rendered = json.loads(archive.read('qa/checkpoint11/rendered_pages.json'))
    reviewed = json.loads(archive.read('notes/checkpoint11_visual_review.json'))
    assert sorted(rendered['rendered_pages']) == reviewed['rendered_and_actually_viewed_pages']
    assert reviewed['reviewed_page_count'] == 51 and reviewed['pdf_sha256'] == pdf_hash
    assert not any(name.startswith(('background/', 'inputs/')) for name in names)

h = hashlib.sha256()
with path.open('rb') as stream:
    for block in iter(lambda: stream.read(1 << 20), b''):
        h.update(block)
result = {
    'status': 'PASS', 'archive': str(path), 'bytes': path.stat().st_size,
    'sha256': h.hexdigest(), 'zip_entries': len(names),
    'manifest_entries': len(entries), 'original_files_accounted_for': len(original['files']),
    'transforms': len(transformed), 'prefixes': len(prefixed), 'exact_duplicate_copies': len(copies),
    'all_crc_and_manifest_hashes_checked': True, 'all_restore_dependencies_present_and_hashed': True,
    'frozen_source_hashes_checked': len(frozen), 'paper_pages': 455,
    'paper_statements': 258, 'actually_reviewed_pages': 51,
    'below_upload_limit': path.stat().st_size <= 536870912,
}
assert result['below_upload_limit']
print(json.dumps(result, indent=2))
