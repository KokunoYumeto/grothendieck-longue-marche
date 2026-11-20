from pathlib import Path
import csv, json, sys
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'SP72_C13_142_work'
SOURCE = ROOT / 'source'
n = int(sys.argv[1])
packet = ROOT / 'packets' / f'scan{n:03}'
packet.mkdir(parents=True, exist_ok=True)
src = SOURCE / 'SP72_C13_142_scans' / f'142_scan{n:03}.jpg'
im = Image.open(src)
w, h = im.size
if w <= h:
    halves = {'top': (0,0,w,round(h*.55)), 'bottom': (0,round(h*.45),w,h)}
else:
    halves = {'left': (0,0,round(w*.55),h), 'right': (round(w*.45),0,w,h)}
for name, box in halves.items():
    dest = packet / (name+'.png')
    if not dest.exists():
        im.crop(box).save(dest)
texts = SOURCE / 'SP72_C13_142_texts'
for name, path in [('C.tex',texts/'pages'/f'142_scan{n:03}.tex'),('H.tex',texts/'hua'/f'hua_142_scan{n:03}.tex')]:
    (packet/name).write_text(path.read_text())
with (texts/'MARKS.tsv').open() as f:
    marks = [r for r in csv.DictReader(f,delimiter='\t') if int(r['scan'])==n]
(packet/'marks.json').write_text(json.dumps(marks,ensure_ascii=False,indent=2))
(packet/'notation.md').write_text((OUT/'notation.md').read_text())
(packet/'source.json').write_text(json.dumps({'scan':n,'whole_image':str(src),'dimensions':[w,h],'halves':halves},indent=2))
print(str(packet), f'{w}x{h}', f'{len(marks)} marks')
