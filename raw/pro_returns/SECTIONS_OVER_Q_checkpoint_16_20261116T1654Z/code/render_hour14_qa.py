#!/usr/bin/env python3
"""Render all hour-fourteen proof pages, corrected displays and distributed samples."""
from pathlib import Path
import json
import fitz
from PIL import Image, ImageDraw

w = Path(__file__).resolve().parents[1]
qa = w/'qa/hour14'
qa.mkdir(exist_ok=True)
old = w/'qa/visual_review.json'
saved = w/'qa/visual_review_hour13.json'
if old.exists() and not saved.exists():
    saved.write_bytes(old.read_bytes())
doc = fitz.open(w/'SECTIONS_OVER_Q_paper.pdf')
texts = [' '.join(page.get_text().split()) for page in doc]
start = next(i+1 for i,t in enumerate(texts) if i>400 and 'A.178. [Proved]' in t)
part_b = next(i+1 for i,t in enumerate(texts) if i>start and 'Part B. Sections and valuations' in t)
refs = next(i+1 for i,t in enumerate(texts) if i>part_b and 'References' in t)
samples = [1,2,3,4,5,6,7,20,38,54,69,82,104,128,145,178,195,229,246,
           283,299,305,317,325,347,351,365,377,395,402,410,416,422,425,
           431,440,447,455,458,465,466,470,472,480,488,496,504]
tags = ['A.160.2','A.166.3','A.178.1','A.178.8','A.178.14','A.179.1',
        'A.180.1','A.180.6','A.180.13','A.181.1','A.181.3','A.181.10',
        'A.181.17','A.181.23','A.182.3','A.182.13','A.182.17','A.182.23',
        'A.183.1','A.183.5','A.183.13','A.183.19','A.183.20','A.183.21',
        'A.184.2','A.184.6','A.184.9','A.184.14']
locations = {tag:[i+1 for i,t in enumerate(texts) if '('+tag+')' in t] for tag in tags}
overflow_tags = ['A.160.2','A.179.1','A.181.1']
corrections_path = w/'notes/hour14_typesetting_corrections.json'
if corrections_path.exists():
    corrections = json.loads(corrections_path.read_text())
    overflow_tags += [r['equation'] for r in corrections if r.get('equation')]
    for tag in overflow_tags:
        if tag not in locations:
            locations[tag] = [i+1 for i,t in enumerate(texts) if '('+tag+')' in t]
overflow_pages = sorted({p for tag in overflow_tags for p in locations[tag]})
edited_pages = locations['A.166.3']
pages = sorted(set(samples + overflow_pages + edited_pages + list(range(start,part_b+1))
                   + [part_b+3,part_b+10,part_b+19,part_b+26] + list(range(refs,len(doc)+1))))
assert all(1<=p<=len(doc) for p in pages)
paths = []
for p in pages:
    path = qa/f'page_{p:03}.png'
    doc[p-1].get_pixmap(matrix=fitz.Matrix(1.35,1.35),alpha=False).save(path)
    paths.append(path)
parts = []
for number,offset in enumerate(range(0,len(pages),16),1):
    block = list(zip(pages[offset:offset+16], paths[offset:offset+16]))
    sheet = Image.new('RGB',(1720,640*((len(block)+3)//4)),'#e8e8e8')
    draw = ImageDraw.Draw(sheet)
    for j,(p,path) in enumerate(block):
        im = Image.open(path).convert('RGB')
        im.thumbnail((414,604))
        left = (j%4)*430+(430-im.width)//2
        top = (j//4)*640+26
        sheet.paste(im,(left,top))
        draw.text(((j%4)*430+10,(j//4)*640+8),f'Page {p}',fill='black')
    path = qa/f'contact_part_{number}.png'
    sheet.save(path)
    parts.append(str(path.relative_to(w)))
record = {'pdf_pages':len(doc),'rendered_pages':pages,
          'new_result_pages':list(range(start,part_b+1)),
          'equation_locations':locations,'prior_overflow_pages':overflow_pages,
          'edited_frontier_pages':edited_pages,
          'reference_pages':list(range(refs,len(doc)+1)),
          'contact_parts':parts,'render_scale':1.35,
          'status':'Rendered; visual review pending.'}
out = json.dumps(record,indent=2)+'\n'
for path in [w/'qa/render_record.json', qa/'render_record.json', w/'code/render_hour14_qa_output.txt']:
    path.write_text(out)
print(out,end='')
