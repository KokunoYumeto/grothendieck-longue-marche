from pathlib import Path
import hashlib,json,re,subprocess,sys
sys.path.insert(0,str(Path('work/scripts').resolve()))
import build_readers,editorial,mechanical_repairs,fitz
from texenv import environment

D=Path('work/layout_probes');records=[];jobs=[]
for lang in ('fr','en'):
    package='LM_C3-435-453'
    text=build_readers.raw_package(package,lang)
    text,_=mechanical_repairs.repair(text,package,lang)
    scan=text[text.index(r'\scanpage{449}'):text.index(r'\scanpage{450}')]
    displays=[]
    for tag,labels in [('137',[r'i_\rho',r'i_\sigma']),('138',[r'\delta_\rho'])]:
        start=scan.index('\\[\n('+tag+')');end=scan.index(r'\]',start)+2
        old=scan[start:end];new=old
        changes=[]
        for label in labels:
            before='"{'+label+'}"]'
            after='"{'+label+'}"{yshift=3pt}]'
            assert new.count(before)==1,(lang,tag,label)
            new=new.replace(before,after)
            changes.append(dict(old=before,new=after))
        records.append(dict(language=lang,package=package,scan=449,tag=tag,old=old,new=new,
            changes=changes,reason='Raise only the indicated short horizontal-map labels 3pt to clear their upper arrowhead barbs. Preserve all endpoints, source targets, type size, cancellation and uncertainty wrappers; leave the clear j label unchanged.'))
        displays.append(new)
    body,entries,meta=editorial.annotate(r'\scanpage{449}'+'\n'.join(displays),package,lang)
    body+='\n'+build_readers.apparatus(entries,lang)
    parts=[build_readers.preamble(lang,1),r'\begin{document}\LMcote{140-3}']
    for form in (0,1,2):parts.append(f'\\clearpage\\LMform={form}\n'+body)
    parts.append(r'\end{document}')
    target=D/f'scan449_labels_{lang}.tex';target.write_text('\n'.join(parts))
    jobs.append((lang,target,subprocess.Popen(['lualatex','--no-shell-escape','-interaction=nonstopmode','-halt-on-error',target.name],cwd=D,env=environment(),stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)))
(D/'scan449_labels_candidate.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
proof=[]
for lang,target,job in jobs:
    stdout,_=job.communicate();target.with_suffix('.console.txt').write_text(stdout)
    log=target.with_suffix('.log').read_text(errors='replace')
    counts=dict(exit=job.returncode,overfull=log.count('Overfull'),missing=log.count('Missing character'))
    print(lang,counts,flush=True)
    if job.returncode:raise SystemExit(job.returncode)
    doc=fitz.open(target.with_suffix('.pdf'))
    assert len(doc)==3,len(doc)
    for form,page in enumerate(doc):
        im=D/f'scan449_labels_{lang}_{form}.png'
        page.get_pixmap(matrix=fitz.Matrix(3,3),clip=fitz.Rect(65,65,550,540)).save(im)
        proof.append(dict(language=lang,form=form,compile=counts,image=im.as_posix(),image_sha256=hashlib.sha256(im.read_bytes()).hexdigest(),status='PENDING_VISUAL'))
(D/'scan449_labels_validation.json').write_text(json.dumps(dict(status='PENDING_VISUAL',forms=proof),ensure_ascii=False,indent=2)+'\n')
