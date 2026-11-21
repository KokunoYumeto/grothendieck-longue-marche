"""Root source-only verification of the completely read C review stream."""
from pathlib import Path
import copy
import hashlib
import json
from datetime import datetime, timezone

BASE = Path('/workspace/scratch/94548b74fbe0')
CHECKS = BASE / 'out/checks'
sha = lambda b: hashlib.sha256(b).hexdigest()
dump = lambda v: json.dumps(v, ensure_ascii=False, separators=(',', ':'))
pretty = lambda v: (json.dumps(v, ensure_ascii=False, indent=2) + '\n').encode()
esc = lambda s: str(s).replace('~', '~0').replace('/', '~1')

def flatten(value, path='', pointer='', result=None, numeric=None):
    if result is None:
        result, numeric = {}, {}
    if isinstance(value, dict):
        node = {'kind': 'object', 'keys': list(value)}
        children = [(key, key, item) for key, item in value.items()]
    elif isinstance(value, list):
        if path == '/differences':
            ids = [item['id'] for item in value]
            assert len(ids) == len(set(ids))
            node = {'kind': 'id-list', 'ids': ids}
            children = [('@' + item['id'], index, item) for index, item in enumerate(value)]
        else:
            node = {'kind': 'array', 'length': len(value)}
            children = [(index, index, item) for index, item in enumerate(value)]
    else:
        node, children = {'kind': 'value', 'value': value}, []
    result[path] = node
    numeric[pointer] = node
    for logical_key, numeric_key, child in children:
        flatten(child, path + '/' + esc(logical_key), pointer + '/' + esc(numeric_key), result, numeric)
    return result, numeric

def inflate(nodes, path=''):
    node = nodes[path]
    kind = node['kind']
    if kind == 'object':
        return {key: inflate(nodes, path + '/' + esc(key)) for key in node['keys']}
    if kind == 'id-list':
        return [inflate(nodes, path + '/' + esc('@' + key)) for key in node['ids']]
    if kind == 'array':
        return [inflate(nodes, path + '/' + str(index)) for index in range(node['length'])]
    assert kind == 'value'
    return node['value']

manifest = json.loads((CHECKS / 'scan026_C_release_manifest_v01.json').read_bytes())
index = json.loads((CHECKS / 'scan026_C_release_review_index_v02.json').read_bytes())
for item in manifest['inputs']:
    data = (BASE / item['path']).read_bytes()
    assert len(data) == item['bytes'] and sha(data) == item['sha256']
old_bytes = (CHECKS / 'scan026_root_preread/C_report.json').read_bytes()
new_bytes = (BASE / 'out/readers/026/C/report.json').read_bytes()
old, old_numeric = flatten(json.loads(old_bytes))
new, new_numeric = flatten(json.loads(new_bytes))
assert pretty(inflate(old)) == old_bytes and pretty(inflate(new)) == new_bytes
records, suffixes, pool, operations = {}, {}, {}, []
for item in index['review_files']:
    data = (BASE / item['path']).read_bytes()
    assert sha(data) == item['sha256'] and len(data) == item['bytes']
    for line in data.splitlines():
        row = json.loads(line)
        if row[0] in ('R', 'S'):
            target = records if row[0] == 'R' else suffixes
            assert row[1] not in target
            target[row[1]] = row[2]
        elif row[0] in ('C', 'V'):
            assert row[1] not in pool
            pool[row[1]] = copy.deepcopy(old_numeric[row[2]] if row[0] == 'C' else row[2])
        else:
            assert row[0] == 'P'
            _, after, before, rr, ss = row
            operations.extend((records[r] + suffixes[s], before, after) for r in rr for s in ss)
assert len(operations) == len({path for path, _, _ in operations}) == 4510
for original, target, reverse in [(old, new_bytes, False), (new, old_bytes, True)]:
    result = copy.deepcopy(original)
    for path, before, after in operations:
        if reverse:
            before, after = after, before
        assert (path not in result) if before is None else dump(result[path]) == dump(pool[before])
        if after is None:
            del result[path]
        else:
            result[path] = copy.deepcopy(pool[after])
    assert pretty(inflate(result)) == target
out = {
    'at_utc': datetime.now(timezone.utc).isoformat(),
    'source_only': True,
    'all_six_input_hashes_and_lengths_verified': True,
    'all_ten_read_review_chunks_hashes_verified': True,
    'prefixes': len(records), 'suffixes': len(suffixes), 'pool_nodes': len(pool),
    'exact_unique_operations': len(operations),
    'forward_exact_bytes_sha256': sha(new_bytes),
    'inverse_exact_bytes_sha256': sha(old_bytes),
    'root_images_opened_by_this_script': 0,
}
(CHECKS / 'scan026_C_release_root_verification.json').write_bytes(pretty(out))
previous = 'out/checks/scan026_root_text_progress_v03.json'
bookmark = json.loads((BASE / previous).read_bytes())
bookmark['at_utc'] = out['at_utc']
bookmark['previous_record'] = previous
bookmark['C'].update({
    'final_return_and_release_delta_still_pending': False,
    'final_release_delta_pending': False,
    'complete_final_report_read': True,
    'captured_text_plus_full_final_text_diffs_read': True,
    'release_manifest_index_all_ten_review_chunks_both_diffs_and_replay_fully_read': True,
    'release_build_source_and_readme_fully_read': True,
    'root_exact_forward_inverse_verification': 'out/checks/scan026_C_release_root_verification.json',
    'release_review_files': index['review_files'],
})
bookmark['pending_before_first_root_image'] = ['physical-locus union review and root crop plan']
bookmark['first_image_gate_open'] = False
(CHECKS / 'scan026_root_text_progress_v04.json').write_bytes(pretty(bookmark))
print(json.dumps(out, indent=2))
