"""Fresh metrics for the recovered seventh-checkpoint PDF, not the lost PDF."""
from pathlib import Path
import csv, hashlib, json, re
from collections import Counter
import fitz

p = Path(__file__).resolve().parents[1]
pdf_path = p / 'LM4_SUCCESSOR_paper.pdf'
pdf_bytes = pdf_path.read_bytes()
doc = fitz.open(pdf_path)
log = (p / 'LM4_SUCCESSOR_paper.log').read_text()
rows = list(csv.DictReader((p / 'LM4_SUCCESSOR_results.csv').open()))
headings = {}
for heading in ['A.55.', 'A.56.', 'A.57.', 'B.65.', 'B.66.', 'C.41.', 'C.42.', 'References']:
    headings[heading] = [i + 1 for i, page in enumerate(doc) if heading in page.get_text()]
metrics = dict(pages=len(doc), pdf_bytes=len(pdf_bytes),
               pdf_sha256=hashlib.sha256(pdf_bytes).hexdigest(),
               statements=len(rows), statuses=dict(Counter(r['status'] for r in rows)),
               bibliography_entries=len(re.findall(r'^@', (p / 'LM4_SUCCESSOR_references.bib').read_text(), re.M)),
               task_rows=len(list(csv.DictReader((p / 'task_coverage.csv').open()))),
               overfull=re.findall(r'^.*Overfull.*$', log, re.M),
               warnings=re.findall(r'^.*Warning.*$', log, re.M),
               errors=re.findall(r'^.*(?:^!|Error|undefined).*$', log, re.M),
               headings=headings)
(p / 'records/checkpoint07_recovery_metrics.json').write_text(json.dumps(metrics, indent=2) + '\n')
print(json.dumps(metrics, indent=2))
assert not metrics['overfull'] and not metrics['warnings'] and not metrics['errors']
assert len(rows) == 206 and metrics['task_rows'] == 49
