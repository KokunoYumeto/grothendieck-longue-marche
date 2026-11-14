#!/usr/bin/env python3
"""Render the exact 267-claim PDF selection without certifying unseen images."""
from pathlib import Path
import fitz,hashlib,json
ROOT=Path(__file__).resolve().parents[2]
PDF=ROOT/'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.pdf'
EXPECTED='42ef0d3fff1be048a0c3d09f065c19114341f15174930173ce847bbcd0b0ae8f'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(PDF)==EXPECTED
doc=fitz.open(PDF);assert len(doc)==600
root_pages=[1,10,29,30,56,57,59,61,62,63,64,85,86,87,88,89,120,
 142,143,144,160,200,208,209,240,250,280,294,295,296,297,298,299,
 300,301,302,303,304,305,320,361]
peer_pages=[360,400,440,459,475,480,491,492,493,494,495,520,544,
 555,556,557,565,575,578,580,581,582,583,584,585,586,587,588,589,
 590,591,596,600]
assert not set(root_pages)&set(peer_pages)
dest=ROOT/'work/root/rendered/review_600_final';dest.mkdir(parents=True,exist_ok=True)
prior_path=ROOT/'work/root/render_review_587.json'
assert sha(prior_path)=='e7331c5a04e448a65143f976e9f416f71ed1d7b517714d7d916c1f5c8fde6b9e'
prior=json.loads(prior_path.read_text())
old_images={x['page']:x for x in prior['rendered_images']}
rows=[]
for p in sorted(root_pages+peer_pages):
 target=dest/f'page{p:03d}.png'
 doc[p-1].get_pixmap(matrix=fitz.Matrix(1.4,1.4),alpha=False).save(target)
 old=old_images.get(p);identical=False
 if old:
  old_path=Path(old['path']);old_path=old_path if old_path.is_absolute() else ROOT/old_path
  assert sha(old_path)==old['sha256'] and old_path.stat().st_size==old['bytes']
  assert p in prior['actually_viewed_pages']
  identical=old_path.read_bytes()==target.read_bytes()
 rows.append({'page':p,'reviewer':'root' if p in root_pages else 'peer',
  'path':str(target.relative_to(ROOT)),'sha256':sha(target),'bytes':target.stat().st_size,
  'byte_identical_to_prior_587_image':identical,
  'prior_image':str(old_path.relative_to(ROOT)) if identical else None,
  'prior_review':'work/root/render_review_587.json' if identical else None})
record={'pdf':str(PDF.relative_to(ROOT)),'sha256':EXPECTED,'pages':600,
 'root_pages':root_pages,'peer_pages':peer_pages,'images':rows,
 'render_only_does_not_certify_visual_review':True,
 'prior_review_sha256':sha(prior_path),
 'historical_passages':{'notation_table':[1],'B17':[29,30],'B34':[56,57],
  'B36':[59],'B37':[61,62,63,64],'C45.4':[142,143,144],
  'C65.2':[208,209],'C77.4':[250],'D37o':[361],'D74.1':[459],
  'F19.9':[544],'F21_exponent_pairs':[556]},
 'new_proof_pages':{'C92':[300,301,302,303,304,305],
  'F27':[582,583,584,585,586],'F28':[586,587,588,589,590]},
 'scope_overview_pages':{'C12':[85,86,87,88,89],'F7':[491,492,493,494,495]}}
(ROOT/'work/root/render_preparation_600_final.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'pdf_sha256':EXPECTED,'images':len(rows),
 'root_fresh':[x['page'] for x in rows if x['reviewer']=='root' and not x['byte_identical_to_prior_587_image']],
 'root_identical':[x['page'] for x in rows if x['reviewer']=='root' and x['byte_identical_to_prior_587_image']],
 'peer_pages':peer_pages},indent=2))
