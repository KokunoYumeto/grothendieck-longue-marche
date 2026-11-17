"""Verify the frozen paper and all evidence required before one immutable capture."""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
read = lambda rel: json.loads((root / rel).read_text())
sha = lambda rel: hashlib.sha256((root / rel).read_bytes()).hexdigest()
m = read('records/checkpoint28_metrics.json')
assert m['statements'] == 308 and m['pages'] == 530 and m['task_rows'] == 49
assert m['statuses'] == {'Known': 6, 'Proved': 264, 'Refuted': 19, 'Open': 19}
assert m['bibliography_entries'] == 113
assert not m['overfull'] and not m['warnings'] and not m['errors']
assert sha('LM4_SUCCESSOR_paper.pdf') == m['pdf_sha256']
review = read('records/checkpoint28_root_formal_reviews.json')
assert review['status'] == 'PASS_COMPLETE_SOURCE_REVIEW' and len(review['copies']) == 5
for row in review['copies']:
    assert (root / row['source']).read_bytes() == (root / row['target']).read_bytes()
    assert sha(row['target']) == row['sha256']
assert read('records/checkpoint28_formal_source_copies.json')['copies'] == review['copies']
rows = list(csv.DictReader((root / 'LM4_SUCCESSOR_results.csv').open()))
assert len(rows) == 308 and dict(Counter(r['status'] for r in rows)) == m['statuses']
tasks = list(csv.DictReader((root / 'task_coverage.csv').open()))
assert len(tasks) == 49
for task in ('A.8', 'B.4'):
    assert next(r for r in tasks if r['task'] == task)['outcome'] == 'Open'
assert (root / 'LM4_SUCCESSOR_report.md').read_text().splitlines()[0] == 'INCOMPLETE'
entries = re.split(r'(?m)(?=^@)', (root / 'LM4_SUCCESSOR_references.bib').read_text())[1:]
assert len(entries) == 113
assert all(re.search(r'\b(?:verified|unverified)\b', entry, re.I) for entry in entries)
assert len(re.findall(r'\\bibitem', (root / 'LM4_SUCCESSOR_paper.bbl').read_text())) == 113
visual = read('records/checkpoint28_visual_review.json')
assert visual['visual_review'] == 'PASS' and visual['pdf_sha256'] == m['pdf_sha256']
assert set(visual['required_math_pages']) <= set(visual['individually_inspected_pages'])
assert len(visual['required_math_pages']) == 21 and visual['contact_sheets_inspected'] == 4
assert visual['final_log_and_stdout_case_insensitive'] == 'PASS'
qa = (root / 'records/checkpoint28_typesetting.txt').read_text()
assert 'Visual review: PASS' in qa and m['pdf_sha256'] in qa
estimate = read('records/checkpoint28_size_estimate.json')
assert estimate['estimated_total_with_allowance'] < estimate['delivery_cap_bytes'] == 536870912
for kind in ('images', 'documents'):
    assert estimate['prospective_bundles'][kind]['compression'] == 'ZIP_LZMA'
freeze = read('records/checkpoint28_writer_pause.json')
assert freeze['all_writers_paused'] and len(freeze['agents']) == 3
assert not freeze['live_producers']
for rel in ('records/twenty_eighth_hour_research_report.md',
            'records/checkpoint28_computation_audit_state.md',
            'records/primary_readings28.md',
            'records/checkpoint28_authored_pdf_retention.json',
            'records/checkpoint28_root_dihedral_boundary.md'):
    assert (root / rel).is_file(), rel
late = read('records/checkpoint28_root_late_reviews.json')
assert late['status'] == 'PASS_COMPLETE_LATE_PROOF_REVIEW_WITH_EXPLICIT_REMAINING_GATES'
assert late['formal_statement_count'] == 308 and not late['formal_promotion']
for rel, digest in late['proof_sources'].items():
    assert sha(rel) == digest, rel
assert not (root.parent / 'LM4_SUCCESSOR_checkpoint_28.zip').exists()
print('PASS308 statements,530 pages,49tasks,113printed references;full proof and final visual QA;both main decisions Open.')
