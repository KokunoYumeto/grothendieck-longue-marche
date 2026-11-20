"""Embed the actual first and last reader briefs in the final workflow report."""
from pathlib import Path
import csv
w=Path(__file__).resolve().parents[1]
rows=list(csv.reader((w/'validation/reader_run_register.tsv').open(),delimiter='\t'))
data=[r for r in rows if r and r[0].isdigit()]
assert len(data)==84,'Run only after the 28 pages have their three reader registrations.'
first=data[0][3];last=data[-1][3]
p=w/'SP41_CW_81_workflow.md';s=p.read_text()
marker='\n## Complete first and last reader briefs\n'
s=s.split(marker)[0].rstrip()+marker+'\n'
s+='### First brief: '+first+'\n\n'+(w/'briefs'/first).read_text().rstrip()+'\n\n'
s+='### Last brief used: '+last+'\n\n'+(w/'briefs'/last).read_text().rstrip()+'\n'
p.write_text(s)
print('Embedded complete first and last briefs:',first,last)
