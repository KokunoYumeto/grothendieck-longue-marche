"""Render new proofs, formerly overflowing tables, and distributed samples.

Rendering is not visual inspection. The inspection field is completed
only after the emitted images have actually been viewed.
"""
from pathlib import Path
import fitz, json, re
from PIL import Image, ImageDraw
W=Path(__file__).resolve().parents[1]
out=W/'qa_pages'; out.mkdir(exist_ok=True)
d=fitz.open(W/'ANABELIAN_A1_SUCCESSOR_paper.pdf')
texts=[re.sub(r'\s+',' ',p.get_text()) for p in d]
starts={}
for i,t in enumerate(texts):
    for ident in re.findall(r'\b([ABC]\.[0-9]+)\. (?:Proved|Known|False as stated|Open)\.',t):
        starts.setdefault(ident,i)
selected=['A.60','A.61','B.52']
selected += [f'B.{n}' for n in range(139,148)]
pages={0,2,4,len(d)//4,len(d)//2,3*len(d)//4,len(d)-1}
pages.update(range(24,len(d),25))
proof_pages={}
ordered=sorted(set(starts.values()))
for ident in selected:
    if ident not in starts: continue
    first=starts[ident]
    later=[x for x in ordered if x>first]
    last=min(later) if later else first
    last=min(last,first+14)
    proof_pages[ident]=list(range(first+1,last+2))
    pages.update(range(first,last+1))
terms=['with the fixed vectors of','Step Opened predecessor','Source locus Use of the fibre input',
       'Locus Condition or use','Definition 1.18','The remaining full CM',
       'The complete cyclic-seven rational-branch exclusion',
       'Targeted primary-source audit','An exact answer for products']
hits={term:[] for term in terms}
for i,t in enumerate(texts):
    for term in terms:
        if term in t:
            hits[term].append(i+1)
            pages.update(range(i,min(i+2,len(d))))
pages=sorted(pages)
for i in pages:
    pix=d[i].get_pixmap(matrix=fitz.Matrix(1.2,1.2),alpha=False)
    pix.save(out/f'page_{i+1:03d}.png')
contacts=[]
for batch in range((len(pages)+5)//6):
    subset=pages[batch*6:(batch+1)*6]
    canvas=Image.new('RGB',(1500,3240),'#d8d8d8'); draw=ImageDraw.Draw(canvas)
    for j,i in enumerate(subset):
        im=Image.open(out/f'page_{i+1:03d}.png'); im.thumbnail((730,1030))
        x=(j%2)*750+10; y=(j//2)*1080+30
        canvas.paste(im,(x,y)); draw.text((x,y-20),f'PDF page {i+1}',fill='black')
    path=out/f'contact_{batch+1}.png'; canvas.save(path)
    contacts.append({'file':str(path),'pages':[i+1 for i in subset]})
report={'pages':len(d),'rendered_pages':[i+1 for i in pages],
        'proof_pages':proof_pages,'former_overflow_and_sample_terms':hits,
        'contact_sheets':contacts,
        'visual_inspection':'Awaiting actual image inspection; not inferred from rendering'}
(W/'notes/PDF_QA.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
