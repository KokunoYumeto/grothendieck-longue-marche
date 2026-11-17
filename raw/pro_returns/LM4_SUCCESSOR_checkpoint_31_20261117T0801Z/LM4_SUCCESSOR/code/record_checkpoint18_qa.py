"""Record the completed visible inspection; this script does not perform it."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
m = json.loads((root/'records/checkpoint18_metrics.json').read_text())
assert hashlib.sha256((root/'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest() == m['pdf_sha256']
assert m['statements'] == 265 and m['pages'] == 374
assert m['statuses'] == {'Known':6, 'Proved':223, 'Refuted':17, 'Open':19}
assert not m['overfull'] and not m['warnings'] and not m['errors']
manifest = json.loads((root/'records/pdf_qa/checkpoint18_final/render_manifest.json').read_text())
pages = manifest['rendered_pages']
assert len(pages) == 54 and manifest['page_count'] == 374
enlarged = [1, 2, *range(270, 288), 371, 374]
assert len(enlarged) == 22 and set(enlarged) <= set(pages)
bib = re.split(r'(?m)(?=^@)', (root/'LM4_SUCCESSOR_references.bib').read_text())[1:]
assert len(bib) == 105 and all(re.search(r'\b(?:unverified|verified)\b', e, re.I) for e in bib)
assert 'Magnus1935' in (root/'sections/b_sources.bib').read_text()

record = f'''# Eighteenth-hour final PDF typesetting and visual verification

Final PDF SHA-256: {m['pdf_sha256']}.
Final size: {m['pdf_bytes']} bytes; {m['pages']} pages.
Register: {m['statements']} statements; {m['statuses']}.
Bibliography records: {m['bibliography_entries']}; task rows: {m['task_rows']}.
Visual review: PASS.

The first combined B93--B96 build completed successfully. Its final log
contains zero overfull boxes, warnings, undefined references or errors.
The before/after overfull counts for the combined build are0/0, including
boxes beyond2pt; maximum0pt. No combined-paper layout repair was needed.
All bibliography entries retain explicit verified/unverified status.

We rendered54 pages and displayed all six contact sheets, one image per
call. This sample covers the title, contents, all Parts, every new proof
page and the complete bibliography. We also displayed and inspected22
critical pages individually at full size: title/abstract, contents, every
B93--B96 proof page270--286, the transition to Part C on287, the Magnus
bibliography page371 and the final bibliography page374. The coefficient
tables, full source words, norm/defect formulas, long exact sequences,
source paths and equation tags are legible. No clipping, overlap,
missing mathematical glyphs or defective proof layout was found.

The new components have separate full-page visual reviews. Their genuine
earlier failures are retained: B93 first missed the restored runtime
format and then repaired an underfull source-path paragraph; B94's final
component resolved its contextual Magnus citation; B95 split a display
that initially overflowed4.137pt; B96 retained its unavailable pdflatex
format and pre-linebreak-fix attempt. These component records are not
misrepresented as failures of the clean combined build. Existing private
runtime font-map warnings, where present, are disclosed in component QA.

Rendered final pages:
{pages}

Full-size critical final pages:
{enlarged}

Combined driver: records/checkpoint18_build1_driver.log.
Complete genuine pass logs: records/build_passes/20261116T182824642814Z/.
Final metrics: records/checkpoint18_metrics.json and checkpoint18_final_metrics.out.
Render output: records/checkpoint18_render.out.
Final renderings: records/pdf_qa/checkpoint18_final/.
Component QA: work_A/B93_component_QA.txt, work_A/B94_component_QA.txt,
work_DE/B95_QA.txt, work_CE/qa_B96/QA.txt.

Recorded at {datetime.now(timezone.utc).isoformat()}.
'''
(root/'records/checkpoint18_typesetting.txt').write_text(record)
(root/'records/checkpoint18_visual_review.json').write_text(json.dumps({
    'pdf_sha256':m['pdf_sha256'], 'rendered_pages':pages,
    'contact_sheets_inspected':6, 'individually_inspected_pages':enlarged,
    'combined_overfull_before':0, 'combined_overfull_after':0,
    'visual_review':'PASS', 'recorded_at':datetime.now(timezone.utc).isoformat()}, indent=2)+'\n')
p = root/'LM4_SUCCESSOR_report.md'
s = p.read_text()
marker = '### Eighteenth-hour final typesetting verification'
assert marker not in s
s += f'''\n{marker}

The final paper has{m['pages']} pages and{m['pdf_bytes']} bytes, SHA-256
{m['pdf_sha256']}. The first combined B93--B96 build is clean: zero
overfull boxes, warnings, undefined references and errors. Before/after
combined overfull counts are0/0, including beyond2pt. All105 bibliography
records have explicit verification status.

We viewed all six contact sheets for54 rendered pages and22 critical
pages individually, including every new proof page, the Part C transition,
the new Magnus reference and the final bibliography page. No clipping,
overlapping tags, missing glyphs or defective layout was found. Component
format and layout attempts remain retained separately; B95's4.137pt
component overflow was repaired before integration. The combined build
needed no layout repair. Exact page lists and logs are recorded in
records/checkpoint18_typesetting.txt. Every earlier archived version is
retained. Both main full decisions remain Open.
'''
p.write_text(s)
print('Final PDF QA recorded:54 pages,6 contact sheets,22 full-size pages; PASS.')
