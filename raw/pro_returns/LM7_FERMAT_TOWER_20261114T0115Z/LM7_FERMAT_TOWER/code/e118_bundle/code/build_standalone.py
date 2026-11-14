#!/usr/bin/env python3
"""Render E.118 using the exact current main-paper preamble and geometry."""
from pathlib import Path
import hashlib
import json
import os
import re
import subprocess
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT.parent
QA = ROOT / 'qa'
QA.mkdir(exist_ok=True)
proof = ROOT / 'sections/E_quartic_five_numerical.tex'
master = WORK / 'LM7_FERMAT_TOWER/LM7_FERMAT_TOWER_paper.tex'
preamble = master.read_text().split(r'\begin{document}',1)[0]
(QA/'e118_standalone.tex').write_text(preamble+r'\begin{document}'+'\n'+proof.read_text()+'\n'+r'\end{document}'+'\n')
runtime = WORK/'.lm7_tex_runtime'
dist = subprocess.check_output(['kpsewhich','-var-value=TEXMFDIST'],text=True).strip()
env = os.environ.copy()
env.update(TEXMF='{.,'+str(runtime)+',/usr/share/texmf,'+dist+'}',
           TEXMFVAR=str(runtime),TEXMFCONFIG=str(runtime),TEXFORMATS=str(runtime),
           TEXINPUTS=str(runtime)+'//:',TEXFONTMAPS=str(runtime)+':')
for i in range(2):
    run = subprocess.run(['lualatex','--interaction=nonstopmode','--halt-on-error',
                          '--fmt=lualatex_type1','e118_standalone.tex'],cwd=QA,env=env,capture_output=True)
    (QA/f'latex_pass_{i+1}.out').write_bytes(run.stdout+run.stderr)
    assert run.returncode==0, (run.stdout+run.stderr).decode()[-5000:]
log = (QA/'e118_standalone.log').read_text()
problems = [line for line in log.splitlines() if 'Overfull' in line or 'Missing character' in line]
run = subprocess.run(['pdftoppm','-r','110','-jpeg','e118_standalone.pdf','page'],cwd=QA,capture_output=True)
(QA/'render.out').write_bytes(run.stdout+run.stderr)
assert run.returncode==0
pages = sorted(QA.glob('page-*.jpg'),key=lambda p:int(p.stem.split('-')[-1]))
sheet = Image.new('RGB',(1140,540*((len(pages)+2)//3)),'white')
for i,path in enumerate(pages):
    im=Image.open(path).convert('RGB');im.thumbnail((360,510))
    tile=Image.new('RGB',(380,540),'#dddddd');tile.paste(im,((380-im.width)//2,20))
    ImageDraw.Draw(tile).text((10,522),path.name,fill='black')
    sheet.paste(tile,((i%3)*380,(i//3)*540))
sheet.save(QA/'contact_sheet.jpg',quality=90)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'statement':'E.118','status':'READY_FOR_VISUAL_REVIEW' if not problems else 'LAYOUT_CORRECTION_REQUIRED',
        'pages':len(pages),'problems':problems,'proof_sha256':sha(proof),
        'preamble_source_sha256':sha(master),'PDF_sha256':sha(QA/'e118_standalone.pdf'),
        'page_images':[{ 'path':str(p.relative_to(ROOT)), 'sha256':sha(p)} for p in pages],
        'actual_visual_review_claimed_by_program':False}
(QA/'layout.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
