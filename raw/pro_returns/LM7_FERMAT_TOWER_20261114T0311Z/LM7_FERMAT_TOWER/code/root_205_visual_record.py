"""Record actual image reviews and verify their frozen image/PDF identities.

The observations were made through the image tool by the named reviewers.
This program verifies files and coverage; it does not claim to inspect images.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

BASE = Path(__file__).resolve().parents[1]
QA = BASE / 'qa'
PDF_HASH = '21253d5b111c7825e82ef7e1c3d4a35a78b95d271708724c1af6b83a2b89227c'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

assert sha(BASE / 'LM7_FERMAT_TOWER_paper.pdf') == PDF_HASH
records = []
for first in range(385, 589, 16):
    last = min(first + 15, 588)
    path = QA / f'contact_{first:03d}_{last:03d}.jpg'
    records.append({'file': str(path.relative_to(BASE)), 'sha256': sha(path),
                    'pages': [first, last], 'actually_viewed': True,
                    'observations': 'Root actually viewed this contact sheet. Text blocks, tables and matrices fit; no clipping, overlap, unexpected blank layout or footer collision observed at contact resolution.'})
detail_pages = [45, 53, 220] + list(range(564, 582))
details = []
manifest = json.loads((QA / 'detail205_manifest.json').read_text())
assert manifest['pdf_sha256'] == PDF_HASH
for n in detail_pages:
    path = QA / f'detail205_page_{n:03d}.jpg'
    digest = sha(path)
    assert any(x['page'] == n and x['sha256'] == digest for x in manifest['pages'])
    details.append({'page': n, 'file': str(path.relative_to(BASE)),
                    'sha256': digest, 'actually_viewed': True,
                    'observations': 'Root viewed the returned 110-dpi image. Displays, matrices, equation numbers and text remain legible and within the margins. No clipping or overlap observed.'})
peer_files = ['visual205_a.json', 'visual205_d.json', 'visual205_d_detail.json']
peer_records = []
for name in peer_files:
    path = QA / name
    data = json.loads(path.read_text())
    assert data['pdf_sha256'] == PDF_HASH and data['status'] == 'PASS'
    peer_records.append({'file': 'qa/' + name, 'sha256': sha(path)})
record = {'checkpoint': 205, 'reviewer': 'root',
          'recorded_at_utc': datetime.now(timezone.utc).isoformat(),
          'pdf_sha256': PDF_HASH, 'pdf_pages': 588,
          'status': 'PASS for layout; editorial spacing observations retained',
          'contact_sheets_actually_viewed': records,
          'detail_images_actually_viewed': details,
          'peer_reviews': peer_records,
          'editorial_observations': [
              {'page': 45, 'examples': ['actual864', 'spaceand', 'order3888', 'dimension2560'],
               'action': 'Insert missing prose spaces in the next manuscript integration; no formula or mathematical status change.'},
              {'pages': [573, 576, 580], 'examples': ['folios733', 'complete.16', 'Hilbert90'],
               'action': 'Inspect the literal source and repair missing prose spaces during the next editorial pass.'}],
          'scope': 'Actual image-tool layout review. The unsuccessful truncated five-image request is not counted. Mathematical proofs and numerical certificates have separate audits.'}
(QA / 'visual205_root.json').write_text(json.dumps(record, indent=2) + '\n')
prior = QA / 'visual_review.md'
history = QA / 'history'
history.mkdir(exist_ok=True)
old = prior.read_text()
if 'Checkpoint200' in old:
    (history / 'visual_review_checkpoint200.md').write_text(old)
prior.write_text(f'''# Checkpoint205 visual review

PDF SHA256: `{PDF_HASH}`.

The 588-page PDF completed three LuaLaTeX passes and BibTeX. The build certificate reports no undefined references or citations, missing characters, or overfull boxes. All 588 pages rendered successfully. The automated geometry check found every one of the 205 statement headings, no empty page, and no word outside its safety border.

All 37 current contact sheets were actually viewed: a_structure reviewed pages 1–192, d_galois reviewed pages 193–384, and root reviewed pages 385–588. The exact image identities and observations are in visual205_a.json, visual205_d.json and visual205_root.json. These contact-resolution reviews found no clipping, overlap, unexpected blank page or missing text block.

All 31 retained detail images at 110 dpi were also actually viewed. Root inspected pages 45, 53, 220 and 564–581; d_galois inspected pages 194–203. The corresponding records are visual205_root.json and visual205_d_detail.json. The revised proof displays, large matrices and repaired E107.13 display are legible and fit their margins. A few missing prose spaces in progress paragraphs and citation-adjacent text are explicitly recorded for the next editorial pass. No claim of flawless copy editing is made.

The initial checkpoint204 build's actual overfull-display failure remains in code/checkpoint204_first_build/. The exact layout-only change is ledger/e107_display_amendment.json. The successful current build and render have their own actual outputs and certificates. Visual review does not replace the complete proof reads, original-source reads, fresh program executions and independent peer audits.
''')
out = {'pdf_sha256': PDF_HASH, 'contact_sheets': 37, 'detail_images': 31,
       'root_contact_sheets': len(records), 'root_detail_images': len(details),
       'peer_reports_verified': len(peer_records), 'image_identities_verified': True,
       'editorial_observations_recorded': True,
       'visual_review_sha256': sha(prior), 'root_record_sha256': sha(QA / 'visual205_root.json')}
text = json.dumps(out, indent=2) + '\n'
Path(__file__).with_suffix('.out').write_text(text)
print(text, end='')
