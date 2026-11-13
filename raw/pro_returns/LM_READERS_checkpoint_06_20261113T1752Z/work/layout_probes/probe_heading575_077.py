from pathlib import Path
import sys,json,subprocess,hashlib
sys.path.insert(0,str(Path('work/scripts').resolve()))
import build_readers,mechanical_repairs,editorial,fitz
from texenv import environment
from PIL import Image,ImageDraw

D=Path('work/layout_probes')
jobs=[]
for site,package,cote,scan,identifier in [
    ('575','LM_C3-568-586','140-3',575,'140-3-575-HProposition'),
    ('077','LM_C4-077-095','140-4',77,'140-4-77-H7')]:
    records=[]
    for lang in ('fr','en'):
        raw=build_readers.raw_package(package,lang)
        heading=(r'\uline{Proposition}' if site=='575' else r'$7^\circ)$')
        start=raw.index(heading,raw.index(r'\scanpage{'+str(scan)+'}'))
        end=raw.index('\n',start)
        old=raw[start:end]
        new=r'\Needspace{12\baselineskip}'+'\n'+old
        records.append(dict(id=identifier,language=lang,package=package,cote=cote,scan=scan,
            source_line=raw.count('\n',0,start)+1,old=old,new=new,expected_match_count=1,
            kind='section-heading pagination',
            reason=('Reserve twelve current baselines before the unchanged Proposition heading so its displayed homomorphism and first assertion remain with it; preserve normal paragraph flow and all source content.' if site=='575' else 'Reserve twelve current baselines before the unchanged item7 heading and its short marginal note so the opening subgroup definition152 follows on the same page; preserve normal paragraph flow and all source marks.')))
        text,_=mechanical_repairs.repair(raw,package,lang)
        a=text.index(heading,text.index(r'\scanpage{'+str(scan)+'}'))
        if site=='575':
            b=text.index('\na) ',a)
        else:
            b=text.index(r'\deleted{On}' if lang=='fr' else r'\deleted{We}',a)
        original=text[a:b]
        assert original.count(old)==1
        for label,source in [('before',original),('after',original.replace(old,new))]:
            body,_,_=editorial.annotate(r'\scanpage{'+str(scan)+'}'+source,package,lang)
            body=body.replace(r'\scanpage{'+str(scan)+'}','',1)
            parts=[build_readers.preamble(lang,1),r'\begin{document}\LMcote{'+cote+'}']
            for form in (0,1,2):
                parts += [f'\\clearpage\\LMform={form}\n'+r'\noindent Preceding material.\par\vspace*{\dimexpr\textheight-60pt\relax}\par\penalty0',body]
            parts.append(r'\end{document}')
            path=D/f'heading{site}_{lang}_{label}.tex';path.write_text('\n'.join(parts))
            jobs.append((site,lang,label,path,subprocess.Popen(['lualatex','--no-shell-escape','-interaction=nonstopmode','-halt-on-error',path.name],cwd=D,env=environment(),stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)))
    (D/f'heading{site}_candidate.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')

results={'575':[],'077':[]}
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
for site,lang,label,path,job in jobs:
    stdout,_=job.communicate();path.with_suffix('.console.txt').write_text(stdout)
    log=path.with_suffix('.log').read_text(errors='replace')
    counts=dict(exit=job.returncode,overfull=log.count('Overfull'),missing=log.count('Missing character'))
    print(site,lang,label,counts,flush=True)
    if job.returncode:
        print(stdout[-2500:]);raise SystemExit(job.returncode)
    doc=fitz.open(path.with_suffix('.pdf'));rows=[];images=[]
    for i,page in enumerate(doc):
        txt=page.get_text()
        hasheading=('Proposition' in txt) if site=='575' else (('Les groupes' if lang=='fr' else 'The groups') in txt)
        if not hasheading:continue
        words=[w for w in page.get_text('words') if w[1]<765 and w[0]<588]
        y0=min(w[1] for w in words);y1=max(w[3] for w in words)
        # Whole-page images retain the stressed placement. Detail crops show
        # the complete accepted opening at native3x, not a relayout.
        out=D/f'heading{site}_{lang}_{label}_p{i+1:02}.png'
        page.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(out)
        detail=D/f'heading{site}_{lang}_{label}_p{i+1:02}_opening3x.png'
        page.get_pixmap(matrix=fitz.Matrix(3,3),clip=fitz.Rect(55,max(45,y0-12),595.276,min(770,y1+12)),alpha=False).save(detail)
        row=dict(form=len(rows),page=i+1,image=str(out),image_sha256=sha(out),detail=str(detail),detail_sha256=sha(detail),status='PENDING_ACTUAL_VISUAL')
        rows.append(row);images.append(detail)
    assert len(rows)==3,(site,lang,label,rows)
    if label=='after':
        ims=[Image.open(x).convert('RGB') for x in images];width=max(im.width for im in ims)
        canvas=Image.new('RGB',(width,sum(im.height+38 for im in ims)),(230,230,230));dr=ImageDraw.Draw(canvas);y=0
        for form,im in enumerate(ims):
            dr.text((10,y+8),f'{site} {lang} form {form} — actual native3x page crop',fill='black');canvas.paste(im,(0,y+38));y+=im.height+38
        contact=D/f'heading{site}_{lang}_all_after_openings3x.png';canvas.save(contact)
    results[site].append(dict(language=lang,version=label,compile=counts,pdf=str(path.with_suffix('.pdf')),pdf_sha256=sha(path.with_suffix('.pdf')),probe_pdf_delivery_status='HISTORICAL_PROBE_NOT_DELIVERED_AS_PUBLICATION',pages=rows,status='PENDING_ACTUAL_VISUAL'))
for site,probes in results.items():
    (D/f'heading{site}_validation.json').write_text(json.dumps(dict(status='PENDING_ACTUAL_VISUAL',remaining_page_height_pt=60,source_changes='Exact Needspace prefix only; no source content removed, no boxing, no font or diagram-geometry changes.',probes=probes),ensure_ascii=False,indent=2)+'\n')
