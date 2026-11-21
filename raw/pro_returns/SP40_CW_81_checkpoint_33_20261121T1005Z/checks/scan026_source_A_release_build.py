"""Source-only, reversible review of the captured A report and frozen A release.

No image data is read. The JSON codec preserves object key order. The only
keyed-list transform is report.differences, whose unique source ids are checked.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

BASE = Path('/workspace/scratch/94548b74fbe0')
OUT = BASE / 'out/checks'
OLD = BASE / 'out/checks/scan026_root_preread/A_report.json'
NEW = BASE / 'out/readers/026/A/report.json'
PREFIX = 'scan026_source_A_release_'


def dumps(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'))


def escaped(s):
    return str(s).replace('~', '~0').replace('/', '~1')


def child(path, key):
    return path + '/' + escaped(key)


def flatten(value, logical='', pointer='', result=None, pointers=None):
    if result is None:
        result, pointers = {}, {}
    pointers[logical] = pointer
    if isinstance(value, dict):
        result[logical] = {'kind': 'object', 'keys': list(value)}
        for k, v in value.items():
            flatten(v, child(logical, k), child(pointer, k), result, pointers)
    elif isinstance(value, list):
        if logical == '/differences':
            ids = [item['id'] for item in value]
            assert len(ids) == len(set(ids)), 'difference ids must be unique'
            result[logical] = {'kind': 'id-list', 'ids': ids}
            for i, (identifier, v) in enumerate(zip(ids, value)):
                flatten(v, child(logical, '@' + identifier), child(pointer, i), result, pointers)
        else:
            result[logical] = {'kind': 'array', 'length': len(value)}
            for i, v in enumerate(value):
                flatten(v, child(logical, i), child(pointer, i), result, pointers)
    else:
        result[logical] = {'kind': 'value', 'value': value}
    return result, pointers


def inflate(flat, path=''):
    node = flat[path]
    if node['kind'] == 'object':
        return {k: inflate(flat, child(path, k)) for k in node['keys']}
    if node['kind'] == 'array':
        return [inflate(flat, child(path, i)) for i in range(node['length'])]
    if node['kind'] == 'id-list':
        return [inflate(flat, child(path, '@' + i)) for i in node['ids']]
    assert node['kind'] == 'value'
    return copy.deepcopy(node['value'])


def prettybytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def rel(path):
    return str(path.relative_to(BASE))


def writejson(suffix, value):
    (OUT / (PREFIX + suffix + '.json')).write_bytes(prettybytes(value))


old_bytes, new_bytes = OLD.read_bytes(), NEW.read_bytes()
old, new = json.loads(old_bytes), json.loads(new_bytes)
assert prettybytes(old) == old_bytes
assert prettybytes(new) == new_bytes
old_flat, old_ptr = flatten(old)
new_flat, new_ptr = flatten(new)
assert prettybytes(inflate(old_flat)) == old_bytes
assert prettybytes(inflate(new_flat)) == new_bytes

pool = []
pool_ids = {}


def intern(value):
    signature = dumps(value)
    if signature not in pool_ids:
        identifier = 'V%04d' % (len(pool) + 1)
        pool_ids[signature] = identifier
        pool.append({'id': identifier, 'node': copy.deepcopy(value)})
    return pool_ids[signature]


ops = []
all_paths = list(old_flat) + [p for p in new_flat if p not in old_flat]
for path in all_paths:
    ov, nv = old_flat.get(path), new_flat.get(path)
    # dumps preserves key order inside structural nodes and scalar type.
    if path in old_flat and path in new_flat and dumps(ov) == dumps(nv):
        continue
    ops.append({
        'id': 'D%04d' % (len(ops) + 1),
        'logical_path': path,
        'old_json_pointer': old_ptr.get(path),
        'new_json_pointer': new_ptr.get(path),
        'old_node': intern(ov) if path in old_flat else None,
        'new_node': intern(nv) if path in new_flat else None,
    })

lookup = {p['id']: p['node'] for p in pool}


def apply(flat, forward):
    result = copy.deepcopy(flat)
    for op in ops:
        before, after = (op['old_node'], op['new_node']) if forward else (op['new_node'], op['old_node'])
        path = op['logical_path']
        if before is None:
            assert path not in result
        else:
            assert dumps(result[path]) == dumps(lookup[before])
        if after is None:
            del result[path]
        else:
            result[path] = copy.deepcopy(lookup[after])
    return result


forward = apply(old_flat, True)
inverse = apply(new_flat, False)
assert prettybytes(inflate(forward)) == new_bytes
assert prettybytes(inflate(inverse)) == old_bytes
assert set(forward) == set(new_flat)
assert set(inverse) == set(old_flat)
assert all(dumps(forward[k]) == dumps(v) for k, v in new_flat.items())
assert all(dumps(inverse[k]) == dumps(v) for k, v in old_flat.items())

old_index = {v['id']: i for i, v in enumerate(old['differences'])}
new_index = {v['id']: i for i, v in enumerate(new['differences'])}
permutation = [{'id': identifier, 'old_index': old_index.get(identifier), 'new_index': i}
               for identifier, i in new_index.items()]
removed = [{'id': identifier, 'old_index': i, 'new_index': None}
           for identifier, i in old_index.items() if identifier not in new_index]
permutation += removed

manifest = {
    'scope': 'Source-only A captured-report to frozen-report release review; no root review is claimed.',
    'old': {'path': rel(OLD), 'sha256': sha(old_bytes), 'bytes': len(old_bytes)},
    'new': {'path': rel(NEW), 'sha256': sha(new_bytes), 'bytes': len(new_bytes)},
    'codec': 'Every object stores its exact key order; every ordinary array stores length and numeric-index children. Only /differences uses its checked unique id as a logical child key, with the complete ordered id list stored. Scalars retain exact parsed JSON values and types. Frozen input JSON bytes equal UTF-8 json.dumps(ensure_ascii=False, indent=2) + LF; this exact serialization is checked in both directions.',
    'logical_path_convention': 'RFC6901 escaping; /differences/@ID logical children are identified by source id and mapped separately to exact old and new numeric JSON pointers.',
    'difference_permutation': permutation,
    'changed_node_count': len(ops),
    'pooled_distinct_nodes': len(pool),
    'novel_review_nodes': len({op['new_node'] for op in ops if op['new_node'] is not None}),
    'inserted_difference_ids': [p['id'] for p in permutation if p['old_index'] is None],
    'removed_difference_ids': [p['id'] for p in permutation if p['new_index'] is None],
    'unchanged_logical_node_count': len(set(old_flat) & set(new_flat)) - sum(1 for o in ops if o['old_node'] is not None and o['new_node'] is not None),
}
writejson('manifest_v01', manifest)
writejson('pool_v01', pool)
writejson('operations_v01', ops)

old_value_occurrences = {}
for path, node in old_flat.items():
    old_value_occurrences.setdefault(dumps(node), []).append(old_ptr[path])

review = []
for pooled in pool:
    used = [op for op in ops if op['new_node'] == pooled['id']]
    if not used:
        continue
    review.append({
        'value_id': pooled['id'],
        'exact_new_node': pooled['node'],
        'all_changed_or_added_occurrences': [{
            'operation': o['id'], 'logical_path': o['logical_path'],
            'old_json_pointer': o['old_json_pointer'], 'old_node': o['old_node'],
            'new_json_pointer': o['new_json_pointer'],
        } for o in used],
        'exact_same_node_preexisted_at_old_pointers': old_value_occurrences.get(dumps(pooled['node']), []),
    })

# Bound the human-facing files by bytes; no value or path list is shortened.
chunks, current, size = [], [], 0
for row in review:
    line = json.dumps(row, ensure_ascii=False) + '\n'
    width = len(line.encode('utf-8'))
    if current and size + width > 13500:
        chunks.append(current)
        current, size = [], 0
    current.append(line)
    size += width
if current:
    chunks.append(current)
chunk_files = []
for i, chunk in enumerate(chunks, 1):
    name = PREFIX + 'review_v01_%02d.jsonl' % i
    data = ''.join(chunk).encode('utf-8')
    (OUT / name).write_bytes(data)
    chunk_files.append({'path': 'out/checks/' + name, 'rows': len(chunk), 'bytes': len(data), 'sha256': sha(data)})

replay = {
    'source_only': True,
    'input_hashes_match_manifest': True,
    'old_json_order_and_serializer_roundtrip_exact': prettybytes(inflate(old_flat)) == old_bytes,
    'new_json_order_and_serializer_roundtrip_exact': prettybytes(inflate(new_flat)) == new_bytes,
    'forward_exact_bytes': prettybytes(inflate(forward)) == new_bytes,
    'inverse_exact_bytes': prettybytes(inflate(inverse)) == old_bytes,
    'forward_sha256': sha(prettybytes(inflate(forward))),
    'inverse_sha256': sha(prettybytes(inflate(inverse))),
    'all_changed_nodes_covered_once': len(ops) == len({o['logical_path'] for o in ops}),
    'all_new_pool_nodes_reviewed_once': len(review) == len({o['new_node'] for o in ops if o['new_node'] is not None}),
    'review_files': chunk_files,
    'no_images_opened_or_modified': True,
    'captured_and_reader_files_unmodified': OLD.read_bytes() == old_bytes and NEW.read_bytes() == new_bytes,
    'root_review_claimed': False,
}
writejson('replay_v01', replay)

note = [
    '# A report release: exact source delta\n',
    'This is a source-only comparison. It records no ink decision and claims no root review.\n',
    f"Old captured report: `{rel(OLD)}` (`{sha(old_bytes)}`).\n",
    f"Final frozen report: `{rel(NEW)}` (`{sha(new_bytes)}`).\n",
    f"The {len(old['differences'])} old difference ids all remain. Final difference row 31 is the new `A026-L13`; old indices 0–30 map to final indices 0–30, and old indices 31–62 map to final indices 32–63. The full 64-entry exact mapping is in the manifest.\n",
    f"There are {len(ops)} changed or added codec nodes and {len(review)} distinct final node values among those changes. Each distinct final value appears once in the review files, with all its exact old/new field paths and any old identical-value paths. Scalar values and container order/length metadata are both included.\n",
    'Read the following review files completely; no field value or occurrence list is abbreviated:\n',
]
for f in chunk_files:
    note.append(f"- `{f['path']}` — {f['rows']} distinct values, {f['bytes']} bytes.\n")
note += [
    '\nThe value pool and operations retain both sides. `scan026_source_A_release_build.py` supplies the finite forward and inverse maps. Replay recovered both original report byte strings exactly, including object key order, with the original hashes. This byte-level equality concerns these source files only.\n',
    '\nA parent inventory attribution and a nested candidate attribution remain separate source fields; this procedure never assigns one field’s scope to another.\n',
]
(OUT / (PREFIX + 'readme_v01.md')).write_text('\n'.join(note), encoding='utf-8')
print(json.dumps({'manifest': manifest, 'review_files': chunk_files, 'replay': replay}, ensure_ascii=False, indent=2))
