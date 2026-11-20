#!/usr/bin/env python3
"""Make the two native-resolution overlapping halves once; print supplied witnesses."""
import sys,csv
from pathlib import Path
from PIL import Image
root=Path(__file__).resolve().parents[2];n=int(sys.argv[1]);stem=f'16_scan{n:03}'
im=Image.open(root/f'source/SP65_C13_16_scans/{stem}.jpg');w,h=im.size
v=root/'views';v.mkdir(exist_ok=True)
if w<h:
    halves=[('top',(0,0,w,round(h*.55))),('bottom',(0,round(h*.45),w,h))]
else:halves=[('left',(0,0,round(w*.55),h)),('right',(round(w*.45),0,w,h))]
for name,box in halves:
    target=v/f'{n:03}_{name}.png'
    if target.exists():raise SystemExit(f'Halves already prepared: {target}')
    im.crop(box).save(target)
print('SIZE',w,h)
for folder,prefix in [('pages',''),('hua','hua_')]:
    p=root/f'source/SP65_C13_16_texts/{folder}/{prefix}{stem}.tex'
    print('\nWITNESS',folder,'\n'+(p.read_text() if p.exists() else 'NO H PAGE'))
print('\nMARKS')
for r in csv.DictReader((root/'source/SP65_C13_16_texts/MARKS.tsv').open(),delimiter='\t'):
    if int(r['scan'])==n:print(r['id'],r['the mark as written'])
