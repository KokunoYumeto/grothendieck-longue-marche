#!/usr/bin/env python3
"""Seal the completed root/peer reviews and preserve the exact published PDF."""
from pathlib import Path
from hashlib import sha256
import json
import re

ROOT = Path(__file__).resolve().parents[2]

def bind(name):
    p = ROOT / name
    return {'path': name, 'bytes': p.stat().st_size,
            'sha256': sha256(p.read_bytes()).hexdigest()}

def verify(entry):
    actual = bind(entry['path'])
    assert all(actual[k] == entry[k] for k in ('bytes', 'sha256')), entry['path']
    return actual

def verify_tree(value, checked):
    if isinstance(value, dict):
        if all(k in value for k in ('path', 'bytes', 'sha256')):
            checked[value['path']] = verify(value)
        for child in value.values():
            verify_tree(child, checked)
    elif isinstance(value, list):
        for child in value:
            verify_tree(child, checked)

def write_record(name, data):
    p = ROOT / name
    content = json.dumps(data, indent=2) + '\n'
    if p.exists():
        assert p.read_text() == content, name
    else:
        p.write_text(content)
    return bind(name)

# Preserve a byte-exact published baseline before any next assembly.
pdf = 'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.pdf'
review = 'work/root/render_review_611.json'
assert bind(pdf)['sha256'] == '6eb08722ef726aaa8894facf55915238861d7981c9d86d63cdc62e6e7dc47a97'
assert bind(review)['sha256'] == 'a6025bedd581aee6e46b67d367707d7cf7808faef06f7f4b002d47cfb94647cf'
snapshot = ROOT / 'work/root/prior_269_snapshot'
snapshot.mkdir(exist_ok=True)
target = snapshot / 'paper.pdf'
if target.exists():
    assert target.read_bytes() == (ROOT/pdf).read_bytes()
else:
    target.write_bytes((ROOT/pdf).read_bytes())
snapshot_record = write_record('work/root/prior_269_snapshot/binding.json', {
    'status': 'EXACT_PUBLISHED_PDF_PRESERVED',
    'source': 'Published checkpoint269; native version29; all final611 visual and build gates complete',
    'pages': 611, **bind('work/root/prior_269_snapshot/paper.pdf'),
    'review': review, 'review_sha256': bind(review)['sha256']})

# Actual class-two note: both full readings and both isolated replays completed.
dmeta_name = 'work/part_d_attack/actual_transporter_class_two_and_gt0_result.json'
dpeer_name = 'work/part_c/actual_transporter_class_two_peer_review/review.json'
dmeta = json.loads((ROOT/dmeta_name).read_text())
dpeer = json.loads((ROOT/dpeer_name).read_text())
assert bind(dmeta_name)['sha256'] == 'b9b0d1a47c04a6a3994152d602a3d20c6d41fe8d4ffc40489da610ee5f2d9926'
assert bind(dpeer_name)['sha256'] == '29fdda593406a1dd3729af053ac746df693f9f01c3ad977abce195800597dfde'
assert dpeer['verdict'] == 'PASS'
assert not dpeer['mathematical_corrections_requested'] and not dpeer['program_corrections_requested']
assert not dpeer['frozen_files_modified']
checked_d = {}
verify_tree(dmeta, checked_d)
verify_tree(dpeer, checked_d)
dr_name = 'work/root/actual_class_two_independent_replay/comparison.json'
dr = json.loads((ROOT/dr_name).read_text())
assert dr['status'] == 'PASS' and dr['named_checks'] == 38
assert dr['raw_output_and_stdout_byte_identical'] and dr['all_frozen_files_unchanged']
for obj in [dr, dpeer['isolated_replay']]:
    assert obj['coordinate_formula_cases'] == 144824
    assert obj['sign_identity_cases'] == 17892
assert dpeer['isolated_replay']['whole_output_and_stdout_raw_byte_identity']
verify_tree(dr, checked_d)
drecord = write_record('work/root/actual_class_two_acceptance_270.json', {
    'status': 'PASS_ROOT_AND_PEER', 'numbered_claim_added': False,
    'proof_lines': 229, 'program_lines': 132, 'root_read_peer_report_in_full': True,
    'peer_report_lines': 183,
    'root_review': bind('work/root/review_actual_transporter_class_two_and_gt0.txt'),
    'author_metadata': bind(dmeta_name), 'peer_review': bind(dpeer_name),
    'root_replay': bind(dr_name),
    'source_program_output_dependency_and_replay_bindings_verified': list(checked_d.values()),
    'named_checks_each': 38, 'coordinate_formula_cases_each': 144824,
    'sign_identity_cases_each': 17892,
    'raw_output_and_stdout_byte_identical_each': True,
    'author_pending_fields_preserved_as_historical': True,
    'scope': 'Exact original full class-two coordinates and inverse maps; actual GT0 order-three lift and transporter word; d=-3t; all prime-coordinate root sets with explicit roots at 2 and 3. No full word zero or all-prime nonemptiness is asserted.'})

# Filled carriers: root full prior-source reading plus every exact clarification.
cstem = 'work/part_c/compact_family_filled_carriers_and_expansions'
cmeta_name = cstem+'_result.json'
cpeer_name = 'work/part_d_attack/review_compact_family_filled_carriers.json'
cmeta = json.loads((ROOT/cmeta_name).read_text())
cpeer = json.loads((ROOT/cpeer_name).read_text())
build = json.loads((ROOT/(cstem+'_build/build_result.json')).read_text())
assert bind(cmeta_name)['sha256'] == '0a5e287ece53e2039202f6815f7ec46c88e683f20881298e6fbfff1965f56f17'
assert bind(cpeer_name)['sha256'] == '923aa35caab8fd0dd5a5b59c6b1fbb32de94d9f58c8a8c019a784e8a935d1fe7'
assert cpeer['disposition'] == 'PASS' and not cpeer['corrections_requested']
assert cpeer['full_final_mathematical_source_read']
assert not cpeer['frozen_source_or_author_files_modified']
before = (ROOT/build['before']['path']).read_text()
after = (ROOT/build['source']['path']).read_text()
replacements = build['clarification_replacements']
assert len(replacements) == 6
forward = before
for replacement in replacements:
    assert forward.count(replacement['old']) == 1
    forward = forward.replace(replacement['old'], replacement['new'], 1)
assert forward == after
inverse = after
for replacement in reversed(replacements):
    assert inverse.count(replacement['new']) == 1
    inverse = inverse.replace(replacement['new'], replacement['old'], 1)
assert inverse == before
assert len(before.splitlines()) == 344 and len(after.splitlines()) == 348
assert re.findall(r'\\tag\{FCE\.(\d+)\}', after) == [str(i) for i in range(1,16)]
wrapper = (ROOT/build['wrapper']['path']).read_text()
assert wrapper.split('\\begin{document}\n',1)[1].rsplit('\\end{document}',1)[0].rstrip() == after.rstrip()
checked_c = {}
verify_tree(cmeta, checked_c)
verify_tree(cpeer, checked_c)
verify_tree(build, checked_c)
assert cmeta['visual_review']['pages_actually_viewed'] == [1,2,3,4]
assert cmeta['visual_review']['all_pages_clear'] and not cmeta['visual_review']['defects']
assert cmeta['build']['full_final_log']['read_in_full']
for k in ['overfull_boxes','underfull_boxes','missing_characters','undefined_control_sequences','undefined_references_or_citations','fatal_errors']:
    assert cmeta['build']['final_notice_counts'][k] == 0
crecord = write_record('work/root/filled_carriers_acceptance_270.json', {
    'status': 'PASS_ROOT_AND_PEER', 'numbered_claim_added': False,
    'root_prior_source_read_lines': 344, 'final_source_lines': 348,
    'root_full_clarification_diff_read': True, 'root_full_author_report_read': True,
    'root_full_peer_report_read': True,
    'exact_replacements': replacements,
    'complete_forward_and_inverse_source_byte_comparisons': True,
    'exact_standalone_wrapper_body_verified': True,
    'root_review': bind('work/root/review_compact_family_filled_carriers.txt'),
    'author_metadata': bind(cmeta_name), 'peer_review': bind(cpeer_name),
    'source_report_build_visual_and_dependency_bindings_verified': list(checked_c.values()),
    'author_four_page_visual_gate_verified': True, 'root_new_visual_review_claimed': False,
    'author_pending_fields_preserved_as_historical': True,
    'scope': 'Actual filled-carrier identities, finite controlled fixed-region expansion with exact inverses and both displacement bounds, actual radial nullhomotopy, and the exact one-stage deck-step obstruction. The original global noncompact deformation remains unresolved.'})
print(json.dumps({'status':'PASS','published611_snapshot':snapshot_record,
                  'class_two_acceptance':drecord,'filled_carrier_acceptance':crecord},indent=2))
