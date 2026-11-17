"""Record the actually completed individual-page and separate contact-sheet reviews."""
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
m = read('records/checkpoint31_metrics.json')
assert m['pages'] == 590 and m['statements'] == 333
assert sha('LM4_SUCCESSOR_paper.pdf') == m['pdf_sha256']
build = 'records/build_passes/20261117T072838170696Z/build_stabilize_0.log'
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
old = (root / 'records/pdf_qa/checkpoint31_before_integration/LM4_SUCCESSOR_paper.log').read_text()
old_underfull = [x for x in old.splitlines() if re.search('underfull', x, re.I)]
assert len(old_underfull) == 19
assert Counter(audits[0]['underfull_notices']) == Counter(old_underfull)
assert Counter(audits[1]['underfull_notices']) == Counter(old_underfull)
failed = (root / 'records/pdf_qa/checkpoint31_before_B151_layout/LM4_SUCCESSOR_paper.log').read_text()
failed_overfull = [float(x) for x in re.findall(r'Overfull \\hbox \((\d+\.?\d*)pt', failed)]
assert failed_overfull == [23.66608, 9.81163]
render = read('records/pdf_qa/checkpoint31_final/render_manifest.json')
required = [*range(147, 155), *range(490, 502)]
individual = sorted(set([*range(1, 7), *range(146, 156), *range(489, 503), 590]))
assert render['pdf_sha256'] == m['pdf_sha256']
assert render['required_new_mathematical_pages'] == required
assert render['rendered_pages'] == individual and len(individual) == 31 and len(required) == 20
assert render['page_count'] == 590 and render['dpi'] == 144 and render['contact_sheets'] == 4
for n in individual:
    assert (root / f'records/pdf_qa/checkpoint31_final/page-{n:03d}.png').exists()
for n in range(1, 5):
    assert (root / f'records/pdf_qa/checkpoint31_final/contact-{n:02d}.png').exists()
assert len(re.findall(r'\\bibitem', (root / 'LM4_SUCCESSOR_paper.bbl').read_text())) == 114
assert ((root / 'LM4_SUCCESSOR_paper.bbl').read_bytes() ==
        (root / 'records/pdf_qa/checkpoint31_before_integration/LM4_SUCCESSOR_paper.bbl.retained.txt').read_bytes())
record = dict(
    recorded_at=datetime.now(timezone.utc).isoformat(), pdf_sha256=m['pdf_sha256'],
    page_count=590, dpi=144, rendered_pages=individual, required_math_pages=required,
    individually_inspected_pages=individual, contact_sheets_inspected=4,
    each_contact_sheet_opened_separately=True, truncated_outputs_counted=False,
    combined_build_attempts=2, combined_overfull_before=2, combined_overfull_after=0,
    maximum_overflow_before_pt=max(failed_overfull), maximum_overflow_after_pt=0,
    printed_bibliography_entries=114, bibliography_bbl_byte_identical_to_checkpoint30=True,
    final_log_and_stdout_audits=audits,
    underfull_scope='All19 prior underfull notices remain byte-identical by multiset in both final engine stdout and the complete log. None was added or removed. This includes the previously accepted B147 provenance-path paragraph, now on page490, which was individually reopened and remains readable without clipping or overlap. The two actual B151 overfull paragraphs from the initial combined build were repaired; their final pages496–497 were individually inspected. The failed PDF, complete log, engine pass outputs, old source bytes and old review bindings are retained.',
    final_log_and_stdout_case_insensitive='PASS', visual_review='PASS',
    visual_findings='All20 new mathematical pages147–154 and490–501 were individually opened and inspected. Front pages1–6, boundary pages146/155/489/502, and final document/bibliography page590 were also individually viewed, for31 total pages. All four contact sheets were opened separately after individual inspection. Equations, tables, repaired subscripts, source paths and margins are complete and readable. Page4 is the short contents continuation. The B151 provenance path continues in two intact lines on page497; its heading paragraph on496 now fits. No clipping, overlap, missing mathematics or empty unintended pages was observed. No component preview substitutes for final inspection.')
out = root / 'records/checkpoint31_visual_review.json'
assert not out.exists()
out.write_text(json.dumps(record, indent=2)+'\n')
(root / 'records/checkpoint31_typesetting.txt').write_text(f'''Visual review: PASS
PDF:590 pages;{m['pdf_bytes']} bytes.
SHA-256:{m['pdf_sha256']}
Two actual combined builds; all genuine engine passes retained.
Initial/final overfull counts:2/0. Maximum overflow:23.66608/0pt.
The initial B151 heading and source-path failures were repaired and preserved.
Final complete log and stabilized stdout scanned case-insensitively: no overfull
boxes, actual warnings, undefined references or errors. All19 old underfull
notices remain byte-identical by multiset; no new notices and none hidden.
All20 new mathematical pages147–154 and490–501 individually inspected.
All31 final rendered pages individually viewed; four contact sheets separately viewed.
All114 printed bibliography entries are byte-identical to the preceding .bbl.
333 statements,49 task rows; Main A and Main B remain Open.
''')
for suffix in ('aux', 'bbl', 'blg'):
    source = root / f'LM4_SUCCESSOR_paper.{suffix}'
    shutil.copy2(source, root / f'records/checkpoint31_final_paper_{suffix}.retained.txt')
pdfs = ['LM4_SUCCESSOR_paper.pdf',
        'records/pdf_qa/checkpoint31_before_integration/LM4_SUCCESSOR_paper.pdf',
        'records/pdf_qa/checkpoint31_before_B151_layout/LM4_SUCCESSOR_paper.pdf']
(root / 'records/checkpoint31_authored_pdf_retention.json').write_text(json.dumps({
    'recorded_at': datetime.now(timezone.utc).isoformat(),
    'status': 'PASS_ALL_LISTED_AUTHORED_PDF_PATHS_INCLUDED',
    'files': [dict(path=rel, bytes=(root / rel).stat().st_size, sha256=sha(rel),
                   destination='direct ZIP entry' if rel == 'LM4_SUCCESSOR_paper.pdf' else 'standard historical_documents.tar with original path and bytes') for rel in pdfs],
    'scope': 'Current, previous and genuine failed combined PDFs. No separate component PDF was generated. All prior authored PDF paths and versions remain retained.'
}, indent=2)+'\n')
print('PASS final590-page PDF;20 new math pages and31 total individual views;4 separate contacts;114 unchanged references;19 unchanged underfull notices;2 actual overflows repaired.')
