"""Recreate per-page inputs from the supplied, already-unpacked source tree.
This script does not unpack archives or replace existing page-half images.
"""
from pathlib import Path
import csv,json
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parent
ORDER=json.loads((ROOT/'scripts/page_order.json').read_text())
INPUT=BASE/'input'
marks=list(csv.DictReader((INPUT/'SP91_C13_150_texts/MARKS.tsv').open(),delimiter='\t',quoting=csv.QUOTE_NONE))
diffs=list(csv.DictReader((INPUT/'SP91_C13_150_C_H_differences.tsv').open(),delimiter='\t',quoting=csv.QUOTE_NONE))
def scan_of(r):
    for k in ('scan','our_scan','page','scan_number'):
        if k in r:
            v=r[k]
            try:return f'{int(v):03}'
            except (ValueError,TypeError):pass
    for v in r.values():
        if isinstance(v,str) and 'scan' in v:
            import re
            m=re.search(r'scan(\d+)',v)
            if m:return f'{int(m[1]):03}'
    raise ValueError('Unrecognized source scan column: '+str(r))
for s in ORDER:
    packet=ROOT/'packets'/f'150_scan{s}'
    packet.mkdir(parents=True,exist_ok=True)
    for name,rows in [('marks',marks),('diffs',diffs)]:
        out=packet/f'{name}.tsv'
        if not out.exists():
            with out.open('w',newline='') as f:
                w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
                w.writeheader();w.writerows(r for r in rows if scan_of(r)==s)
    halfdir=BASE/'halves';halfdir.mkdir(exist_ok=True)
    src=INPUT/'SP91_C13_150_scans'/f'150_scan{s}.jpg'
    with Image.open(src) as im:
        w,h=im.size
        halves={'top':(0,0,w,round(h*.55)),'bottom':(0,round(h*.45),w,h)}
        for name,box in halves.items():
            p=halfdir/f'150_scan{s}_{name}.png'
            if not p.exists():im.crop(box).save(p)
print('Missing page packets and halves prepared; existing files preserved.')
