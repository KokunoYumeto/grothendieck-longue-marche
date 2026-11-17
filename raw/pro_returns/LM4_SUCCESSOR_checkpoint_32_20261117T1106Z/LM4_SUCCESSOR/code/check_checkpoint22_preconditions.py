"""Verify the final reviewed formal artifacts before the checkpoint22 capture."""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
m = json.loads((root/'records/checkpoint22_metrics.json').read_text())
assert m['statements'] == 280 and m['pages'] >= 420 and m['task_rows'] == 49
assert m['statuses'] == {'Known':6,'Proved':236,'Refuted':19,'Open':19}
assert m['bibliography_entries'] == 109
assert not m['overfull'] and not m['warnings'] and not m['errors']
assert hashlib.sha256((root/'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest() == m['pdf_sha256']
qa = (root/'records/checkpoint22_typesetting.txt').read_text()
assert 'Visual review: PASS' in qa and m['pdf_sha256'] in qa
review = json.loads((root/'records/checkpoint22_root_formal_reviews.json').read_text())
assert review['status'] == 'PASS'
for rel,digest in review['formal_sources'].items():
    assert hashlib.sha256((root/rel).read_bytes()).hexdigest() == digest, rel
rows = list(csv.DictReader((root/'LM4_SUCCESSOR_results.csv').open()))
assert len(rows) == 280 and dict(Counter(r['status'] for r in rows)) == m['statuses']
tasks = list(csv.DictReader((root/'task_coverage.csv').open()))
assert len(tasks) == 49
for task in ('A.8','B.4'):
    assert next(r for r in tasks if r['task'] == task)['outcome'] == 'Open'
assert (root/'LM4_SUCCESSOR_report.md').read_text().splitlines()[0] == 'INCOMPLETE'
entries = re.split(r'(?m)(?=^@)',(root/'LM4_SUCCESSOR_references.bib').read_text())[1:]
assert len(entries) == 109
assert all(re.search(r'\b(?:verified|unverified)\b',entry,re.I) for entry in entries)
for rel in ('records/twenty_second_hour_research_report.md',
            'records/checkpoint22_computation_audit_state.md',
            'work_A/review_B110_final22.md',
            'work_A/review_B111_final22.md',
            'work_DE/next_marginal_source/review_B110_final22.md',
            'work_DE/next_marginal_source/review_B111_final22.md'):
    assert (root/rel).is_file(), rel
assert not (root.parent/'LM4_SUCCESSOR_checkpoint_22.zip').exists()
print('PASS final280-statement formal artifacts,49 tasks,109 bibliography records, complete reviews and clean QA; both main decisions Open.')
