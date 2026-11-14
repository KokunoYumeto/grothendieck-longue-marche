"""Record actual model image inspection and validate the three review records.

This program hashes the reviewed images; it does not perform visual inspection.
The image inspection was performed before this program was run.
"""
from pathlib import Path
import hashlib
import json
import shutil

BASE = Path(__file__).resolve().parents[1]
QA = BASE / 'qa'
digest = 'ad61c2e1120a18288d49259048e5e80013baad81395248ecc33e8753b294658d'
assert hashlib.sha256((BASE / 'LM7_FERMAT_TOWER_paper.pdf').read_bytes()).hexdigest() == digest
data = json.loads((QA / 'pdf_qa.json').read_text())
assert data['sha256'] == digest and data['pages'] == 560
files = []
for start in range(353,561,16):
    rel = f'qa/contact_{start:03d}_{min(start+15,560):03d}.jpg'
    files.append({'path': rel, 'sha256': hashlib.sha256((BASE / rel).read_bytes()).hexdigest(),
                  'finding': 'PASS: actually viewed at contact-sheet resolution; no visible clipping, overlap, missing page/text blocks, or unexpected blank pages.'})
details = json.loads((QA / 'details200/manifest.json').read_text())
assert details['pdf_sha256'] == digest
assert [i['page'] for i in details['files']] == [1, *range(188,194), *range(535,554), 554, 560]
for entry in details['files']:
    assert hashlib.sha256((BASE / entry['path']).read_bytes()).hexdigest() == entry['sha256']
root = {'status':'PASS', 'checkpoint':200, 'pdf_sha256':digest,
        'scope':'Root actually viewed all13 contact sheets covering pages353-560 and all28 retained110dpi full-page images. The latter include every page of D56, E101, E103 and E104, the two E102 boundary pages, the title page and two bibliography pages. This is layout inspection, not a replacement for the separately retained proof and program audits.',
        'files':files, 'full_page_details':details['files'],
        'finding':'No clipping, overlapping formula numbers, malformed matrices, missing glyphs, or margin collisions observed. The repaired E101 coefficient transpose and both fifteen-column matrices are fully legible.'}
(QA / 'visual200_root.json').write_text(json.dumps(root, indent=2) + '\n')
all_paths = set(f['path'] for f in files)
for stem in ('visual200_a','visual200_d'):
    report = json.loads((QA / (stem+'.json')).read_text())
    assert report['status'] == 'PASS'
    assert digest in json.dumps(report)
    for entry in report['files']:
        assert hashlib.sha256((BASE / entry['path']).read_bytes()).hexdigest() == entry['sha256']
        assert entry['path'] not in all_paths
        all_paths.add(entry['path'])
assert all_paths == set(data['contact_sheets']) and len(all_paths) == 35
old = QA / 'visual_review.md'
backup = QA / 'visual_review196.md'
if not backup.exists():
    shutil.copy2(old, backup)
old.write_text(f'''# Checkpoint200 visual review

PDF SHA256: `{digest}`.

The final560-page PDF completed all three LuaLaTeX passes and BibTeX before rendering began. The build certificate reports no undefined references or citations, missing characters, or overfull boxes. Poppler rendered all560 pages. All200 statement headings are present; no page is empty and no word crosses the twelve-point safety border.

All35 refreshed contact sheets were actually viewed: a_structure reviewed pages1-176, d_galois reviewed pages177-352, and root reviewed pages353-560. The exact image filenames, SHA256 values and findings are in visual200_a.json, visual200_d.json and visual200_root.json. These are contact-resolution layout inspections.

Root additionally viewed all28 retained full-page images at110dpi in details200. These include every page of the four new sections, the E102 boundary, the title page and two bibliography pages. No clipping, overlapping equation numbers, missing glyphs, malformed matrices or margin collisions were observed. The E101 formula repairs preserve the checked coefficient matrix through its displayed exact transpose; their complete source diff and coefficient checks are in ledger/checkpoint200_layout_corrections.json.

The first build's actual column-limit failure and overfull displays are retained in code/build200_initial_layout_failure.out. The successful complete build is code/build200.out. Visual review does not replace the separate full-proof reads, exact program rebuilds and independent peer audits.
''')
print(json.dumps({'status':'PASS', 'pdf_sha256':digest, 'pages':560,
                  'actually_viewed_contact_sheets':len(all_paths),
                  'root_actually_viewed_full_pages':len(details['files'])}, indent=2))
