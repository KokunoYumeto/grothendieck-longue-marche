from pathlib import Path
import sys,json,subprocess,hashlib
sys.path.insert(0,str(Path('work/scripts').resolve()))
import build_readers,mechanical_repairs,editorial,fitz
from texenv import environment
D=Path('work/layout_probes');records=[];jobs=[]
for lang in ('fr','en'):
    package='LM_C3-644-662';raw=build_readers.raw_package(package,lang)
    heading=r'\uline{Remarques}' if lang=='fr' else r'\uline{Remarks}'
    start=raw.index(heading,raw.index(r'\scanpage{656}'))
    deletion=raw.index(r'\deleted{',start)
    stop=editorial.brace_end(raw,deletion+len(r'\deleted'))
    old=raw[start:stop]
    new=r'\Needspace{10\baselineskip}'+'\n'+old
    records.append(dict(id='140-3-656-HRemarks',language=lang,package=package,cote='140-3',scan=656,source_line=raw.count('\n',0,start)+1,old=old,new=new,expected_match_count=1,kind='section-heading pagination',reason='Reserve ten current baselines before the existing Remarks opening so the heading is followed by substantive opening content in all three forms, including when the first paragraph is cancelled. Preserve the entire heading and cancellation, normal paragraph mode, all source words and mathematics.'))
    text,_=mechanical_repairs.repair(raw,package,lang)
    a=text.index(heading,text.index(r'\scanpage{656}'))
    b=text.index(r'\uline{',a+len(heading))
    original=text[a:b]
    assert original.count(old)==1
    for label,source in [('before',original),('after',original.replace(old,new))]:
        body,_,_=editorial.annotate(r'\scanpage{656}'+source,package,lang)
        body=body.replace(r'\scanpage{656}','',1)
        parts=[build_readers.preamble(lang,1),r'\begin{document}\LMcote{140-3}']
        for form in (0,1,2):
            parts += [f'\\clearpage\\LMform={form}\n'+r'\noindent Preceding material.\par\vspace*{\dimexpr\textheight-60pt\relax}\par\penalty0',body]
        parts.append(r'\end{document}')
        path=D/f'scan656_remarks_{lang}_{label}.tex';path.write_text('\n'.join(parts))
        jobs.append((lang,label,path,subprocess.Popen(['lualatex','--no-shell-escape','-interaction=nonstopmode','-halt-on-error',path.name],cwd=D,env=environment(),stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)))
(D/'scan656_remarks_candidate.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
results=[]
for lang,label,path,job in jobs:
    stdout,_=job.communicate();path.with_suffix('.console.txt').write_text(stdout);log=path.with_suffix('.log').read_text(errors='replace')
    counts=dict(exit=job.returncode,overfull=log.count('Overfull'),missing=log.count('Missing character'));print(lang,label,counts,flush=True)
    if job.returncode:print(stdout[-2000:]);raise SystemExit(job.returncode)
    doc=fitz.open(path.with_suffix('.pdf'));rows=[]
    for i,page in enumerate(doc):
        text=page.get_text();hasheading=('Remarques' if lang=='fr' else 'Remarks') in text
        hasopening='projection' in text
        row=dict(page=i+1,heading=hasheading,opening=hasopening)
        if hasheading:
            out=D/f'scan656_remarks_{lang}_{label}_p{i+1:02}.png';page.get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(out)
            row.update(image=str(out),image_sha256=hashlib.sha256(out.read_bytes()).hexdigest())
        rows.append(row)
    results.append(dict(language=lang,version=label,compile=counts,pdf=str(path.with_suffix('.pdf')),pdf_sha256=hashlib.sha256(path.with_suffix('.pdf').read_bytes()).hexdigest(),pages=rows,status='PENDING_ACTUAL_VISUAL'))
(D/'scan656_remarks_validation.json').write_text(json.dumps(dict(status='PENDING_ACTUAL_VISUAL',probes=results),ensure_ascii=False,indent=2)+'\n')
