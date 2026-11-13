from pathlib import Path
import json,sys,subprocess,hashlib
sys.path.insert(0,str(Path('work/scripts').resolve()))
import build_readers,editorial,mechanical_repairs,fitz
from texenv import environment
D=Path('work/layout_probes');records=[];jobs=[]
for lang in ('fr','en'):
    package='LM_C3-435-453';text=build_readers.raw_package(package,lang)
    text,_=mechanical_repairs.repair(text,package,lang)
    start=text.index(r'\scanpage{441}');start=text.index(r'\begin{tikzcd}',start)
    end=text.index(r'\end{tikzcd}',start)+len(r'\end{tikzcd}');old=text[start:end]
    before=r'\mathcal M_{\rho,\sigma}^{\circ}\arrow[uuu,hook,"{{\mu_2\times\mu_2}}",description]'
    after=r'\mathcal M_{\rho,\sigma}^{\circ}\arrow[uuu,hook,"{{\mu_2\times\mu_2}}"{pos=.25},description]'
    assert old.count(before)==1
    new=old.replace(before,after)
    before=r'\arrow[uuu,hook,"{{\mu_2\times\mu_2}}"]\arrow[ull]'
    after=r'\arrow[uuu,hook,"{{\mu_2\times\mu_2}}"{pos=.28}]\arrow[ull]'
    assert new.count(before)==1
    new=new.replace(before,after)
    records.append(dict(language=lang,package=package,scan=441,tag='117',old=old,new=new,
      reason='Move the two unchanged right-side mu_2 times mu_2 labels lower along their own vertical maps, to positions .25 and .28, clearing the ascending G_m diagonals. Preserve row/column spacing, outer height, endpoints, source wording and type size.'))
    parts=[build_readers.preamble(lang,1),r'\begin{document}\LMcote{140-3}']
    for diagram in (old,new):
        body,_,_=editorial.annotate(r'\scanpage{441}\diagram{'+diagram+'}',package,lang)
        for form in (0,1,2):parts.append(f'\\clearpage\\LMform={form}\n'+body)
    parts.append(r'\end{document}');target=D/f'scan441_eq117_{lang}.tex';target.write_text('\n'.join(parts))
    jobs.append((lang,target,subprocess.Popen(['lualatex','--no-shell-escape','-interaction=nonstopmode','-halt-on-error',target.name],cwd=D,env=environment(),stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)))
(D/'scan441_eq117_candidate.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
proof=[]
for lang,target,job in jobs:
    stdout,_=job.communicate();target.with_suffix('.console.txt').write_text(stdout);log=target.with_suffix('.log').read_text(errors='replace')
    counts=dict(exit=job.returncode,overfull=log.count('Overfull'),missing=log.count('Missing character'));print(lang,counts,flush=True)
    if job.returncode:raise SystemExit(job.returncode)
    for i,page in enumerate(fitz.open(target.with_suffix('.pdf'))):
        if i>=3:
            im=D/f'scan441_eq117_{lang}_{i-3}.png';page.get_pixmap(matrix=fitz.Matrix(3,3),clip=fitz.Rect(100,80,500,500)).save(im)
            proof.append(dict(language=lang,form=i-3,compile=counts,image=im.as_posix(),image_sha256=hashlib.sha256(im.read_bytes()).hexdigest(),status='PENDING_VISUAL'))
(D/'scan441_eq117_validation.json').write_text(json.dumps(dict(status='PENDING_VISUAL',forms=proof),ensure_ascii=False,indent=2)+'\n')
