"""Render every paper page with Poppler and record structural PDF checks.

The temporary individual page PNGs live outside the deliverable directory.
Contact sheets and the machine-readable QA report are retained under qa/.
Visual review is a separate human-readable record; this program does not
assert that a model or person has inspected its images.
"""
from pathlib import Path
import csv
import hashlib
import json
import re
import subprocess
import fitz
from PIL import Image, ImageDraw, ImageFont

BASE=Path(__file__).resolve().parents[1]
PDF=BASE/'LM7_FERMAT_TOWER_paper.pdf'
QA=BASE/'qa'
TMP=BASE.parent/'.lm7_pdf_qa'
QA.mkdir(exist_ok=True)
TMP.mkdir(exist_ok=True)

def main():
    doc=fitz.open(PDF)
    pages=len(doc)
    # Poppler changes numeric padding at page100; discard old render names.
    for old_page in TMP.glob('page-*.png'):
        old_page.unlink()
    subprocess.run(['pdftoppm','-r','52','-png',str(PDF),str(TMP/'page')],check=True,
                   stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    files=sorted(TMP.glob('page-*.png'),key=lambda p:int(p.stem.split('-')[-1]))
    # Remove old rendered pages from a formerly longer build from consideration.
    files=[p for p in files if int(p.stem.split('-')[-1])<=pages]
    assert len(files)==pages
    headings={}
    outside=[]
    empty=[]
    for i,page in enumerate(doc):
        text=page.get_text()
        if len(text.strip())<10:empty.append(i+1)
        for block in page.get_text('dict')['blocks']:
            for line in block.get('lines',[]):
                spans=line['spans']
                rendered=''.join(s['text'] for s in spans)
                m=re.match(r'^([A-E]\.\d+)\.',rendered)
                if m and spans and spans[0]['flags'] & 16:
                    assert m.group(1) not in headings,(m.group(1),headings)
                    headings[m.group(1)]=i+1
        for word in page.get_text('words'):
            x0,y0,x1,y1=word[:4]
            if x0<12 or y0<12 or x1>page.rect.width-12 or y1>page.rect.height-12:
                outside.append({'page':i+1,'word':word[4],'bbox':list(word[:4])})
    with (BASE/'LM7_FERMAT_TOWER_results.csv').open() as f:
        ids={r['id'] for r in csv.DictReader(f)}
    missing=sorted(ids-set(headings))
    assert not missing,missing
    assert not outside,outside
    assert not empty,empty
    contact_paths=[]
    cellw,cellh=310,470
    for old_contact in QA.glob('contact_*.jpg'):
        old_contact.unlink()
    for start in range(0,pages,16):
        rows=(min(16,pages-start)+3)//4
        canvas=Image.new('RGB',(4*cellw,rows*cellh),'#e8e8e8')
        draw=ImageDraw.Draw(canvas)
        for offset,path in enumerate(files[start:start+16]):
            im=Image.open(path).convert('RGB')
            im.thumbnail((cellw-12,cellh-27))
            x=(offset%4)*cellw+(cellw-im.width)//2
            y=(offset//4)*cellh+22
            canvas.paste(im,(x,y))
            draw.text(((offset%4)*cellw+8,(offset//4)*cellh+5),
                      f'Page {start+offset+1}',fill='black')
        path=QA/f'contact_{start+1:03d}_{min(start+16,pages):03d}.jpg'
        canvas.save(path,quality=88)
        contact_paths.append(str(path.relative_to(BASE)))
    result={'pdf':PDF.name,'sha256':hashlib.sha256(PDF.read_bytes()).hexdigest(),
            'pages':pages,'bytes':PDF.stat().st_size,'metadata':doc.metadata,
            'all_statement_headings_present':True,'statement_pages':headings,
            'empty_pages':empty,'text_outside_page_safety_border':outside,
            'all_pages_rendered_with':'pdftoppm -r 52 -png',
            'contact_sheets':contact_paths,'individual_render_directory':str(TMP),
            'visual_review_claimed_by_program':False}
    (QA/'pdf_qa.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('metadata','statement_pages')},indent=2))

if __name__=='__main__':main()
