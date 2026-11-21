"""Exact, source-only captured-to-frozen reader C release delta.

Only files named out/checks/scan026_C_release_* are written. No images are
opened, no source file is changed, and no root review or ink decision is claimed.
"""
from __future__ import annotations

import collections
import copy
import difflib
import hashlib
import json
import re
from pathlib import Path

BASE = Path('/workspace/scratch/94548b74fbe0')
OUT = BASE / 'out/checks'
PREFIX = 'scan026_C_release_'
CHUNK_BYTES = 11000
EXPECTED = {
    'out/checks/scan026_root_preread/C_reading.tex': '5cba4cd65505de034fdca3b6a14a8647b14ff6c6fce11bec16565a89fa0a42e5',
    'out/checks/scan026_root_preread/C_reading.md': '56cb68b7714f3a852cf3ed38f96ab259eb1a2fd2149359a5009512927eed02cb',
    'out/checks/scan026_root_preread/C_report.json': 'fdde5ed7074567d2e7945a93dd71a665dcc2af6d4409d46d2e942d5d1d8298c4',
    'out/readers/026/C/reading.tex': '7c05f3fc0f28985e2cd66c3fbe6486eaf7d38ab20a4a2f7fbf29b1742868b951',
    'out/readers/026/C/reading.md': '2dca9f025556945f69c0b47dab83a87497c733252e9528f00095428c28d80193',
    'out/readers/026/C/report.json': 'b7d7ef133f3b8943075e860c2ecc60249db0f9eb0afc10d15edc3a18d499c621',
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def dumps(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'))


def prettybytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def write(name, data):
    assert name.startswith(PREFIX)
    path = OUT / name
    path.write_bytes(data)
    return {'path': str(path.relative_to(BASE)), 'bytes': len(data), 'sha256': sha(data)}


def writejson(name, value):
    return write(name, prettybytes(value))


def escaped(value):
    return str(value).replace('~', '~0').replace('/', '~1')


def child(path, key):
    return path + '/' + escaped(key)


def flatten(value, logical='', pointer='', result=None, pointers=None):
    if result is None:
        result, pointers = {}, {}
    pointers[logical] = pointer
    if isinstance(value, dict):
        result[logical] = {'kind': 'object', 'keys': list(value)}
        for key, item in value.items():
            flatten(item, child(logical, key), child(pointer, key), result, pointers)
    elif isinstance(value, list):
        if logical == '/differences':
            ids = [item['id'] for item in value]
            assert all(isinstance(identifier, str) for identifier in ids)
            assert len(ids) == len(set(ids)), 'difference ids must be unique'
            result[logical] = {'kind': 'id-list', 'ids': ids}
            for index, (identifier, item) in enumerate(zip(ids, value)):
                flatten(item, child(logical, '@' + identifier), child(pointer, index), result, pointers)
        else:
            result[logical] = {'kind': 'array', 'length': len(value)}
            for index, item in enumerate(value):
                flatten(item, child(logical, index), child(pointer, index), result, pointers)
    else:
        result[logical] = {'kind': 'value', 'value': value}
    return result, pointers


def inflate(flat, path=''):
    node = flat[path]
    if node['kind'] == 'object':
        return {key: inflate(flat, child(path, key)) for key in node['keys']}
    if node['kind'] == 'array':
        return [inflate(flat, child(path, index)) for index in range(node['length'])]
    if node['kind'] == 'id-list':
        return [inflate(flat, child(path, '@' + identifier)) for identifier in node['ids']]
    assert node['kind'] == 'value'
    return copy.deepcopy(node['value'])


def apply_ops(flat, operations, lookup, forward=True):
    result = copy.deepcopy(flat)
    for op in operations:
        before, after = (op['old_node'], op['new_node']) if forward else (op['new_node'], op['old_node'])
        path = op['logical_path']
        if before is None:
            assert path not in result
        else:
            assert path in result and dumps(result[path]) == dumps(lookup[before])
        if after is None:
            del result[path]
        else:
            result[path] = copy.deepcopy(lookup[after])
    return result


def apply_unified(source_bytes, diff_bytes, reverse=False):
    """Read the written unified diff and replay it against exact UTF-8 lines."""
    source = source_bytes.decode('utf-8').splitlines(keepends=True)
    delta = diff_bytes.decode('utf-8').splitlines(keepends=True)
    assert delta[0].startswith('--- ') and delta[1].startswith('+++ ')
    out, position, row = [], 0, 2
    while row < len(delta):
        match = re.fullmatch(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@\n', delta[row])
        assert match, repr(delta[row])
        old_start, old_count, new_start, new_count = match.groups()
        old_start, new_start = int(old_start), int(new_start)
        old_count = 1 if old_count is None else int(old_count)
        new_count = 1 if new_count is None else int(new_count)
        start, count = (new_start, new_count) if reverse else (old_start, old_count)
        start = start - 1 if count else start
        assert start >= position
        out.extend(source[position:start])
        position = start
        row += 1
        old_seen = new_seen = 0
        while old_seen < old_count or new_seen < new_count:
            line = delta[row]
            row += 1
            mark, body = line[0], line[1:]
            assert mark in ' +-'
            old_seen += mark in ' -'
            new_seen += mark in ' +'
            effective = {'+': '-', '-': '+'}.get(mark, mark) if reverse else mark
            if effective in ' -':
                assert position < len(source) and source[position] == body
                position += 1
            if effective in ' +':
                out.append(body)
        assert old_seen == old_count and new_seen == new_count
    out.extend(source[position:])
    return ''.join(out).encode('utf-8')


inputs = {path: (BASE / path).read_bytes() for path in EXPECTED}
assert all(sha(data) == EXPECTED[path] for path, data in inputs.items())
old_path = 'out/checks/scan026_root_preread/C_report.json'
new_path = 'out/readers/026/C/report.json'
old_bytes, new_bytes = inputs[old_path], inputs[new_path]
old, new = json.loads(old_bytes), json.loads(new_bytes)
assert prettybytes(old) == old_bytes
assert prettybytes(new) == new_bytes
old_flat, old_ptr = flatten(old)
new_flat, new_ptr = flatten(new)
assert len(set(old_ptr.values())) == len(old_ptr)
assert len(set(new_ptr.values())) == len(new_ptr)
assert prettybytes(inflate(old_flat)) == old_bytes
assert prettybytes(inflate(new_flat)) == new_bytes

pool, pool_ids = [], {}


def intern(node):
    signature = dumps(node)
    if signature not in pool_ids:
        identifier = 'V%04d' % (len(pool) + 1)
        pool_ids[signature] = identifier
        pool.append({'id': identifier, 'node': copy.deepcopy(node)})
    return pool_ids[signature]


ops = []
for path in list(old_flat) + [path for path in new_flat if path not in old_flat]:
    if path in old_flat and path in new_flat and dumps(old_flat[path]) == dumps(new_flat[path]):
        continue
    ops.append({
        'id': 'D%04d' % (len(ops) + 1),
        'logical_path': path,
        'old_json_pointer': old_ptr.get(path),
        'new_json_pointer': new_ptr.get(path),
        'old_node': intern(old_flat[path]) if path in old_flat else None,
        'new_node': intern(new_flat[path]) if path in new_flat else None,
    })
assert len(ops) == len({op['logical_path'] for op in ops})
lookup = {entry['id']: entry['node'] for entry in pool}
forward = apply_ops(old_flat, ops, lookup)
inverse = apply_ops(new_flat, ops, lookup, forward=False)
assert set(forward) == set(new_flat)
assert set(inverse) == set(old_flat)
assert all(dumps(forward[path]) == dumps(node) for path, node in new_flat.items())
assert all(dumps(inverse[path]) == dumps(node) for path, node in old_flat.items())
assert prettybytes(inflate(forward)) == new_bytes
assert prettybytes(inflate(inverse)) == old_bytes

old_index = {item['id']: index for index, item in enumerate(old['differences'])}
new_index = {item['id']: index for index, item in enumerate(new['differences'])}
permutation = [{'id': identifier, 'old_index': old_index.get(identifier), 'new_index': index}
               for identifier, index in new_index.items()]
permutation += [{'id': identifier, 'old_index': index, 'new_index': None}
                for identifier, index in old_index.items() if identifier not in new_index]
assert len(permutation) == len(set(old_index) | set(new_index))

text_diffs = []
for extension in ('tex', 'md'):
    before_path = 'out/checks/scan026_root_preread/C_reading.' + extension
    after_path = 'out/readers/026/C/reading.' + extension
    before, after = inputs[before_path], inputs[after_path]
    before_lines = before.decode('utf-8').splitlines(keepends=True)
    after_lines = after.decode('utf-8').splitlines(keepends=True)
    assert all(line.endswith('\n') for line in before_lines + after_lines)
    diff = ''.join(difflib.unified_diff(before_lines, after_lines, fromfile=before_path, tofile=after_path)).encode('utf-8')
    item = write(PREFIX + 'reading.' + extension + '.diff', diff)
    written = (BASE / item['path']).read_bytes()
    assert written == diff
    recovered_after = apply_unified(before, written)
    recovered_before = apply_unified(after, written, reverse=True)
    assert recovered_after == after and recovered_before == before
    item.update({'old_path': before_path, 'new_path': after_path,
                 'lines': len(diff.splitlines()), 'forward_exact_bytes': True,
                 'inverse_exact_bytes': True, 'forward_sha256': sha(recovered_after),
                 'inverse_sha256': sha(recovered_before)})
    text_diffs.append(item)

pool_file = writejson(PREFIX + 'pool_v01.json', pool)
ops_file = writejson(PREFIX + 'operations_v01.json', ops)

# Exact path factoring. Prefixes and suffixes are literal strings; no source
# value, field name, index, order, scope, or attribution is rewritten.
def split(path):
    bits = path.split('/')
    record_arrays = {'differences', 'doubts', 'inventory', 'notation',
                     'C_uncertainty_rows', 'crops', 'all_Sigma_occurrences'}
    if len(bits) > 2 and bits[1] in record_arrays:
        return '/'.join(bits[:3]), '/'.join([''] + bits[3:]) if len(bits) > 3 else ''
    return path, ''


products = []
for after in [entry['id'] for entry in pool] + [None]:
    assigned = [op for op in ops if op['new_node'] == after]
    if not assigned:
        continue
    by_suffix = collections.OrderedDict()
    for op in assigned:
        record, suffix = split(op['logical_path'])
        by_suffix.setdefault((op['old_node'], suffix), []).append(record)
    factors = collections.OrderedDict()
    for (before, suffix), records in by_suffix.items():
        assert len(records) == len(set(records))
        factors.setdefault((before, tuple(records)), []).append(suffix)
    for (before, records), suffixes in factors.items():
        products.append({'new_node': after, 'old_node': before,
                         'records': list(records), 'suffixes': suffixes})

expanded = [(record + suffix, product['old_node'], product['new_node'])
            for product in products for record in product['records'] for suffix in product['suffixes']]
expected_triples = [(op['logical_path'], op['old_node'], op['new_node']) for op in ops]
assert len(expanded) == len(set(expanded))
assert set(expanded) == set(expected_triples)

record_ids, suffix_ids = {}, {}
for product in products:
    for record in product['records']:
        record_ids.setdefault(record, len(record_ids) + 1)
    for suffix in product['suffixes']:
        suffix_ids.setdefault(suffix, len(suffix_ids) + 1)

old_signatures = collections.defaultdict(list)
for path, node in old_flat.items():
    old_signatures[dumps(node)].append(old_ptr[path])
old_pointer_nodes = {old_ptr[path]: node for path, node in old_flat.items()}

# Complete review stream: literal path dictionaries, all pooled values (either
# an exact captured-node reference or the complete novel node), then every
# Cartesian-product field mapping, including deletions.
rows = [['R', identifier, record] for record, identifier in record_ids.items()]
rows += [['S', identifier, suffix] for suffix, identifier in suffix_ids.items()]
captured_count = novel_count = 0
novel_final_ids = []
final_value_ids = {op['new_node'] for op in ops if op['new_node'] is not None}
for entry in pool:
    number = int(entry['id'][1:])
    signature = dumps(entry['node'])
    matches = old_signatures.get(signature, [])
    if matches:
        pointer = min(matches, key=lambda p: (len(p.encode('utf-8')), p))
        assert dumps(old_pointer_nodes[pointer]) == signature
        rows.append(['C', number, pointer])
        captured_count += 1
    else:
        rows.append(['V', number, entry['node']])
        novel_count += 1
        assert entry['id'] in final_value_ids
        novel_final_ids.append(entry['id'])

for product in products:
    rows.append(['P', int(product['new_node'][1:]) if product['new_node'] else None,
                 int(product['old_node'][1:]) if product['old_node'] else None,
                 [record_ids[record] for record in product['records']],
                 [suffix_ids[suffix] for suffix in product['suffixes']]])

review_files, chunk, size = [], [], 0


def save_chunk():
    if not chunk:
        return
    name = PREFIX + 'review_v02_%02d.jsonl' % (len(review_files) + 1)
    item = write(name, b''.join(chunk))
    item['rows'] = len(chunk)
    review_files.append(item)


for row in rows:
    line = (dumps(row) + '\n').encode('utf-8')
    assert len(line) <= CHUNK_BYTES, 'one complete row exceeds review chunk bound'
    if chunk and size + len(line) > CHUNK_BYTES:
        save_chunk()
        chunk, size = [], 0
    chunk.append(line)
    size += len(line)
save_chunk()
assert all(item['bytes'] <= CHUNK_BYTES for item in review_files)

# Decode the actual on-disk compact files. The following equality checks cover
# all pool nodes and all operations, not selected examples or dict equality.
decoded_rows = []
for item in review_files:
    data = (BASE / item['path']).read_bytes()
    assert sha(data) == item['sha256']
    decoded_rows.extend(json.loads(line) for line in data.splitlines())
assert decoded_rows == rows
decoded_records, decoded_suffixes, decoded_pool = {}, {}, {}
decoded_products = []
for row in decoded_rows:
    tag = row[0]
    if tag in ('R', 'S'):
        target = decoded_records if tag == 'R' else decoded_suffixes
        assert row[1] not in target
        target[row[1]] = row[2]
    elif tag in ('C', 'V'):
        identifier = 'V%04d' % row[1]
        assert identifier not in decoded_pool
        decoded_pool[identifier] = copy.deepcopy(old_pointer_nodes[row[2]] if tag == 'C' else row[2])
    else:
        assert tag == 'P'
        decoded_products.append(row)
assert set(decoded_pool) == set(lookup)
assert all(dumps(decoded_pool[key]) == dumps(node) for key, node in lookup.items())
compact_ops = []
for _, after, before, records, suffixes in decoded_products:
    for record in records:
        for suffix in suffixes:
            path = decoded_records[record] + decoded_suffixes[suffix]
            compact_ops.append({'logical_path': path,
                                'old_node': 'V%04d' % before if before is not None else None,
                                'new_node': 'V%04d' % after if after is not None else None,
                                'old_json_pointer': old_ptr.get(path),
                                'new_json_pointer': new_ptr.get(path)})
compact_triples = [(op['logical_path'], op['old_node'], op['new_node']) for op in compact_ops]
assert len(compact_triples) == len(set(compact_triples))
assert set(compact_triples) == set(expected_triples)
original_with_pointers = {(op['logical_path'], op['old_node'], op['new_node'],
                          op['old_json_pointer'], op['new_json_pointer']) for op in ops}
decoded_with_pointers = {(op['logical_path'], op['old_node'], op['new_node'],
                         op['old_json_pointer'], op['new_json_pointer']) for op in compact_ops}
assert original_with_pointers == decoded_with_pointers
compact_forward = prettybytes(inflate(apply_ops(old_flat, compact_ops, decoded_pool)))
compact_inverse = prettybytes(inflate(apply_ops(new_flat, compact_ops, decoded_pool, forward=False)))
assert compact_forward == new_bytes
assert compact_inverse == old_bytes

# Reload the full pool and operations as well, to check the written v01 files.
disk_pool = json.loads((BASE / pool_file['path']).read_bytes())
disk_ops = json.loads((BASE / ops_file['path']).read_bytes())
disk_lookup = {entry['id']: entry['node'] for entry in disk_pool}
v01_forward = prettybytes(inflate(apply_ops(old_flat, disk_ops, disk_lookup)))
v01_inverse = prettybytes(inflate(apply_ops(new_flat, disk_ops, disk_lookup, forward=False)))
assert v01_forward == new_bytes and v01_inverse == old_bytes
assert all((BASE / path).read_bytes() == data for path, data in inputs.items())

manifest = {
    'scope': 'Exact source-only C captured-to-frozen release delta; no ink decision and no root review claimed.',
    'inputs': [{'path': path, 'bytes': len(data), 'sha256': sha(data)} for path, data in inputs.items()],
    'codec': 'Each object retains its exact ordered keys. Ordinary arrays retain length and numeric-index children. Only /differences uses checked unique source ids for logical children and retains the complete ordered id list. Scalars retain parsed JSON types and values. Both complete input report byte strings exactly equal UTF-8 json.dumps(ensure_ascii=False, indent=2) plus LF; flatten/inflate and both delta directions reproduce those exact bytes.',
    'logical_path_rule': 'RFC6901 escaping; /differences/@ID uses the exact source id. Replace @ID by old_index or new_index from difference_permutation to obtain the numeric pointer. Every other logical path is already a numeric JSON pointer. A missing old_node or new_node has a null corresponding pointer.',
    'old_difference_count': len(old_index), 'new_difference_count': len(new_index),
    'difference_permutation': permutation,
    'inserted_difference_ids': [item['id'] for item in permutation if item['old_index'] is None],
    'removed_difference_ids': [item['id'] for item in permutation if item['new_index'] is None],
    'old_logical_nodes': len(old_flat), 'new_logical_nodes': len(new_flat),
    'changed_node_count': len(ops),
    'added_node_count': sum(op['old_node'] is None for op in ops),
    'deleted_node_count': sum(op['new_node'] is None for op in ops),
    'replaced_node_count': sum(op['old_node'] is not None and op['new_node'] is not None for op in ops),
    'pooled_distinct_nodes': len(pool), 'distinct_final_changed_nodes': len(final_value_ids),
    'novel_final_nodes': novel_count, 'captured_exact_pool_matches': captured_count,
    'full_pool_file': pool_file, 'full_operations_file': ops_file,
    'text_diffs': text_diffs,
    'root_review_claimed': False,
}
manifest_file = writejson(PREFIX + 'manifest_v01.json', manifest)

replay = {
    'source_only': True,
    'input_hashes_match_expected': True,
    'old_report_serializer_and_key_order_roundtrip_exact': True,
    'new_report_serializer_and_key_order_roundtrip_exact': True,
    'v01_reloaded_pool_and_operations_forward_exact_bytes': v01_forward == new_bytes,
    'v01_reloaded_pool_and_operations_inverse_exact_bytes': v01_inverse == old_bytes,
    'v02_reloaded_compact_review_forward_exact_bytes': compact_forward == new_bytes,
    'v02_reloaded_compact_review_inverse_exact_bytes': compact_inverse == old_bytes,
    'forward_sha256': sha(compact_forward), 'inverse_sha256': sha(compact_inverse),
    'all_pooled_values_recovered_with_key_order_and_types': True,
    'all_captured_node_references_equal_exact_pool_nodes': True,
    'all_novel_pool_nodes_printed_in_full': True,
    'all_record_suffix_products_expand_exactly': True,
    'all_operations_with_old_and_new_numeric_pointers_recovered': True,
    'no_duplicate_operation_path': True,
    'deleted_operations_included': sum(op['new_node'] is None for op in compact_ops),
    'all_six_source_files_unchanged': True,
    'no_image_operations': True,
    'root_review_claimed': False,
}
replay_file = writejson(PREFIX + 'replay_v01.json', replay)

review_index = {
    'scope': 'Complete compact exact delta review; captured C has already been read by the requesting root, but this artifact claims no root review.',
    'read_order': 'Read manifest_v01.json, this index, all numbered review_v02 JSONL files in order, both complete text diffs, and replay_v01.json.',
    'row_schemas': {
        'R': '["R", record_number, exact_logical_prefix]',
        'S': '["S", suffix_number, exact_suffix]',
        'C': '["C", pool_number, exact_captured_numeric_JSON_pointer]. The node at that captured pointer, encoded by the manifest codec, exactly equals pool node V%04d for pool_number. The complete equality was checked; choose the shortest literal pointer deterministically among exact matches.',
        'V': '["V", pool_number, complete_exact_novel_codec_node]. Every node absent from the captured report node pool appears here in full exactly once.',
        'P': '["P", new_pool_number_or_null, old_pool_number_or_null, record_numbers, suffix_numbers]. Every Cartesian product record-prefix + suffix is exactly one original operation with those old/new pool nodes. Null new means deletion; null old means addition. The product equality and lack of duplicate paths were checked over all operations.',
    },
    'pool_number_rule': 'Integer n denotes the full v01 pool id V%04d formatted with n; it is an exact numeric alias, not a source value.',
    'pointer_rule': manifest['logical_path_rule'],
    'value_scope': 'All role, hand, attachment, candidate, and container fields are retained through exact nodes and paths. Exact references retain their captured source values. Complete candidates are recovered by ordered object/array nodes plus all descendant values. The procedure performs no consistency repair or attribution transfer.',
    'record_dictionary_entries': len(record_ids), 'suffix_dictionary_entries': len(suffix_ids),
    'all_pool_values_declared': len(pool), 'captured_exact_matches': captured_count,
    'complete_novel_final_nodes': novel_count,
    'product_rows': len(products), 'expanded_operations': len(compact_ops),
    'expanded_deleted_operations': sum(op['new_node'] is None for op in compact_ops),
    'maximum_chunk_bytes': CHUNK_BYTES,
    'review_files': review_files,
    'manifest': manifest_file, 'byte_replay': replay_file,
    'root_review_claimed': False,
}
index_file = writejson(PREFIX + 'review_index_v02.json', review_index)

note = '# C release: exact source delta\n\n'
note += 'Source-only comparison; no ink decision and no root review are claimed. All six captured/frozen input hashes matched, and all source files remained unchanged.\n\n'
note += 'Read `scan026_C_release_manifest_v01.json`, `scan026_C_release_review_index_v02.json`, every numbered review chunk below, both complete text diffs, and `scan026_C_release_replay_v01.json`. The index defines every finite alias and Cartesian product used by the compact review.\n\n'
note += f'The complete report delta has {len(ops)} operations: {manifest["added_node_count"]} additions, {manifest["replaced_node_count"]} replacements, and {manifest["deleted_node_count"]} deletions. The pool contains {len(pool)} exact nodes; {novel_count} novel final nodes are printed in full and {captured_count} exact captured-node matches are identified by literal numeric JSON pointers. All full candidates and role/hand/attachment fields remain reconstructible with their exact paths and container order.\n\n'
note += 'All 76 captured difference ids remain. New D43 and D44 occupy final indices 44 and 45. Old indices 0–43 map to the same indices; old indices 44–75 map to final indices 46–77. The manifest prints the complete 78-entry id-to-index mapping.\n\n'
note += 'The written full pool/operations and the written compact review were independently reloaded and expanded. Both yielded the complete frozen report bytes forward and the complete captured report bytes backward. The unified TeX and Markdown diffs were also parsed and replayed in both directions with exact byte equality. No raw source inconsistency was edited.\n\n'
for item in review_files:
    note += f'- `{item["path"]}` — {item["rows"]} complete rows, {item["bytes"]} bytes.\n'
note += '\nComplete text diffs:\n\n'
for item in text_diffs:
    note += f'- `{item["path"]}` — {item["lines"]} lines, {item["bytes"]} bytes.\n'
write(PREFIX + 'readme_v02.md', note.encode('utf-8'))

print(json.dumps({'manifest': manifest_file, 'review_index': index_file,
                  'replay': replay_file, 'review_files': review_files,
                  'text_diffs': text_diffs,
                  'counts': {key: manifest[key] for key in ('changed_node_count', 'added_node_count', 'deleted_node_count', 'replaced_node_count', 'pooled_distinct_nodes', 'distinct_final_changed_nodes', 'novel_final_nodes', 'captured_exact_pool_matches')},
                  'all_exact_byte_replays_passed': True}, ensure_ascii=False, indent=2))
