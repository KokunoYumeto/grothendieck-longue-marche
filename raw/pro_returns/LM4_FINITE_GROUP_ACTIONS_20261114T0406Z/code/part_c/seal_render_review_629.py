#!/usr/bin/env python3
"""Seal eight actual final629 views, 96 whole-PNG carries and five fragments."""
from datetime import datetime, timezone
from pathlib import Path
import json
import re
import runpy

ROOT = Path(__file__).resolve().parents[3]
HELPER = ROOT / 'work/part_c/code/seal_render_review_611.py'
helpers = runpy.run_path(str(HELPER))
bind, counts = helpers['bind'], helpers['counts']
assembled_comparison = helpers['assembled_comparison']
OUT = ROOT / 'work/part_c/render_review_629.json'
REPORT = ROOT / 'work/part_c/render_review_629.txt'
PDF_HASH = '693902ed60a12a9ef5d26160d56cac7b96b9ff9cde034b4f02f9b41231b2871d'
TEX_HASH = 'e1528a9249bb5c6806becea9c3bc5d90c07446d5ad0a9e084bac8113a6db9cbc'
PREP_HASH = '8cd7fd459a308a42d0853af378f6525a71a66f3b737074d109b9afc86958f86c'
VIEW_GROUPS = [[615, 616], [619, 620], [621, 625], [626, 629]]
OBSERVATIONS = {
    615: 'The changed F32 conclusion page is clear: kernel F32.23, trace F32.24, both inline crossing tuples, certificate and continuity discussion, positive-sign transport and proof square fit within the margins with an intact footer.',
    616: 'The F33 heading and claim, exact paired kernel F33.2, all-field matrix domain, manuscript passage, source and character F33.3, seeds F33.4, complete 64-word order F33.5 and coefficient ring F33.6 are clear, legible and unclipped.',
    619: 'The F33 H1 conclusion, literal-word audit, positive crossing tuple F33.18, negative crossing tuple, certificate counts, based sign maps F33.19 and proof conclusion are clear. Tags and exponents fit; the lower whitespace follows the completed proof.',
    620: 'References heading and entries 1-8 are clear, including labels, accents, italic titles, hanging paragraphs and footer separation.',
    621: 'Reference 8 continuation and entries 9-15, including detailed F7 source scopes and mathematical symbols, are clear and fit within the margins.',
    625: 'References 43-51 and their long journal and source descriptions are legible with intact labels, margins and footer.',
    626: 'References 52-59, including long descriptions and formulas, are clear. The final continued entry and page footer have normal spacing.',
    629: 'The continuation of reference 76 and final reference 77 are complete and clear. Final page number 629 is intact; the remaining whitespace follows the end of the bibliography.',
}


def verify_binding(row):
    observed = bind(row['path'])
    assert observed['sha256'] == row['sha256'], row['path']
    if 'bytes' in row:
        assert observed['bytes'] == row['bytes'], row['path']
    return observed


def main():
    assert not OUT.exists() and not REPORT.exists(), 'Never overwrite a sealed review.'
    prep_path = ROOT / 'work/root/render_preparation_629_final.json'
    prep = json.loads(prep_path.read_text())
    assert bind(prep_path)['sha256'] == PREP_HASH
    pages = [p for group in VIEW_GROUPS for p in group]
    assert pages == prep['peer_pages']
    assert len(pages) == len(set(pages)) == len(OBSERVATIONS) == 8
    assert prep['pages'] == 629 and prep['sha256'] == PDF_HASH
    assert prep['new_proof_pages']['F33'] == list(range(616, 620))
    assert prep['no_typesetting_edit_required_for_F33']
    pdf = bind(prep['pdf'])
    assert pdf['sha256'] == PDF_HASH and pdf['bytes'] == 4257801
    assert bind('deliverable/LM4_FINITE_GROUP_ACTIONS_paper.tex')['sha256'] == TEX_HASH
    assert len(prep['images']) == 106 and len(prep['root_pages']) == 98
    assert len({r['page'] for r in prep['images']}) == 106
    assert set(pages).isdisjoint(prep['root_pages'])

    prior_root_path = ROOT / 'work/root/render_review_625.json'
    prior_root = json.loads(prior_root_path.read_text())
    assert bind(prior_root_path)['sha256'] == prep['prior_review_sha256'] == \
        'a5f7b890a3a04d2993d555293325bd32be6ad3a019e6f3e52927059212f90bb5'
    assert prior_root['sha256'] == prep['prior_pdf_sha256'] == \
        '9d80a79e439f1928b2b7096cf9a6d5ec5ac1e01638b119c4872bf394ef635364'
    assert bind(prep['prior_pdf'])['sha256'] == prep['prior_pdf_sha256']
    prior_rows = {r['page']: r for r in prior_root['rendered_images']}
    prior_peer_path = ROOT / 'work/part_c/render_review_625.json'
    prior_peer = json.loads(prior_peer_path.read_text())
    assert bind(prior_peer_path)['sha256'] == \
        '1ae0fe2e6babe0594653e7120e8d2dd24200aa93c88d3258018a74b78384e58a'
    assert prior_root['independent_review_sha256'] == bind(prior_peer_path)['sha256']

    images, carries, all_bindings = [], [], []
    for record in prep['images']:
        observed = verify_binding(record)
        all_bindings.append({'page': record['page'], **observed})
        if record['byte_identical_to_prior_625_image']:
            old = prior_rows[record['page']]
            old_path = ROOT / record['prior_image']
            assert record['prior_review'] == str(prior_root_path.relative_to(ROOT))
            assert (ROOT / record['path']).read_bytes() == old_path.read_bytes()
            assert bind(old_path)['sha256'] == old['sha256'] == observed['sha256']
            assert bind(old_path)['bytes'] == old['bytes'] == observed['bytes']
            assert Path(old['path']).resolve() == old_path.resolve()
            assert record['page'] in prior_root['actually_viewed_pages']
            carries.append({**record, 'whole_png_bytes_compared': True,
                            'prior_sealed_review_entry_and_hash_verified': True,
                            'fresh_view_claimed_by_this_peer': False})
        if record['page'] in pages:
            assert record['reviewer'] == 'peer' and not record['byte_identical_to_prior_625_image']
            images.append({**record, 'actual_viewed': True,
                           'fresh_view_for_this_final_pdf': True, 'review_result': 'PASS',
                           'observation': OBSERVATIONS[record['page']]})
    assert len(carries) == 96 and [r['page'] for r in images] == pages
    carry_pages = {r['page'] for r in carries}
    assert carry_pages.issubset(prep['root_pages'])
    assert set(range(591, 615)).issubset(carry_pages)
    assert {1, 491, 492, 493, 494, 495, 496}.issubset(carry_pages)
    assert 615 not in carry_pages

    root_review_path = ROOT / 'work/root/root_visual_review_629.json'
    root_review = json.loads(root_review_path.read_text())
    assert bind(root_review_path)['sha256'] == \
        '61b08122ac0eb3d90d126eb19d068cac4e4ca8c8eadbc09fa89985a66a9c74ab'
    assert root_review['sha256'] == PDF_HASH and root_review['status'] == 'PASS'
    assert root_review['images_opened_this_final_review'] == [617, 618]
    assert root_review['actual_view_calls'] == [[617, 618]]
    assert set(root_review['byte_identical_prior_review_pages']) == carry_pages
    assert root_review['render_preparation_sha256'] == PREP_HASH
    assert not root_review['issues']

    retained = []
    inventory_path = ROOT / 'work/part_c/final_629_retained_evidence_inventory.json'
    for row in json.loads(inventory_path.read_text()):
        observed = verify_binding(row)
        assert (ROOT / row['source_path']).read_bytes() == (ROOT / row['path']).read_bytes()
        retained.append({**observed, 'source_path': row['source_path'],
                         'lines': len((ROOT / row['path']).read_text().splitlines()),
                         'read_in_full': True})
    assert len(retained) == 8
    log = (ROOT / 'work/part_c/final_629_build.log').read_text()
    blg = (ROOT / 'work/part_c/final_629_build.blg').read_text()
    stages = [(ROOT / f'work/part_c/final_629_stage_{i}_stdout.txt').read_text() for i in range(1, 5)]
    assert len(log.splitlines()) == 2003 and len(blg.splitlines()) == 48
    assert [len(s.splitlines()) for s in stages] == [760, 6, 756, 756]
    stage_counts = []
    for i, text in enumerate(stages, 1):
        observed_counts = {'stage': i, **counts(text), 'bibtex_warnings': text.count('Warning--')}
        for key in ['overfull_boxes', 'missing_characters', 'undefined_control_sequences',
                    'undefined_reference_or_citation_lines', 'package_warning_lines',
                    'latex_font_warnings', 'fatal_error_lines']:
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
    assert '629 pages, 4257801 bytes' in log
    commands = json.loads((ROOT / 'deliverable/build_commands.json').read_text())
    artifact = json.loads((ROOT / 'deliverable/build_artifact.json').read_text())
    assert len(commands) == 4 and all(r['exit_code'] == 0 for r in commands)
    assert artifact['success'] and artifact['stage_count'] == 4 and artifact['pdf_sha256'] == PDF_HASH
    for name, digest in artifact['source_sha256'].items():
        assert bind('deliverable/' + name)['sha256'] == digest
    bib = (ROOT / 'deliverable/LM4_FINITE_GROUP_ACTIONS_references.bib').read_text()
    bbl = (ROOT / 'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.bbl').read_text()
    bib_count = len(re.findall(r'^@\w+\s*\{', bib, re.M))
    used = int(re.search(r"You've used (\d+) entries", blg).group(1))
    assert bib_count == 89 and used == bbl.count(r'\bibitem') == 77

    frozen = [verify_binding(row) for row in prior_peer['frozen_source_and_review_bindings_unchanged']]
    f33_review_path = ROOT / 'work/part_c/review_f33.json'
    f33_review = json.loads(f33_review_path.read_text())
    assert bind(f33_review_path)['sha256'] == \
        'd3c2da9e4ba0f452f337438004baed16bb49d836133c86bcd3a59c03f7ae1fbb'
    frozen.extend(verify_binding(row) for row in f33_review['author'].values())
    frozen.extend(verify_binding(f33_review[key]) for key in ['report', 'mathematical_body', 'binding_audit', 'sealer'])
    frozen.append(bind(f33_review_path))
    manifest = json.loads((ROOT / f33_review['author']['_evidence_manifest.json']['path']).read_text())
    assert len(manifest['entries']) == manifest['entry_count'] == 69
    evidence_checks = [verify_binding(entry) for entry in manifest['entries']]

    assembled = (ROOT / 'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.tex').read_text()
    comparisons = {}
    for claim, stem, repair_name in [
        ('F.29', 'f_four_parameter_product_one_images', 'f29_typesetting_repair.json'),
        ('F.30', 'f_product_one_first_scalar_field_images', None),
        ('F.31', 'f_full_product_one_affine_images', 'f31_typesetting_repair.json'),
        ('F.32', 'f_nonproduct_first_character_one_images', None),
        ('F.33', 'f_quadratic_sign_pair_restriction', None)]:
        repair = None
        key = 'assembly_' + claim.lower().replace('.', '') + '_exact_comparison'
        if repair_name:
            repair_path = ROOT / 'work/root' / repair_name
            assert bind(repair_path) == prior_peer[key]['root_typography_record']
            repair = json.loads(repair_path.read_text())
            if claim == 'F.31':
                repair = {**repair, 'frozen_fragment_unchanged_sha256': repair['proof_sha256']}
        comparison = assembled_comparison(claim, stem, assembled, repair)
        comparison['final_pages'] = prep['new_proof_pages'][claim.replace('.', '')]
        comparison['whole_png_carry_pages'] = [p for p in comparison['final_pages'] if p in carry_pages]
        comparison['freshly_viewed_by_this_peer'] = [p for p in comparison['final_pages'] if p in pages]
        comparison['root_fresh_view_pages'] = [p for p in comparison['final_pages'] if p in [617, 618]]
        comparison['frozen_proof_unchanged'] = True
        if repair_name:
            comparison.update(root_typography_record=bind(repair_path),
                              old=repair['old'], new=repair['new'], replacement_count=1,
                              historical_repair_record_preserved_unchanged=True)
        else:
            comparison['no_typography_repair_required'] = True
        if claim != 'F.33':
            assert comparison['assembled_fragment_sha256'] == prior_peer[key]['assembled_fragment_sha256']
        else:
            assert comparison['frozen_source']['sha256'] == \
                '8a2cd87d9139c6e2bccd99cc9bb8db53883d064da5653fd804e2e2457ab96037'
        comparisons[key] = comparison

    notices = [
        'One inherited underfull hbox, badness 7133, at source lines 62-63 in the opening notation table; page 1 is an exact whole-PNG carry from sealed625.',
        'One inherited luaotfload-main lookup failure and OT1 fallback per LuaLaTeX run; fontenc/lmodern subsequently load T1 Latin Modern and the final log lists the embedded Type1 fonts.',
        'Two informational microtype generic protrusion notices in the final log, for T1/lmtt and OT1/lmss.',
        'One inherited BibTeX warning: C_Tukia1972 has a number but no volume.',
        'Stage 1 has one label-rerun notice. Stages 3 and 4 have none and their complete stdout byte strings are identical; final .out unchanged. No final undefined-reference/citation, LaTeX/package/font, overfull, missing-character or fatal issue.',
    ]
    report_lines = [
        'INDEPENDENT FINAL629 PDF AND BUILD REVIEW',
        'Reviewer: /root/c89_review_and_general_c', 'Verdict: PASS', '',
        f'PDF: {pdf["path"]}', f'SHA256: {PDF_HASH}',
        '629 pages; 4,257,801 bytes; checkpoint 272.',
        f'Final TeX SHA256: {TEX_HASH}', f'Render preparation SHA256: {PREP_HASH}',
        f'Root visual record SHA256: {bind(root_review_path)["sha256"]}', '',
        '1. ACTUAL VIEWS AND PREVIOUSLY VIEWED IMAGE TRANSPORT',
        'Actual peer view calls, with at most two images per call: ' + json.dumps(VIEW_GROUPS),
        'All eight assigned fresh images were actually viewed. No defect was found.',
        'Root independently viewed pages 617 and 618, bound by its sealed record.',
        'All 106 selected image hashes and byte lengths were independently checked.',
        'For each of the 96 carried images, I compared the complete current PNG',
        'bytes with the previous PNG, both SHA256 values and lengths, the exact',
        'previous path, and the entry in the sealed final625 actual-view chain.',
        'The previous PDF snapshot and aggregate/peer review hashes were checked.',
        'I do not claim a new visual opening for any carried image or root image.',
        'Counts: root 98 = 96 carries + 2 fresh; peer 8 fresh; total 106.', '',
    ]
    for row in images:
        report_lines.extend([f'Page {row["page"]}: {row["observation"]}',
                             f'  PNG: {row["path"]}', f'  SHA256: {row["sha256"]}', ''])
    report_lines.extend(['2. COMPLETE BUILD EVIDENCE',
        'I read the complete 2,003-line final LaTeX log, 48-line BibTeX log,',
        'all four stdout files (760, 6, 756 and 756 lines), and both build records.',
        'All four stages exited zero. The eight retained copies equal their',
        'final source files byte for byte. Stage 3 and stage 4 stdout are identical.',
        'The bibliography has 89 records and 77 used/printed entries.', ''])
    report_lines.extend(notices)
    report_lines.append('')
    for row in retained:
        report_lines.extend([row['path'], f'  Source: {row["source_path"]}',
                             f'  SHA256: {row["sha256"]}; {row["bytes"]} bytes; {row["lines"]} lines.'])
    report_lines.extend(['', '3. FIVE COMPLETE REVERSIBLE ASSEMBLY MAPS',
        'For each frozen proof F29-F33, I formed the complete forward fragment,',
        'compared it with the exact complete assembled claim/proof fragment,',
        'then applied the inverse and compared every recovered proof byte.',
        'Each passage map removes the one final period from manuscript_passages,',
        'wraps the remaining text in the passage macro and inserts that line',
        'plus two newlines immediately after the claim terminator newline.',
        'Its inverse removes that exact insertion and restores the metadata period.',
        'The only typography maps are the established F29 gathered-row break',
        'and F31 allowbreak token. Both original repair records remain unchanged.',
        'F30, F32 and F33 require only their exact passage insertion.', ''])
    for key, row in comparisons.items():
        report_lines.extend([key, f'  Frozen source SHA256: {row["frozen_source"]["sha256"]}',
            f'  Frozen metadata SHA256: {row["frozen_metadata"]["sha256"]}',
            f'  Assembled whole-fragment SHA256: {row["assembled_fragment_sha256"]}',
            '  Whole forward and inverse comparisons: PASS.',
            f'  Final pages: {row["final_pages"]}; typography replacements: {row["typography_repair_count"]}.'])
        if 'old' in row:
            report_lines.extend(['  Exact old string: ' + json.dumps(row['old']),
                                 '  Exact new string: ' + json.dumps(row['new'])])
    report_lines.extend(['', '4. FROZEN SOURCE SCOPE',
        'All inherited frozen source/review bindings and the final F33 author',
        'files, complete review and 69-entry evidence manifest verify unchanged.',
        'The F33 matrix and paired-cocycle domains remain exactly those of the',
        'accepted proof. This PDF review introduces no mathematical scope change.',
        'No frozen source, prior review, historical repair record or final PDF',
        'was edited in this review. The accompanying JSON retains all 106 image',
        'bindings, all 96 carry comparisons, all log counts and every exact map.', ''])
    REPORT.write_text('\n'.join(report_lines))

    result = {
        'reviewer': '/root/c89_review_and_general_c',
        'review_scope': 'Eight actual fresh final629 views, all 96 complete-PNG carries from sealed625, full final LaTeX/BibTeX logs and all four outputs/records, and exact reversible F29-F33 assembly comparisons.',
        'status': 'PASS', 'sealed_at_utc': datetime.now(timezone.utc).isoformat(),
        'report': bind(REPORT), 'pdf': {**pdf, 'pages': 629, 'claims_in_parent_build': 272},
        'render_preparation': bind(prep_path), 'total_parent_selection_pages': 106,
        'root_assigned_pages_count': 98, 'peer_assigned_pages_count': 8,
        'peer_freshly_viewed_pages': pages, 'peer_reused_without_fresh_view_pages': [],
        'actual_image_view_groups_in_order': VIEW_GROUPS, 'maximum_images_per_view_call': 2,
        'no_unviewed_page_certified': True, 'images': images,
        'visual_findings': {
            'defects_found': [], 'reference_samples_freshly_viewed': [620, 621, 625, 626, 629],
            'F32_changed_conclusion_page_freshly_viewed': 615,
            'F33_actual_proof_pages': list(range(616, 620)),
            'F33_peer_fresh_view_pages': [616, 619], 'F33_root_fresh_view_pages': [617, 618],
            'F33_root_review_binding': bind(root_review_path),
            'F7_scope_pages_byte_identical_to_reviewed_625': [491, 492, 493, 494, 495, 496],
            'F29_25_repaired_page_byte_identical_to_reviewed_625': 596,
            'F31_repaired_negative_crossing_page_byte_identical_to_reviewed_625': 603},
        'parent_selection_counts_from_preparation': {
            'total': 106, 'root': 98, 'peer': 8, 'prior_whole_png_carries': 96,
            'fresh_root': 2, 'fresh_peer': 8, 'fresh_total': 10},
        'all_selected_image_hashes_independently_verified': all_bindings,
        'whole_png_carry_audit': {
            'count': 96, 'prior_aggregate_review': bind(prior_root_path),
            'prior_peer_review': bind(prior_peer_path), 'prior_pdf_snapshot': bind(prep['prior_pdf']),
            'comparison_method': 'Complete PNG byte equality, exact current/prior SHA256 and length, exact prior image path, and membership/hash in the sealed aggregate625 actual-view chain.',
            'entries': carries, 'all_passed': True, 'new_visual_views_claimed_for_carries': False},
        'entire_final_build_logs_and_all_four_stage_outputs_read': True,
        'retained_log_copies': retained, 'retained_evidence_inventory': bind(inventory_path),
        'four_stage_commands': commands, 'all_four_exit_codes_zero': True,
        'stage_1_3_4_stdout_byte_identical': False, 'stage_3_4_stdout_byte_identical': True,
        'stage_output_notice_counts': stage_counts, 'final_log_notice_counts': final_counts,
        'notice_interpretations': notices, 'bibliography_record_count': bib_count,
        'bibtex_used_entries': used, 'printed_bibliography_entries': 77,
        'build_source_bindings': [bind('deliverable/' + name) for name in [
            'LM4_FINITE_GROUP_ACTIONS_paper.tex', 'LM4_FINITE_GROUP_ACTIONS_references.bib',
            'LM4_FINITE_GROUP_ACTIONS_paper.bbl']],
        **comparisons, 'frozen_source_and_review_bindings_unchanged': frozen,
        'f33_manifest_entries_verified_unchanged': evidence_checks,
        'review_writer': bind(Path(__file__).resolve()), 'reused_review_helpers': bind(HELPER),
        'no_frozen_source_or_final_pdf_edits': True,
    }
    OUT.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': 'PASS', 'record': bind(OUT), 'report': bind(REPORT),
                      'fresh_pages': pages, 'whole_png_carries': 96, 'all_selected_images': 106,
                      'complete_forward_and_inverse_fragment_comparisons': ['F.29', 'F.30', 'F.31', 'F.32', 'F.33'],
                      'final_notice_counts': final_counts}, indent=2))


if __name__ == '__main__':
    main()
