"""Finite exact factoring of release-delta paths; no image operations."""
import collections
import hashlib
import json
from pathlib import Path

BASE = Path('/workspace/scratch/94548b74fbe0')
OUT = BASE / 'out/checks'
P = 'scan026_source_A_release_'
ops = json.loads((OUT / (P + 'operations_v01.json')).read_text())
pool = json.loads((OUT / (P + 'pool_v01.json')).read_text())
manifest = json.loads((OUT / (P + 'manifest_v01.json')).read_text())
lookup = {v['id']: v['node'] for v in pool}


def split(path):
    bits = path.split('/')
    if len(bits) > 2 and bits[1] in ('differences', 'doubts', 'inventory', 'notation', 'C_doubt_source_rows', 'crops'):
        return '/'.join(bits[:3]), '/'.join([''] + bits[3:]) if len(bits) > 3 else ''
    return path, ''


review = []
for value in pool:
    assigned = [o for o in ops if o['new_node'] == value['id']]
    if not assigned:
        continue
    # A product is used only for exactly equal ordered record sets.
    by_suffix = collections.OrderedDict()
    for op in assigned:
        record, suffix = split(op['logical_path'])
        by_suffix.setdefault((op['old_node'], suffix), []).append(record)
    factors = collections.OrderedDict()
    for (before, suffix), records in by_suffix.items():
        assert len(records) == len(set(records))
        key = (before, tuple(records))
        factors.setdefault(key, []).append(suffix)
    products = [{'old_node': before, 'records': list(records), 'suffixes': suffixes}
                for (before, records), suffixes in factors.items()]
    expanded = [(r + s, product['old_node'], value['id']) for product in products
                for r in product['records'] for s in product['suffixes']]
    expected = [(o['logical_path'], o['old_node'], o['new_node']) for o in assigned]
    assert len(expanded) == len(set(expanded))
    assert set(expanded) == set(expected)
    review.append({'value_id': value['id'], 'exact_final_node': value['node'], 'exact_field_products': products})

expanded_all = [(r + s, product['old_node'], row['value_id']) for row in review
                for product in row['exact_field_products'] for r in product['records'] for s in product['suffixes']]
expected_all = [(o['logical_path'], o['old_node'], o['new_node']) for o in ops if o['new_node'] is not None]
assert len(expanded_all) == len(set(expanded_all))
assert set(expanded_all) == set(expected_all)

files, chunk, size = [], [], 0


def save_chunk():
    if not chunk:
        return
    name = P + 'review_v02_%02d.jsonl' % (len(files) + 1)
    b = ''.join(chunk).encode()
    (OUT / name).write_bytes(b)
    files.append({'path': 'out/checks/' + name, 'rows': len(chunk), 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()})


for row in review:
    line = json.dumps(row, ensure_ascii=False) + '\n'
    n = len(line.encode())
    if chunk and size + n > 12500:
        save_chunk()
        chunk, size = [], 0
    chunk.append(line)
    size += n
save_chunk()

result = {
    'scope': 'Exact source-only final-field-value review; no root review claimed.',
    'rule': 'For each exact_field_products entry, the logical paths are every record + every suffix. The finite equality check confirms each listed product exactly equals its assigned original operation set. No absent cross-product combination is supplied.',
    'pointer_rule': 'For logical /differences/@ID paths, replace @ID by that source id\u2019s old_index or new_index from the manifest. The old pointer is null when the old node is absent; the final pointer is null when the final node is absent. Other logical paths are ordinary JSON pointers. All use RFC6901 escaping. Numeric indices are zero-based.',
    'old_value_rule': 'old_node is the exact prior node id in pool_v01.json; null means this field did not exist. All final values are printed once. Unchanged field values are omitted from the delta only and remain in the frozen raw sources.',
    'container_rule': 'A node of kind object retains its exact ordered key array; array retains exact length; id-list retains the full ordered ids. A kind value node is the exact JSON scalar.',
    'distinct_final_values': len(review),
    'final_field_operations': len(expanded_all),
    'deleted_field_operations': [o for o in ops if o['new_node'] is None],
    'all_products_expand_exactly': True,
    'no_path_duplicate': len(expanded_all) == len(set(expanded_all)),
    'all_final_operations_recovered': set(expanded_all) == set(expected_all),
    'byte_forward_inverse_evidence': P + 'replay_v01.json',
    'review_files': files,
    'root_review_claimed': False,
}
(OUT / (P + 'compact_replay_v02.json')).write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
note = '# A release review v02\n\n'
note += 'Use this exact factored review instead of the verbose v01 review chunks. The v01 pool, operations and byte replay remain the reversible source record. No original file was changed, and no root review is claimed.\n\n'
note += 'All 63 captured difference rows remain. New final row 31 is A026-L13. The full exact id permutation is in `scan026_source_A_release_manifest_v01.json`.\n\n'
note += result['rule'] + '\n\n' + result['pointer_rule'] + '\n\n' + result['old_value_rule'] + '\n\n' + result['container_rule'] + '\n\n'
note += f"The review prints {len(review)} distinct final values once and maps all {len(expanded_all)} final changed/added nodes. Both complete report byte strings were recovered exactly, including JSON key order.\n\n"
for f in files:
    note += f"- `{f['path']}`: {f['rows']} values, {f['bytes']} bytes.\n"
(OUT / (P + 'readme_v02.md')).write_text(note)
print(json.dumps(result, ensure_ascii=False, indent=2))
