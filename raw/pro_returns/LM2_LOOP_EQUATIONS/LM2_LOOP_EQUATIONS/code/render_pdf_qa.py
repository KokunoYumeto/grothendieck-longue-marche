#!/usr/bin/env python3
"""Render every PDF page and make contact sheets for visual inspection.

Requires PyMuPDF and Pillow. Images are build intermediates, not figures in
the mathematical paper. A text bounding-box check detects obvious clipping;
human/model visual inspection remains necessary and was performed for the
distributed PDF.
"""
from pathlib import Path
import json
import math
import fitz
from PIL import Image, ImageOps, ImageDraw

ROOT=Path(__file__).resolve().parents[1]
pdf=ROOT/'LM2_LOOP_EQUATIONS_paper.pdf'
destination=ROOT/'.build'/'qa'
destination.mkdir(parents=True,exist_ok=True)
doc=fitz.open(pdf)
thumbs=[];outside=[];empty=[]
for i,page in enumerate(doc):
    pix=page.get_pixmap(matrix=fitz.Matrix(1.45,1.45),alpha=False)
    output=destination/f'page-{i+1:02d}.png';pix.save(output)
    im=Image.open(output).convert('RGB')
    im.thumbnail((285,405))
    card=Image.new('RGB',(305,440),'#e9edf0')
    card.paste(im,((305-im.width)//2,22))
    ImageDraw.Draw(card).text((10,5),f'Page {i+1}',fill='black')
    thumbs.append(card)
    words=page.get_text('words')
    if not words:empty.append(i+1)
    for x0,y0,x1,y1,word,*_ in words:
        if x0<0 or y0<0 or x1>page.rect.width or y1>page.rect.height:
            outside.append({'page':i+1,'word':word,'box':[x0,y0,x1,y1]})
for start in range(0,len(thumbs),16):
    batch=thumbs[start:start+16]
    sheet=Image.new('RGB',(4*305,math.ceil(len(batch)/4)*440),'#d6dce0')
    for j,card in enumerate(batch):sheet.paste(card,((j%4)*305,(j//4)*440))
    sheet.save(destination/f'contact-{start//16+1}.png')
result={'pdf_pages':len(doc),'all_pages_rendered':True,
        'empty_pages':empty,'text_outside_page':outside,
        'contact_sheets':math.ceil(len(doc)/16),
        'render_directory':'.build/qa',
        'note':'No off-page text is a necessary check, not a proof of good layout.'}
(ROOT/'code'/'render_pdf_qa.json').write_text(json.dumps(result,indent=2)+'\n')
assert not empty and not outside,result
print(json.dumps(result,indent=2))
