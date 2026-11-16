"""Audit an hourly PDF/register and record fresh metrics and result locations."""
from pathlib import Path
from collections import Counter
import argparse, csv, hashlib, json, re
import fitz

a=argparse.ArgumentParser()
a.add_argument('number',type=int)
a.add_argument('--expected',type=int,required=True)
a.add_argument('--headings',required=True)
o=a.parse_args()
p=Path(__file__).resolve().parents[1]
pdf=p/'LM4_SUCCESSOR_paper.pdf'
data=pdf.read_bytes();doc=fitz.open(pdf)
log=(p/'LM4_SUCCESSOR_paper.log').read_text()
rows=list(csv.DictReader((p/'LM4_SUCCESSOR_results.csv').open()))
texts=[page.get_text() for page in doc]
heads={h:[i+1 for i,t in enumerate(texts) if h in t] for h in o.headings.split(',')}
m=dict(pages=len(doc),pdf_bytes=len(data),pdf_sha256=hashlib.sha256(data).hexdigest(),
       statements=len(rows),statuses=dict(Counter(r['status'] for r in rows)),
       bibliography_entries=len(re.findall(r'^@',(p/'LM4_SUCCESSOR_references.bib').read_text(),re.M)),
       task_rows=len(list(csv.DictReader((p/'task_coverage.csv').open()))),
       overfull=re.findall(r'^.*Overfull.*$',log,re.M),
       warnings=re.findall(r'^.*Warning.*$',log,re.M),
       errors=re.findall(r'^.*(?:^!|Error|undefined).*$',log,re.M),headings=heads)
(p/'records'/f'checkpoint{o.number:02d}_metrics.json').write_text(json.dumps(m,indent=2)+'\n')
print(json.dumps(m,indent=2))
assert len(rows)==o.expected and m['task_rows']==49
assert not m['overfull'] and not m['warnings'] and not m['errors']
