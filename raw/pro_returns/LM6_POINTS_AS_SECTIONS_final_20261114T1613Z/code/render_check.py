#!/usr/bin/env python3
"""Render a spread of the current PDF for actual visual inspection."""
from pathlib import Path
import subprocess,json,hashlib,re
from pypdf import PdfReader
R=Path(__file__).resolve().parents[1]
pdf=R/'deliverable/LM6_POINTS_AS_SECTIONS_paper.pdf'
n=len(PdfReader(pdf).pages)
pages={1,4,35,69,80,100,111,143,174,217,218,n}
aux=pdf.with_suffix('.aux').read_text()
for ident in ['A.61','A.64','A.66','A.67','B.40','B.41','B.42',
              'E.34','E.35','E.36','E.37','E.38','E.39','F.45','F.46','F.47']:
    m=re.search(r'\\newlabel\{st:'+re.escape(ident)+r'\}\{\{[^}]*\}\{(\d+)\}',aux)
    if m:pages.add(int(m.group(1)))
pages=sorted(pages)
dest=R/'rendered/current';dest.mkdir(parents=True,exist_ok=True)
for p in pages:
    subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-scale-to','1400',
                    '-singlefile','-png',str(pdf),str(dest/f'page{p:03d}')],check=True,
                   stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
out={'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
     'pages_total':n,'rendered_pages':pages,
     'visually_inspected_pages':[],
     'status':'rendered; visual inspection must be recorded separately'}
(R/'render_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
