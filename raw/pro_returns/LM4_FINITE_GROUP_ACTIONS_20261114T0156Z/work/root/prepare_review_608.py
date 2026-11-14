#!/usr/bin/env python3
"""Render the selected final268 pages; keep rendering separate from viewing."""
from pathlib import Path
import hashlib
import json
import fitz

ROOT=Path(__file__).resolve().parents[2]
PDF=ROOT/'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.pdf'
EXPECTED='2038bacd186770710f3a949d2edf6adb92fb800ab6d531133088b6694fd07cd5'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(PDF)==EXPECTED
doc=fitz.open(PDF);assert len(doc)==608
prior_path=ROOT/'work/root/render_review_600.json'
assert sha(prior_path)=='8f48863df4f5f033bde1f0754cc8ffcb3a1f8cad16520ca1604d7d360c1d7b2a'
prior=json.loads(prior_path.read_text())
old={x['page']:x for x in prior['rendered_images']}
selected=set(old)|set(range(491,497))|set(range(591,599))|{599,603,608}
root_fresh_assignment=set(range(491,497))|{520,544,591,592,593,594}
dest=ROOT/'work/root/rendered/review_608_final'
dest.mkdir(parents=True,exist_ok=True)
rows=[]
for p in sorted(selected):
 target=dest/f'page{p:03d}.png'
 doc[p-1].get_pixmap(matrix=fitz.Matrix(1.4,1.4),alpha=False).save(target)
 previous=old.get(p);identical=False;old_path=None
 if previous:
  old_path=Path(previous['path']);old_path=old_path if old_path.is_absolute() else ROOT/old_path
  assert sha(old_path)==previous['sha256'] and old_path.stat().st_size==previous['bytes']
  assert p in prior['actually_viewed_pages']
  identical=old_path.read_bytes()==target.read_bytes()
 reviewer='root' if identical or p in root_fresh_assignment else 'peer'
 rows.append({'page':p,'reviewer':reviewer,'path':str(target.relative_to(ROOT)),
              'sha256':sha(target),'bytes':target.stat().st_size,
              'byte_identical_to_prior_600_image':identical,
              'prior_image':str(old_path.relative_to(ROOT)) if identical else None,
              'prior_review':'work/root/render_review_600.json' if identical else None})
record={'pdf':str(PDF.relative_to(ROOT)),'sha256':EXPECTED,'pages':608,
        'root_pages':[x['page'] for x in rows if x['reviewer']=='root'],
        'peer_pages':[x['page'] for x in rows if x['reviewer']=='peer'],
        'images':rows,'render_only_does_not_certify_visual_review':True,
        'prior_review_sha256':sha(prior_path),
        'prior_pdf':'work/root/prior_267_snapshot/paper.pdf',
        'prior_pdf_sha256':'42ef0d3fff1be048a0c3d09f065c19114341f15174930173ce847bbcd0b0ae8f',
        'historical_passages':{'notation_table':[1],'B17':[29,30],'B34':[56,57],
          'B36':[59],'B37':[61,62,63,64],'C45.4':[142,143,144],
          'C65.2':[208,209],'C77.4':[250],'D37o':[361],'D74.1':[459],
          'F19.9':[544],'F21_exponent_pairs':[555,556,557],'F29.25':[596]},
        'new_proof_pages':{'F29':list(range(591,599))},
        'scope_overview_pages':{'F7':list(range(491,497))},
        'reference_samples':[599,600,603,608]}
(ROOT/'work/root/render_preparation_608_final.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'pdf_sha256':EXPECTED,'images':len(rows),
                  'root_fresh':[x['page'] for x in rows if x['reviewer']=='root' and not x['byte_identical_to_prior_600_image']],
                  'root_identical':[x['page'] for x in rows if x['byte_identical_to_prior_600_image']],
                  'peer_pages':record['peer_pages']},indent=2))
