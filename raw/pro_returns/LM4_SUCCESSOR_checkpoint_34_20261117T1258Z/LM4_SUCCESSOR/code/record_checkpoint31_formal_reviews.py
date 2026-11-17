"""Bind the ten final complete root and independent source reviews."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root = Path(__file__).resolve().parents[1]
specs = [
 ('A.92','work_A/A92_common_word_odd_heads_proposed.tex','sections/a_common_word_odd_heads.tex','381c0bb5a22b110f930a4afd044ab823f612d8699411098cebf0897f506ef9e4'),
 ('A.93','work_A/A93_canonical_three_module_boundary_proposed.tex','sections/a_canonical_three_module_boundary.tex','cf8a88d1201b9a17b2ee4a65817f7efc859b2ad2b2ed9eb12723d6779015cb75'),
 ('A.94','work_A/A94_affine_character_pentagon_proposed.tex','sections/a_affine_character_pentagon.tex','6b5901d89caa328fa0bc47e8a22fff587e4db7b9a1a86a4af24e984715cbf79e'),
 ('B.148','work_CE/B148_actual_stabilizer_normalization_proposed.tex','sections/b_actual_stabilizer_normalization.tex','f576a0281ab1ba191f8335c48a948d608ee4e3a65069748fd8445df7d0557fa8'),
 ('B.149','work_CE/B149_full_stabilizer_marked_section_proposed.tex','sections/b_full_stabilizer_marked_section.tex','6f0948892dfe4cc95321a869d521578449d24b0911352035dbb00b2a25f06a8d'),
 ('B.150','work_CE/B150_remaining_contact_kernel_proposed.tex','sections/b_remaining_contact_kernel.tex','8ffe1019e6d86be8017fad8bd49ddaec8f3a2b92d6e7853cf744485588ded0c4'),
 ('B.151','work_DE/B151_one_sided_family_extension_proposed.tex','sections/b_one_sided_family_extension.tex','3977034db5a4bf8ad203033fd9826d040504f96b76097631ca340152aaeb1644'),
 ('B.152','work_DE/B152_mirrored_neck_preservation_proposed.tex','sections/b_mirrored_neck_preservation.tex','cd80f7650ec63674ef0dbcfc1391017d3f8d97affdd3e6b5123606faed66012e'),
 ('B.153','work_CE/B153_compact_one_family_stabilizer_proposed.tex','sections/b_compact_one_family_stabilizer.tex','aa5968f0630349aa466dcceb51532f9e8649719bb030fd631481bcbd4026c4c8'),
 ('B.154','work_CE/B154_fixed_source_topology_section_proposed.tex','sections/b_fixed_source_topology_section.tex','2c980eed6ced5e6976ff2d87d7e3dbcee9b937853ecf11edec460089c1040c32'),
]
independent_paths = [
 'work_DE/next_marginal_source/review_A92_A93_A94_formal31.md',
 'work_DE/next_marginal_source/review_A92_B154_final_token_repairs31.md',
 'work_DE/next_marginal_source/review_A92_B154_final_token_repairs31.json',
 'work_A/review_B148_B154_formal31.md',
 'work_A/review_B148_B154_formal31.json',
 'work_CE/review_B151_B152_formal31.txt',
 'work_CE/review_B151_B152_formal31.json',
 'work_CE/review_A92_final_notation31.txt',
 'work_CE/review_A92_final_notation31.json',
]
sha = lambda path: hashlib.sha256((root / path).read_bytes()).hexdigest()
copies = []
for sid, source, target, digest in specs:
    data = (root / source).read_bytes()
    assert sha(source) == digest
    assert not any(c < 32 and c not in (9, 10) for c in data)
    assert ('\\statement{' + sid + '}{Proved}').encode() in data
    copies.append({'statement':sid, 'source':source, 'target':target,
                   'sha256':digest, 'root_entire_final_source_read':True})
binding = json.loads((root / 'work_A/review_B148_B154_formal31.json').read_text())
assert binding['verdict'] == 'PASS' and binding['entire_formal_source_read']
assert {(row['path'],row['sha256']) for row in binding['sources']} == {
    (row['source'],row['sha256']) for row in copies if row['statement'].startswith('B.')}
record = {
 'recorded_at':datetime.now(timezone.utc).isoformat(),
 'status':'PASS_COMPLETE_SOURCE_REVIEW',
 'copies':copies,
 'independent_reviews':{path:sha(path) for path in independent_paths},
 'root_review_scope':'Every complete final source was actually read, including the entire corrected A92, A93, A94 and B154; all arguments and stated limits passed. Literal notation predecessors and their repair diffs are retained.',
 'main_A':'Open', 'main_B':'Open',
 'primary_binding':'A94 uses the exact retained Cohen/Furusho marking audit. Final B153 uses the explicit actual cocycle and finite-index free bases and does not depend on the separate geometric/CSP primary investigation.',
 'no_private_build_or_render_at_review':True,
}
out = root / 'records/checkpoint31_root_formal_reviews.json'
assert not out.exists()
out.write_text(json.dumps(record,indent=2)+'\n')
print('PASS: ten complete final root reviews and exact independent bindings.')
