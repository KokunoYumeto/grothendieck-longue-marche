#!/usr/bin/env python3
"""Seal ten actual final619 views, 82 entire-PNG carries, and final build review."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re
import runpy

ROOT = Path(__file__).resolve().parents[3]
HELPER = ROOT / 'work/part_c/code/seal_render_review_611.py'
helpers = runpy.run_path(str(HELPER))
bind = helpers['bind']
counts = helpers['counts']
assembled_comparison = helpers['assembled_comparison']
OUT = ROOT / 'work/part_c/render_review_619.json'
PDF_HASH = '4546799ef3198a11c19a7b7a81e3d9a20aca2016c9f97633826fd971ffc02175'
VIEW_GROUPS = [[601,606],[607,608],[609,610],[611,615],[616,619]]
OBSERVATIONS = {
    601: 'The changed preceding F30 conclusion displays the summed restriction, inverse intertwiners, kernel/rank/trace conclusion and positive-sign transport clearly. Its proof ends here; F31 starts on page602.',
    606: 'F31.18 principal X3 quotient, F31.19 inverse basis/quotient, F31.20 block and F31.21-22 four eigenrows/unit determinant are clear. Dense entries and tags fit; the F31.19 tag on its separate lower line is legible.',
    607: 'The core/type comparisons, signs F31.23, coefficient map F31.24, extended rows F31.25 and unique boundary-lift argument are clear. The sentence continuation on page608 is intact.',
    608: 'All fifteen sign-table rows in F31.26 are legible, including their sign tuples, vectors, selected sources, coordinates and residuals. The nonzero-factor discussion, summed restriction F31.27 and inverse intertwiners F31.28 fit clearly.',
    609: 'The exact kernel F31.29, trace formula F31.30, affine reduction, certificate/continuity discussion, positive-sign transport and proof ending are clear.',
    610: 'The References heading and entries1-8 are legible, with clear wrapping, mathematical symbols, accents and margins.',
    611: 'References9-15 and the continued entry are clear, including the source discussion of F7 scope; no clipping or overlap appears.',
    615: 'References43-51 are clear, with intact labels, mathematical titles, paragraph breaks and footer spacing.',
    616: 'References52-59 are legible, including long source descriptions, formulas and the final continued entry.',
    619: 'The final bibliography continuation and entry77 are complete and legible; the final page number is intact and the remaining whitespace is unobstructed.',
}

def verify_binding(row):
    actual = bind(row['path'])
    assert all(actual[k] == row[k] for k in actual)
    return actual

def main():
    assert not OUT.exists(), 'Never overwrite a sealed review.'
    prep_path = ROOT/'work/root/render_preparation_619_final.json'
    prep = json.loads(prep_path.read_text())
    pages = [p for group in VIEW_GROUPS for p in group]
    assert pages == prep['peer_pages']
    assert len(pages) == len(set(pages)) == len(OBSERVATIONS) == 10
    assert prep['pages'] == 619 and prep['sha256'] == PDF_HASH
    assert prep['new_proof_pages']['F31'] == list(range(602,610))
    assert prep['adjacent_changed_pages'] == [601]
    pdf = bind(prep['pdf'])
    assert pdf['sha256'] == PDF_HASH and pdf['bytes'] == 4194159
    assert len(prep['images']) == 96 and len(prep['root_pages']) == 86
    assert set(pages).isdisjoint(prep['root_pages'])
    assert len({r['page'] for r in prep['images']}) == 96

    prior_root_path = ROOT/'work/root/render_review_611.json'
    prior_root = json.loads(prior_root_path.read_text())
    assert bind(prior_root_path)['sha256'] == prep['prior_review_sha256']
    assert prior_root['sha256'] == prep['prior_pdf_sha256']
    assert bind(prep['prior_pdf'])['sha256'] == prep['prior_pdf_sha256']
    prior_rows = {r['page']:r for r in prior_root['rendered_images']}
    prior_peer_path = ROOT/'work/part_c/render_review_611.json'
    prior_peer = json.loads(prior_peer_path.read_text())
    assert bind(prior_peer_path)['sha256'] == 'a3b34404998973913fb4e4c3afd8d748bd9cbdb1770c1405e74730f614887cb4'
    assert prior_root['independent_review_sha256'] == bind(prior_peer_path)['sha256']
    images, carries, all_bindings = [], [], []
    for record in prep['images']:
        actual = verify_binding(record)
        all_bindings.append({'page':record['page'], **actual})
        if record['byte_identical_to_prior_611_image']:
            old = prior_rows[record['page']]
            prior_image = ROOT/record['prior_image']
            assert record['prior_review'] == str(prior_root_path.relative_to(ROOT))
            assert (ROOT/record['path']).read_bytes() == prior_image.read_bytes()
            assert bind(prior_image)['sha256'] == old['sha256'] == actual['sha256']
            assert bind(prior_image)['bytes'] == old['bytes'] == actual['bytes']
            assert Path(old['path']).resolve() == prior_image.resolve()
            assert record['page'] in prior_root['actually_viewed_pages']
            carries.append({**record, 'whole_png_bytes_compared':True,
                'prior_sealed_review_entry_and_hash_verified':True,
                'fresh_view_claimed_by_this_peer':False})
        if record['page'] in pages:
            assert record['reviewer'] == 'peer' and not record['byte_identical_to_prior_611_image']
            images.append({**record,'actual_viewed':True,'fresh_view_for_this_final_pdf':True,
                'review_result':'PASS','observation':OBSERVATIONS[record['page']]})
    assert len(carries) == 82 and [r['page'] for r in images] == pages
    carry_pages = {r['page'] for r in carries}
    assert carry_pages.issubset(prep['root_pages'])
    assert {491,492,493,494,495,496,596,598,599,600}.issubset(carry_pages)
    assert 601 not in carry_pages
    root_review_path = ROOT/'work/root/root_visual_review_619.json'
    root_review = json.loads(root_review_path.read_text())
    assert bind(root_review_path)['sha256'] == '5b2d6945100fe1ef68e09360e88add3995eb3b067d14341d15568590d395cf17'
    assert root_review['sha256'] == PDF_HASH and root_review['status'] == 'PASS'
    assert root_review['images_opened_this_final_review'] == [602,603,604,605]
    assert root_review['actual_view_calls'] == [[602,603],[604,605]]
    assert set(root_review['byte_identical_prior_review_pages']) == carry_pages
    assert root_review['render_preparation_sha256'] == bind(prep_path)['sha256']
    assert not root_review['issues']

    retained = []
    for old in prior_peer['retained_log_copies']:
        source = ROOT/old['source_path']
        local = ROOT/old['path'].replace('final_611','final_619')
        assert source.read_bytes() == local.read_bytes()
        retained.append({**bind(local),'source_path':old['source_path'],
            'lines':len(local.read_text().splitlines()),'read_in_full':True})
    log = (ROOT/'work/part_c/final_619_build.log').read_text()
    blg = (ROOT/'work/part_c/final_619_build.blg').read_text()
    stages = [(ROOT/f'work/part_c/final_619_stage_{i}_stdout.txt').read_text() for i in range(1,5)]
    stage_counts = []
    for i,text in enumerate(stages,1):
        actual_counts = {'stage':i,**counts(text),'bibtex_warnings':text.count('Warning--')}
        for key in ['overfull_boxes','missing_characters','undefined_control_sequences',
                    'undefined_reference_or_citation_lines','package_warning_lines',
                    'latex_font_warnings','fatal_error_lines','latex_warnings',
                    'label_rerun_warnings']:
            assert actual_counts[key] == 0
        stage_counts.append(actual_counts)
    assert stages[0] == stages[2] == stages[3]
    final_counts = {**counts(log),'bibtex_warnings':blg.count('Warning--')}
    expected = {key:0 for key in final_counts}
    expected.update(underfull_hboxes=1,luaotfload_fallback_events=1,
                    generic_microtype_protrusion_notices=2,bibtex_warnings=1)
    assert final_counts == expected
    assert 'badness 7133' in log and 'lines 62--63' in log
    assert 'C_Tukia1972' in blg and 'has not \nchanged' in log
    assert '619 pages, 4194159 bytes' in log
    commands = json.loads((ROOT/'deliverable/build_commands.json').read_text())
    artifact = json.loads((ROOT/'deliverable/build_artifact.json').read_text())
    assert len(commands) == 4 and all(r['exit_code'] == 0 for r in commands)
    assert artifact['success'] and artifact['stage_count'] == 4 and artifact['pdf_sha256'] == PDF_HASH
    for name,digest in artifact['source_sha256'].items():
        assert bind('deliverable/'+name)['sha256'] == digest
    bib = (ROOT/'deliverable/LM4_FINITE_GROUP_ACTIONS_references.bib').read_text()
    bbl = (ROOT/'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.bbl').read_text()
    bib_count = len(re.findall(r'^@\w+\s*\{',bib,re.M))
    used = int(re.search(r"You've used (\d+) entries",blg).group(1))
    assert bib_count == 88 and used == bbl.count(r'\bibitem') == 77

    frozen = [verify_binding(row) for row in prior_peer['frozen_source_and_review_bindings_unchanged']]
    f31_review_path = ROOT/'work/part_c/review_f31.json'
    f31_review = json.loads(f31_review_path.read_text())
    assert bind(f31_review_path)['sha256'] == 'e2e3b24eb352c3e20fe6fd936e03ae4f12d8082f83450a1896c442ae9570bb79'
    frozen.extend(verify_binding(row) for row in f31_review['primary_bindings'].values())
    frozen.append(verify_binding(f31_review['report']))
    frozen.append(bind(f31_review_path))
    repair29_path = ROOT/'work/root/f29_typesetting_repair.json'
    assert bind(repair29_path) == prior_peer['assembly_f29_exact_comparison']['root_typography_record']
    repair29 = json.loads(repair29_path.read_text())
    assembled = (ROOT/'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.tex').read_text()
    f29 = assembled_comparison('F.29','f_four_parameter_product_one_images',assembled,repair29)
    f29.update(root_typography_record=bind(repair29_path),old=repair29['old'],new=repair29['new'],
        replacement_count=1,final_page=596,freshly_viewed_in_this_peer_review=False,
        prior_actual_view_chain=bind(prior_root_path),
        whole_png_equal_to_that_reviewed_page=True)
    assert f29['assembled_fragment_sha256'] == prior_peer['assembly_f29_exact_comparison']['assembled_fragment_sha256']
    f30 = assembled_comparison('F.30','f_product_one_first_scalar_field_images',assembled)
    assert f30['assembled_fragment_sha256'] == prior_peer['assembly_f30_exact_comparison']['assembled_fragment_sha256']
    f30.update(final_pages=[598,599,600,601],whole_png_carry_pages=[598,599,600],
        freshly_viewed_by_this_peer=[601],frozen_proof_unchanged=True)
    repair31_path = ROOT/'work/root/f31_typesetting_repair.json'
    repair31 = json.loads(repair31_path.read_text())
    repair31_for_helper = {**repair31,'frozen_fragment_unchanged_sha256':repair31['proof_sha256']}
    f31 = assembled_comparison('F.31','f_full_product_one_affine_images',assembled,repair31_for_helper)
    f31.update(root_typography_record=bind(repair31_path),old=repair31['old'],new=repair31['new'],
        replacement_count=1,final_pages=list(range(602,610)),repaired_page=603,
        freshly_viewed_by_this_peer=[606,607,608,609],root_fresh_views=[602,603,604,605],
        root_fresh_view_record=bind(root_review_path),frozen_proof_unchanged=True,
        historical_repair_record_preserved_unchanged=True,
        this_record_supplies_final_build_and_peer_visual_gate=True)
    assert f31['frozen_source']['sha256'] == '909cb42466354ecebfede5b5d27077381d13e87f9261ea62180dc507cf91c345'

    result = {
        'reviewer':'/root/c89_review_and_general_c',
        'review_scope':'Ten actual fresh final619 views, all82 complete-PNG carry comparisons, full final LaTeX/BibTeX logs and all four stage outputs, and complete reversible F29/F30/F31 assembly comparisons.',
        'status':'PASS','sealed_at_utc':datetime.now(timezone.utc).isoformat(),
        'pdf':{**pdf,'pages':619,'claims_in_parent_build':270},
        'render_preparation':bind(prep_path),'total_parent_selection_pages':96,
        'root_assigned_pages_count':86,'peer_assigned_pages_count':10,
        'peer_freshly_viewed_pages':pages,'peer_reused_without_fresh_view_pages':[],
        'actual_image_view_groups_in_order':VIEW_GROUPS,'maximum_images_per_view_call':2,
        'no_unviewed_page_certified':True,'images':images,
        'visual_findings':{'defects_found':[],'reference_samples_freshly_viewed':[610,611,615,616,619],
            'F30_changed_preceding_page_freshly_viewed':601,
            'F31_actual_proof_pages':list(range(602,610)),
            'F31_peer_fresh_view_pages':[606,607,608,609],
            'F31_root_fresh_view_pages':[602,603,604,605],
            'F31_root_review_binding':bind(root_review_path),
            'F7_scope_pages_byte_identical_to_reviewed_611':[491,492,493,494,495,496],
            'F29_25_repaired_page_byte_identical_to_reviewed_611':596},
        'parent_selection_counts_from_preparation':{'total':96,'root':86,'peer':10,
            'prior_whole_png_carries':82,'fresh_root':4,'fresh_peer':10,'fresh_total':14},
        'all_selected_image_hashes_independently_verified':all_bindings,
        'whole_png_carry_audit':{'count':82,'prior_aggregate_review':bind(prior_root_path),
            'prior_peer_review':bind(prior_peer_path),'prior_pdf_snapshot':bind(prep['prior_pdf']),
            'comparison_method':'Exact complete PNG byte equality, current and prior SHA256 and length, exact prior image path, and membership/hash in the sealed aggregate611 actual-view chain.',
            'entries':carries,'all_passed':True,'new_visual_views_claimed_for_carries':False},
        'entire_final_build_logs_and_all_four_stage_outputs_read':True,
        'retained_log_copies':retained,'four_stage_commands':commands,'all_four_exit_codes_zero':True,
        'stage_1_3_4_stdout_byte_identical':True,'stage_3_4_stdout_byte_identical':True,
        'stage_output_notice_counts':stage_counts,'final_log_notice_counts':final_counts,
        'notice_interpretations':[
            'One inherited underfull hbox, badness7133, at source lines62-63 in the opening notation table; page1 is an exact whole-PNG carry from the sealed611 review.',
            'One inherited luaotfload-main lookup failure and OT1 fallback per LuaLaTeX run; fontenc/lmodern subsequently load T1 Latin Modern and the final log lists embedded Type1 fonts.',
            'Two informational microtype generic protrusion notices in the final log: T1/lmtt and OT1/lmss.',
            'One inherited BibTeX warning: C_Tukia1972 has a number but no volume.',
            'No label-rerun, undefined-reference, undefined-citation, LaTeX/package/font or fatal warning occurs in any final stage. LuaLaTeX stage1,stage3 andstage4 stdout are byte-identical; the final .out file is unchanged.',
        ],
        'bibliography_record_count':bib_count,'bibtex_used_entries':used,'printed_bibliography_entries':77,
        'build_source_bindings':[bind('deliverable/'+n) for n in ['LM4_FINITE_GROUP_ACTIONS_paper.tex','LM4_FINITE_GROUP_ACTIONS_references.bib','LM4_FINITE_GROUP_ACTIONS_paper.bbl']],
        'assembly_f29_exact_comparison':f29,'assembly_f30_exact_comparison':f30,
        'assembly_f31_exact_comparison':f31,
        'frozen_source_and_review_bindings_unchanged':frozen,
        'review_writer':bind(Path(__file__).resolve()),'reused_review_helpers':bind(HELPER),
        'no_frozen_source_or_final_pdf_edits':True,
    }
    OUT.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','record':bind(OUT),'fresh_pages':pages,
        'whole_png_carries':82,'all_selected_images':96,
        'complete_forward_and_inverse_fragment_comparisons':['F.29','F.30','F.31'],
        'final_notice_counts':final_counts},indent=2))

if __name__ == '__main__':
    main()
