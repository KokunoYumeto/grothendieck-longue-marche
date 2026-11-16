"""Record completed visual inspection; this script does not perform that inspection."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parents[1]
m = json.loads((root / 'records/checkpoint11_metrics.json').read_text())
assert hashlib.sha256((root / 'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest() == m['pdf_sha256']
manifests = [json.loads((root / p).read_text()) for p in (
    'records/pdf_qa/checkpoint11_final/render_manifest.json',
    'records/pdf_qa/checkpoint11_A56_update/render_manifest.json')]
pages = sorted({n for manifest in manifests for n in manifest['rendered_pages']})
assert len(pages) == 52
enlarged = [1, 62, 63, 64, 95, 96, 97, 100, 102, 104, 105, 106, 107, 201, 202]
assert set(enlarged) <= set(pages)
text = f'''# Eleventh-hour final PDF typesetting and visual verification

Final PDF SHA-256: {m['pdf_sha256']}.
Final size: {m['pdf_bytes']} bytes; {m['pages']} pages.
Register: {m['statements']} statements; {m['statuses']}.
Bibliography entries: {m['bibliography_entries']}; requested task rows: {m['task_rows']}.
Visual review: PASS.

The first three integration builds failed on display delimiters and
bibliography syntax. Four missing B75 display closers were repaired;
the first repair also introduced a duplicate closer, corrected in the
next attempt. The ATLAS corporate author and no-date field were made
explicit, and stale bibliography auxiliaries were preserved before
regeneration. Two bare math commands and malformed exponent commas in
new A sections were also corrected. Genuine failed driver outputs and
the saved failed bibliography files are retained. The earliest two
full per-pass TeX stdout files were overwritten before per-pass archival
was added; we do not claim those unavailable full stdout bytes survive.

The first complete eleventh-hour build had zero overfull boxes, warnings,
undefined references and errors. The final build, incorporating A76,
the updated abstract and A56's revised scope, also has zero in each
category. Complete-build counts before/after:0/0; boxes over2pt:0/0.

We rendered52 unique pages from the final290-page PDF. The49-page main
render includes every page of A70-A76 and B75, adjacent pages, title,
contents, references, and a sample spread across every Part. Its six
contact sheets were visually inspected. The additional three-page
render covers the revised A56 statement and adjacent proof pages.
The exact unique rendered pages are:
{pages}

We additionally inspected these15 pages at full rendered size:
{enlarged}
No clipped text, overlapping display tags, missing symbols, or misplaced
formula/table material was observed. The title and status, updated A56
scope, new matrix/table proofs, exact norm invariant and Birman formulas
are legible. No formal source or PDF change follows this visual review.

The final build driver is records/checkpoint11_final_build_driver.log.
The final full per-pass outputs are under
records/build_passes/20261116T113350081997Z/; compatibility build_i.log
files are also retained. The first clean preliminary build is separately
identified by checkpoint11_build4_driver.log and its metrics stdout.
Final metrics are records/checkpoint11_metrics.json and
records/checkpoint11_final_metrics.out. Render manifests and all PNGs
are retained in the two directories named above.

Recorded at {datetime.now(timezone.utc).isoformat()}.
'''
(root / 'records/checkpoint11_typesetting.txt').write_text(text)
p = root / 'LM4_SUCCESSOR_report.md'
s = p.read_text()
marker = '### Eleventh-hour final typesetting verification'
if marker not in s:
    s += f'''\n{marker}

The final paper has{m['pages']} pages and{m['pdf_bytes']} bytes, with SHA-256
{m['pdf_sha256']}.
The initial complete and final complete builds both have zero overfull
boxes, warnings, undefined references and errors: before/after0/0,
including boxes beyond2pt. Earlier failed syntax/bibliography integration
attempts and the limits of their preserved stdout are documented in
records/checkpoint11_typesetting.txt. We rendered and visually inspected
52 pages across all Parts, including every new result and the updated
A56 statement, with15 enlarged critical pages. No clipping, crossed
display tags or missing mathematical glyphs was observed. The formal
paper is frozen after this review; later research is saved separately.
'''
    p.write_text(s)
print('Final PDF visual QA recorded:52 unique pages,15 enlarged,zero log defects.')
