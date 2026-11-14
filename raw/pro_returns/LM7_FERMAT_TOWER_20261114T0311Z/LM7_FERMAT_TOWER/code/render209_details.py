"""Render every newly added E108--E110 proof page for actual visual review."""
from pathlib import Path
import hashlib
import json
import fitz

base=Path(__file__).resolve().parents[1]
pdf=base/'LM7_FERMAT_TOWER_paper.pdf'
document=fitz.open(pdf)
rows=[]
for page in range(587,607):
    image=document[page-1].get_pixmap(dpi=110,alpha=False)
    path=base/'qa'/('detail209_page_'+str(page)+'.jpg')
    image.save(path)
    rows.append({'page':page,'path':str(path.relative_to(base)),
                 'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
result={'status':'PASS','pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
        'pages':rows,'visual_review_claimed':False}
(base/'qa'/'detail209_manifest.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
