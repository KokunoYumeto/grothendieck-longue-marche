#!/usr/bin/env python3
"""Record the observed checkpoint-06 visual inspection and exact image comparison."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent.parent
old = json.loads((ROOT/'research/checkpoint06_sixth_visual_qa.json').read_text())
path = ROOT/'research/visual_qa.json'
qa = json.loads(path.read_text())
assert qa['pdf_sha256'] == hashlib.sha256((ROOT/'LM7_PUSH_paper.pdf').read_bytes()).hexdigest()
hashes = {name: hashlib.sha256((ROOT/'build/renders'/name).read_bytes()).hexdigest()
          for name in old['image_sha256']}
changed = sorted(name for name in hashes if hashes[name] != old['image_sha256'][name])
assert changed == ['contact_sheet_14.png', 'page_326.png', 'page_327.png'], changed
log = (ROOT/'build/LM7_PUSH_paper.log').read_text()
assert not any(s in log for s in ('Overfull', 'Warning', 'undefined'))
assert qa['page_count'] == 331
qa['visually_inspected'] = True
qa['inspected_contact_sheets'] = old['inspected_contact_sheets']
qa['full_resolution_inspected_pages'] = old['full_resolution_inspected_pages']
qa['image_sha256'] = hashes
qa['inspection_basis'] = {
    'sixth_pdf': old['pdf_sha256'],
    'sixth_record': 'research/checkpoint06_sixth_visual_qa.json',
    'all_unchanged_images_sha256_verified': True,
    'changed_images_inspected_again': changed,
    'reader': 'root',
}
qa['inspection_notes'] = [
    'All 242 rendered sample pages were inspected in fourteen contact sheets; thirty-two listed pages were inspected at full resolution.',
    'Every formerly overflowing line or display is included: A.31, A.34, D.36, E.45, E.47.11, E.47.22, F.1 and F.26.',
    'The seventh build changes only the rendered coverage pages 326 and 327 and their contact sheet. These three images were inspected again after the mathematical typography and spacing correction. Every other inspected image is byte-identical to the sixth-build image.',
    'No clipping, overlapping equation tags, broken matrices, footer collision, or margin overflow was observed. The exact current build has zero overfull boxes, zero warnings and no undefined references or citations.',
]
path.write_text(json.dumps(qa, indent=2)+'\n')
(ROOT/'research/checkpoint06_visual_qa.json').write_text(json.dumps(qa, indent=2)+'\n')
report = ROOT/'research/report_body.md'
text = report.read_text()
assert 'Checkpoint 06 preserves' not in text
text += '''

Checkpoint 06 preserves the completed Parts A, B, C and F and the concurrent
accepted results D.36--D.39, E.44--E.47 and E.49. Its 331-page PDF contains
180 numbered statements: 166 Proved, 7 Refuted, 3 Known and 4 Open, with all
29 lead and task rows. D.1, D.2, E.2 and E.3 remain unresolved. The separate
D.40 and D.41 drafts, full inner/free A6 calculations for E.48, and the
prime-five symplectic calculations for E.50 are retained as work in progress;
they are outside this checkpoint's compiled statement register.

The first checkpoint-06 typesetting pass failed at a proof-opening command
and recorded two filename overflows, 63.24359 and 35.40152 pt. The second and
third completed builds have zero overfull boxes. The fourth pass failed at
an unbraced accent; its preservation record explicitly distinguishes the
previous complete PDF from the failed build. The fifth completed pass had
two overfull displays, 72.9224 and 11.25229 pt. Both were split in the source.
The sixth complete build has zero overfull boxes. Visual inspection then
identified unformatted mathematics and missing spaces in four coverage-table
rows. Their exact earlier passages are preserved, and the seventh build
corrects that typography without changing the proofs. It has zero overfull
boxes, zero warnings, no undefined citations or references, and verified
hashes for every active source in the actual LuaLaTeX input graph.

All 242 rendered sample pages were inspected in fourteen contact sheets,
and thirty-two pages were inspected at full resolution, including every
formerly overflowing display or filename paragraph and samples across all
six Parts. The seventh build changes only the images of coverage pages 326
and 327 and their contact sheet; all three were inspected again. Every other
inspected image is byte-identical to the sixth-build image. No clipping,
overlapping tags, broken matrix, footer collision or margin overflow was
observed. The exact page list, image hashes and comparison are retained in
`research/checkpoint06_visual_qa.json`. The final PDF SHA-256 is
`560a3619cf5f208b96503470ffd15ed60992f199e63342bd6a85ee4c48335619`.

All seven preserved checkpoint-06 build attempts, all accepted proofs and
their executed certificates, the independent replays, superseded passages,
failed programs and recorded interruptions are retained. Regenerable render
images and caches are excluded with their generating scripts and inspection
records retained. The five earlier checkpoint archives remain unchanged in
`history/`. This checkpoint is an intermediate preservation of active work;
the four unresolved tasks continue beyond it.
'''
report.write_text(text)
search = ROOT/'research/root_searches_02.md'
with search.open('a') as out:
    out.write('''

96. Checkpoint-06 typesetting preserves all seven passes. The fourth failed
    at an unbraced accent; the fifth completed with two overflows, 72.9224
    and 11.25229 pt, in E47.11 and E47.22. Both displays were split. The
    sixth and seventh complete logs have zero overfull boxes, zero warnings,
    no undefined references or citations and verified active-source hashes.
    The seventh pass corrects only coverage-table typography and spacing.
    Earlier passages and the earlier clean PDF remain preserved.

97. Root visually inspected all 242 sampled pages in fourteen contact sheets
    and thirty-two full-resolution pages, including every formerly overflowing
    display and distributed samples. The exact seventh-build render changes
    only pages 326 and 327 and contact sheet 14; these were inspected again,
    with every other image hash unchanged. No clipping or overlap remains.
    The final PDF has 331 pages and SHA256
    560a3619cf5f208b96503470ffd15ed60992f199e63342bd6a85ee4c48335619.

98. Root reopened Broto--Moeller--Oliver Lemma A.1 and its complete proof in
    the author PDF, retrieval turn451view1, printed pages 15--17. The DOI
    resolver failed; the publisher issue result turn452search0 and the
    author's published-PDF search result turn452search4 agree on JAMS 25
    (2012), 1--20, DOI 10.1090/S0894-0347-2011-00713-3. Opening the latter
    PDF timed out (turn453view0). D40's complete integral pairing proof has
    been read by root and independently by geometry; root program replay
    and integration remain pending at checkpoint06.

99. The D41 relative pro-p draft now supplies an exact integral homology
    image and full literal-fibre description. It awaits root audit. E50's
    prime-five residual certificate identifies the actual SL2(F5) factor
    and elementary abelian five-kernels; its common source with the old
    double cover remains under computation. E48's new metabelian source
    has full affine generating fibres over all 864 old points, whereas
    only 288 admit zero module value. The common-source generation and
    remaining perfect-residual comparison are not yet integrated. These
    are ongoing calculations, not answers to the full-source tasks.
''')
print(json.dumps({'status':'PASS','page_count':qa['page_count'],
    'rendered_pages':len(qa['rendered_pages']),
    'contact_sheets':len(qa['contact_sheets']),
    'full_resolution_pages':len(qa['full_resolution_inspected_pages']),
    'pdf_sha256':qa['pdf_sha256'],'changed_images':changed}, indent=2))
