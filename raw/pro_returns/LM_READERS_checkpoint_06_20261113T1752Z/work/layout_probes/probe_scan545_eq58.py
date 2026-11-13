from pathlib import Path
import json,sys,subprocess,hashlib
sys.path.insert(0,str(Path('work/scripts').resolve()))
import build_readers,editorial,mechanical_repairs,fitz
from texenv import environment
D=Path('work/layout_probes');jobs=[];records=[]
for lang in ('fr','en'):
    package='LM_C3-530-548';text=build_readers.raw_package(package,lang)
    text,_=mechanical_repairs.repair(text,package,lang)
    start=text.index(r'\scanpage{545}');start=text.index(r'\noindent(58)',start);start=text.index(r'\begin{tikzcd}',start)
    end=text.index(r'\end{tikzcd}',start)+len(r'\end{tikzcd}');old=text[start:end]
    before=r'"{\varepsilon_{\rho,\sigma}=(\unsure{\varepsilon_\sigma},\varepsilon_\rho)}"]'
    after=r'"{\varepsilon_{\rho,\sigma}=(\unsure{\varepsilon_\sigma},\varepsilon_\rho)}"{yshift=3pt}]'
    assert old.count(before)==1
    new=old.replace(before,after)
    records.append(dict(language=lang,package=package,scan=545,tag='58',old=old,new=new,
      reason='Raise the unchanged epsilon-pair arrow label3pt so its closing parenthesis clears the upper arrowhead barb; preserve the matrix, endpoints, notation, uncertainty marks and type size.'))
    body,_,_=editorial.annotate(r'\scanpage{545}\diagram{'+new+'}',package,lang)
    parts=[build_readers.preamble(lang,1),r'\begin{document}\LMcote{140-3}']
    for form in (0,1,2):parts.append(f'\\clearpage\\LMform={form}\n'+body)
    parts.append(r'\end{document}');target=D/f'scan545_eq58_{lang}.tex';target.write_text('\n'.join(parts))
    jobs.append((lang,target,subprocess.Popen(['lualatex','--no-shell-escape','-interaction=nonstopmode','-halt-on-error',target.name],cwd=D,env=environment(),stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)))
(D/'scan545_eq58_candidate.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
proof=[]
for lang,target,job in jobs:
    stdout,_=job.communicate();target.with_suffix('.console.txt').write_text(stdout);log=target.with_suffix('.log').read_text(errors='replace')
    counts=dict(exit=job.returncode,overfull=log.count('Overfull'),missing=log.count('Missing character'))
    print(lang,counts,flush=True)
    if job.returncode:raise SystemExit(job.returncode)
    for form,page in enumerate(fitz.open(target.with_suffix('.pdf'))):
        image=D/f'scan545_eq58_{lang}_{form}.png';page.get_pixmap(matrix=fitz.Matrix(6,6),clip=fitz.Rect(175,80,420,145)).save(image)
        proof.append(dict(language=lang,form=form,compile=counts,image=image.as_posix(),image_sha256=hashlib.sha256(image.read_bytes()).hexdigest(),status='PENDING_VISUAL'))
(D/'scan545_eq58_validation.json').write_text(json.dumps({'status':'PENDING_VISUAL','forms':proof},ensure_ascii=False,indent=2)+'\n')
