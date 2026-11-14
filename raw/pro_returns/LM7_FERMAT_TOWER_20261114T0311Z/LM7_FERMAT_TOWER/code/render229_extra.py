"""Render the three additional E.23 boundary pages; retain the prior manifest."""
from pathlib import Path
import hashlib,json,subprocess

BASE=Path(__file__).resolve().parents[1]
PDF=BASE/'LM7_FERMAT_TOWER_paper.pdf';QA=BASE/'qa'
EXPECTED='f6307cb0c8d6ad23873f51fe60ce306d9c73f0bc89ae30702fa6c4e0dd5b10af'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(PDF)==EXPECTED
mp=QA/'detail229_manifest.json'
before=mp.read_bytes(); record=json.loads(before)
assert len(record['images'])==37 and record['pdf_sha256']==EXPECTED
hp=QA/'history'/'detail229_before_extra_manifest.json'
assert not hp.exists()
hp.parent.mkdir(parents=True,exist_ok=True);hp.write_bytes(before)
for page in (276,277,278):
    prefix=QA/f'detail229_{page:03d}'
    p=subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-singlefile',
                      '-r','110','-jpeg','-jpegopt','quality=93',str(PDF),str(prefix)],
                     capture_output=True,check=True)
    assert not p.stdout and not p.stderr
    path=prefix.with_suffix('.jpg')
    record['images'].append({'page':page,'path':str(path.relative_to(BASE)),
                            'bytes':path.stat().st_size,'sha256':sha(path)})
record['images'].sort(key=lambda x:x['page'])
assert len(record['images'])==40
record['previous_manifest']={'path':str(hp.relative_to(BASE)),'sha256':sha(hp)}
mp.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':'PASS','additional_pages':[276,277,278],
                  'total_detail_images':40,'manifest_sha256':sha(mp)},indent=2))
