#!/usr/bin/env python3
"""Accept F32 after complete proof/code/author/peer reads and exact replays."""
from pathlib import Path
from hashlib import sha256
import json
import re

ROOT = Path(__file__).resolve().parents[2]
stem = 'work/part_a/f_nonproduct_first_character_one_images'
expected = {
    stem+'.tex': 'b91fd2611f1d9bd5cde096c6307004dca0fc740463971c164aa0fe52a146af13',
    stem+'_results.json': 'ba4c8a418f8a6b11fd083a2568689c1cb7fcec159003b290b53de968a7938cef',
    stem+'_report.txt': '3522480edbca67dba678009f9e530e6670fefa60e787783b84a4245a8ffce37c',
    stem+'_evidence_manifest.json': '86e68a925d9d6a151d5ce5e292d9042cf7848402e84e7b9d0a6a125d99a6881f',
    'work/root/review_f32.txt': '6082bf0e4b5795654ae2b4f466b7a370882aca7d0689a6190324b3f61f506656',
    'work/part_c/review_f32.txt': 'ba32cf253dda348d3a7a127c123153d7a2ca69b95205b6a83f418b616dec1a2b',
    'work/part_c/review_f32.json': 'ba2ee61498b0af1ed906b3e16ee49b1a25e73447d6f0c763a65d162c50546ec1',
    'work/root/f32_independent_replay/comparison.json': '4118e928fae7da36e9c2253394736c49d43bbd44838fd99c75fb711c25d69e2a',
    'work/part_c/f32_independent_replay/comparison.json': '27fbfce87e9485dcb2bc728c7f25e49a9894eff2737576c38156536d63fe8dfa',
    'work/part_c/f32_independent_replay/printed_formula_crosscheck.py': 'c0d191fc5ba4d354804eed3ce90e7b503edcc858c82f926b37e17f4483e9a0cc',
    'work/part_c/f32_independent_replay/printed_formula_crosscheck_output.json': '62837fb0c8824431e64ee1cf518103760bdd7b5805c286dc41d03beeeeac442d',
}

def path(name):
    p = Path(name)
    return p if p.is_absolute() else ROOT/p

def bind(name):
    p = path(name)
    b = p.read_bytes()
    return {'path': str(p.relative_to(ROOT)), 'bytes': len(b), 'sha256': sha256(b).hexdigest()}

def read(name):
    return json.loads(path(name).read_text())

all_bound = {}
def verify_tree(value):
    if isinstance(value, dict):
        if isinstance(value.get('path'), str) and 'sha256' in value:
            got = bind(value['path'])
            assert got['sha256'] == value['sha256'], value['path']
            if 'bytes' in value:
                assert got['bytes'] == value['bytes'], value['path']
            all_bound[got['path']] = got
        for child in value.values():
            verify_tree(child)
    elif isinstance(value, list):
        for child in value:
            verify_tree(child)

for name, digest in expected.items():
    assert bind(name)['sha256'] == digest, name
proof = path(stem+'.tex').read_text()
assert len(proof.splitlines()) == 677
assert re.findall(r'\\tag\{F\.32\.(\d+)\}', proof) == [str(i) for i in range(1,25)]
meta = read(stem+'_results.json')
assert meta['id'] == 'F.32' and meta['status'] == 'Proved'
manifest = read(stem+'_evidence_manifest.json')
assert len(manifest['entries']) == 59
verify_tree(manifest)
assert len({e['path'] for e in manifest['entries']}) == 59
peer = read('work/part_c/review_f32.json')
assert peer['status'] == 'PASS_INDEPENDENT_F32_FULL_PROOF_CODE_EVIDENCE_AND_REPLAY_REVIEW'
assert peer['proof_full_read_lines'] == 677 and peer['checker_full_read_lines'] == 318
assert not peer['corrections_requested'] and not peer['mathematical_issues']
assert peer['evidence_manifest']['entry_count'] == 59
assert peer['evidence_manifest']['all_entries_exact']
assert peer['all_completed_earlier_sources_unchanged']
assert peer['prior_route_count'] == 277
verify_tree(peer)
root_replay = read('work/root/f32_independent_replay/comparison.json')
peer_replay = read('work/part_c/f32_independent_replay/comparison.json')
verify_tree(root_replay)
verify_tree(peer_replay)
assert root_replay['status'] == 'PASS' and root_replay['total_exact_checks'] == 1088
assert root_replay['module_checks'] == 710 and root_replay['word_and_parser_checks'] == 378
assert not root_replay['raw_output_byte_identical']
assert peer_replay['status'] == 'PASS_F32_UNCHANGED_ISOLATED_LITERAL_WORD_REPLAY'
assert peer_replay['total_exact_checks'] == 1088 and peer_replay['copied_input_count'] == 12
assert peer_replay['all_original_files_unchanged_after_replay']
encode = lambda v: (json.dumps(v, indent=2)+'\n').encode()
for record, actual_key, original_key, mapping in [
    (root_replay, 'actual', 'reference', root_replay['inverse_path_map']),
    (peer_replay, 'isolated_output', 'source_output', peer_replay['input_path_bijection']),
]:
    actual_bytes = path(record[actual_key]['path']).read_bytes()
    original_bytes = path(record[original_key]['path']).read_bytes()
    actual, original = json.loads(actual_bytes), json.loads(original_bytes)
    assert len(mapping) == len(set(mapping.values())) == 12
    inverse = {v: k for k, v in mapping.items()}
    forward = dict(actual)
    forward['inputs'] = {mapping[k]: v for k, v in actual['inputs'].items()}
    backward = dict(original)
    backward['inputs'] = {inverse[k]: v for k, v in original['inputs'].items()}
    assert encode(forward) == original_bytes
    assert encode(backward) == actual_bytes
    assert actual_bytes != original_bytes
st = peer_replay['stdout_transport']
peer_stdout = path(peer_replay['stdout']['path']).read_bytes()
author_stdout = path(st['source_stdout']['path']).read_bytes()
old, new = st['substitution_from'].encode(), st['substitution_to'].encode()
assert peer_stdout.count(old) == author_stdout.count(new) == 1
assert peer_stdout.replace(old, new, 1) == author_stdout
assert author_stdout.replace(new, old, 1) == peer_stdout
printed = read('work/part_c/f32_independent_replay/printed_formula_crosscheck_output.json')
verify_tree(printed)
assert printed['status'] == 'PASS_F32_ACTUAL_TEX_FORMULA_COMPARISON'
assert printed['total_exact_checks'] == 86
body = path(peer['review_body']['path']).read_bytes()
full = path('work/part_c/review_f32.txt').read_bytes()
assert full.startswith(body)
record = {
    'status': 'PASS_ROOT_AND_PEER', 'claim': 'F.32',
    'proof_sha256': expected[stem+'.tex'], 'proof_lines': 677,
    'numbered_displays': 24, 'checker_lines': 318,
    'producer_lines': [125,72,104,100],
    'frozen_artifacts': [bind(p) for p in expected],
    'root_mathematical_audit': bind('work/root/review_f32.txt'),
    'root_read_final_author_metadata_and_report_in_full': True,
    'root_final_author_report_lines': 385,
    'root_read_final_peer_report_in_full': True,
    'peer_report_lines': len(full.splitlines()),
    'peer_body_exact_prefix_of_final_report': True,
    'manifest_entries_verified': [bind(e['path']) for e in manifest['entries']],
    'manifest_entry_count': 59,
    'complete_bound_closure_count': len(all_bound),
    'complete_bound_closure': [all_bound[k] for k in sorted(all_bound)],
    'root_independent_checks': 1088, 'peer_independent_checks': 1088,
    'peer_actual_TeX_formula_checks': 86,
    'root_read_complete_additional_parser_lines': 291,
    'exact_input_path_bijection_size_each': 12,
    'raw_output_byte_identity_claimed': False,
    'root_recomputed_complete_forward_and_inverse_output_identity_each': True,
    'root_recomputed_complete_peer_stdout_forward_and_inverse_identity': True,
    'source_changes_required': False, 'pdf_gate_completed': False,
    'scope': 'All finite affine marginal images on first character one and nontrivial total product, both original signs and every finite coefficient field; exact summed H1 injection, principal tuple kernel and rank6m+1. The arbitrary-first-character nonproduct case, full marginal equality and original interaction membership remain unresolved.',
}
out = ROOT/'work/root/final_new_claim_acceptance_271.json'
assert not out.exists()
out.write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps({'status': record['status'], 'claim': 'F.32',
                  'manifest_entries': 59, 'bound_closure': len(all_bound),
                  'checks_each': 1088, 'additional_TeX_checks': 86,
                  'acceptance': bind(out)}, indent=2))
