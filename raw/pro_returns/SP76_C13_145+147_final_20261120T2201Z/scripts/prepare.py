from pathlib import Path
from PIL import Image
import csv, json

ROOT=Path('/workspace/scratch/3933aa5dedf2')
SRC=ROOT/'source'
WORK=ROOT/'work'
PACKETS=ROOT/'packets'
PACKETS.mkdir(exist_ok=True)
marks=list(csv.DictReader((SRC/'SP76_C13_145+147_texts/MARKS.tsv').open(),delimiter='\t'))
diffs=list(csv.DictReader((SRC/'SP76_C13_145+147_C_H_differences.tsv').open(),delimiter='\t',quoting=csv.QUOTE_NONE))
pages=[p.stem for p in sorted((SRC/'SP76_C13_145+147_scans').glob('*.jpg'))]
(WORK/'page_order.txt').write_text('\n'.join(pages)+'\n')
for page in pages:
    dest=PACKETS/page
    dest.mkdir(exist_ok=True)
    cote,scan=page.split('_scan')
    source=SRC/'SP76_C13_145+147_scans'/f'{page}.jpg'
    img=Image.open(source)
    w,h=img.size
    if not (dest/'top.png').exists():
        if w<=h:
            img.crop((0,0,w,round(h*.55))).save(dest/'top.png')
            img.crop((0,round(h*.45),w,h)).save(dest/'bottom.png')
        else:
            img.crop((0,0,round(w*.55),h)).save(dest/'top.png')
            img.crop((round(w*.45),0,w,h)).save(dest/'bottom.png')
    m=[r for r in marks if r['cote']==cote and int(r['scan'])==int(scan)]
    d=[r for r in diffs if r['page']==page]
    text=f'# Page {page}\n\nOriginal image: {source}\nDimensions: {w} x {h}.\nFull-resolution overlapping halves: {dest}/top.png and {dest}/bottom.png.\n\n## Witness C\n\n```latex\n'+(SRC/'SP76_C13_145+147_texts/pages'/f'{page}.tex').read_text()+'\n```\n\n## Witness H\n\n```latex\n'+(SRC/'SP76_C13_145+147_texts/hua'/f'hua_{page}.tex').read_text()+'\n```\n\n## C/H differences (script candidates; discard pure macro/editorial differences)\n\n'+json.dumps(d,ensure_ascii=False,indent=2)+'\n\n## C marks\n\n'+json.dumps(m,ensure_ascii=False,indent=2)+'\n'
    (dest/'input.md').write_text(text)
print(f'Prepared {len(pages)} page packets; {len(marks)} original marks; {len(diffs)} candidate C/H differences.')
