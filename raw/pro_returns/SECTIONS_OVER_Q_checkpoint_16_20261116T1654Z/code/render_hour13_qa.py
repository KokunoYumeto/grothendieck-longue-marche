#!/usr/bin/env python3
"""Render every hour13 proof and coefficient page, prior repair, and samples."""
from pathlib import Path
import json
import fitz
from PIL import Image,ImageDraw

w=Path(__file__).resolve().parents[1]
qa=w/'qa/hour13';qa.mkdir(exist_ok=True)
old=w/'qa/visual_review.json';saved=w/'qa/visual_review_hour12.json'
if old.exists() and not saved.exists(): saved.write_bytes(old.read_bytes())
doc=fitz.open(w/'SECTIONS_OVER_Q_paper.pdf')
texts=[' '.join(p.get_text().split()) for p in doc]
start=next(i+1 for i,t in enumerate(texts) if i>400 and 'A.169. [Proved]' in t)
part_b=next(i+1 for i,t in enumerate(texts) if i>start and 'Part B. Sections and valuations' in t)
refs=next(i+1 for i,t in enumerate(texts) if i>part_b and 'References' in t)
samples=[1,2,3,4,5,6,7,20,38,54,69,82,104,128,145,178,195,229,246,283,299,305,317,325,347,351,365,377,395,402,410,416,422,425,431,440,447,455,458,465,466,470,472]
locations={}
for tag in ['A.160.2','A.169.1','A.169.18','A.170.4','A.171.1','A.171.15','A.172.19','A.172.23','A.172.24','A.173.5','A.173.14','A.174.4','A.175.7','A.175.10','A.175.14','A.175.18','A.176.4','A.176.13','A.177.1','A.177.7','A.177.13','A.179.1','A.179.3','A.179.9','A.179.14','A.179.17']:
    locations[tag]=[i+1 for i,t in enumerate(texts) if '('+tag+')' in t]
overflow_pages=[p for tag in ['A.160.2','A.179.1'] for p in locations[tag]]
pages=sorted(set(samples+overflow_pages+list(range(start,part_b+1))+[part_b+3,part_b+10,part_b+19,part_b+26]+list(range(refs,len(doc)+1))))
assert all(1<=p<=len(doc) for p in pages)
paths=[]
for p in pages:
    path=qa/f'page_{p:03}.png'
    doc[p-1].get_pixmap(matrix=fitz.Matrix(1.35,1.35),alpha=False).save(path)
    paths.append(path)
parts=[]
for number,offset in enumerate(range(0,len(pages),16),1):
    block=list(zip(pages[offset:offset+16],paths[offset:offset+16]))
    sheet=Image.new('RGB',(1720,640*((len(block)+3)//4)),'#e8e8e8')
    draw=ImageDraw.Draw(sheet)
    for j,(p,path) in enumerate(block):
        im=Image.open(path).convert('RGB');im.thumbnail((414,604))
        left=(j%4)*430+(430-im.width)//2;top=(j//4)*640+26
        sheet.paste(im,(left,top));draw.text(((j%4)*430+10,(j//4)*640+8),f'Page {p}',fill='black')
    path=qa/f'contact_part_{number}.png';sheet.save(path);parts.append(str(path.relative_to(w)))
record={'pdf_pages':len(doc),'rendered_pages':pages,'new_result_pages':list(range(start,part_b+1)),
        'equation_locations':locations,'prior_overflow_pages':overflow_pages,
        'reference_pages':list(range(refs,len(doc)+1)),'contact_parts':parts,
        'render_scale':1.35,'status':'Rendered; visual review pending.'}
out=json.dumps(record,indent=2)+'\n'
for path in [w/'qa/render_record.json',qa/'render_record.json',w/'code/render_hour13_qa_output.txt']:
    path.write_text(out)
print(out,end='')
