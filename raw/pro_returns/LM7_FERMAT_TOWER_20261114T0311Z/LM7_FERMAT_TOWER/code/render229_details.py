"""Render changed pages and proof boundaries for actual visual inspection."""
from pathlib import Path
import hashlib,json,subprocess

BASE=Path(__file__).resolve().parents[1]
PDF=BASE/'LM7_FERMAT_TOWER_paper.pdf';QA=BASE/'qa'
EXPECTED='f6307cb0c8d6ad23873f51fe60ce306d9c73f0bc89ae30702fa6c4e0dd5b10af'
PAGES=sorted({1,2,42,46,47,51,55,56,269,273,274,275,740,748,
              *range(250,258),*range(724,739)})
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(PDF)==EXPECTED
images=[]
for page in PAGES:
    prefix=QA/f'detail229_{page:03d}'
    p=subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-singlefile',
                      '-r','110','-jpeg','-jpegopt','quality=93',str(PDF),str(prefix)],
                     capture_output=True,check=True)
    assert not p.stdout and not p.stderr
    path=prefix.with_suffix('.jpg')
    images.append({'page':page,'path':str(path.relative_to(BASE)),
                   'bytes':path.stat().st_size,'sha256':sha(path)})
record={'pdf':PDF.name,'pdf_sha256':EXPECTED,'dpi':110,'renderer':'pdftoppm',
        'images':images,'visual_review_claimed_by_program':False}
(QA/'detail229_manifest.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
