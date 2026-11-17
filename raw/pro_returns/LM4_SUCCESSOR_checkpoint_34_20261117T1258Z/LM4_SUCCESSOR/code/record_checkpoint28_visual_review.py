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
m = read('records/checkpoint28_metrics.json')
assert m['pages'] == 530 and m['statements'] == 308
assert sha('LM4_SUCCESSOR_paper.pdf') == m['pdf_sha256']
build = 'records/build_passes/20261117T042017839089Z/build_stabilize_0.log'
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
old = (root / 'records/pdf_qa/checkpoint28_before_integration/LM4_SUCCESSOR_paper.log').read_text()
old_underfull = [x for x in old.splitlines() if re.search('underfull', x, re.I)]
assert len(old_underfull) == 18
assert Counter(old_underfull) == Counter(audits[0]['underfull_notices'])
rendered = read('records/pdf_qa/checkpoint28_final/render_manifest.json')['rendered_pages']
required = [*range(130, 137), *range(427, 441)]
individual = [1, 2, 3, 4, *required, 530]
assert len(rendered) == 35 and len(individual) == 26
for n in rendered:
    assert (root / f'records/pdf_qa/checkpoint28_final/page-{n:03d}.png').exists()
for n in range(1, 5):
    assert (root / f'records/pdf_qa/checkpoint28_final/contact-{n:02d}.png').exists()
assert len(re.findall(r'\\bibitem', (root / 'LM4_SUCCESSOR_paper.bbl').read_text())) == 113
record = dict(
    recorded_at=datetime.now(timezone.utc).isoformat(), pdf_sha256=m['pdf_sha256'],
    rendered_pages=rendered, required_math_pages=required,
    individually_inspected_pages=individual, contact_sheets_inspected=4,
    each_contact_sheet_opened_separately=True, truncated_outputs_counted=False,
    combined_build_attempts=1, combined_overfull_before=0, combined_overfull_after=0,
    maximum_overflow_before_pt=0, maximum_overflow_after_pt=0,
    printed_bibliography_entries=113, final_log_and_stdout_audits=audits,
    underfull_scope='The same18 notices occur in the preceding combined log, byte-identical by multiset. No new underfull notice. All21 new math pages were individually inspected.',
    final_log_and_stdout_case_insensitive='PASS', visual_review='PASS',
    visual_findings='Readable complete equations, matrices and tables; intact margins; no clipping, overlap or stray blank pages. All new mathematical pages130–136 and427–440 were individually viewed, as were opening pages1–4 and final bibliography page530. Each of four contact sheets was opened as its own image and inspected across the35 rendered pages. No private QA or truncated display substitutes for these final views.')
(root / 'records/checkpoint28_visual_review.json').write_text(json.dumps(record, indent=2) + '\n')
(root / 'records/checkpoint28_typesetting.txt').write_text(f'''Visual review: PASS
PDF:530 pages;{m['pdf_bytes']} bytes.
SHA-256:{m['pdf_sha256']}
One combined build using records/checkpoint25_tex_env.json; genuine passes retained.
Initial/final combined overfull counts:0/0; maximum overflow:0/0pt.
The actual final log and stabilized engine stdout were scanned case-insensitively:
no overfull boxes, actual warnings, undefined references or errors.
The18 existing underfull notices are unchanged by exact multiset comparison.
All21 new mathematical pages130–136 and427–440 were individually viewed.
Opening pages1–4 and final bibliography page530 give26 total individual views.
Four contact sheets were each inspected as a separate image, covering35 pages.
All113 bibliography entries are printed;308 statements and49 task/lead rows.
All initial sources, private layout attempts and precision edits remain retained.
''')
for suffix in ('aux', 'bbl', 'blg'):
    source = root / f'LM4_SUCCESSOR_paper.{suffix}'
    if source.exists():
        shutil.copy2(source, root / f'records/checkpoint28_final_paper_{suffix}.retained.txt')
pdfs = {
    'LM4_SUCCESSOR_paper.pdf',
    'records/pdf_qa/checkpoint28_before_integration/LM4_SUCCESSOR_paper.pdf',
    'work_DE/B136_review.pdf', 'work_DE/B137_review.pdf',
}
for f in (root / 'work_A').rglob('*.pdf'):
    if any(part.startswith(('A85', 'A86')) for part in f.relative_to(root / 'work_A').parts):
        pdfs.add(str(f.relative_to(root)))
pdfs.update(str(f.relative_to(root)) for f in (root / 'work_CE/qa_B135').rglob('*.pdf'))
for rel in sorted(pdfs):
    assert (root / rel).is_file()
    if rel.startswith('work_DE/'):
        assert (root / rel).with_suffix('.tex').exists()
(root / 'records/checkpoint28_authored_pdf_retention.json').write_text(json.dumps({
    'recorded_at': datetime.now(timezone.utc).isoformat(),
    'status': 'PASS_ALL_LISTED_AUTHORED_PDF_PATHS_INCLUDED',
    'files': [dict(path=rel, bytes=(root / rel).stat().st_size, sha256=sha(rel),
                   destination='direct ZIP entry' if rel == 'LM4_SUCCESSOR_paper.pdf' else 'standard historical_documents.tar with original path and bytes') for rel in sorted(pdfs)],
    'scope': 'Current and previous complete combined PDFs, all A85/A86 private PDF paths and precursors, all B135 private PDF paths, and both DE private PDFs. Every earlier archived version is retained separately; no earlier archive is changed.'
}, indent=2) + '\n')
print('PASS final530-page PDF;21new math and26total individual-page inspections;4contact sheets;113printed references.')
