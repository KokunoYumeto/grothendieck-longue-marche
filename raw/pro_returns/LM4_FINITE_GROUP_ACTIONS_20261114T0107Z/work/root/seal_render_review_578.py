#!/usr/bin/env python3
"""Bind the completed actual-image review to the frozen262-claim PDF."""
from pathlib import Path
import datetime
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'deliverable'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def read(name):
    return json.loads((ROOT / name).read_text())

prep_path = ROOT / 'work/root/render_preparation_578_final.json'
prep = json.loads(prep_path.read_text())
peer_path = ROOT / 'work/part_c/render_review_578.json'
peer = json.loads(peer_path.read_text())
prior_path = ROOT / 'work/root/render_review_567.json'
prior = json.loads(prior_path.read_text())
qa = read('deliverable/pdf_qa.json')
build = read('deliverable/build_artifact.json')
pdf = OUT / 'LM4_FINITE_GROUP_ACTIONS_paper.pdf'
pdf_hash = sha(pdf)
assert pdf_hash == '7b32432e84921f17f1a8635e03621a30370b4f5254a1ea5656f0b8a0b1aa65ee'
assert pdf_hash == prep['sha256'] == peer['pdf_sha256'] == qa['sha256'] == build['pdf_sha256']
assert sha(peer_path) == '64ad49ca83ab1e52fe314e3cf02afb538e341b6ea974c5ad4bc8a1e75f8ab9d3'
assert sha(prior_path) == prep['prior_review_sha256']
assert build['success'] and build['stage_count'] == 4
assert qa['pages'] == peer['pdf_pages'] == 578
assert not qa['overfull_widths_pt'] and qa['overfull_greater_than_2pt'] == 0
assert not peer['remaining_visual_issues']

# These39 fresh images were actually opened and seen by root, including a
# successful reopening of160/303 after the earlier truncated tool result.
root_fresh = [86,87,120,141,142,143,160,303,304,305,481,482,483,534,
              538,539,540,541,542,543,544,546,549,550,551,552,553,554,
              555,556,557,558,559,560,561,569,573,576,578]
assert root_fresh == prep['root_fresh_pages']
peer_pages = peer['pages_covered_by_actual_image_viewing']
peer_fresh = peer['fresh_final_pages_actually_viewed']
assert peer_pages == sorted(prep['peer_assigned_pages'] + [351])
assert peer_fresh == sorted(prep['peer_fresh_pages'] + [351])
pages = sorted(prep['root_assigned_pages'] + peer_pages)
reused = prep['byte_identical_prior_review_pages']
assert len(pages) == len(set(pages)) == 104
assert sorted(root_fresh + peer_fresh + reused) == pages
assert len(root_fresh) == 39 and len(peer_fresh) == 26 and len(reused) == 39

images = list(prep['images'])
extra = next(im for im in peer['pages'] if im['page'] == 351)
images.append({'page':351, 'path':extra['final_image'],
               'sha256':extra['final_sha256'], 'bytes':extra['final_bytes'],
               'extra_historical_equation_page':True})
images.sort(key=lambda im:im['page'])
assert [im['page'] for im in images] == pages
prior_images = {im['page']:im for im in prior['rendered_images']}
for im in images:
    p = Path(im['path'])
    assert p.is_file() and p.stat().st_size == im['bytes'] and sha(p) == im['sha256'], p
    if im['page'] in reused:
        old = prior_images[im['page']]
        old_path = Path(old['path'])
        assert im['page'] in prior['actually_viewed_pages']
        assert old['sha256'] == im['sha256'] and old_path.read_bytes() == p.read_bytes()
for im in peer['pages']:
    assert sha(Path(im['final_image'])) == im['final_sha256']
for item in peer['build_review']['files']:
    original = ROOT / item['original']['path']
    sealed = ROOT / item['sealed_copy']['path']
    assert sha(original) == item['original']['sha256']
    assert original.read_bytes() == sealed.read_bytes()

review = {
    'pdf':pdf.name, 'sha256':pdf_hash, 'pages':578, 'pdf_bytes':pdf.stat().st_size,
    'actually_viewed_pages':pages, 'actually_viewed_count':len(pages),
    'root_actually_viewed_pages':prep['root_assigned_pages'],
    'peer_actually_viewed_pages':peer_pages,
    'root_images_opened_this_final_review':root_fresh,
    'peer_images_opened_this_final_review':peer_fresh,
    'byte_identical_prior_review_images':reused,
    'prior_review':'work/root/render_review_567.json', 'prior_review_sha256':sha(prior_path),
    'independent_review':'work/part_c/render_review_578.json',
    'independent_review_sha256':sha(peer_path),
    'render_preparation':'work/root/render_preparation_578_final.json',
    'render_preparation_sha256':sha(prep_path),
    'reviewed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'method':('Root actually viewed all39 fresh assigned final-PDF PNGs. The initial '
              'truncated160/303 result was not counted; both were reopened and seen. '
              'The peer actually viewed26 fresh final-PDF PNGs, including351 added '
              'after locating the historical D.37o equation. All39 reused final PNGs '
              'were verified byte for byte and by SHA-256 against previously actually '
              'viewed final567 PNGs and their sealed review. Every104 final image '
              'hash was checked by this script. Rendering alone is never counted as viewing.'),
    'new_proof_coverage':{
        'C85':list(range(277,283)), 'C86':list(range(282,286)),
        'C87':list(range(285,288)), 'C88':list(range(287,291)),
        'C89':list(range(290,294)), 'C90':list(range(293,296)),
        'D78':list(range(466,471)), 'F23':list(range(555,563)),
        'F24':list(range(562,567)), 'F25':list(range(566,569)),
        'F20_coordinate_calibration':list(range(538,545)),
        'F22_coordinate_calibration':list(range(549,556)),
        'current_scope_overviews':[85,86,87,303,304,305,481,482,483],
        'bibliography_sample':[569,573,576,578]},
    'historical_overflow_widths_pt':qa['historical_overflow_widths_pt'],
    'historical_passages_reviewed':{
        'first-page notation table':[1], 'B17 inline list':[29,30],
        'B34 comparison display':[56,57], 'B36 filenames':[59],
        'B37 filenames':[61,62,63,64], 'D37o deck display':[351],
        'C45.4 compatible-group display':[141,142,143],
        'C65.2 finite-word path display':[207,208],
        'D74.1 normalized involution display':[449],
        'F19.9 fiber-product alignment':[534],
        'C77.4 former invalid alignment repair':[249],
        'F21 exponent-pair list':[546]},
    'current_build_repairs':[{
        'source':'work/part_a/f_rank_one_marginal_obstruction.tex',
        'repair':'Added the two omitted closing display delimiters afterF24.1 andF24.4; mathematics and certificate unchanged.',
        'record':'work/root/f24_typesetting_repair.json', 'reviewed_pages':[562,563,564,565,566]}],
    'log_review':{
        'stages_passed':4, 'overfull_boxes':0, 'overfull_greater_than_2pt':0,
        'missing_glyphs':0, 'undefined_references_or_citations':0, 'fatal_errors':0,
        'final_lualatex_log_read':True, 'bibtex_log_read':True,
        'full_log_reader':'c89_review_and_general_c; root checked the exact final diagnostic records and log bindings.',
        'full_log_review_record':'work/part_c/render_review_578.json',
        'final_log_sha256':sha(OUT/'LM4_FINITE_GROUP_ACTIONS_paper.log'),
        'final_bibtex_log_sha256':sha(OUT/'LM4_FINITE_GROUP_ACTIONS_paper.blg'),
        'diagnostic_counts':peer['build_review']['diagnostic_counts'],
        'nonfatal_notices':peer['build_review']['nonfatal_notices'],
        'bibliographic_warning_scope':'C_Tukia1972 is Series A I, number504; no fictitious volume supplied.'},
    'visual_observations':('All selected text, equations, tables, diagrams, page edges and tags are legible. '
                           'The actual skeleton section, cocompact lift proof, finite-field coefficient charts '
                           'and affine scalar-field proof fit. All historical overflow passages were checked '
                           'at their final page locations. No clipped text, overlaps or missing glyphs observed.'),
    'issues':[], 'rendered_images':images}
for path in [ROOT/'work/root/render_review_578.json', OUT/'render_review.json']:
    path.write_text(json.dumps(review,indent=2)+'\n')

extra_path = ROOT/'work/root/checkpoint_262_extra_paths.json'
extras = json.loads(extra_path.read_text())
extras += ['work/root/seal_render_review_578.py','work/root/render_review_578.json',
           'work/root/render_preparation_578_final.json','work/part_c/render_review_578.json']
extras += [item['sealed_copy']['path'] for item in peer['build_review']['files']]
extras += [str(Path(im['path']).relative_to(ROOT)) for im in images]
extra_path.write_text(json.dumps(list(dict.fromkeys(extras)),indent=2)+'\n')
print(json.dumps({'pdf_sha256':pdf_hash, 'reviewed_pages':len(pages),
                  'root_fresh':len(root_fresh), 'peer_fresh':len(peer_fresh),
                  'exact_image_reuse':len(reused), 'review_sha256':sha(OUT/'render_review.json')},indent=2))
