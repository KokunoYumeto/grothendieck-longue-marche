"""Record completed visible PDF inspection; this script does not perform it."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
m = json.loads((root / 'records/checkpoint16_metrics.json').read_text())
assert hashlib.sha256((root / 'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest() == m['pdf_sha256']
assert m['statements'] == 258 and m['pages'] == 348
assert m['statuses'] == {'Known': 6, 'Proved': 216, 'Refuted': 17, 'Open': 19}
assert not m['overfull'] and not m['warnings'] and not m['errors']
manifest = json.loads((root / 'records/pdf_qa/checkpoint16_final/render_manifest.json').read_text())
pages = manifest['rendered_pages']
assert len(pages) == 45 and manifest['page_count'] == 348
enlarged = [1, 2, *range(245, 262), 341, 342, 344, 348]
assert len(enlarged) == 23 and set(enlarged) <= set(pages)
bib = re.split(r'(?m)(?=^@)', (root / 'LM4_SUCCESSOR_references.bib').read_text())[1:]
assert len(bib) == 104 and all(re.search(r'\b(?:unverified|verified)\b', e, re.I) for e in bib)
initial = json.loads((root / 'records/checkpoint16_initial_metrics.json').read_text())
assert initial['pages'] == 343 and initial['statements'] == 256
assert not initial['overfull'] and not initial['warnings'] and not initial['errors']

record = f'''# Sixteenth-hour final PDF typesetting and visual verification

Final PDF SHA-256: {m['pdf_sha256']}.
Final size: {m['pdf_bytes']} bytes; {m['pages']} pages.
Register: {m['statements']} statements; {m['statuses']}.
Bibliography records: {m['bibliography_entries']}; task rows: {m['task_rows']}.
Visual review: PASS.

The first complete B84--B87 integration produced a clean 343-page PDF
with 256 statements. Its PDF and metrics remain separately preserved.
The subsequent B88--B89 integration produced the final 348-page PDF
with 258 statements. The final build process completed successfully
before its final metrics were computed. Both complete builds have zero
overfull boxes, warnings, undefined references, and errors. Before/after
overfull counts are 0/0, also for boxes exceeding 2pt. No layout repair
was needed in this cycle.

An intermediate metrics command was inadvertently run while the second
build was still active. It observed a partial first-pass 340-page file
without References. Its observation is preserved under
checkpoint16_during_build_metrics.json/.out and is not treated as a
successful final build or final PDF verification. All final metrics,
renderings, and visible inspection below concern the completed second
build and the SHA-256 given above.

We rendered 45 final pages and visibly reviewed all five contact sheets,
one image per call. The earlier two-image output was truncated and is not
counted as a review; both affected sheets were reopened individually.
We also displayed and inspected 23 critical final pages individually at
full size: the title/abstract, contents, every new B84--B89 proof page,
the Brown/Brown--Loday and Deligne bibliography pages, the Herfort--Ribes
entry, and the final page. No clipping, colliding equation tags, missing
mathematical glyphs, or defective proof layout was found. The six new
statements, exact finite detector table, compact-topology proof, and
scope paragraphs are legible. All 104 bibliography entries have an
explicit verified or unverified label.

Rendered final pages:
{pages}

Full-size critical final pages:
{enlarged}

Final driver: records/checkpoint16_build2_driver.log.
Final complete pass logs: records/build_passes/20261116T162500958338Z/.
Initial driver: records/checkpoint16_build1_driver.log.
Initial complete pass logs: records/build_passes/20261116T161127027900Z/.
Preserved initial PDF: records/checkpoint16_initial_paper.pdf.
Metrics: records/checkpoint16_metrics.json and checkpoint16_final_metrics.out.
Renderings: records/pdf_qa/checkpoint16_final/.

Recorded at {datetime.now(timezone.utc).isoformat()}.
'''
(root / 'records/checkpoint16_typesetting.txt').write_text(record)
p = root / 'LM4_SUCCESSOR_report.md'
s = p.read_text()
marker = '### Sixteenth-hour final typesetting verification'
assert marker not in s
s += f'''\n{marker}

The final paper has {m['pages']} pages and {m['pdf_bytes']} bytes, SHA-256
{m['pdf_sha256']}. Both complete builds have zero overfull boxes,
warnings, undefined references, and errors; before/after overfull counts
are 0/0, also beyond 2pt. The initial 343-page B84--B87 integration is
preserved separately from the final 348-page B84--B89 integration. The
inadvertent observation of a 340-page in-progress first pass is preserved
as an intermediate observation and is not final verification. We viewed
all five final contact sheets for 45 rendered pages and 23 critical final
pages at full size, including every new proof page and the relevant
bibliography entries. No clipping, overlapping tags, missing glyphs, or
defective layout was found. All 104 references have explicit verification
status. Exact page and build records are in
records/checkpoint16_typesetting.txt. Both main full decisions remain Open.
'''
p.write_text(s)
print('Final PDF QA recorded: 45 pages, 5 contact sheets, 23 full-size pages; PASS.')
