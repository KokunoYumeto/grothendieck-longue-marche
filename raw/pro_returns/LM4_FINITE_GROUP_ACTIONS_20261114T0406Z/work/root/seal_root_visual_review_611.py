#!/usr/bin/env python3
"""Seal root's actual four-page view and exact whole-image carry to final611."""
from pathlib import Path
import datetime
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
prep_path = ROOT/'work/root/render_preparation_611_final.json'
prior_path = ROOT/'work/root/render_review_608.json'
prep = json.loads(prep_path.read_text())
prior = json.loads(prior_path.read_text())
expected = '6eb08722ef726aaa8894facf55915238861d7981c9d86d63cdc62e6e7dc47a97'
assert sha(ROOT/'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.pdf') == expected == prep['sha256']
assert sha(prior_path) == 'aff852bc32f486a5799ede8ebb6878d413dc98c9081aa8dfc27e32e5149af599'
# Both calls actually displayed these exact final images to root.
view_calls = [[598,599],[600,601]]
fresh = [page for group in view_calls for page in group]
assert len(fresh) == len(set(fresh)) == 4 and all(len(group)<=2 for group in view_calls)
prior_images = {x['page']:x for x in prior['rendered_images']}
rows = []
carry = []
for item in prep['images']:
    if item['reviewer'] != 'root':
        continue
    path = ROOT/item['path']
    assert sha(path) == item['sha256'] and path.stat().st_size == item['bytes']
    if item['byte_identical_to_prior_608_image']:
        old = prior_images[item['page']]
        old_path = Path(old['path'])
        old_path = old_path if old_path.is_absolute() else ROOT/old_path
        assert item['page'] in prior['actually_viewed_pages']
        assert old['sha256'] == item['sha256'] and old['bytes'] == item['bytes']
        assert old_path.read_bytes() == path.read_bytes()
        carry.append(item['page'])
    else:
        assert item['page'] in fresh
    rows.append(dict(item, actual_viewed=True,
        fresh_view_for_this_final_pdf=item['page'] in fresh,
        review_basis='fresh actual image view' if item['page'] in fresh else
        'exact entire-PNG identity with a previously viewed bound image'))
assert sorted(fresh+carry) == prep['root_pages'] and len(carry) == 79
record = {
    'status':'PASS', 'sha256':expected, 'pdf_pages':611,
    'reviewed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'actually_viewed_pages':prep['root_pages'],
    'images_opened_this_final_review':fresh, 'actual_view_calls':view_calls,
    'byte_identical_prior_review_pages':carry,
    'prior_review':'work/root/render_review_608.json', 'prior_review_sha256':sha(prior_path),
    'prior_pdf':'work/root/prior_268_snapshot/paper.pdf',
    'prior_pdf_sha256':sha(ROOT/'work/root/prior_268_snapshot/paper.pdf'),
    'render_preparation_sha256':sha(prep_path), 'images':rows,
    'observations':[
        'Page598 clearly shows the complete F29 conclusion and the F30 statement, original locus, rank, manuscript metadata and proof opening.',
        'Page599 retains the original scalar fields, coefficient map, principal quotient, boundary covector, inclusion, section and inverse basis with legible tags and no clipping.',
        'Page600 displays the original principal correction, three-source action table, Frobenius maps and all three type comparisons clearly.',
        'Page601 retains the summed restriction and explicit intertwiners, principal kernel and trace formulas, evidence scope and both-sign transport; all tags and text fit.',
        'All79 other root-assigned final PNGs are byte-identical as whole files to the sealed608 images. Each prior view membership, complete size and digest was checked, including every historical overflow passage and the F29.25 repair.'
    ], 'issues':[],
    'scope':'Root83 selected pages:4 newly opened and79 exact previously viewed images. Peer5 fresh pages and full final logs are sealed separately.'
}
out = ROOT/'work/root/root_visual_review_611.json'
out.write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps({'status':'PASS', 'root_pages':83, 'fresh_actual_views':4,
                  'whole_png_carry':79, 'sha256':sha(out)}, indent=2))
