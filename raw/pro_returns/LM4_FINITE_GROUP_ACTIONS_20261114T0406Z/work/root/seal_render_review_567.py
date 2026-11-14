#!/usr/bin/env python3
"""Seal records of actual page viewing against the final 258-claim build."""
from pathlib import Path
import datetime, hashlib, json

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'deliverable'
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):
    return json.loads((ROOT / p).read_text())

prep = read('work/root/render_preparation_567_final.json')
peer_path = ROOT / 'work/part_c/render_review_567.json'
peer = json.loads(peer_path.read_text())
initial_root = read('work/root/root_visual_review_567_initial.json')
qa = read('deliverable/pdf_qa.json')
pdf_hash = sha(OUT / 'LM4_FINITE_GROUP_ACTIONS_paper.pdf')
assert pdf_hash == prep['sha256'] == peer['pdf_sha256'] == qa['sha256']
assert pdf_hash == '5924d78e3b9162accc82097e84064634e6abd5ffab1127aaf80745836ed5a5d4'
root_fresh = [249,265,272,275,529,533,539,545,548,549,550,551,552,553,554,555,556,557,558,562,565,567]
assert root_fresh == prep['root_fresh_pages']
assert peer['fresh_final_pages_actually_viewed'] == prep['peer_fresh_pages']
assert peer['pages_covered_by_actual_image_viewing'] == prep['peer_assigned_pages']
assert not peer['remaining_issues']
pages = sorted(prep['root_assigned_pages'] + prep['peer_assigned_pages'])
assert len(pages) == len(set(pages)) == 92
assert sorted(root_fresh + prep['peer_fresh_pages'] + prep['byte_identical_initial_review_pages']) == pages
for im in prep['images']:
    p = Path(im['path'])
    assert p.is_file() and sha(p) == im['sha256'], p
    if 'byte_identical_to_actually_reviewed_initial567_page' in im:
        old = ROOT / f"work/root/rendered/review_567/page{im['page']:03d}.png"
        assert old.read_bytes() == p.read_bytes(), p
assert sha(peer_path) == '94d77a702a58d63b754e6a9fe1128262e3290deb5f7d6af040756a4fdf997f48'
assert sha(OUT / 'LM4_FINITE_GROUP_ACTIONS_paper.log') == peer['build_review']['final_build_log_sha256']
assert qa['overfull_greater_than_2pt'] == 0 and not qa['overfull_widths_pt']

review = {
    'pdf': 'LM4_FINITE_GROUP_ACTIONS_paper.pdf', 'sha256': pdf_hash, 'pages': 567,
    'actually_viewed_pages': pages, 'actually_viewed_count': len(pages),
    'root_actually_viewed_pages': prep['root_assigned_pages'],
    'peer_actually_viewed_pages': prep['peer_assigned_pages'],
    'root_images_opened_this_final_review': root_fresh,
    'peer_images_opened_this_final_review': prep['peer_fresh_pages'],
    'byte_identical_prior_review_images': prep['byte_identical_initial_review_pages'],
    'root_initial567_images_actually_opened': initial_root['actually_opened_pages'],
    'initial_root_review': 'work/root/root_visual_review_567_initial.json',
    'initial_root_review_sha256': sha(ROOT/'work/root/root_visual_review_567_initial.json'),
    'initial_peer_review': 'work/part_c/render_review_567_initial.json',
    'initial_peer_review_sha256': sha(ROOT/'work/part_c/render_review_567_initial.json'),
    'prior541_review': 'work/root/render_review_541.json',
    'prior541_review_sha256': sha(ROOT/'work/root/render_review_541.json'),
    'independent_review': 'work/part_c/render_review_567.json',
    'independent_review_sha256': sha(peer_path),
    'render_preparation': 'work/root/render_preparation_567_final.json',
    'render_preparation_sha256': sha(ROOT/'work/root/render_preparation_567_final.json'),
    'reviewed_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'method': ('Root actually opened all 22 changed/new final images in batches of at most two. '
               'The final images for pages554 and555 were reopened after a truncated tool result; '
               'the truncated result was not counted as viewing. The independent reviewer actually '
               'opened the four changed final peer images. All other66 selected final images were '
               'verified byte for byte against images actually viewed in the sealed initial567 '
               'review, including its explicitly recorded prior541 byte-identical reuse. '
               'Every final image hash was independently checked again by this sealing script. '
               'Rendering alone is never counted as viewing.'),
    'new_proof_coverage': {
        'C85':list(range(277,283)), 'C86':list(range(282,286)),
        'C87':list(range(285,288)), 'C88':list(range(287,291)),
        'D78':list(range(461,466)), 'F23':list(range(550,558)),
        'F20_coordinate_calibration':[533,534,535,536,537,538,539],
        'F22_coordinate_calibration':[544,545,546,547,548,549,550],
        'current_scope_overviews':[85,86,87,298,299,300,476,477,478],
        'bibliography_sample':[558,562,565,567]
    },
    'historical_overflow_widths_pt':qa['historical_overflow_widths_pt'],
    'historical_passages_reviewed':{
        'first-page notation table':[1], 'B17 inline list':[29,30],
        'B34 comparison display':[56,57], 'B36 filenames':[59],
        'B37 filenames':[61,62,63,64], 'D37o deck display':[345],
        'C45.4 compatible-group display':[141,142,143],
        'C65.2 finite-word path display':[207,208],
        'D74.1 normalized involution display':[444],
        'F19.9 fiber-product alignment':[529],
        'C77.4 former invalid alignment repair':[249],
        'F21 exponent-pair list':[541]
    },
    'current_build_repairs':[
        {'source':'work/part_b/c88.tex','repair':'Replaced split by aligned for two alignment column pairs; mathematics unchanged.',
         'record':'work/root/c88_typesetting_repair.json','reviewed_pages':[287]},
        {'source':'work/root/assemble.py','repair':'Remove an existing terminal provenance period before the macro appends its period.',
         'record':'work/root/passage_punctuation_repair_258.json','reviewed_pages':root_fresh+prep['peer_fresh_pages']}
    ],
    'log_review':{
        'stages_passed':4,'overfull_boxes':0,'overfull_greater_than_2pt':0,
        'missing_glyphs':0,'undefined_references_or_citations':0,'fatal_errors':0,
        'final_lualatex_log_read':True,'bibtex_log_read':True,
        'full_log_reader':'part_c_review525; root independently read all final diagnostic lines and both changed log lines.',
        'full_log_review_record':'work/part_c/render_review_567.json',
        'final_log_sha256':sha(OUT/'LM4_FINITE_GROUP_ACTIONS_paper.log'),
        'final_bibtex_log_sha256':sha(OUT/'LM4_FINITE_GROUP_ACTIONS_paper.blg'),
        'bibtex_warnings':["there's a number but no volume in C_Tukia1972"],
        'nonfatal_build_observations':['luaotfload fallback to OT1; final T1 Latin Modern fonts rendered successfully','one underfull first-page notation-table cell'],
        'bibliographic_warning_scope':'The source is Series A I, number504; no fictitious volume supplied.'
    },
    'visual_observations':('All selected text, equations, tables, diagrams, page edges and tags are legible. '
                           'The corrected provenance notes have one terminal period. The C88 inverse map, '
                           'D78 finite-invariant maps, F23 source-sign diagram, exact coordinate comparisons '
                           'and finite-image table all fit. No clipped text, overlaps or missing glyphs observed.'),
    'issues':[], 'rendered_images':prep['images']
}
for p in [ROOT/'work/root/render_review_567.json', OUT/'render_review.json']:
    p.write_text(json.dumps(review,indent=2)+'\n')
extra_path=ROOT/'work/root/checkpoint_258_extra_paths.json'
extra=json.loads(extra_path.read_text())
extra += ['work/root/seal_render_review_567.py','work/root/render_review_567.json',
          'work/root/render_preparation_567_final.json','work/part_c/render_review_567.json',
          'work/part_c/final_567_sealed_build.log','work/part_c/final_567_sealed_build.blg']
extra += [str(Path(im['path']).relative_to(ROOT)) for im in prep['images']]
extra_path.write_text(json.dumps(list(dict.fromkeys(extra)),indent=2)+'\n')
print(json.dumps({'pdf_sha256':pdf_hash,'reviewed_pages':len(pages),'root_fresh':len(root_fresh),
                  'peer_fresh':len(prep['peer_fresh_pages']),'exact_image_reuse':len(prep['byte_identical_initial_review_pages']),
                  'review_sha256':sha(OUT/'render_review.json'),'extra_paths':len(set(extra))},indent=2))
