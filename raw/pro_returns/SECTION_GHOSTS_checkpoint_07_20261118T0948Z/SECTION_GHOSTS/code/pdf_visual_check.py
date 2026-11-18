#!/usr/bin/env python3
"""Render sample pages and the corrected-display pages for human/AI visual inspection."""
from pathlib import Path
import subprocess
from pypdf import PdfReader
from PIL import Image,ImageDraw
p=Path(__file__).resolve().parents[1]
r=PdfReader(p/'SECTION_GHOSTS_paper.pdf');q=p/'build/qa';q.mkdir(exist_ok=True)
fix=[]
for i,page in enumerate(r.pages):
 text=page.extract_text() or ''
 if any(term in text for term in ['(m, n, t)', '1085', 'Historical claim register', 'common-exponent obstruction', 'E.80.', 'E.81.', 'E.82.', 'E.83.', 'E.95.', 'E.96.', 'E.97.', 'E.98.', 'E.99.', 'E.100.', 'E.130.', 'E.131.', 'E.132.', 'E.133.', 'E.134.', 'E.135.', 'E.136.', 'E.137.', 'E.140.', 'E.141.', 'E.142.', 'E.143.', 'E.144.', 'E.145.']):
  fix.append(i+1)
ns=sorted(set([1,3,12,23,28,40,52,64,76,88,100,112,124,136,148,160,172,len(r.pages)]+fix))
ns=[n for n in ns if n<=len(r.pages)]
for n in ns:
 if n>len(r.pages):continue
 subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-scale-to','1200','-png','-singlefile',str(p/'SECTION_GHOSTS_paper.pdf'),str(q/f'page_{n:03}')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
for z in range(0,len(ns),3):
 ims=[]
 for n in ns[z:z+3]:
  im=Image.open(q/f'page_{n:03}.png').convert('RGB');frame=Image.new('RGB',(im.width,im.height+35),'#dddddd');frame.paste(im,(0,35));ImageDraw.Draw(frame).text((10,10),f'Page {n}',fill='black');ims.append(frame)
 out=Image.new('RGB',(sum(i.width for i in ims),max(i.height for i in ims)),'white');x=0
 for im in ims:out.paste(im,(x,0));x+=im.width
 out.save(q/f'spread_{z//3+1}.png')
print('PDF pages:',len(r.pages));print('Rendered pages:',ns);print('Corrected display matches:',fix)
print('Rendering completed; inspection is recorded separately in the report.')
