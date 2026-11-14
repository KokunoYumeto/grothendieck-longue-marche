#!/usr/bin/env python3
"""Render final629 selections and compare complete PNG bytes with sealed625."""
from pathlib import Path
from hashlib import sha256
import json
import fitz

ROOT=Path(__file__).resolve().parents[2]
PDF=ROOT/'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.pdf'
EXPECTED='693902ed60a12a9ef5d26160d56cac7b96b9ff9cde034b4f02f9b41231b2871d'
sha=lambda p:sha256(p.read_bytes()).hexdigest()
assert sha(PDF)==EXPECTED
doc=fitz.open(PDF);assert len(doc)==629
prior_path=ROOT/'work/root/render_review_625.json'
assert sha(prior_path)=='a5f7b890a3a04d2993d555293325bd32be6ad3a019e6f3e52927059212f90bb5'
prior=json.loads(prior_path.read_text());old={x['page']:x for x in prior['rendered_images']}
selected={p for p in old if p<=615}|set(range(616,620))|{620,621,625,626,629}
root_fresh={617,618}
dest=ROOT/'work/root/rendered/review_629_final';dest.mkdir(parents=True,exist_ok=True)
rows=[]
for page in sorted(selected):
    target=dest/f'page{page:03d}.png'
    doc[page-1].get_pixmap(matrix=fitz.Matrix(1.4,1.4),alpha=False).save(target)
    previous=old.get(page);identical=False;old_path=None
    if previous:
        old_path=Path(previous['path']);old_path=old_path if old_path.is_absolute() else ROOT/old_path
        assert sha(old_path)==previous['sha256'] and old_path.stat().st_size==previous['bytes']
        assert page in prior['actually_viewed_pages']
        identical=old_path.read_bytes()==target.read_bytes()
    reviewer='root' if identical or page in root_fresh else 'peer'
    rows.append({'page':page,'reviewer':reviewer,'path':str(target.relative_to(ROOT)),
                 'sha256':sha(target),'bytes':target.stat().st_size,
                 'byte_identical_to_prior_625_image':identical,
                 'prior_image':str(old_path.relative_to(ROOT)) if identical else None,
                 'prior_review':'work/root/render_review_625.json' if identical else None})
record={
 'pdf':str(PDF.relative_to(ROOT)),'sha256':EXPECTED,'pages':629,
 'root_pages':[x['page'] for x in rows if x['reviewer']=='root'],
 'peer_pages':[x['page'] for x in rows if x['reviewer']=='peer'],
 'images':rows,'render_only_does_not_certify_visual_review':True,
 'prior_review_sha256':sha(prior_path),'prior_pdf':'work/root/prior_271_snapshot/paper.pdf',
 'prior_pdf_sha256':'9d80a79e439f1928b2b7096cf9a6d5ec5ac1e01638b119c4872bf394ef635364',
 'historical_passages':prior['historical_passages_reviewed'],
 'new_proof_pages':{'F29':list(range(591,599)),'F30':list(range(598,602)),
                    'F31':list(range(602,610)),'F32':list(range(609,616)),
                    'F33':list(range(616,620))},
 'scope_overview_pages':{'F7':list(range(491,497))},
 'reference_samples':[620,621,625,626,629],'no_typesetting_edit_required_for_F33':True}
out=ROOT/'work/root/render_preparation_629_final.json'
assert not out.exists();out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'pdf_sha256':EXPECTED,'images':len(rows),
 'root_fresh':[x['page'] for x in rows if x['reviewer']=='root' and not x['byte_identical_to_prior_625_image']],
 'root_identical_count':sum(x['byte_identical_to_prior_625_image'] for x in rows),
 'peer_pages':record['peer_pages'],'preparation_sha256':sha(out)},indent=2))
