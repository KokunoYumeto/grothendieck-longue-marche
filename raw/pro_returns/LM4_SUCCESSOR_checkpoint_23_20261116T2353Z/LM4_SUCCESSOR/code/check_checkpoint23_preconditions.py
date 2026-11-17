"""Verify the reviewed formal artifacts and explicit capture prerequisites."""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
m = json.loads((root/'records/checkpoint23_metrics.json').read_text())
assert m['statements'] == 283 and m['pages'] >= 439 and m['task_rows'] == 49
assert m['statuses'] == {'Known':6,'Proved':239,'Refuted':19,'Open':19}
assert m['bibliography_entries'] == 111
assert not m['overfull'] and not m['warnings'] and not m['errors']
assert hashlib.sha256((root/'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest() == m['pdf_sha256']
qa = (root/'records/checkpoint23_typesetting.txt').read_text()
assert 'Visual review: PASS' in qa and m['pdf_sha256'] in qa
review = json.loads((root/'records/checkpoint23_root_formal_reviews.json').read_text())
assert review['status'] == 'PASS'
for rel,digest in review['formal_sources'].items():
    assert hashlib.sha256((root/rel).read_bytes()).hexdigest() == digest, rel
rows = list(csv.DictReader((root/'LM4_SUCCESSOR_results.csv').open()))
assert len(rows) == 283 and dict(Counter(r['status'] for r in rows)) == m['statuses']
tasks = list(csv.DictReader((root/'task_coverage.csv').open()))
assert len(tasks) == 49
for task in ('A.8','B.4'):
    assert next(r for r in tasks if r['task'] == task)['outcome'] == 'Open'
assert (root/'LM4_SUCCESSOR_report.md').read_text().splitlines()[0] == 'INCOMPLETE'
entries = re.split(r'(?m)(?=^@)',(root/'LM4_SUCCESSOR_references.bib').read_text())[1:]
assert len(entries) == 111
assert all(re.search(r'\b(?:verified|unverified)\b',entry,re.I) for entry in entries)
bbl = (root/'LM4_SUCCESSOR_paper.bbl').read_text()
assert len(re.findall(r'\\bibitem',bbl)) == 111
assert 'B_Maassarani2021Orbit' in bbl and 'B_Roushon2026Orbit' in bbl
for rel in ('records/twenty_third_hour_research_report.md',
            'records/checkpoint23_computation_audit_state.md',
            'records/checkpoint23_writer_pause.md',
            'work_CE/review_B112_formal23.txt',
            'work_DE/next_marginal_source/review_B112_B113_final23.md',
            'work_DE/next_marginal_source/review_B114_upper_collar23.md'):
    assert (root/rel).is_file(), rel
assert not (root.parent/'LM4_SUCCESSOR_checkpoint_23.zip').exists()
print('PASS final283-statement artifacts,49 tasks,111 printed bibliography records, complete reviews and clean QA; both main decisions Open.')
