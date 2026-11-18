"""Render complete newly integrated result ranges and a distributed sample.

Rendering is not visual inspection. Actual image reads are separately recorded.
"""
from pathlib import Path
import re
import fitz
from PIL import Image, ImageDraw

root=Path(__file__).resolve().parents[1]
doc=fitz.open(root/'SECTION_GHOSTS_paper.pdf')
terms=['P.15']+[f'E.{n}' for n in range(203,214)]
starts={}
all_heads=[]
for i,page in enumerate(doc):
    for match in re.finditer(r'(?m)^([PABCDE]\.\d+)\.\s',page.get_text()):
        all_heads.append((i+1,match.group(1)))
for term in terms:
    starts[term]=[p for p,s in all_heads if s==term]
pages={1,2,3,4,25,60,100,140,180,220,260,300,len(doc)-1,len(doc)}
for term,hits in starts.items():
    for p in hits:
        later=[q for q,s in all_heads if q>p and s not in terms]
        end=min(later) if later else len(doc)
        pages.update(range(p,end+1))
pages=sorted(p for p in pages if 1<=p<=len(doc))
dest=root/'build/qa08';dest.mkdir(exist_ok=True)
for p in pages:
    page=doc[p-1]
    pix=page.get_pixmap(matrix=fitz.Matrix(1200/page.rect.height,1200/page.rect.height),alpha=False)
    pix.save(dest/f'page_{p:03}.png')
for k in range(0,len(pages),3):
    ims=[]
    for p in pages[k:k+3]:
        im=Image.open(dest/f'page_{p:03}.png').convert('RGB')
        frame=Image.new('RGB',(im.width,im.height+32),'#dddddd')
        frame.paste(im,(0,32))
        ImageDraw.Draw(frame).text((10,10),f'Page {p}',fill='black')
        ims.append(frame)
    out=Image.new('RGB',(sum(im.width for im in ims),max(im.height for im in ims)),'white')
    x=0
    for im in ims:
        out.paste(im,(x,0));x+=im.width
    out.save(dest/f'spread_{k//3+1:02}.png')
print('PDF pages:',len(doc))
print('Rendered pages:',pages)
print('Result heading matches:',starts)
print('Montages:',(len(pages)+2)//3)
print('Rendering is not visual inspection; actual image reads are recorded separately.')
