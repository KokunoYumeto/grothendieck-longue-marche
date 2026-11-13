from pathlib import Path
import hashlib,json,subprocess,sys
sys.path.insert(0,str(Path('work/scripts').resolve()))
import build_readers,editorial,mechanical_repairs,fitz
from texenv import environment
D=Path('work/layout_probes');jobs=[];records=[]
specs=[('LM_C3-435-453',443,'121',r'\tag{121}',r'"{{\lambda\mapsto\lambda^2}}"]',r'"{{\lambda\mapsto\lambda^2}}"{yshift=3pt}]'),
       ('LM_C3-511-529',520,'81',None,r'"\varphi=\varphi_{\mathcal G}"]',r'"\varphi=\varphi_{\mathcal G}"{yshift=3pt}]')]
for package,scan,tag,marker,before,after in specs:
 for lang in ('fr','en'):
    text=build_readers.raw_package(package,lang);text,_=mechanical_repairs.repair(text,package,lang)
    start=text.index('\\scanpage{'+str(scan)+'}')
    if marker:start=text.index(marker,start)
    start=text.index(r'\begin{tikzcd}',start);end=text.index(r'\end{tikzcd}',start)+len(r'\end{tikzcd}')
    old=text[start:end];assert old.count(before)==1,(scan,lang);new=old.replace(before,after)
    records.append(dict(language=lang,package=package,scan=scan,tag=tag,old=old,new=new,
       reason='Raise the unchanged label3pt to separate its final glyph from the upper arrowhead barb. Preserve the matrix, endpoints, type size, and every other source label.'))
    body,entries,meta=editorial.annotate('\\scanpage{'+str(scan)+'}\\diagram{'+new+'}',package,lang)
    parts=[build_readers.preamble(lang,1),r'\begin{document}\LMcote{140-3}']
    for form in (0,1,2):parts.append(f'\\clearpage\\LMform={form}\n'+body)
    parts.append(r'\end{document}');target=D/f'scan{scan}_eq{tag}_{lang}.tex';target.write_text('\n'.join(parts))
    jobs.append((scan,tag,lang,target,subprocess.Popen(['lualatex','--no-shell-escape','-interaction=nonstopmode','-halt-on-error',target.name],cwd=D,env=environment(),stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)))
(D/'scan443_520_labels_candidate.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
proof=[]
for scan,tag,lang,target,job in jobs:
    stdout,_=job.communicate();target.with_suffix('.console.txt').write_text(stdout);log=target.with_suffix('.log').read_text(errors='replace')
    counts=dict(exit=job.returncode,overfull=log.count('Overfull'),missing=log.count('Missing character'));print(scan,lang,counts,flush=True)
    if job.returncode:raise SystemExit(job.returncode)
    doc=fitz.open(target.with_suffix('.pdf'));assert len(doc)==3
    for form,page in enumerate(doc):
        im=D/f'scan{scan}_eq{tag}_{lang}_{form}.png'
        clip=fitz.Rect(195,85,405,160) if scan==443 else fitz.Rect(250,85,350,140)
        page.get_pixmap(matrix=fitz.Matrix(8,8),clip=clip).save(im)
        proof.append(dict(scan=scan,tag=tag,language=lang,form=form,compile=counts,image=im.as_posix(),image_sha256=hashlib.sha256(im.read_bytes()).hexdigest(),status='PENDING_VISUAL'))
(D/'scan443_520_labels_validation.json').write_text(json.dumps(dict(status='PENDING_VISUAL',forms=proof),ensure_ascii=False,indent=2)+'\n')
