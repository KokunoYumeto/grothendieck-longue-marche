#!/usr/bin/env python3
"""Bind the completed independent mathematical reviews before registering F30."""
from pathlib import Path
from hashlib import sha256
import json
import re

ROOT = Path(__file__).resolve().parents[2]
stem = 'work/part_a/f_product_one_first_scalar_field_images'
expected = {
    stem+'.tex': '1703a98c06269ec8ad73cdd5e420f7213ba620e06a6dcc104905447566a613f5',
    stem+'_results.json': '80fe630dac50268185f2541c2e31af18357c0377476cf08f2101da2bdcbd7024',
    stem+'_report.txt': 'f56d55b085decabd05bc311dc63abf490fcad6093480418fdc735ac2761fb4ed',
    stem+'_evidence_manifest.json': 'b0c06fce03242c96486fe51a1e1f18a19e7c1fa6886feace48db75a391f37d3e',
    'work/part_c/review_f30.txt': 'd25df8152c9a8a60b315cf1861514f58b14df3f16c11bd6fee10c813054e75e8',
    'work/part_c/review_f30.json': '4f8823a9be1532dc08d7c5af9e60cba6d52572e9060ef6fe7a219d22ef5bf467',
    'work/part_c/f30_independent_replay/comparison.json': '2da069c3c20c705a8580076c6dfd32482ed4c1a6e41385c9cb68088e7b1e738d',
}

def bind(path):
    p = Path(path)
    p = p if p.is_absolute() else ROOT/p
    return {'path': str(p.relative_to(ROOT)), 'bytes': p.stat().st_size,
            'sha256': sha256(p.read_bytes()).hexdigest()}

for path, value in expected.items():
    assert bind(path)['sha256'] == value, path
proof = (ROOT/(stem+'.tex')).read_text()
assert len(proof.splitlines()) == 376
assert re.findall(r'\\tag\{F\.30\.(\d+)\}', proof) == [str(x) for x in range(1, 16)]
metadata = json.loads((ROOT/(stem+'_results.json')).read_text())
assert metadata['id'] == 'F.30' and metadata['status'] == 'Proved'
manifest = json.loads((ROOT/(stem+'_evidence_manifest.json')).read_text())
assert len(manifest['entries']) == 37
verified = []
for entry in manifest['entries']:
    actual = bind(entry['path'])
    assert actual['bytes'] == entry['bytes'] and actual['sha256'] == entry['sha256'], entry['path']
    verified.append(actual)
peer = json.loads((ROOT/'work/part_c/review_f30.json').read_text())
assert peer['status'] == 'PASS' and peer['complete_proof_read']
assert peer['manifest_entry_count_verified'] == 37
assert not peer['mathematical_corrections_requested'] and not peer['source_files_edited']
root_replay = json.loads((ROOT/'work/root/f30_independent_replay/comparison.json').read_text())
peer_replay = json.loads((ROOT/'work/part_c/f30_independent_replay/comparison.json').read_text())
for replay in [root_replay, peer_replay]:
    assert replay['status'] == 'PASS' and replay['checks'] == 45
    assert not replay['raw_byte_identical']
    assert len(replay['exact_five_input_path_bijection']) == 5
    assert replay['path_transported_output_byte_identical']
assert peer_replay['all_original_inputs_unchanged_after_replay']
result = {
    'status': 'PASS_ROOT_AND_PEER', 'claim': 'F.30',
    'proof_sha256': expected[stem+'.tex'], 'proof_lines': 376,
    'numbered_displays': 15,
    'frozen_artifacts': [bind(p) for p in expected],
    'root_mathematical_audit': bind('work/root/review_f30.txt'),
    'root_read_peer_report_in_full': True,
    'peer_report_lines': len((ROOT/'work/part_c/review_f30.txt').read_text().splitlines()),
    'manifest_entries_verified': verified, 'manifest_entry_count': 37,
    'root_replay': bind('work/root/f30_independent_replay/comparison.json'),
    'peer_replay': bind('work/part_c/f30_independent_replay/comparison.json'),
    'root_independent_checks': 45, 'peer_independent_checks': 45,
    'source_changes_required': False, 'pdf_gate_completed': False,
    'scope': 'The complete product-one character theorem on the exact field-generation locus k0=k1(chi(Y1)), both actual signs and every original finite coefficient field. The general product-one locus and the original full marginal and interaction comparisons remain unresolved.'
}
(ROOT/'work/root/final_new_claim_acceptance_269.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({'status': result['status'], 'claim': 'F.30',
                  'manifest_entries': 37, 'checks_each': 45,
                  'proof_unchanged': True}, indent=2))
