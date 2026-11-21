from pathlib import Path
import json
from PIL import Image, ImageOps, ImageEnhance, ImageFilter

ROOT = Path('/workspace/scratch/0cab6a548abb')
SOURCE = ROOT / 'packets/149_scan124/full.jpg'
TARGET = ROOT / 'edition/crops'
TARGET.mkdir(parents=True, exist_ok=True)
PLAN = [
    ('p01', [340,65,1640,200], 2.2, 0, 'whole first line: plain O forms, barred first L and plain final L'),
    ('p02', [335,210,1665,600], 2.2, 0, 'point primes, decomposition/inertia indices, au dessus and ayant'),
    ('p03', [320,600,1630,880], 2.2, 0, 'signalé descender and plain O in the particular case'),
    ('p04', [310,880,1665,1290], 2.2, 0, 'L’idée through complete valuation parenthesis and trouve'),
    ('p05', [20,1260,1640,1660], 1.9, 0, 'main T expression and complete margin identity, codim quotation and x∈X'),
    ('p06', [300,1635,1550,1905], 2.4, 0, 'et si point, dim0, aur./aura and complete E expression'),
    ('p07', [300,1885,1665,2130], 2.2, 0, 'ss-groupe, whole k argument, inserted fini and layered par with whole T-alpha'),
    ('p08', [300,2100,1665,2330], 2.2, 0, 'last two main lines through the written donne-'),
    ('p09', [15,1985,300,2240], 5.0, -25, 'still-open lower marginal note, rotated'),
    ('p10', [15,2308,115,2355], 8.0, 0, 'thin foliation 123'),
    ('p11', [335,470,1450,640], 2.5, 0, 'incomplete-view repair: full ayant descender clipped at p02 bottom'),
    ('p12', [1100,1930,1520,2100], 6.0, 0, 'still-open layered par, with complete T-alpha and adjoining dash'),
    ('p13', [470,1930,740,2120], 7.5, 0, 'still-open fini insertion: lower strokes and attachment to alg.'),
    ('p14', [300,1840,1665,2335], 2.2, 0, 'incomplete-view repair: upper boundary of pouvoir in p08, with complete lower context and E_K/puisque'),
]
im = Image.open(SOURCE).convert('RGB')
assert im.size == (1680,2364)
manifest = []
for place,box,scale,angle,purpose in PLAN:
    path = TARGET / f'149_scan124_{place}.png'
    if path.exists():
        with Image.open(path) as saved:
            manifest.append({'id':place,'bbox':box,'scale':scale,'rotation_degrees':angle,
                             'purpose':purpose,'file':f'crops/{path.name}','size':list(saved.size)})
        continue
    out = ImageOps.autocontrast(im.crop(tuple(box)),cutoff=0.4)
    out = out.resize((round(out.width*scale),round(out.height*scale)),Image.Resampling.LANCZOS)
    if angle:
        out=out.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
    out=ImageEnhance.Contrast(out).enhance(1.12)
    out=out.filter(ImageFilter.UnsharpMask(radius=1.2,percent=90,threshold=3))
    out.save(path)
    manifest.append({'id':place,'bbox':box,'scale':scale,'rotation_degrees':angle,
                     'purpose':purpose,'file':f'crops/{path.name}','size':list(out.size)})
(ROOT/'edition/review/149_scan124_crop_geometry.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'crops':len(manifest),'files':[g['file'] for g in manifest]}))
