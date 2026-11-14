#!/usr/bin/env python3
"""Bind both complete proofs/replays of the actual order-three candidate identity."""
from pathlib import Path
from hashlib import sha256
import datetime
import json

ROOT = Path(__file__).resolve().parents[2]
sha = lambda p: sha256(p.read_bytes()).hexdigest()
def binding(name):
    p = ROOT / name
    return {'path': name, 'bytes': p.stat().st_size, 'sha256': sha(p)}

author_name = 'work/part_d_attack/actual_order_three_defect_and_canonical_candidate_result.json'
peer_name = 'work/part_c/review_actual_order_three_defect_and_canonical_candidate.json'
root_replay_name = 'work/root/actual_order_three_defects_independent_replay/comparison.json'
expected = {
    author_name: 'b5c422c5570c93f8ce4c795412a8426d9c7d3edd88e5465984ccd3b8fd087923',
    peer_name: 'a659dfc5b30ba05d2422b8c9ff6fd95653ba288d8116b03602bf02fd836ad4d0',
    'work/part_d_attack/actual_order_three_defect_and_canonical_candidate.txt': '5ade89b50075a8c600576f0e8033a47164fba9947a7a501bd9ff66551bfedd5b',
    'work/part_c/review_actual_order_three_defect_and_canonical_candidate.txt': 'd4f62316f95e6d29fa9bc6aa318f3083770a4e6d46c1e06bc7ca9a64abd5d92a',
    root_replay_name: '02334d7a29277e325028c0be089e2c86e379a29f89a210a4531d9c01215b7c1d',
    'work/part_c/order_three_defects_peer_replay/comparison.json': 'd33d78c7ea75217be996e70739290358aad0231e219d4fe93b4340b51924292c'}
for name, digest in expected.items(): assert sha(ROOT / name) == digest, name
author, peer, replay = [json.loads((ROOT / name).read_text()) for name in [author_name, peer_name, root_replay_name]]
assert peer['verdict'] == 'PASS' and not peer['correction_requested']
assert not peer['frozen_author_and_dependency_files_changed']
assert len(author['files']) + len(author['dependencies']) + len(author['source_comparison_only']) == 20
assert len(peer['all_20_author_routes_verified']) == 20
assert replay['status'] == 'PASS_UNCHANGED_ISOLATED_ROOT_REPLAY'
assert replay['named_checks'] == peer['replay']['named_checks'] == 24
assert replay['defect_cases'] == peer['replay']['defect_cases'] == 644
assert replay['finite_nonzero_separations'] == peer['replay']['finite_nonzero_separations'] == 642
assert peer['replay']['exit_code'] == 0 and peer['replay']['stderr_bytes'] == 0
bound = {}
def verify(value):
    if isinstance(value, dict):
        if all(k in value for k in ['path', 'bytes', 'sha256']):
            p = Path(value['path'])
            p = p if p.is_absolute() else ROOT / p
            assert p.stat().st_size == value['bytes'] and sha(p) == value['sha256'], str(p)
            relative = str(p.relative_to(ROOT))
            bound[relative] = binding(relative)
        for child in value.values(): verify(child)
    elif isinstance(value, list):
        for child in value: verify(child)
for data in [author, peer, replay]: verify(data)
peer_comparison = json.loads((ROOT / 'work/part_c/order_three_defects_peer_replay/comparison.json').read_text())
verify(peer_comparison)
for name in expected:
    bound[name] = binding(name)
for name in ['work/root/review_actual_order_three_defect_and_canonical_candidate.txt',
             'work/root/replay_actual_order_three_defects.py',
             'work/root/replay_actual_order_three_defects_stdout.json',
             'work/root/marked_v4_continuation_acceptance.json',
             'work/root/negative_transposition_continuation_acceptance.json',
             'work/root/norm_branch_acceptance_270.json',
             'work/root/actual_class_two_acceptance_270.json']:
    bound[name] = binding(name)

outputs = [
    'work/part_d_attack/code/actual_order_three_defects_output.json',
    'work/part_d_attack/code/actual_order_three_defects_stdout.txt',
    'work/root/actual_order_three_defects_independent_replay/actual_order_three_defects_output.json',
    'work/root/actual_order_three_defects_independent_replay/stdout.txt',
    'work/part_c/order_three_defects_peer_replay/actual_order_three_defects_output.json',
    'work/part_c/order_three_defects_peer_replay/stdout.txt']
original = (ROOT / outputs[0]).read_bytes()
assert sha256(original).hexdigest() == '634910286efa79d802c6c08efa0f131b987b9ea2f329bccb0e0b22927fe6a5d4'
assert all((ROOT / name).read_bytes() == original for name in outputs)
result = json.loads(original)
assert len(result['checks']) == 24 and all(x['passed'] for x in result['checks'])
assert result['finite_nonzero_separations_by_prime'] == {'3': 598, '5': 44}
assert result['simultaneous_solutions_in_corpus'] == [
    {'nu': -1, 'epsilon': 1, 'c': 'y'}, {'nu': 1, 'epsilon': -1, 'c': 'x^-1'}]
record = {
    'status': 'ACCEPTED_UNNUMBERED_CONTINUATION_ROOT_AND_PEER_PASS',
    'sealed_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'numbered_claim_registered': False,
    'root_full_author_proof_lines_read': 424, 'root_full_program_lines_read': 255,
    'root_full_output_lines_read': 209, 'root_full_author_metadata_read': True,
    'root_full_primary_comparison_note_lines_read': 40,
    'root_full_peer_report_lines_read': 400, 'root_peer_metadata_read': True,
    'root_new_external_source_opening_claimed': False,
    'mathematical_corrections_requested': [], 'author_routes_verified': 20,
    'named_checks_each': 24, 'defect_cases_each': 644,
    'finite_nonzero_separations_each': 642, 'separation_prime_counts_each': {'3': 598, '5': 44},
    'six_author_root_peer_output_stdout_files_whole_bytes_identical': True,
    'forward_and_inverse_output_maps': 'identity on each entire output byte string',
    'serialized_witness_scope': 'Counts and first finite witness in each of four branches; every one of642 nonzero cases is separately checked by the retained executed deterministic program.',
    'accepted_scope': 'The exact actual M=C2*C3 inverse maps, full three-defect extension space, original-T homeomorphism in both directions, canonical original m/W set identity and complete continuous conjugator fibers.',
    'retained_target': 'Actual full-unit m, full original W=1, image <z,g>=F and original T nonemptiness.',
    'binding_count': len(bound), 'bindings': [bound[k] for k in sorted(bound)],
    'published_pdf_preserved': binding('work/root/prior_271_snapshot/binding.json'),
    'sealed_by': binding('work/root/seal_order_three_candidate_review.py')}
out = ROOT / 'work/root/order_three_candidate_continuation_acceptance.json'
assert not out.exists()
out.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'status': record['status'], 'binding_count': len(bound),
                  'acceptance': binding(str(out.relative_to(ROOT)))}, indent=2))
