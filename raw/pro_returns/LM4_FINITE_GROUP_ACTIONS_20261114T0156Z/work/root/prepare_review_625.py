#!/usr/bin/env python3
"""Render current selections and compare complete PNGs with sealed619."""
from pathlib import Path
from hashlib import sha256
import json
import fitz

ROOT = Path(__file__).resolve().parents[2]
PDF = ROOT/'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.pdf'
EXPECTED = '9d80a79e439f1928b2b7096cf9a6d5ec5ac1e01638b119c4872bf394ef635364'
sha = lambda p: sha256(p.read_bytes()).hexdigest()
assert sha(PDF) == EXPECTED
doc = fitz.open(PDF)
assert len(doc) == 625
prior_path = ROOT/'work/root/render_review_619.json'
assert sha(prior_path) == '798efaa2f4066f49f18437bed1e3efb015945b6920562f635c0acb2f0cfc2235'
prior = json.loads(prior_path.read_text())
old = {x['page']: x for x in prior['rendered_images']}
selected = {p for p in old if p <= 609} | set(range(609,616)) | {616,617,621,622,625}
root_fresh = {611,612,613,614}
dest = ROOT/'work/root/rendered/review_625_final'
dest.mkdir(parents=True, exist_ok=True)
rows = []
for page in sorted(selected):
    target = dest/f'page{page:03d}.png'
    doc[page-1].get_pixmap(matrix=fitz.Matrix(1.4,1.4), alpha=False).save(target)
    previous = old.get(page)
    identical = False
    old_path = None
    if previous:
        old_path = Path(previous['path'])
        old_path = old_path if old_path.is_absolute() else ROOT/old_path
        assert sha(old_path) == previous['sha256']
        assert old_path.stat().st_size == previous['bytes']
        assert page in prior['actually_viewed_pages']
        identical = old_path.read_bytes() == target.read_bytes()
    reviewer = 'root' if identical or page in root_fresh else 'peer'
    rows.append({'page': page, 'reviewer': reviewer,
                 'path': str(target.relative_to(ROOT)),
                 'sha256': sha(target), 'bytes': target.stat().st_size,
                 'byte_identical_to_prior_619_image': identical,
                 'prior_image': str(old_path.relative_to(ROOT)) if identical else None,
                 'prior_review': 'work/root/render_review_619.json' if identical else None})
record = {
    'pdf': str(PDF.relative_to(ROOT)), 'sha256': EXPECTED, 'pages': 625,
    'root_pages': [x['page'] for x in rows if x['reviewer']=='root'],
    'peer_pages': [x['page'] for x in rows if x['reviewer']=='peer'],
    'images': rows, 'render_only_does_not_certify_visual_review': True,
    'prior_review_sha256': sha(prior_path),
    'prior_pdf': 'work/root/prior_270_snapshot/paper.pdf',
    'prior_pdf_sha256': '4546799ef3198a11c19a7b7a81e3d9a20aca2016c9f97633826fd971ffc02175',
    'historical_passages': {
        'notation_table': [1], 'B17': [29,30], 'B34': [56,57],
        'B36': [59], 'B37': [61,62,63,64], 'C45.4': [142,143,144],
        'C65.2': [208,209], 'C77.4': [250], 'D37o': [361], 'D74.1': [459],
        'F19.9': [544], 'F21_exponent_pairs': [555,556,557],
        'F29.25': [596], 'F31_negative_crossing': [603],
    },
    'new_proof_pages': {'F29': list(range(591,599)), 'F30': list(range(598,602)),
                        'F31': list(range(602,610)), 'F32': list(range(609,616))},
    'shared_previous_and_new_proof_page': [609],
    'scope_overview_pages': {'F7': list(range(491,497))},
    'reference_samples': [616,617,621,622,625],
    'no_typesetting_edit_required_for_F32': True,
}
out = ROOT/'work/root/render_preparation_625_final.json'
out.write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps({'pdf_sha256': EXPECTED, 'images': len(rows),
    'root_fresh': [x['page'] for x in rows if x['reviewer']=='root' and not x['byte_identical_to_prior_619_image']],
    'root_identical_count': sum(x['byte_identical_to_prior_619_image'] for x in rows),
    'peer_pages': record['peer_pages'],
    'preparation_sha256': sha(out)}, indent=2))
