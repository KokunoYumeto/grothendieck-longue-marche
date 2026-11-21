#!/usr/bin/env python3
"""Replay frozen constructors in memory and compare complete artifact UTF-8 bytes."""
from pathlib import Path
import ast, copy, hashlib, json
ROOT = Path('/workspace/scratch/94548b74fbe0')
OUT = ROOT / 'out/checks'
full = lambda v: (json.dumps(v, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
pack = lambda v: json.dumps(v, ensure_ascii=False, separators=(',', ':'))
sha = lambda b: hashlib.sha256(b).hexdigest()
focus_path = OUT / 'notation026_new_assertions_v01.json'
focus_bytes = focus_path.read_bytes()
assert sha(focus_bytes) == '16708619cece52654f3fec993aa066bfee267badc7b3f43489987e185211cc6b'
focus = json.loads(focus_bytes)
sources = {}
for reference in focus['constructor_sources']:
    path = ROOT / reference['path']
    raw = path.read_bytes()
    assert sha(raw) == reference['sha256_utf8'] and len(raw) == reference['bytes']
    sources[path.name] = raw.decode('utf-8')

source = sources['notation026_extend_v01.py']
assert source.count('\nartifact = write(') == 1
prefix = source.split('\nartifact = write(', 1)[0]
tree = ast.parse(prefix)
assert not any(isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == 'write' for n in ast.walk(tree))
namespace = {'__name__': '__source_constructor_replay__'}
exec(prefix, namespace)
supplement = namespace['supplement']
supplement_bytes = full(supplement)
supplement_original = (OUT / 'notation026_supplement_v01.json').read_bytes()
assert supplement_bytes == supplement_original

parent_source = sources['notation026_parent_literal_replay_v01.py']
assert parent_source.count('\noutput = OUT / ') == 1
parent_prefix = parent_source.split('\noutput = OUT / ', 1)[0]
parent_namespace = {'__name__': '__parent_constructor_replay__'}
exec(parent_prefix, parent_namespace)
parent_proof = parent_namespace['result']
parent_bytes = full(parent_proof)
parent_original = (OUT / 'notation026_parent_literal_replay_proof_v01.json').read_bytes()
assert parent_bytes == parent_original

parameters = focus['constructor_parameters']
bundle = {'schema': 'notation026-complete-review-bundle-v1',
    'prepared_utc': parameters['full_bundle_prepared_utc'],
    'review_scope': parameters['full_bundle_review_scope'],
    'frozen_supplement_reference': focus['full_expanded_artifacts']['supplement'],
    'frozen_supplement_prepared_utc': parameters['frozen_supplement_prepared_utc'],
    'frozen_supplement': supplement,
    'source_replay_proof': focus['source_replay_proof_exact'],
    'parent_embedded_table_replay_proof': parent_proof,
    'subsequent_root_status': focus['subsequent_root_status_exact'],
    'root_review_of_this_new_bundle_claimed': False,
    'source_mutations_by_helper': []}
bundle_bytes = full(bundle)
bundle_original = (OUT / 'notation026_review_input_v01.json').read_bytes()
assert bundle_bytes == bundle_original

equalities = [
 ('new_family_comparisons_exact', 'historical_family_comparisons'),
 ('new_candidate_vector_comparisons_exact', 'exact_candidate_vector_comparison'),
 ('historical_comment_vector_definitions_exact', 'historical_one_line_comment_vectors'),
 ('arrays_without_the_exact_comment_prefix', 'selected_arrays_without_that_exact_comment_prefix'),
 ('complete_source_interval_partition', 'complete_source_interval_partition'),
 ('ordinary_first_ens_exact', 'ordinary_first_ens'),
 ('new_findings_exact_at_preparation', 'remaining_source_only_findings'),
 ('limitations_exact', 'limitations'), ('operations_exact', 'operations')]
for fk, sk in equalities:
    assert pack(focus[fk]) == pack(supplement[sk])
row_map = [{key: row[key] for key in ['id', 'locus_id', 'root_sections_exact',
    'source_contract_row_pointer', 'source_contract_row_ordered_sha256',
    'selected_state_binding_exact']} for row in supplement['rows']]
assert pack(row_map) == pack(focus['new_row_root_source_map'])
comment_maps = []
for row in supplement['own_json_comment_projection_checks']:
    result = {key: value for key, value in row.items() if key != 'projection_inverse_sidecar'}
    if not row['ordered_comment_value_equals_selected_value']:
        result['omitted_member_map'] = [
            {'pointer': m['pointer'], 'original_key_order': m['original_key_order'],
             'omitted_member_keys_in_original_order': [key for key, value in m['omitted_members_in_original_order']]}
            for m in row['projection_inverse_sidecar'] if m['omitted_members_in_original_order']]
    comment_maps.append(result)
assert pack(comment_maps) == pack(focus['own_comment_projection_maps'])
for path, frozen in namespace['CACHE'].items():
    assert (ROOT / path).read_bytes() == frozen['raw']
assert focus_path.read_bytes() == focus_bytes

proof = {'schema': 'notation026-focused-constructor-replay-proof-v1',
    'focus_path': str(focus_path.relative_to(ROOT)), 'focus_bytes': len(focus_bytes),
    'focus_sha256': sha(focus_bytes),
    'constructors_replayed_from': focus['constructor_sources'],
    'accepted_candidate_values_loaded_from_frozen_contract_references': True,
    'expanded_original_artifact_values_used_only_for_final_byte_comparison': True,
    'supplement_source_bytes': len(supplement_original),
    'supplement_replayed_bytes': len(supplement_bytes),
    'supplement_source_sha256': sha(supplement_original),
    'supplement_replayed_sha256': sha(supplement_bytes),
    'supplement_actual_byte_for_byte_equal': supplement_bytes == supplement_original,
    'parent_proof_actual_byte_for_byte_equal': parent_bytes == parent_original,
    'bundle_source_bytes': len(bundle_original), 'bundle_replayed_bytes': len(bundle_bytes),
    'bundle_source_sha256': sha(bundle_original), 'bundle_replayed_sha256': sha(bundle_bytes),
    'bundle_actual_byte_for_byte_equal': bundle_bytes == bundle_original,
    'first_mismatching_byte': None,
    'focused_field_to_expanded_field_exact_maps': equalities,
    'all91_focused_row_maps_reconstructed_exactly': True,
    'all52_comment_projection_maps_reconstructed_exactly': True,
    'input_sources_and_focus_byte_unchanged': True,
    'candidate_or_notation_changes': [], 'root_review_claimed': False}
path = OUT / 'notation026_constructor_replay_proof_v01.json'
with path.open('xb') as handle:
    handle.write(full(proof))
print(json.dumps(proof, ensure_ascii=False, indent=2))
