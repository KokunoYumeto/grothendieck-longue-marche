from pathlib import Path
from PIL import Image
import csv, json, shutil, sys

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / 'source'
ED = ROOT / 'edition'
scan = int(sys.argv[1])
stem = f'145_scan{scan:03d}'
packet = ROOT / 'packets' / stem
packet.mkdir(exist_ok=True)
image_path = SRC / 'SP75_C13_145_scans' / (stem+'.jpg')
shutil.copyfile(image_path, packet/'page.jpg')
shutil.copyfile(SRC/'SP75_C13_145_texts/pages'/(stem+'.tex'), packet/'C.tex')
shutil.copyfile(SRC/'SP75_C13_145_texts/hua'/('hua_'+stem+'.tex'), packet/'H.tex')
shutil.copyfile(SRC/'SP75_C13_145_texts/PREAMBLE.tex', packet/'PREAMBLE.tex')
shutil.copyfile(ROOT/'reader_guidance.md', packet/'guidance.md')
shutil.copyfile(ED/'notation.md', packet/'notation.md')
for source,target,key,value in [('SP75_C13_145_texts/MARKS.tsv','marks.tsv','scan',str(scan)),('SP75_C13_145_C_H_differences.tsv','differences.tsv','page',stem)]:
    with (SRC/source).open() as f:
        # The supplied lists are literal TSV: quote characters are manuscript tokens.
        reader=csv.DictReader(f,delimiter='\t',quoting=csv.QUOTE_NONE); fields=reader.fieldnames
        rows=[r for r in reader if r[key]==value]
    with (packet/target).open('w') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t'); w.writeheader(); w.writerows(rows)
im=Image.open(image_path); width,height=im.size
if height>=width:
    boxes=[(0,0,width,round(height*.55)),(0,round(height*.45),width,height)]
else:
    boxes=[(0,0,round(width*.55),height),(round(width*.45),0,width,height)]
for label,box in zip(['top','bottom'],boxes):
    dest=ROOT/'halves'/(stem+'_'+label+'.png')
    if not dest.exists(): im.crop(box).save(dest)
    shutil.copyfile(dest,packet/(label+'.png'))
(packet/'geometry.json').write_text(json.dumps({'scan':scan,'size':[width,height],'half_boxes':boxes},indent=2))
print(packet)
