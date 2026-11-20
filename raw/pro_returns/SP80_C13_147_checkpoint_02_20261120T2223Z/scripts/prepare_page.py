from pathlib import Path
import csv, shutil, sys
from PIL import Image

BASE=Path('/workspace/scratch/12caffedf246')
SRC=BASE/'source'
OUT=BASE/'edition'
for scan in map(int,sys.argv[1:]):
    stem=f'147_scan{scan:03d}'
    p=BASE/'packets'/stem
    p.mkdir(parents=True,exist_ok=True)
    im=Image.open(SRC/'SP80_C13_147_scans'/f'{stem}.jpg')
    w,h=im.size
    if not (p/'top.jpg').exists():
        if h>=w:
            im.crop((0,0,w,round(h*.55))).save(p/'top.jpg',quality=97)
            im.crop((0,round(h*.45),w,h)).save(p/'bottom.jpg',quality=97)
        else:
            im.crop((0,0,round(w*.55),h)).save(p/'top.jpg',quality=97)
            im.crop((round(w*.45),0,w,h)).save(p/'bottom.jpg',quality=97)
    shutil.copy2(SRC/'SP80_C13_147_scans'/f'{stem}.jpg',p/'page.jpg')
    shutil.copy2(SRC/'SP80_C13_147_texts/pages'/f'{stem}.tex',p/'C.tex')
    shutil.copy2(SRC/'SP80_C13_147_texts/hua'/f'hua_{stem}.tex',p/'H.tex')
    shutil.copy2(SRC/'SP80_C13_147_texts/PREAMBLE.tex',p/'PREAMBLE.tex')
    shutil.copy2(OUT/'notation.md',p/'notation.md')
    for source,dest,key,value in [
        (SRC/'SP80_C13_147_texts/MARKS.tsv','marks.tsv','scan',str(scan)),
        (SRC/'SP80_C13_147_C_H_differences.tsv','differences.tsv','page',stem)]:
        with source.open() as f:
            reader=csv.DictReader(f,delimiter='\t'); cols=reader.fieldnames
            rows=[r for r in reader if r[key]==value]
        with (p/dest).open('w') as f:
            writer=csv.DictWriter(f,fieldnames=cols,delimiter='\t'); writer.writeheader();writer.writerows(rows)
    print(stem, 'dimensions',w,h,'packet',p)
