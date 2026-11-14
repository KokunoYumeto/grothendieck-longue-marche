#!/usr/bin/env python3
"""Record the root's completed actual visual inspection of the current PDF."""
from pathlib import Path
import hashlib
import json

base = Path(__file__).resolve().parents[2]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
pdf = base / 'LM7_FERMAT_TOWER_paper.pdf'
expected = '792de5e54e0b7513bb3d006bbc76d046b0b636aec16572a622254e179a721899'
assert sha(pdf) == expected
contacts = [1,17,33,49,65,81,97,113,129,145,161,177,193,209,225,241,257,273,289,305,321,337,353,369,385,401,417,433,449,465,481,497,513,529,545,561,577,593,609,625,641,657]
details = [216,217,218,219,220,221,222,619,626,636,641,642,643,644,645,646,647,648,649,650,651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667]
qa = json.loads((base/'qa/pdf_qa.json').read_text())
manifest = json.loads((base/'qa/detail218_manifest.json').read_text())
assert qa['sha256'] == manifest['pdf_sha256'] == expected
assert contacts == list(range(1,668,16)) and len(contacts) == 42
assert details == manifest['pages'] and len(details) == 37
contact_rows = []
for p in contacts:
    path = base / ('qa/contact_%03d_%03d.jpg' % (p,min(p+15,667)))
    contact_rows.append({'first_page':p,'last_page':min(p+15,667),'path':str(path.relative_to(base)),'sha256':sha(path),'actually_viewed':True})
for row in manifest['images']:
    assert sha(base/row['path']) == row['sha256']
record = {
    'status':'PASS_VISUAL_LAYOUT', 'pdf_sha256':expected, 'pdf_pages':667,
    'reviewer':'root assistant',
    'all_contact_sheets_actually_viewed':True, 'contact_sheets':contact_rows,
    'detail_pages_actually_viewed':details, 'detail_images':manifest['images'],
    'inspection_findings':'All 42 page overview sheets and all 37 specified 110-dpi detail pages were actually opened and visually inspected. No clipping, overlapping material, broken table, empty page, or displaced equation label was observed.',
    'scope':'Full-document layout overview; entire D61, E115, E116 and E118 additions and all bibliography pages at detail resolution; changed-spacing samples at E111, E112 and E114. Mathematical proof audits are separate retained records.',
    'truncated_tool_result_handling':'Contacts beginning at417 and433 were reopened and actually viewed after the earlier output-truncated call. The truncated result was not counted as a view.'
}
(base/'qa/visual218_root.json').write_text(json.dumps(record,indent=2)+'\n')
(base/'qa/visual_review.md').write_text(
    '# Actual visual review of the assembled 218-statement paper\n\n'
    'PDF SHA256: `'+expected+'`. Pages: 667.\n\n'
    'All 42 contact sheets, covering pages 1-667, were actually opened and inspected by the root assistant. All 37 detail images listed in visual218_root.json were separately opened at 110 dpi: pages 216-222, 619, 626, 636 and 641-667. This covers the entire newly integrated D61, E115, E116 and E118 proofs, their adjoining material, every bibliography page, and the three earlier spacing samples.\n\n'
    'No clipping, overlap, broken table, blank page, or displaced equation label was observed. The automatic renderer separately checked all 218 statement headings and page borders. The detailed proof and arithmetic-replay audits remain separate from this layout review.\n\n'
    'The earlier truncated tool return was not used as visual evidence; its two contact sheets were reopened successfully. The previous checkpoint review remains archived under qa/history/checkpoint214_before218.\n')
source_log = base/'ledger/d_original_source_recheck.md'
old = source_log.read_text()
assert 'turn1020' not in old
source_log.write_text(old+'\nThe further exact-title PDF and Kyoto repository search in retrieval family turn1020 returned the same NDL Coleman record, the Ihara author bibliography, later citations, and the separate Tilouine exposition and Ihara ICM lecture. No requested original Ihara1986, Coleman1989 or Ihara1999 PartI proof was obtained. Those separate works were not substituted for the requested originals, and no original-proof verification label changed.\n')
print(json.dumps({'status':'PASS','pdf_sha256':expected,'contacts_actually_viewed':42,'details_actually_viewed':37,'visual_record_sha256':sha(base/'qa/visual218_root.json'),'source_retrieval_family_recorded':'turn1020'},indent=2))
