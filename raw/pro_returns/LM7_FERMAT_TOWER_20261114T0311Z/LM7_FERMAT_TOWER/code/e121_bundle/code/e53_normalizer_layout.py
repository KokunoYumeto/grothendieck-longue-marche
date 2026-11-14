#!/usr/bin/env python3
"""Render all E121 formulas in the actual paper geometry and retain QA."""
from pathlib import Path
import hashlib,json,re,subprocess,os
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parent.parent
QA=ROOT/'qa';QA.mkdir(exist_ok=True)
preamble=r'''\documentclass[11pt,a4paper]{article}
\usepackage[T1]{fontenc}\usepackage{lmodern}
\usepackage[a4paper,margin=27mm,headheight=14pt]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools,graphicx}
\usepackage{xcolor,microtype,hyperref}
\setlength{\parindent}{1.3em}\setlength{\parskip}{.22em}
\setlength{\emergencystretch}{2em}\setcounter{secnumdepth}{0}
\allowdisplaybreaks[2]
\newenvironment{statement}[3]{\par\addvspace{1.1em}\noindent
\textbf{#1. #3}\quad\textsf{\small[#2]}\par\nobreak\smallskip\ignorespaces}
{\par\smallskip}
\begin{document}
'''
proof=ROOT/'sections/E_fiftythree_normalizer.tex'
bib=r'''\begin{thebibliography}{9}
\bibitem{E_MilneCFT} J. S. Milne, \emph{Class Field Theory}, version4.03, 2020.
\bibitem{E_LemmermeyerAmbiguous} F. Lemmermeyer, \emph{The Ambiguous Class Number Formula Revisited}, arXiv:1309.1071, 2013.
\bibitem{E_PARICertifiedUnits} The PARI Group, \emph{PARI/GP2.19.0 User's Guide}, \texttt{bnfcertify}, and official source \texttt{buch3.c}.
\end{thebibliography}\end{document}
'''
(QA/'e121_standalone.tex').write_text(preamble+proof.read_text()+bib)
runtime=ROOT.parent/'.lm7_tex_runtime'
dist=subprocess.check_output(['kpsewhich','-var-value=TEXMFDIST'],text=True).strip()
env=os.environ.copy();env.update(TEXMF='{.,'+str(runtime)+',/usr/share/texmf,'+dist+'}',
    TEXMFVAR=str(runtime),TEXMFCONFIG=str(runtime),TEXFORMATS=str(runtime),
    TEXINPUTS=str(runtime)+'//:',TEXFONTMAPS=str(runtime)+':')
for i in range(2):
    p=subprocess.run(['lualatex','--interaction=nonstopmode','--halt-on-error',
                      '--fmt=lualatex_type1','e121_standalone.tex'],cwd=QA,env=env,
                     stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (QA/f'latex_pass_{i+1}.out').write_bytes(p.stdout)
    assert p.returncode==0,p.stdout.decode()[-5000:]
log=(QA/'e121_standalone.log').read_text()
overfull=re.findall(r'Overfull[^\n]*(?:\n[^\n]*)?',log)
p=subprocess.run(['pdftoppm','-r','100','-png','e121_standalone.pdf','page'],cwd=QA,
                 stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
(QA/'render.out').write_bytes(p.stdout);assert p.returncode==0
pages=sorted(QA.glob('page-*.png'))
sheet=Image.new('RGB',(1140,540*((len(pages)+2)//3)),'white')
for i,path in enumerate(pages):
    im=Image.open(path).convert('RGB');im.thumbnail((360,510))
    tile=Image.new('RGB',(380,540),'#dddddd');tile.paste(im,((380-im.width)//2,20))
    ImageDraw.Draw(tile).text((10,522),path.name,fill='black')
    sheet.paste(tile,((i%3)*380,(i//3)*540))
sheet.save(QA/'contact_sheet.png')
out={'statement':'E.121','status':'LAYOUT_PASS' if not overfull else 'OVERFULL_REQUIRES_CORRECTION',
     'pages':len(pages),'overfull':overfull,
     'section_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
     'PDF_sha256':hashlib.sha256((QA/'e121_standalone.pdf').read_bytes()).hexdigest()}
(ROOT/'code/e53_normalizer_layout.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
