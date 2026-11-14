#!/usr/bin/env python3
"""Inspect the final TeX log and render a distributed, claim-aware PDF sample.

Rendering is evidence for manual visual review, never a substitute for it.
The output JSON expressly distinguishes rendered from visually reviewed pages.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import re
import subprocess
from PIL import Image, ImageDraw

ROOT=Path(__file__).resolve().parents[1]
PDF=ROOT/'ANABELIAN_149_PUSH_paper.pdf'
LOG=ROOT/'build/lualatex-final.log'
if not LOG.exists():raise FileNotFoundError('Run the stabilized LuaLaTeX build first')
log=LOG.read_text()
overflows=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt too (?:wide|high)\)',log)]
warnings=[line for line in log.splitlines() if 'Warning' in line]
if any(x>2 for x in overflows):raise RuntimeError('An overfull box exceeds 2pt; fix it before review')
if warnings:raise RuntimeError('Final build still has warnings: '+str(warnings))
raw=subprocess.check_output(['pdftotext','-layout',str(PDF),'-'],text=True)
pages=raw.split('\f')
if not pages[-1].strip():pages.pop()
selected={1,len(pages)}|set(range(5,len(pages)+1,15))
claims=['A.19','A.C2.4','A.27','A.28','A.29','A.29a','A.29b','A.29c',
        'B.11d','B.11e','B.11f','B.12','B.15a','B.15u','B.16u','B.20','B.21','B.24',
        'C.6','D.12','D.14','E.10','E.11',
        'F.16','F.17','F.18','F.19','F.20','F.21','F.22','F.23','F.24','F.25',
        'F.26','F.27','F.28','F.29','F.30','F.31']
found={}
for claim in claims:
    pattern=re.compile(re.escape(claim)+r'\s*\(')
    for index,page in enumerate(pages,1):
        if pattern.search(page):found[claim]=index;selected.add(index);break
# Review the previously overflowing physical page and the bibliography entry
# even when additions have moved it to a different page.
former_overflow_pages=[]
before=ROOT/'audit/typesetting_overflow_before.json'
if before.exists():
    old=json.loads(before.read_text()).get('page')
    if old and old<=len(pages):selected.add(old);former_overflow_pages.append(old)
    for old in json.loads(before.read_text()).get('pages_with_observed_overflow',[]):
        if old<=len(pages):selected.add(old);former_overflow_pages.append(old)
for index,page in enumerate(pages,1):
    if 'Minamide' in page and 'References' not in page and '2022' in page and index>len(pages)-15:
        selected.add(index);former_overflow_pages.append(index)
output=ROOT/'audit/pdf_pages'
output.mkdir(exist_ok=True)
def render(n):
    prefix=output/f'page_{n:03d}'
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-scale-to','1450',
                    '-singlefile','-png',str(PDF),str(prefix)],check=True,
                   stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    return str(prefix.with_suffix('.png').relative_to(ROOT))
with ThreadPoolExecutor(max_workers=3) as pool:
    images=list(pool.map(render,sorted(selected)))
contact_files=[]
for start in range(0,len(images),9):
    batch=images[start:start+9]
    canvas=Image.new('RGB',(1260,3*625),(224,228,232))
    draw=ImageDraw.Draw(canvas)
    for j,name in enumerate(batch):
        with Image.open(ROOT/name) as page:
            page.thumbnail((400,585))
            x=10+(j%3)*420;y=30+(j//3)*625
            canvas.paste(page,(x,y))
            draw.text((x,y-20),Path(name).stem,fill='black')
    path=output/f'contact_{start//9+1:02d}.png'
    canvas.save(path);contact_files.append(str(path.relative_to(ROOT)))
result={'pdf_sha256':hashlib.sha256(PDF.read_bytes()).hexdigest(),
        'pages':len(pages),'overfull_boxes':len(overflows),
        'overfull_above_2pt':sum(x>2 for x in overflows),
        'largest_overflow_pt':max(overflows,default=0),'final_warnings':warnings,
        'claim_pages':found,'former_overflow_pages':sorted(set(former_overflow_pages)),
        'rendered_pages':sorted(selected),
        'rendered_files':images,'contact_sheets':contact_files,
        'visually_reviewed_pages':[],
        'review_status':'Rendered for manual review; this program does not assert visual approval.'}
(ROOT/'code/PDF_layout_audit_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
