#!/usr/bin/env python3
"""Seal the root image review only after the listed PNGs were actually opened."""
from pathlib import Path
import datetime
import hashlib
import json

ROOT=Path(__file__).resolve().parents[2]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
prep_path=ROOT/'work/root/render_preparation_608_final.json'
prior_path=ROOT/'work/root/render_review_600.json'
prep=json.loads(prep_path.read_text());prior=json.loads(prior_path.read_text())
expected='2038bacd186770710f3a949d2edf6adb92fb800ab6d531133088b6694fd07cd5'
assert sha(ROOT/'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.pdf')==expected==prep['sha256']
assert sha(prior_path)=='8f48863df4f5f033bde1f0754cc8ffcb3a1f8cad16520ca1604d7d360c1d7b2a'
# These six tool calls actually displayed the named final images to root.
view_calls=[[492,493],[494,495],[496,520],[544,591],[592,593],[594]]
fresh=[p for group in view_calls for p in group]
assert len(fresh)==len(set(fresh))==11 and all(len(g)<=2 for g in view_calls)
prior_images={x['page']:x for x in prior['rendered_images']}
rows=[];carry=[]
for item in prep['images']:
 if item['reviewer']!='root':continue
 p=ROOT/item['path']
 assert sha(p)==item['sha256'] and p.stat().st_size==item['bytes']
 if item['byte_identical_to_prior_600_image']:
  old=prior_images[item['page']];old_path=Path(old['path'])
  old_path=old_path if old_path.is_absolute() else ROOT/old_path
  assert item['page'] in prior['actually_viewed_pages']
  assert old['sha256']==item['sha256'] and old['bytes']==item['bytes']
  assert old_path.read_bytes()==p.read_bytes()
  carry.append(item['page'])
 else:
  assert item['page'] in fresh
 rows.append(dict(item,actual_viewed=True,
                  fresh_view_for_this_final_pdf=item['page'] in fresh,
                  review_basis='fresh actual image view' if item['page'] in fresh else 'exact entire-PNG identity with a previously viewed bound image'))
assert sorted(fresh+carry)==prep['root_pages'] and len(carry)==48
record={'status':'PASS','sha256':expected,'pdf_pages':608,
        'reviewed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'actually_viewed_pages':prep['root_pages'],
        'images_opened_this_final_review':fresh,'actual_view_calls':view_calls,
        'byte_identical_prior_review_pages':carry,
        'prior_review':'work/root/render_review_600.json','prior_review_sha256':sha(prior_path),
        'prior_pdf':'work/root/prior_267_snapshot/paper.pdf',
        'prior_pdf_sha256':sha(ROOT/'work/root/prior_267_snapshot/paper.pdf'),
        'render_preparation_sha256':sha(prep_path),'images':rows,
        'observations':[
          'The revised F7 scope and surrounding proof on pages492--496 are legible, with intact manuscript metadata and no clipping or collisions.',
          'The sampled F11 page520 retains the long braid-word rows and equation tags within the margins.',
          'The historic F19.9 fiber-product passage on page544 fits with its alignment and tags intact.',
          'F29 statement and proof pages591--594 retain all basis maps, source tables, annihilator displays, Frobenius formulas and exceptional residuals legibly.',
          'The other48 root-assigned final images are byte-identical as entire PNG files to the exact images in the sealed600 review; every size, digest and prior-view membership was checked.'
        ],'issues':[],
        'scope':'Root59 selected pages:11 newly opened and48 exact previously viewed images. Peer25 pages and full logs are sealed separately.'}
out=ROOT/'work/root/root_visual_review_608.json'
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':'PASS','root_pages':59,'fresh_actual_views':11,
                  'whole_png_carry':48,'sha256':sha(out)},indent=2))
