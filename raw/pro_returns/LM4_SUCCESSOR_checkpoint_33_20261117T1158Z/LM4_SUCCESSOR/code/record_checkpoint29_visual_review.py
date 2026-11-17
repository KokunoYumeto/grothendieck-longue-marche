"""Bind completed individual-page and separate contact-sheet inspections."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import hashlib
import json
import re
import shutil

root = Path(__file__).resolve().parents[1]
read = lambda rel: json.loads((root / rel).read_text())
sha = lambda rel: hashlib.sha256((root / rel).read_bytes()).hexdigest()
m = read('records/checkpoint29_metrics.json')
assert m['pages'] == 551 and m['statements'] == 314
assert sha('LM4_SUCCESSOR_paper.pdf') == m['pdf_sha256']
build = 'records/build_passes/20261117T051754498798Z/build_stabilize_0.log'
audits = []
for rel in ['LM4_SUCCESSOR_paper.log', build]:
    lines = (root / rel).read_text(errors='replace').splitlines()
    metadata = lambda x: 'infwarerr' in x or 'Providing info/warning/error messages' in x
    underfull = [x for x in lines if re.search('underfull', x, re.I)]
    warnings = [x for x in lines if re.search('warning', x, re.I) and not metadata(x)]
    issues = [x for x in lines if re.search(r'overfull|undefined|^!|error', x, re.I) and not metadata(x)]
    assert not warnings and not issues
    audits.append(dict(path=rel, sha256=sha(rel), warnings=warnings,
                       issues=issues, underfull_notices=underfull))
old = (root / 'records/pdf_qa/checkpoint29_before_integration/LM4_SUCCESSOR_paper.log').read_text()
old_underfull = [x for x in old.splitlines() if re.search('underfull', x, re.I)]
assert len(old_underfull) == 18
assert Counter(old_underfull) == Counter(audits[0]['underfull_notices'])
rendered = read('records/pdf_qa/checkpoint29_final/render_manifest.json')['rendered_pages']
required = [*range(136, 143), *range(446, 463)]
individual = [1, 2, 3, 4, 5, *required, 551]
assert len(rendered) == 39 and len(individual) == 30
for n in rendered:
    assert (root / f'records/pdf_qa/checkpoint29_final/page-{n:03d}.png').exists()
for n in range(1, 6):
    assert (root / f'records/pdf_qa/checkpoint29_final/contact-{n:02d}.png').exists()
assert len(re.findall(r'\\bibitem', (root / 'LM4_SUCCESSOR_paper.bbl').read_text())) == 114
record = dict(
    recorded_at=datetime.now(timezone.utc).isoformat(), pdf_sha256=m['pdf_sha256'],
    rendered_pages=rendered, required_math_pages=required,
    individually_inspected_pages=individual, contact_sheets_inspected=5,
    each_contact_sheet_opened_separately=True, truncated_outputs_counted=False,
    combined_build_attempts=1, combined_overfull_before=0, combined_overfull_after=0,
    maximum_overflow_before_pt=0, maximum_overflow_after_pt=0,
    printed_bibliography_entries=114, final_log_and_stdout_audits=audits,
    underfull_scope='The same18 notices occur in the preceding combined log, byte-identical by multiset. No new underfull notice. All24 new math pages were individually inspected.',
    final_log_and_stdout_case_insensitive='PASS', visual_review='PASS',
    visual_findings='Readable complete equations, matrices and tables; intact margins; no clipping, overlap or stray blank pages. All new mathematical pages136–142 and446–462 were individually viewed, as were opening pages1–5 and final bibliography page551. Each of five contact sheets was opened as its own image and inspected across the39 rendered pages. No private QA or truncated display substitutes for these final views.')
(root / 'records/checkpoint29_visual_review.json').write_text(json.dumps(record, indent=2) + '\n')
(root / 'records/checkpoint29_typesetting.txt').write_text(f'''Visual review: PASS
PDF:551 pages;{m['pdf_bytes']} bytes.
SHA-256:{m['pdf_sha256']}
One combined build using records/checkpoint25_tex_env.json; genuine passes retained.
Initial/final combined overfull counts:0/0; maximum overflow:0/0pt.
The actual final log and stabilized engine stdout were scanned case-insensitively:
no overfull boxes, actual warnings, undefined references or errors.
The18 existing underfull notices are unchanged by exact multiset comparison.
All24 new mathematical pages136–142 and446–462 were individually viewed.
Opening pages1–5 and final bibliography page551 give30 total individual views.
Five contact sheets were each inspected as a separate image, covering39 pages.
All114 bibliography entries are printed;314 statements and49 task/lead rows.
All initial sources, private layout attempts and precision edits remain retained.
''')
for suffix in ('aux', 'bbl', 'blg'):
    source = root / f'LM4_SUCCESSOR_paper.{suffix}'
    if source.exists():
        shutil.copy2(source, root / f'records/checkpoint29_final_paper_{suffix}.retained.txt')
pdfs = {
    'LM4_SUCCESSOR_paper.pdf',
    'records/pdf_qa/checkpoint29_before_integration/LM4_SUCCESSOR_paper.pdf',
    'work_DE/B138_review.pdf', 'work_DE/B141_review.pdf',
}
for f in (root / 'work_A').rglob('*.pdf'):
    if any(part.startswith(('A87', 'A88')) for part in f.relative_to(root / 'work_A').parts):
        pdfs.add(str(f.relative_to(root)))
for component in ('B139', 'B140'):
    pdfs.update(str(f.relative_to(root)) for f in (root / ('work_CE/qa_' + component)).rglob('*.pdf'))
for rel in sorted(pdfs):
    assert (root / rel).is_file()
    if rel.startswith('work_DE/'):
        assert (root / rel).with_suffix('.tex').exists()
(root / 'records/checkpoint29_authored_pdf_retention.json').write_text(json.dumps({
    'recorded_at': datetime.now(timezone.utc).isoformat(),
    'status': 'PASS_ALL_LISTED_AUTHORED_PDF_PATHS_INCLUDED',
    'files': [dict(path=rel, bytes=(root / rel).stat().st_size, sha256=sha(rel),
                   destination='direct ZIP entry' if rel == 'LM4_SUCCESSOR_paper.pdf' else 'standard historical_documents.tar with original path and bytes') for rel in sorted(pdfs)],
    'scope': 'Current and previous complete combined PDFs, all A87/A88 private PDF paths and precursors, all B139/B140 private PDF paths, and both DE private PDFs. Every earlier archived version is retained separately; no earlier archive is changed.'
}, indent=2) + '\n')
print('PASS final551-page PDF;24new math and30total individual-page inspections;5contact sheets;114printed references.')
