"""Record completed visible inspection; this script does not perform it."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
m = json.loads((root/'records/checkpoint19_metrics.json').read_text())
assert hashlib.sha256((root/'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest() == m['pdf_sha256']
assert m['statements'] == 269 and m['pages'] == 386
assert m['statuses'] == {'Known':6, 'Proved':225, 'Refuted':19, 'Open':19}
assert not m['overfull'] and not m['warnings'] and not m['errors']
manifest = json.loads((root/'records/pdf_qa/checkpoint19_final/render_manifest.json').read_text())
pages = manifest['rendered_pages']
assert len(pages) == 49 and manifest['page_count'] == 386
enlarged = [1, 2, *range(287, 299), 381, 382, 383, 386]
assert len(enlarged) == 18 and set(enlarged) <= set(pages)
bib = re.split(r'(?m)(?=^@)', (root/'LM4_SUCCESSOR_references.bib').read_text())[1:]
assert len(bib) == 108 and all(re.search(r'\b(?:unverified|verified)\b', e, re.I) for e in bib)
now = datetime.now(timezone.utc).isoformat()
record = f'''# Nineteenth-hour final PDF typesetting and visual verification

Final PDF SHA-256: {m['pdf_sha256']}.
Final size: {m['pdf_bytes']} bytes; {m['pages']} pages.
Register: {m['statements']} statements; {m['statuses']}.
Bibliography records: {m['bibliography_entries']}; task rows: {m['task_rows']}.
Visual review: PASS.

Both combined B97--B100 builds completed successfully. The second adds
the proved mod-two universal-cover homology conclusion and its primary
Hatcher reference. It is not a layout-repair build. Both final logs have
zero overfull boxes, warnings, undefined references and errors. Combined
before/after overfull counts are 0/0, including boxes beyond 2pt; maximum
0pt. All 108 bibliography records retain explicit verification status.

We rendered 49 pages spread across every Part and the bibliography and
displayed and inspected all six contact sheets. We also displayed and
inspected the 18 critical pages listed below individually at full size:
the title/abstract and contents, all new proof pages 287--298, the new
Hatcher, Kim--Rolfsen and Milnor references, and the final bibliography
page. In a first attempted combined image call pages 294--296 were
truncated by the context limit; these pages were subsequently displayed
one at a time and inspected. We do not count the truncated attempt as
visual inspection. All row/parity tables, literal word arrays, factored
coefficient displays, exact sequences, diagrams and equation tags fit
and remain legible. No clipping, overlap, missing mathematical glyphs
or defective proof layout was found.

B99 also has its separate four-page component review and complete pass
logs under work_CE/qa_B99/. Its genuine earlier component format/compile
attempts are retained. The earlier failed coarse path-margin assertion,
the interrupted giant full-chain expansion and their outputs remain
research records; neither is described as a successful computation.

Rendered final pages:
{pages}

Full-size critical final pages:
{enlarged}

Combined drivers: records/checkpoint19_build1_driver.log and
records/checkpoint19_build2_driver.log.
Complete genuine pass logs: records/build_passes/20261116T192451709561Z/
and records/build_passes/20261116T192708960505Z/.
First PDF and metrics: records/pdf_qa/checkpoint19_build1/ and
records/checkpoint19_build1_metrics.json.
Final metrics: records/checkpoint19_metrics.json and checkpoint19_final_metrics.out.
Render output: records/checkpoint19_render.out.
Final renderings: records/pdf_qa/checkpoint19_final/.

Recorded at {now}.
'''
(root/'records/checkpoint19_typesetting.txt').write_text(record)
(root/'records/checkpoint19_visual_review.json').write_text(json.dumps({
    'pdf_sha256':m['pdf_sha256'], 'rendered_pages':pages,
    'contact_sheets_inspected':6, 'individually_inspected_pages':enlarged,
    'combined_overfull_before':0, 'combined_overfull_after':0,
    'visual_review':'PASS', 'recorded_at':now}, indent=2)+'\n')
p = root/'LM4_SUCCESSOR_report.md'
s = p.read_text()
marker = '### Nineteenth-hour final typesetting verification'
assert marker not in s
s += f'''\n{marker}

The final paper has {m['pages']} pages and {m['pdf_bytes']} bytes, SHA-256
{m['pdf_sha256']}. Both combined B97--B100 builds are clean: zero
overfull boxes, warnings, undefined references and errors. The second
adds the proved mod-two homology statement and Hatcher dependency.
Before/after combined overfull counts are 0/0, including beyond 2pt.
All 108 bibliography records have explicit verification status.

We inspected six contact sheets for 49 rendered pages and 18 critical
pages individually, including every new proof page and all three new
references. No clipping, overlapping tags, missing glyphs or defective
layout was found. Genuine component attempts remain retained. The
combined build needed no layout repair. Exact page lists and logs are
recorded in records/checkpoint19_typesetting.txt. Both main full
decisions remain Open.
'''
p.write_text(s)
print('Final PDF QA recorded: 49 pages, 6 contact sheets, 18 full-size pages; PASS.')
