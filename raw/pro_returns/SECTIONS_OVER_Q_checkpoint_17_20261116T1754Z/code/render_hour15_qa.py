#!/usr/bin/env python3
"""Render every new proof page, the repaired overflow, and distributed samples."""
from pathlib import Path
import json, hashlib
import fitz
from PIL import Image, ImageDraw

w=Path(__file__).resolve().parents[1]
qa=w/'qa/hour15'
qa.mkdir(exist_ok=True)
old=w/'qa/visual_review.json'
saved=w/'qa/visual_review_hour14.json'
if old.exists() and not saved.exists():saved.write_bytes(old.read_bytes())
doc=fitz.open(w/'SECTIONS_OVER_Q_paper.pdf')
texts=[' '.join(p.get_text().split()) for p in doc]
def locations(tag):return [i+1 for i,t in enumerate(texts) if tag in t]
start=next(p for p in locations('A.185. [Proved]') if p>400)
part_b=next(i+1 for i,t in enumerate(texts) if i+1>start and 'Part B. Sections and valuations' in t)
refs=next(i+1 for i,t in enumerate(texts) if i+1>part_b and 'References' in t)
samples=[1,2,3,4,5,6,7,20,54,82,104,128,145,178,195,229,246,
         283,305,317,347,351,377,395,410,422,440,447,465,470,488,504]
tags=['A.185.1','A.185.7','A.186.15','A.186.18','A.186.20',
      'A.187.10','A.187.13','A.188.4','A.188.5','A.188.7',
      'A.189.8','A.189.10','A.189.14','A.190.2','A.190.5','A.190.9',
      'A.190.11','A.191.7','A.191.8','A.191.9']
eq={tag:locations('('+tag+')') for tag in tags}
corrections=json.loads((w/'notes/hour15_typesetting_corrections.json').read_text())
overflow=sorted({p for r in corrections for p in locations(r['anchor']) if p>400})
assert overflow
old_full=[4,437,440,525,532,540,543,547,548]
new_full=[eq[tag][0] for tag in ['A.185.1','A.186.20','A.189.8','A.190.11','A.191.7']]
if locations('A.192. [Proved]'):
    new_full+=locations('A.192. [Proved]')
required_full=sorted(set(old_full+overflow+new_full))
pages=sorted(set(samples+required_full+list(range(start,part_b+1))+
                 [part_b+3,part_b+10,part_b+19,part_b+26]+list(range(refs,len(doc)+1))))
assert all(1<=p<=len(doc) for p in pages)
paths=[]
for p in pages:
    path=qa/f'page_{p:03d}.png'
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
        sheet.paste(im,(left,top))
        draw.text(((j%4)*430+10,(j//4)*640+8),f'Page {p}',fill='black')
    path=qa/f'contact_part_{number}.png';sheet.save(path)
    parts.append(str(path.relative_to(w)))
record={'pdf_pages':len(doc),'pdf_sha256':hashlib.sha256((w/'SECTIONS_OVER_Q_paper.pdf').read_bytes()).hexdigest(),'rendered_pages':pages,
        'new_result_pages':list(range(start,part_b+1)),
        'equation_locations':eq,'prior_overflow_pages':overflow,
        'earlier_full_resolution_locations':old_full,
        'required_full_resolution_pages':required_full,
        'reference_pages':list(range(refs,len(doc)+1)),
        'contact_parts':parts,'render_scale':1.35,
        'status':'Rendered; actual visual review pending.'}
out=json.dumps(record,indent=2)+'\n'
for p in [w/'qa/render_record.json',qa/'render_record.json',w/'code/render_hour15_qa_output.txt']:
    p.write_text(out)
print(out,end='')
