#!/usr/bin/env python3
"""Bind the initial-fixed-region proof, full log read, and five actual views."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re
import runpy

ROOT = Path(__file__).resolve().parents[3]
BUILD = Path(__file__).resolve().parent
STEM = ROOT/'work/part_c/compact_family_initial_fixed_region'
SOURCE = STEM.with_suffix('.tex')
REPORT = Path(str(STEM)+'_report.txt')
OUT = Path(str(STEM)+'_result.json')
helpers = runpy.run_path(str(ROOT/'work/part_c/code/seal_render_review_611.py'))
bind,counts = helpers['bind'],helpers['counts']

assert not OUT.exists(), 'Do not overwrite a sealed result.'
assert bind(SOURCE)['sha256'] == 'af88a37da26d8576f6294060e7e3558900719b7596e7338228b3b049fd5d4b54'
assert len(SOURCE.read_text().splitlines()) == 397
record = json.loads((BUILD/'build_result.json').read_text())
for key in ['source','before_self_review','self_review_diff','wrapper','registered_record',
            'standalone_bibliography','build_commands','log','bibtex_log','pdf','build_script']:
    assert bind(record[key]['path']) == record[key]
assert record['complete_forward_and_inverse_edit_equalities']
assert record['source_is_exact_wrapper_body'] and record['source_display_pairs'] == 19
assert record['pdf_pages'] == 5
assert record['pdf']['sha256'] == '4107e7ae2bfc2a907732213b95d9ebbadb28367a82d693fe04889c80de7c6f37'
assert record['pdf']['bytes'] == 211635

dependencies = {
    'work/part_b/c81.tex':'d24ec0b95c132e56b14f1775339b64799c02f032589a3cd9d0f05379f5846267',
    'work/part_b/c82.tex':None,
    'work/part_b/c83.tex':'33c766356d2124a148167158c326bdcf70757088ebc2f9a9a913aba09b9550e1',
    'work/part_b/c88.tex':'683ee6d104493c2945aa9af7e6e37c7770e39f0827c7cf42b1aa3e29612a2166',
    'work/part_c/c91.tex':'0b5db75c25411d069d4316995b410faab63b5c624bed7f4044a963e27d1952ff',
    'work/part_c/c92.tex':'e978d4c54fa14090d67e1fd0620561bd251a8e3673132284aa144030b129ad7c',
    'work/part_c/compact_family_displacement_graph.tex':'e3f724056664f2e1e2ae164b2e046b1dd8f5cd4495a66b45866b88191ef58338',
    'work/part_c/compact_family_filled_carriers_and_expansions.tex':'7a88ef1bdfa3fe3fc4a4c2588db43be9047ff6ea3d7ef6c0ab2c02a01f22f098',
}
dependency_bindings = []
for path,digest in dependencies.items():
    actual = bind(path)
    if digest:
        assert actual['sha256'] == digest
    dependency_bindings.append(actual)

primary_tex = ROOT/'background/literature/yagasaki-homeo-noncompact-surfaces/src_arXiv_math_0010223/main.tex'
primary_pdf = ROOT/'work/part_b/research_data/yagasaki2000_homeomorphism_groups.pdf'
assert bind(primary_pdf)['sha256'] == '2b93668cd16e0534dfa6689393c6a9bfd369a7651bfadfe65bbcdc50af6a52f1'
primary_views = []
for page,digest in [
        (1,'07459151ccada9289a8c65efa734a6e7bcb2076e5de72e0c9f5057e8028084cb'),
        (2,'18a24ad028ba7d0198877a866b035ac8ed515108034d1329c174568f4c5c094a')]:
    item = bind(ROOT/f'work/part_c/initial_fixed_region_research/yagasaki2000-{page:02d}.png')
    assert item['sha256'] == digest
    primary_views.append({'printed_page':page,**item,'actually_viewed':True})

observations = [
    'The full statement, exact compact-open group comparison, local extension theorem and beginning of the finite construction are clear.',
    'The finite cover, partition functions, intermediate times, chart products and their explicit inverses are legible and properly spaced.',
    'All Yagasaki exceptions, the original Alexander map/inverse and supported lift formulas are clear; dense equations fit.',
    'The compact original circle transport, endpoint constant-track argument and both actual displacement envelope estimates are clear.',
    'The sum-metric estimate, compatible finite stages, precise remaining scope and full primary reference are clear and complete.',
]
images = []
for page,item in enumerate(record['rendered_images'],1):
    assert bind(item['path']) == item
    assert Path(item['path']).name == f'page-{page}.png'
    images.append({'page':page,**item,'actually_viewed':True,'status':'PASS','observation':observations[page-1]})
assert len(images) == 5
log = (BUILD/'note.log').read_text()
blg = (BUILD/'note.blg').read_text()
log_counts = {**counts(log),'bibtex_warnings':blg.count('Warning--')}
expected = {k:0 for k in log_counts}
expected['luaotfload_fallback_events'] = 1
assert log_counts == expected
assert '5 pages, 211635 bytes' in log
assert "You've used 1 entry" in blg
commands = json.loads((BUILD/'build_commands.json').read_text())
stage_checks = []
for command in commands:
    assert command['exit_code'] == 0
    for key in ['stdout','stderr']:
        assert bind(command[key]['path']) == command[key]
    assert command['stderr']['bytes'] == 0
    text = (ROOT/command['stdout']['path']).read_text()
    c = counts(text)
    assert c['overfull_boxes'] == c['underfull_hboxes'] == c['underfull_vboxes'] == 0
    assert c['missing_characters'] == c['undefined_control_sequences'] == c['fatal_error_lines'] == 0
    stage_checks.append({'stage':command['stage'],'notice_counts':c,
        'full_stdout_read':True,'stdout':command['stdout'],'stderr':command['stderr']})
assert [r['notice_counts']['latex_warnings'] for r in stage_checks] == [3,0,4,0]
assert [r['notice_counts']['package_warning_lines'] for r in stage_checks] == [1,0,0,0]
assert [r['notice_counts']['label_rerun_warnings'] for r in stage_checks] == [0,0,1,0]
assert [r['notice_counts']['undefined_reference_or_citation_lines'] for r in stage_checks] == [2,0,2,0]

prior_qa_path = ROOT/'work/part_c/render_review_619.json'
prior_qa = json.loads(prior_qa_path.read_text())
assert bind(prior_qa_path)['sha256'] == 'e1ee62c58e81aa0f0a64cfdf279287c05370e4ec9e539548bf576c11bd93d528'
unchanged = []
for row in prior_qa['frozen_source_and_review_bindings_unchanged']:
    assert bind(row['path']) == row
    unchanged.append(row)
assert bind('deliverable/LM4_FINITE_GROUP_ACTIONS_paper.pdf')['sha256'] == prior_qa['pdf']['sha256']

result = {
    'status':'AUTHOR_PROOF_AND_BUILD_PASS_INDEPENDENT_ACCEPTANCE_PENDING',
    'numbered_claim_registered':False,'sealed_at_utc':datetime.now(timezone.utc).isoformat(),
    'author_agent':'/root/c89_review_and_general_c',
    'source':bind(SOURCE),'source_lines':397,'display_pairs':19,'tags':list(range(1,20)),
    'report':bind(REPORT),'full_author_source_review':True,
    'proved_result':{
        'input':'Every compact metric based actual family h:P->C_Q(x), with noncompact N, and every compact quotient subpolyhedron X containing p.',
        'deformation':'H_{u,t}=G_{u,t}^{-1}h_u; H^{-1}_{u,t}=h_u^{-1}G_{u,t}.',
        'endpoint':'H_{u,1} fixes all of pi^{-1}X pointwise, with every original deck label retained.',
        'correction':'G and its inverse have one common compact quotient support, fix x and the original circle, and vary in the original uniform map/inverse topology.',
        'relative_component_witness':'k_{u,t}=g_{u,t}^{-1}B_{u,t}, identity on X at all times; its unique pointed lifted tracks over X are constant.',
        'finite_iteration':'Compatible stages for each finite nested compact-polyhedron chain beginning with a disk neighborhood of p.',
    },
    'exact_maps_checked':[
        'Identity in both directions between downstairs compact-open map and map/inverse group topologies.',
        'Each local Yagasaki extension phi_f(g) and its continuous inverse.',
        'Pasted Gamma_i and reversed-factor inverse, plus finite strip product and its inverse.',
        'Normalized ordinary contraction path and inverse; all five exceptional pairs retained.',
        'Original Mobius adjustment, Alexander family and displayed inverses for trivial Q.',
        'C92 pointed lift lambda(g), lambda(g^{-1}), every original q, and constant-track support.',
        'Compact actual centralizer transport qbx=ba^{-1}(z) and both original-circle limits.',
        'Residual k and its inverse, exact lambda group identity and lifted relative-X endpoint.',
        'Exact forward/inverse support carriers, common envelopes, inverse modulus and original sum metric.',
    ],
    'proof_dependencies':dependency_bindings,
    'primary_source_check':{
        'tex':bind(primary_tex),'pdf':bind(primary_pdf),
        'read_scope':'Complete Theorems1.1 and2.1, compact-open/identity-component definitions, proper-embedding definition and nearby introductory text.',
        'actually_viewed_printed_pages':[1,2],'actual_view_groups':[[1,2]],
        'images':primary_views,
        'exception_scope':'All five listed cases; pointed plane handled explicitly by original Alexander maps.',
        'bibliography_heading_transport':record['bibliography_key_map'],
        'registered_record':record['registered_record'],
        'standalone_record':record['standalone_bibliography'],
    },
    'build':{
        'result':bind(BUILD/'build_result.json'),'commands':commands,'all_four_exits_zero':True,
        'source_is_exact_wrapper_body':True,'complete_self_review_edit_forward_and_inverse_equalities':True,
        'exact_edits':record['self_review_exact_edits'],'before':record['before_self_review'],
        'diff':record['self_review_diff'],'wrapper':record['wrapper'],
        'pdf':record['pdf'],'pdf_pages':5,'log':record['log'],'bibtex_log':record['bibtex_log'],
        'final_log_lines':len(log.splitlines()),'bibtex_log_lines':len(blg.splitlines()),
        'all_final_logs_and_all_stage_stdout_read_in_full':True,
        'final_notice_counts':log_counts,'stage_checks':stage_checks,
        'notice_explanation':[
            'One inherited luaotfload-main lookup fallback per LuaLaTeX run, followed by T1 Latin Modern loading and embedded Type1 fonts.',
            'Stages1 and3 have two unresolved citation lines and their summary before final auxiliary resolution; stage1 also has one outline-rerun notice and stage3 one label-rerun notice.',
            'Final stage4 and final log have zero overfull, underfull, missing, undefined, LaTeX/package-warning and fatal counts. BibTeX has no warning.',
        ],
        'actual_visual_review':{'status':'PASS','groups':[[1,2],[3,4],[5]],
            'maximum_images_per_call':2,'images':images,'defects':[]},
        'build_script':record['build_script'],'seal_script':bind(Path(__file__).resolve()),
        'notice_count_helper':bind(ROOT/'work/part_c/code/seal_render_review_611.py'),
    },
    'remaining_global_problem':{
        'constructed_infinite_deformation':False,
        'missing_quantitative_construction':'Relative embedding homotopies and actual translated carriers controlled by the input common C0 displacement envelope, with accumulated factor displacement tending to zero along an exhaustion.',
        'uniform_number_of_future_stages_assumed':False,
        'C83_infinite_evaluation_obstruction_retained':True,
        'whole_lifted_tail_region_diameter_assumed_small':False,
    },
    'previous_final619_review':bind(prior_qa_path),
    'previous_frozen_bindings_reverified_unchanged':unchanged,
    'current619_pdf_unchanged':True,
    'independent_mathematical_reviews_pending':['root','/root/d78_actual_peripheral'],
}
OUT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'source':bind(SOURCE),'report':bind(REPORT),
    'result':bind(OUT),'pdf':record['pdf'],'actual_viewed_pages':[1,2,3,4,5]},indent=2))
