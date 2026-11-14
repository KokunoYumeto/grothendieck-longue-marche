#!/usr/bin/env python3
"""Bind actual final611 visual review, exact carried images and complete log audit."""
from pathlib import Path
import datetime
import hashlib
import json

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'deliverable'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda name:json.loads((ROOT/name).read_text())
def binding(name):
 p=ROOT/name
 return {'path':name,'bytes':p.stat().st_size,'sha256':sha(p)}
prep_path=ROOT/'work/root/render_preparation_611_final.json'
root_path=ROOT/'work/root/root_visual_review_611.json'
peer_path=ROOT/'work/part_c/render_review_611.json'
prior_path=ROOT/'work/root/render_review_608.json'
prep,root,peer,prior=[json.loads(p.read_text()) for p in [prep_path,root_path,peer_path,prior_path]]
qa,build=read('deliverable/pdf_qa.json'),read('deliverable/build_artifact.json')
pdf=OUT/'LM4_FINITE_GROUP_ACTIONS_paper.pdf'
expected='6eb08722ef726aaa8894facf55915238861d7981c9d86d63cdc62e6e7dc47a97'
assert sha(pdf)==expected==prep['sha256']==root['sha256']==peer['pdf']['sha256']
assert qa['sha256']==build['pdf_sha256']==expected
assert sha(peer_path)=='a3b34404998973913fb4e4c3afd8d748bd9cbdb1770c1405e74730f614887cb4'
assert sha(root_path)=='3e975fb5daee725a5f5af05ac532ff1244a775a875cbb7c7fda44a4f9931d474'
assert sha(prior_path)==root['prior_review_sha256']
assert build['success'] and build['stage_count']==4
assert qa['pages']==peer['pdf']['pages']==611 and pdf.stat().st_size==4139349
assert peer['status']=='PASS' and not peer['visual_findings']['defects_found']
assert not root['issues'] and not qa['overfull_widths_pt']
assert peer['entire_final_build_logs_and_all_four_stage_outputs_read']
assert peer['all_four_exit_codes_zero'] and peer['stage_3_4_stdout_byte_identical']
assert root['actually_viewed_pages']==prep['root_pages']
assert peer['peer_freshly_viewed_pages']==prep['peer_pages']
assert peer['whole_png_carry_audit']['all_passed'] and peer['whole_png_carry_audit']['count']==79
prior_images={x['page']:x for x in prior['rendered_images']}
peer_images={x['page']:x for x in peer['images']}
images=[]
for item in prep['images']:
 p=ROOT/item['path']
 assert p.is_file() and sha(p)==item['sha256'] and p.stat().st_size==item['bytes']
 if item['reviewer']=='peer':
  q=peer_images[item['page']]
  assert q['actual_viewed'] and q['fresh_view_for_this_final_pdf']
  assert q['sha256']==item['sha256'] and q['bytes']==item['bytes']
 elif item['byte_identical_to_prior_608_image']:
  old=prior_images[item['page']];old_path=Path(old['path'])
  old_path=old_path if old_path.is_absolute() else ROOT/old_path
  assert item['page'] in prior['actually_viewed_pages']
  assert old['sha256']==item['sha256'] and old['bytes']==item['bytes']
  assert p.read_bytes()==old_path.read_bytes()
 else:
  assert item['page'] in root['images_opened_this_final_review']
 images.append(dict(item,path=str(p)))
pages=[x['page'] for x in images]
assert len(pages)==len(set(pages))==88
assert len(root['images_opened_this_final_review'])==4
assert len(peer['peer_freshly_viewed_pages'])==5
assert len(root['byte_identical_prior_review_pages'])==79
for item in peer['retained_log_copies']:
 src,copied=ROOT/item['source_path'],ROOT/item['path']
 assert item['read_in_full'] and sha(src)==sha(copied)==item['sha256']
 assert src.read_bytes()==copied.read_bytes()
for item in peer['frozen_source_and_review_bindings_unchanged']:
 actual=binding(item['path'])
 assert actual['sha256']==item['sha256'] and actual['bytes']==item['bytes']
for label in ['f29','f30']:
 comp=peer['assembly_'+label+'_exact_comparison']
 assert comp['entire_forward_fragment_equals_assembled_fragment']
 assert comp['entire_inverse_fragment_equals_frozen_proof']
assert peer['assembly_f29_exact_comparison']['whole_png_equal_to_that_reviewed_page']
assert peer['assembly_f30_exact_comparison']['typography_repair_count']==0
repair=peer['assembly_f29_exact_comparison']['root_typography_record']
assert binding(repair['path'])==repair
f29_gate={'status':'PASS_FINAL_TYPOGRAPHY_GATE','equation':'F.29.25','page':596,
 'pdf_sha256':expected,'pdf_pages':611,'immutable_initial_repair':repair,
 'sealed_prior_completion':binding('work/root/f29_typesetting_final_gate_608.json'),
 'peer_review':binding('work/part_c/render_review_611.json'),
 'exact_forward_and_inverse_fragment_comparisons':True,
 'image':next(x for x in images if x['page']==596),
 'whole_png_equal_to_previously_actually_viewed_final_608_page':True,
 'fresh_view_for_this_pdf_claimed':False,'overfull_boxes':0}
f30_gate={'status':'PASS_FINAL_DOCUMENT_GATE','claim':'F.30','pdf_sha256':expected,'pdf_pages':611,
 'accepted_proof':binding('work/part_a/f_product_one_first_scalar_field_images.tex'),
 'mathematical_acceptance':binding('work/root/final_new_claim_acceptance_269.json'),
 'exact_forward_and_inverse_fragment_comparisons':True,'typography_changes':0,
 'assembled_fragment_sha256':peer['assembly_f30_exact_comparison']['assembled_fragment_sha256'],
 'actual_fresh_root_views':[x for x in images if x['page'] in range(598,602)],
 'overfull_boxes':0,'issues':[]}
for name,record in [('f29_typesetting_final_gate_611.json',f29_gate),('f30_final_document_gate_611.json',f30_gate)]:
 (ROOT/'work/root'/name).write_text(json.dumps(record,indent=2)+'\n')
review={
 'pdf':pdf.name,'sha256':expected,'pages':611,'pdf_bytes':pdf.stat().st_size,
 'actually_viewed_pages':pages,'actually_viewed_count':88,
 'root_actually_viewed_pages':prep['root_pages'],'peer_actually_viewed_pages':prep['peer_pages'],
 'root_images_opened_this_final_review':root['images_opened_this_final_review'],
 'peer_images_opened_this_final_review':peer['peer_freshly_viewed_pages'],
 'byte_identical_prior_review_images':root['byte_identical_prior_review_pages'],
 'prior_review':str(prior_path.relative_to(ROOT)),'prior_review_sha256':sha(prior_path),
 'prior_pdf':binding('work/root/prior_268_snapshot/paper.pdf'),
 'root_review':str(root_path.relative_to(ROOT)),'root_review_sha256':sha(root_path),
 'independent_review':str(peer_path.relative_to(ROOT)),'independent_review_sha256':sha(peer_path),
 'render_preparation':str(prep_path.relative_to(ROOT)),'render_preparation_sha256':sha(prep_path),
 'reviewed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'method':'Root actually viewed4 final PNGs and peer actually viewed5. Seventy-nine further final PNGs equal the complete sealed608 images byte for byte; prior view membership, size and digest were checked independently by both reviewers. All88 current images are bound to the final611 PDF. Rendering alone is not counted as viewing.',
 'new_proof_coverage':prep['new_proof_pages'],'scope_overview_coverage':prep['scope_overview_pages'],
 'historical_overflow_widths_pt':qa['historical_overflow_widths_pt'],
 'historical_passages_reviewed':prep['historical_passages'],
 'current_document_gates':[binding('work/root/f29_typesetting_final_gate_611.json'),binding('work/root/f30_final_document_gate_611.json')],
 'log_review':{
  'stages_passed':4,'overfull_boxes':0,'overfull_greater_than_2pt':0,
  'missing_glyphs':0,'undefined_references_or_citations':0,'fatal_errors':0,
  'final_lualatex_log_read':True,'bibtex_log_read':True,
  'full_log_reader':'c89_review_and_general_c; root checked diagnostic and exact-file bindings.',
  'full_log_review_record':str(peer_path.relative_to(ROOT)),
  'final_log_sha256':sha(OUT/'LM4_FINITE_GROUP_ACTIONS_paper.log'),
  'final_bibtex_log_sha256':sha(OUT/'LM4_FINITE_GROUP_ACTIONS_paper.blg'),
  'diagnostic_counts':peer['final_log_notice_counts'],'nonfatal_notices':peer['notice_interpretations'],
  'stage_1_3_4_stdout_byte_identical':False,'stage_3_4_stdout_byte_identical':True,
  'bibliographic_warning_scope':'Tukia Series A I number504 has no invented volume.',
  'bibliography_records':88,'cited_printed_entries':77},
 'visual_observations':'All four F30 pages were freshly viewed. Its original maps, source table, cross-factor proof, trace formulas and manuscript metadata fit without clipping or collisions. Every earlier selected passage, including F29.25, has exact whole-image carry or a fresh view. Five changed reference pages were freshly viewed and are clear.',
 'issues':[],'rendered_images':images}
for path in [ROOT/'work/root/render_review_611.json',OUT/'render_review.json']:
 path.write_text(json.dumps(review,indent=2)+'\n')
print(json.dumps({'pdf_sha256':expected,'reviewed_pages':88,'root_fresh':4,'peer_fresh':5,
 'whole_image_byte_identical_carry':79,'review_sha256':sha(OUT/'render_review.json')},indent=2))
