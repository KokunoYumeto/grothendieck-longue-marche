"""Record the completed visible inspection; this script does not perform it."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
m = json.loads((root / 'records/checkpoint17_metrics.json').read_text())
assert hashlib.sha256((root / 'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest() == m['pdf_sha256']
assert m['statements'] == 261 and m['pages'] == 357
assert m['statuses'] == {'Known': 6, 'Proved': 219, 'Refuted': 17, 'Open': 19}
assert not m['overfull'] and not m['warnings'] and not m['errors']
manifest = json.loads((root / 'records/pdf_qa/checkpoint17_final/render_manifest.json').read_text())
pages = manifest['rendered_pages']
assert len(pages) == 40 and manifest['page_count'] == 357
enlarged = [1, 2, *range(261, 271), 350, 357]
assert len(enlarged) == 14 and set(enlarged) <= set(pages)
bib = re.split(r'(?m)(?=^@)', (root / 'LM4_SUCCESSOR_references.bib').read_text())[1:]
assert len(bib) == 104 and all(re.search(r'\b(?:unverified|verified)\b', e, re.I) for e in bib)
initial = json.loads((root / 'records/checkpoint17_initial_overflow_metrics.json').read_text())
second = json.loads((root / 'records/checkpoint17_second_build_metrics.json').read_text())
assert initial['pages'] == second['pages'] == 354
assert initial['statements'] == second['statements'] == 260
assert len(initial['overfull']) == 1 and '19.57776pt' in initial['overfull'][0]
assert not initial['warnings'] and not initial['errors']
assert not second['overfull'] and not second['warnings'] and not second['errors']
assert hashlib.sha256((root / 'records/checkpoint17_second_build_paper.pdf').read_bytes()).hexdigest() == second['pdf_sha256']

record = f'''# Seventeenth-hour final PDF typesetting and visual verification

Final PDF SHA-256: {m['pdf_sha256']}.
Final size: {m['pdf_bytes']} bytes; {m['pages']} pages.
Register: {m['statements']} statements; {m['statuses']}.
Bibliography records: {m['bibliography_entries']}; task rows: {m['task_rows']}.
Visual review: PASS.

The first complete B90--B91 integration produced a 354-page PDF with260
statements. All TeX passes finished, but the layout gate correctly failed
one display extending19.57776pt beyond the right margin. We preserved its
exact source, genuine pass logs, final log, failure metrics and rendered
page261. An initial image call was truncated and was not counted as a
review; we reopened the single page and inspected it. The first B90
module display was split into two aligned lines without changing its
mathematics.

The second complete build has354 pages and zero overfull boxes, warnings,
undefined references or errors. Its completed PDF and metrics are
preserved separately. We viewed the corrected page261. The subsequent
B92 integration produced the final357-page,261-statement PDF. It also
has zero overfull boxes, warnings, undefined references and errors.
Thus the before/after overfull counts are1/0, including beyond2pt;
the maximum decreased from19.57776pt to0pt. Final metrics were computed
only after the producer completed successfully.

We rendered40 final pages and visibly reviewed all five contact sheets,
one image per call. We also displayed and inspected14 critical final
pages individually at full size: title/abstract, contents, every new
B90--B92 proof page including the continuation onto270, the Brown and
Brown--Loday bibliography page, and the final bibliography page. No
clipping, colliding equation tags, missing mathematical glyphs, or
defective proof layout was found. All104 bibliography entries have an
explicit verified or unverified status in the bibliography source.

Rendered final pages:
{pages}

Full-size critical final pages:
{enlarged}

Final driver: records/checkpoint17_build3_driver.log.
Final complete pass logs: records/build_passes/20261116T171838283836Z/.
Second driver: records/checkpoint17_build2_driver.log.
Second complete pass logs: records/build_passes/20261116T170635406807Z/.
Initial driver: records/checkpoint17_build1_driver.log.
Initial complete pass logs: records/build_passes/20261116T170406013333Z/.
Initial diagnostic PDF: records/checkpoint17_before_layout_fix_check.pdf.
The diagnostic PDF is a transient overflowing preview excluded by the
established packager; its exact source, logs, metrics and image remain.
Preserved successful second PDF: records/checkpoint17_second_build_paper.pdf.
Final metrics: records/checkpoint17_metrics.json and checkpoint17_final_metrics.out.
Final renderings: records/pdf_qa/checkpoint17_final/.

Recorded at {datetime.now(timezone.utc).isoformat()}.
'''
(root / 'records/checkpoint17_typesetting.txt').write_text(record)
p = root / 'LM4_SUCCESSOR_report.md'
s = p.read_text()
marker = '### Seventeenth-hour final typesetting verification'
assert marker not in s
s += f'''\n{marker}

The final paper has {m['pages']} pages and {m['pdf_bytes']} bytes, SHA-256
{m['pdf_sha256']}. The first complete B90--B91 build had one19.57776pt
overfull display. We viewed the offending page, split the display, and
rebuilt cleanly. The subsequent B92 integration also has zero overfull
boxes, warnings, undefined references or errors. Before/after overfull
counts are1/0, also beyond2pt. Both the successful second build and the
initial failure diagnostics remain distinct. The overflowing preview
PDF is excluded as a superseded transient typesetting check; its source,
logs, metrics and image remain. Every earlier archived version is retained.

We viewed all five final contact sheets for40 rendered pages and14
critical final pages at full size, including every new B90--B92 proof
page, the repaired display and relevant bibliography entries. No clipping,
overlapping tags, missing glyphs or defective layout was found. All104
bibliography entries have explicit verification status. Exact page and
build records are in records/checkpoint17_typesetting.txt. Both main
full decisions remain Open. Computational convention audits are recorded
separately from this typesetting verification.
'''
p.write_text(s)
print('Final PDF QA recorded:40 pages,5 contact sheets,14 full-size pages; PASS.')
