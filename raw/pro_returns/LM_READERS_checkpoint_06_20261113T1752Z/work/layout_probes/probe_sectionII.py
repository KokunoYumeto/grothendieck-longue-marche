from pathlib import Path
import hashlib,json,subprocess,sys
sys.path.insert(0,str(Path('work/scripts').resolve()))
import build_readers,editorial,mechanical_repairs,fitz
from texenv import environment
D=Path('work/layout_probes');jobs=[];candidates=[]
for lang in ('fr','en'):
    package='LM_C3-169-187';text=build_readers.raw_package(package,lang);text,_=mechanical_repairs.repair(text,package,lang)
    start=text.index('II \\uline{',text.index(r'\scanpage{186}'));end=text.index(r'\]',start)+2
    original=text[start:end];heading=original.split('\n\n',1)[0]
    old=heading+'\n\n';new=r'\Needspace{8\baselineskip}'+'\n'+heading+r'\par\nobreak'+'\n'
    assert original.count(old)==1
    candidates.append(dict(language=lang,package=package,scan=186,old=old,new=new,
      reason='Keep the original sectionII heading attached to the opening paragraph; reserve eight baselines and prohibit a page break immediately after the heading. Preserve every heading word and its original number.'))
    for label,source in [('before',original),('after',original.replace(old,new))]:
        body,entries,meta=editorial.annotate(r'\scanpage{186}'+source,package,lang)
        body=body.replace(r'\scanpage{186}','',1)
        parts=[build_readers.preamble(lang,1),r'\begin{document}\LMcote{140-2}']
        for form in (0,1,2):
            parts.append(f'\\clearpage\\LMform={form}\n'+r'\noindent Preceding material.\par\vspace*{\dimexpr\textheight-3\baselineskip\relax}'+'\n'+body+r'\par\noindent End of opening paragraph.\par')
        parts.append(r'\end{document}')
        target=D/f'sectionII_{label}_{lang}.tex';target.write_text('\n'.join(parts))
        jobs.append((lang,label,target,subprocess.Popen(['lualatex','--no-shell-escape','-interaction=nonstopmode','-halt-on-error',target.name],cwd=D,env=environment(),stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)))
(D/'sectionII_candidate.json').write_text(json.dumps(candidates,ensure_ascii=False,indent=2)+'\n')
proof=[]
for lang,label,target,job in jobs:
    stdout,_=job.communicate();target.with_suffix('.console.txt').write_text(stdout);log=target.with_suffix('.log').read_text(errors='replace')
    counts=dict(exit=job.returncode,overfull=log.count('Overfull'),missing=log.count('Missing character'));print(lang,label,counts,flush=True)
    if job.returncode:raise SystemExit(job.returncode)
    doc=fitz.open(target.with_suffix('.pdf'));rows=[]
    for i,page in enumerate(doc):
        text=page.get_text();heading='Détermination calculatoire' in text or 'Computational determination' in text
        opening='Rappelons' in text if lang=='fr' else ('Recall' in text or 'Let us recall' in text)
        row=dict(page=i+1,heading=heading,opening=opening)
        if heading:
            im=D/f'sectionII_{label}_{lang}_p{i+1:02}.png';page.get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(im)
            row.update(image=im.as_posix(),image_sha256=hashlib.sha256(im.read_bytes()).hexdigest())
        rows.append(row)
    proof.append(dict(language=lang,variant=label,compile=counts,pages=rows))
(D/'sectionII_validation.json').write_text(json.dumps(dict(status='PENDING_VISUAL',probes=proof),ensure_ascii=False,indent=2)+'\n')
