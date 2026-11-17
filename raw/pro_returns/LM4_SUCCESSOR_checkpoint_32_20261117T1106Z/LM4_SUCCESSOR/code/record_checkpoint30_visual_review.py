"""Bind actual completed final-page inspections to the exact combined PDF."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import hashlib, json, re, shutil

root = Path(__file__).resolve().parents[1]
read = lambda rel: json.loads((root / rel).read_text())
sha = lambda rel: hashlib.sha256((root / rel).read_bytes()).hexdigest()
m = read('records/checkpoint30_metrics.json')
assert m['pages'] == 573 and m['statements'] == 323
assert sha('LM4_SUCCESSOR_paper.pdf') == m['pdf_sha256']
build = 'records/build_passes/20261117T062009459413Z/build_stabilize_0.log'
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
old = (root / 'records/pdf_qa/checkpoint30_before_integration/LM4_SUCCESSOR_paper.log').read_text()
old_underfull = [x for x in old.splitlines() if re.search('underfull', x, re.I)]
assert len(old_underfull) == 18
new_notice = r'Underfull \hbox (badness 10000) in paragraph at lines 222--227'
assert Counter(audits[0]['underfull_notices']) == Counter(old_underfull) + Counter([new_notice])
assert len(audits[0]['underfull_notices']) == 19
assert Counter(audits[1]['underfull_notices']) == Counter(audits[0]['underfull_notices'])
manifest_path = 'records/pdf_qa/checkpoint30_final/render_manifest.json'
render = read(manifest_path)
required = [*range(143, 148), *range(467, 484)]
individual = sorted(set([*range(1, 7), *range(142, 149), *range(466, 485), 573]))
assert render['rendered_pages'] == individual and len(individual) == 33 and len(required) == 22
for n in individual:
    assert (root / f'records/pdf_qa/checkpoint30_final/page-{n:03d}.png').exists()
for n in range(1, 5):
    assert (root / f'records/pdf_qa/checkpoint30_final/contact-{n:02d}.png').exists()
assert len(re.findall(r'\\bibitem', (root / 'LM4_SUCCESSOR_paper.bbl').read_text())) == 114
bibliography_unchanged = ((root / 'LM4_SUCCESSOR_paper.bbl').read_bytes() ==
    (root / 'records/pdf_qa/checkpoint30_before_integration/LM4_SUCCESSOR_paper.bbl.retained.txt').read_bytes())
assert bibliography_unchanged
# Inspection identifies the final page as verification-note continuation,
# not the last bibliography page. Preserve and correct only that description.
for rel in ['code/render_checkpoint30_pdf.py', manifest_path]:
    f = root / rel
    prior = f.read_text()
    if 'final bibliography page' in prior:
        saved = root / 'records/checkpoint30_before_render_scope_correction' / rel
        saved.parent.mkdir(parents=True, exist_ok=True)
        assert not saved.exists()
        shutil.copy2(f, saved)
        f.write_text(prior.replace('final bibliography page', 'final document page'))
record = dict(
    recorded_at=datetime.now(timezone.utc).isoformat(), pdf_sha256=m['pdf_sha256'],
    rendered_pages=individual, required_math_pages=required,
    individually_inspected_pages=individual, contact_sheets_inspected=4,
    each_contact_sheet_opened_separately=True, truncated_outputs_counted=False,
    combined_build_attempts=1, combined_overfull_before=0, combined_overfull_after=0,
    maximum_overflow_before_pt=0, maximum_overflow_after_pt=0,
    printed_bibliography_entries=114, bibliography_bbl_byte_identical_to_checkpoint29=True,
    final_log_and_stdout_audits=audits,
    underfull_scope='All18 previous notices remain byte-identical by multiset. One additional notice occurs only in the B147 evidence-path paragraph on page483. That actual final page was individually inspected: the complete filename and following text are readable within the margins; no clipping or overlap. Total19 notices; none is hidden or recategorized as absent.',
    final_log_and_stdout_case_insensitive='PASS', visual_review='PASS',
    visual_findings='All22 new mathematical pages143–147 and467–483 were opened as individual images and inspected. Front pages1–6, boundary pages142/148/466/484 and final document page573 were individually inspected, giving33 final-page views. All four contact sheets were separately opened and inspected. Equations, tables and source paths are complete and readable with intact margins and no overlapping text. Page4 is the short table-of-contents continuation; page573 is the final verification-note continuation, not a blank page or a bibliography page. No private preview substitutes for final inspection.')
(root / 'records/checkpoint30_visual_review.json').write_text(json.dumps(record, indent=2) + '\n')
(root / 'records/checkpoint30_typesetting.txt').write_text(f'''Visual review: PASS
PDF:573 pages;{m['pdf_bytes']} bytes.
SHA-256:{m['pdf_sha256']}
One combined build using records/checkpoint25_tex_env.json; all genuine passes retained.
Initial/final combined overfull counts:0/0; maximum overflow:0/0pt.
The actual final log and stabilized engine stdout were scanned case-insensitively:
no overfull boxes, actual warnings, undefined references or errors.
All18 previous underfull notices remain unchanged; one new B147 evidence-path
paragraph notice is explicitly retained and visually accepted. Total19 notices.
All22 new mathematical pages143–147 and467–483 were individually inspected.
All33 rendered final pages were individually viewed; all four contact sheets
were separately opened and inspected. Final document page573 contains the
verification-note continuation. No private component PDF was generated this interval.
All114 printed bibliography entries are byte-identical to the previous .bbl.
There are323 statements and49 task/lead rows; both main outcomes remain Open.
''')
for suffix in ('aux', 'bbl', 'blg'):
    source = root / f'LM4_SUCCESSOR_paper.{suffix}'
    assert source.exists()
    shutil.copy2(source, root / f'records/checkpoint30_final_paper_{suffix}.retained.txt')
pdfs = ['LM4_SUCCESSOR_paper.pdf', 'records/pdf_qa/checkpoint30_before_integration/LM4_SUCCESSOR_paper.pdf']
(root / 'records/checkpoint30_authored_pdf_retention.json').write_text(json.dumps({
    'recorded_at': datetime.now(timezone.utc).isoformat(),
    'status': 'PASS_ALL_LISTED_AUTHORED_PDF_PATHS_INCLUDED',
    'files': [dict(path=rel, bytes=(root / rel).stat().st_size, sha256=sha(rel),
                   destination='direct ZIP entry' if rel == 'LM4_SUCCESSOR_paper.pdf' else 'standard historical_documents.tar with original path and bytes') for rel in pdfs],
    'scope': 'Current and previous complete combined PDFs. No separate component PDF was generated in cycle30. All earlier authored PDFs and archived versions remain retained; no earlier archive is changed.'
}, indent=2) + '\n')
print('PASS final573-page PDF;22new math and33total individual-page inspections;4contact sheets;114unchanged printed references;18old+1documented new underfull notices.')
