"""Record only the root page/contact images actually opened individually."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

root=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256((root/p).read_bytes()).hexdigest()
expected='2124bdcf0bc9e3fc34f0bb69d2c232ef216f94ab56ed3afae7045cbea275add1'
assert sha('LM4_SUCCESSOR_paper.pdf')==expected
render='records/pdf_qa/checkpoint36_final/render_manifest.json'
observations={
 1:'Title, GPT-6 Astra credit, date, explicit INCOMPLETE status and opening abstract are legible; all margins and page number are clear.',
 2:'New elliptic cubic, derived transporter, exact boundary obstruction and unchanged open-class scope render clearly within the abstract; no missing glyphs or clipping.',
 4:'New complementary-contact summary and remaining-open qualifications are intact; the contents opening and Part A page reference fit with clear separation.',
 684:'The complete E52 statement/proof and References opening are legible. The corrected space after printed page159 now separates the citation clearly; its line break causes no collision. The centralizer display and proof-ending square fit.',
 687:'The new Enriquez entry begins with correct author/year/title/journal/volume/pages at the bottom; the preceding complete bibliography text is legible and unclipped. Its continuation is separately inspected on688.',
 688:'The complete continuation of the new Enriquez verification-scope note is clear, including the full profinite category and limited whole-paper claim. All other entries fit with intact accents and formulas.',
 695:'Final bibliography entries and precise primary-reading scopes are legible; the last page number and lower margin are clear, with no clipped material.'
}
pages=[]
for n,obs in observations.items():
    path=f'records/pdf_qa/checkpoint36_final/page-{n:03d}.png'
    pages.append(dict(page=n,path=path,sha256=sha(path),actually_viewed_individually=True,result='PASS',observation=obs,issues=[]))
contacts=[]
for n in range(1,7):
    path=f'records/pdf_qa/checkpoint36_final/contact-{n:02d}.png'
    contacts.append(dict(path=path,sha256=sha(path),actually_viewed_separately=True,result='PASS',issues=[]))
record=dict(recorded_at=datetime.now(timezone.utc).isoformat(),reviewer='/root',result='PASS',
    pdf_sha256=expected,render_manifest_sha256=sha(render),truncated_outputs_counted=False,
    pages=pages,contacts=contacts,
    contact_observation='All six contact images were opened in six separate actual image outputs. Their51 rendered pages have consistent margins and intact formulas, headings and page numbers; no clipping or overlap was observed. The27 new mathematical pages and legacy correction intervals also have separate individual reviewer receipts.',
    nonblocking_notes=[],issues=[])
with (root/'records/checkpoint36_root_visual_observations.json').open('x') as stream:
    json.dump(record,stream,indent=2);stream.write('\n')
print('Recorded7 actual individual page images and6 separately opened contact images; no invented or text-only image inspection.')
