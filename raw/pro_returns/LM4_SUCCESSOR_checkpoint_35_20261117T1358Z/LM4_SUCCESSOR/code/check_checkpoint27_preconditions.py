"""Verify frozen proof, final PDF, review and immutable delivery prerequisites."""
from pathlib import Path
from collections import Counter
import csv,hashlib,json,re

root=Path(__file__).resolve().parents[1]
read=lambda rel:json.loads((root/rel).read_text())
m=read('records/checkpoint27_metrics.json')
assert m['statements']==303 and m['pages']>493 and m['task_rows']==49
assert m['statuses']=={'Known':6,'Proved':259,'Refuted':19,'Open':19}
assert m['bibliography_entries']==113
assert not m['overfull'] and not m['warnings'] and not m['errors']
assert hashlib.sha256((root/'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest()==m['pdf_sha256']
review=read('records/checkpoint27_root_formal_reviews.json')
assert review['status']=='PASS_COMPLETE_SOURCE_REVIEW' and len(review['copies'])==4
for row in review['copies']:
    assert (root/row['source']).read_bytes()==(root/row['target']).read_bytes()
    assert hashlib.sha256((root/row['target']).read_bytes()).hexdigest()==row['sha256']
assert read('records/checkpoint27_formal_source_copies.json')['copies']==review['copies']
rows=list(csv.DictReader((root/'LM4_SUCCESSOR_results.csv').open()))
assert len(rows)==303 and dict(Counter(r['status'] for r in rows))==m['statuses']
tasks=list(csv.DictReader((root/'task_coverage.csv').open()))
assert len(tasks)==49
for task in ('A.8','B.4'):
    assert next(r for r in tasks if r['task']==task)['outcome']=='Open'
report=(root/'LM4_SUCCESSOR_report.md').read_text()
assert report.splitlines()[0]=='INCOMPLETE'
entries=re.split(r'(?m)(?=^@)',(root/'LM4_SUCCESSOR_references.bib').read_text())[1:]
assert len(entries)==113
assert all(re.search(r'\b(?:verified|unverified)\b',entry,re.I) for entry in entries)
assert len(re.findall(r'\\bibitem',(root/'LM4_SUCCESSOR_paper.bbl').read_text()))==113
visual=read('records/checkpoint27_visual_review.json')
assert visual['visual_review']=='PASS' and visual['pdf_sha256']==m['pdf_sha256']
assert set(visual['required_math_pages'])<=set(visual['individually_inspected_pages'])
assert visual['final_log_and_stdout_case_insensitive']=='PASS'
qa=(root/'records/checkpoint27_typesetting.txt').read_text()
assert 'Visual review: PASS' in qa and m['pdf_sha256'] in qa
estimate=read('records/checkpoint27_size_estimate.json')
assert estimate['estimated_total_with_allowance']<estimate['delivery_cap_bytes']==536870912
for kind in ('images','documents'):
    assert estimate['prospective_bundles'][kind]['compression']=='ZIP_LZMA'
freeze=read('records/checkpoint27_writer_pause.json')
assert freeze['all_writers_paused'] and len(freeze['agents'])==3
assert not freeze['live_producers']
for rel in ('records/twenty_seventh_hour_research_report.md',
            'records/checkpoint27_computation_audit_state.md',
            'records/primary_readings27.md',
            'records/checkpoint27_authored_pdf_retention.json',
            'records/checkpoint27_edge_scope_correction.md'):
    assert (root/rel).is_file(),rel
late=read('records/checkpoint27_root_MainA_review.json')
assert late['status']=='PASS_COMPLETE_ACTUAL_V4_DEFECT_PROOF_READ'
assert hashlib.sha256((root/late['source']).read_bytes()).hexdigest()==late['source_sha256']
assert hashlib.sha256((root/late['independent_full_review']).read_bytes()).hexdigest()==late['independent_full_review_sha256']
latest=read('records/checkpoint27_root_late_reviews.json')
assert latest['status']=='PASS_COMPLETE_LATE_PROOF_REVIEW_WITH_EXPLICIT_REMAINING_GATES'
assert latest['formal_statement_count']==303 and not latest['formal_promotion']
for rel,digest in latest['proof_sources'].items():
    assert hashlib.sha256((root/rel).read_bytes()).hexdigest()==digest,rel
local=read('records/checkpoint27_root_local_fixed_review.json')
assert local['status']=='PASS_COMPLETE_LOCAL_FIXED_SUBGROUP_PROOF_READ'
assert hashlib.sha256((root/local['source']).read_bytes()).hexdigest()==local['sha256']
assert not (root.parent/'LM4_SUCCESSOR_checkpoint_27.zip').exists()
print('PASS 303 statements, 49 tasks, 113 printed references, complete proofs and final visible QA; both main decisions Open.')
