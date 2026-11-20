"""Remove reading hints from box-kind labels before the image-only audit.

Coordinates and first readings stay unchanged. Detailed coverage reasons remain
in the first-pass reports, which are not supplied to the blind readers.
"""
from pathlib import Path
import csv,json,re
W=Path(__file__).resolve().parents[1]
if (W/'second/first_readings_manifest.json').exists():
    raise SystemExit('Audit manifest exists; box lists must not be altered.')
order=(W/'page_order.txt').read_text().splitlines()
for page in order:
    p=W/'reports'/f'{page}.json'
    if not p.exists() or not json.loads(p.read_text()).get('adjudicated'):
        raise SystemExit('All first pages must be committed: '+page)
patterns=[('insertion',r'insert'),('deletion',r'struck|delet|cancel'),
          ('margin',r'margin'),('mathematical passage',r'formula|diagram|arrow|tuple|pair|index|indices|subscript|exponent|symbol|relation|inequality'),
          ('handwritten number',r'number|numeric|numeral|pagination|ordinal'),
          ('disputed wording',r'word|abbreviat|shorthand|spelling'),
          ('textual mark',r'punctuation|underline|quotation|quotes|capital|emphasis|hyphen'),
          ('uncertain passage',r'doubt|uncertain|low.confidence|medium.confidence|overwork|retrace')]
n=0
for page in order:
    p=W/'second'/f'{page}_boxes.tsv'
    with p.open(newline='') as f: rows=list(csv.DictReader(f,delimiter='\t'))
    for row in rows:
        kind=row['kind'].lower()
        labels=[label for label,pattern in patterns if re.search(pattern,kind)]
        row['kind']='; '.join(labels or ['source passage'])
    with p.open('w',newline='') as f:
        out=csv.DictWriter(f,fieldnames=['box','kind','x0','y0','x1','y1'],delimiter='\t')
        out.writeheader();out.writerows(rows)
    n+=len(rows)
print('Prepared neutral coverage labels for',n,'blind boxes; no coordinates or first readings changed.')
