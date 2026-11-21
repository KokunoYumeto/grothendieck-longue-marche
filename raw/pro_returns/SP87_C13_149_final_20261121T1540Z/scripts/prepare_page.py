from pathlib import Path
import csv,json,sys
from PIL import Image
ROOT=Path('/workspace/scratch/b8c6ff258063')
OUT=ROOT/'SP87_C13_149_work'
SRC=ROOT/'source'
def prepare(scan):
    page=f'149_scan{scan:03d}'
    d=OUT/'readers'/page; d.mkdir(exist_ok=True)
    image=SRC/'SP87_C13_149_scans'/f'{page}.jpg'
    im=Image.open(image); w,h=im.size
    halves=ROOT/'halves'; halves.mkdir(exist_ok=True)
    boxes=[(0,0,w,round(h*.55)),(0,round(h*.45),w,h)] if h>=w else [(0,0,round(w*.55),h),(round(w*.45),0,w,h)]
    for label,box in zip(['top','bottom'] if h>=w else ['left','right'],boxes):
        f=halves/f'{page}_{label}.png'
        if not f.exists():im.crop(box).save(f)
    diffs=list(csv.DictReader((SRC/'SP87_C13_149_C_H_differences.tsv').open(),delimiter='\t'))
    diffs=[dict(diff_id=f'D{i+1:04d}',**x) for i,x in enumerate(diffs) if x['page']==page]
    marks=[x for x in csv.DictReader((SRC/'SP87_C13_149_texts/MARKS.tsv').open(),delimiter='\t') if int(x['scan'])==scan]
    packet={'scan':scan,'page':page,'image':str(image),'size':[w,h],'halves':[str(halves/f'{page}_{s}.png') for s in (['top','bottom'] if h>=w else ['left','right'])],'witness_C':(SRC/'SP87_C13_149_texts/pages'/f'{page}.tex').read_text(),'witness_H':(SRC/'SP87_C13_149_texts/hua'/f'hua_{page}.tex').read_text(),'differences':diffs,'marks':marks,'preamble':(SRC/'SP87_C13_149_texts/PREAMBLE.tex').read_text(),'notation_table':(OUT/'notation.md').read_text()}
    (d/'input.json').write_text(json.dumps(packet,ensure_ascii=False,indent=2))
    print(page,im.size,len(diffs),'diff rows',len(marks),'marks',d/'input.json')
if __name__=='__main__':
    for scan in map(int,sys.argv[1:]):prepare(scan)
