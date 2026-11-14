#!/usr/bin/env python3
"""Seal eight actual final625 views, 90 whole-PNG carries and four fragments."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re
import runpy

ROOT = Path(__file__).resolve().parents[3]
HELPER = ROOT/'work/part_c/code/seal_render_review_611.py'
helpers = runpy.run_path(str(HELPER))
bind, counts = helpers['bind'], helpers['counts']
assembled_comparison = helpers['assembled_comparison']
OUT = ROOT/'work/part_c/render_review_625.json'
PDF_HASH = '9d80a79e439f1928b2b7096cf9a6d5ec5ac1e01638b119c4872bf394ef635364'
TEX_HASH = 'a802cb776f0aaea062c2a80d2978bc4ac61d3a2c8feb2cf40da707d915986193'
VIEW_GROUPS = [[609,610],[615,616],[617,621],[622,625]]
OBSERVATIONS = {
    609: 'The F31 kernel/trace formulas and complete conclusion remain legible. The new F32 heading and opening character-locus formula F32.1 fit at the foot of this shared page, with clear separation and intact page number.',
    610: 'The F32 image statement, rank assertion, manuscript annotation and beginning of proof are clear. Scalar fields F32.3, coefficient maps F32.4-5 and boundary quotient F32.6 fit with legible exponents, fractions and tags.',
    615: 'The F32 summed-restriction conclusion, exact kernel F32.23, trace formula F32.24, affine reduction, literal positive/negative crossing formulas, certificate/continuity discussion and positive-sign transport are clear. Both inline crossing tuples fit; the proof ends cleanly.',
    616: 'References heading and entries1-8 are legible, with intact hanging labels, accents, italic titles, line wrapping and footer separation.',
    617: 'Reference8 continuation and entries9-15 are clear, including the detailed F7 source-scope discussion and mathematical symbols; no clipping or overlap.',
    621: 'References43-51 are clear, including long source descriptions and mathematical titles; labels and final footer spacing are intact.',
    622: 'References52-59 are legible, including the long descriptions, formulas and final continued entry, with intact paragraph and margin spacing.',
    625: 'The final bibliography continuation and reference77 are complete and legible. Final page number625 is clear; no clipped or overlapping text appears.',
}


def verify_binding(row):
    observed = bind(row['path'])
    assert observed['sha256'] == row['sha256'], row['path']
    if 'bytes' in row:
        assert observed['bytes'] == row['bytes'], row['path']
    return observed


def main():
    assert not OUT.exists(), 'Never overwrite a sealed review.'
    prep_path = ROOT/'work/root/render_preparation_625_final.json'
    prep = json.loads(prep_path.read_text())
    pages = [p for group in VIEW_GROUPS for p in group]
    assert pages == prep['peer_pages']
    assert len(pages) == len(set(pages)) == len(OBSERVATIONS) == 8
    assert prep['pages'] == 625 and prep['sha256'] == PDF_HASH
    assert prep['new_proof_pages']['F32'] == list(range(609,616))
    assert prep['shared_previous_and_new_proof_page'] == [609]
    assert prep['no_typesetting_edit_required_for_F32']
    pdf = bind(prep['pdf'])
    assert pdf['sha256'] == PDF_HASH and pdf['bytes'] == 4233896
    assert bind('deliverable/LM4_FINITE_GROUP_ACTIONS_paper.tex')['sha256'] == TEX_HASH
    assert len(prep['images']) == 102 and len(prep['root_pages']) == 94
    assert len({r['page'] for r in prep['images']}) == 102
    assert set(pages).isdisjoint(prep['root_pages'])

    prior_root_path = ROOT/'work/root/render_review_619.json'
    prior_root = json.loads(prior_root_path.read_text())
    assert bind(prior_root_path)['sha256'] == prep['prior_review_sha256'] == \
        '798efaa2f4066f49f18437bed1e3efb015945b6920562f635c0acb2f0cfc2235'
    assert prior_root['sha256'] == prep['prior_pdf_sha256'] == \
        '4546799ef3198a11c19a7b7a81e3d9a20aca2016c9f97633826fd971ffc02175'
    assert bind(prep['prior_pdf'])['sha256'] == prep['prior_pdf_sha256']
    prior_rows = {r['page']: r for r in prior_root['rendered_images']}
    prior_peer_path = ROOT/'work/part_c/render_review_619.json'
    prior_peer = json.loads(prior_peer_path.read_text())
    assert bind(prior_peer_path)['sha256'] == \
        'e1ee62c58e81aa0f0a64cfdf279287c05370e4ec9e539548bf576c11bd93d528'
    assert prior_root['independent_review_sha256'] == bind(prior_peer_path)['sha256']

    images, carries, all_bindings = [], [], []
    for record in prep['images']:
        observed = verify_binding(record)
        all_bindings.append({'page': record['page'], **observed})
        if record['byte_identical_to_prior_619_image']:
            old = prior_rows[record['page']]
            old_path = ROOT/record['prior_image']
            assert record['prior_review'] == str(prior_root_path.relative_to(ROOT))
            assert (ROOT/record['path']).read_bytes() == old_path.read_bytes()
            assert bind(old_path)['sha256'] == old['sha256'] == observed['sha256']
            assert bind(old_path)['bytes'] == old['bytes'] == observed['bytes']
            assert Path(old['path']).resolve() == old_path.resolve()
            assert record['page'] in prior_root['actually_viewed_pages']
            carries.append({**record, 'whole_png_bytes_compared': True,
                            'prior_sealed_review_entry_and_hash_verified': True,
                            'fresh_view_claimed_by_this_peer': False})
        if record['page'] in pages:
            assert record['reviewer'] == 'peer' and not record['byte_identical_to_prior_619_image']
            images.append({**record, 'actual_viewed': True,
                           'fresh_view_for_this_final_pdf': True, 'review_result': 'PASS',
                           'observation': OBSERVATIONS[record['page']]})
    assert len(carries) == 90 and [r['page'] for r in images] == pages
    carry_pages = {r['page'] for r in carries}
    assert carry_pages.issubset(prep['root_pages'])
    assert {491,492,493,494,495,496,596,598,599,600,601,602,603,604,605,606,607,608}.issubset(carry_pages)
    assert 609 not in carry_pages

    root_review_path = ROOT/'work/root/root_visual_review_625.json'
    root_review = json.loads(root_review_path.read_text())
    assert bind(root_review_path)['sha256'] == \
        'deb528643781c79f8f7291631c01611421cebd547a740c2128096767fece40ca'
    assert root_review['sha256'] == PDF_HASH and root_review['status'] == 'PASS'
    assert root_review['images_opened_this_final_review'] == [611,612,613,614]
    assert root_review['actual_view_calls'] == [[611,612],[613,614]]
    assert set(root_review['byte_identical_prior_review_pages']) == carry_pages
    assert root_review['render_preparation_sha256'] == bind(prep_path)['sha256']
    assert not root_review['issues']

    retained = []
    inventory_path = ROOT/'work/part_c/final_625_retained_evidence_inventory.json'
    for row in json.loads(inventory_path.read_text()):
        observed = verify_binding(row)
        assert (ROOT/row['source_path']).read_bytes() == (ROOT/row['path']).read_bytes()
        retained.append({**observed, 'source_path': row['source_path'],
                         'lines': len((ROOT/row['path']).read_text().splitlines()),
                         'read_in_full': True})
    assert len(retained) == 8
    log = (ROOT/'work/part_c/final_625_build.log').read_text()
    blg = (ROOT/'work/part_c/final_625_build.blg').read_text()
    stages = [(ROOT/f'work/part_c/final_625_stage_{i}_stdout.txt').read_text() for i in range(1,5)]
    assert len(log.splitlines()) == 1995 and len(blg.splitlines()) == 48
    assert [len(s.splitlines()) for s in stages] == [756,6,752,752]
    stage_counts = []
    for i, text in enumerate(stages,1):
        observed_counts = {'stage': i, **counts(text), 'bibtex_warnings': text.count('Warning--')}
        for key in ['overfull_boxes','missing_characters','undefined_control_sequences',
                    'undefined_reference_or_citation_lines','package_warning_lines',
                    'latex_font_warnings','fatal_error_lines']:
            assert observed_counts[key] == 0
        assert observed_counts['latex_warnings'] == observed_counts['label_rerun_warnings'] == (1 if i == 1 else 0)
        stage_counts.append(observed_counts)
    assert stages[2] == stages[3] and stages[0] != stages[2]
    final_counts = {**counts(log), 'bibtex_warnings': blg.count('Warning--')}
    expected = {key: 0 for key in final_counts}
    expected.update(underfull_hboxes=1, luaotfload_fallback_events=1,
                    generic_microtype_protrusion_notices=2, bibtex_warnings=1)
    assert final_counts == expected
    assert 'badness 7133' in log and 'lines 62--63' in log
    assert 'C_Tukia1972' in blg and 'has not \nchanged' in log
    assert '625 pages, 4233896 bytes' in log
    commands = json.loads((ROOT/'deliverable/build_commands.json').read_text())
    artifact = json.loads((ROOT/'deliverable/build_artifact.json').read_text())
    assert len(commands) == 4 and all(r['exit_code'] == 0 for r in commands)
    assert artifact['success'] and artifact['stage_count'] == 4 and artifact['pdf_sha256'] == PDF_HASH
    for name, digest in artifact['source_sha256'].items():
        assert bind('deliverable/'+name)['sha256'] == digest
    bib = (ROOT/'deliverable/LM4_FINITE_GROUP_ACTIONS_references.bib').read_text()
    bbl = (ROOT/'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.bbl').read_text()
    bib_count = len(re.findall(r'^@\w+\s*\{', bib, re.M))
    used = int(re.search(r"You've used (\d+) entries", blg).group(1))
    assert bib_count == 88 and used == bbl.count(r'\bibitem') == 77

    frozen = [verify_binding(row) for row in prior_peer['frozen_source_and_review_bindings_unchanged']]
    f32_review_path = ROOT/'work/part_c/review_f32.json'
    f32_review = json.loads(f32_review_path.read_text())
    assert bind(f32_review_path)['sha256'] == \
        'ba2ee61498b0af1ed906b3e16ee49b1a25e73447d6f0c763a65d162c50546ec1'
    frozen.extend(verify_binding(row) for row in f32_review['primary_bindings'])
    frozen.append(verify_binding(f32_review['report']))
    frozen.append(bind(f32_review_path))
    for entry in f32_review['evidence_manifest']['entry_checks']:
        verify_binding(entry)
    assembled = (ROOT/'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.tex').read_text()
    comparisons = {}
    for claim, stem, repair_name in [
        ('F.29','f_four_parameter_product_one_images','f29_typesetting_repair.json'),
        ('F.30','f_product_one_first_scalar_field_images',None),
        ('F.31','f_full_product_one_affine_images','f31_typesetting_repair.json'),
        ('F.32','f_nonproduct_first_character_one_images',None)]:
        repair = None
        if repair_name:
            repair_path = ROOT/'work/root'/repair_name
            old_key = 'assembly_'+claim.lower().replace('.','')+'_exact_comparison'
            assert bind(repair_path) == prior_peer[old_key]['root_typography_record']
            repair = json.loads(repair_path.read_text())
            if claim == 'F.31':
                repair = {**repair, 'frozen_fragment_unchanged_sha256': repair['proof_sha256']}
        comparison = assembled_comparison(claim, stem, assembled, repair)
        comparison['final_pages'] = prep['new_proof_pages'][claim.replace('.','')]
        comparison['whole_png_carry_pages'] = [
            p for p in comparison['final_pages'] if p in carry_pages]
        comparison['freshly_viewed_by_this_peer'] = [
            p for p in comparison['final_pages'] if p in pages]
        comparison['root_fresh_view_pages'] = [
            p for p in comparison['final_pages'] if p in [611,612,613,614]]
        comparison['frozen_proof_unchanged'] = True
        if repair_name:
            comparison.update(root_typography_record=bind(repair_path),
                              old=repair['old'], new=repair['new'], replacement_count=1,
                              historical_repair_record_preserved_unchanged=True)
        if claim != 'F.32':
            key = 'assembly_'+claim.lower().replace('.','')+'_exact_comparison'
            assert comparison['assembled_fragment_sha256'] == prior_peer[key]['assembled_fragment_sha256']
        else:
            assert comparison['frozen_source']['sha256'] == \
                'b91fd2611f1d9bd5cde096c6307004dca0fc740463971c164aa0fe52a146af13'
            comparison['no_typography_repair_required'] = True
        comparisons['assembly_'+claim.lower().replace('.','')+'_exact_comparison'] = comparison

    result = {
        'reviewer': '/root/c89_review_and_general_c',
        'review_scope': 'Eight actual fresh final625 views, all90 complete-PNG carries from sealed619, full final LaTeX/BibTeX logs and all four outputs/records, and exact reversible F29-F32 assembly comparisons.',
        'status': 'PASS', 'sealed_at_utc': datetime.now(timezone.utc).isoformat(),
        'pdf': {**pdf, 'pages': 625, 'claims_in_parent_build': 271},
        'render_preparation': bind(prep_path), 'total_parent_selection_pages': 102,
        'root_assigned_pages_count': 94, 'peer_assigned_pages_count': 8,
        'peer_freshly_viewed_pages': pages, 'peer_reused_without_fresh_view_pages': [],
        'actual_image_view_groups_in_order': VIEW_GROUPS, 'maximum_images_per_view_call': 2,
        'no_unviewed_page_certified': True, 'images': images,
        'visual_findings': {
            'defects_found': [], 'reference_samples_freshly_viewed': [616,617,621,622,625],
            'F31_F32_shared_changed_page_freshly_viewed': 609,
            'F32_actual_proof_pages': list(range(609,616)),
            'F32_peer_fresh_view_pages': [609,610,615],
            'F32_root_fresh_view_pages': [611,612,613,614],
            'F32_root_review_binding': bind(root_review_path),
            'F7_scope_pages_byte_identical_to_reviewed_619': [491,492,493,494,495,496],
            'F29_25_repaired_page_byte_identical_to_reviewed_619': 596,
            'F31_repaired_negative_crossing_page_byte_identical_to_reviewed_619': 603},
        'parent_selection_counts_from_preparation': {
            'total': 102, 'root': 94, 'peer': 8, 'prior_whole_png_carries': 90,
            'fresh_root': 4, 'fresh_peer': 8, 'fresh_total': 12},
        'all_selected_image_hashes_independently_verified': all_bindings,
        'whole_png_carry_audit': {
            'count': 90, 'prior_aggregate_review': bind(prior_root_path),
            'prior_peer_review': bind(prior_peer_path),
            'prior_pdf_snapshot': bind(prep['prior_pdf']),
            'comparison_method': 'Complete PNG byte equality, exact current/prior SHA256 and length, exact prior image path, and membership/hash in the sealed aggregate619 actual-view chain.',
            'entries': carries, 'all_passed': True,
            'new_visual_views_claimed_for_carries': False},
        'entire_final_build_logs_and_all_four_stage_outputs_read': True,
        'retained_log_copies': retained,
        'retained_evidence_inventory': bind(inventory_path),
        'four_stage_commands': commands, 'all_four_exit_codes_zero': True,
        'stage_1_3_4_stdout_byte_identical': False, 'stage_3_4_stdout_byte_identical': True,
        'stage_output_notice_counts': stage_counts, 'final_log_notice_counts': final_counts,
        'notice_interpretations': [
            'One inherited underfull hbox, badness7133, at source lines62-63 in the opening notation table; page1 is an exact whole-PNG carry from sealed619.',
            'One inherited luaotfload-main lookup failure and OT1 fallback per LuaLaTeX run; fontenc/lmodern subsequently load T1 Latin Modern and the final log lists the embedded Type1 fonts.',
            'Two informational microtype generic protrusion notices in the final log, for T1/lmtt and OT1/lmss.',
            'One inherited BibTeX warning: C_Tukia1972 has a number but no volume.',
            'Stage1 has one label-rerun notice. Stages3 and4 have none and their complete stdout byte strings are identical; final .out unchanged. No final undefined-reference/citation, LaTeX/package/font, overfull, missing-character or fatal issue.'],
        'bibliography_record_count': bib_count, 'bibtex_used_entries': used,
        'printed_bibliography_entries': 77,
        'build_source_bindings': [bind('deliverable/'+name) for name in [
            'LM4_FINITE_GROUP_ACTIONS_paper.tex',
            'LM4_FINITE_GROUP_ACTIONS_references.bib',
            'LM4_FINITE_GROUP_ACTIONS_paper.bbl']],
        **comparisons,
        'frozen_source_and_review_bindings_unchanged': frozen,
        'review_writer': bind(Path(__file__).resolve()),
        'reused_review_helpers': bind(HELPER),
        'no_frozen_source_or_final_pdf_edits': True,
    }
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'record': bind(OUT), 'fresh_pages': pages,
                      'whole_png_carries': 90, 'all_selected_images': 102,
                      'complete_forward_and_inverse_fragment_comparisons': ['F.29','F.30','F.31','F.32'],
                      'final_notice_counts': final_counts}, indent=2))


if __name__ == '__main__':
    main()
