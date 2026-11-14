#!/usr/bin/env python3
"""Record the root's completed actual visual inspection of the current PDF."""
from pathlib import Path
import hashlib
import json

base = Path(__file__).resolve().parents[2]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
pdf = base / 'LM7_FERMAT_TOWER_paper.pdf'
expected = 'd14aa56386e13d3cb32224cbc8d6ecca7543c7e00350d36f2bf55094018ec5d2'
assert sha(pdf) == expected
contacts = [1,17,33,49,65,81,97,113,129,145,161,177,193,209,225,241,257,273,289,305,321,337,353,369,385,401,417,433,449,465,481,497,513,529,545,561,577,593,609,625,641,657,673]
details = [45,46,53,54,222,223,224,225,226,227,228,244,245,632,661,662,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677,678,679,680,681,682,683,684,685]
qa = json.loads((base/'qa/pdf_qa.json').read_text())
manifest = json.loads((base/'qa/detail220_manifest.json').read_text())
assert qa['sha256'] == manifest['pdf_sha256'] == expected
assert contacts == list(range(1,686,16)) and len(contacts) == 43
assert details == manifest['pages'] and len(details) == 39
contact_rows = []
for p in contacts:
    path = base / ('qa/contact_%03d_%03d.jpg' % (p,min(p+15,685)))
    contact_rows.append({'first_page':p,'last_page':min(p+15,685),'path':str(path.relative_to(base)),'sha256':sha(path),'actually_viewed':True})
for row in manifest['images']:
    assert sha(base/row['path']) == row['sha256']
record = {
    'status':'PASS_VISUAL_LAYOUT', 'pdf_sha256':expected, 'pdf_pages':685,
    'reviewer':'root assistant',
    'all_contact_sheets_actually_viewed':True, 'contact_sheets':contact_rows,
    'detail_pages_actually_viewed':details, 'detail_images':manifest['images'],
    'inspection_findings':'All 43 page overview sheets and all 39 specified 110-dpi detail pages were actually opened and visually inspected. No clipping, overlapping material, broken table, empty page, or displaced equation label was observed. Page 677 contains the short proof ending and is not blank.',
    'scope':'Full-document layout overview; entire newly integrated D62 and E117 proofs and adjoining pages; complete E118 and bibliography; updated D13/D19/E23 conclusions and E112 forward status. Mathematical proof audits are separate retained records.',
    'truncated_tool_result_handling':'Detail pages 661 and 662 were reopened and actually viewed after the earlier output-truncated call. The truncated result was not counted as a view.'
}
(base/'qa/visual220_root.json').write_text(json.dumps(record,indent=2)+'\n')
(base/'qa/visual_review.md').write_text(
    '# Actual visual review of the assembled 220-statement paper\n\n'
    'PDF SHA256: `'+expected+'`. Pages: 685.\n\n'
    'All 43 contact sheets, covering pages 1-685, were actually opened and inspected by the root assistant. All 39 detail images listed in visual220_root.json were separately opened at 110 dpi: pages 45-46, 53-54, 222-228, 244-245, 632 and 661-685. This covers the entire newly integrated D62 and E117 proofs, adjoining material, the complete E118 proof, every bibliography page, and the updated D13/D19/E23 conclusions and E112 forward status.\n\n'
    'No clipping, overlap, broken table, blank page, or displaced equation label was observed. Page 677 contains the short proof ending. The automatic renderer separately checked all 220 statement headings and page borders. The detailed proof and arithmetic-replay audits remain separate from this layout review.\n\n'
    'The earlier truncated tool return was not used as visual evidence; detail pages 661 and 662 were reopened successfully. The previous checkpoint review remains archived under qa/history/checkpoint218_before220.\n')
source_log = base/'ledger/d_original_source_recheck.md'
old = source_log.read_text()
assert 'turn1024' not in old
source_log.write_text(old+'\nRetrieval family turn1024 checked the exact Coleman1989 title at the Mathematical Society of Japan, the exact Ihara1986 title with previously exhausted original hosts excluded, and the RIMS1177 PDF identifier. It returned CiNii metadata and separate later citing works, including a Hiroshima teaching manuscript and Hain--Matsumoto2003. No requested original PDF was retrieved, and those separate works were not opened or substituted as verification of the requested originals. No original-proof label changed.\n')
print(json.dumps({'status':'PASS','pdf_sha256':expected,'contacts_actually_viewed':43,'details_actually_viewed':39,'visual_record_sha256':sha(base/'qa/visual220_root.json'),'source_retrieval_family_recorded':'turn1024'},indent=2))

