#!/usr/bin/env python3
"""Prepare checkpoint15's verified storage plan; never create an archive."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return json.loads(path.read_text())

def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()

old = read(ROOT / 'notes/checkpoint14_storage_plan.json')
plan = json.loads(json.dumps(old))
qa = read(ROOT / 'notes/checkpoint15_qa_encoding.json')
state = read(ROOT / 'notes/checkpoint15_frozen_state.json')
history = read(ROOT / 'notes/checkpoint15_history_inventory.out')
assert qa['status'] == 'PASS' and qa['encoded_images'] == 485
assert state['paper_pages'] == 566 and state['paper_statements'] == 287
assert history['through_checkpoint'] == 14
assert history['historical_entries'] == 16776
large = [e for e in old['transforms'] if e.get('codec') != 'PNG_FROM_PDF01']
assert len(large) == 13
# The successful standard-GAP trace was already added in checkpoint14.
# Preserve these thirteen entries byte-for-byte as JSON values; append none.
plan['transforms'] = large + qa['transforms']
assert [e for e in plan['transforms'] if e.get('codec') != 'PNG_FROM_PDF01'] == large
plan.update({
    'scheduled_utc': '2026-11-16T01:00:00Z',
    'paper_pages': state['paper_pages'],
    'paper_statements': state['paper_statements'],
    'history_through_checkpoint': 14,
    'verification_scope': (
        'All thirteen non-PNG transforms from checkpoint14 are retained unchanged, '
        'with their complete decoded count and SHA-256 checks, full byte comparisons '
        'and exact prefixes. The successful standard-GAP G86 trace is present once; '
        'all original-source and full-lift proof gates remain recorded, and failed '
        'attempts remain retained separately. All485 encoded QA images were regenerated '
        'and compared byte for byte. The materialized checkpoint01-14 history retains '
        'every historical entry or individually specified exact decoded replacement; '
        'all16776 historical entries were checked, including3175 checkpoint14 entries. '
        'This script verifies storage recipes, payloads and executable/source dependencies; '
        'it does not create a ZIP or repeat the long mathematical computations.'),
})
names = [e['original_path'] for key in ('transforms', 'exact_prefix_reconstructions',
                                      'superseded_compression_wrappers')
         for e in plan.get(key, [])]
assert len(names) == len(set(names))
stored = {}
local_paths = {}
checked = {}
def retain(path_name, path, digest):
    path = Path(path)
    actual = sha(path)
    assert actual == digest, (str(path), actual, digest)
    if path_name in stored:
        assert checked[path_name] == actual, path_name
    stored[path_name] = path.stat().st_size
    local_paths[path_name] = path
    checked[path_name] = actual

encoded_prefixes = [e for e in plan['exact_prefix_reconstructions']
                    if 'local_encoded_file' in e]
for entry in plan['transforms'] + encoded_prefixes:
    assert entry['entire_decoded_byte_hash_verified']
    if entry in plan['transforms']:
        assert entry['kind'] in ('raw_bytes', 'gzip_payload')
    if 'local_encoded_file' in entry:
        retain(entry['stored_path'], entry['local_encoded_file'],
               entry.get('encoded_xz_sha256', entry.get('stored_sha256')))
    for extra in entry.get('additional_payloads', []):
        retain(extra['path'], extra['local_file'], extra['sha256'])
for extra in plan.get('additional_payloads', []):
    retain(extra['path'], extra['local_file'], extra['sha256'])

recipe_checks = []
def resolve(name):
    path = ROOT / name
    return path if path.is_file() else local_paths[name]
for entry in large:
    if entry.get('codec') != 'PBC_REPLAY01':
        continue
    recipe = read(Path(entry['local_encoded_file']))
    assert recipe['entire_original_byte_comparison']
    assert recipe['decoded_sha256'] == entry['decoded_sha256']
    assert recipe['decoded_bytes'] == entry['decoded_bytes']
    count = 0
    for name, digest in [('source_dat', 'source_dat_sha256'),
                         ('identity_rows_path', 'identity_rows_sha256'),
                         ('replay_source', 'replay_source_sha256'),
                         ('replay_executable', 'replay_executable_sha256'),
                         ('leaf_payload_path', 'leaf_payload_sha256')]:
        if name in recipe:
            assert sha(resolve(recipe[name])) == recipe[digest], recipe[name]
            count += 1
    for dep in recipe.get('build_dependencies', []):
        assert sha(resolve(dep['path'])) == dep['sha256'], dep['path']
        count += 1
    recipe_checks.append({'path': entry['stored_path'], 'status': 'PASS',
                          'dependencies_checked': count})

dest = ROOT / 'notes/checkpoint15_storage_plan.json'
dest.write_text(json.dumps(plan, indent=2) + '\n')
result = {
    'status': 'PASS', 'scheduled_utc': plan['scheduled_utc'],
    'paper_pages': state['paper_pages'], 'paper_statements': state['paper_statements'],
    'transforms': len(plan['transforms']), 'unchanged_non_png_transforms': len(large),
    'exact_prefix_reconstructions': len(plan['exact_prefix_reconstructions']),
    'encoded_pngs': qa['encoded_images'], 'history_through_checkpoint': 14,
    'distinct_stored_payloads': len(stored), 'stored_payload_bytes': sum(stored.values()),
    'all_payload_hashes_checked': True, 'replay_recipe_checks': recipe_checks,
    'no_zip_created': True, 'path': str(dest), 'plan_sha256': sha(dest),
}
(ROOT / 'notes/checkpoint15_storage_plan_verification.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
