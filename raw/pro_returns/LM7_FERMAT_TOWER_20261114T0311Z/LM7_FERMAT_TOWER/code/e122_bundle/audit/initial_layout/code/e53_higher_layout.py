#!/usr/bin/env python3
"""Render the full E122 proof in the actual manuscript page geometry."""
from pathlib import Path
import hashlib,json,re,subprocess,os
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parents[1];Q=R/'qa';Q.mkdir(exist_ok=True)
p=R/'sections/E_fiftythree_higher_action.tex'
pre=r'''\documentclass[11pt,a4paper]{article}
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
post=r'''\begin{thebibliography}{9}
\bibitem{E_MilneCFT} J. S. Milne, \emph{Class Field Theory}, version4.03, 2020.
\bibitem{E_PARICertifiedUnits} The PARI Group, \emph{PARI/GP2.19.0 User's Guide}, official function contracts and implementation.
\end{thebibliography}\end{document}
'''
assert not re.search('[\x00-\x08\x0b\x0c\x0e-\x1f]',p.read_text())
(Q/'e122_standalone.tex').write_text(pre+p.read_text()+post)
runtime=R.parent/'.lm7_tex_runtime';dist=subprocess.check_output(['kpsewhich','-var-value=TEXMFDIST'],text=True).strip()
env=os.environ.copy();env.update(TEXMF='{.,'+str(runtime)+',/usr/share/texmf,'+dist+'}',
 TEXMFVAR=str(runtime),TEXMFCONFIG=str(runtime),TEXFORMATS=str(runtime),
 TEXINPUTS=str(runtime)+'//:',TEXFONTMAPS=str(runtime)+':')
for i in range(2):
    run=subprocess.run(['lualatex','--interaction=nonstopmode','--halt-on-error','--fmt=lualatex_type1','e122_standalone.tex'],cwd=Q,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (Q/f'latex_pass_{i+1}.out').write_bytes(run.stdout)
    assert run.returncode==0,run.stdout.decode()[-5000:]
log=(Q/'e122_standalone.log').read_text();bad=re.findall(r'Overfull[^\n]*(?:\n[^\n]*)?',log)
run=subprocess.run(['pdftoppm','-r','110','-png','e122_standalone.pdf','page'],cwd=Q,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
(Q/'render.out').write_bytes(run.stdout);assert run.returncode==0
pages=sorted(Q.glob('page-*.png'));sheet=Image.new('RGB',(1140,540*((len(pages)+2)//3)),'white')
for i,path in enumerate(pages):
    im=Image.open(path).convert('RGB');im.thumbnail((360,510))
    tile=Image.new('RGB',(380,540),'#dddddd');tile.paste(im,((380-im.width)//2,20))
    ImageDraw.Draw(tile).text((10,522),path.name,fill='black');sheet.paste(tile,((i%3)*380,(i//3)*540))
sheet.save(Q/'contact_sheet.png')
d={'statement':'E.122','status':'LAYOUT_PASS' if not bad else 'OVERFULL_REQUIRES_CORRECTION',
   'pages':len(pages),'overfull':bad,'section_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
   'PDF_sha256':hashlib.sha256((Q/'e122_standalone.pdf').read_bytes()).hexdigest(),
   'visual_review':'Pending actual page-image review; automated layout result only.'}
t=json.dumps(d,indent=2)+'\n';(R/'code/e53_higher_layout.json').write_text(t);print(t,end='')
