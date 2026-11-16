#!/usr/bin/env python3
"""Render twelfth-hour proofs, both literal tables, overflow pages and samples."""
from pathlib import Path
import json,fitz
from PIL import Image,ImageDraw
w=Path(__file__).resolve().parents[1]
qa=w/'qa/hour12';qa.mkdir(exist_ok=True)
old=w/'qa/visual_review.json';save=w/'qa/visual_review_hour11.json'
if old.exists() and not save.exists():save.write_bytes(old.read_bytes())
doc=fitz.open(w/'SECTIONS_OVER_Q_paper.pdf')
texts=[' '.join(p.get_text().split()) for p in doc]
start=next(i+1 for i,t in enumerate(texts) if i>300 and 'A.159. [Proved]' in t)
part_b=next(i+1 for i,t in enumerate(texts) if i>start and 'Part B. Sections and valuations' in t)
refs=next(i+1 for i,t in enumerate(texts) if i>part_b and 'References' in t)
samples=[1,2,3,4,5,6,7,20,38,54,69,82,104,128,145,178,195,229,246,283,299,305,317,325,347,351,365,377,395,402,410,416,422,425]
pages=sorted(set(samples+list(range(start,part_b+1))+[part_b+3,part_b+10,part_b+19,part_b+26]+list(range(refs,len(doc)+1))))
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
locations={}
for tag in ['A.159.1','A.159.C4','A.160.2','A.161.5','A.162.14','A.162.16','A.163.14','A.164.7','A.165.14','A.166.1','A.167.1']:
 locations[tag]=[i+1 for i,t in enumerate(texts) if '('+tag+')' in t]
record={'pdf_pages':len(doc),'rendered_pages':pages,
        'new_result_pages':list(range(start,part_b+1)),
        'equation_locations':locations,'reference_pages':list(range(refs,len(doc)+1)),
        'contact_parts':parts,'render_scale':1.35,'status':'Rendered; visual review pending.'}
out=json.dumps(record,indent=2)+'\n'
for p in [w/'qa/render_record.json',qa/'render_record.json',w/'code/render_hour12_qa_output.txt']:p.write_text(out)
print(out,end='')
