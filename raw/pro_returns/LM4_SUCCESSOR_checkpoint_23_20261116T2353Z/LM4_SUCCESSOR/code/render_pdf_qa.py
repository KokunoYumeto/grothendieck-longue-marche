"""Render specified one-based PDF pages and numbered nine-page contact sheets.

Usage: python3 code/render_pdf_qa.py --out records/pdf_qa/checkpoint03 \
       --pages 1,22-27,67-84,100,119,141
Rendering supplies images for human/model visual inspection; it is not an
automatic claim that the document layout has passed review.
"""
from pathlib import Path
import argparse,json,math
import fitz
from PIL import Image,ImageDraw
P=Path(__file__).resolve().parents[1]
a=argparse.ArgumentParser();a.add_argument('--out',required=True);a.add_argument('--pages',required=True)
a.add_argument('--pdf',default='LM4_SUCCESSOR_paper.pdf');o=a.parse_args()
pdf=fitz.open(P/o.pdf);pages=set()
for item in o.pages.split(','):
 if '-' in item:
  lo,hi=map(int,item.split('-'));pages.update(range(lo,hi+1))
 else:pages.add(int(item))
pages=sorted(pages);assert all(1<=n<=len(pdf) for n in pages)
out=P/o.out;out.mkdir(parents=True,exist_ok=True)
for n in pages:
 pix=pdf[n-1].get_pixmap(matrix=fitz.Matrix(1.6,1.6),alpha=False)
 pix.save(out/f'page-{n:03}.png')
for start in range(0,len(pages),9):
 block=pages[start:start+9];w,h=330,490
 sheet=Image.new('RGB',(3*w,math.ceil(len(block)/3)*h),'#d9d9d9');d=ImageDraw.Draw(sheet)
 for k,n in enumerate(block):
  im=Image.open(out/f'page-{n:03}.png');im.thumbnail((w-12,h-27))
  x=(k%3)*w+(w-im.width)//2;y=(k//3)*h+22
  sheet.paste(im,(x,y));d.text(((k%3)*w+10,(k//3)*h+5),f'Page {n}',fill='black')
 sheet.save(out/f'contact-{start//9+1:02}.png')
(out/'render_manifest.json').write_text(json.dumps({'pdf':o.pdf,'page_count':len(pdf),'rendered_pages':pages},indent=2)+'\n')
print('Rendered',len(pages),'pages from',len(pdf),'to',out)
