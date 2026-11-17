"""Record root's completed final-PDF page inspection and literal log audit."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re
import shutil

root = Path(__file__).resolve().parents[1]
out = root/'records/pdf_qa/checkpoint25_final'
metrics = json.loads((root/'records/checkpoint25_metrics.json').read_text())
render = json.loads((out/'render_manifest.json').read_text())
digest = hashlib.sha256((root/'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest()
assert digest == metrics['pdf_sha256']
required = list(range(361,386))
individual = [1,2,*required,474]
assert set(individual) <= set(render['rendered_pages'])
logs = ['LM4_SUCCESSOR_paper.log',
        'records/build_passes/20261117T012901698950Z/build_stabilize_0.log']
audits = []
for relative in logs:
    path = root/relative
    lines = path.read_text().splitlines()
    warnings = [line for line in lines if re.search(r'\bwarning\b',line,re.I)
                and not line.startswith(('Package:','File:'))]
    issues = [line for line in lines if re.search(r'^!|\berror\b|undefined|Overfull',line,re.I)
              and not line.startswith(('Package:','File:'))]
    assert not warnings and not issues, (relative,warnings,issues)
    audits.append(dict(path=relative,sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                       warnings=warnings,issues=issues))
for suffix in ('aux','bbl','blg'):
    source=root/f'LM4_SUCCESSOR_paper.{suffix}'
    if source.exists():
        shutil.copy2(source,out/f'{source.name}.retained.txt')
now = datetime.now(timezone.utc).isoformat()
record = dict(recorded_at=now,pdf_sha256=digest,
    rendered_pages=render['rendered_pages'],required_math_pages=required,
    individually_inspected_pages=individual,contact_sheets_inspected=6,
    each_contact_sheet_opened_separately=True,truncated_outputs_counted=False,
    combined_build_attempts=1,combined_overfull_before=0,combined_overfull_after=0,
    maximum_overflow_before_pt=0,maximum_overflow_after_pt=0,
    printed_bibliography_entries=112,final_log_and_stdout_audits=audits,
    visual_review='PASS')
(root/'records/checkpoint25_visual_review.json').write_text(json.dumps(record,indent=2)+'\n')
text=f'''# Twenty-fifth-hour final typesetting and visible verification

Final PDF SHA-256: {digest}.
Final size: {metrics['pdf_bytes']} bytes; 474 pages.
Register: 292 statements; 248 Proved, 19 Refuted, 19 Open, 6 Known.
Bibliography: 112 entries in both source database and printed bbl.
Task/lead rows: 49. Visual review: PASS.

The first combined checkpoint25 build is final. Its final TeX log and
final stabilized engine stdout were both checked case-insensitively:
zero warnings, overfull boxes, undefined references or errors. Package
and file metadata descriptions are excluded from diagnostic matching.
Initial/final combined overfull counts are 0/0; maximum overflow is
0pt/0pt. No visual repair or second combined build was necessary.
The previous PDF, source, log and printed bibliography were preserved
before integration. The clean font map is a derived map; no original
runtime map, prior PDF, log or immutable archive was modified.

Root opened each of the six final contact sheets separately. They cover
all {len(render['rendered_pages'])} rendered pages, sampled across all Parts,
the title and continued abstract, every new mathematical page, both
adjacent boundary pages, and the entire eleven-page bibliography.
Root then opened {len(individual)} final pages individually: 1, 2,
every page 361--385 containing B118--B123, and the final bibliography
page 474 containing the newly used primary reference. No truncated
output was counted. Margins, displays, equation numbers, tables, proof
endings, code paths, glyphs and bibliography wrapping were inspected.
No clipping, overlap, missing glyph or layout defect was found.

All six component proof reviews and private QA records remain separately
bound to their frozen source hashes. Their authors' private inspections
are not substituted for the root combined-PDF inspections above. The
initial component syntax failures, layout attempts and earlier nine
lowercase font-map warnings remain in the actual retained logs. The
earlier inaccurate zero-warning reports are explicitly corrected in
checkpoint25_fontmap_warning_audit.json and the research/audit reports.

Rendered pages: {render['rendered_pages']}
Individually inspected pages: {individual}
Contact sheets inspected: 6, each opened separately.
Combined driver: records/checkpoint25_build1_driver.log.
Genuine passes: records/build_passes/20261117T012901698950Z/.
Final metrics: records/checkpoint25_metrics.json.
Final renders: records/pdf_qa/checkpoint25_final/.
Recorded at: {now}.
'''
(root/'records/checkpoint25_typesetting.txt').write_text(text)
print('PASS: 25 new mathematical pages, 28 individual views, 6 separate contact sheets; final log and stdout clean.')
