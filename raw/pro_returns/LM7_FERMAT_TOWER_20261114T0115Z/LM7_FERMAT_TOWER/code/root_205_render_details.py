"""Render the new proof pages and changed original-task summaries for review."""
from pathlib import Path
import hashlib
import json
import fitz

BASE=Path(__file__).resolve().parents[1]
PDF=BASE/'LM7_FERMAT_TOWER_paper.pdf'
digest=hashlib.sha256(PDF.read_bytes()).hexdigest()
assert digest=='21253d5b111c7825e82ef7e1c3d4a35a78b95d271708724c1af6b83a2b89227c'
doc=fitz.open(PDF)
pages=set(range(194,204))|set(range(564,582))
summary_pages=[]
for i,page in enumerate(doc):
    text=page.get_text()
    if i+1<240 and any(s in text for s in [
        'D.58 retains the entire D.57', 'E.107 now determines the previously']):
        pages.add(i+1);summary_pages.append(i+1)
records=[]
for number in sorted(pages):
    path=BASE/'qa'/f'detail205_page_{number:03d}.jpg'
    doc[number-1].get_pixmap(dpi=110,alpha=False).save(path,jpg_quality=90)
    records.append({'page':number,'path':str(path.relative_to(BASE)),
                    'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
result={'status':'PASS','pdf_sha256':digest,'dpi':110,'pages':records,
        'changed_summary_pages':summary_pages,'visual_review_claimed_by_program':False}
(BASE/'qa/detail205_manifest.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','pdf_sha256':digest,'rendered_pages':[r['page'] for r in records],
                  'changed_summary_pages':summary_pages,'visual_review_claimed_by_program':False},indent=2))
