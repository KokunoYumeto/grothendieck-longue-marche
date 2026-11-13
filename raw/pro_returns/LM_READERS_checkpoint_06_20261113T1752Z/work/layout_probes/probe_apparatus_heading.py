"""Probe apparatus heading attachment without changing frozen dependencies."""
from pathlib import Path
import hashlib,json,subprocess,sys
sys.path.insert(0,str(Path('work/scripts').resolve()))
import build_readers,fitz
from texenv import environment
D=Path('work/layout_probes')
old=r'\newenvironment{LMapparatus}{\par\smallskip\begingroup\LMinApp=1\footnotesize\noindent\textcolor{gray}{\rule{.26\linewidth}{.35pt}}\par\noindent\textbf{\LMappheading}\par\smallskip}{\par\endgroup}'
new=r'\newenvironment{LMapparatus}{\par\smallskip\begingroup\LMinApp=1\footnotesize\Needspace{4\baselineskip}\csname @beginparpenalty\endcsname=10000\relax\noindent\textcolor{gray}{\rule{.26\linewidth}{.35pt}}\par\nobreak\noindent\textbf{\LMappheading}\par\nobreak\smallskip}{\par\endgroup}'
jobs=[];rows=[]
for lang in ('fr','en'):
    annotated,entries,meta,provenance=build_readers.package_data('LM_C3-625-643',lang,'build')
    selected=[e for e in entries if int(e['scan'])==638]
    body=build_readers.apparatus(selected,lang)
    preamble=build_readers.preamble(lang,1);assert preamble.count(old)==1
    for variant in ('before','after'):
        pre=preamble if variant=='before' else preamble.replace(old,new)
        parts=[pre,r'\begin{document}\LMcote{140-3}\scanpage{638}']
        for spare in (28,35,42,50,110):
            parts.append(r'\clearpage\noindent Preceding material.\par'+f'\\vspace*{{\\dimexpr\\textheight-{spare}pt-\\baselineskip\\relax}}\n'+body+r'\par\noindent Following text.\par')
        parts.append(r'\end{document}')
        target=D/f'apparatus_heading_{variant}_{lang}.tex';target.write_text('\n'.join(parts))
        jobs.append((lang,variant,target,subprocess.Popen(['lualatex','--no-shell-escape','-interaction=nonstopmode','-halt-on-error',target.name],cwd=D,env=environment(),stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)))
(D/'apparatus_heading_candidate.json').write_text(json.dumps(dict(old_definition=old,new_definition=new,reason='Keep the generated apparatus rule and heading with the first unchanged entry. Reserve four footnote baselines, forbid breaks after rule and heading, and protect a starting trivlist locally; retain page breaking within later entries and long apparatus.',manuscript_text_changed=False,affects_forms=[1],actual_witnesses='work/data/apparatus_heading_orphans_revision512.json'),ensure_ascii=False,indent=2)+'\n')
for lang,variant,target,job in jobs:
    output,_=job.communicate();target.with_suffix('.console.txt').write_text(output);log=target.with_suffix('.log').read_text(errors='replace')
    counts=dict(exit=job.returncode,overfull=log.count('Overfull'),missing=log.count('Missing character'));print(lang,variant,counts,flush=True);assert counts==dict(exit=0,overfull=0,missing=0)
    doc=fitz.open(target.with_suffix('.pdf'));heading='Apparat du scan' if lang=='fr' else 'Apparatus for this scan';occurrence=0
    for i,page in enumerate(doc):
        text=page.get_text()
        if heading not in text:continue
        occurrence+=1;rect=page.search_for(heading)[0];image=D/f'apparatus_heading_{variant}_{lang}_p{i+1:02}.png'
        clip=fitz.Rect(65,max(65,rect.y0-25),530,min(800,rect.y1+105));page.get_pixmap(matrix=fitz.Matrix(2.5,2.5),clip=clip).save(image)
        first='140-3-s638-D001';entrypages=[]
        for j in range(i,len(doc)):
            t=doc[j].get_text()
            if '140-3-s638-' in t:entrypages.append(j+1)
            if 'Following text.' in t:break
        rows.append(dict(language=lang,variant=variant,occurrence=occurrence,page=i+1,first_entry_same_page=first in text,entry_pages=entrypages,compile=counts,image=image.as_posix(),image_sha256=hashlib.sha256(image.read_bytes()).hexdigest(),status='PENDING_VISUAL'))
(D/'apparatus_heading_validation.json').write_text(json.dumps(dict(status='PENDING_VISUAL',probes=rows),ensure_ascii=False,indent=2)+'\n')
