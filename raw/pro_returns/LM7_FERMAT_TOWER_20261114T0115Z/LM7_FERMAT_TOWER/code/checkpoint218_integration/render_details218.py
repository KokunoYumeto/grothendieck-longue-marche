#!/usr/bin/env python3
"""Render the new proofs, bibliography and changed prose samples; claim no viewing."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import subprocess

base=Path(__file__).resolve().parents[2]
pdf=base/'LM7_FERMAT_TOWER_paper.pdf'
qa=base/'qa'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(pdf)=='792de5e54e0b7513bb3d006bbc76d046b0b636aec16572a622254e179a721899'
pages=list(range(216,223))+[619,626,636]+list(range(641,668))
def render(n):
    prefix=qa/f'detail218_page_{n}'
    run=subprocess.run(['pdftoppm','-r','110','-jpeg','-singlefile','-f',str(n),'-l',str(n),str(pdf),str(prefix)],capture_output=True)
    assert run.returncode==0,run.stderr.decode()
    p=prefix.with_suffix('.jpg')
    return {'page':n,'path':str(p.relative_to(base)),'sha256':sha(p),'bytes':p.stat().st_size}
with ThreadPoolExecutor(max_workers=4) as pool:images=list(pool.map(render,pages))
result={'status':'RENDERED_FOR_REVIEW','pdf_sha256':sha(pdf),'pages':pages,'images':images,
        'scope':'Entire D61 proof; entire E115,E116,E118 proofs and bibliography; prose-spacing samples at E111,E112,E114 openings.',
        'visual_review_claimed_by_program':False}
(qa/'detail218_manifest.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'pdf_sha256':result['pdf_sha256'],'pages':pages,'count':len(pages)},indent=2))
