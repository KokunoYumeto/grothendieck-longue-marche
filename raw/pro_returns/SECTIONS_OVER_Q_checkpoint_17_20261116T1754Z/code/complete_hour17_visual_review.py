#!/usr/bin/env python3
"""Combine actually displayed root/peer images for the same final PDF."""
from pathlib import Path
import datetime
import hashlib
import json

w = Path(__file__).resolve().parents[1]
qa = w/'qa/hour17'
render = json.loads((qa/'render_record.json').read_text())
sha = hashlib.sha256((w/'SECTIONS_OVER_Q_paper.pdf').read_bytes()).hexdigest()
assert render['pdf_sha256']==sha
paths = ['root_visual_review.json','birational_visual_review.json','local_preprint_visual_review.json']
records=[]
full=set()
for name in paths:
    r=json.loads((qa/name).read_text())
    assert r['pdf_sha256']==sha, name
    assert r['status'].startswith('PASS'), name
    pages=r.get('reviewed_pages',r.get('pages'))
    assert pages and isinstance(pages,list),name
    assert set(pages)<=set(render['required_full_resolution_pages'])
    full.update(pages)
    records.append(r)
root=records[0]
assert set(root['contact_parts_reviewed'])==set(render['contact_parts'])
assert set(render['required_full_resolution_pages'])<=full
assert set(render['new_result_pages'])<=set(root['reviewed_pages'])
review={
    'status':'Visually inspected every final-build contact sheet and every required full-resolution page; no clipping, overlap or margin overflow observed.',
    'reviewed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'reviewed_build_pages':render['pdf_pages'],
    'pdf_sha256':sha,
    'contact_parts_reviewed':render['contact_parts'],
    'rendered_pages':render['rendered_pages'],
    'full_resolution_pages_reviewed':sorted(full),
    'required_full_resolution_pages':render['required_full_resolution_pages'],
    'contact_sha256':{p:hashlib.sha256((w/p).read_bytes()).hexdigest() for p in render['contact_parts']},
    'full_resolution_sha256':{str(p):hashlib.sha256((qa/f'full/page_{p:03d}.png').read_bytes()).hexdigest() for p in sorted(full)},
    'root_review':'qa/hour17/root_visual_review.json',
    'peer_reviews':['qa/hour17/'+name for name in paths[1:]],
    'observations':[{'reviewer':r['reviewer'],'observations':r['observations']} for r in records],
    'review_method':'Actual tool-displayed images. Root opened every contact sheet and every new proof page individually. Peers opened the complete front matter and every historical repaired page individually. Every record is bound to the same final PDF hash.'
}
out=json.dumps(review,indent=2)+'\n'
for p in [qa/'visual_review.json',w/'qa/visual_review.json']:
    p.write_text(out)
summary={'pdf_pages':render['pdf_pages'],'pdf_sha256':sha,
         'rendered_pages':len(render['rendered_pages']),
         'contact_sheets':len(render['contact_parts']),
         'full_resolution_pages':len(full),'status':review['status']}
result=json.dumps(summary,indent=2)+'\n'
(w/'code/complete_hour17_visual_review_output.txt').write_text(result)
print(result,end='')
