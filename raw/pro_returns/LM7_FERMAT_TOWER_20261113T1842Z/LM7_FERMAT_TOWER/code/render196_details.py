"""Retain selected full-resolution Poppler pages for actual visual inspection."""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import subprocess
from PIL import Image

BASE=Path(__file__).resolve().parents[1]
PDF=BASE/'LM7_FERMAT_TOWER_paper.pdf'
DEST=BASE/'qa/details196';DEST.mkdir(exist_ok=True)
PAGES=[173,175,177,178,180,182,183,185,186,
       506,508,509,510,512,514,516,517,520,
       522,524,525,527,528,529,530,531,532,538]
digest=hashlib.sha256(PDF.read_bytes()).hexdigest()
assert digest==json.loads((BASE/'qa/pdf_qa.json').read_text())['sha256']
def render(page):
    prefix=DEST/f'page_{page:03d}'
    run=subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-singlefile',
                        '-r','110','-png',str(PDF),str(prefix)],capture_output=True)
    assert run.returncode==0,(page,run.stderr.decode())
    src=prefix.with_suffix('.png');dst=prefix.with_suffix('.jpg')
    im=Image.open(src).convert('RGB');im.save(dst,quality=92);src.unlink()
    return {'page':page,'path':str(dst.relative_to(BASE)),'sha256':hashlib.sha256(dst.read_bytes()).hexdigest(),
            'pixels':list(im.size),'returncode':run.returncode}
with ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(render,PAGES))
assert hashlib.sha256(PDF.read_bytes()).hexdigest()==digest
record={'pdf_sha256':digest,'dpi':110,'pages':rows,'actual_visual_inspection_claimed':False}
(DEST/'manifest.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
