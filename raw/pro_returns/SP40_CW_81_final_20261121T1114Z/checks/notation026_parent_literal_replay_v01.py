#!/usr/bin/env python3
"""Parse the two exact embedded source tables and replay their finite state lists."""
from pathlib import Path
import copy, hashlib, json, re
ROOT = Path('/workspace/scratch/94548b74fbe0')
OUT = ROOT / 'out/checks'
pack = lambda v: json.dumps(v, ensure_ascii=False, separators=(',', ':'))
full = lambda v: (json.dumps(v, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
sha = lambda b: hashlib.sha256(b.encode('utf-8') if isinstance(b, str) else b).hexdigest()
contract = json.loads((OUT / 'scan026_source_selected_contract_v01.json').read_bytes())
tex_path = ROOT / contract['final_staged_source']['path']
tex_bytes = tex_path.read_bytes()
tex = tex_bytes.decode('utf-8')
assert sha(tex_bytes) == '318b043580aba18b302169e52d7c3570208e8211cc7f32f8828cc070ee743615'

def parse_comments(kind, gid):
    descriptor = contract['source_group_registry'][gid]['final_source']
    literal = tex[descriptor['char_start']:descriptor['char_end']]
    prefix = '% ROOT ' + kind + ' '
    parsed, spans, active = {}, [], None
    position = descriptor['char_start']
    for line in literal.splitlines(keepends=True):
        if line.startswith(prefix):
            rest = line[len(prefix):].removesuffix('\n')
            key, body = rest.split(' ', 1)
            indexed = re.fullmatch(r'([^\[]+)\[(\d+)\]', key)
            if body == 'BEGIN':
                assert active is None and key not in parsed
                active = key
                parsed[key] = []
            elif body == 'END':
                assert active == key
                active = None
            elif indexed:
                key, index = indexed.group(1), int(indexed.group(2))
                assert active == key and index == len(parsed[key])
                parsed[key].append(json.loads(body))
            else:
                assert active is None and key not in parsed
                parsed[key] = json.loads(body)
            spans.append({'char_start': position, 'char_end': position + len(line),
                          'line_sha256_utf8': sha(line)})
        position += len(line)
    assert active is None
    return parsed, spans

def diagram_expand(c, row):
    li, ri, ei, eh, mh, ph = row['tuple']
    ai = c['reordered_base_lookup'][li][ri][ei]
    assert row['original_A_candidate_index'] == ai
    assert row['E_state_index'] == eh * 2 + ei
    assert row['S15_state_index'] == mh and row['S16_state_index'] == ph
    base = c['original_A_base_candidates'][ai]
    return {'tuple': row['tuple'], 'complete_base_reading': base['reading'],
        'cancelled_upper_label': r'\deleted{' + c['axes'][0][li] + '}',
        'relation_state': c['axes'][1][ri] + (' with extra lower retrace' if ri else ''),
        'E_complete_state': copy.deepcopy(c['root_E_states'][row['E_state_index']]),
        'S15_complete_state': copy.deepcopy(c['exact_C_S15_states'][mh]),
        'S16_complete_state': copy.deepcopy(c['exact_C_S16_states'][ph]),
        'detached_point_state': copy.deepcopy(c['root_point_state']),
        'base_A_candidate_provenance': copy.deepcopy(base),
        'hand_scope_rule': 'Current component hands are the E/S15/S16/point fields above; the complete original A parent object is retained as provenance.',
        'literal_drawing_source_group': 'B026-DIAG'}

def pair_expand(c, row):
    opener, h18, h19, h20 = row['tuple']
    children = c['exact_A_local_states']
    return {'tuple': row['tuple'], 'complete_base_reading': c['resolved_parent_base_candidates'][opener]['reading'],
        'opener_complete_state': copy.deepcopy(children['A026-G09'][opener]),
        'S17_complete_state': copy.deepcopy(children['A026-S17'][0]),
        'S18_complete_state': copy.deepcopy(children['A026-S18'][h18]),
        'S19_complete_state': copy.deepcopy(children['A026-S19'][h19]),
        'S20_complete_state': copy.deepcopy(children['A026-S20'][h20]),
        'base_A_parent_candidate_provenance': copy.deepcopy(c['original_A_parent_candidates'][opener]),
        'hand_scope_rule': 'The exact local child fields retain every independent-run hand. Original broad A parent attribution remains raw provenance.',
        'fixed_text_state': r'\deleted{distinctes} \inserted{de X,}',
        'literal_drawing_source_group': 'A026-G08'}

proofs = []
for name, kind, gid, expand, expected_count in [
    ('diagram96', 'DIAGRAM96', 'B026-DIAG', diagram_expand, 96),
    ('pair16', 'PAIR16', 'A026-G08', pair_expand, 16)]:
    path = OUT / ('scan026_source_' + name + '_codec_v01.json')
    original_bytes = path.read_bytes()
    original = json.loads(original_bytes)
    parsed, spans = parse_comments(kind, gid)
    expected = {k: v for k, v in original.items() if k != 'root_authority_refs'}
    assert pack(parsed) == pack(expected)
    restored = dict(parsed)
    restored['root_authority_refs'] = copy.deepcopy(original['root_authority_refs'])
    assert full(restored) == original_bytes
    expanded = [expand(parsed, row) for row in parsed['tuple_to_complete_state']]
    assert len(expanded) == expected_count
    expanded_path = OUT / ('scan026_source_' + name + '_expanded_v01.json')
    expanded_bytes = expanded_path.read_bytes()
    assert full(expanded) == expanded_bytes
    recovered = []
    for value in expanded:
        if name == 'diagram96':
            row = {'tuple': value['tuple'],
                'original_A_candidate_index': next(i for i, v in enumerate(parsed['original_A_base_candidates']) if pack(v) == pack(value['base_A_candidate_provenance'])),
                'E_state_index': next(i for i, v in enumerate(parsed['root_E_states']) if pack(v) == pack(value['E_complete_state'])),
                'S15_state_index': next(i for i, v in enumerate(parsed['exact_C_S15_states']) if pack(v) == pack(value['S15_complete_state'])),
                'S16_state_index': next(i for i, v in enumerate(parsed['exact_C_S16_states']) if pack(v) == pack(value['S16_complete_state']))}
        else:
            fields = [('A026-G09', 'opener_complete_state'), ('A026-S18', 'S18_complete_state'),
                      ('A026-S19', 'S19_complete_state'), ('A026-S20', 'S20_complete_state')]
            row = {'tuple': [next(i for i, v in enumerate(parsed['exact_A_local_states'][g]) if pack(v) == pack(value[f])) for g, f in fields]}
        assert pack(expand(parsed, row)) == pack(value)
        recovered.append(row)
    assert pack(recovered) == pack(parsed['tuple_to_complete_state'])
    proofs.append({'name': name, 'source_group': gid, 'source_path': str(tex_path.relative_to(ROOT)),
        'source_sha256': sha(tex_bytes), 'exact_comment_line_spans': spans,
        'original_definition_path': str(path.relative_to(ROOT)), 'original_definition_bytes': len(original_bytes),
        'original_definition_sha256': sha(original_bytes),
        'embedded_exact_keys_in_order': list(parsed),
        'inverse_additional_member': ['root_authority_refs', copy.deepcopy(original['root_authority_refs'])],
        'embedded_field_projection_and_definition_inverse_byte_exact': True,
        'expanded_path': str(expanded_path.relative_to(ROOT)), 'expanded_bytes': len(expanded_bytes),
        'expanded_sha256': sha(expanded_bytes), 'states': expected_count,
        'embedded_table_replay_matches_every_expanded_utf8_byte': True,
        'all_expanded_states_inverse_to_original_explicit_tuples': True})
result = {'schema': 'notation026-embedded-parent-tables-replay-v1', 'proofs': proofs,
          'images_accessed': 0, 'ink_decisions_added': 0, 'source_mutations': [], 'root_review_claimed': False}
output = OUT / 'notation026_parent_literal_replay_proof_v01.json'
with output.open('xb') as handle:
    handle.write(full(result))
print(json.dumps({'proof': str(output.relative_to(ROOT)), 'sha256': sha(output.read_bytes()),
                  'all_assertions_passed': True, 'expanded_states': [96, 16]}, indent=2))
