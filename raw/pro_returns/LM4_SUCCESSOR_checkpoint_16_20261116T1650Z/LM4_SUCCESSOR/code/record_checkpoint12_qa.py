"""Record completed visual inspection; this script does not perform it."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parents[1]
m = json.loads((root / 'records/checkpoint12_metrics.json').read_text())
assert hashlib.sha256((root / 'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest() == m['pdf_sha256']
assert not m['overfull'] and not m['warnings'] and not m['errors']
manifest = json.loads((root / 'records/pdf_qa/checkpoint12_final/render_manifest.json').read_text())
comparison = json.loads((root / 'records/checkpoint12_render_comparison.json').read_text())
pages = manifest['rendered_pages']
assert len(pages) == 42 and comparison['changed_page_images'] == [108]
assert len(comparison['same_page_images']) == 41
enlarged = [1, 108, 109, 110, 206, 208, 211, 212, 213]
assert set(enlarged) <= set(pages)
text = f'''# Twelfth-hour final PDF typesetting and visual verification

Final PDF SHA-256: {m['pdf_sha256']}.
Final size: {m['pdf_bytes']} bytes; {m['pages']} pages.
Register: {m['statements']} statements; {m['statuses']}.
Bibliography records: {m['bibliography_entries']}; task rows: {m['task_rows']}.
Visual review: PASS.

Both complete LuaLaTeX builds have zero overfull boxes, warnings,
undefined references and errors: before/after0/0, including boxes
exceeding2pt. Before the first build, eighteen missing display closers
in the B78 draft were repaired. The initial register integration also
needed the three new B inputs in the combined paper; its exact scope
is recorded in checkpoint12_initial_integration_failure.txt. Neither
pre-build issue is represented as a failed complete TeX build.

The preliminary300-page PDF was rendered on42 pages. All five contact
sheets were visually inspected, covering every new A77-A78 and
B76-B78 page, adjacent pages, title, contents, every Part, and the
complete rendered bibliography range. Nine critical pages were also
read at full rendered size. That inspection found one missing space
before a citation in A77; it was repaired in all three source copies.
No clipped text, crossed equation tags, missing mathematical glyphs,
or defective table placement was observed.

The final PDF was rebuilt and all42 pages were rendered again.
SHA256 comparison proves that41 final page PNGs are byte-identical
to the images just reviewed. Only page108 changed; the final version
was separately viewed at full size and passes. The exact comparison
is records/checkpoint12_render_comparison.json. The preliminary PDF
and renderings are preserved, not silently represented as final.

Final rendered pages:
{pages}

Full-size critical pages (with final page108 rechecked):
{enlarged}

Final driver:records/checkpoint12_final_build_driver.log.
Final complete per-pass logs:records/build_passes/20261116T122704539396Z/.
Preliminary driver:records/checkpoint12_build1_driver.log.
Preliminary per-pass logs:records/build_passes/20261116T122253784357Z/.
Final metrics:records/checkpoint12_metrics.json and
records/checkpoint12_final_metrics.out.
Final renderings:records/pdf_qa/checkpoint12_final/.
Preliminary renderings and PDF:records/pdf_qa/checkpoint12_preliminary/.

No mathematical source or PDF change follows this final inspection.
Recorded at {datetime.now(timezone.utc).isoformat()}.
'''
(root / 'records/checkpoint12_typesetting.txt').write_text(text)
p = root / 'LM4_SUCCESSOR_report.md'
s = p.read_text()
marker = '### Twelfth-hour final typesetting verification'
assert marker not in s
s += f'''\n{marker}

The final paper has{m['pages']} pages and{m['pdf_bytes']} bytes, SHA-256
{m['pdf_sha256']}.
Both complete builds have zero overfull boxes, warnings, undefined
references and errors: before/after0/0, including boxes beyond2pt.
We rendered42 pages covering all new proofs and a sample across the
whole document, and inspected all five contact sheets and9 enlarged
critical pages. After correcting one citation-spacing defect, the
final rerender has41 byte-identical reviewed page images and only
page108 changed; that final page was rechecked at full size. No
clipping, overlapping equation tags, missing glyphs or misplaced
tables was found. Complete details and preserved preliminary/final
records are in records/checkpoint12_typesetting.txt.
'''
p.write_text(s)
print('Final PDF QA recorded:42 pages,9 enlarged;41 identical and final108 reviewed.')
