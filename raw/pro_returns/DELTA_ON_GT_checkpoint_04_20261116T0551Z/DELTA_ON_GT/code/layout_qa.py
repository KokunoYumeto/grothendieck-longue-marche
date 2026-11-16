"""Render specified one-based PDF pages and a contact sheet for visual review.

Rendering is a preparation for inspection, not an automated claim of visual QA.
Use --tag to retain each independent review's images without overwriting them.
"""
from pathlib import Path
import argparse,json
import fitz
from PIL import Image,ImageDraw
p=argparse.ArgumentParser();p.add_argument('--pages',required=True)
p.add_argument('--tag',required=True);a=p.parse_args()
root=Path(__file__).resolve().parents[1]
dest=root/'records'/('pdf_qa_'+a.tag);dest.mkdir(parents=True,exist_ok=False)
doc=fitz.open(root/'DELTA_ON_GT_paper.pdf')
pages=sorted(set(int(x) for x in a.pages.split(',')))
thumbs=[]
for n in pages:
    assert 1<=n<=len(doc)
    pix=doc[n-1].get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False)
    path=dest/f'page_{n:03d}.png';pix.save(path)
    im=Image.open(path);im.thumbnail((420,595))
    tile=Image.new('RGB',(440,630),'#eeeeee');tile.paste(im,((440-im.width)//2,24))
    ImageDraw.Draw(tile).text((15,8),f'Page {n}',fill='black');thumbs.append(tile)
cols=4;rows=(len(thumbs)+cols-1)//cols
sheet=Image.new('RGB',(cols*440,rows*630),'white')
for i,im in enumerate(thumbs):sheet.paste(im,((i%cols)*440,(i//cols)*630))
sheet.save(dest/'contact_sheet.png')
meta={'pdf_pages':len(doc),'rendered_pages':pages,'tag':a.tag,'visual_review':'pending'}
(dest/'render_record.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta))
