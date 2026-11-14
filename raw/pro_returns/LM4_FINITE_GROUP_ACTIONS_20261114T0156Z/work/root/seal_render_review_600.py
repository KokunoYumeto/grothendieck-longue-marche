#!/usr/bin/env python3
"""Seal completed root/peer actual-image review for the exact267-claim PDF."""
from pathlib import Path
import datetime, hashlib, json

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT/'deliverable'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
read = lambda name: json.loads((ROOT/name).read_text())
prep_path = ROOT/'work/root/render_preparation_600_final.json'
peer_path = ROOT/'work/part_c/render_review_600.json'
root_path = ROOT/'work/root/root_visual_review_600.json'
prior_path = ROOT/'work/root/render_review_587.json'
prep,peer,root,prior = [json.loads(p.read_text()) for p in
                       [prep_path,peer_path,root_path,prior_path]]
qa,build = read('deliverable/pdf_qa.json'),read('deliverable/build_artifact.json')
pdf = OUT/'LM4_FINITE_GROUP_ACTIONS_paper.pdf'
expected = '42ef0d3fff1be048a0c3d09f065c19114341f15174930173ce847bbcd0b0ae8f'
assert sha(pdf)==expected==prep['sha256']==root['sha256']==peer['pdf']['sha256']
assert qa['sha256']==build['pdf_sha256']==expected
assert sha(peer_path)=='4aa69acbd3f4588a20c6edecb025e47f6afd6350285cefd7834914442b4446a9'
assert sha(prior_path)==root['prior_review_sha256']
assert build['success'] and build['stage_count']==4
assert qa['pages']==peer['pdf']['pages']==600 and pdf.stat().st_size==4061958
assert peer['status']=='PASS' and not peer['visual_findings']['defects_found']
assert not root['issues'] and not qa['overfull_widths_pt']
assert peer['entire_final_build_logs_and_all_four_stage_outputs_read']
assert peer['all_four_exit_codes_zero']
assert root['actually_viewed_pages']==prep['root_pages']
assert peer['peer_freshly_viewed_pages']==prep['peer_pages']
images=[]
prior_images={x['page']:x for x in prior['rendered_images']}
peer_images={x['page']:x for x in peer['images']}
for item in prep['images']:
    p=ROOT/item['path']
    assert p.is_file() and sha(p)==item['sha256'] and p.stat().st_size==item['bytes']
    if item['reviewer']=='peer':
        q=peer_images[item['page']]
        assert q['actual_viewed'] and q['fresh_view_for_this_final_pdf']
        assert q['sha256']==item['sha256'] and q['bytes']==item['bytes']
    elif item['byte_identical_to_prior_587_image']:
        old=prior_images[item['page']]
        assert item['page'] in prior['actually_viewed_pages']
        assert old['sha256']==item['sha256'] and old['bytes']==item['bytes']
        assert p.read_bytes()==Path(old['path']).read_bytes()
    else:
        assert item['page'] in root['images_opened_this_final_review']
    images.append(dict(item,path=str(p)))
pages=[x['page'] for x in images]
assert len(pages)==len(set(pages))==74
assert len(root['images_opened_this_final_review'])==12
assert len(peer['peer_freshly_viewed_pages'])==33
assert len(root['byte_identical_prior_review_pages'])==29
for item in peer['retained_log_copies']:
    source=ROOT/item['source_path'];copied=ROOT/item['path']
    assert item['read_in_full'] and sha(source)==sha(copied)==item['sha256']
    assert source.read_bytes()==copied.read_bytes()
review={
    'pdf':pdf.name,'sha256':expected,'pages':600,'pdf_bytes':pdf.stat().st_size,
    'actually_viewed_pages':pages,'actually_viewed_count':74,
    'root_actually_viewed_pages':prep['root_pages'],
    'peer_actually_viewed_pages':prep['peer_pages'],
    'root_images_opened_this_final_review':root['images_opened_this_final_review'],
    'peer_images_opened_this_final_review':peer['peer_freshly_viewed_pages'],
    'byte_identical_prior_review_images':root['byte_identical_prior_review_pages'],
    'prior_review':'work/root/render_review_587.json','prior_review_sha256':sha(prior_path),
    'root_review':'work/root/root_visual_review_600.json','root_review_sha256':sha(root_path),
    'independent_review':'work/part_c/render_review_600.json','independent_review_sha256':sha(peer_path),
    'render_preparation':'work/root/render_preparation_600_final.json','render_preparation_sha256':sha(prep_path),
    'reviewed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'method':'Root opened and actually viewed12 final PNGs; peer opened and actually viewed33. Twenty-nine further final PNGs are whole-file byte-identical to the sealed587 images previously actually viewed. All74 final images and their review bindings were checked here. Rendering alone is not counted as viewing.',
    'new_proof_coverage':prep['new_proof_pages'],
    'scope_overview_coverage':prep['scope_overview_pages'],
    'historical_overflow_widths_pt':qa['historical_overflow_widths_pt'],
    'historical_passages_reviewed':dict(prep['historical_passages'],C77_4=[250]),
    'current_build_repairs':[],
    'log_review':{
        'stages_passed':4,'overfull_boxes':0,'overfull_greater_than_2pt':0,
        'missing_glyphs':0,'undefined_references_or_citations':0,'fatal_errors':0,
        'final_lualatex_log_read':True,'bibtex_log_read':True,
        'full_log_reader':'c89_review_and_general_c; root checked all diagnostic and exact-file bindings.',
        'full_log_review_record':'work/part_c/render_review_600.json',
        'final_log_sha256':sha(OUT/'LM4_FINITE_GROUP_ACTIONS_paper.log'),
        'final_bibtex_log_sha256':sha(OUT/'LM4_FINITE_GROUP_ACTIONS_paper.blg'),
        'diagnostic_counts':peer['final_log_notice_counts'],
        'nonfatal_notices':peer['notice_interpretations'],
        'bibliographic_warning_scope':'Tukia Series A I number504 has no invented volume.',
        'bibliography_records':87,'cited_printed_entries':77},
    'visual_observations':'All selected equations, tags, text, manuscript metadata, tables and page edges are legible. The complete new C92, F27 and F28 proofs and every historical overflow passage fit. No clipping, collision, missing glyph or malformed display was observed.',
    'issues':[],'rendered_images':images}
for p in [ROOT/'work/root/render_review_600.json',OUT/'render_review.json']:
    p.write_text(json.dumps(review,indent=2)+'\n')
ep=ROOT/'work/root/checkpoint_267_extra_paths.json';extras=json.loads(ep.read_text())
extras+=['work/root/prepare_review_600.py','work/root/seal_render_review_600.py',
         'work/root/render_preparation_600_final.json','work/root/root_visual_review_600.json',
         'work/root/render_review_600.json','work/part_c/render_review_600.json',
         'work/root/verify_package_267.py']
extras+=[x['path'] for x in peer['retained_log_copies']]
extras+=[str(Path(x['path']).relative_to(ROOT)) for x in images]
ep.write_text(json.dumps(sorted(set(extras)),indent=2)+'\n')
print(json.dumps({'pdf_sha256':expected,'reviewed_pages':74,'root_fresh':12,
    'peer_fresh':33,'whole_image_byte_identical_carry':29,
    'review_sha256':sha(OUT/'render_review.json'),'extras':len(set(extras))},indent=2))
