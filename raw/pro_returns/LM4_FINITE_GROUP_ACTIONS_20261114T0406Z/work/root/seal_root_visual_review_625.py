#!/usr/bin/env python3
"""Bind actual root views and exact whole-PNG carry to the final625 PDF."""
from pathlib import Path
from hashlib import sha256
import datetime
import json

ROOT = Path(__file__).resolve().parents[2]
sha = lambda p: sha256(p.read_bytes()).hexdigest()
prep_path = ROOT / 'work/root/render_preparation_625_final.json'
prior_path = ROOT / 'work/root/render_review_619.json'
prep = json.loads(prep_path.read_text())
prior = json.loads(prior_path.read_text())
expected = '9d80a79e439f1928b2b7096cf9a6d5ec5ac1e01638b119c4872bf394ef635364'
assert sha(ROOT / 'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.pdf') == expected == prep['sha256']
assert sha(prior_path) == '798efaa2f4066f49f18437bed1e3efb015945b6920562f635c0acb2f0cfc2235'
view_calls = [[611, 612], [613, 614]]
fresh = [page for group in view_calls for page in group]
assert len(fresh) == len(set(fresh)) == 4
assert all(len(group) <= 2 for group in view_calls)
prior_images = {x['page']: x for x in prior['rendered_images']}
rows, carry = [], []
for item in prep['images']:
    if item['reviewer'] != 'root':
        continue
    path = ROOT / item['path']
    assert sha(path) == item['sha256'] and path.stat().st_size == item['bytes']
    if item['byte_identical_to_prior_619_image']:
        old = prior_images[item['page']]
        old_path = Path(old['path'])
        old_path = old_path if old_path.is_absolute() else ROOT / old_path
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
assert sorted(fresh + carry) == prep['root_pages'] and len(carry) == 90
record = {
    'status': 'PASS', 'sha256': expected, 'pdf_pages': 625,
    'reviewed_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'actually_viewed_pages': prep['root_pages'],
    'images_opened_this_final_review': fresh, 'actual_view_calls': view_calls,
    'byte_identical_prior_review_pages': carry,
    'prior_review': 'work/root/render_review_619.json',
    'prior_review_sha256': sha(prior_path),
    'prior_pdf': 'work/root/prior_270_snapshot/paper.pdf',
    'prior_pdf_sha256': sha(ROOT / 'work/root/prior_270_snapshot/paper.pdf'),
    'render_preparation_sha256': sha(prep_path), 'images': rows,
    'observations': [
        'Page611 visibly contains the original-word row D, the complete principal-quotient inverse maps, the seven/six-coordinate identities, all source decoration scalars and the five-dimensional kernel basis with its displayed inverse; formulas and tags are clear.',
        'Page612 visibly contains the invariant block and quotient characters, all eight base/moving-root rows, the integral eigenrow identities, the first four explicit covectors and the complete P4/P6 polynomials; entries, subscripts and tags fit.',
        'Page613 visibly contains the other four complete covectors, including P4/P6, the four determinant formulas and the start of the fixed-field comparison; the wide matrix entries remain within the text block and are readable.',
        'Page614 visibly contains the full moving-root separation and determinant-cover argument, the three simple-subspace comparisons, the summed restriction and the explicit inverse intertwiners; all text, equations and tags are clear.',
        'All90 other root-assigned PNGs are byte-identical as whole files to previously viewed sealed619 images. Complete bytes, size, digest and prior-view membership were verified, including the first-page notation table, every inherited overflow passage, F29.25 and the F31 negative-crossing repair.'
    ],
    'issues': [],
    'scope': 'Root94 selected pages:4 freshly viewed and90 exact previously viewed images. Peer8 fresh pages and the complete final logs are separately sealed.'
}
out = ROOT / 'work/root/root_visual_review_625.json'
assert not out.exists()
out.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'root_pages': 94, 'fresh_actual_views': 4,
                  'whole_png_carry': 90, 'sha256': sha(out)}, indent=2))
