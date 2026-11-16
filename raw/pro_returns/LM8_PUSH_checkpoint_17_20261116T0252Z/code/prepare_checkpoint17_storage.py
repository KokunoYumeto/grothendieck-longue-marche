#!/usr/bin/env python3
"""Prepare checkpoint17's verified storage plan; never create an archive."""
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

old = read(ROOT / 'notes/checkpoint16_storage_plan.json')
plan = json.loads(json.dumps(old))
qa = read(ROOT / 'notes/checkpoint17_qa_encoding.json')
state = read(ROOT / 'notes/checkpoint17_frozen_state.json')
history = read(ROOT / 'notes/checkpoint17_history_inventory.out')
assert qa['status'] == 'PASS' and qa['encoded_images'] >= 544
assert state['paper_pages'] >= 600 and state['paper_statements'] >= 303
assert history['through_checkpoint'] == 16
assert history['historical_entries'] == 24074
large = [e for e in old['transforms'] if e.get('codec') != 'PNG_FROM_PDF01']
assert len(large) == 21
delta = read(ROOT / 'notes/checkpoint16_pdf_delta_encoding.json')
assert delta['status'] == 'PASS' and len(delta['transforms']) == 8
assert [e for e in large if e.get('codec') == 'ZSTD_PDF_DICT01'] == delta['transforms']
new_delta = read(ROOT / 'notes/checkpoint17_pdf_delta_encoding.json')
assert new_delta['status'] == 'PASS' and len(new_delta['transforms']) == 1
large += new_delta['transforms']
# The thirteen numerical transforms, including the standard-GAP trace
# added in checkpoint14, and the eight prior PDF restorations remain unchanged.
plan['transforms'] = large + qa['transforms']
assert [e for e in plan['transforms'] if e.get('codec') != 'PNG_FROM_PDF01'] == large
plan.update({
    'scheduled_utc': '2026-11-16T03:00:00Z',
    'paper_pages': state['paper_pages'],
    'paper_statements': state['paper_statements'],
    'history_through_checkpoint': 16,
    'verification_scope': (f'Thirteen unchanged numerical transforms, eight retained PDF-delta transforms plus one new exact first-build PDF restoration, and {qa["encoded_images"]} byte-exact PNG regenerations. History through checkpoint16 accounts for all24074 historical entries. Every failed/superseded PDF byte is retained exactly. The new decoder was executed with a complete original-byte comparison; superseded PNGs also have a verified missing-source-PDF restoration path. All stored payload and literal dependency hashes are checked. No ZIP is created by this script.'),
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

pdf_recipe_checks = []
seen_pdf_recipes = set()
for entry in delta['transforms'] + new_delta['transforms']:
    recipe_path = entry['stored_path']
    if recipe_path in seen_pdf_recipes:
        continue
    seen_pdf_recipes.add(recipe_path)
    recipe = read(Path(entry['local_encoded_file']))
    assert recipe['entire_original_byte_comparison']
    assert recipe['decoded_sha256'] == entry['decoded_sha256']
    assert recipe['decoded_bytes'] == entry['decoded_bytes']
    for prefix in ('base', 'payload'):
        name = recipe[prefix + '_path']
        actual = ROOT / name
        assert actual.is_file()
        assert sha(actual) == recipe[prefix + '_sha256']
        assert actual.stat().st_size == recipe[prefix + '_bytes']
    pdf_recipe_checks.append({'path': recipe_path, 'status': 'PASS',
                              'literal_dependencies_checked': 2})

dest = ROOT / 'notes/checkpoint17_storage_plan.json'
dest.write_text(json.dumps(plan, indent=2) + '\n')
result = {
    'status': 'PASS', 'scheduled_utc': plan['scheduled_utc'],
    'paper_pages': state['paper_pages'], 'paper_statements': state['paper_statements'],
    'transforms': len(plan['transforms']), 'unchanged_numerical_transforms': 13, 'retained_pdf_delta_transforms': 8, 'new_pdf_delta_transforms': 1,
    'exact_prefix_reconstructions': len(plan['exact_prefix_reconstructions']),
    'encoded_pngs': qa['encoded_images'], 'history_through_checkpoint': 16,
    'distinct_stored_payloads': len(stored), 'stored_payload_bytes': sum(stored.values()),
    'all_payload_hashes_checked': True, 'replay_recipe_checks': recipe_checks, 'pdf_recipe_checks': pdf_recipe_checks,
    'no_zip_created': True, 'path': str(dest), 'plan_sha256': sha(dest),
}
(ROOT / 'notes/checkpoint17_storage_plan_verification.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
