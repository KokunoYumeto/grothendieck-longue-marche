#!/usr/bin/env python3
"""Seal the actual final629 views, whole-image carries and reversible source maps."""
from pathlib import Path
from hashlib import sha256
import datetime
import json

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'deliverable'
sha = lambda p: sha256(p.read_bytes()).hexdigest()
read = lambda name: json.loads((ROOT / name).read_text())
def binding(name):
    p = ROOT / name
    return {'path': name, 'bytes': p.stat().st_size, 'sha256': sha(p)}
def verify(item):
    p = Path(item['path'])
    p = p if p.is_absolute() else ROOT / p
    assert p.stat().st_size == item['bytes'] and sha(p) == item['sha256'], str(p)
    return p

prep_name = 'work/root/render_preparation_629_final.json'
root_name = 'work/root/root_visual_review_629.json'
peer_name = 'work/part_c/render_review_629.json'
prior_name = 'work/root/render_review_625.json'
prep, root, peer, prior = [read(x) for x in [prep_name, root_name, peer_name, prior_name]]
qa, build = read('deliverable/pdf_qa.json'), read('deliverable/build_artifact.json')
pdf = OUT / 'LM4_FINITE_GROUP_ACTIONS_paper.pdf'
expected = '693902ed60a12a9ef5d26160d56cac7b96b9ff9cde034b4f02f9b41231b2871d'
assert sha(pdf) == expected == prep['sha256'] == root['sha256'] == peer['pdf']['sha256']
assert qa['sha256'] == build['pdf_sha256'] == expected
assert sha(ROOT / peer_name) == '28cf30c44d8b34892b5b4cd9b973c00018710562f72aa5fe502c7f60c871a40f'
assert sha(ROOT / root_name) == '61b08122ac0eb3d90d126eb19d068cac4e4ca8c8eadbc09fa89985a66a9c74ab'
assert sha(ROOT / prior_name) == root['prior_review_sha256']
assert build['success'] and build['stage_count'] == 4
assert qa['pages'] == peer['pdf']['pages'] == 629 and pdf.stat().st_size == peer['pdf']['bytes']
assert peer['status'] == 'PASS' and not peer['visual_findings']['defects_found']
assert not root['issues'] and not qa['overfull_widths_pt']
assert peer['entire_final_build_logs_and_all_four_stage_outputs_read']
assert peer['all_four_exit_codes_zero'] and peer['stage_3_4_stdout_byte_identical']
assert not peer['stage_1_3_4_stdout_byte_identical']
assert (OUT / 'build_stage_3_stdout.txt').read_bytes() == (OUT / 'build_stage_4_stdout.txt').read_bytes()
assert (OUT / 'build_stage_1_stdout.txt').read_bytes() != (OUT / 'build_stage_4_stdout.txt').read_bytes()
assert root['actually_viewed_pages'] == prep['root_pages']
assert peer['peer_freshly_viewed_pages'] == prep['peer_pages']
assert peer['whole_png_carry_audit']['all_passed'] and peer['whole_png_carry_audit']['count'] == 96
for key in ['overfull_boxes', 'missing_characters', 'undefined_control_sequences',
            'undefined_reference_or_citation_lines', 'latex_warnings', 'package_warning_lines',
            'latex_font_warnings', 'fatal_error_lines', 'label_rerun_warnings']:
    assert peer['final_log_notice_counts'][key] == 0
prior_images = {x['page']: x for x in prior['rendered_images']}
peer_images = {x['page']: x for x in peer['images']}
images = []
for item in prep['images']:
    p = verify(item)
    if item['reviewer'] == 'peer':
        q = peer_images[item['page']]
        assert q['actual_viewed'] and q['fresh_view_for_this_final_pdf']
        assert q['sha256'] == item['sha256'] and q['bytes'] == item['bytes']
    elif item['byte_identical_to_prior_625_image']:
        old = prior_images[item['page']]
        old_path = verify(old)
        assert item['page'] in prior['actually_viewed_pages']
        assert old['sha256'] == item['sha256'] and old['bytes'] == item['bytes']
        assert p.read_bytes() == old_path.read_bytes()
    else:
        assert item['page'] in root['images_opened_this_final_review']
    images.append(dict(item, path=str(p)))
pages = [x['page'] for x in images]
assert len(pages) == len(set(pages)) == 106
assert len(root['images_opened_this_final_review']) == 2
assert len(peer['peer_freshly_viewed_pages']) == 8
assert len(root['byte_identical_prior_review_pages']) == 96
for item in peer['retained_log_copies']:
    copied = verify(item)
    assert item['read_in_full'] and (ROOT / item['source_path']).read_bytes() == copied.read_bytes()
for item in peer['frozen_source_and_review_bindings_unchanged'] + peer['build_source_bindings']:
    verify(item)

# Re-execute all five complete forward and inverse maps at root.
paper = (OUT / 'LM4_FINITE_GROUP_ACTIONS_paper.tex').read_bytes()
source_comparisons = {}
for label, repairs in [('f29', 1), ('f30', 0), ('f31', 1), ('f32', 0), ('f33', 0)]:
    comp = peer['assembly_' + label + '_exact_comparison']
    assert comp['entire_forward_fragment_equals_assembled_fragment']
    assert comp['entire_inverse_fragment_equals_frozen_proof']
    source = verify(comp['frozen_source']).read_bytes()
    meta = json.loads(verify(comp['frozen_metadata']).read_text())
    passage = '\\passage{' + meta['manuscript_passages'].removesuffix('.') + '}'
    assert passage == comp['exact_added_passage_line']
    assert comp['typography_repair_count'] == repairs
    transformed = source
    if repairs:
        verify(comp['root_typography_record'])
        old, new = comp['old'].encode(), comp['new'].encode()
        assert transformed.count(old) == 1 and transformed.count(new) == 0
        transformed = transformed.replace(old, new, 1)
    terminator = b'\\end{claim}'
    insertion = terminator + b'\n' + passage.encode() + b'\n'
    assert transformed.count(terminator) == 1
    transformed = transformed.replace(terminator, insertion, 1)
    assert paper.count(transformed) == 1, label
    assert sha256(transformed).hexdigest() == comp['assembled_fragment_sha256']
    inverse = transformed.replace(insertion, terminator, 1)
    if repairs:
        inverse = inverse.replace(new, old, 1)
    assert inverse == source, label
    source_comparisons[label] = {
        'entire_forward_fragment_equals_assembled_fragment': True,
        'entire_inverse_fragment_equals_frozen_proof': True,
        'comparison_is_complete_bytes': True,
        'assembled_fragment_sha256': sha256(transformed).hexdigest(),
        'typography_repair_count': repairs}

gates = []
proofs = {
    'f29': ('f_four_parameter_product_one_images', 268, range(591, 599)),
    'f30': ('f_product_one_first_scalar_field_images', 269, range(598, 602)),
    'f31': ('f_full_product_one_affine_images', 270, range(602, 610)),
    'f32': ('f_nonproduct_first_character_one_images', 271, range(609, 616)),
    'f33': ('f_quadratic_sign_pair_restriction', 272, range(616,620))}
for label, (stem, checkpoint, proof_pages) in proofs.items():
    selected = list(proof_pages)
    record = {
        'status': 'PASS_FINAL_DOCUMENT_GATE', 'claim': label.upper().replace('F', 'F.'),
        'pdf_sha256': expected, 'pdf_pages': 629,
        'accepted_proof': binding('work/part_a/' + stem + '.tex'),
        'mathematical_acceptance': binding('work/root/final_new_claim_acceptance_' + str(checkpoint) + '.json'),
        'root_complete_source_comparison': source_comparisons[label],
        'peer_review': binding(peer_name), 'root_review': binding(root_name),
        'final_page_images': [x for x in images if x['page'] in selected],
        'whole_png_carry_pages': [p for p in selected if p in root['byte_identical_prior_review_pages']],
        'root_fresh_pages': [p for p in selected if p in root['images_opened_this_final_review']],
        'peer_fresh_pages': [p for p in selected if p in peer['peer_freshly_viewed_pages']],
        'overfull_boxes': 0, 'issues': []}
    assert len(record['final_page_images']) == len(selected)
    if label in ['f29', 'f31']:
        record['status'] = 'PASS_FINAL_DOCUMENT_AND_TYPOGRAPHY_GATE'
        record['immutable_initial_repair'] = binding('work/root/' + label + '_typesetting_repair.json')
        previous = 'f29_typesetting_final_gate_625.json' if label == 'f29' else 'f31_final_document_gate_625.json'
        record['sealed_prior_completion'] = binding('work/root/' + previous)
    name = 'f29_typesetting_final_gate_629.json' if label == 'f29' else label + '_final_document_gate_629.json'
    destination = ROOT / 'work/root' / name
    assert not destination.exists()
    destination.write_text(json.dumps(record, indent=2) + '\n')
    gates.append(binding('work/root/' + name))

review = {
    'pdf': pdf.name, 'sha256': expected, 'pages': 629, 'pdf_bytes': pdf.stat().st_size,
    'actually_viewed_pages': pages, 'actually_viewed_count': 106,
    'root_actually_viewed_pages': prep['root_pages'], 'peer_actually_viewed_pages': prep['peer_pages'],
    'root_images_opened_this_final_review': root['images_opened_this_final_review'],
    'peer_images_opened_this_final_review': peer['peer_freshly_viewed_pages'],
    'byte_identical_prior_review_images': root['byte_identical_prior_review_pages'],
    'prior_review': prior_name, 'prior_review_sha256': sha(ROOT / prior_name),
    'prior_pdf': binding('work/root/prior_271_snapshot/paper.pdf'),
    'root_review': root_name, 'root_review_sha256': sha(ROOT / root_name),
    'independent_review': peer_name, 'independent_review_sha256': sha(ROOT / peer_name),
    'render_preparation': prep_name, 'render_preparation_sha256': sha(ROOT / prep_name),
    'reviewed_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'method': 'Root actually viewed2 final PNGs and peer actually viewed8. Ninety-six further entire PNGs equal previously viewed sealed625 images byte for byte; both reviewers independently checked complete size, digest, bytes and prior-view membership. All106 current images are bound to the final629 PDF. Rendering alone is not counted as viewing.',
    'new_proof_coverage': prep['new_proof_pages'], 'scope_overview_coverage': prep['scope_overview_pages'],
    'historical_overflow_widths_pt': qa['historical_overflow_widths_pt'],
    'historical_passages_reviewed': prep['historical_passages'], 'current_document_gates': gates,
    'log_review': {
        'stages_passed': 4, 'overfull_boxes': 0, 'overfull_greater_than_2pt': 0,
        'missing_glyphs': 0, 'undefined_references_or_citations': 0, 'fatal_errors': 0,
        'final_lualatex_log_read': True, 'bibtex_log_read': True,
        'full_log_reader': 'c89_review_and_general_c; root checked diagnostic and exact-file bindings.',
        'full_log_review_record': peer_name,
        'final_log_sha256': sha(OUT / 'LM4_FINITE_GROUP_ACTIONS_paper.log'),
        'final_bibtex_log_sha256': sha(OUT / 'LM4_FINITE_GROUP_ACTIONS_paper.blg'),
        'diagnostic_counts': peer['final_log_notice_counts'], 'nonfatal_notices': peer['notice_interpretations'],
        'stage_1_3_4_stdout_byte_identical': False, 'stage_3_4_stdout_byte_identical': True,
        'bibliographic_warning_scope': 'Tukia Series A I number504 has no invented volume.',
        'bibliography_records': 89, 'cited_printed_entries': 77},
    'visual_observations': 'All four F33 proof pages were freshly viewed, including the exact original source and coefficient maps, full gauge and inverse, four charts, all50 printed pivots, the terminal block, paired inverse and exact kernel/H1 conclusions. The changed end of F32 and five bibliography samples were freshly viewed. All inherited selected passages, including the notation concordance and both F29/F31 repairs, have complete-PNG carry or a fresh actual view.',
    'issues': [], 'rendered_images': images}
destination = ROOT / 'work/root/render_review_629.json'
assert not destination.exists()
destination.write_text(json.dumps(review, indent=2) + '\n')
(OUT / 'render_review.json').write_bytes(destination.read_bytes())
print(json.dumps({'pdf_sha256': expected, 'reviewed_pages': 106, 'root_fresh': 2,
    'peer_fresh': 8, 'whole_image_byte_identical_carry': 96,
    'complete_reversible_fragment_maps': 5, 'review_sha256': sha(destination)}, indent=2))
