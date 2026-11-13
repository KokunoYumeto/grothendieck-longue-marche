from pathlib import Path
import json,sys,subprocess,re
sys.path.insert(0,str(Path('work/scripts').resolve()))
import build_readers,editorial,mechanical_repairs,fitz
from texenv import environment
D=Path('work/layout_probes');jobs=[];records=[]
for lang in ('fr','en'):
    package='LM_C3-435-453'
    text=build_readers.raw_package(package,lang)
    text,_=mechanical_repairs.repair(text,package,lang)
    start=text.index(r'\scanpage{440}')
    start=text.index(r'\begin{tikzcd}',start)
    end=text.index(r'\end{tikzcd}',start)+len(r'\end{tikzcd}')
    old=text[start:end]
    first=r'\& G_m\arrow[ddr,dashed'
    new=old.replace(first,r'\& |[xshift=24pt]| G_m\arrow[ddr,dashed',1)
    before=r'''\deleted{\unsure{\mu_2\times\mu_2}}\end{gathered}}"']'''
    after=r'''\deleted{\unsure{\mu_2\times\mu_2}}\end{gathered}}"'{pos=.77,xshift=4pt}]'''
    assert old.count(first)==1 and old.count(before)==1,(lang,old.count(first),old.count(before))
    new=new.replace(before,after,1)
    vertical=r'\arrow[uuuu,hook,"{\mu_2\times\mu_2}"]'
    assert new.count(vertical)==2
    new=new.replace(vertical,r'\arrow[uuuu,hook,"{\mu_2\times\mu_2}"{pos=.25}]',1)
    new=new.replace(vertical,r'\arrow[uuuu,hook,"{\mu_2\times\mu_2}"{pos=.76}]',1)
    kappa=r'''\arrow[urr,dashed,"{\kappa^{\circ}}"']'''
    assert new.count(kappa)==1
    new=new.replace(kappa,r'''\arrow[urr,dashed,"{\kappa^{\circ}}"'{pos=.25,xshift=-9pt}]''',1)
    pg=r'\arrow[drr,hook,"{PG}"]'
    assert new.count(pg)==2
    at=new.rindex(pg);new=new[:at]+new[at:].replace(pg,r'\arrow[drr,hook,"{PG}"{pos=.25,xshift=-9pt}]',1)
    records.append(dict(language=lang,package=package,scan=440,tag='116',old=old,new=new,
        reason='Move the standalone G_m node 24pt right to clear the independent M-circ to M vertical arrow; relocate the three affected mu_2 times mu_2 labels along their own vertical arrows and offset the kappa-circ and lower PG labels left to clear shafts and diagonal edges. Preserve matrix row and column spacing, logical arrow endpoints, notation, uncertainty, cancellation wrappers and type size.'))
    parts=[build_readers.preamble(lang,1),r'\begin{document}\LMcote{140-3}']
    for label,diagram in [('before',old),('candidate',new)]:
        body,_,_=editorial.annotate(r'\scanpage{440}\diagram{'+diagram+'}',package,lang)
        for mode in (0,1,2):parts.append(f'\\clearpage\\LMform={mode}\n'+body)
    parts.append(r'\end{document}')
    target=D/f'scan440_candidate_{lang}.tex';target.write_text('\n'.join(parts))
    jobs.append((lang,target,subprocess.Popen(['lualatex','--no-shell-escape','-interaction=nonstopmode','-halt-on-error',target.name],cwd=D,env=environment(),stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)))
(D/'scan440_candidate.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
for lang,target,job in jobs:
    stdout,_=job.communicate();target.with_suffix('.console.txt').write_text(stdout)
    log=target.with_suffix('.log').read_text(errors='replace')
    print(lang,dict(exit=job.returncode,overfull=log.count('Overfull'),missing=log.count('Missing character')),flush=True)
    if job.returncode:raise SystemExit(job.returncode)
    for i,page in enumerate(fitz.open(target.with_suffix('.pdf'))):
        page.get_pixmap(matrix=fitz.Matrix(3,3),clip=fitz.Rect(160,50,450,490)).save(D/f'scan440_candidate_{lang}_{i}.png')
