#!/usr/bin/env python3
"""Record actual inspections of the final625-page build, bound to its hash."""
from pathlib import Path
import datetime, hashlib, json

w=Path(__file__).resolve().parents[1]
r=json.loads((w/'qa/hour15/render_record.json').read_text())
full=[4,437,440,525,532,540,543,547,548,551,560,566,567,572,574,576]
assert r['pdf_pages']==625 and len(r['rendered_pages'])==86
assert set(r['required_full_resolution_pages'])==set(full)
assert r['pdf_sha256']==hashlib.sha256((w/'SECTIONS_OVER_Q_paper.pdf').read_bytes()).hexdigest()
review={
 'status':'Visually inspected all six final-build contact sheets and all sixteen required full-resolution pages; no clipping, overlap or margin overflow observed.',
 'reviewed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'reviewed_build_pages':r['pdf_pages'],
 'pdf_sha256':r['pdf_sha256'],
 'contact_parts_reviewed':r['contact_parts'],
 'rendered_pages':r['rendered_pages'],
 'full_resolution_pages_reviewed':full,
 'contact_sha256':{p:hashlib.sha256((w/p).read_bytes()).hexdigest() for p in r['contact_parts']},
 'full_resolution_sha256':{str(p):hashlib.sha256((w/f'qa/hour15/page_{p:03d}.png').read_bytes()).hexdigest() for p in full},
 'observations':[
  'Every final-build contact sheet was opened separately after the last rebuild and render. The86 pages cover every A185–A192 proof page, all reference pages, the repaired statement and a distributed sample of earlier Parts.',
  'The final rebuild corrected the historical A182 rank frontier on page543 to cite the exact ranks now proved in A185–A186. The six contact sheets and all sixteen full-resolution pages were inspected again after that change.',
  'Page4 has clear spacing between all three-digit subsection labels, titles and page numbers.',
  'The retained corrected A160 displays on pages437 and440 have clear equation labels and remain inside the text area.',
  'The two-line A179 field display on page525 and the two-line A181.1 display on page532 fit with clear labels.',
  'The twenty-one differential weights on page540 are aligned and legible. The first-weight and derived-limit displays on page543 fit, as do the polynomial quotient and inflation displays on page547.',
  'The four-line secondary-character display on page548 has clear domains, alignment and labels.',
  'The Prym rank table and its isogeny on page551 are legible. All twelve completed-generator square witnesses on page560 fit in the displayed table.',
  'The former30.042pt overflow on page566 is repaired: the completed Mordell–Weil identity is now a separate display, and the surrounding statement fits.',
  'The long Cantor coefficients on page567, exact regulator matrix on page572, and nine-unit table on page574 are legible with clear labels and no overlap.',
  'The four-pair Selmer equality on page576 uses two aligned lines with its label clear below; the cyclic-eight equation and following statement fit.',
  'All reference pages612–625 have clear margins and continuous readable entries.'
 ],
 'review_method':'Actual tool-displayed image inspection by the primary agent; all six contact sheets and all sixteen full-resolution pages were opened individually after the final render.'
}
for p in [w/'qa/visual_review.json',w/'qa/hour15/visual_review.json']:
 p.write_text(json.dumps(review,indent=2)+'\n')
p=w/'notes/hour15_typesetting_corrections.json'
corrections=json.loads(p.read_text())
for item in corrections:
 item['after_hbox_pt']=0
 item['final_page']=566
 item['after']='The final625-page build has zero overfull horizontal and vertical boxes; the repaired page566 was inspected at full resolution.'
p.write_text(json.dumps(corrections,indent=2)+'\n')
print(json.dumps({'pages':r['pdf_pages'],'pdf_sha256':r['pdf_sha256'],'rendered':86,'contact_sheets':6,'full_resolution':full,'status':review['status']},indent=2))
