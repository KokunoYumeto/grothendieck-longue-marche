"""Write image-only audit box lists without leaking proposed readings in labels."""
from pathlib import Path
import csv, json, re, sys

ROOT = Path(__file__).resolve().parents[1]

def neutral_kind(description):
    s = description.lower()
    kinds = []
    for pattern, label in [
        (r'margin|marginal|foliation', 'margin'),
        (r'formula|display|mathematical|index|indices|subscript', 'formula'),
        (r'diagram', 'diagram'),
        (r'drawing', 'drawing'),
        (r'insert|replacement|leader|raised', 'insertion or attachment'),
        (r'struck|cancel|deletion|overtrac|rework|overlap', 'revision'),
        (r'number|digit|ordinal|folio|heading|label', 'handwritten number or heading'),
        (r'word|prose|sentence|adjective|verb|text|abbrevi|quote|quotation|punctuation|letter|ligature', 'text'),
    ]:
        if re.search(pattern, s): kinds.append(label)
    return '; '.join(kinds or ['selected handwritten region'])

def write_boxes(page, record=None):
    d = record or json.loads((ROOT/'records'/f'{page}.json').read_text())
    columns = ['box', 'kind', 'x0', 'y0', 'x1', 'y1']
    with (ROOT/'second'/f'{page}_boxes.tsv').open('w', newline='') as f:
        out = csv.DictWriter(f, fieldnames=columns, delimiter='\t', extrasaction='ignore')
        out.writeheader()
        for b in d['second_boxes']:
            out.writerow(dict(b, kind=neutral_kind(b['kind'])))

if __name__ == '__main__':
    selected = sys.argv[1:] or [p.stem for p in (ROOT/'pages').glob('*.tex')]
    for page in selected: write_boxes(page)
    print(f'Wrote {len(selected)} neutral box lists; first readings unchanged.')
