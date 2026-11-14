#!/usr/bin/env python3
"""Seal the 25 actual final608 image views and complete build-log review."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'work/part_c/render_review_608.json'
PDF_HASH = '2038bacd186770710f3a949d2edf6adb92fb800ab6d531133088b6694fd07cd5'
VIEW_GROUPS = [[555,556],[557,565],[575,578],[580,581],[582,583],
               [584,585],[586,587],[588,589],[590,595],[596,597],
               [598,599],[600,603],[608]]
OBSERVATIONS = {
    555: 'F.21.3-7 scalar-image statement, based source coordinates and covering maps are clear; tags, multirow expressions and footer fit.',
    556: 'Historical F.21 exponent pairs (0,3),(2,4),(3,2),(4,0), coordinate inverse and derivative displays are legible and unobstructed.',
    557: 'F.21.15-21 quotient comparisons, actual section and rational identities are clear; the final multirow display is separated from the footer.',
    565: 'F22 end, exact two-row inclusion diagram and F23 opening/sign diagram render cleanly, with intact arrows and labels.',
    575: 'F24 pivot-row/column table, exact final pivot and restriction/fixed-point conclusions are legible; all symbols and labels fit.',
    578: 'F25 closing coefficient argument and F26 opening trace statement are clear; multirow F.26.1 and maps F.26.2-3 fit.',
    580: 'F26 trace-pairing and coefficient maps, affine representation and tensor comparison render clearly, with no collision at the lower page break.',
    581: 'F26 inverse interpolation, cocycle splitting, finite-field formulas and 7560-count display are legible and within margins.',
    582: 'F26 rank-distribution and closure-stage tables, block matrix and row-span formula are clear and aligned; no clipping or footer overlap.',
    583: 'F26 end and F27 opening are clean; exact locus, H1 restriction, principal kernel and scalar-field displays fit.',
    584: 'F27 coefficient maps, principal quotient, actual source labels and basis/inverse formulas are legible; final display clears the footer.',
    585: 'F27 five-by-five commutator matrix, exact determinant and actual seed formulas render clearly with intact entries, brackets and tags.',
    586: 'F27 recurrence, Frobenius maps, Vandermonde determinant and explicit interpolation inverse are legible and correctly spaced.',
    587: 'F27 conclusion and F28 opening are clear; field formulas, proof marker and final display have unobstructed page spacing.',
    588: 'F28 original coefficient/principal maps, core inclusion/section and block action are legible with intact equation labels.',
    589: 'F28 selected-source comparison table, actual seed evaluations and Frobenius field-generation argument are clear.',
    590: 'F28 cross-type comparisons, exact intertwiners, principal kernel and trace consequence render clearly through the page break.',
    595: 'F29 exceptional residual conclusion and actual X4-pivot coefficient/basis maps and comparison table are readable and aligned.',
    596: 'Repaired F.29.25 puts g=(s-1)(t-1) on its own row above the full five-by-five H matrix. Every entry, bracket and tag is clear; determinant, essential-line argument and seed display fit without clipping or overlap.',
    597: 'F29 actual K-word recurrence, summed restriction, both inverse intertwiners, Vandermonde matrix/inverse and trace criterion are clear and within margins.',
    598: 'F29 evidence and actual positive-sign transport conclude cleanly; proof box is visible and the following references start on a new page.',
    599: 'References heading and entries1-8 are legible, with intact accents, italic titles and paragraph breaks; continued entry at bottom is properly spaced.',
    600: 'Bibliography continuation and entries9-15 are clear, including the new finite-quotient source note and long publication titles.',
    603: 'Bibliography entries35-42 and continuation text are legible; long author names, JSON filenames and article titles fit.',
    608: 'Final bibliography continuation and entry77 are legible; the final page number is clear and no text is clipped.'
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
}


def counts(text):
    return {key: len(re.findall(pattern, text, re.M)) for key,pattern in PATTERNS.items()}


def main():
    assert not OUT.exists(), 'Do not overwrite a sealed visual-review record.'
    prep_path = ROOT/'work/root/render_preparation_608_final.json'
    prep = json.loads(prep_path.read_text())
    pages = [page for group in VIEW_GROUPS for page in group]
    assert pages == prep['peer_pages']
    assert len(pages) == len(set(pages)) == len(OBSERVATIONS) == 25
    assert max(map(len, VIEW_GROUPS)) == 2
    assert prep['pages'] == 608 and prep['sha256'] == PDF_HASH
    pdf = bind(prep['pdf'])
    assert pdf['sha256'] == PDF_HASH and pdf['bytes'] == 4117520
    assert len(prep['images']) == 84 and len(prep['root_pages']) == 59
    assert set(pages).isdisjoint(prep['root_pages'])
    images, carries = [], []
    for record in prep['images']:
        actual = bind(record['path'])
        assert actual['sha256'] == record['sha256']
        assert actual['bytes'] == record['bytes']
        if record['byte_identical_to_prior_600_image']:
            assert (ROOT/record['path']).read_bytes() == (ROOT/record['prior_image']).read_bytes()
            carries.append(record['page'])
        if record['page'] in pages:
            assert record['reviewer'] == 'peer'
            assert not record['byte_identical_to_prior_600_image']
            images.append({**record, 'actual_viewed': True,
                           'fresh_view_for_this_final_pdf': True,
                           'review_result': 'PASS',
                           'observation': OBSERVATIONS[record['page']]})
    assert len(carries) == 48 and set(carries).issubset(prep['root_pages'])
    assert [entry['page'] for entry in images] == pages

    source_names = ['LM4_FINITE_GROUP_ACTIONS_paper.log', 'LM4_FINITE_GROUP_ACTIONS_paper.blg',
                    'build_commands.json','build_artifact.json'] + [f'build_stage_{j}_stdout.txt' for j in range(1,5)]
    local_names = ['final_608_build.log','final_608_build.blg','final_608_build_commands.json',
                   'final_608_build_artifact.json'] + [f'final_608_stage_{j}_stdout.txt' for j in range(1,5)]
    retained = []
    for source_name, local_name in zip(source_names, local_names):
        source = ROOT/'deliverable'/source_name
        local = ROOT/'work/part_c'/local_name
        assert source.read_bytes() == local.read_bytes()
        retained.append({**bind(local), 'source_path': str(source.relative_to(ROOT)),
                         'lines': len(local.read_text().splitlines()), 'read_in_full': True})
    log = (ROOT/'work/part_c/final_608_build.log').read_text()
    blg = (ROOT/'work/part_c/final_608_build.blg').read_text()
    stages = [(ROOT/f'work/part_c/final_608_stage_{j}_stdout.txt').read_text() for j in range(1,5)]
    stage_counts = []
    for j, text in enumerate(stages, start=1):
        entry = {'stage': j, **counts(text),
                 'label_rerun_warnings': text.count('Label(s) may have changed'),
                 'bibtex_warnings': text.count('Warning--')}
        for key in ['overfull_boxes','missing_characters','undefined_control_sequences',
                    'undefined_reference_or_citation_lines','latex_warnings','package_warning_lines',
                    'latex_font_warnings','fatal_error_lines','label_rerun_warnings']:
            assert entry[key] == 0, (j,key,entry[key])
        stage_counts.append(entry)
    assert stages[0] == stages[2] == stages[3]
    final_counts = {**counts(log), 'bibtex_warnings': blg.count('Warning--')}
    expected = {key: 0 for key in final_counts}
    expected.update(underfull_hboxes=1,luaotfload_fallback_events=1,
                    generic_microtype_protrusion_notices=2,bibtex_warnings=1)
    assert final_counts == expected
    assert 'badness 7133' in log and 'lines 62--63' in log
    assert "C_Tukia1972" in blg
    assert 'has not \nchanged' in log
    assert '608 pages, 4117520 bytes' in log
    commands = json.loads((ROOT/'deliverable/build_commands.json').read_text())
    artifact = json.loads((ROOT/'deliverable/build_artifact.json').read_text())
    assert len(commands) == 4 and all(item['exit_code'] == 0 for item in commands)
    assert artifact['success'] and artifact['stage_count'] == 4 and artifact['pdf_sha256'] == PDF_HASH
    for name,digest in artifact['source_sha256'].items():
        assert bind('deliverable/'+name)['sha256'] == digest

    bib = (ROOT/'deliverable/LM4_FINITE_GROUP_ACTIONS_references.bib').read_text()
    bbl = (ROOT/'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.bbl').read_text()
    bib_count = len(re.findall(r'^@\w+\s*\{',bib,re.M))
    used_count = int(re.search(r"You've used (\d+) entries",blg).group(1))
    printed_count = bbl.count(r'\bibitem')
    assert bib_count == 88 and used_count == printed_count == 77

    prior = json.loads((ROOT/'work/part_c/render_review_600.json').read_text())
    frozen = prior['frozen_source_and_review_bindings_unchanged'][:]
    for entry in frozen:
        assert bind(entry['path']) == entry
    extra = [
        'work/part_a/f_four_parameter_product_one_images.tex',
        'work/part_a/f_four_parameter_product_one_images_results.json',
        'work/part_a/f_four_parameter_product_one_images_report.txt',
        'work/part_a/f_four_parameter_product_one_images_evidence_manifest.json',
        'work/part_c/review_f29.txt', 'work/part_c/review_f29.json',
        'work/part_c/compact_family_displacement_graph.tex',
        'work/part_c/compact_family_displacement_graph_result.json',
        'work/part_c/compact_family_displacement_graph_report.txt',
    ]
    f29_review = json.loads((ROOT/'work/part_c/review_f29.json').read_text())
    for entry in f29_review['reviewed_frozen_artifacts'] + [f29_review['review_report']]:
        assert bind(entry['path']) == entry
    assert bind('work/part_c/review_f29.json')['sha256'] == 'dca50aac722ceb317fa9e4d9609c0aa3cd0354939db92fb942bf2b417902d880'
    for entry in f29_review['protected_bindings_checked_unchanged']:
        assert bind(entry['path']) == entry
    frozen.extend(bind(path) for path in extra)

    # Record the exact reversible proof-to-assembled-fragment map.
    repair_path = ROOT/'work/root/f29_typesetting_repair.json'
    repair = json.loads(repair_path.read_text())
    proof = (ROOT/'work/part_a/f_four_parameter_product_one_images.tex').read_text()
    metadata = json.loads((ROOT/'work/part_a/f_four_parameter_product_one_images_results.json').read_text())
    assembled = (ROOT/'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.tex').read_text()
    assert sha256(proof.encode()).hexdigest() == repair['frozen_fragment_unchanged_sha256']
    assert proof.count(repair['old']) == 1
    passage_text = metadata['manuscript_passages']
    assert passage_text.endswith('.') and not passage_text.endswith('..')
    passage = r'\passage{' + passage_text[:-1] + '}'
    forward = proof.replace(repair['old'],repair['new'],1)
    assert forward.count(repair['new']) == 1
    forward = forward.replace(r'\end{claim}'+'\n',r'\end{claim}'+'\n'+passage+'\n\n',1)
    start = assembled.index(r'\begin{claim}{F.29}')
    end = assembled.index(r'\end{proof}',start)+len(r'\end{proof}')+1
    extracted = assembled[start:end]
    assert forward == extracted
    inverse = extracted.replace(passage+'\n\n','',1).replace(repair['new'],repair['old'],1)
    assert inverse == proof
    assert passage[len(r'\passage{'):-1]+'.' == passage_text

    result = {
        'reviewer': '/root/c89_review_and_general_c',
        'review_scope': 'Independent actual fresh visual review of the 25 assigned final608 pages and complete final LaTeX/BibTeX/build-stage review.',
        'status': 'PASS', 'sealed_at_utc': datetime.now(timezone.utc).isoformat(),
        'pdf': {**pdf,'pages':608,'claims_in_parent_build':268},
        'render_preparation': bind(prep_path), 'total_parent_selection_pages':84,
        'root_assigned_pages_count':59, 'peer_assigned_pages_count':25,
        'peer_freshly_viewed_pages':pages, 'peer_reused_without_fresh_view_pages':[],
        'actual_image_view_groups_in_order':VIEW_GROUPS,
        'maximum_images_per_view_call':2, 'no_unviewed_page_certified':True,
        'images':images,
        'visual_findings':{
            'defects_found':[], 'all_f27_pages_freshly_viewed':[583,584,585,586,587],
            'f28_sample_pages_freshly_viewed':[587,588,589,590],
            'f28_conclusion_page_reviewed_by':'Root, page591; this peer does not certify a fresh view of that unassigned page.',
            'f26_sample_pages_freshly_viewed':[578,580,581,582,583],
            'f29_assigned_pages_freshly_viewed':[595,596,597,598],
            'other_f29_pages_reviewed_by':'Root, pages591-594; this peer does not certify fresh views of those unassigned pages.',
            'historical_passages_checked':{'F.21_exponent_pairs':[555,556,557],'F.29.25':596},
            'bibliography_pages_checked':[599,600,603,608],
            'overall':'No clipping, overlap, missing glyph, malformed display, bad table/diagram alignment or footer collision observed on any assigned page.'},
        'parent_selection_counts_from_preparation':{
            'root_fresh_assignment':11,'root_whole_png_carry_comparisons':48,
            'peer_fresh_assignment':25,'total_fresh_assignment':36,
            'all_84_current_png_hashes_independently_verified':True,
            'all_48_root_carry_whole_png_byte_equalities_independently_verified':True,
            'scope':'These are exact preparation/binary checks; fresh visual certification in this peer record is limited to its listed25 actual views.'},
        'entire_final_build_logs_and_all_four_stage_outputs_read':True,
        'retained_log_copies':retained, 'four_stage_commands':commands,
        'all_four_exit_codes_zero':True, 'stage_1_3_4_stdout_byte_identical':True,
        'stage_3_4_stdout_byte_identical':True,
        'stage_output_notice_counts':stage_counts, 'final_log_notice_counts':final_counts,
        'notice_interpretations':[
            'One inherited underfull hbox, badness7133, at source lines62-63 in the opening table. Root owns final page1 visual review.',
            'One inherited luaotfload-main lookup failure and OT1 fallback per LuaLaTeX run; fontenc/lmodern then load T1 Latin Modern and the final log lists embedded Type1 fonts. The nonfatal loader notice is retained explicitly.',
            'Two informational microtype generic protrusion-setting notices in the final log, for T1/lmtt and OT1/lmss.',
            'One inherited BibTeX warning: C_Tukia1972 has a number but no volume.',
            'No label-rerun or undefined-reference/citation warning occurs in any stage of this final four-stage build. Stages1,3,4 stdout are byte-identical, and the final log reports the .out file unchanged.'
        ],
        'bibliography_record_count':bib_count,'bibtex_used_entries':used_count,
        'printed_bibliography_entries':printed_count,
        'build_source_bindings':[bind('deliverable/'+name) for name in
                                 ['LM4_FINITE_GROUP_ACTIONS_paper.tex','LM4_FINITE_GROUP_ACTIONS_references.bib','LM4_FINITE_GROUP_ACTIONS_paper.bbl']],
        'assembly_f29_exact_comparison':{
            'root_typography_record':bind(repair_path),
            'old':repair['old'],'new':repair['new'],'replacement_count':1,
            'manuscript_passage_metadata':passage_text,
            'exact_added_passage_line':passage,
            'passage_forward_map':'Remove the one terminal period from metadata.manuscript_passages, wrap in \\passage{...}, and insert that line plus two newlines immediately after the claim terminator newline.',
            'passage_inverse_map':'Remove that exact inserted line plus its two newlines. For the metadata annotation, unwrap and append the one terminal period.',
            'entire_forward_fragment_equals_assembled_fragment':True,
            'entire_inverse_fragment_equals_frozen_proof':True,
            'assembled_fragment_sha256':sha256(extracted.encode()).hexdigest(),
            'actual_fresh_final_page_checked':596,
            'final_display_result':'PASS: row break retains every expression and tag and removes the prior overflow.'},
        'frozen_source_and_review_bindings_unchanged':frozen,
        'review_writer':bind(Path(__file__).resolve()),
        'no_frozen_source_or_final_pdf_edits':True
    }
    OUT.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','record':bind(OUT),'fresh_pages':25,
                      'final_notice_counts':final_counts},indent=2))


if __name__ == '__main__':
    main()
