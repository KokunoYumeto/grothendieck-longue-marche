#!/usr/bin/env python3
"""Render the final 264-claim PDF selection; record, without certifying, views."""
from pathlib import Path
import fitz, hashlib, json

ROOT = Path(__file__).resolve().parents[2]
PDF = ROOT/'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.pdf'
EXPECTED = '3dbd3037a1cb9199a564ac7ce6d1bf2fcc584297d0821d284b434834b600fcf9'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(PDF) == EXPECTED
doc = fitz.open(PDF)
assert len(doc) == 587
root_pages = [1,10,29,30,56,57,59,61,62,63,64,85,86,87,88,120,
              142,143,144,160,200,208,209,240,250,280,294,295,
              296,297,298,299,300,320,355]
peer_pages = [360,400,440,454,471,480,486,487,488,489,520,539,
              550,551,552,560,567,571,573,574,575,576,577,578,
              580,584,587]
assert not set(root_pages) & set(peer_pages)
dest = ROOT/'work/root/rendered/review_587_final'
dest.mkdir(parents=True, exist_ok=True)
prior_dir = ROOT/'work/root/rendered/review_578_final'
rows = []
for p in sorted(root_pages+peer_pages):
    target = dest/f'page{p:03d}.png'
    doc[p-1].get_pixmap(matrix=fitz.Matrix(1.4,1.4),alpha=False).save(target)
    prior = prior_dir/f'page{p:03d}.png'
    identical = prior.is_file() and prior.read_bytes() == target.read_bytes()
    rows.append({'page':p,'reviewer':'root' if p in root_pages else 'peer',
                 'path':str(target.relative_to(ROOT)),'sha256':sha(target),
                 'bytes':target.stat().st_size,
                 'byte_identical_to_prior_578_image':identical,
                 'prior_image':str(prior.relative_to(ROOT)) if identical else None,
                 'prior_review':'work/root/render_review_578.json' if identical else None})
record={'pdf':str(PDF.relative_to(ROOT)),'sha256':EXPECTED,'pages':587,
        'root_pages':root_pages,'peer_pages':peer_pages,'images':rows,
        'render_only_does_not_certify_visual_review':True,
        'historical_passages':{'notation_table':[1],'B17':[29,30],
            'B34':[56,57],'B36':[59],'B37':[61,62,63,64],
            'C45.4':[142,143,144],'C65.2':[208,209],
            'D37o':[355],'D74.1':[454],'F19.9':[539],
            'F21_exponent_pairs':[551]},
        'new_proof_pages':{'C91':[296,297,298,299,300],
                           'F26':[573,574,575,576,577]},
        'scope_overview_pages':{'C12':[85,86,87,88],'F7':[486,487,488,489]}}
(ROOT/'work/root/render_preparation_587_final.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'pdf_sha256':EXPECTED,'images':len(rows),
    'root_fresh':[r['page'] for r in rows if r['reviewer']=='root' and not r['byte_identical_to_prior_578_image']],
    'root_identical':[r['page'] for r in rows if r['reviewer']=='root' and r['byte_identical_to_prior_578_image']],
    'peer_pages':peer_pages},indent=2))
