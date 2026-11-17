"""Record completed human-visible PDF inspection; this script does not perform it."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parents[1]
m = json.loads((root / 'records/checkpoint13_metrics.json').read_text())
assert hashlib.sha256((root / 'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest() == m['pdf_sha256']
assert not m['overfull'] and not m['warnings'] and not m['errors']
manifest = json.loads((root / 'records/pdf_qa/checkpoint13_final/render_manifest.json').read_text())
pages = manifest['rendered_pages']
assert len(pages) == 43 and manifest['page_count'] == 309
enlarged = [1, 82, 111, 112, 113, 114, 217, 218, 219, 220, 221, 222]
assert set(enlarged) <= set(pages)
record = f'''# Thirteenth-hour final PDF typesetting and visual verification

Final PDF SHA-256: {m['pdf_sha256']}.
Final size: {m['pdf_bytes']} bytes; {m['pages']} pages.
Register: {m['statements']} statements; {m['statuses']}.
Bibliography records: {m['bibliography_entries']}; task rows: {m['task_rows']}.
Visual review: PASS.

The first complete build attempt stopped at the first B80 display:
the incoming fragment had eleven missing closing display delimiters.
The exact failed source, driver and complete pass log are preserved.
Root repaired precisely those eleven delimiters and reassembled the
paper without a mathematical change. The subsequent complete build
passes with zero overfull boxes, warnings, undefined references and
errors. No overfull box was reported before the first build stopped;
the successful final count is also zero, including boxes beyond 2pt.

We rendered 43 pages spread through the 309-page paper. All five
contact sheets were viewed. They include the title and contents, every
Part, all new A79/B79/B80 proof pages and adjacent pages, the A65 forward
correction, and the complete bibliography range 301-309. We also viewed
12 critical pages at full rendered size. No clipped text, crossing
equation tags, missing mathematical glyphs, or defective table placement
was observed. No visual repair or further PDF change was necessary.

Rendered pages:
{pages}

Full-size critical pages:
{enlarged}

Successful driver: records/checkpoint13_build2_driver.log.
Successful complete pass logs: records/build_passes/20261116T132722813749Z/.
Failed driver: records/checkpoint13_build1_driver.log.
Failed complete pass log: records/build_passes/20261116T132544523819Z/.
Failed-source and repair audit: records/checkpoint13_initial_build_failure.txt.
Metrics: records/checkpoint13_metrics.json and checkpoint13_final_metrics.out.
Renderings: records/pdf_qa/checkpoint13_final/.

Recorded at {datetime.now(timezone.utc).isoformat()}.
'''
(root / 'records/checkpoint13_typesetting.txt').write_text(record)
p = root / 'LM4_SUCCESSOR_report.md'
s = p.read_text()
marker = '### Thirteenth-hour final typesetting verification'
assert marker not in s
s += f'''\n{marker}

The final paper has {m['pages']} pages and {m['pdf_bytes']} bytes, SHA-256
{m['pdf_sha256']}. The first build stopped because eleven B80 displays
lacked their closing delimiters; the failed source and complete log are
retained. After repairing those delimiters, the complete build has zero
overfull boxes, warnings, undefined references and errors. Overfull
counts before/after are 0/0 (the first count is only through the failed
build's stopping point), including boxes beyond 2pt. We inspected all
five contact sheets for 43 rendered pages and 12 enlarged critical pages.
No clipping, overlapping tags, missing glyphs or misplaced tables was
found. See records/checkpoint13_typesetting.txt for the exact page list.
'''
p.write_text(s)
print('Final PDF QA recorded: 43 pages, five contact sheets, 12 enlarged pages; PASS.')
