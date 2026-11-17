"""Verify actual frozen proof, PDF, review and delivery prerequisites."""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import json
import re

root=Path(__file__).resolve().parents[1]
read=lambda rel:json.loads((root/rel).read_text())
m=read('records/checkpoint26_metrics.json')
assert m['statements']==299 and m['pages']>474 and m['task_rows']==49
assert m['statuses']=={'Known':6,'Proved':255,'Refuted':19,'Open':19}
assert m['bibliography_entries']==112
assert not m['overfull'] and not m['warnings'] and not m['errors']
assert hashlib.sha256((root/'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest()==m['pdf_sha256']
review=read('records/checkpoint26_root_formal_reviews.json')
assert review['status']=='PASS_COMPLETE_SOURCE_REVIEW' and len(review['formal_sources'])==7
for rel,digest in review['formal_sources'].items():
    assert hashlib.sha256((root/rel).read_bytes()).hexdigest()==digest,rel
for row in read('records/checkpoint26_formal_source_copies.json')['copies']:
    assert (root/row['source']).read_bytes()==(root/row['integrated']).read_bytes()
    assert hashlib.sha256((root/row['integrated']).read_bytes()).hexdigest()==row['sha256']
rows=list(csv.DictReader((root/'LM4_SUCCESSOR_results.csv').open()))
assert len(rows)==299 and dict(Counter(r['status'] for r in rows))==m['statuses']
tasks=list(csv.DictReader((root/'task_coverage.csv').open()))
assert len(tasks)==49
for task in ('A.8','B.4'):
    assert next(r for r in tasks if r['task']==task)['outcome']=='Open'
assert (root/'LM4_SUCCESSOR_report.md').read_text().splitlines()[0]=='INCOMPLETE'
entries=re.split(r'(?m)(?=^@)',(root/'LM4_SUCCESSOR_references.bib').read_text())[1:]
assert len(entries)==112
assert all(re.search(r'\b(?:verified|unverified)\b',entry,re.I) for entry in entries)
assert len(re.findall(r'\\bibitem',(root/'LM4_SUCCESSOR_paper.bbl').read_text()))==112
visual=read('records/checkpoint26_visual_review.json')
assert visual['visual_review']=='PASS' and visual['pdf_sha256']==m['pdf_sha256']
assert set(visual['required_math_pages'])<=set(visual['individually_inspected_pages'])
assert visual['final_log_and_stdout_case_insensitive']=='PASS'
qa=(root/'records/checkpoint26_typesetting.txt').read_text()
assert 'Visual review: PASS' in qa and m['pdf_sha256'] in qa
estimate=read('records/checkpoint26_size_estimate.json')
assert estimate['estimated_total_with_allowance']<estimate['delivery_cap_bytes']==536870912
freeze=read('records/checkpoint26_writer_pause.json')
assert freeze['all_writers_paused'] and len(freeze['agents'])==3
assert not freeze['live_producers']
for rel in ('records/twenty_sixth_hour_research_report.md',
            'records/checkpoint26_computation_audit_state.md',
            'records/primary_readings26.md','records/checkpoint26_authored_pdf_retention.json'):
    assert (root/rel).is_file(),rel
late=read('records/checkpoint26_root_full_topology_review.json')
assert late['status']=='PASS_ARBITRARY_FINITE_TARGET_EXTENSION_IN_ACTUAL_AMBIENT_GROUP'
assert hashlib.sha256((root/late['proof']).read_bytes()).hexdigest()==late['proof_sha256']
assert hashlib.sha256((root/late['independent_full_review']).read_bytes()).hexdigest()==late['independent_full_review_sha256']
assert read('records/checkpoint26_root_late_reviews.json')['status']=='PASS_COMPLETE_LATE_PROOF_SOURCE_REVIEW'
assert not (root.parent/'LM4_SUCCESSOR_checkpoint_26.zip').exists()
print('PASS 299 statements,49 tasks,112 printed references,complete proofs and final visible QA;both main decisions Open.')
