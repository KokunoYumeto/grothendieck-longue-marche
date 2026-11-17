"""Check the final reviewed formal artifacts before the hourly writer pause."""
from pathlib import Path
import csv,hashlib,json,re
from collections import Counter
root=Path(__file__).resolve().parents[1]
m=json.loads((root/'records/checkpoint21_metrics.json').read_text())
assert m['statements']==276 and m['pages']==408 and m['task_rows']==49
assert m['statuses']=={'Known':6,'Proved':232,'Refuted':19,'Open':19}
assert m['bibliography_entries']==108
assert not m['overfull'] and not m['warnings'] and not m['errors']
assert hashlib.sha256((root/'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest()==m['pdf_sha256']
qa=(root/'records/checkpoint21_typesetting.txt').read_text()
assert 'Visual review: PASS' in qa and m['pdf_sha256'] in qa
review=json.loads((root/'records/checkpoint21_root_formal_reviews.json').read_text())
assert review['status']=='PASS'
for rel,digest in review['formal_sources'].items():
    assert hashlib.sha256((root/rel).read_bytes()).hexdigest()==digest
rows=list(csv.DictReader((root/'LM4_SUCCESSOR_results.csv').open()))
assert len(rows)==276 and dict(Counter(r['status'] for r in rows))==m['statuses']
tasks=list(csv.DictReader((root/'task_coverage.csv').open()))
assert len(tasks)==49
for task in ['A.8','B.4']:
    assert next(r for r in tasks if r['task']==task)['outcome']=='Open'
assert (root/'LM4_SUCCESSOR_report.md').read_text().splitlines()[0]=='INCOMPLETE'
for rel in ['records/checkpoint21_late_root_reviews.md',
            'work_DE/next_marginal_source/review_B106_B107_21h.md',
            'work_A/review_B107_retracted_amalgam21.md',
            'work_CE/shared_five_generator_neck_21h.txt',
            'work_DE/next_marginal_source/middle_neck_marked_noninjection21.md',
            'work_A/review_middle_neck_noninjection21.md']:
    assert (root/rel).is_file(),rel
assert not (root.parent/'LM4_SUCCESSOR_checkpoint_21.zip').exists()
print('PASS final276-statement/408-page formal artifacts,49 task rows,108 bibliography records, independent reviews, clean QA; both main decisions Open. Capture not started.')
