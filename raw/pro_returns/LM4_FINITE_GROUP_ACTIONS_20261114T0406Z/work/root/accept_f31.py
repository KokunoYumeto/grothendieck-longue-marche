#!/usr/bin/env python3
"""Accept the frozen full product-one proof after complete root/peer review."""
from pathlib import Path
from hashlib import sha256
import json
import re

ROOT = Path(__file__).resolve().parents[2]
stem = 'work/part_a/f_full_product_one_affine_images'
expected = {
    stem+'.tex': '909cb42466354ecebfede5b5d27077381d13e87f9261ea62180dc507cf91c345',
    stem+'_results.json': 'e74ccba7fc9b7eb5743e20490af3ede5c924341d791539933b0d278b0261f547',
    stem+'_report.txt': '84dffb91eded382d3dd79201a56665ad0f567bc32b5d45e850905f4f8e9ca49e',
    stem+'_evidence_manifest.json': '35e49d3b7a55c5cde795481e0103044874441709e95f3211f097b9163b2ced98',
    'work/root/review_f31.txt': 'fe189b5a95525492f13c18d3d6397b88e2a36e5f9e6766242250e26f6521c6db',
    'work/part_c/review_f31.txt': 'e074079e42d7efe319cf9a300632ae349acb70e6378706a5db49fda64f198447',
    'work/part_c/review_f31.json': 'e2e3b24eb352c3e20fe6fd936e03ae4f12d8082f83450a1896c442ae9570bb79',
    'work/root/f31_independent_replay/comparison.json': 'a5d3a7b405c7b5bd218a8f744853d94bb75ba975fc0c7a95794f4f0b6dca8f54',
    'work/part_c/f31_independent_replay/comparison.json': 'e0040984113b7bc3bb0239ac03a9154fcfb992d57c617c06cce9c6ed06476665',
}

def bind(name):
    p = Path(name)
    p = p if p.is_absolute() else ROOT/p
    return {'path': str(p.relative_to(ROOT)), 'bytes': p.stat().st_size,
            'sha256': sha256(p.read_bytes()).hexdigest()}

for path, digest in expected.items():
    assert bind(path)['sha256'] == digest, path
proof = (ROOT/(stem+'.tex')).read_text()
assert len(proof.splitlines()) == 885
assert re.findall(r'\\tag\{F\.31\.(\d+)\}', proof) == [str(i) for i in range(1,31)]
meta = json.loads((ROOT/(stem+'_results.json')).read_text())
assert meta['id'] == 'F.31' and meta['status'] == 'Proved'
manifest = json.loads((ROOT/(stem+'_evidence_manifest.json')).read_text())
assert len(manifest['entries']) == 54
verified = []
for entry in manifest['entries']:
    actual = bind(entry['path'])
    assert all(actual[k] == entry[k] for k in ['bytes','sha256']), entry['path']
    verified.append(actual)
assert len({entry['path'] for entry in verified}) == 54
peer = json.loads((ROOT/'work/part_c/review_f31.json').read_text())
assert peer['status'] == 'PASS_INDEPENDENT_F31_FULL_PROOF_CODE_EVIDENCE_AND_REPLAY_REVIEW'
assert peer['proof_full_read_lines'] == 885 and peer['checker_full_read_lines'] == 421
assert peer['evidence_manifest_entry_count'] == 54 and peer['all_manifest_entries_exact']
assert not peer['corrections_requested'] and not peer['mathematical_issues']
assert peer['all_completed_earlier_sources_unchanged']
root_replay = json.loads((ROOT/'work/root/f31_independent_replay/comparison.json').read_text())
peer_replay = json.loads((ROOT/'work/part_c/f31_independent_replay/comparison.json').read_text())
assert root_replay['status'] == 'PASS' and root_replay['checks'] == 1603
assert root_replay['module_checks'] == 977 and root_replay['reviewed_word_and_parser_checks'] == 626
assert not root_replay['raw_byte_identical']
assert len(root_replay['exact_ten_input_path_bijection']) == 10
assert len(root_replay['inverse_bijection']) == 10
assert root_replay['path_transported_output_byte_identical']
assert root_replay['inverse_transport_recovers_entire_replay']
assert root_replay['all_original_inputs_unchanged_after_replay']
assert peer_replay['status'] == 'PASS_F31_UNCHANGED_ISOLATED_LITERAL_WORD_REPLAY'
assert peer_replay['total_exact_checks'] == 1603 and peer_replay['copied_input_count'] == 10
assert peer_replay['whole_output_bytes_equal_after_exact_key_transport']
assert peer_replay['stdout_transport']['whole_bytes_equal_after_transport']
assert peer_replay['all_original_files_unchanged_after_replay']
body = (ROOT/'work/part_c/f31_peer_review_body.txt').read_bytes()
full = (ROOT/'work/part_c/review_f31.txt').read_bytes()
assert full.startswith(body)
record = {
    'status': 'PASS_ROOT_AND_PEER', 'claim': 'F.31',
    'proof_sha256': expected[stem+'.tex'], 'proof_lines': 885,
    'numbered_displays': 30, 'checker_lines': 421,
    'producer_lines': [156,106,128,138],
    'frozen_artifacts': [bind(p) for p in expected],
    'root_mathematical_audit': bind('work/root/review_f31.txt'),
    'root_read_final_author_metadata_and_report_in_full': True,
    'root_read_final_peer_report_in_full': True,
    'peer_report_lines': len(full.splitlines()),
    'peer_body_exact_prefix_of_final_report': True,
    'manifest_entries_verified': verified, 'manifest_entry_count': 54,
    'root_independent_checks': 1603, 'peer_independent_checks': 1603,
    'exact_input_path_bijection_size_each': 10,
    'raw_output_byte_identity_claimed': False,
    'complete_output_identity_after_exact_path_bijection_each': True,
    'root_inverse_bijection_recovers_entire_replay': True,
    'source_changes_required': False, 'pdf_gate_completed': False,
    'scope': 'All product-one characters for the actual marginal inclusions, both original signs and all finite coefficient fields; exact summed H1 restriction and cocycle kernel of rank6m+1. General characters with chi(P0) different from one, full marginal equality and original interaction membership remain unresolved.'}
out = ROOT/'work/root/final_new_claim_acceptance_270.json'
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status': record['status'], 'claim':'F.31',
                  'manifest_entries':54,'checks_each':1603,
                  'acceptance_sha256':sha256(out.read_bytes()).hexdigest()},indent=2))
