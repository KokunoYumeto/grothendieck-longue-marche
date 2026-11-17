"""Record actual completed visible inspection; this script does not inspect images."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
m = json.loads((root/'records/checkpoint24_metrics.json').read_text())
assert m['statements'] == 286 and m['pages'] == 450
assert m['statuses'] == {'Known': 6, 'Proved': 242, 'Refuted': 19, 'Open': 19}
assert m['bibliography_entries'] == 111 and m['task_rows'] == 49
assert not m['overfull'] and not m['warnings'] and not m['errors']
assert hashlib.sha256((root/'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest() == m['pdf_sha256']
assert len(re.findall(r'\\bibitem', (root/'LM4_SUCCESSOR_paper.bbl').read_text())) == 111
directory = root/'records/pdf_qa/checkpoint24_final'
manifest = json.loads((directory/'render_manifest.json').read_text())
pages = manifest['rendered_pages']
individual = [1, 2] + list(range(352, 362)) + [448, 449, 450]
assert manifest['page_count'] == m['pages']
assert set(individual) <= set(pages)
assert len(pages) == 39 and len(list(directory.glob('contact-*.png'))) == 5
now = datetime.now(timezone.utc).isoformat()
record = f'''# Twenty-fourth-hour final typesetting and visible verification

Final PDF SHA-256: {m['pdf_sha256']}.
Final size: {m['pdf_bytes']} bytes; {m['pages']} pages.
Register: 286 statements; 242 Proved, 19 Refuted, 19 Open, 6 Known.
Bibliography: 111 entries in both source database and printed bbl.
Task/lead rows: 49. Visual review: PASS.

The first combined checkpoint24 build is final. It compiles cleanly in
450 pages, with zero overfull boxes, warnings, undefined references or
errors. Initial/final combined overfull counts are 0/0, including boxes
exceeding 2pt; maximum initial/final overflow is 0pt/0pt. No visual repair
or additional combined build was necessary. The earlier checkpoint23
PDF, source, log and printed bibliography were preserved before integration.

The first attempted tool output containing several contact sheets was
truncated. It was not counted as an inspection. We subsequently opened
each of the five final contact sheets individually, covering all 39
rendered pages across every Part and the bibliography. We then opened
15 final pages individually: title, continued abstract and contents,
every mathematical page 352--361 containing B115--B117, and bibliography
pages 448--450. We inspected margins, displays, equation numbers, tables,
proof endings, record paths, glyphs and bibliography wrapping. No clipping,
overlap, missing glyph or layout defect was found. Boundary pages 351 and
362 were included in the final contact-sheet inspection.

B115's private component retains its genuine initial missing-format
failure and its subsequent clean LuaLaTeX builds. B117's private component
also retains its clean builds and component renders. Those component
inspections were performed by their authors and are not counted as root's
final combined inspection. All genuine component and combined build logs
are retained. This record concerns only the final PDF with the hash above.

Rendered pages: {pages}
Individually inspected final pages: {individual}
Contact sheets inspected: 5, each opened separately from the final PDF.
Combined driver: records/checkpoint24_build1_driver.log.
Complete genuine TeX/BibTeX passes: records/build_passes/.
Final metrics: records/checkpoint24_metrics.json.
Final renders: records/pdf_qa/checkpoint24_final/.
Recorded at: {now}.
'''
(root/'records/checkpoint24_typesetting.txt').write_text(record)
(root/'records/checkpoint24_visual_review.json').write_text(json.dumps({
    'recorded_at': now, 'pdf_sha256': m['pdf_sha256'],
    'rendered_pages': pages, 'individually_inspected_pages': individual,
    'contact_sheets_inspected': 5, 'combined_overfull_before': 0,
    'combined_overfull_after': 0, 'maximum_overflow_before_pt': 0,
    'maximum_overflow_after_pt': 0, 'combined_build_attempts': 1,
    'truncated_multisheet_output_counted': False,
    'printed_bibliography_entries': 111, 'visual_review': 'PASS'
}, indent=2)+'\n')
p = root/'LM4_SUCCESSOR_report.md'
s = p.read_text()
marker = '### Twenty-fourth-hour final typesetting verification'
assert marker not in s
s += f'''\n{marker}

The final paper has 450 pages, 286 statements and 111 printed bibliography
entries. Its SHA-256 is {m['pdf_sha256']}; size {m['pdf_bytes']} bytes.
The first combined build is clean. Initial/final overfull counts are 0/0,
including boxes exceeding 2pt, with zero warnings, undefined references
or errors. Five final contact sheets cover 39 pages across all Parts.
We inspected 15 final pages individually, including every new mathematical
page 352--361. No clipping, overlap, missing glyph or layout defect was
found. A truncated multi-image output was not counted; every contact sheet
was reopened separately. Full record: records/checkpoint24_typesetting.txt
and records/checkpoint24_visual_review.json. Both main decisions remain Open.
'''
p.write_text(s)
print('PASS final visible QA: 450 pages; 39 sampled; 15 individual; 5 sheets; 111 printed references.')
