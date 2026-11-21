from pathlib import Path
from PIL import Image
import csv,json,sys
ROOT=Path('/workspace/scratch/8759b8008681')
SRC=ROOT/'source';WORK=ROOT/'work'
def prepare(page):
 dest=ROOT/'packets'/page;dest.mkdir(parents=True,exist_ok=True)
 source=SRC/'SP89_C13_149+150_scans'/f'{page}.jpg'
 im=Image.open(source);w,h=im.size
 half=ROOT/'halves'
 if w>h: boxes=[(0,0,round(w*.55),h),(round(w*.45),0,w,h)]
 else: boxes=[(0,0,w,round(h*.55)),(0,round(h*.45),w,h)]
 for i,b in enumerate(boxes,1):
  target=half/f'{page}_half{i}.png'
  if not target.exists(): im.crop(b).save(target)
 for name,content in [('C.tex',(SRC/'SP89_C13_149+150_texts/pages'/f'{page}.tex').read_text()),('H.tex',(SRC/'SP89_C13_149+150_texts/hua'/f'hua_{page}.tex').read_text()),('notation.md',(WORK/'notation.md').read_text()),('PREAMBLE.tex',(SRC/'SP89_C13_149+150_texts/PREAMBLE.tex').read_text())]: (dest/name).write_text(content)
 for f,match,out in [('SP89_C13_149+150_C_H_differences.tsv',lambda r:r['page']==page,'differences.tsv'),('SP89_C13_149+150_texts/MARKS.tsv',lambda r:f"{r['cote']}_scan{int(r['scan']):03d}"==page,'marks.tsv')]:
  with (SRC/f).open() as fp:
   rd=csv.DictReader(fp,delimiter='\t',quoting=csv.QUOTE_NONE if out=='differences.tsv' else csv.QUOTE_MINIMAL);rows=[r for r in rd if match(r)]
   with (dest/out).open('w') as op:
    wr=csv.DictWriter(op,fieldnames=rd.fieldnames,delimiter='\t');wr.writeheader();wr.writerows(rows)
 (WORK/'reports'/page).mkdir(exist_ok=True)
 print(page,'image=',source,'halves=',str(half/f'{page}_half1.png'),str(half/f'{page}_half2.png'))
for p in sys.argv[1:]:prepare(p)
