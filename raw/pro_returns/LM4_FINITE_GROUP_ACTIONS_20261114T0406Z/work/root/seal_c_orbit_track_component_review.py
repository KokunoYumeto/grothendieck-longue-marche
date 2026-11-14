#!/usr/bin/env python3
"""Seal both complete mathematical reviews of the paired finite C construction."""
from pathlib import Path
from hashlib import sha256
import datetime
import json

ROOT = Path(__file__).resolve().parents[2]
sha = lambda p: sha256(p.read_bytes()).hexdigest()
def binding(name):
    p = ROOT / name
    return {'path': name, 'bytes': p.stat().st_size, 'sha256': sha(p)}
def write_new(name, value):
    p = ROOT / name
    assert not p.exists(), str(p)
    p.write_text(json.dumps(value, indent=2) + '\n')
    return binding(name)

expected = {
    'work/part_c/compact_family_orbit_track_research.txt': 'a503f9cf0ade2f3e61d3c316a102dcdb5400cbe391db526e2c0a6da89a0a1241',
    'work/part_c/compact_family_orbit_track_component_witness.txt': 'ef6924382ddeb22e287df37995e850e4df530b43f64167694d81d77e3779e2b3',
    'work/part_c/orbit_track_primary_review/primary_review.json': '938251f0bcf819aecc55dfd2f147e17233c5a0009a081b5da9afdc796b4ecf49',
    'work/part_a/review_c_orbit_track_component_witness.txt': 'c5ab4fa8952ad367c9d8d1cc92e1a7a47fbd8beca273fc3a058718e013f2e441',
    'work/part_a/review_c_orbit_track_component_witness.json': 'f8b365f7344fe3d1315185bfd76bf1c3f7ba24950c32e611b6f68ea3672c4ec7'}
for name, digest in expected.items(): assert sha(ROOT / name) == digest, name
peer = json.loads((ROOT / 'work/part_a/review_c_orbit_track_component_witness.json').read_text())
primary = json.loads((ROOT / 'work/part_c/orbit_track_primary_review/primary_review.json').read_text())
assert peer['status'] == 'INDEPENDENT_MATHEMATICAL_PEER_PASS_NO_CORRECTION'
assert peer['input_count'] == len(peer['inputs']) == 15
assert not peer['corrections_requested'] and not peer['author_files_modified']
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
verify(peer)
verify(primary)
for name in expected:
    bound[name] = binding(name)
for name in ['work/root/review_c_orbit_track_component_witness.txt',
             'work/root/initial_fixed_region_continuation_acceptance.json',
             'work/root/filled_carriers_acceptance_270.json']:
    bound[name] = binding(name)

# Preserve the exact current published paper and view chain for later appends.
snapshot = ROOT / 'work/root/prior_271_snapshot'
snapshot.mkdir(exist_ok=True)
original_pdf = ROOT / 'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.pdf'
original_review = ROOT / 'work/root/render_review_625.json'
assert sha(original_pdf) == '9d80a79e439f1928b2b7096cf9a6d5ec5ac1e01638b119c4872bf394ef635364'
assert sha(original_review) == 'a5f7b890a3a04d2993d555293325bd32be6ad3a019e6f3e52927059212f90bb5'
for source, target in [(original_pdf, snapshot / 'paper.pdf'), (original_review, snapshot / 'render_review.json')]:
    assert not target.exists()
    target.write_bytes(source.read_bytes())
    assert target.read_bytes() == source.read_bytes()
snapshot_binding = write_new('work/root/prior_271_snapshot/binding.json', {
    'checkpoint': 271, 'published_library_version': 31, 'pdf_pages': 625,
    'original_pdf': binding('deliverable/LM4_FINITE_GROUP_ACTIONS_paper.pdf'),
    'archived_pdf': binding('work/root/prior_271_snapshot/paper.pdf'),
    'original_review': binding('work/root/render_review_625.json'),
    'archived_review': binding('work/root/prior_271_snapshot/render_review.json'),
    'whole_pdf_and_review_byte_identity': True})
record = {
    'status': 'ACCEPTED_UNNUMBERED_CONTINUATION_ROOT_AND_PEER_PASS',
    'sealed_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'numbered_claim_registered': False, 'published_checkpoint_modified': False,
    'root_full_author_source_lines_read': [216, 225],
    'root_full_primary_record_lines_read': 57, 'root_full_peer_report_lines_read': 301,
    'root_actual_primary_view_groups': [[85, 86], [105]],
    'root_primary_read_scope': 'Epstein1.7 full statement/proof;1.8 full statement/proof on85-86;A1 statement and initial disk-extension paragraph on105. Newman169 not inspected.',
    'parameter_scope': 'Compact connected finite CW spaces with a specified basepoint, including S^n for n>=1, in the original fixed-region setup.',
    'accepted_scope': 'Actual small full-Q-orbit restriction homotopy and its original-circle variable-image inverse; explicit finite ambient correction and exact relative-(X union {y}) component witness, retaining every original sheet and deck label.',
    'retained_target': 'An ambient displacement bound from the original common C0 envelope, quantitative successive vertex/edge/cycle stages and the controlled infinite deformation.',
    'mathematical_corrections_requested': [], 'numerical_replay_claimed': False,
    'binding_count': len(bound), 'bindings': [bound[k] for k in sorted(bound)],
    'published_pdf_preserved': snapshot_binding,
    'sealed_by': binding('work/root/seal_c_orbit_track_component_review.py')}
out = write_new('work/root/orbit_track_component_continuation_acceptance.json', record)
print(json.dumps({'status': record['status'], 'binding_count': len(bound),
                  'acceptance': out, 'snapshot': snapshot_binding}, indent=2))
