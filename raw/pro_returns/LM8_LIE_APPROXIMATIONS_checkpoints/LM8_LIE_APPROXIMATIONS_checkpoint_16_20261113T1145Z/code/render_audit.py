#!/usr/bin/env python3
"""Render an immutable PDF snapshot for visual review; never auto-approve it."""
from pathlib import Path
import hashlib,json,re,shutil,subprocess,sys,unicodedata
from PIL import Image,ImageOps,ImageDraw
from pypdf import PdfReader

root=Path(__file__).resolve().parents[1]
pdf=root/'LM8_LIE_APPROXIMATIONS_paper.pdf'
out=root.parent/'texbuild'/('qa_'+(sys.argv[1] if len(sys.argv)>1 else 'current'))
out.mkdir(parents=True,exist_ok=True)
snapshot=out/'paper.pdf'
shutil.copyfile(pdf,snapshot)
reader=PdfReader(snapshot)
pages=len(reader.pages)
texts=[p.extract_text() or '' for p in reader.pages]
def normalize(text):
    # PDF extraction may insert whitespace and discretionary hyphens.
    return ''.join(c for c in unicodedata.normalize('NFKD',text).casefold()
                   if c.isalnum())
normalized=[normalize(t) for t in texts]
anchors=json.loads((root/'audit/overflow_sources.json').read_text())
locations=[]
for anchor in anchors:
    choices=[anchor.get('current_text',anchor['text'])]+anchor.get('alternatives',[])
    hits=[i+1 for i,t in enumerate(normalized)
          if any(normalize(choice) in t for choice in choices)]
    if not hits:
        raise SystemExit('Former-overflow source cannot be located: '+anchor['id'])
    locations.append({**anchor,'pages':hits})
affected=sorted({p for item in locations for p in item['pages']})
new_statements=['A.19.','A.22.','A.23.','A.24.','A.25.','A.26.','B.14b.','B.14c.','B.14d.','B.24a.','B.24b.',
                'B.29.','B.30.','B.31.','B.32.','B.33.','B.34.','B.35.',
                'D.17.','D.18.','D.19.','D.20.',
                'D.21.','D.22.','D.23.','F.16.','F.17.','F.18.','F.19.','F.20.',
                'F.21.','F.22.','F.23.','F.24.','G.22.','G.23.','G.24.']
new_pages=[i+1 for i,t in enumerate(texts)
           if any(ident in t for ident in new_statements)]
selected=sorted(set([1,2,3,4,11,17,23,30,33,37,43,49,55,61,67,73,79,85,pages]
                    +affected+new_pages))
selected=[p for p in selected if p<=pages]
subprocess.run(['pdftoppm','-r','72','-png',str(snapshot),str(out/'page')],check=True,
               stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
raw=sorted(out.glob('page-*.png'))
contacts=[]
for first in range(0,pages,20):
    subset=raw[first:first+20]
    width,height=300,446
    sheet=Image.new('RGB',(4*width,5*height),'#e6e8eb')
    draw=ImageDraw.Draw(sheet)
    for j,path in enumerate(subset):
        picture=Image.open(path).convert('RGB')
        picture.thumbnail((284,414))
        x=(j%4)*width+(width-picture.width)//2
        y=(j//4)*height+22
        sheet.paste(picture,(x,y))
        draw.text(((j%4)*width+10,(j//4)*height+5),f'Page {first+j+1}',fill='black')
    name=out/f'contact_{first+1:03d}_{first+len(subset):03d}.png'
    sheet.save(name)
    contacts.append(str(name))
details=[]
for page in selected:
    stem=out/f'detail_{page:03d}'
    subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-singlefile',
                    '-scale-to','1600','-png',str(snapshot),str(stem)],check=True,
                    stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    details.append(str(stem)+'.png')
manifest={'pdf_sha256':hashlib.sha256(snapshot.read_bytes()).hexdigest(),
          'pages':pages,'renderer':'Poppler pdftoppm',
          'all_pages_rendered':True,'overflow_source_pages':affected,
          'former_overflow_locations':locations,
          'new_statement_pages':new_pages,
          'detail_pages':selected,'contact_sheets':contacts,'detail_images':details,
          'visual_review_status':'awaiting human/model image inspection'}
(out/'render_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
(root/'audit/render_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2),flush=True)
