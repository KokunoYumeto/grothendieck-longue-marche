#!/usr/bin/env python3
"""Independent, source-only verification of the frozen scan026 record v02.

No release constructor is imported or executed. No image is opened. The sole
output is the sibling scan026_source_release_independent_v02.json proof.
Equality preserves JSON types, array order, object key order and exact strings.
"""
from pathlib import Path
from collections import Counter
from copy import deepcopy
import csv
import hashlib
import io
import json
import re

BASE = Path(__file__).resolve().parents[2]
CHECKS = BASE / 'out/checks'
OUT = CHECKS / 'scan026_source_release_independent_v02.json'
RECORD_PATH = 'out/checks/scan026_release_record_proposal_v02.json'
RECORD_SHA = '098043e22a7a7edb2e9e00280b472ac5f16a6f0858fa0fdcf362d8a463cf5668'
FINAL_SHA = '318b043580aba18b302169e52d7c3570208e8211cc7f32f8828cc070ee743615'
CONTRACT_SHA = '31635052f19c29904453133ad8c18c7607dcb39b9ddbdb4ff45c54905fc0bc5b'
cache = {}
json_cache = {}
checks = Counter()
failures = []
details = {}


def sha(b):
    return hashlib.sha256(b).hexdigest()


def packed(x):
    return json.dumps(x, ensure_ascii=False, separators=(',', ':')).encode('utf-8')


def eq(a, b):
    return packed(a) == packed(b)


def check(ok, category, label, extra=None):
    checks[category] += 1
    if not ok:
        row = {'category': category, 'label': label}
        if extra is not None:
            row['detail'] = extra
        failures.append(row)
    return ok


def same(a, b, category, label):
    return check(eq(a, b), category, label,
                 None if eq(a, b) else {'actual_ordered_sha256': sha(packed(a)),
                                       'expected_ordered_sha256': sha(packed(b))})


def path(p):
    q = Path(p)
    if q.is_absolute():
        return q
    if p.startswith('checks/'):
        return BASE / 'out' / q
    return BASE / q


def data(p):
    q = path(p)
    if q.suffix.lower() in {'.png', '.jpg', '.jpeg', '.tif', '.tiff', '.gif', '.pdf'}:
        raise RuntimeError('Forbidden nontext input: ' + str(q))
    key = str(q.relative_to(BASE))
    if key not in cache:
        cache[key] = q.read_bytes()
    return cache[key]


def doc(p):
    q = str(path(p).relative_to(BASE))
    if q not in json_cache:
        json_cache[q] = json.loads(data(q))
    return json_cache[q]


def cj(n):
    return doc('out/checks/' + n)


def pointer(obj, ptr):
    if ptr == '':
        return obj
    assert ptr.startswith('/'), ptr
    for token in ptr[1:].split('/'):
        token = token.replace('~1', '/').replace('~0', '~')
        obj = obj[int(token)] if isinstance(obj, list) else obj[token]
    return obj


def ref(r):
    return pointer(doc(r['path']), r['json_pointer'])


def walk(x, p=''):
    yield p, x
    if isinstance(x, dict):
        for k, v in x.items():
            yield from walk(v, p + '/' + k.replace('~', '~0').replace('/', '~1'))
    elif isinstance(x, list):
        for i, v in enumerate(x):
            yield from walk(v, p + '/' + str(i))


def span(s, label, category='literal_source_spans'):
    p = s.get('path', s.get('source_path'))
    b = data(p)
    t = b.decode('utf-8')
    a, z = s['char_start'], s['char_end']
    check(type(a) is int and type(z) is int and 0 <= a <= z <= len(t), category, label + ': char range')
    literal = t[a:z]
    for k in ('source_sha256', 'file_sha256', 'sha256'):
        if k in s:
            same(sha(b), s[k], category, label + ': ' + k)
    if 'literal' in s:
        same(literal, s['literal'], category, label + ': literal')
    for k in ('literal_sha256', 'body_sha256'):
        if k in s:
            same(sha(literal.encode()), s[k], category, label + ': ' + k)
    aa, zz = len(t[:a].encode()), len(t[:z].encode())
    if 'utf8_byte_start' in s:
        same(aa, s['utf8_byte_start'], category, label + ': byte start')
    if 'utf8_byte_end' in s:
        same(zz, s['utf8_byte_end'], category, label + ': byte end')
    same(b[aa:zz], literal.encode(), category, label + ': byte/character inverse')
    if 'line_start' in s:
        same(t.count('\n', 0, a) + 1, s['line_start'], category, label + ': line start')
    if 'line_end' in s:
        same(t.count('\n', 0, max(a, z - 1)) + 1, s['line_end'], category, label + ': line end')
    if 'line' in s:
        same(t.count('\n', 0, a) + 1, s['line'], category, label + ': source line')
    return literal


# bytes have no JSON representation; use direct equality for byte statements.
old_same = same
def same(a, b, category, label):
    if isinstance(a, bytes) or isinstance(b, bytes):
        return check(type(a) is type(b) and a == b, category, label,
                     None if a == b else {'actual_sha256': sha(a), 'expected_sha256': sha(b)})
    return old_same(a, b, category, label)


r = doc(RECORD_PATH)
same(sha(data(RECORD_PATH)), RECORD_SHA, 'frozen_inputs', 'record SHA256')
for f in r['provenance']['frozen_inputs']:
    same(sha(data(f['path'])), f['sha256'], 'frozen_inputs', f['path'] + ': hash')
    same(len(data(f['path'])), f['bytes'], 'frozen_inputs', f['path'] + ': bytes')

authority = cj('scan026_root_scalar_authority_v01.json')
projection = cj('scan026_release_scalar_authority_projection_v02.json')
correction = cj('scan026_release_S06_scope_correction_v01.json')
applied = deepcopy(authority)
for change in correction['scalar_changes']:
    same(pointer(applied, change['pointer']), change['before'], 'scalar_authority', change['pointer'] + ': before')
    parent, key = change['pointer'].rsplit('/', 1)
    pointer(applied, parent)[key] = deepcopy(change['after'])
same(applied['rows'], projection['rows'], 'scalar_authority', 'only the exact three S06 changes produce projection v02')
same(len(correction['scalar_changes']), 3, 'scalar_authority', 'three authorized S06 field changes')
same(ref(projection['root_authority_ref']), authority, 'scalar_authority', 'projection authority reference')

contract = cj('scan026_source_selected_contract_v01.json')
same(sha(data('out/checks/scan026_source_selected_contract_v01.json')), CONTRACT_SHA, 'selected_contract', 'contract frozen hash')
same(sha(data(r['selected_draft'])), FINAL_SHA, 'selected_contract', 'root final draft frozen hash')
same(data(r['selected_draft']), data('out/checks/scan026_source_sections01_27_proposal_v01.tex'),
     'selected_contract', 'staged/root draft byte identity')
same(ref(r['selected_source_contract']), contract, 'selected_contract', 'record contract reference')
co_loci = {z['locus_id']: z for z in contract['loci']}
decisions = {z['source_locus_id']: z for z in r['decisions']}
contract_order = [z['locus_id'] for z in contract['loci']]
record_to_contract = [contract_order.index(lid) for lid in decisions]
contract_to_record = [list(decisions).index(lid) for lid in contract_order]
same([contract_order[i] for i in record_to_contract], list(decisions), 'counts', 'exact contract-to-record locus permutation')
same([list(decisions)[i] for i in contract_to_record], contract_order, 'counts', 'exact record-to-contract inverse permutation')
same(len(set(decisions)), 91, 'counts', '91 unique contract loci')
details['locus_order_morphism'] = {'record_index_to_contract_index': record_to_contract,
                                  'contract_index_to_record_index': contract_to_record,
                                  'forward_and_inverse_equal': True}
counts = {'C': sum(z['diff_C'] for z in r['decisions']),
          'H': sum(z['diff_H'] for z in r['decisions']),
          'decision_loci': len(r['decisions']),
          'remaining_doubt_loci': sum(z['remaining_doubt'] for z in r['decisions']),
          'inventory_elements': len(r['inventory']), 'check_events': len(r['check_events'])}
same(counts, {'C': 70, 'H': 82, 'decision_loci': 91, 'remaining_doubt_loci': 66,
              'inventory_elements': 106, 'check_events': 0}, 'counts', 'requested exact counts')
same(counts, r['counts'], 'counts', 'declared counts equal actual records')
same(sum(z['marked_in_H'] == 'yes' for z in r['decisions']), 9, 'counts', 'marked H9')
same(len(r['doubts']), 66, 'counts', '66 actual doubt rows')
same(sum(k.startswith('S') for k in decisions), 39, 'counts', '39 local Sigma occurrences')
same([z['decision_id'] for z in r['doubts']], [z['id'] for z in r['decisions'] if z['remaining_doubt']],
     'counts', 'doubt row bijection')
same(len(r['C_source_rows']), 15, 'counts', '15 original C parent rows')
same(len(r['selected_graphical_groups']), 71, 'counts', '71 source groups')
same(len(r['source_locus_coverage']), 91, 'counts', '91 coverage objects')
details['counts'] = {**counts, 'marked_H': 9, 'Sigma_loci': 39}

# Decode every exact contract JSON reference directly from its frozen source.
jrefs = {}
for j in contract['reference_table']:
    p = j['path']; b = data(p); t = b.decode()
    a, z = j['raw_json_char_start'], j['raw_json_char_end']
    aa, zz = j['raw_json_utf8_start'], j['raw_json_utf8_end']
    name = j['reference_id']
    same(sha(b), j['file_sha256'], 'contract_json_refs', name + ': file hash')
    same(t[a:z].encode(), b[aa:zz], 'contract_json_refs', name + ': character/byte map')
    same(len(t[:a].encode()), aa, 'contract_json_refs', name + ': start')
    same(len(t[:z].encode()), zz, 'contract_json_refs', name + ': end')
    same(sha(b[aa:zz]), j['raw_json_sha256'], 'contract_json_refs', name + ': lexeme hash')
    v = pointer(doc(p), j['json_pointer'])
    same(json.loads(b[aa:zz]), v, 'contract_json_refs', name + ': exact pointer/lexeme inverse')
    same(sha(packed(v)), j['ordered_decoded_value_sha256'], 'contract_json_refs', name + ': ordered value hash')
    same(type(v).__name__, j['type'], 'contract_json_refs', name + ': type')
    if 'original_key_order' in j:
        same(list(v), j['original_key_order'], 'contract_json_refs', name + ': original key order')
    if 'array_length' in j:
        same(len(v), j['array_length'], 'contract_json_refs', name + ': array length')
    jrefs[name] = v
same(len(jrefs), 364, 'contract_json_refs', '364 unique references')


def model(lid, stack=()):
    assert lid not in stack, (lid, stack)
    b = co_loci[lid]['selected_state_binding']; k = b['kind']
    if k == 'exact_complete_candidate_array':
        x = {'kind': k, 'candidates': jrefs[b['array_ref']]}
    elif k == 'singleton_exact_object':
        x = {'kind': k, 'candidates': [jrefs[b['object_ref']]]}
    elif k == 'whole_object_permutation':
        original = jrefs[b['original_array_ref']]
        selected = [original[i] for i in b['new_index_to_old_index']]
        same([selected[i] for i in b['inverse_old_index_to_new_index']], original,
             'selected_models', lid + ': permutation inverse')
        x = {'kind': k, 'candidates': selected, 'exact_original_candidates': original,
             'new_index_to_old_index': b['new_index_to_old_index'],
             'inverse_old_index_to_new_index': b['inverse_old_index_to_new_index'],
             'root_scope': jrefs[b['root_scope_ref']]}
    elif k == 'exact_parent_component_projection':
        x = {'kind': k, 'component_values': [jrefs[j] for j in b['ordered_value_refs']],
             'root_scope': jrefs[b['shared_root_scope_ref']],
             'complete_parent_candidates': jrefs[b['parent_array_ref']],
             'explicit_parent_indices': b['explicit_parent_indices']}
        for component, parent_index, jid in zip(x['component_values'], x['explicit_parent_indices'], b['ordered_value_refs']):
            j = next(q for q in contract['reference_table'] if q['reference_id'] == jid)
            parent_j = next(q for q in contract['reference_table'] if q['reference_id'] == b['parent_array_ref'])
            prefix = parent_j['json_pointer'] + '/' + str(parent_index)
            check(j['path'] == parent_j['path'] and j['json_pointer'].startswith(prefix + '/'),
                  'selected_models', lid + ': explicit parent component reference ' + jid)
    elif k in ('fixed_parent_with_scoped_child_candidates', 'fixed_parent_text_with_scoped_child_candidates'):
        x = {'kind': k, 'root_scope': jrefs[b['root_scope_ref']],
             'children': [{'locus_id': child, 'complete_selected_scope': model(child, (*stack, lid))}
                          for child in b['child_loci']], 'scope_rule': b['scope_rule']}
        if 'original_A_parent_candidate_provenance_ref' in b:
            x['original_A_parent_candidate_provenance'] = jrefs[b['original_A_parent_candidate_provenance_ref']]
    else:
        raise RuntimeError('Undecoded model: ' + k)
    if 'candidate_count' in b:
        same(len(x.get('candidates', x.get('component_values', []))), b['candidate_count'],
             'selected_models', lid + ': complete state count')
    return x


def attachment(s):
    return {'path': r['selected_draft'], 'sha256': FINAL_SHA, 'manifest': 'root.final_draft.tex',
            'char_start': s['char_start'], 'char_end': s['char_end'],
            'utf8_byte_start': s['utf8_byte_start'], 'utf8_byte_end': s['utf8_byte_end'],
            'line_start': s['line_start'], 'line_end': s['line_end'],
            'body_sha256': s['literal_sha256'], 'scope': s['scope'],
            'original_staged_source_span': s}


consequence = cj('scan026_root_consequential_authority_v01.json')
witness = cj('scan026_release_witness_bindings_v02.json')
same(len(witness['rows']), 91, 'witness_bindings', '91 witness rows')
expected_models = {}
for i, (d, scalar, wit) in enumerate(zip(r['decisions'], projection['rows'], witness['rows'])):
    lid = d['source_locus_id']; name = '/decisions/' + str(i)
    locus = co_loci[lid]
    same(lid, locus['locus_id'], 'scalar_authority', lid + ': locus order')
    for k, v in scalar.items():
        same(d['root_final_exact'] if k == 'final' else d[k], v, 'scalar_authority', lid + ': ' + k)
    expected_models[lid] = m = model(lid)
    same(d['root_selected_state_model'], m, 'selected_models', lid + ': entire selected state model')
    same(d['selected_state_binding'], locus['selected_state_binding'], 'selected_models', lid + ': exact binding descriptor')
    same(d['selected_group_ids'], locus['selected_source_groups'], 'selected_models', lid + ': group IDs')
    final_prefix = d['root_final_exact'] + '\nComplete selected state objects, with original scopes and fields:\n'
    check(d['final'].startswith(final_prefix), 'selected_models', lid + ': root final prefix')
    same(d['final'][len(final_prefix):].encode(), packed(m), 'selected_models', lid + ': exact complete model suffix')
    same([json.loads(q) for q in d['alternatives']], m.get('candidates', [m]),
         'selected_models', lid + ': alternatives retain complete objects')
    same(d['source_attachments'], [attachment(s) for s in locus['selected_source_spans']],
         'selected_attachments', lid + ': identity source mapping')
    same(json.loads(d['qualification']), ref(d['provenance']['root_qualification_object_ref']),
         'root_evidence', lid + ': exact qualification object')
    same(d['evidence'], ref(d['provenance']['root_evidence_ref']), 'root_evidence', lid + ': complete root journal body')
    same(d['mathematical_consequence'], consequence['mathematical_consequence_by_locus'].get(
        lid, consequence['all_other_loci_mathematical_consequence']), 'root_evidence', lid + ': consequential authority')
    same(wit['locus_id'], lid, 'witness_bindings', lid + ': row order')
    same(d['witness_source_references'], wit['witnesses'], 'witness_bindings', lid + ': complete exact witnesses')
    for who in ('C', 'H'):
        same(d[who], [s['literal'] for s in wit['witnesses'][who]], 'witness_bindings', lid + ': ' + who + ' literal projection')
        same(d['witness_scope'][who], [s['scope'] for s in wit['witnesses'][who]], 'witness_bindings', lid + ': ' + who + ' scope projection')
        for j, s in enumerate(wit['witnesses'][who]):
            span(s, lid + ': witness ' + who + str(j), 'witness_bindings')
    for s in locus['selected_source_spans']:
        span(s, lid + ': frozen staged source', 'selected_attachments')
    for s in d['source_attachments']:
        span(s, lid + ': final source', 'selected_attachments')

# Complete group/coverage objects: exact inverse from final paths to staged refs.
for gid, original in contract['source_group_registry'].items():
    actual = next(z for z in r['selected_graphical_groups'] if z['group_id'] == gid)
    inverse = {k: v for k, v in actual.items() if k != 'original_contract_group_ref'}
    inverse['final_source'] = actual['final_source']['original_staged_source_span']
    same(inverse, original, 'group_and_locus_inverse', gid + ': original contract group recovered')
    same(ref(actual['original_contract_group_ref']), original, 'group_and_locus_inverse', gid + ': group pointer')
    same(actual['final_source'], attachment(original['final_source']), 'group_and_locus_inverse', gid + ': final attachment')
for original, actual in zip(contract['loci'], r['source_locus_coverage']):
    inverse = {k: v for k, v in actual.items() if k != 'original_contract_locus_ref'}
    inverse['selected_source_spans'] = [s['original_staged_source_span'] for s in actual['selected_source_spans']]
    same(inverse, original, 'group_and_locus_inverse', original['locus_id'] + ': contract locus recovered')
    same(ref(actual['original_contract_locus_ref']), original, 'group_and_locus_inverse', original['locus_id'] + ': locus pointer')

for q in r['doubts']:
    d = next(d for d in r['decisions'] if d['id'] == q['decision_id'])
    for k in ('location', 'alternatives', 'confidence', 'selected_group_ids', 'source_attachments',
              'root_crop_evidence', 'main_approved', 'selected_state_binding'):
        same(q[k], d[k], 'doubt_bijection', q['id'] + ': ' + k)
    same(q['reading'], d['final'], 'doubt_bijection', q['id'] + ': complete reading')
    same(q['reason'], d['qualification'], 'doubt_bijection', q['id'] + ': complete qualification')

# All 1,106 original objects, without replacing own reader candidates or flags.
registry = cj('scan026_source_union_sources_v01.json')
for key, f in registry.items():
    same(sha(data(f['path'])), f['sha256'], 'original_source_registry', key + ': hash')
    same(len(data(f['path'])), f['bytes'], 'original_source_registry', key + ': bytes')
pool = cj('scan026_source_union_state_pool_v01.json')
raw = cj('scan026_release_exact_raw_values_v01.json')
raw_by_id = {z['record_id']: z for z in raw['records']}
same(len(raw_by_id), 1106, 'raw_original_objects', '1106 unique raw objects')
for i, (p, target) in enumerate(zip(pool, raw['records'])):
    rr = p['raw_ref']; source = registry[rr['source']]
    original = pointer(doc(source['path']), rr['json_pointer'])
    value = {f['key']: (f['value'] if 'value' in f else pointer(doc(registry[f['exact_value_ref']['source']]['path']),
                         f['exact_value_ref']['json_pointer'])) for f in p['ordered_fields']} if 'ordered_fields' in p else p['value']
    same(value, original, 'raw_original_objects', p['record_id'] + ': pool exact decode')
    same(target['value'], original, 'raw_original_objects', p['record_id'] + ': release exact raw value')
    same(target['record_id'], p['record_id'], 'raw_original_objects', p['record_id'] + ': identity')
    expected = {'path': source['path'], 'source_sha256': source['sha256'], 'json_pointer': rr['json_pointer'],
                'ordered_value_sha256': sha(packed(original)), 'original_pool_pointer': '/' + str(i)}
    same(target['source'], expected, 'raw_original_objects', p['record_id'] + ': exact source binding')
    same(ref(target['source']), target['value'], 'raw_original_objects', p['record_id'] + ': inverse pointer')

raw_paths = cj('scan026_release_raw_path_mappings_v01.json')
for row in raw_paths['records']:
    value = raw_by_id[row['record_id']]['value']
    suffixes = [s for s, _ in walk(value)]
    same(row['suffixes'], suffixes, 'raw_node_maps', row['record_id'] + ': exhaustive ordered paths')
    same(sha(packed(value)), row['root_ordered_value_sha256'], 'raw_node_maps', row['record_id'] + ': value hash')
    for suffix in suffixes:
        same(pointer(doc(row['source_path']), row['source_pointer_prefix'] + suffix),
             pointer(doc(row['target_path']), row['target_pointer_prefix'] + suffix),
             'raw_node_maps', row['record_id'] + suffix)

original_coverage = {}
for who in 'ABC':
    report_path = registry[who + '.report']['path']; report = doc(report_path)
    original_coverage[who] = {}
    for field in ('differences', 'doubts', 'inventory'):
        expected = ['/' + field + '/' + str(i) for i in range(len(report[field]))]
        actual = [z['source']['json_pointer'] for z in raw['records'] if z['source']['path'] == report_path
                  and re.fullmatch('/' + field + r'/\d+', z['source']['json_pointer'])]
        same(actual, expected, 'reader_complete_array_coverage', who + ': ' + field)
        original_coverage[who][field] = len(expected)
details['original_reader_array_coverage'] = original_coverage

# Own TeX source spans and complete partition inverses for A, B and C.
source_spans = cj('scan026_release_exact_own_source_spans_v01.json')
spans_by_id = {z['span_id']: z for z in source_spans['spans']}
same(len(spans_by_id), 430, 'own_source_partitions', '430 exact source spans')
for s in source_spans['spans']:
    span(s['span'], s['span_id'], 'own_source_partitions')
for who in 'ABC':
    parts = source_spans['reader_source_partitions'][who]
    joined = []; cursor = 0
    for part in parts:
        q = spans_by_id[part['span_id']]['span']; original = ref(part['original_partition_ref'])
        same(q['char_start'], cursor, 'own_source_partitions', who + ': contiguous ' + part['span_id'])
        same(q['path'], registry[who + '.tex']['path'], 'own_source_partitions', who + ': source identity')
        for k in ('char_start', 'char_end', 'utf8_byte_start', 'utf8_byte_end', 'line_start', 'line_end'):
            same(q[k], original['exact_source'][k], 'own_source_partitions', who + ': original ' + k)
        same(part['containing_source_groups'], original['containing_source_groups'], 'own_source_partitions', who + ': group scopes')
        cursor = q['char_end']; joined.append(q['literal'])
    same(''.join(joined).encode(), data(registry[who + '.tex']['path']), 'own_source_partitions', who + ': complete byte inverse')

union = cj('scan026_source_union_v01.json')
union_by_id = {z['locus_id']: z for z in union}
projection_maps = cj('scan026_release_reader_projection_maps_v02.json')
excluded = set(projection_maps['exact_excluded_report_field_names'])
observed_projections = []
payloads = {}
raw_occurrences = []
role_map = [('complete_original_source_groups', 'source_group_records'),
            ('original_inventory_scopes', 'inventory_records'),
            ('original_complete_source_scope_records', 'other_state_records'),
            ('original_declared_crop_metadata', 'declared_crop_records')]
for i, d in enumerate(r['decisions']):
    lid = d['source_locus_id']
    for who in 'ABC':
        payload = json.loads(d['readers'][who]); payloads[(lid, who)] = payload
        same(payload['reader'], who, 'own_reader_payloads', lid + '/' + who + ': reader identity')
        own = union_by_id[lid]['reader_sources'][who] if lid in union_by_id else {
            'source_group_records': [], 'difference_records': [], 'doubt_records': [], 'inventory_records': [],
            'other_state_records': [], 'local_source_spans': [], 'declared_crop_records': []}
        for target_key, source_key in role_map:
            expected = [{'raw_record': rid, 'exact_original_fields': raw_by_id[rid]['value']} for rid in own[source_key]]
            same(payload[target_key], expected, 'own_reader_payloads', lid + '/' + who + ': ' + target_key)
        expected_report = []; expected_own = []
        for role in ('difference_records', 'doubt_records'):
            for rid in own[role]:
                v = raw_by_id[rid]['value']
                own_fields = {k: x for k, x in v.items() if k not in excluded}
                expected_report.append({'raw_record': rid, 'original_role': role, 'exact_original_fields': v})
                expected_own.append({'raw_record': rid, 'original_role': role, 'own_fields': own_fields})
                observed_projections.append((lid, who, rid, v, own_fields))
        same(payload['original_report_and_doubt_records'], expected_report, 'own_reader_payloads', lid + '/' + who + ': full report objects')
        same(payload['own_report_and_doubt_fields'], expected_own, 'own_reader_payloads', lid + '/' + who + ': exact field projection')
        same(len(payload['exact_local_source']), len(own['local_source_spans']), 'own_reader_payloads', lid + '/' + who + ': local span count')
        for selected, original in zip(payload['exact_local_source'], own['local_source_spans']):
            s = spans_by_id[selected['span_id']]['span']
            original_literal = data(registry[original['source']]['path']).decode()[original['start_char']:original['end_char_exclusive']]
            if 'literal' in original:
                same(original['literal'], original_literal, 'own_reader_payloads', lid + '/' + who + ': original inline source literal')
            same(sha(original_literal.encode()), original['sha256'], 'own_reader_payloads', lid + '/' + who + ': original local source hash')
            same(selected['literal'], original_literal, 'own_reader_payloads', lid + '/' + who + ': exact local literal')
            same(s['literal'], original_literal, 'own_reader_payloads', lid + '/' + who + ': span-pool literal')
            same(s['char_start'], original['start_char'], 'own_reader_payloads', lid + '/' + who + ': local start')
            same(s['char_end'], original['end_char_exclusive'], 'own_reader_payloads', lid + '/' + who + ': local end')
            same(s['path'], registry[original['source']]['path'], 'own_reader_payloads', lid + '/' + who + ': local source')
        same(payload['complete_own_source_partition'], {'path': 'out/checks/scan026_source_state_catalog_v01.json',
             'json_pointer': '/complete_source_partitions/' + who}, 'own_reader_payloads', lid + '/' + who + ': entire own source partition binding')
        for field in ('complete_original_source_groups', 'original_report_and_doubt_records', 'original_inventory_scopes',
                      'original_complete_source_scope_records', 'original_declared_crop_metadata'):
            for j, value in enumerate(payload[field]):
                raw_occurrences.append((value['raw_record'], '/decisions/' + str(i) + '/readers/' + who,
                                        '/' + field + '/' + str(j) + '/exact_original_fields', value['exact_original_fields']))

same(len(observed_projections), 461, 'reader_projection_inverse', '461 field projection occurrences')
for observed, saved in zip(observed_projections, projection_maps['rows']):
    lid, who, rid, original, own_fields = observed
    same((lid, who, rid), (saved['locus_id'], saved['reader'], saved['raw_record']), 'reader_projection_inverse', rid + ': exact occurrence')
    same(list(original), saved['original_key_order'], 'reader_projection_inverse', rid + ': original order')
    same(list(own_fields), saved['retained_keys'], 'reader_projection_inverse', rid + ': retained keys')
    removed = {k: v for k, v in original.items() if k in excluded}
    same(list(removed), saved['excluded_keys'], 'reader_projection_inverse', rid + ': excluded keys')
    rejoined = {k: own_fields[k] if k in own_fields else removed[k] for k in saved['original_key_order']}
    same(rejoined, original, 'reader_projection_inverse', rid + ': finite field inverse')
    same(ref(saved['exact_source_ref']), original, 'reader_projection_inverse', rid + ': original pointer')

inverse_maps = cj('scan026_release_raw_object_inverse_mappings_v02.json')
same(len(raw_occurrences), 1333, 'original_object_lexeme_inverse', '1333 exact raw object occurrences')
occurrence_map = {(rid, rp, dp): value for rid, rp, dp, value in raw_occurrences}
same(len(occurrence_map), 1333, 'original_object_lexeme_inverse', '1333 distinct occurrence pointers')
for rid, record_ptr, decoded_ptr, value in raw_occurrences:
    same(value, raw_by_id[rid]['value'], 'original_object_lexeme_inverse', rid + ': complete source-pool inverse for ' + record_ptr + decoded_ptr)
same(len(inverse_maps['raw_objects']), 1066, 'original_object_lexeme_inverse', '1066 explicit source lexeme maps')
for mapping in inverse_maps['raw_objects']:
    rid, record_ptr, decoded_ptr = mapping['record_id'], mapping['record_string_pointer'], mapping['decoded_string_pointer']
    value = occurrence_map[(rid, record_ptr, decoded_ptr)]
    same(pointer(json.loads(pointer(r, record_ptr)), decoded_ptr), value,
         'original_object_lexeme_inverse', rid + ': exact record occurrence pointer')
    original = data(mapping['original_source_path'])
    lexeme = original[mapping['original_utf8_byte_start']:mapping['original_utf8_byte_end']]
    same(sha(lexeme), mapping['original_lexeme_sha256'], 'original_object_lexeme_inverse', rid + ': lexeme hash')
    same(json.loads(lexeme), value, 'original_object_lexeme_inverse', rid + ': source lexeme inverse')
    same(pointer(doc(mapping['original_source_path']), mapping['original_json_pointer']), value,
         'original_object_lexeme_inverse', rid + ': original pointer inverse')
for f in inverse_maps['full_original_file_partitions']:
    b = data(f['path']); cursor = 0; chunks = []
    for part in f['parts']:
        a, z = part['source_utf8_span']
        same(a, cursor, 'original_file_partitions', f['path'] + ': contiguous source fragment')
        chunk = b[a:z]
        if part['kind'] == 'exact_original_value_lexeme':
            v = raw_by_id[part['record_id']]['value']
            same(json.loads(chunk), v, 'original_file_partitions', part['record_id'] + ': exact source object')
            same(sha(chunk), part['original_value_sha256'], 'original_file_partitions', part['record_id'] + ': raw source lexeme hash')
        else:
            same(part['kind'], 'frozen_literal_complement', 'original_file_partitions', f['path'] + ': literal complement type')
        chunks.append(chunk); cursor = z
    same(cursor, len(b), 'original_file_partitions', f['path'] + ': complete end')
    same(b''.join(chunks), b, 'original_file_partitions', f['path'] + ': byte inverse with frozen literal complements')

# Original C parent rows, canonical part order, recurrence maps and exact scopes.
scaffold = cj('scan026_source_record_scaffold_v01.json')
c_binding = cj('scan026_source_union_C_rows_v01.json')
c_outcomes = cj('scan026_release_C_row_outcomes_v01.json')
for i, (actual, original, binding, outcome) in enumerate(zip(r['C_source_rows'], scaffold['C_source_rows'], c_binding, c_outcomes['rows'])):
    sid = actual['source_id']
    canonical = raw_by_id[binding['canonical_record']]['value']
    for k, v in original.items():
        if k not in ('source_parts', 'selected_outcome', 'decision_ids'):
            same(actual[k], v, 'C_original_rows', sid + ': original ' + k)
    same(actual['original_source_parts'], canonical['source_parts'], 'C_original_rows', sid + ': complete original canonical parts')
    same(actual['source_bindings'], binding, 'C_original_rows', sid + ': complete own-reader binding map')
    same(actual['selected_outcome'], authority['all_C_parent_outcomes'][sid], 'C_original_rows', sid + ': root outcome')
    same(ref(actual['root_outcome_mapping_ref']), outcome, 'C_original_rows', sid + ': outcome pointer')
    span(actual, sid, 'C_original_rows')
    for k in ('source_path', 'line', 'char_start', 'char_end', 'utf8_byte_start', 'utf8_byte_end', 'literal', 'source_id'):
        same(actual[k], canonical[k], 'C_original_rows', sid + ': canonical ' + k)
    same(len(actual['source_parts']), len(original['source_parts']), 'C_original_rows', sid + ': original part count')
    for j, (part, old) in enumerate(zip(actual['source_parts'], canonical['source_parts'])):
        same({k: part[k] for k in old}, old, 'C_original_rows', part['part_id'] + ': original part fields')
        same(part['original_decision_status'], old['decision_status'], 'C_original_rows', part['part_id'] + ': original status preserved')
        same(part['selected_outcome'], ref(part['root_authority']), 'C_original_rows', part['part_id'] + ': selected outcome authority')
        for attachment_value in part['source_attachments']:
            check(any(eq(attachment_value, s) for did in part['decision_ids'] for s in
                      next(q for q in r['decisions'] if q['id'] == did)['source_attachments']),
                  'C_original_rows', part['part_id'] + ': selected source attachment association')
    same(actual['decision_ids'], ['SOURCE026-' + x for x in binding['loci']], 'C_original_rows', sid + ': locus association order')
same([q['locus'] for q in c_binding[1]['four_local_part_correspondences']], ['S04', 'S05', 'S05', 'S07'], 'C_compound_scopes', 'R02 canonical four physical bindings')
same([q['A_part_index'] for q in c_binding[1]['four_local_part_correspondences']], [0, 2, 1, 3], 'C_compound_scopes', 'R02 exact A part permutation')
same([q['B_part_index'] for q in c_binding[1]['four_local_part_correspondences']], [0, 2, 1, 3], 'C_compound_scopes', 'R02 exact B part permutation')
same([q['C_part_index'] for q in c_binding[1]['four_local_part_correspondences']], [0, 1, 2, 3], 'C_compound_scopes', 'R02 exact C part permutation')
same(len(r['C_source_rows'][14]['original_source_parts']), 1, 'C_compound_scopes', 'R15 one original source part')
same([q['locus'] for q in c_binding[14]['eight_local_recurrences']], ['S05', 'S08', 'S09', 'S10', 'S11', 'S12', 'S13', 'S14'],
     'C_compound_scopes', 'R15 eight exact local recurrences')

# All 262 original inventory identities and wider paragraph/display containers.
inventory_bindings = cj('scan026_release_inventory_bindings_v01.json')
same(r['original_reader_inventory_bindings'], inventory_bindings, 'inventory_original_bindings', 'complete embedded inventory bindings')
ib = inventory_bindings['reader_inventory_bindings']
same(len(ib), 262, 'inventory_original_bindings', '262 raw inventory references')
same(len({(q['reader'], q['raw_inventory_ref']['json_pointer']) for q in ib}), 262, 'inventory_original_bindings', '262 distinct original identities')
for q in ib:
    value = ref(q['raw_inventory_ref'])
    same(value, raw_by_id[q['raw_record']]['value'], 'inventory_original_bindings', q['raw_record'] + ': exact raw reader object')
    same(sha(packed(value)), q['raw_inventory_ref']['ordered_value_sha256'], 'inventory_original_bindings', q['raw_record'] + ': ordered original hash')
    same(pointer(union, q['original_union_inventory_pointer']), q['raw_record'], 'inventory_original_bindings', q['raw_record'] + ': union binding')
    for broad in q['broad_scope_context_refs']:
        check(isinstance(ref(broad), dict), 'inventory_original_bindings', q['raw_record'] + ': original wider context reference resolves')
    for hp in q['raw_hand_field_paths']:
        check(pointer(value, hp) is not None, 'inventory_original_bindings', q['raw_record'] + ': original hand field ' + hp)
same(Counter(q['reader'] for q in ib), Counter({'A': 79, 'B': 95, 'C': 88}), 'inventory_original_bindings', '79/95/88 original inventory split')

context = cj('scan026_source_context_inventory_v01.json')
same(r['complete_selected_source_contexts'], context, 'context_inventory', 'entire exact context supplement')
same(len(context['contexts']), 15, 'context_inventory', '15 exact context containers')
cursor = 0; joins = []
for q in context['complete_source_partition']:
    s = q['source']; same(s['char_start'], cursor, 'context_inventory', q['context_id'] + ': contiguous selected source')
    joins.append(span(s, q['context_id'], 'context_inventory')); cursor = s['char_end']
same(len(joins), 8, 'context_inventory', 'eight complete source partition segments')
same(''.join(joins).encode(), data(r['selected_draft']), 'context_inventory', 'complete selected-source byte inverse')
for i, c in enumerate(context['contexts']):
    public = r['inventory'][91+i]
    same(public['element'], '026.CONTEXT.' + c['context_id'], 'context_inventory', c['context_id'] + ': public identity')
    same(public['source_attachments'], [attachment(c['selected_source'])], 'context_inventory', c['context_id'] + ': exact complete source span')
    same(public['original_inventory_refs'], c['original_inventory_refs'], 'context_inventory', c['context_id'] + ': original wider reader scopes')
    same(ref(public['provenance']['context_supplement_ref']), c, 'context_inventory', c['context_id'] + ': exact source pointer')
    for v in public['original_inventory_hand_scope_map']['assignments']:
        same(public['original_inventory_hand_scope_map']['values'][v['value_index']],
             pointer(raw_by_id[v['raw_record']]['value'], v['field_pointer']),
             'inventory_hand_source_maps', c['context_id'] + ': exact own-reader hand assignment')
    for v in public['selected_child_hand_scope_refs']:
        target = pointer(r, v['record_inventory_pointer'])
        di = list(decisions).index(v['locus_id'])
        same(target, r['inventory'][di]['selected_hand_scope_map'], 'inventory_hand_source_maps', c['context_id'] + ': child scope pointer')

inventory_review = cj('scan026_release_inventory_review_v02.json')
inventory_review_by_id = {q['locus_id']: q for q in inventory_review['rows'] if 'locus_id' in q}
for i, d in enumerate(r['decisions']):
    public = r['inventory'][i]; lid = d['source_locus_id']; hs = public['selected_hand_scope_map']
    same(public['element'], '026.S.' + lid, 'inventory_selected_loci', lid + ': public identity')
    same(public['decision_ids'], [d['id']], 'inventory_selected_loci', lid + ': decision identity')
    same(public['source_attachments'], d['source_attachments'], 'inventory_selected_loci', lid + ': exact selected source spans')
    same(public['selected_group_ids'], d['selected_group_ids'], 'inventory_selected_loci', lid + ': exact group IDs')
    same(public['first_words_or_objects'], d['root_final_exact'], 'inventory_selected_loci', lid + ': exact root reading')
    same(public['kind'], inventory_review_by_id[lid]['kind_proposal'], 'inventory_selected_loci', lid + ': exact v02 inventory kind proposal')
    same(ref(inventory_review_by_id[lid]['source_contract_ref']), co_loci[lid], 'inventory_selected_loci', lid + ': exact kind-review contract scope')
    same(json.loads(public['hand']), {'exact_hand_field_values': hs['values']}, 'inventory_hand_source_maps', lid + ': v02 public hand value projection')
    for v in hs['assignments']:
        source = json.loads(d['qualification']) if v['source_scope'] == 'root_decision' else d[v['source_scope']]
        same(hs['values'][v['value_index']], pointer(source, v['pointer']), 'inventory_hand_source_maps', lid + ': exact scoped hand assignment')

for q in context['all262_raw_inventory_pointer_bindings']:
    original = doc('out/readers/026/' + q['reader'] + '/report.json')['inventory'][q['inventory_index']]
    same(original, raw_by_id[q['pool_record_id']]['value'], 'context_inventory', q['pool_record_id'] + ': context complete original inventory binding')
    same(original['element'], q['raw_element_identity'], 'context_inventory', q['pool_record_id'] + ': original element ID')

# Root notes, abbreviation strings and local complete source attachments.
notes = cj('scan026_root_notes_abbreviation_authority_v01.json')
same(r['notes'], notes['notes'], 'notes_abbreviations', 'exact root notes')
same(r['check_events'], notes['check_events'], 'notes_abbreviations', 'exact empty check events')
for k in ('attributed_content_note', 'root_selected_content_note'):
    same(r[k]['text'], notes['notes'], 'notes_abbreviations', k + ': exact notes')
    same(ref(r[k]['root_authority']), notes['notes'], 'notes_abbreviations', k + ': exact authority pointer')
same(len(r['abbreviations']), 5, 'notes_abbreviations', 'five root abbreviation objects')
for i, (a, original) in enumerate(zip(r['abbreviations'], notes['abbreviations'])):
    same({k: a[k] for k in original}, original, 'notes_abbreviations', str(i) + ': all exact original fields')
    same(ref(a['root_authority']), original, 'notes_abbreviations', str(i) + ': authority pointer')
    for j, s in enumerate(a['source_attachments']):
        span(s, 'abbreviation ' + str(i) + '/' + str(j), 'notes_abbreviations')

# The S scope remains indirect in v02; record the exact reachability and gap.
s_scope = cj('scan026_S_scope.json')
same(scaffold['S_source_only_context'], s_scope, 'S_scope_indirect_chain', 'scaffold complete S scope identity')
same(sha(data(s_scope['source'])), s_scope['source_sha256'], 'S_scope_indirect_chain', 'complete original S TSV hash')
s_rows = list(csv.DictReader(io.StringIO(data(s_scope['source']).decode()), delimiter='\t'))
same(len(s_rows), 7, 'S_scope_indirect_chain', 'seven complete original S rows')
same(s_scope['row_scopes'], [{k: z[k] for k in ('id', 'where', 'kind')} for z in s_rows],
     'S_scope_indirect_chain', 'seven exact source-only id/where/kind projections')
same(s_scope['direct_page_26_reading_rows'], [], 'S_scope_indirect_chain', 'root direct-page scope unchanged')
check('S_source_only_context' not in r, 'S_scope_indirect_chain', 'v02 has no explicit S scope field')
same([z for z in r['provenance']['frozen_inputs'] if z['path'] == 'out/checks/scan026_source_record_scaffold_v01.json'][0]['sha256'],
     sha(data('out/checks/scan026_source_record_scaffold_v01.json')), 'S_scope_indirect_chain', 'record-to-frozen-scaffold hash edge')

# Validate every embedded selected/witness span again by its own declared path.
embedded_span_occurrences = 0
embedded_reference_occurrences = 0
for ptr, node in walk(r):
    if not isinstance(node, dict):
        continue
    if 'path' in node and 'char_start' in node and 'char_end' in node:
        span(node, ptr, 'all_record_span_occurrences'); embedded_span_occurrences += 1
    if 'path' in node and 'json_pointer' in node:
        try:
            ref(node)
            check(True, 'all_record_json_pointer_occurrences', ptr)
        except (KeyError, IndexError, ValueError, FileNotFoundError) as e:
            check(False, 'all_record_json_pointer_occurrences', ptr, type(e).__name__ + ': ' + str(e))
        embedded_reference_occurrences += 1

# Limited v02 presentation findings already escalated; no correction is applied.
first_offsets = [min(s['char_start'] for s in q['source_attachments']) for q in r['inventory']]
adjacent_descents = [{'left_index': i, 'left_element': r['inventory'][i]['element'], 'left_start': a,
                     'right_index': i+1, 'right_element': r['inventory'][i+1]['element'], 'right_start': b}
                    for i, (a, b) in enumerate(zip(first_offsets, first_offsets[1:])) if b < a]
details['limited_v02_findings'] = [
    {'id': 'S_EXPLICIT_ATTACHMENT', 'record_pointer': '',
     'fact': 'No explicit S_source_only_context or complete seven-row S attachment occurs in v02. The exact seven-row scope is reachable through the frozen scaffold and registry; the complete original TSV remains hash-bound there.',
     'indirect_scope_path': 'out/checks/scan026_source_record_scaffold_v01.json',
     'indirect_scope_pointer': '/S_source_only_context', 'original_row_ids': [x['id'] for x in s_rows]},
    {'id': 'PUBLIC_HAND_FIELD_PROJECTION',
     'fact': 'The v02 inventory hand string carries pooled values. Exact assignments remain in selected_hand_scope_map or original_inventory_hand_scope_map; every supplied assignment was resolved against its exact source object.',
     'locus_inventory_rows': 91, 'context_inventory_rows': 15},
    {'id': 'PUBLIC_INVENTORY_ORDER',
     'fact': 'v02 orders 91 locus rows followed by 15 context rows; the following adjacent pairs decrease in their first selected-source character offset.',
     'adjacent_descents': adjacent_descents},
    {'id': 'S08_V02_KIND', 'record_pointer': '/inventory/' + str(list(decisions).index('S08')) + '/kind',
     'exact_v02_value': r['inventory'][list(decisions).index('S08')]['kind'], 'fixed_parent_locus': 'L011',
     'parent_exact_v02_value': r['inventory'][list(decisions).index('L011')]['kind'],
     'fact': 'These values exactly match the v02 inventory review proposal. Root has separately requested the successor presentation correction; this verifier applies none.'}
]
details['scope'] = {'image_access': 0, 'ink_decisions': 0, 'new_classifications': 0,
                    'constructor_imported_or_executed': False,
                    'exact_json_equality': 'UTF-8 json.dumps ensure_ascii=False, separators=(comma,colon), no sorted keys; JSON types, strings, array order and object key order are preserved.',
                    'byte_inverse_scope': 'Raw original-file complements are read from hash-bound frozen originals; this proof does not claim the public record alone embeds every original formatting byte.'}
details['C_scope_closure'] = {'parents': 15, 'R02_parts': 4, 'R02_A_B_new_to_old_part_indices': [0, 2, 1, 3],
                              'R02_C_part_indices': [0, 1, 2, 3], 'R15_original_parts': 1,
                              'R15_local_recurrences': ['S05', 'S08', 'S09', 'S10', 'S11', 'S12', 'S13', 'S14']}
details['references_checked'] = {'contract_json_refs': len(jrefs),
                                 'contract_locus_source_spans': sum(len(z['selected_source_spans']) for z in contract['loci']),
                                 'embedded_record_span_occurrences': embedded_span_occurrences,
                                 'embedded_record_json_pointer_occurrences': embedded_reference_occurrences,
                                 'raw_original_values': len(raw_by_id), 'raw_object_occurrences_in_reader_payloads': len(raw_occurrences),
                                 'own_reader_source_spans': len(spans_by_id), 'reader_field_projection_occurrences': len(observed_projections),
                                 'original_full_JSON_file_partitions': len(inverse_maps['full_original_file_partitions']),
                                 'original_inventory_references': len(ib), 'complete_contexts': len(context['contexts'])}

# Independently ensure every read input is unchanged before writing the proof.
for p, original in list(cache.items()):
    same((BASE / p).read_bytes(), original, 'inputs_unchanged', p)
proof = {'schema': 'scan026-independent-release-verification-v02', 'author': '/root/source026',
         'record': {'path': RECORD_PATH, 'sha256': RECORD_SHA, 'bytes': len(data(RECORD_PATH))},
         'verification_completed': True, 'all_executed_exact_checks_passed': not failures,
         'record_approval': False, 'successor_changes_applied': False,
         'checks_by_category': dict(checks), 'failure_count': len(failures), 'failures': failures,
         **details,
         'inputs': [{'path': p, 'sha256': sha(b), 'bytes': len(b)} for p, b in cache.items()]}
OUT.write_text(json.dumps(proof, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'proof': str(OUT.relative_to(BASE)), 'sha256': sha(OUT.read_bytes()),
                  'checks': sum(checks.values()), 'failure_count': len(failures),
                  'failures_first_20': failures[:20]}, ensure_ascii=False))
