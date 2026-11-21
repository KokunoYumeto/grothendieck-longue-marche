from pathlib import Path
import csv,sys,shutil,json
from PIL import Image
ROOT=Path('/workspace/scratch/0cab6a548abb')
SRC=ROOT/'source'; OUT=ROOT/'edition'
def prepare(n):
    page=f'149_scan{n:03d}'
    packet=ROOT/'packets'/page; packet.mkdir(exist_ok=True)
    source=SRC/'SP88_C13_149_scans'/f'{page}.jpg'
    image=Image.open(source); w,h=image.size
    for name,box in [('top',(0,0,w,round(h*.55))),('bottom',(0,round(h*.45),w,h))]:
        dest=ROOT/'halves'/f'{page}_{name}.png'
        if not dest.exists():image.crop(box).save(dest)
        link=packet/f'{name}.png'
        if not link.exists():link.symlink_to(dest)
    link=packet/'full.jpg'
    if not link.exists():link.symlink_to(source)
    shutil.copyfile(SRC/'SP88_C13_149_texts/pages'/f'{page}.tex',packet/'C.tex')
    shutil.copyfile(SRC/'SP88_C13_149_texts/hua'/f'hua_{page}.tex',packet/'H.tex')
    for src,dest,key,value in [(SRC/'SP88_C13_149_C_H_differences.tsv','differences.tsv','page',page),(SRC/'SP88_C13_149_texts/MARKS.tsv','marks.tsv','scan',str(n))]:
        with src.open() as f:
            reader=csv.DictReader(f,delimiter='\t'); rows=[r for r in reader if r[key]==value]
            with (packet/dest).open('w') as g:
                writer=csv.DictWriter(g,reader.fieldnames,delimiter='\t');writer.writeheader();writer.writerows(rows)
    (packet/'notation_at_assignment.md').write_text((OUT/'SP88_C13_149_doubts.md').read_text().split('## Remaining doubts')[0])
    documentation=OUT/'review/assignment_documentation'; documentation.mkdir(exist_ok=True)
    snapshot=documentation/f'{page}_notation_at_assignment.md'
    if not snapshot.exists():shutil.copyfile(packet/'notation_at_assignment.md',snapshot)
    print(packet)
for n in map(int,sys.argv[1:]):prepare(n)
