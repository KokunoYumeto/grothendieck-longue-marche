"""Show a bounded set of differing blind-reading boxes for the main reader."""
from pathlib import Path
import csv, json, sys
ROOT=Path(__file__).resolve().parents[1]
scan=int(sys.argv[1]); start=int(sys.argv[2]) if len(sys.argv)>2 else 0
stop=int(sys.argv[3]) if len(sys.argv)>3 else start+4
stem=f'147_scan{scan}'
with (ROOT/'second'/f'{stem}_boxes.tsv').open() as f:
    boxes={r['box']:r for r in csv.DictReader(f,delimiter='\t')}
with (ROOT/'second'/f'{stem}_comparison.tsv').open() as f:
    rows=[r for r in csv.DictReader(f,delimiter='\t') if r['equal']=='no']
for r in rows:
    r['coordinates']=[int(boxes[r['box']][k]) for k in ('x0','y0','x1','y1')]
    r['crop']=str(ROOT/'crops'/f'{stem}_second_{r["box"]}.jpg')
print(json.dumps(rows[start:stop],ensure_ascii=False))
