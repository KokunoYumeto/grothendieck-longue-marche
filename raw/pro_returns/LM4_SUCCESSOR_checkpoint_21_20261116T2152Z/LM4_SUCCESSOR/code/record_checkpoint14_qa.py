"""Record completed visible PDF inspection; this script does not perform it."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re

root=Path(__file__).resolve().parents[1]
m=json.loads((root/'records/checkpoint14_metrics.json').read_text())
assert hashlib.sha256((root/'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest()==m['pdf_sha256']
assert not m['overfull'] and not m['warnings'] and not m['errors']
manifest=json.loads((root/'records/pdf_qa/checkpoint14_final/render_manifest.json').read_text())
pages=manifest['rendered_pages']
assert len(pages)==42 and manifest['page_count']==320
enlarged=[1,114,115,116,117,118,119,120,121,122,230,231,232,233,317,320]
assert set(enlarged)<=set(pages)
comparison=json.loads((root/'records/pdf_qa/checkpoint14_final/unchanged_rendering_comparison.json').read_text())
assert comparison['byte_identical'] and len(comparison['unchanged_pre_bibliography_renderings'])==33
assert set(enlarged[:-2])<=set(comparison['unchanged_pre_bibliography_renderings'])
bib=re.split(r'(?m)(?=^@)',(root/'LM4_SUCCESSOR_references.bib').read_text())[1:]
assert len(bib)==99 and all('verified' in e.lower() for e in bib)

record=f'''# Fourteenth-hour final PDF typesetting and visual verification

Final PDF SHA-256:{m['pdf_sha256']}.
Final size:{m['pdf_bytes']} bytes;{m['pages']} pages.
Register:{m['statements']} statements;{m['statuses']}.
Bibliography records:{m['bibliography_entries']};task rows:{m['task_rows']}.
Visual review: PASS.

The complete mathematical integration compiled at its first attempt.
The first two builds had321 pages. A source-status audit found two
older bibliography notes without their literal verified label; the
existing direct-reading records justified adding those labels. No
mathematical claim or source scope changed. The complete logs of all
three builds are preserved, with final overflow, warning,
undefined-reference and error counts all zero. Before/after overfull
counts are0/0, including boxes beyond2pt.

The first rendered review inspected all five contact sheets for43
pages and all new A80/A81/B81 proof pages at full size. It found no
clipped text, colliding equation tags, missing mathematical glyphs,
or defective proof layout. It did identify an almost empty final
bibliography page with only the continuation of the last reference.
Setting bibliography entry spacing to3pt removed that page without
changing type size or any proof layout. The pre-adjustment321-page
PDF, metrics and renderings are preserved. All311 pages preceding
the bibliography have identical extracted text after the adjustment.
All33 rendered proof/sample pages preceding the bibliography are
byte-identical PNGs, as checked in the retained comparison record.

We rendered42 pages from the final320-page PDF and viewed all five
final contact sheets. The16 full-size critical pages comprise14
already viewed, byte-identical title/proof images and two newly
viewed final bibliography pages. The new Milne entries and the
complete final reference have clear, legible placement. Every new
proof page and the complete bibliography range312-320 are covered.
No further repair is required.

Rendered final pages:
{pages}

Full-size critical final pages:
{enlarged}

Final driver:records/checkpoint14_build3_driver.log.
Final complete pass logs:records/build_passes/20261116T142418629462Z/.
Earlier successful drivers:records/checkpoint14_build1_driver.log,
records/checkpoint14_build2_driver.log.
Earlier pass logs:records/build_passes/20261116T141843896588Z/,
records/build_passes/20261116T142100440186Z/.
Pre-adjustment PDF:records/checkpoint14_before_bib_spacing.pdf.
Metrics:records/checkpoint14_metrics.json and checkpoint14_final_metrics.out.
Renderings:records/pdf_qa/checkpoint14_final/.

Recorded at{datetime.now(timezone.utc).isoformat()}.
'''
(root/'records/checkpoint14_typesetting.txt').write_text(record)
p=root/'LM4_SUCCESSOR_report.md'
s=p.read_text()
marker='### Fourteenth-hour final typesetting verification'
assert marker not in s
s+=f'''\n{marker}

The final paper has{m['pages']} pages and{m['pdf_bytes']} bytes, SHA-256
{m['pdf_sha256']}. Its complete build has zero overfull boxes,
warnings, undefined references, and errors; before/after overfull
counts are0/0, also beyond2pt. Two older bibliography entries received
their missing literal verification labels from the retained reading
records. A bibliography-only spacing adjustment removed a two-line
last page, leaving the proof text and reviewed proof images unchanged.
The pre-adjustment PDF and renderings remain. We viewed all five
final contact sheets for42 rendered pages and16 critical pages at
full size, including byte-identical proof renderings inspected before
the bibliography adjustment. No clipping, overlapping tags, missing
glyphs, or defective layout remains. See
records/checkpoint14_typesetting.txt for exact pages and build records.
'''
p.write_text(s)
print('Final PDF QA recorded:42 pages,5 final contact sheets,16 critical pages; PASS.')
