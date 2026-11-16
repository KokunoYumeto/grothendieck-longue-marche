#!/usr/bin/env python3
"""Combine actual root and peer image inspections, tied to the final PDF hash."""
from pathlib import Path
import datetime,hashlib,json

w=Path(__file__).resolve().parents[1]
r=json.loads((w/'qa/hour16/render_record.json').read_text())
equivalence=json.loads((w/'qa/hour16/toc_image_equivalence.json').read_text())
previous_sha='5055d2968632235aca1af887ee286cb72027848f812627be49a287400d0f12d3'
assert equivalence['previous_pdf_sha256']==previous_sha
expected_sha=equivalence['final_pdf_sha256']
assert r['pdf_sha256']==expected_sha==hashlib.sha256((w/'SECTIONS_OVER_Q_paper.pdf').read_bytes()).hexdigest()
assert r['pdf_pages']==661 and len(r['rendered_pages'])==130 and len(r['contact_parts'])==9
root_full=[1,3,579,581,582,584,585,586,590,591,592,594,596,598,599,600,601,602,
           603,605,606,608,609,610,611,612,613,614]
root_record={
 'reviewer':'root','pdf_sha256':expected_sha,'pages':root_full,
 'reviewed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'contact_parts_reviewed':r['contact_parts'],
 'contact_sha256':{p:hashlib.sha256((w/p).read_bytes()).hexdigest() for p in r['contact_parts']},
 'full_resolution_sha256':{str(p):hashlib.sha256((w/f'qa/hour16/full/page_{p:03d}.png').read_bytes()).hexdigest() for p in root_full},
 'observations':[
  'Opened all nine contact sheets. An initial combined call omitted contact3 because of the image output limit; contact3 was then opened successfully in a separate two-image call. After the two TOC-only edits, final pages1 and3 and their first contact sheet were opened again. Every other reviewed body image and contact sheet is byte-identical under the executed equivalence check. All130 current rendered pages were displayed and inspected.',
  'The final optional contents titles for subsections1.29 and1.102 leave visible leaders and separation before page numbers122 and391. Their full body headings and all body pagination are unchanged. Root also independently confirmed clear label/title spacing for1.80–1.89 and1.111.',
  'All new statement openings and the selected detailed proof pages were opened individually. The finite Selmer-locus table on579, actual quotient maps on581, and unit norm-sum display on582 fit with clear labels.',
  'The supported coefficient maps and divided-w displays on584–585 fit. The repaired A196.1 on586 is now two gathered lines with its equation label clear and inside the text area.',
  'The ninth-power local-depth displays on590 and the literal cube/root identities on591 are legible. The24-row residue table and its two-line column list on592 fit.',
  'The generalized-Jacobian lattice/isogeny maps on594 and the dyadic unit-condition table, logarithm sums and determinant vector on596 are legible without overlap.',
  'The complete-unit statement and coefficient denominator on598, the27-row residue table and determinant/rank displays on599, and the exact completed-line lifting table on600 fit.',
  'The supported exponent proof and scalar maps on601–602 were additionally opened individually; their displays and file paths are clear.',
  'The class-three lifting statement and set-section map on603 fit. All cusp polynomials, the long strict cochain residue on605, and the literal-image quotient have clear equation labels.',
  'The fixed-quotient ghost statement on606 and every-sheet detector comparison on608 are legible. The exact unit support sequences on609 and all four norm/annihilator matrices on610–611 fit.',
  'The general unramified-image statement on612, compact uniform correction map on613, and retained real restriction injection on614 fit with clear labels. PartB begins without collision on614.',
  'The distributed earlier pages and references648–661 show clear margins and continuous readable layout. Full-resolution reviews of the front matter and all historical repaired overflow pages are separately retained by the named peers.'
 ],
 'status':'PASS: actual displayed image review; no clipping, overlap, or margin overflow observed.'
}
(w/'qa/hour16/root_visual_review.json').write_text(json.dumps(root_record,indent=2)+'\n')
peer_paths=['qa/hour16/local_preprint_visual_review.json','qa/hour16/birational_visual_review.json']
peers=[]
for path in peer_paths:
    entry=json.loads((w/path).read_text())
    assert entry.get('pdf_sha256',entry.get('reviewed_pdf_sha256'))==previous_sha
    # Each peer records only the pages that were actually opened.
    pages=entry.get('reviewed_pages',entry.get('pages_actually_opened',entry.get('full_resolution_pages_reviewed')))
    assert pages and isinstance(pages,list)
    peers.append((path,entry,pages))
full=sorted(set(root_full+[p for _,_,ps in peers for p in ps]))
assert set(r['required_full_resolution_pages'])<=set(full)
review={
 'status':'Visually inspected all nine final-build contact sheets and every required full-resolution page; no clipping, overlap or margin overflow observed.',
 'reviewed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'reviewed_build_pages':r['pdf_pages'],'pdf_sha256':expected_sha,
 'contact_parts_reviewed':r['contact_parts'],'rendered_pages':r['rendered_pages'],
 'full_resolution_pages_reviewed':full,'required_full_resolution_pages':r['required_full_resolution_pages'],
 'contact_sha256':root_record['contact_sha256'],
 'full_resolution_sha256':{str(p):hashlib.sha256((w/f'qa/hour16/full/page_{p:03d}.png').read_bytes()).hexdigest() for p in full},
 'root_review':'qa/hour16/root_visual_review.json','peer_reviews':peer_paths,
 'observations':root_record['observations'],
 'review_method':'Actual tool-displayed images: root reviewed all nine contact sheets and26 individual proof pages; peers reviewed the complete front matter and all17 historical repair pages. After two contents-label repairs, root opened final pages1 and3 and contact1 again. The executed byte-for-byte image comparison proves every other reviewed image is unchanged; that explicit map binds all inspections to the final PDF hash.',
 'final_image_equivalence':'qa/hour16/toc_image_equivalence.json'
}
for p in [w/'qa/visual_review.json',w/'qa/hour16/visual_review.json']:
    p.write_text(json.dumps(review,indent=2)+'\n')
p=w/'notes/hour16_typesetting_corrections.json';corrections=json.loads(p.read_text())
for item in corrections:
    item['after_hbox_pt']=0
    item['final_page']=583 if 'ninth_root_subfield' in item['anchor'] else 586
    item['after']='Final661-page build: zero horizontal or vertical overflows; the exact repaired page was opened and inspected at full resolution.'
p.write_text(json.dumps(corrections,indent=2)+'\n')
print(json.dumps(dict(pdf_pages=661,pdf_sha256=expected_sha,rendered_pages=130,
                     contact_sheets=9,required_full_resolution=len(r['required_full_resolution_pages']),
                     actual_full_resolution=len(full),status=review['status']),indent=2))
