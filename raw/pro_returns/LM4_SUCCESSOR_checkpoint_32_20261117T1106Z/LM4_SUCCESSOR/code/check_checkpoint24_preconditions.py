"""Verify frozen reviewed artifacts and concrete checkpoint24 prerequisites."""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
read = lambda rel: json.loads((root/rel).read_text())
m = read('records/checkpoint24_metrics.json')
assert m['statements'] == 286 and m['pages'] == 450 and m['task_rows'] == 49
assert m['statuses'] == {'Known': 6, 'Proved': 242, 'Refuted': 19, 'Open': 19}
assert m['bibliography_entries'] == 111
assert not m['overfull'] and not m['warnings'] and not m['errors']
assert hashlib.sha256((root/'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest() == m['pdf_sha256']
qa = (root/'records/checkpoint24_typesetting.txt').read_text()
assert 'Visual review: PASS' in qa and m['pdf_sha256'] in qa
review = read('records/checkpoint24_root_formal_reviews.json')
assert review['status'] == 'PASS_COMPLETE_SOURCE_REVIEW'
for rel, digest in review['formal_sources'].items():
    assert hashlib.sha256((root/rel).read_bytes()).hexdigest() == digest, rel
copies = read('records/checkpoint24_formal_source_copies.json')
for row in copies['copies']:
    assert (root/row['source']).read_bytes() == (root/row['integrated']).read_bytes()
    assert hashlib.sha256((root/row['integrated']).read_bytes()).hexdigest() == row['sha256']
rows = list(csv.DictReader((root/'LM4_SUCCESSOR_results.csv').open()))
assert len(rows) == 286 and dict(Counter(r['status'] for r in rows)) == m['statuses']
tasks = list(csv.DictReader((root/'task_coverage.csv').open()))
assert len(tasks) == 49
for task in ('A.8', 'B.4'):
    assert next(r for r in tasks if r['task'] == task)['outcome'] == 'Open'
assert (root/'LM4_SUCCESSOR_report.md').read_text().splitlines()[0] == 'INCOMPLETE'
entries = re.split(r'(?m)(?=^@)', (root/'LM4_SUCCESSOR_references.bib').read_text())[1:]
assert len(entries) == 111
assert all(re.search(r'\b(?:verified|unverified)\b', entry, re.I) for entry in entries)
assert len(re.findall(r'\\bibitem', (root/'LM4_SUCCESSOR_paper.bbl').read_text())) == 111
visual = read('records/checkpoint24_visual_review.json')
assert visual['visual_review'] == 'PASS' and visual['contact_sheets_inspected'] == 5
assert set(range(352, 362)) <= set(visual['individually_inspected_pages'])
estimate = read('records/checkpoint24_size_estimate.json')
assert estimate['estimated_total_with_allowance'] < estimate['delivery_cap_bytes'] == 536870912
compat = read('records/checkpoint24_container_compatibility.json')
assert compat['all_reencoded_pdf_bytes'] == compat['both_container_logical_namespace'] == 'PASS'
late = read('records/checkpoint24_late_root_reviews.json')
assert late['status'] == 'PASS_COMPLETE_ROOT_READS_AT_STATED_SCOPES'
for rel, digest in late['sources'].items():
    assert hashlib.sha256((root/rel).read_bytes()).hexdigest() == digest, rel
assert 'To be appended only after' not in (root/'records/checkpoint24_computation_audit_state.md').read_text()
addendum = read('records/checkpoint24_completed_intersection_review.json')
assert addendum['status'] == 'PASS_ROOT_PROOF_AND_INDEPENDENT_READ_ONLY_CHECK'
assert hashlib.sha256((root/addendum['source']).read_bytes()).hexdigest() == addendum['source_sha256']
for rel in ('records/twenty_fourth_hour_research_report.md',
            'records/checkpoint24_computation_audit_state.md',
            'records/checkpoint24_writer_pause.md',
            'work_DE/next_marginal_source/review_B115_frozen_source24.md',
            'work_A/review_B116_intrinsic_centralizers24.md',
            'work_DE/next_marginal_source/review_B117_frozen_source24.md'):
    assert (root/rel).is_file(), rel
assert not (root.parent/'LM4_SUCCESSOR_checkpoint_24.zip').exists()
print('PASS frozen 286-statement artifacts, 450 pages, 49 tasks, 111 printed references, complete reviews and final QA; both main decisions Open.')
