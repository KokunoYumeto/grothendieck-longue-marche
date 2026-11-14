#!/usr/bin/env python3
"""Bind the root's actual views and exact whole-PNG carry to final619."""
from pathlib import Path
from hashlib import sha256
import datetime
import json

ROOT=Path(__file__).resolve().parents[2]
sha=lambda p:sha256(p.read_bytes()).hexdigest()
prep_path=ROOT/'work/root/render_preparation_619_final.json'
prior_path=ROOT/'work/root/render_review_611.json'
prep=json.loads(prep_path.read_text())
prior=json.loads(prior_path.read_text())
expected='4546799ef3198a11c19a7b7a81e3d9a20aca2016c9f97633826fd971ffc02175'
assert sha(ROOT/'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.pdf')==expected==prep['sha256']
assert sha(prior_path)=='a6025bedd581aee6e46b67d367707d7cf7808faef06f7f4b002d47cfb94647cf'
view_calls=[[602,603],[604,605]]
fresh=[page for group in view_calls for page in group]
assert len(fresh)==len(set(fresh))==4 and all(len(group)<=2 for group in view_calls)
prior_images={x['page']:x for x in prior['rendered_images']}
rows=[];carry=[]
for item in prep['images']:
    if item['reviewer']!='root':
        continue
    path=ROOT/item['path']
    assert sha(path)==item['sha256'] and path.stat().st_size==item['bytes']
    if item['byte_identical_to_prior_611_image']:
        old=prior_images[item['page']]
        old_path=Path(old['path'])
        old_path=old_path if old_path.is_absolute() else ROOT/old_path
        assert item['page'] in prior['actually_viewed_pages']
        assert old['sha256']==item['sha256'] and old['bytes']==item['bytes']
        assert old_path.read_bytes()==path.read_bytes()
        carry.append(item['page'])
    else:
        assert item['page'] in fresh
    rows.append(dict(item,actual_viewed=True,
        fresh_view_for_this_final_pdf=item['page'] in fresh,
        review_basis='fresh actual image view' if item['page'] in fresh else
        'exact entire-PNG identity with a previously viewed bound image'))
assert sorted(fresh+carry)==prep['root_pages'] and len(carry)==82
record={
    'status':'PASS','sha256':expected,'pdf_pages':619,
    'reviewed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'actually_viewed_pages':prep['root_pages'],
    'images_opened_this_final_review':fresh,'actual_view_calls':view_calls,
    'byte_identical_prior_review_pages':carry,
    'prior_review':'work/root/render_review_611.json','prior_review_sha256':sha(prior_path),
    'prior_pdf':'work/root/prior_269_snapshot/paper.pdf',
    'prior_pdf_sha256':sha(ROOT/'work/root/prior_269_snapshot/paper.pdf'),
    'render_preparation_sha256':sha(prep_path),'images':rows,
    'observations':[
        'Page602 clearly displays the complete F31 statement, all original field/scalar hypotheses, exact image/rank conclusions, manuscript metadata, scalar cases and coefficient homomorphism.',
        'Page603 shows the repaired negative-crossing tuple with its permitted break at the exact separator; all tuple entries and decoration order remain legible. The principal quotient, kernel, both basis inverses and all displayed tags fit.',
        'Page604 clearly displays the complete moving-root table, all eight explicit eigenrows and four determinant identities. Dense matrix entries, subscripts, powers and tags fit within the text block.',
        'Page605 retains the complete fixed-field proof, every nonzero-factor argument and all three generic minimal-type comparisons with clear text and equations.',
        'All82 other root-assigned PNGs are byte-identical as whole files to previously viewed sealed611 images. Complete bytes, size, digest and prior-view membership were verified, including every inherited overflow passage and F29.25.'
    ],'issues':[],
    'scope':'Root86 selected pages:4 freshly viewed and82 exact previously viewed images. Peer10 fresh pages and full final logs are separately sealed.'}
out=ROOT/'work/root/root_visual_review_619.json'
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':'PASS','root_pages':86,'fresh_actual_views':4,
                  'whole_png_carry':82,'sha256':sha(out)},indent=2))
