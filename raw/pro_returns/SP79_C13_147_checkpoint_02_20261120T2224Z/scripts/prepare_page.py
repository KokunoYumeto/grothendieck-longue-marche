from pathlib import Path
from PIL import Image
import csv, shutil, sys

WORK=Path(__file__).resolve().parents[1]
BASE=WORK.parents[1]
SOURCE=BASE/'source'

def prepare(n):
    stem=f'147_scan{n:03d}'
    packet=WORK/'packets'/stem
    packet.mkdir(exist_ok=True)
    for src,name in [(SOURCE/'SP79_C13_147_texts/pages'/f'{stem}.tex','C.tex'),(SOURCE/'SP79_C13_147_texts/hua'/f'hua_{stem}.tex','H.tex'),(SOURCE/'SP79_C13_147_texts/PREAMBLE.tex','PREAMBLE.tex'),(WORK/'notation.md','notation.md')]:
        shutil.copyfile(src,packet/name)
    for src,name,key,value in [(SOURCE/'SP79_C13_147_texts/MARKS.tsv','marks.tsv','scan',str(n)),(SOURCE/'SP79_C13_147_C_H_differences.tsv','differences.tsv','page',stem)]:
        with src.open() as f:
            r=csv.DictReader(f,delimiter='\t',quoting=csv.QUOTE_NONE)
            fields=r.fieldnames
            rows=[row for row in r if row[key]==value]
        with (packet/name).open('w') as f:
            w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
    image=SOURCE/'SP79_C13_147_scans'/f'{stem}.jpg'
    link=packet/'page.jpg'
    if not link.exists(): link.symlink_to(image)
    if not (packet/'top.jpg').exists():
        im=Image.open(image);w,h=im.size
        if h>=w:
            im.crop((0,0,w,round(h*.55))).save(packet/'top.jpg',quality=98)
            im.crop((0,round(h*.45),w,h)).save(packet/'bottom.jpg',quality=98)
        else:
            im.crop((0,0,round(w*.55),h)).save(packet/'top.jpg',quality=98)
            im.crop((round(w*.45),0,w,h)).save(packet/'bottom.jpg',quality=98)
        (packet/'image_geometry.txt').write_text(f'Original size {w} x {h}; halves overlap by 10 percent. All boxes use original image coordinates.\n')
    print(packet)

if __name__=='__main__':
    for n in map(int,sys.argv[1:]): prepare(n)
