from pathlib import Path
from PIL import Image
import csv,json,sys
BASE=Path(__file__).resolve().parents[2]
SRC=BASE/'source'; OUT=BASE/'edition'; WORK=BASE/'work'
def packet(n):
    page=f'149_scan{n:03d}'
    dest=WORK/'packets'/page;dest.mkdir(parents=True,exist_ok=True)
    for src,name in [(SRC/f'SP84_C13_149_texts/pages/{page}.tex','C.tex'),(SRC/f'SP84_C13_149_texts/hua/hua_{page}.tex','H.tex'),(SRC/'SP84_C13_149_texts/PREAMBLE.tex','PREAMBLE.tex')]:
        (dest/name).write_bytes(src.read_bytes())
    for src,name,key,val in [(SRC/'SP84_C13_149_C_H_differences.tsv','differences.tsv','page',page),(SRC/'SP84_C13_149_texts/MARKS.tsv','marks.tsv','scan',str(n))]:
        with src.open() as f:
            # Supplied files are literal, unquoted TSV. A leading manuscript
            # quotation mark must not start a multiline CSV field.
            rr=csv.DictReader(f,delimiter='\t',quoting=csv.QUOTE_NONE); fields=rr.fieldnames; rows=[r for r in rr if r[key]==val]
        with (dest/name).open('w') as f:
            w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
    (dest/'notation.md').write_text((OUT/'notation_current.md').read_text())
    documentation=OUT/'documentation';documentation.mkdir(exist_ok=True)
    (documentation/f'notation_given_{n:03d}.md').write_text((dest/'notation.md').read_text())
    imgpath=SRC/f'SP84_C13_149_scans/{page}.jpg';im=Image.open(imgpath);w,h=im.size
    halves=[]
    boxes=[(0,0,w,int(h*.55)),(0,int(h*.45),w,h)] if h>=w else [(0,0,int(w*.55),h),(int(w*.45),0,w,h)]
    for i,box in enumerate(boxes,1):
        fn=WORK/f'halves/{page}_{i}.png'
        if not fn.exists(): im.crop(box).save(fn)
        halves.append({'path':str(fn),'box':box})
    info={'page':page,'scan':n,'image':str(imgpath),'size':[w,h],'halves':halves,'packet':str(dest)}
    (dest/'paths.json').write_text(json.dumps(info,indent=2))
    print(json.dumps(info))
if __name__=='__main__':
    for n in map(int,sys.argv[1:]):packet(n)
