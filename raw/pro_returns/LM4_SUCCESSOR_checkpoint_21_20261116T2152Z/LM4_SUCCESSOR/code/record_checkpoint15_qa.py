"""Record completed visible PDF inspection; this script does not perform it."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re

root=Path(__file__).resolve().parents[1]
m=json.loads((root/'records/checkpoint15_metrics.json').read_text())
assert hashlib.sha256((root/'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest()==m['pdf_sha256']
assert m['statements']==252 and m['pages']==332
assert not m['overfull'] and not m['warnings'] and not m['errors']
manifest=json.loads((root/'records/pdf_qa/checkpoint15_final/render_manifest.json').read_text())
pages=manifest['rendered_pages']
assert len(pages)==42 and manifest['page_count']==332
enlarged=[1,*range(122,130),*range(240,246),327,331,332]
assert len(enlarged)==18 and set(enlarged)<=set(pages)
bib=re.split(r'(?m)(?=^@)',(root/'LM4_SUCCESSOR_references.bib').read_text())[1:]
assert len(bib)==101 and all(re.search(r'\b(?:unverified|verified)\b',e,re.I) for e in bib)
initial=json.loads((root/'records/checkpoint15_initial_metrics.json').read_text())
previous=json.loads((root/'records/checkpoint15_before_orientation_clarification_metrics.json').read_text())
for earlier in (initial,previous):
    assert not earlier['overfull'] and not earlier['warnings'] and not earlier['errors']

record=f'''# Fifteenth-hour final PDF typesetting and visual verification

Final PDF SHA-256:{m['pdf_sha256']}.
Final size:{m['pdf_bytes']} bytes;{m['pages']} pages.
Register:{m['statements']} statements;{m['statuses']}.
Bibliography records:{m['bibliography_entries']};task rows:{m['task_rows']}.
Visual review: PASS.

The first integrated A82-A84/B82 build had329 pages and251 statements.
It compiled cleanly. B83 then produced a clean332-page,252-statement
build. The exact local-loop calculation resolved the retained b
orientation: a conventional positive q-loop represents b inverse.
The detecting character is now explicitly minus conventional winding.
That convention clarification produced the final third build without
altering the quotient arguments. The initial329-page PDF and the
pre-orientation-clarification332-page PDF remain separately preserved,
with their own metrics. No earlier version is called the final PDF.

All three complete builds have zero overfull boxes, warnings,
undefined references, and errors. Before/after overfull counts are0/0,
also for boxes exceeding2pt. No layout repair was needed in this cycle.
Every one of the101 bibliography records has an explicit verified or
unverified label. The new Haran and Webb entries are included in the
visible inspection.

We rendered42 final pages and visibly reviewed all five contact sheets.
We also displayed and inspected18 final pages at full size, comprising
the title/abstract, every new A82-A84 and B82-B83 proof page, and the
new bibliography entries and final page. All final full-size reviews
were performed on the final renderings directly; none relies on the
earlier four-image attempt whose output was truncated. There is no
clipped text, colliding equation tag, missing mathematical glyph, or
defective proof layout in the reviewed pages. The explicit orientation
paragraph and six-column conjugator table are legible. The final
bibliography page has substantial content and a clean ending.

Rendered final pages:
{pages}

Full-size critical final pages:
{enlarged}

Final driver:records/checkpoint15_build3_driver.log.
Final complete pass logs:records/build_passes/20261116T153347620877Z/.
Earlier successful drivers:records/checkpoint15_build1_driver.log,
records/checkpoint15_build2_driver.log.
Initial pass logs:records/build_passes/20261116T151057748004Z/.
Preserved initial PDF:records/checkpoint15_initial_paper.pdf.
Preserved pre-clarification PDF:
records/checkpoint15_before_orientation_clarification.pdf.
Metrics:records/checkpoint15_metrics.json and checkpoint15_final_metrics.out.
Renderings:records/pdf_qa/checkpoint15_final/.

Recorded at{datetime.now(timezone.utc).isoformat()}.
'''
(root/'records/checkpoint15_typesetting.txt').write_text(record)
p=root/'LM4_SUCCESSOR_report.md'
s=p.read_text()
marker='### Fifteenth-hour final typesetting verification'
assert marker not in s
s+=f'''\n{marker}

The final paper has{m['pages']} pages and{m['pdf_bytes']} bytes, SHA-256
{m['pdf_sha256']}. Its complete build has zero overfull boxes,
warnings, undefined references, and errors; before/after overfull
counts are0/0, also beyond2pt. The initial A82-A84/B82 integration,
the subsequent B83 integration, and the final explicit local-loop
orientation clarification all compiled cleanly. Their PDFs and
diagnostic records remain distinguishable. We viewed all five final
contact sheets for42 rendered pages and18 critical final pages at
full size, including every new proof page and both new bibliography
entries. No clipping, overlapping tags, missing glyphs, or defective
layout was found. All101 references have explicit verification status.
See records/checkpoint15_typesetting.txt for exact pages and build
records. Both main full decisions remain Open.
'''
p.write_text(s)
print('Final PDF QA recorded:42 pages,5 final contact sheets,18 full-size pages; PASS.')
