#!/usr/bin/env python3
"""Seal actual final619 views, complete PNG carries, logs and exact source maps."""
from pathlib import Path
from hashlib import sha256
import datetime
import json

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'deliverable'
sha=lambda p:sha256(p.read_bytes()).hexdigest()
read=lambda name:json.loads((ROOT/name).read_text())
def binding(name):
    p=ROOT/name
    return {'path':name,'bytes':p.stat().st_size,'sha256':sha(p)}
prep_path=ROOT/'work/root/render_preparation_619_final.json'
root_path=ROOT/'work/root/root_visual_review_619.json'
peer_path=ROOT/'work/part_c/render_review_619.json'
prior_path=ROOT/'work/root/render_review_611.json'
prep,root,peer,prior=[json.loads(p.read_text()) for p in [prep_path,root_path,peer_path,prior_path]]
qa,build=read('deliverable/pdf_qa.json'),read('deliverable/build_artifact.json')
pdf=OUT/'LM4_FINITE_GROUP_ACTIONS_paper.pdf'
expected='4546799ef3198a11c19a7b7a81e3d9a20aca2016c9f97633826fd971ffc02175'
assert sha(pdf)==expected==prep['sha256']==root['sha256']==peer['pdf']['sha256']
assert qa['sha256']==build['pdf_sha256']==expected
assert sha(peer_path)=='e1ee62c58e81aa0f0a64cfdf279287c05370e4ec9e539548bf576c11bd93d528'
assert sha(root_path)=='5b2d6945100fe1ef68e09360e88add3995eb3b067d14341d15568590d395cf17'
assert sha(prior_path)==root['prior_review_sha256']
assert build['success'] and build['stage_count']==4
assert qa['pages']==peer['pdf']['pages']==619 and pdf.stat().st_size==4194159
assert peer['status']=='PASS' and not peer['visual_findings']['defects_found']
assert not root['issues'] and not qa['overfull_widths_pt']
assert peer['entire_final_build_logs_and_all_four_stage_outputs_read']
assert peer['all_four_exit_codes_zero'] and peer['stage_1_3_4_stdout_byte_identical']
assert peer['stage_3_4_stdout_byte_identical']
assert root['actually_viewed_pages']==prep['root_pages']
assert peer['peer_freshly_viewed_pages']==prep['peer_pages']
assert peer['whole_png_carry_audit']['all_passed'] and peer['whole_png_carry_audit']['count']==82
prior_images={x['page']:x for x in prior['rendered_images']}
peer_images={x['page']:x for x in peer['images']}
images=[]
for item in prep['images']:
    p=ROOT/item['path']
    assert sha(p)==item['sha256'] and p.stat().st_size==item['bytes']
    if item['reviewer']=='peer':
        q=peer_images[item['page']]
        assert q['actual_viewed'] and q['fresh_view_for_this_final_pdf']
        assert q['sha256']==item['sha256'] and q['bytes']==item['bytes']
    elif item['byte_identical_to_prior_611_image']:
        old=prior_images[item['page']];old_path=Path(old['path'])
        old_path=old_path if old_path.is_absolute() else ROOT/old_path
        assert item['page'] in prior['actually_viewed_pages']
        assert old['sha256']==item['sha256'] and old['bytes']==item['bytes']
        assert p.read_bytes()==old_path.read_bytes()
    else:
        assert item['page'] in root['images_opened_this_final_review']
    images.append(dict(item,path=str(p)))
pages=[x['page'] for x in images]
assert len(pages)==len(set(pages))==96
assert len(root['images_opened_this_final_review'])==4
assert len(peer['peer_freshly_viewed_pages'])==10
assert len(root['byte_identical_prior_review_pages'])==82
for item in peer['retained_log_copies']:
    src,copied=ROOT/item['source_path'],ROOT/item['path']
    assert item['read_in_full'] and sha(src)==sha(copied)==item['sha256']
    assert src.read_bytes()==copied.read_bytes()
for item in peer['frozen_source_and_review_bindings_unchanged']:
    actual=binding(item['path'])
    assert actual['sha256']==item['sha256'] and actual['bytes']==item['bytes']

# Execute the complete source/assembled-fragment maps again at root.
paper=(OUT/'LM4_FINITE_GROUP_ACTIONS_paper.tex').read_text()
source_comparisons={}
for label in ['f29','f30','f31']:
    comp=peer['assembly_'+label+'_exact_comparison']
    assert comp['entire_forward_fragment_equals_assembled_fragment']
    assert comp['entire_inverse_fragment_equals_frozen_proof']
    source=(ROOT/comp['frozen_source']['path']).read_text()
    meta=read(comp['frozen_metadata']['path'])
    passage='\\passage{'+meta['manuscript_passages'].removesuffix('.')+'}'
    assert passage==comp['exact_added_passage_line']
    transformed=source
    if comp['typography_repair_count']:
        repair=read(comp['root_typography_record']['path'])
        assert binding(comp['root_typography_record']['path'])==comp['root_typography_record']
        assert transformed.count(comp['old'])==1 and transformed.count(comp['new'])==0
        transformed=transformed.replace(comp['old'],comp['new'],1)
    assert transformed.count('\\end{claim}')==1
    insertion='\\end{claim}\n'+passage+'\n'
    transformed=transformed.replace('\\end{claim}',insertion,1)
    assert paper.count(transformed)==1,label
    assert sha256(transformed.encode()).hexdigest()==comp['assembled_fragment_sha256']
    inverse=transformed.replace(insertion,'\\end{claim}',1)
    if comp['typography_repair_count']:
        inverse=inverse.replace(comp['new'],comp['old'],1)
    assert inverse==source,label
    source_comparisons[label]={'entire_forward_fragment_equals_assembled_fragment':True,
        'entire_inverse_fragment_equals_frozen_proof':True,
        'assembled_fragment_sha256':sha256(transformed.encode()).hexdigest(),
        'typography_repair_count':comp['typography_repair_count']}
assert peer['assembly_f29_exact_comparison']['whole_png_equal_to_that_reviewed_page']
assert peer['assembly_f30_exact_comparison']['typography_repair_count']==0
assert peer['assembly_f31_exact_comparison']['typography_repair_count']==1

f29_gate={'status':'PASS_FINAL_TYPOGRAPHY_GATE','equation':'F.29.25','page':596,
    'pdf_sha256':expected,'pdf_pages':619,
    'immutable_initial_repair':binding('work/root/f29_typesetting_repair.json'),
    'sealed_prior_completion':binding('work/root/f29_typesetting_final_gate_611.json'),
    'peer_review':binding('work/part_c/render_review_619.json'),
    'root_complete_source_comparison':source_comparisons['f29'],
    'image':next(x for x in images if x['page']==596),
    'whole_png_equal_to_previously_actually_viewed_final611_page':True,
    'fresh_view_for_this_pdf_claimed':False,'overfull_boxes':0}
f30_gate={'status':'PASS_FINAL_DOCUMENT_GATE','claim':'F.30','pdf_sha256':expected,'pdf_pages':619,
    'accepted_proof':binding('work/part_a/f_product_one_first_scalar_field_images.tex'),
    'mathematical_acceptance':binding('work/root/final_new_claim_acceptance_269.json'),
    'root_complete_source_comparison':source_comparisons['f30'],
    'final_page_images':[x for x in images if x['page'] in range(598,602)],
    'whole_png_carry_pages':[598,599,600],'freshly_viewed_peer_pages':[601],
    'overfull_boxes':0,'issues':[]}
f31_gate={'status':'PASS_FINAL_DOCUMENT_AND_TYPOGRAPHY_GATE','claim':'F.31',
    'pdf_sha256':expected,'pdf_pages':619,
    'accepted_proof':binding('work/part_a/f_full_product_one_affine_images.tex'),
    'mathematical_acceptance':binding('work/root/final_new_claim_acceptance_270.json'),
    'immutable_initial_repair':binding('work/root/f31_typesetting_repair.json'),
    'root_complete_source_comparison':source_comparisons['f31'],
    'initial_overfull_boxes':1,'initial_overfull_width_pt':2.14531,
    'final_overfull_boxes':0,'initial_page_actually_viewed_by_root':603,
    'root_fresh_pages':[602,603,604,605],'peer_fresh_pages':[606,607,608,609],
    'all_proof_pages_actually_viewed':list(range(602,610)),
    'final_page_images':[x for x in images if x['page'] in range(602,610)],'issues':[]}
gates=[('f29_typesetting_final_gate_619.json',f29_gate),
       ('f30_final_document_gate_619.json',f30_gate),
       ('f31_final_document_gate_619.json',f31_gate)]
for name,record in gates:
    (ROOT/'work/root'/name).write_text(json.dumps(record,indent=2)+'\n')
review={
    'pdf':pdf.name,'sha256':expected,'pages':619,'pdf_bytes':pdf.stat().st_size,
    'actually_viewed_pages':pages,'actually_viewed_count':96,
    'root_actually_viewed_pages':prep['root_pages'],'peer_actually_viewed_pages':prep['peer_pages'],
    'root_images_opened_this_final_review':root['images_opened_this_final_review'],
    'peer_images_opened_this_final_review':peer['peer_freshly_viewed_pages'],
    'byte_identical_prior_review_images':root['byte_identical_prior_review_pages'],
    'prior_review':str(prior_path.relative_to(ROOT)),'prior_review_sha256':sha(prior_path),
    'prior_pdf':binding('work/root/prior_269_snapshot/paper.pdf'),
    'root_review':str(root_path.relative_to(ROOT)),'root_review_sha256':sha(root_path),
    'independent_review':str(peer_path.relative_to(ROOT)),'independent_review_sha256':sha(peer_path),
    'render_preparation':str(prep_path.relative_to(ROOT)),'render_preparation_sha256':sha(prep_path),
    'reviewed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'method':'Root actually viewed4 final PNGs and peer actually viewed10. Eighty-two further entire PNGs equal previously viewed sealed611 images byte for byte; both reviewers independently checked complete size, digest, bytes and prior-view membership. All96 current images are bound to the final619 PDF. Rendering alone is not counted as viewing.',
    'new_proof_coverage':prep['new_proof_pages'],'scope_overview_coverage':prep['scope_overview_pages'],
    'historical_overflow_widths_pt':qa['historical_overflow_widths_pt'],
    'historical_passages_reviewed':prep['historical_passages'],
    'current_document_gates':[binding('work/root/'+name) for name,_ in gates],
    'log_review':{'stages_passed':4,'overfull_boxes':0,'overfull_greater_than_2pt':0,
        'missing_glyphs':0,'undefined_references_or_citations':0,'fatal_errors':0,
        'final_lualatex_log_read':True,'bibtex_log_read':True,
        'full_log_reader':'c89_review_and_general_c; root checked diagnostic and exact-file bindings.',
        'full_log_review_record':str(peer_path.relative_to(ROOT)),
        'final_log_sha256':sha(OUT/'LM4_FINITE_GROUP_ACTIONS_paper.log'),
        'final_bibtex_log_sha256':sha(OUT/'LM4_FINITE_GROUP_ACTIONS_paper.blg'),
        'diagnostic_counts':peer['final_log_notice_counts'],'nonfatal_notices':peer['notice_interpretations'],
        'stage_1_3_4_stdout_byte_identical':True,'stage_3_4_stdout_byte_identical':True,
        'bibliographic_warning_scope':'Tukia Series A I number504 has no invented volume.',
        'bibliography_records':88,'cited_printed_entries':77},
    'visual_observations':'All eight F31 proof pages were freshly viewed, including the repaired crossing tuple, every displayed moving row, all fifteen sign strata and the final kernel/trace maps. The changed adjacent F30 page and five changed reference samples were also freshly viewed. All inherited selected passages, including the notation concordance and F29.25 repair, have complete-PNG carry or a fresh actual view.',
    'issues':[],'rendered_images':images}
for path in [ROOT/'work/root/render_review_619.json',OUT/'render_review.json']:
    path.write_text(json.dumps(review,indent=2)+'\n')
print(json.dumps({'pdf_sha256':expected,'reviewed_pages':96,'root_fresh':4,'peer_fresh':10,
    'whole_image_byte_identical_carry':82,'review_sha256':sha(OUT/'render_review.json')},indent=2))
