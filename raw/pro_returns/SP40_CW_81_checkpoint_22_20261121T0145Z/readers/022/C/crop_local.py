from PIL import Image, ImageOps, ImageEnhance, ImageFilter
from pathlib import Path
import json

ROOT=Path('/workspace/scratch/94548b74fbe0')
OUT=ROOT/'out/readers/022/C'
SOURCE=ROOT/'source/SP40_CW_81_scans/J81-03_81_scan022.jpg'
targets=[
 ('c01_opening', (245,65,850,255), 'Opening cancelled wording, insertion and the complete descender of que'),
 ('c02_top_right', (875,140,1678,385), 'Top parenthetical formula, hats, underbrace/vertical equality, opener and disjoints ending'),
 ('c03_first_conditions', (390,260,1040,500), 'First two conditions, looped left brace, marginal arrow, Sigma head, cancelled relation and empty set'),
 ('c04_main_annotations', (585,630,1220,870), 'Main barred Sigma and both lower annotations with their complete connectors and crossing line'),
 ('c05_cancelled_upper', (245,775,1665,1110), 'Cancelled Comme sentence and inverse inclusion; independent Sigma heads and the displayed endpoint'),
 ('c06_soit', (245,1105,1668,1325), 'Cancelled x and neighbourhood argument, accents, all bars, i.e. and rencontre continuation attachment'),
 ('c07_or_on', (680,1305,1620,1440), 'Cancelled Or/on/peut considérer cette with full local strike and preceding qu’il continuation'),
 ('c08_old_noun', (245,1410,1265,1535), 'Old noun under inserted égalité and complete comme égalité dans continuation'),
 ('c09_old_variable', (290,1525,1365,1665), 'Complete cancelled l’espace and Y/Z/X group, equality and both Sigma glyphs'),
 ('c10_detached_stroke', (1130,1720,1365,1915), 'Detached oblique stroke with complete neighbouring preceding word and lower line context'),
 ('c11_bottom_pair', (605,1910,1350,2090), 'Bottom Y/Z display, Sigma hats/heads, union and its full lower beta/alpha limit'),
]
im=Image.open(SOURCE)
records=[]
for name,bbox,purpose in targets:
 crop=ImageOps.autocontrast(im.crop(bbox).convert('RGB'), cutoff=0)
 scale=2400/crop.width
 crop=crop.resize((2400,round(crop.height*scale)),Image.Resampling.LANCZOS)
 crop=crop.filter(ImageFilter.UnsharpMask(radius=1,percent=90,threshold=3))
 path=OUT/(name+'.png')
 crop.save(path)
 records.append(dict(path=path.name,bbox=list(bbox),coordinate_system='full scan, top-left origin, half-open pixel bounds',rotation=0,purpose=purpose,output_size=list(crop.size),viewed=False))
(OUT/'crop_manifest.json').write_text(json.dumps(records,indent=2,ensure_ascii=False)+'\n')
