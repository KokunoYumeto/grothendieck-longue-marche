#!/usr/bin/env python3
"""Bind the actual root views and whole-PNG carries to the final629 PDF."""
from pathlib import Path
from hashlib import sha256
import datetime,json

ROOT=Path(__file__).resolve().parents[2]
sha=lambda p:sha256(p.read_bytes()).hexdigest()
prep_path=ROOT/'work/root/render_preparation_629_final.json'
prior_path=ROOT/'work/root/render_review_625.json'
prep=json.loads(prep_path.read_text());prior=json.loads(prior_path.read_text())
expected='693902ed60a12a9ef5d26160d56cac7b96b9ff9cde034b4f02f9b41231b2871d'
assert sha(ROOT/'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.pdf')==expected==prep['sha256']
assert sha(prior_path)=='a5f7b890a3a04d2993d555293325bd32be6ad3a019e6f3e52927059212f90bb5'
view_calls=[[617,618]]
fresh=[page for group in view_calls for page in group]
assert len(fresh)==len(set(fresh))==2 and all(len(g)<=2 for g in view_calls)
prior_images={x['page']:x for x in prior['rendered_images']}
rows=[];carry=[]
for item in prep['images']:
    if item['reviewer']!='root':continue
    path=ROOT/item['path'];assert sha(path)==item['sha256'] and path.stat().st_size==item['bytes']
    if item['byte_identical_to_prior_625_image']:
        old=prior_images[item['page']];old_path=Path(old['path'])
        old_path=old_path if old_path.is_absolute() else ROOT/old_path
        assert item['page'] in prior['actually_viewed_pages']
        assert old['sha256']==item['sha256'] and old['bytes']==item['bytes']
        assert old_path.read_bytes()==path.read_bytes();carry.append(item['page'])
    else:assert item['page'] in fresh
    rows.append(dict(item,actual_viewed=True,fresh_view_for_this_final_pdf=item['page'] in fresh,
                     review_basis='fresh actual image view' if item['page'] in fresh else
                     'exact entire-PNG identity with a previously viewed bound image'))
assert sorted(fresh+carry)==prep['root_pages'] and len(carry)==96
record={
 'status':'PASS','sha256':expected,'pdf_pages':629,
 'reviewed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'actually_viewed_pages':prep['root_pages'],'images_opened_this_final_review':fresh,
 'actual_view_calls':view_calls,'byte_identical_prior_review_pages':carry,
 'prior_review':'work/root/render_review_625.json','prior_review_sha256':sha(prior_path),
 'prior_pdf':'work/root/prior_271_snapshot/paper.pdf',
 'prior_pdf_sha256':sha(ROOT/'work/root/prior_271_snapshot/paper.pdf'),
 'render_preparation_sha256':sha(prep_path),'images':rows,
 'observations':[
 'Page617 visibly contains the full integer parity formula, exact Fox identity, fourteen-entry principal vector, gauge and inverse, thirteen-column order, exhaustive four-chart table and complete divisor explanation. All entries, fractions, exponents and tags fit clearly.',
 'Page618 visibly contains every one of the50 printed pivots in the complete four-column table, the ordered terminal block and determinant, its adjugate and row-swap comparison, the full paired map and inverse, and the paired principal line. All table rows and every displayed tag remain inside the text block and are readable.',
 'All96 other root-assigned PNGs equal previously viewed sealed625 images as entire byte strings. Complete bytes, size, digest and prior-view membership were checked, including the first-page notation concordance and every historical overflow passage.'],
 'issues':[],
 'scope':'Root98 selected pages:2 freshly viewed and96 exact previously viewed images. Peer8 fresh pages and the complete final logs are separately reviewed.'}
out=ROOT/'work/root/root_visual_review_629.json';assert not out.exists()
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':'PASS','root_pages':98,'fresh_actual_views':2,
 'whole_png_carry':96,'sha256':sha(out)},indent=2))
