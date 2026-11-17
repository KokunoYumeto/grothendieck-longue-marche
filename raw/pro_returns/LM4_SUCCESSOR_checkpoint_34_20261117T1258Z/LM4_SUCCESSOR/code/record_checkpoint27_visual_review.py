"""Record completed individual-page and separate contact-sheet inspection."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import hashlib,json,re,shutil

root=Path(__file__).resolve().parents[1]
read=lambda p:json.loads((root/p).read_text())
sha=lambda p:hashlib.sha256((root/p).read_bytes()).hexdigest()
m=read('records/checkpoint27_metrics.json')
assert m['pages']==509 and m['statements']==303
assert sha('LM4_SUCCESSOR_paper.pdf')==m['pdf_sha256']
build='records/build_passes/20261117T032230884013Z/build_stabilize_0.log'
audits=[]
for rel in ['LM4_SUCCESSOR_paper.log',build]:
    text=(root/rel).read_text(errors='replace')
    lines=text.splitlines()
    underfull=[x for x in lines if re.search(r'underfull',x,re.I)]
    warnings=[x for x in lines if re.search(r'warning',x,re.I)
              and not ('infwarerr' in x or 'Providing info/warning/error messages' in x)]
    issues=[x for x in lines if re.search(r'overfull|undefined|^!|error',x,re.I)
            and not ('infwarerr' in x or 'Providing info/warning/error messages' in x)]
    assert not warnings and not issues
    audits.append(dict(path=rel,sha256=sha(rel),warnings=warnings,issues=issues,
                       underfull_notices=underfull))
old=(root/'records/pdf_qa/checkpoint27_before_integration/LM4_SUCCESSOR_paper.log').read_text()
old_underfull=[x for x in old.splitlines() if re.search(r'underfull',x,re.I)]
assert Counter(old_underfull)==Counter(audits[0]['underfull_notices'])
assert len(old_underfull)==18
rendered=[1,2,3,50,130,230,350,403,*range(404,420),420,421,440,480,509]
individual=[1,2,3,*range(404,420),509]
for n in rendered:assert (root/f'records/pdf_qa/checkpoint27_final/page-{n:03d}.png').exists()
for n in range(1,5):assert (root/f'records/pdf_qa/checkpoint27_final/contact-{n:02d}.png').exists()
assert len(re.findall(r'\\bibitem',(root/'LM4_SUCCESSOR_paper.bbl').read_text()))==113
record=dict(recorded_at=datetime.now(timezone.utc).isoformat(),
 pdf_sha256=m['pdf_sha256'],rendered_pages=rendered,
 required_math_pages=list(range(404,420)),individually_inspected_pages=individual,
 contact_sheets_inspected=4,each_contact_sheet_opened_separately=True,
 truncated_outputs_counted=False,combined_build_attempts=1,
 combined_overfull_before=0,combined_overfull_after=0,
 maximum_overflow_before_pt=0,maximum_overflow_after_pt=0,
 printed_bibliography_entries=113,final_log_and_stdout_audits=audits,
 underfull_scope='The same 18 notices occur in the prior combined PDF log, byte-identical by multiset. No new underfull notice; all new math pages individually inspected and four contact sheets inspected separately.',
 final_log_and_stdout_case_insensitive='PASS',visual_review='PASS',
 visual_findings='Readable equations/tables and intact margins, no clipping or overlap, clear proof boundaries and page transitions. All sixteen new mathematical pages404--419 inspected individually; opening pages1--3 and final bibliography page509 also inspected individually. The contact sheets additionally sample every part of the paper.')
(root/'records/checkpoint27_visual_review.json').write_text(json.dumps(record,indent=2)+'\n')
(root/'records/checkpoint27_typesetting.txt').write_text(f'''Visual review: PASS
PDF: 509 pages; {m['pdf_bytes']} bytes.
SHA-256: {m['pdf_sha256']}
One combined build using records/checkpoint25_tex_env.json; genuine passes retained.
Initial/final combined overfull counts: 0/0; maximum overflow: 0/0pt.
Actual final log and stabilized engine stdout scanned case-insensitively:
no overfull boxes, actual warnings, undefined references or errors.
The existing18 underfull notices are unchanged by exact multiset comparison.
Every new mathematical page404--419 individually viewed, together with1--3
and509:20 individual final-page views. Four contact sheets were each opened
separately, covering29 pages across all parts and the bibliography.
No truncated output or prior private QA substitutes for these final views.
All113 bibliography entries printed;303 statements and49 task/lead rows.
Private B131 layout failures, B132 engine mismatch, B133 explicit map
clarification and B134 mirror/typed-map precursors all remain preserved.
''')
for suffix in ('aux','bbl','blg'):
    source=root/f'LM4_SUCCESSOR_paper.{suffix}'
    if source.exists():shutil.copy2(source,root/f'records/checkpoint27_final_paper_{suffix}.retained.txt')
pdfs=['LM4_SUCCESSOR_paper.pdf',
 'records/pdf_qa/checkpoint27_before_integration/LM4_SUCCESSOR_paper.pdf',
 'work_A/B131_component.pdf','work_A/B131_component_initial.pdf','work_A/B131_component_layout1.pdf',
 'work_CE/qa_B132/B132_check.pdf',
 'work_DE/B133_review.pdf','work_DE/B133_before_explicit_z.pdf',
 'work_DE/B134_review.pdf','work_DE/B134_before_typed_Phi.pdf']
for rel in pdfs:
    assert (root/rel).is_file()
    if rel.startswith('work_DE/'):assert (root/rel).with_suffix('.tex').is_file()
(root/'records/checkpoint27_authored_pdf_retention.json').write_text(json.dumps({
 'recorded_at':datetime.now(timezone.utc).isoformat(),
 'status':'PASS_ALL_LISTED_AUTHORED_PDF_PATHS_INCLUDED',
 'files':[dict(path=rel,bytes=(root/rel).stat().st_size,sha256=sha(rel),
               destination='direct ZIP entry' if rel=='LM4_SUCCESSOR_paper.pdf' else 'standard historical_documents.tar with original path and bytes') for rel in pdfs],
 'scope':'Current main PDF, prior complete combined PDF and every authored private PDF/precursor from the four integrated sources. Historical retention separately covers every earlier archived byte. No prior archive is changed.'
},indent=2)+'\n')
print('PASS final509-page PDF;16newmath pages and20total pages individually viewed;4separate contact sheets;113printed references.')
