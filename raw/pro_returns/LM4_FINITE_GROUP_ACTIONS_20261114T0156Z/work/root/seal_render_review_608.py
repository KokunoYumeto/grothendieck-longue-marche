#!/usr/bin/env python3
"""Seal actual root/peer visual review and exact final268 build bindings."""
from pathlib import Path
import datetime
import hashlib
import json

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'deliverable'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads((ROOT/p).read_text())
prep_path=ROOT/'work/root/render_preparation_608_final.json'
root_path=ROOT/'work/root/root_visual_review_608.json'
peer_path=ROOT/'work/part_c/render_review_608.json'
prior_path=ROOT/'work/root/render_review_600.json'
prep,root,peer,prior=[json.loads(p.read_text()) for p in [prep_path,root_path,peer_path,prior_path]]
qa,build=read('deliverable/pdf_qa.json'),read('deliverable/build_artifact.json')
pdf=OUT/'LM4_FINITE_GROUP_ACTIONS_paper.pdf'
expected='2038bacd186770710f3a949d2edf6adb92fb800ab6d531133088b6694fd07cd5'
assert sha(pdf)==expected==prep['sha256']==root['sha256']==peer['pdf']['sha256']
assert qa['sha256']==build['pdf_sha256']==expected
assert sha(peer_path)=='19e084cc0e3c0b39317b4076ed2781caa4a58c89d7e28f079d90e99f515621bb'
assert sha(root_path)=='74a43c5d4504b3e73a4f8af6d26cf3a54682f73de833b179bf073c21be349911'
assert sha(prior_path)==root['prior_review_sha256']
assert build['success'] and build['stage_count']==4
assert qa['pages']==peer['pdf']['pages']==608 and pdf.stat().st_size==4117520
assert peer['status']=='PASS' and not peer['visual_findings']['defects_found']
assert not root['issues'] and not qa['overfull_widths_pt']
assert peer['entire_final_build_logs_and_all_four_stage_outputs_read']
assert peer['all_four_exit_codes_zero']
assert root['actually_viewed_pages']==prep['root_pages']
assert peer['peer_freshly_viewed_pages']==prep['peer_pages']
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
 elif item['byte_identical_to_prior_600_image']:
  old=prior_images[item['page']];old_path=Path(old['path'])
  old_path=old_path if old_path.is_absolute() else ROOT/old_path
  assert item['page'] in prior['actually_viewed_pages']
  assert old['sha256']==item['sha256'] and old['bytes']==item['bytes']
  assert p.read_bytes()==old_path.read_bytes()
 else:
  assert item['page'] in root['images_opened_this_final_review']
 images.append(dict(item,path=str(p)))
pages=[x['page'] for x in images]
assert len(pages)==len(set(pages))==84
assert len(root['images_opened_this_final_review'])==11
assert len(peer['peer_freshly_viewed_pages'])==25
assert len(root['byte_identical_prior_review_pages'])==48
for item in peer['retained_log_copies']:
 src,copied=ROOT/item['source_path'],ROOT/item['path']
 assert item['read_in_full'] and sha(src)==sha(copied)==item['sha256']
 assert src.read_bytes()==copied.read_bytes()

typography=peer['assembly_f29_exact_comparison']
repair=ROOT/typography['root_typography_record']['path']
assert sha(repair)==typography['root_typography_record']['sha256']
assert typography['entire_forward_fragment_equals_assembled_fragment']
assert typography['entire_inverse_fragment_equals_frozen_proof']
assert typography['actual_fresh_final_page_checked']==596
addendum={
 'status':'PASS_FINAL_TYPOGRAPHY_GATE','equation':'F.29.25','page':596,
 'pdf_sha256':expected,'pdf_pages':608,
 'initial_repair_record':str(repair.relative_to(ROOT)),
 'initial_repair_record_sha256':sha(repair),
 'initial_record_preserved_byte_for_byte':True,
 'peer_review':str(peer_path.relative_to(ROOT)),'peer_review_sha256':sha(peer_path),
 'exact_assembled_fragment_sha256':typography['assembled_fragment_sha256'],
 'forward_and_inverse_full_fragment_comparisons':True,
 'final_image':next(x for x in images if x['page']==596),
 'overfull_boxes':0,'fresh_final_image_actually_viewed':True,
 'meaning':'This separate addendum completes the final gate left pending in the immutable initial repair record.'}
addendum_path=ROOT/'work/root/f29_typesetting_final_gate_608.json'
addendum_path.write_text(json.dumps(addendum,indent=2)+'\n')
review={
 'pdf':pdf.name,'sha256':expected,'pages':608,'pdf_bytes':pdf.stat().st_size,
 'actually_viewed_pages':pages,'actually_viewed_count':84,
 'root_actually_viewed_pages':prep['root_pages'],'peer_actually_viewed_pages':prep['peer_pages'],
 'root_images_opened_this_final_review':root['images_opened_this_final_review'],
 'peer_images_opened_this_final_review':peer['peer_freshly_viewed_pages'],
 'byte_identical_prior_review_images':root['byte_identical_prior_review_pages'],
 'prior_review':str(prior_path.relative_to(ROOT)),'prior_review_sha256':sha(prior_path),
 'root_review':str(root_path.relative_to(ROOT)),'root_review_sha256':sha(root_path),
 'independent_review':str(peer_path.relative_to(ROOT)),'independent_review_sha256':sha(peer_path),
 'render_preparation':str(prep_path.relative_to(ROOT)),'render_preparation_sha256':sha(prep_path),
 'reviewed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'method':'Root opened and actually viewed11 final PNGs; peer opened and actually viewed25. Forty-eight further final PNGs are whole-file byte-identical to the sealed600 images previously actually viewed. All84 final images, prior memberships and review bindings were checked. Rendering alone is not counted as viewing.',
 'new_proof_coverage':prep['new_proof_pages'],'scope_overview_coverage':prep['scope_overview_pages'],
 'historical_overflow_widths_pt':qa['historical_overflow_widths_pt'],
 'historical_passages_reviewed':prep['historical_passages'],
 'current_build_repairs':[{'path':str(addendum_path.relative_to(ROOT)),'sha256':sha(addendum_path)}],
 'log_review':{
  'stages_passed':4,'overfull_boxes':0,'overfull_greater_than_2pt':0,
  'missing_glyphs':0,'undefined_references_or_citations':0,'fatal_errors':0,
  'final_lualatex_log_read':True,'bibtex_log_read':True,
  'full_log_reader':'c89_review_and_general_c; root checked diagnostic and exact-file bindings.',
  'full_log_review_record':str(peer_path.relative_to(ROOT)),
  'final_log_sha256':sha(OUT/'LM4_FINITE_GROUP_ACTIONS_paper.log'),
  'final_bibtex_log_sha256':sha(OUT/'LM4_FINITE_GROUP_ACTIONS_paper.blg'),
  'diagnostic_counts':peer['final_log_notice_counts'],
  'nonfatal_notices':peer['notice_interpretations'],
  'stage_1_3_4_stdout_byte_identical':peer['stage_1_3_4_stdout_byte_identical'],
  'bibliographic_warning_scope':'Tukia Series A I number504 has no invented volume.',
  'bibliography_records':88,'cited_printed_entries':77},
 'visual_observations':'The complete new F29 proof and all historical overflow passages fit. The new F29.25 gathered row break retains the full matrix and tag. All selected equations, metadata, text, tables and page edges are legible without clipping, collisions, missing glyphs or malformed displays.',
 'issues':[],'rendered_images':images}
for p in [ROOT/'work/root/render_review_608.json',OUT/'render_review.json']:
 p.write_text(json.dumps(review,indent=2)+'\n')
print(json.dumps({'pdf_sha256':expected,'reviewed_pages':84,'root_fresh':11,
                  'peer_fresh':25,'whole_image_byte_identical_carry':48,
                  'review_sha256':sha(OUT/'render_review.json'),
                  'typography_final_gate_sha256':sha(addendum_path)},indent=2))
