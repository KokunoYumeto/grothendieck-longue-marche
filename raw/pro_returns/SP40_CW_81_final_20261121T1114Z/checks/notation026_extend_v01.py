#!/usr/bin/env python3
"""Exact scan026 notation supplement from frozen source objects; no ink decisions."""
from pathlib import Path
from datetime import datetime, timezone
import collections, copy, hashlib, json, re

ROOT = Path('/workspace/scratch/94548b74fbe0')
OUT = ROOT / 'out/checks'
CONTRACT = 'out/checks/scan026_source_selected_contract_v01.json'
BASE = 'out/checks/notation_audit_through025_preparation.json'
AUTHORITY = 'out/checks/notation026_root_authority_index_v01.json'
CACHE = {}

def sha(value):
    return hashlib.sha256(value.encode('utf-8') if isinstance(value, str) else value).hexdigest()

def pack(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'))

def load(path):
    if path not in CACHE:
        raw = (ROOT / path).read_bytes()
        CACHE[path] = {'raw': raw, 'text': raw.decode('utf-8'), 'sha256': sha(raw)}
    return CACHE[path]

def document(path):
    return json.loads(load(path)['text'])

def get(value, pointer):
    for token in pointer.split('/')[1:] if pointer else []:
        token = token.replace('~1', '/').replace('~0', '~')
        value = value[int(token)] if isinstance(value, list) else value[token]
    return value

def esc(value):
    return str(value).replace('~', '~0').replace('/', '~1')

def descriptor(path):
    d = load(path)
    return {'path': path, 'bytes': len(d['raw']), 'sha256_utf8': d['sha256']}

def write(name, value):
    raw = (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
    path = OUT / name
    with path.open('xb') as handle:
        handle.write(raw)
    return {'path': str(path.relative_to(ROOT)), 'bytes': len(raw), 'sha256_utf8': sha(raw)}

def leaves(value, pointer=''):
    if isinstance(value, dict):
        for key, child in value.items():
            yield from leaves(child, pointer + '/' + esc(key))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from leaves(child, pointer + '/' + str(index))
    else:
        yield pointer, value

def first_byte_difference(a, b):
    a, b = pack(a).encode('utf-8'), pack(b).encode('utf-8')
    return next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)) if len(a) != len(b) else None)

def projection(template, value, pointer=''):
    """Return exact template-shaped projection plus a full inverse sidecar."""
    assert type(template) is type(value), (pointer, type(template), type(value))
    if isinstance(template, dict):
        assert all(k in value for k in template), pointer
        projected = {}
        omitted = []
        for key in template:
            child, extra = projection(template[key], value[key], pointer + '/' + esc(key))
            projected[key] = child
            omitted.extend(extra)
        omitted.append({'pointer': pointer, 'original_key_order': list(value),
                        'omitted_members_in_original_order': [[k, value[k]] for k in value if k not in template]})
        return projected, omitted
    if isinstance(template, list):
        assert len(template) == len(value), pointer
        projected, omitted = [], []
        for i, (a, b) in enumerate(zip(template, value)):
            child, extra = projection(a, b, pointer + '/' + str(i))
            projected.append(child)
            omitted.extend(extra)
        return projected, omitted
    assert type(template) is type(value) and template == value, (pointer, template, value)
    return value, []

def invert_projection(projected, sidecar):
    result = copy.deepcopy(projected)
    for row in sidecar:
        obj = get(result, row['pointer'])
        obj.update(copy.deepcopy(dict(row['omitted_members_in_original_order'])))
        ordered = {k: obj[k] for k in row['original_key_order']}
        obj.clear()
        obj.update(ordered)
    return result

contract = document(CONTRACT)
base = document(BASE)
authority = document(AUTHORITY)
assert load(CONTRACT)['sha256'] == '31635052f19c29904453133ad8c18c7607dcb39b9ddbdb4ff45c54905fc0bc5b'
assert load(BASE)['sha256'] == 'a410950b40eb25df5be17cb40e05e1fde1c8a28f33f583edff3f49e3aebf60b7'
assert len(base['exact_notation_rows']) == 180 and len(base['recurring_form_families']) == 14
tex_path = contract['final_staged_source']['path']
tex = load(tex_path)['text']
assert load(tex_path)['sha256'] == '318b043580aba18b302169e52d7c3570208e8211cc7f32f8828cc070ee743615'
refs = {r['reference_id']: r for r in contract['reference_table']}
values = {}
for rid, ref in refs.items():
    data = load(ref['path'])
    assert data['sha256'] == ref['file_sha256'], rid
    raw = data['text'][ref['raw_json_char_start']:ref['raw_json_char_end']]
    assert raw.encode('utf-8') == data['raw'][ref['raw_json_utf8_start']:ref['raw_json_utf8_end']], rid
    assert sha(raw) == ref['raw_json_sha256'], rid
    value = get(document(ref['path']), ref['json_pointer'])
    assert pack(json.loads(raw)) == pack(value), rid
    assert sha(pack(value)) == ref['ordered_decoded_value_sha256'], rid
    values[rid] = value

authority_loci = {x['locus_id']: (i, x) for i, x in enumerate(authority['loci'])}
rows, own_comment_checks, deferred_comment_checks = [], [], []
used_refs = set()
for index, original in enumerate(contract['loci']):
    locus = original['locus_id']
    binding = original['selected_state_binding']
    kind = binding['kind']
    if kind == 'exact_complete_candidate_array':
        selected = copy.deepcopy(values[binding['array_ref']])
    elif kind == 'singleton_exact_object':
        selected = copy.deepcopy(values[binding['object_ref']])
    elif kind == 'whole_object_permutation':
        source = values[binding['original_array_ref']]
        selected = [copy.deepcopy(source[i]) for i in binding['new_index_to_old_index']]
        assert pack([selected[i] for i in binding['inverse_old_index_to_new_index']]) == pack(source)
    elif kind == 'exact_parent_component_projection':
        selected = [copy.deepcopy(values[rid]) for rid in binding['ordered_value_refs']]
        parent = values[binding['parent_array_ref']]
        field = 'cancelled_upper_label' if locus == 'L016' else 'relation_state'
        assert pack(selected) == pack([parent[i][field] for i in binding['explicit_parent_indices']])
    else:
        assert kind in ['fixed_parent_with_scoped_child_candidates', 'fixed_parent_text_with_scoped_child_candidates']
        selected = copy.deepcopy(values[binding['root_scope_ref']])
    ai, al = authority_loci[locus]
    for span in original['selected_source_spans']:
        literal = tex[span['char_start']:span['char_end']]
        assert sha(literal) == span['literal_sha256']
        assert literal.encode('utf-8') == load(tex_path)['raw'][span['utf8_byte_start']:span['utf8_byte_end']]
    root_sections = list(dict.fromkeys(x['root_section'] for x in al['root_authorities']))
    local_refs = []
    for pointer, value in leaves(binding):
        if isinstance(value, str) and value in refs:
            local_refs.append(value)
            used_refs.add(value)
    used_refs.add(original['root_decision_ref'])
    row = {'id': 'N026-' + locus, 'locus_id': locus,
           'source_contract_row_pointer': '/loci/' + str(index),
           'source_contract_row_ordered_sha256': sha(pack(original)),
           'root_sections_exact': root_sections,
           'root_authority_index_pointer': '/loci/' + str(ai),
           'root_decision_ref': original['root_decision_ref'],
           'location_exact': original['location'],
           'selected_state_binding_exact': copy.deepcopy(binding),
           'selected_value_exact': selected,
           'selected_source_spans_exact': copy.deepcopy(original['selected_source_spans']),
           'selected_source_groups_exact': copy.deepcopy(original['selected_source_groups']),
           'parent_locus_scopes_exact': copy.deepcopy(original['parent_locus_scopes']),
           'binding_reference_ids_in_descriptor_order': local_refs}
    rows.append(row)
    if kind != 'exact_complete_candidate_array':
        continue
    checked = False
    for gid in original['selected_source_groups']:
        span = contract['source_group_registry'][gid]['final_source']
        literal = tex[span['char_start']:span['char_end']]
        assert sha(literal) == span['literal_sha256']
        stack, offset = [], span['char_start']
        for line in literal.splitlines(keepends=True):
            marker = re.search(r'% BEGIN ([ABCR]026-[A-Za-z0-9]+)', line)
            if marker:
                stack.append(marker.group(1))
            prefix = '% complete candidates: '
            if stack == [gid] and line.startswith(prefix + '['):
                comment_text = line[len(prefix):].removesuffix('\n')
                comment = json.loads(comment_text)
                projected, sidecar = projection(comment, selected)
                assert pack(projected) == pack(comment)
                recovered = invert_projection(projected, sidecar)
                assert pack(recovered) == pack(selected)
                own_comment_checks.append({'locus_id': locus, 'source_group': gid,
                    'comment_json_char_start': offset + len(prefix),
                    'comment_json_char_end': offset + len(prefix) + len(comment_text),
                    'comment_json_sha256_utf8': sha(comment_text),
                    'candidate_count': len(comment),
                    'ordered_comment_value_equals_selected_value': pack(comment) == pack(selected),
                    'ordered_comment_projection_exact': True,
                    'projection_inverse_sidecar': sidecar,
                    'selected_value_pointer': '/rows/' + str(index) + '/selected_value_exact',
                    'inverse_reconstructs_complete_selected_value': True})
                checked = True
            marker = re.search(r'% END ([ABCR]026-[A-Za-z0-9]+)', line)
            if marker:
                assert stack.pop() == marker.group(1)
            offset += len(line)
        assert not stack
    if not checked:
        deferred_comment_checks.append({'locus_id': locus, 'binding_kind': kind,
            'reason': 'The selected source group has no own one-line JSON array under the exact prefix % complete candidates: . The exact selected binding and source spans remain supplied.'})

assert len(rows) == 91
assert {r['locus_id'] for r in rows} == {f'S{i:02d}' for i in range(1, 40)} | {f'L{i:03d}' for i in range(1, 53)}

# Every string used for retrieval is retained literally and located in a full value.
READING_KEYS = {'reading', 'complete_reading', 'complete_base_reading',
                'enclosing_complete_state', 'fixed_text_state',
                'cancelled_upper_label', 'relation_state', 'ring_candidate'}
PRIMARY_KEYS = {'reading', 'complete_reading', 'complete_base_reading'}
reading_values, reading_ids, candidate_vectors, sigma_index = [], {}, [], []
def intern_reading(value, locus, pointer):
    assert isinstance(value, str)
    if value not in reading_ids:
        rid = f'V{len(reading_values) + 1:04d}'
        reading_ids[value] = rid
        reading_values.append({'id': rid, 'value_exact': value,
            'first_locus_id': locus, 'first_supplement_pointer': pointer,
            'locus_ids_in_source_contract_order': [locus]})
    else:
        rid = reading_ids[value]
        item = reading_values[int(rid[1:]) - 1]
        if locus not in item['locus_ids_in_source_contract_order']:
            item['locus_ids_in_source_contract_order'].append(locus)
    return rid

for ri, row in enumerate(rows):
    selected = row['selected_value_exact']
    locus = row['locus_id']
    for pointer, value in leaves(selected):
        key = pointer.rsplit('/', 1)[-1]
        if isinstance(value, str) and (key in READING_KEYS or isinstance(selected, list) and pointer.count('/') == 1):
            intern_reading(value, locus, f'/rows/{ri}/selected_value_exact' + pointer)
    items = selected if isinstance(selected, list) else [selected]
    fields, vector, missing = [], [], []
    for ci, item in enumerate(items):
        source_pointer = f'/rows/{ri}/selected_value_exact' + ('/' + str(ci) if isinstance(selected, list) else '')
        if isinstance(item, str):
            found = [('', item)]
        else:
            assert isinstance(item, dict)
            found = [(k, v) for k, v in item.items() if k in PRIMARY_KEYS and isinstance(v, str)]
        if not found:
            missing.append(ci)
        for key, value in found:
            pointer = source_pointer + ('/' + esc(key) if key else '')
            rid = intern_reading(value, locus, pointer)
            fields.append({'candidate_index': ci, 'source_field_name': key,
                           'source_pointer': pointer, 'reading_value_id': rid})
            vector.append(value)
    candidate_vectors.append({'locus_id': locus, 'binding_kind': row['selected_state_binding_exact']['kind'],
        'direct_reading_fields_in_original_order': fields,
        'candidate_indices_without_direct_primary_reading_field': missing,
        'literal_string_vector': vector, 'ordered_vector_sha256': sha(pack(vector))})
    if locus.startswith('S'):
        sigma_index.append({'locus_id': locus, 'root_sections_exact': row['root_sections_exact'],
            'complete_candidate_count': len(selected),
            'complete_selected_value_pointer': f'/rows/{ri}/selected_value_exact',
            'reading_fields': fields,
            'full_field_keys_in_candidate_order': [list(v) for v in selected]})
assert len(sigma_index) == 39

# Mechanical TeX-string spans: no glyph state is inferred from these substrings.
sigma_reading_ids = {f['reading_value_id'] for r in sigma_index for f in r['reading_fields']}
sigma_lexical_spans = []
def following_atom_end(s, i):
    if i == len(s):
        return i
    if s[i] == '{':
        depth = 0
        for j in range(i, len(s)):
            if s[j] == '{' and (j == 0 or s[j-1] != '\\'):
                depth += 1
            if s[j] == '}' and (j == 0 or s[j-1] != '\\'):
                depth -= 1
                if depth == 0:
                    return j + 1
        raise AssertionError(('unclosed literal group', s, i))
    if s[i] == '\\':
        m = re.match(r'\\(?:[A-Za-z]+|.)', s[i:])
        assert m
        return i + len(m.group())
    return i + 1

for field in reading_values:
    if field['id'] not in sigma_reading_ids:
        continue
    s = field['value_exact']
    commands = [{'char_start': m.start(), 'char_end': m.end(), 'literal': m.group()}
                for m in re.finditer(r'\\[A-Za-z]+', s)]
    scripts = []
    for m in re.finditer(r'[_^]', s):
        end = following_atom_end(s, m.end())
        scripts.append({'char_start': m.start(), 'char_end': end, 'literal': s[m.start():end]})
    with_at = s.find(' with ')
    sigma_lexical_spans.append({'reading_value_id': field['id'],
        'commands_in_literal_order': commands, 'script_fragments_in_literal_order': scripts,
        'literal_first_with_suffix': None if with_at < 0 else {'char_start': with_at,
            'char_end': len(s), 'literal': s[with_at:]},
        'scope': 'Exact string offsets only. Complete candidate hand, role, attachment, cancellation, insertion and uncertainty fields remain in the selected value.'})

# Historical candidate-comment suffixes remain literal source strings in their order.
historical_vectors = []
for source_id, historical in base['new_source_reference_pool'].items():
    if not source_id.startswith('S'):
        continue
    literal = historical.get('source', {}).get('literal', '')
    matches = list(re.finditer(r'^% Complete candidate: (.*)$', literal, re.M))
    if not matches:
        continue
    source = historical['source']
    original = load(source['path'])
    assert original['sha256'] == source['file_sha256_utf8'], source_id
    a, b = source['char_start_zero_based'], source['char_end_exclusive']
    assert original['text'][a:b] == literal
    assert sha(literal) == source['span_sha256_utf8']
    suffixes = [{'literal_char_start': m.start(1), 'literal_char_end': m.end(1),
                 'suffix_exact': m.group(1)} for m in matches]
    vector = [r['suffix_exact'] for r in suffixes]
    historical_vectors.append({'source_reference_id': source_id,
        'baseline_literal_pointer': '/new_source_reference_pool/' + esc(source_id) + '/source/literal',
        'historical_row_ids': [r['id'] for r in base['exact_notation_rows'] if source_id in r.get('selected_source_reference_ids', [])],
        'source_path': source['path'], 'source_file_sha256': source['file_sha256_utf8'],
        'source_char_start': a, 'source_char_end': b, 'literal_sha256': sha(literal),
        'exact_comment_suffix_spans': suffixes, 'literal_string_vector': vector,
        'ordered_vector_sha256': sha(pack(vector)),
        'projection_scope': 'Only the exact suffix after the exact one-line prefix % Complete candidate: . Other source comments and fields stay at the frozen baseline pointer.'})

array_matrix, equal_pairs, individual_equalities = [], [], []
for current in candidate_vectors:
    vector = current['literal_string_vector']
    offsets = []
    for previous in historical_vectors:
        old = previous['literal_string_vector']
        offset = first_byte_difference(vector, old)
        offsets.append(offset)
        if offset is None:
            equal_pairs.append([current['locus_id'], previous['source_reference_id']])
        for ni, new in enumerate(vector):
            for oi, old_value in enumerate(old):
                if new == old_value:
                    individual_equalities.append({'locus_id': current['locus_id'],
                        'current_vector_index': ni, 'historical_source_reference_id': previous['source_reference_id'],
                        'historical_vector_index': oi, 'exact_shared_string': new})
    array_matrix.append({'locus_id': current['locus_id'], 'first_differing_utf8_byte_offsets': offsets})

# A finite literal retrieval index over the unchanged historical family rows.
TOKENS = {
 'SIGMA': [r'\Sigma', 'Sigma', r'\overline', 'head', 'retrace'],
 'PI_RING': [r'\Pi', r'\circ', 'circle', 'ring'],
 'JOIN': [r'\cap', r'\cup', r'\bigcap', r'\bigcup', r'\sqcup', r'\wedge', 'intersection'],
 'INDEX_ALPHABET': [r'\alpha', r'\mathcal', r'\mathscr', r'\varepsilon', 'E_', 'E with'],
 'RELATION': [r'\subset', r'\supset', r'\supseteq', r'\in', r'\ne', r'\varnothing', 'relation', 'inclusion', 'intersection'],
 'MARK_LEVEL': [r'\prime', r'\circ', 'raised', 'upper', 'lower'],
 'SMALL_TRACE': ['independent', 'point', 'trace', 'detached', 'undetermined'],
 'CORRECTION': [r'\deleted', r'\inserted', 'cancelled', 'cancellation', 'insertion'],
 'ACCENT': ['être', 'etre', 'où', 'ou', 'décomposition', 'dècomposition', 'decomposition', 'déf'],
 'ABBREVIATION': ['ens.', 'ens', 'i.e.', 'i.e', 'ie', 'def', 'déf'],
 'FRAME': [r'\inserted', 'guide', 'parenthetical', 'opener', 'closer'],
 'COMPARISON': [r'\leq', r'\geq', r'\equiv', 'equals'],
 'LABEL': ['``', "''", 'diagramme', 'label'],
 'BOWL_BINOMIAL': [r'\binom', r'\mathbb', 'bowl'],
}
assert set(TOKENS) == {f['family_id'] for f in base['recurring_form_families']}
def token_spans(text, token):
    expression = re.escape(token)
    if re.fullmatch(r'\\[A-Za-z]+', token):
        expression += r'(?![A-Za-z])'
    elif re.fullmatch(r'[A-Za-zÀ-ÖØ-öø-ÿ.]+', token):
        expression = r'(?<![A-Za-zÀ-ÖØ-öø-ÿ\\])' + expression + r'(?![A-Za-zÀ-ÖØ-öø-ÿ.])'
    return [[m.start(), m.end()] for m in re.finditer(expression, text)]

baseline_rows = {r['id']: (i, r) for i, r in enumerate(base['exact_notation_rows'])}
family_comparisons = []
for fi, family in enumerate(base['recurring_form_families']):
    matches = []
    for token in TOKENS[family['family_id']]:
        old_matches, new_matches = [], []
        for row_id in family['notation_row_ids']:
            bi, previous = baseline_rows[row_id]
            literal = previous['source']['literal']
            assert literal.startswith('| ') and literal.endswith(' |\n')
            cells = literal[2:-3].split(' | ')
            assert len(cells) == 4 and '| ' + ' | '.join(cells) + ' |\n' == literal
            start = 2
            for ci, cell in enumerate(cells):
                positions = token_spans(cell, token)
                if positions:
                    old_matches.append({'notation_row_id': row_id,
                        'baseline_literal_pointer': f'/exact_notation_rows/{bi}/source/literal',
                        'source_cell_index': ci, 'cell_char_start_in_literal': start,
                        'exact_token_char_intervals_in_cell': positions})
                start += len(cell) + 3
        for value in reading_values:
            positions = token_spans(value['value_exact'], token)
            if positions:
                new_matches.append({'reading_value_id': value['id'],
                    'exact_token_char_intervals': positions,
                    'locus_ids': value['locus_ids_in_source_contract_order']})
        if old_matches and new_matches:
            matches.append({'literal_token': token, 'historical_cell_matches': old_matches,
                            'selected_reading_matches': new_matches})
    family_comparisons.append({'historical_family_id': family['family_id'],
        'baseline_family_pointer': '/recurring_form_families/' + str(fi),
        'historical_family_ordered_sha256': sha(pack(family)),
        'explicit_literal_retrieval_tokens': TOKENS[family['family_id']],
        'shared_literal_token_matches': matches,
        'scope': 'These are exact source substring retrieval pairs. Original family objects, member lists, candidate objects and local root authorities remain unchanged.'})

# The complement of the 71 framed groups preserves ordinary prose and formula text.
intervals = sorted((g['final_source']['char_start'], g['final_source']['char_end'])
                   for g in contract['source_group_registry'].values())
merged = []
for a, b in intervals:
    if merged and a <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], b)
    else:
        merged.append([a, b])
unframed, partition, cursor = [], [], 0
for a, b in merged + [[len(tex), len(tex)]]:
    if cursor < a:
        literal = tex[cursor:a]
        unframed.append({'id': f'T{len(unframed)+1:03d}', 'char_start': cursor, 'char_end': a,
            'utf8_byte_start': len(tex[:cursor].encode('utf-8')),
            'utf8_byte_end': len(tex[:a].encode('utf-8')), 'literal_exact': literal,
            'literal_sha256': sha(literal)})
        partition.append([cursor, a, 'unframed', unframed[-1]['id']])
    if a < b:
        partition.append([a, b, 'framed', None])
    cursor = b
assert ''.join(tex[a:b] for a, b, _, _ in partition) == tex
first_ens = [m for u in unframed for m in re.finditer(r'(?<![A-Za-z])ens\.(?![A-Za-z.])', u['literal_exact'])]
assert len(first_ens) == 1
ens_span = next((u['char_start'] + m.start(), u['char_start'] + m.end())
    for u in unframed for m in re.finditer(r'(?<![A-Za-z])ens\.(?![A-Za-z.])', u['literal_exact']))
ordinary_abbreviation = {'id': 'N026-TEXT-ENS-FIRST', 'literal': tex[ens_span[0]:ens_span[1]],
    'source_char_start': ens_span[0], 'source_char_end': ens_span[1],
    'source_path': tex_path, 'source_sha256': load(tex_path)['sha256'],
    'root_section': '02', 'root_section_authority_pointer': '/root_sections/1',
    'scope': 'The first ordinary ens. stays separate from the exact L002 second ens reading. Both literal source strings are preserved.'}

supplement = {
 'schema': 'notation026-exact-source-supplement-v1', 'source_only': True,
 'audit_complete': False, 'main_approved': False, 'root_review_claimed': False,
 'baseline': {'source': descriptor(BASE), 'original_row_count': 180, 'original_family_count': 14,
              'exact_rows_ordered_sha256': sha(pack(base['exact_notation_rows'])),
              'exact_families_ordered_sha256': sha(pack(base['recurring_form_families'])),
              'baseline_mutations': []},
 'root_authority_index': descriptor(AUTHORITY), 'source_contract': descriptor(CONTRACT),
 'selected_tex': descriptor(tex_path),
 'physical_loci': 91, 'sigma_loci': 39, 'row_order': contract['locus_order'],
 'rows': rows,
 'binding_reference_table': [copy.deepcopy(refs[rid]) for rid in refs if rid in used_refs],
 'resolved_binding_values_exact': {rid: copy.deepcopy(values[rid]) for rid in refs if rid in used_refs},
 'sigma_complete_state_index': sigma_index,
 'reading_value_pool': reading_values, 'sigma_literal_facets': sigma_lexical_spans,
 'historical_family_comparisons': family_comparisons,
 'current_direct_reading_vectors': candidate_vectors,
 'historical_one_line_comment_vectors': historical_vectors,
 'exact_candidate_vector_comparison': {
     'domain': 'UTF-8 bytes of json.dumps(vector, ensure_ascii=False, separators=(comma, colon)); vectors are exact ordered source string projections defined above.',
     'historical_column_order': [x['source_reference_id'] for x in historical_vectors],
     'rows': array_matrix, 'equal_vector_pairs': equal_pairs,
     'pair_count': len(candidate_vectors) * len(historical_vectors),
     'null_entry_means_exact_byte_equality': True,
     'integer_entry_is_first_unequal_byte_or_shorter_byte_length': True,
     'individual_exact_string_equalities': individual_equalities},
 'own_json_comment_projection_checks': own_comment_checks,
 'selected_arrays_without_that_exact_comment_prefix': deferred_comment_checks,
 'unframed_literal_segments': unframed,
 'complete_source_interval_partition': partition,
 'ordinary_first_ens': ordinary_abbreviation,
 'remaining_source_only_findings': [
     {'id': 'N026-REPORT-FIELD-PROJECTION', 'scope': 'Own one-line JSON candidate comments',
      'checked_loci': len(own_comment_checks),
      'complete_object_equalities': sum(x['ordered_comment_value_equals_selected_value'] for x in own_comment_checks),
      'exact_reversible_projections': sum(not x['ordered_comment_value_equals_selected_value'] for x in own_comment_checks),
      'conflicting_retained_values_or_orders': 0,
      'action_applied': None,
      'evidence': '/own_json_comment_projection_checks'},
     {'id': 'N026-PARENT-SCOPE', 'scope': 'The four scoped parent bindings retain their named child loci, and the expanded diagram96 and pair16 arrays retain each complete component object.',
      'action_applied': None,
      'evidence': '/rows'},
     {'id': 'N026-NREV-PENDING', 'scope': 'NREV01/NREV02 remain root-owned unapplied public-report proposals. This supplement makes no mutation to those proposals, their pages, reader records, historical maps or notation rows.',
      'evidence_source': 'out/checks/notation_NREV01_NREV02_public_report_proposal_v01.json',
      'action_applied': None}],
 'limitations': ['The helper inspected source text and exact data values only.',
                 'Root performs the final cross-page notation review and acceptance.',
                 'Historical lexical retrieval does not choose a candidate or alter a local hand, role, attachment or physical locus.'],
 'operations': {'ink_decisions_added': 0, 'images_accessed': 0, 'global_notation_substitutions': [],
                'NREV_applied': False, 'source_page_edits': [], 'render_or_compile': False},
}
for path, original in CACHE.items():
    assert (ROOT / path).read_bytes() == original['raw'], path
artifact = write('notation026_supplement_v01.json', supplement)
proof = {'utc': datetime.now(timezone.utc).isoformat(), 'supplement': artifact,
         'source_documents': [descriptor(path) for path in CACHE],
         'raw_json_references_verified': len(refs), 'all_raw_json_reference_bytes_and_ordered_values_match': True,
         'physical_loci': 91, 'sigma_loci': 39,
         'all_selected_tex_spans_byte_verified': True,
         'own_json_comment_arrays_checked': len(own_comment_checks),
         'all_own_comment_projections_and_full_inverse_values_exact': True,
         'historical_vector_count': len(historical_vectors),
         'ordered_vector_pairs_compared': len(candidate_vectors) * len(historical_vectors),
         'unframed_segment_count': len(unframed), 'source_partition_reconstructs_original_utf8_bytes': True,
         'historical180_rows_and14_families_unchanged': True,
         'all_source_inputs_byte_identical_after_build': True,
         'root_review_claimed': False, 'output_files_written_only_under_notation026_prefix': True}
write('notation026_source_replay_proof_v01.json', proof)
print(json.dumps({'artifact': artifact, 'rows': len(rows), 'sigma_loci': len(sigma_index),
                  'reading_values': len(reading_values), 'historical_vectors': len(historical_vectors),
                  'exact_vector_equalities': equal_pairs, 'individual_exact_string_equalities': len(individual_equalities),
                  'own_comment_arrays': len(own_comment_checks), 'unframed_segments': len(unframed),
                  'all_assertions_passed': True}, ensure_ascii=False, indent=2))
