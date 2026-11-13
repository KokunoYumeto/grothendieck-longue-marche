from pathlib import Path
import sys,json,subprocess,hashlib
sys.path.insert(0,str(Path('work/scripts').resolve()))
import build_readers,mechanical_repairs,layout_repairs,editorial,fitz
from texenv import environment
from PIL import Image,ImageDraw
D=Path('work/layout_probes');jobs=[];records=[]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
for lang in ('fr','en'):
    package='LM_C4-058-076';raw=build_readers.raw_package(package,lang)
    text,_=mechanical_repairs.repair(raw,package,lang)
    text,_=layout_repairs.repair(text,package,lang,include_pagination=False)
    phrase=r'\text{épi}' if lang=='fr' else r'\text{epimorphism}'
    anchor=text.index(phrase,text.index(r'\scanpage{65}'))
    start=text.rindex(r'\begin{tikzcd}',0,anchor);end=text.index(r'\end{tikzcd}',anchor)+len(r'\end{tikzcd}')
    old=text[start:end];needle='"'+phrase+'"]';assert old.count(needle)==2
    new=old.replace(needle,'"'+phrase+'"{yshift=3pt}]')
    records.append(dict(id='140-4-65-Vepi',language=lang,package=package,cote='140-4',scan=65,source_line=391,old=old,new=new,expected_match_count=1,kind='diagram label clearance',reason='Raise each of the two existing epimorphism/epi labels by3pt to clear its upper arrowhead barb. Preserve both label words, the doubtful middle object, matrix parameters, fonts, all arrows and all endpoints.'))
    parts=[build_readers.preamble(lang,1),r'\begin{document}\LMcote{140-4}']
    for version,fragment in [('before',old),('after',new)]:
        body,_,_=editorial.annotate(r'\scanpage{65}\[\diagram{'+fragment+r'}\]',package,lang)
        for form in (0,1,2):parts.append(f'\\clearpage\\LMform={form}\n'+body)
    parts.append(r'\end{document}');path=D/f'scan65_epi_{lang}.tex';path.write_text('\n'.join(parts))
    jobs.append((lang,path,subprocess.Popen(['lualatex','--no-shell-escape','-interaction=nonstopmode','-halt-on-error',path.name],cwd=D,env=environment(),stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)))
(D/'scan65_epi_candidate.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
results=[]
for lang,path,job in jobs:
    stdout,_=job.communicate();path.with_suffix('.console.txt').write_text(stdout);log=path.with_suffix('.log').read_text(errors='replace')
    counts=dict(exit=job.returncode,overfull=log.count('Overfull'),missing=log.count('Missing character'));print(lang,counts,flush=True)
    if job.returncode:print(stdout[-2500:]);raise SystemExit(job.returncode)
    doc=fitz.open(path.with_suffix('.pdf'));assert len(doc)==6;after=[]
    for i,page in enumerate(doc):
        version='before' if i<3 else 'after';form=i%3
        words=[w for w in page.get_text('words') if 65<w[1]<350 and w[0]<530 and w[4] not in ('[scan','65]')]
        rect=fitz.Rect(min(w[0] for w in words)-12,min(w[1] for w in words)-8,max(w[2] for w in words)+12,max(w[3] for w in words)+12)
        out=D/f'scan65_epi_{lang}_{form}_{version}_context4x.png';page.get_pixmap(matrix=fitz.Matrix(4,4),clip=rect,alpha=False).save(out)
        labels=[w for w in words if ('épi' in w[4] or 'epimorphism' in w[4])];assert len(labels)==2
        detailrect=fitz.Rect(min(w[0] for w in words)-5,min(w[1] for w in labels)-5,max(w[2] for w in words)+5,max(w[3] for w in labels)+15)
        detail=D/f'scan65_epi_{lang}_{form}_{version}_labels12x.png';page.get_pixmap(matrix=fitz.Matrix(12,12),clip=detailrect,alpha=False).save(detail)
        if version=='after':after.append((out,detail))
        results.append(dict(language=lang,form=form,version=version,compile=counts,pdf=str(path.with_suffix('.pdf')),pdf_sha256=sha(path.with_suffix('.pdf')),probe_pdf_delivery_status='HISTORICAL_PROBE_NOT_DELIVERED_AS_PUBLICATION',page=i+1,image=str(out),image_sha256=sha(out),detail=str(detail),detail_sha256=sha(detail),status='PENDING_ACTUAL_VISUAL'))
    for kind,k in [('contexts4x',0),('labels12x',1)]:
        ims=[Image.open(t[k]).convert('RGB') for t in after];cv=Image.new('RGB',(max(x.width for x in ims),sum(x.height+38 for x in ims)),(230,230,230));dr=ImageDraw.Draw(cv);y=0
        for form,im in enumerate(ims):dr.text((10,y+8),f'C4:65 {lang} form{form} actual {kind}',fill='black');cv.paste(im,(0,y+38));y+=im.height+38
        cv.save(D/f'scan65_epi_{lang}_all_after_{kind}.png')
(D/'scan65_epi_validation.json').write_text(json.dumps(dict(status='PENDING_ACTUAL_VISUAL',forms=results),ensure_ascii=False,indent=2)+'\n')
