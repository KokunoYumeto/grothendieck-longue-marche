#!/usr/bin/env python3
"""Render every ninth-hour addition and a distributed unchanged-page sample."""
from pathlib import Path
import json, fitz
from PIL import Image,ImageDraw
w=Path(__file__).resolve().parents[1]
qa=w/'qa/hour09'
qa.mkdir(exist_ok=True)
doc=fitz.open(w/'SECTIONS_OVER_Q_paper.pdf')
texts=[' '.join(p.get_text().split()) for p in doc]
part_b=next(i+1 for i,t in enumerate(texts) if i>200 and 'Part B. Sections and valuations' in t)
part_c=next(i+1 for i,t in enumerate(texts) if i>part_b and 'Part C. Cyclotomic fields and actions' in t)
new=next(i+1 for i,t in enumerate(texts) if i>250 and 'Arbitrary twists, constant local evaluations' in t)
two=next(i+1 for i,t in enumerate(texts) if i>=part_b and 'B.16.' in t)
samples=[1,2,20,28,38,48,54,59,63,67,69,72,75,77,80,82,84,87,90,104,107,111,128,145,161,178,195,212,229,246,263,283,291,299,304]
pages=sorted(set(samples+list(range(new,part_b+1))+list(range(two,part_c+1))+[len(doc)-26,len(doc)-14,len(doc)-7,len(doc)]))
paths=[]
for p in pages:
    path=qa/f'page_{p:03}.png'
    doc[p-1].get_pixmap(matrix=fitz.Matrix(1.35,1.35),alpha=False).save(path)
    paths.append(path)
parts=[]
for n,start in enumerate(range(0,len(pages),16),1):
    block=list(zip(pages[start:start+16],paths[start:start+16]))
    sheet=Image.new('RGB',(1720,640*((len(block)+3)//4)),'#e8e8e8')
    draw=ImageDraw.Draw(sheet)
    for j,(p,path) in enumerate(block):
        im=Image.open(path).convert('RGB');im.thumbnail((414,604))
        left=(j%4)*430+(430-im.width)//2;top=(j//4)*640+26
        sheet.paste(im,(left,top));draw.text(((j%4)*430+10,(j//4)*640+8),f'Page {p}',fill='black')
    part=qa/f'contact_part_{n}.png';sheet.save(part);parts.append(str(part.relative_to(w)))
former={}
for tag in ['A.128.1','A.128.22','A.130.S5','A.132.2']:
    former[tag]=[i+1 for i,t in enumerate(texts) if '('+tag+')' in t]
record={'pdf_pages':len(doc),'rendered_pages':pages,'new_result_pages':list(range(new,part_b+1)),'two_coefficient_pages':list(range(two,part_c+1)),'former_overflow_equations':former,'contact_parts':parts,'render_scale':1.35,'status':'Rendered; visual review pending.'}
for p in [w/'qa/render_record.json',qa/'render_record.json',w/'code/render_hour9_qa_output.txt']:p.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
