#!/usr/bin/env python3
"""Seal five actual final611 views, every carry, and full build-log review."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'work/part_c/render_review_611.json'
PDF_HASH = '6eb08722ef726aaa8894facf55915238861d7981c9d86d63cdc62e6e7dc47a97'
VIEW_GROUPS = [[602,603],[607,608],[611]]
OBSERVATIONS = {
    602: 'References heading and entries 1-8 are clear, with intact accents, italic titles and paragraph breaks. The continuation of entry 8 is separated from the footer.',
    603: 'Entry 8 continuation and entries 9-15 are legible; long source descriptions and publication titles fit without clipping or overlap.',
    607: 'References 43-51, including the order-three source note and long mathematical titles, render clearly with intact labels and footer spacing.',
    608: 'References 52-59 are clear; formulas, accents, journal titles and the final continued entry fit within the text area.',
    611: 'Final bibliography continuation and entry 77 are legible; the final page number is clear, with no clipping or unwanted text overlap.',
}

def bind(path):
    path = ROOT/path if isinstance(path, str) else path
    data = path.read_bytes()
    return {'path': str(path.relative_to(ROOT)), 'bytes': len(data),
            'sha256': sha256(data).hexdigest()}

PATTERNS = {
    'overfull_boxes': r'Overfull \\[hv]box',
    'underfull_hboxes': r'Underfull \\hbox',
    'underfull_vboxes': r'Underfull \\vbox',
    'missing_characters': r'Missing character:',
    'undefined_control_sequences': r'Undefined control sequence',
    'undefined_reference_or_citation_lines': r'^.*(?:Reference|Citation).*undefined.*$',
    'latex_warnings': r'LaTeX Warning:',
    'package_warning_lines': r'^Package .* Warning:',
    'latex_font_warnings': r'LaTeX Font Warning:',
    'fatal_error_lines': r'^!|Fatal error|Emergency stop',
    'luaotfload_fallback_events': r'Error in luaotfload: reverting to OT1',
    'generic_microtype_protrusion_notices': r'Loading generic protrusion settings',
    'label_rerun_warnings': r'Label\(s\) may have changed',
}

def counts(text):
    return {key: len(re.findall(pattern,text,re.M)) for key,pattern in PATTERNS.items()}

def assembled_comparison(claim, stem, assembled, repair=None):
    proof_path = ROOT/f'work/part_a/{stem}.tex'
    metadata_path = ROOT/f'work/part_a/{stem}_results.json'
    proof = proof_path.read_text()
    metadata = json.loads(metadata_path.read_text())
    passage_text = metadata['manuscript_passages']
    assert passage_text.endswith('.') and not passage_text.endswith('..')
    passage = r'\passage{' + passage_text[:-1] + '}'
    forward = proof
    if repair is not None:
        assert bind(proof_path)['sha256'] == repair['frozen_fragment_unchanged_sha256']
        assert proof.count(repair['old']) == 1
        forward = forward.replace(repair['old'],repair['new'],1)
        assert forward.count(repair['new']) == 1
    forward = forward.replace(r'\end{claim}'+'\n',r'\end{claim}'+'\n'+passage+'\n\n',1)
    start = assembled.index(r'\begin{claim}{'+claim+'}')
    end = assembled.index(r'\end{proof}',start)+len(r'\end{proof}')+1
    extracted = assembled[start:end]
    assert forward == extracted
    inverse = extracted.replace(passage+'\n\n','',1)
    if repair is not None:
        inverse = inverse.replace(repair['new'],repair['old'],1)
    assert inverse == proof
    assert passage[len(r'\passage{'):-1]+'.' == passage_text
    return {
        'frozen_source':bind(proof_path), 'frozen_metadata':bind(metadata_path),
        'manuscript_passage_metadata':passage_text,
        'exact_added_passage_line':passage,
        'passage_forward_map':'Remove the one terminal period from manuscript_passages, wrap in \\passage{...}, and insert that line plus two newlines immediately after the claim terminator newline.',
        'passage_inverse_map':'Remove the exact inserted line plus two newlines; unwrap the metadata annotation and restore its one terminal period.',
        'entire_forward_fragment_equals_assembled_fragment':True,
        'entire_inverse_fragment_equals_frozen_proof':True,
        'assembled_fragment_sha256':sha256(extracted.encode()).hexdigest(),
        'typography_repair_count': 1 if repair else 0,
    }

def main():
    assert not OUT.exists(), 'Do not overwrite a sealed review.'
    prep_path = ROOT/'work/root/render_preparation_611_final.json'
    prep = json.loads(prep_path.read_text())
    pages = [p for group in VIEW_GROUPS for p in group]
    assert pages == prep['peer_pages']
    assert len(pages) == len(set(pages)) == len(OBSERVATIONS) == 5
    assert prep['pages'] == 611 and prep['sha256'] == PDF_HASH
    pdf = bind(prep['pdf'])
    assert pdf['sha256'] == PDF_HASH and pdf['bytes'] == 4139349
    assert len(prep['images']) == 88 and len(prep['root_pages']) == 83
    assert set(pages).isdisjoint(prep['root_pages'])

    prior_root_path = ROOT/'work/root/render_review_608.json'
    prior_root = json.loads(prior_root_path.read_text())
    assert bind(prior_root_path)['sha256'] == prep['prior_review_sha256']
    assert prior_root['sha256'] == prep['prior_pdf_sha256']
    assert bind(prep['prior_pdf'])['sha256'] == prep['prior_pdf_sha256']
    prior_rows = {r['page']:r for r in prior_root['rendered_images']}
    prior_peer_path = ROOT/'work/part_c/render_review_608.json'
    prior_peer = json.loads(prior_peer_path.read_text())
    assert bind(prior_peer_path)['sha256'] == '19e084cc0e3c0b39317b4076ed2781caa4a58c89d7e28f079d90e99f515621bb'
    assert prior_root['independent_review_sha256'] == bind(prior_peer_path)['sha256']
    images, carries, all_bindings = [], [], []
    for record in prep['images']:
        actual = bind(record['path'])
        assert actual['sha256'] == record['sha256'] and actual['bytes'] == record['bytes']
        all_bindings.append({'page':record['page'], **actual})
        if record['byte_identical_to_prior_608_image']:
            old = prior_rows[record['page']]
            prior_image = ROOT/record['prior_image']
            assert (ROOT/record['path']).read_bytes() == prior_image.read_bytes()
            assert bind(prior_image)['sha256'] == old['sha256'] == actual['sha256']
            assert bind(prior_image)['bytes'] == old['bytes'] == actual['bytes']
            assert Path(old['path']).resolve() == prior_image.resolve()
            assert record['page'] in prior_root['actually_viewed_pages']
            carries.append({**record, 'whole_png_bytes_compared':True,
                            'prior_sealed_review_entry_and_hash_verified':True,
                            'fresh_view_claimed_by_this_peer':False})
        if record['page'] in pages:
            assert record['reviewer'] == 'peer' and not record['byte_identical_to_prior_608_image']
            images.append({**record,'actual_viewed':True,'fresh_view_for_this_final_pdf':True,
                           'review_result':'PASS','observation':OBSERVATIONS[record['page']]})
    assert len(carries) == 79
    assert [r['page'] for r in images] == pages
    assert set(r['page'] for r in carries).issubset(prep['root_pages'])
    assert set([491,492,493,494,495,496,596]).issubset(r['page'] for r in carries)

    retained = []
    for old in prior_peer['retained_log_copies']:
        source = ROOT/old['source_path']
        local = ROOT/old['path'].replace('final_608','final_611')
        assert source.read_bytes() == local.read_bytes()
        retained.append({**bind(local),'source_path':old['source_path'],
                         'lines':len(local.read_text().splitlines()),'read_in_full':True})
    log = (ROOT/'work/part_c/final_611_build.log').read_text()
    blg = (ROOT/'work/part_c/final_611_build.blg').read_text()
    stages = [(ROOT/f'work/part_c/final_611_stage_{i}_stdout.txt').read_text() for i in range(1,5)]
    stage_counts = []
    for i,text in enumerate(stages,1):
        actual_counts = {'stage':i,**counts(text),'bibtex_warnings':text.count('Warning--')}
        for key in ['overfull_boxes','missing_characters','undefined_control_sequences',
                    'undefined_reference_or_citation_lines','package_warning_lines',
                    'latex_font_warnings','fatal_error_lines']:
            assert actual_counts[key] == 0
        assert actual_counts['latex_warnings'] == actual_counts['label_rerun_warnings'] == (1 if i==1 else 0)
        stage_counts.append(actual_counts)
    assert stages[2] == stages[3] and stages[0] != stages[2]
    final_counts = {**counts(log),'bibtex_warnings':blg.count('Warning--')}
    expected = {key:0 for key in final_counts}
    expected.update(underfull_hboxes=1,luaotfload_fallback_events=1,
                    generic_microtype_protrusion_notices=2,bibtex_warnings=1)
    assert final_counts == expected
    assert 'badness 7133' in log and 'lines 62--63' in log
    assert 'C_Tukia1972' in blg and 'has not \nchanged' in log
    assert '611 pages, 4139349 bytes' in log
    commands = json.loads((ROOT/'deliverable/build_commands.json').read_text())
    artifact = json.loads((ROOT/'deliverable/build_artifact.json').read_text())
    assert len(commands)==4 and all(r['exit_code']==0 for r in commands)
    assert artifact['success'] and artifact['stage_count']==4 and artifact['pdf_sha256']==PDF_HASH
    for name,digest in artifact['source_sha256'].items():
        assert bind('deliverable/'+name)['sha256']==digest
    bib = (ROOT/'deliverable/LM4_FINITE_GROUP_ACTIONS_references.bib').read_text()
    bbl = (ROOT/'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.bbl').read_text()
    bib_count = len(re.findall(r'^@\w+\s*\{',bib,re.M))
    used = int(re.search(r"You've used (\d+) entries",blg).group(1))
    assert bib_count==88 and used==bbl.count(r'\bibitem')==77

    frozen = prior_peer['frozen_source_and_review_bindings_unchanged'][:]
    for row in frozen:
        assert bind(row['path'])==row
    f30_review_path = ROOT/'work/part_c/review_f30.json'
    f30_review = json.loads(f30_review_path.read_text())
    assert bind(f30_review_path)['sha256']=='4f8823a9be1532dc08d7c5af9e60cba6d52572e9060ef6fe7a219d22ef5bf467'
    f30_rows = f30_review['reviewed_frozen_artifacts']+[f30_review['review_report']]
    for row in f30_rows:
        assert bind(row['path'])==row
    frozen.extend(f30_rows+[bind(f30_review_path)])
    repair_path = ROOT/'work/root/f29_typesetting_repair.json'
    assert bind(repair_path)==prior_peer['assembly_f29_exact_comparison']['root_typography_record']
    repair = json.loads(repair_path.read_text())
    assembled = (ROOT/'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.tex').read_text()
    f29 = assembled_comparison('F.29','f_four_parameter_product_one_images',assembled,repair)
    f29.update(root_typography_record=bind(repair_path),old=repair['old'],new=repair['new'],replacement_count=1,
               final_page=596,freshly_viewed_in_this_peer_review=False,
               prior_actual_peer_view_record=bind(prior_peer_path),
               whole_png_equal_to_that_reviewed_page=True)
    assert f29['assembled_fragment_sha256']==prior_peer['assembly_f29_exact_comparison']['assembled_fragment_sha256']
    f30 = assembled_comparison('F.30','f_product_one_first_scalar_field_images',assembled)
    assert f30['frozen_source']['sha256']=='1703a98c06269ec8ad73cdd5e420f7213ba620e06a6dcc104905447566a613f5'

    result = {
        'reviewer':'/root/c89_review_and_general_c',
        'review_scope':'Five actual fresh final611 reference-page views, all 79 whole-PNG carry comparisons, full final build logs/stage outputs, and exact reversible F29/F30 assembly comparisons.',
        'status':'PASS','sealed_at_utc':datetime.now(timezone.utc).isoformat(),
        'pdf':{**pdf,'pages':611,'claims_in_parent_build':269},
        'render_preparation':bind(prep_path),'total_parent_selection_pages':88,
        'root_assigned_pages_count':83,'peer_assigned_pages_count':5,
        'peer_freshly_viewed_pages':pages,'peer_reused_without_fresh_view_pages':[],
        'actual_image_view_groups_in_order':VIEW_GROUPS,'maximum_images_per_view_call':2,
        'no_unviewed_page_certified':True,'images':images,
        'visual_findings':{'defects_found':[],'reference_samples_freshly_viewed':pages,
            'F30_new_proof_visual_scope':'Root owns pages598-601; this peer makes no fresh-view claim for those four pages.',
            'F7_scope_pages_all_byte_identical_to_reviewed_608':[491,492,493,494,495,496],
            'F29_25_repaired_page_byte_identical_to_own_actual_608_view':596},
        'parent_selection_counts_from_preparation':{'total':88,'root':83,'peer':5,'prior_whole_png_carries':79,'fresh_root':4,'fresh_peer':5,'fresh_total':9},
        'all_selected_image_hashes_independently_verified':all_bindings,
        'whole_png_carry_audit':{'count':79,'prior_aggregate_review':bind(prior_root_path),
            'prior_peer_review':bind(prior_peer_path),'prior_pdf_snapshot':bind(prep['prior_pdf']),
            'comparison_method':'Exact complete PNG byte equality, current and prior file SHA256 and length, exact prior image path, and membership/hash in the sealed aggregate608 review.',
            'entries':carries,'all_passed':True,'new_visual_views_claimed_for_carries':False},
        'entire_final_build_logs_and_all_four_stage_outputs_read':True,
        'retained_log_copies':retained,'four_stage_commands':commands,'all_four_exit_codes_zero':True,
        'stage_1_3_4_stdout_byte_identical':False,'stage_3_4_stdout_byte_identical':True,
        'stage_output_notice_counts':stage_counts,'final_log_notice_counts':final_counts,
        'notice_interpretations':[
            'One inherited underfull hbox, badness7133, at source lines62-63 in the opening table; page1 is a byte-identical sealed608 carry.',
            'One inherited luaotfload-main lookup failure and OT1 fallback per LuaLaTeX run; fontenc/lmodern then load T1 Latin Modern and the final log lists embedded Type1 fonts.',
            'Two informational microtype generic protrusion notices in the final log: T1/lmtt and OT1/lmss.',
            'One inherited BibTeX warning: C_Tukia1972 has a number but no volume.',
            'Stage1 has one label-rerun warning. Stages3 and4 have none and are byte-identical; the final log reports the .out file unchanged. No undefined-reference/citation warning occurs in any stage.'
        ],
        'bibliography_record_count':bib_count,'bibtex_used_entries':used,'printed_bibliography_entries':77,
        'build_source_bindings':[bind('deliverable/'+n) for n in ['LM4_FINITE_GROUP_ACTIONS_paper.tex','LM4_FINITE_GROUP_ACTIONS_references.bib','LM4_FINITE_GROUP_ACTIONS_paper.bbl']],
        'assembly_f29_exact_comparison':f29,'assembly_f30_exact_comparison':f30,
        'frozen_source_and_review_bindings_unchanged':frozen,
        'review_writer':bind(Path(__file__).resolve()),'no_frozen_source_or_final_pdf_edits':True,
    }
    OUT.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','record':bind(OUT),'fresh_pages':pages,'whole_png_carries':79,
                      'final_notice_counts':final_counts},indent=2))

if __name__=='__main__':
    main()
