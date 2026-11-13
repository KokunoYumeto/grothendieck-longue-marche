from pathlib import Path
import sys, json, subprocess, hashlib
sys.path.insert(0, str(Path('work/scripts').resolve()))
import build_readers, mechanical_repairs, layout_repairs, editorial, fitz
from texenv import environment
D = Path('work/layout_probes')
jobs, records = [], []
for lang in ('fr', 'en'):
    package = 'LM_C3-644-662'
    text = build_readers.raw_package(package, lang)
    text, _ = mechanical_repairs.repair(text, package, lang)
    text, _ = layout_repairs.repair(text, package, lang, include_pagination=False)
    anchor = text.index(r'(59)\quad1', text.index(r'\scanpage{649}'))
    start = text.rindex(r'\begin{tikzcd}', 0, anchor)
    end = text.index(r'\end{tikzcd}', anchor) + len(r'\end{tikzcd}')
    old = text[start:end]
    label = r'"\inserted{\mathrm{\acute{e}pi}}"]'
    assert old.count(label) == 1
    new = old.replace(label, r'"\inserted{\mathrm{\acute{e}pi}}"{yshift=3pt}]')
    records.append(dict(id='140-3-649-V59', language=lang, package=package, scan=649, tag='59', old=old, new=new,
      reason='Raise only the existing inserted epi label by3pt so its p clears the upper arrowhead barb. Preserve all words, insertion and deletion wrappers, objects, endpoints, matrix spacing and type size.'))
    parts = [build_readers.preamble(lang, 1), r'\begin{document}\LMcote{140-3}']
    for version, fragment in [('before', old), ('after', new)]:
        body, _, _ = editorial.annotate(r'\scanpage{649}\diagram{' + fragment + '}', package, lang)
        for form in (0, 1, 2):
            parts.append(f'\\clearpage\\LMform={form}\n' + body)
    parts.append(r'\end{document}')
    path = D / f'scan649_epi59_{lang}.tex'
    path.write_text('\n'.join(parts))
    jobs.append((lang, path, subprocess.Popen(['lualatex', '--no-shell-escape', '-interaction=nonstopmode', '-halt-on-error', path.name], cwd=D, env=environment(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)))
(D/'scan649_epi59_candidate.json').write_text(json.dumps(records, ensure_ascii=False, indent=2)+'\n')
results=[]
for lang,path,job in jobs:
    stdout,_=job.communicate();path.with_suffix('.console.txt').write_text(stdout)
    log=path.with_suffix('.log').read_text(errors='replace')
    counts=dict(exit=job.returncode,overfull=log.count('Overfull'),missing=log.count('Missing character'))
    print(lang, counts, flush=True)
    if job.returncode: print(stdout[-2000:]);raise SystemExit(job.returncode)
    doc=fitz.open(path.with_suffix('.pdf'));assert len(doc)==6
    for i,page in enumerate(doc):
        version='before' if i<3 else 'after';form=i%3
        bodywords=[w for w in page.get_text('words') if 85 < w[1] < 300]
        rect=fitz.Rect(min(w[0] for w in bodywords)-15,min(w[1] for w in bodywords)-10,max(w[2] for w in bodywords)+15,max(w[3] for w in bodywords)+15)
        out=D/f'scan649_epi59_{lang}_{form}_{version}_context4x.png'
        page.get_pixmap(matrix=fitz.Matrix(4,4),clip=rect).save(out)
        words=[w for w in page.get_text('words') if 'pi' in w[4]]
        labelrect=fitz.Rect(words[0][:4])+(-8,-5,12,15)
        close=D/f'scan649_epi59_{lang}_{form}_{version}_14x.png'
        page.get_pixmap(matrix=fitz.Matrix(14,14),clip=labelrect).save(close)
        results.append(dict(language=lang,form=form,version=version,compile=counts,pdf=str(path.with_suffix('.pdf')),pdf_sha256=hashlib.sha256(path.with_suffix('.pdf').read_bytes()).hexdigest(),page=i+1,image=str(out),image_sha256=hashlib.sha256(out.read_bytes()).hexdigest(),detail=str(close),detail_sha256=hashlib.sha256(close.read_bytes()).hexdigest(),status='PENDING_ACTUAL_VISUAL'))
(D/'scan649_epi59_validation.json').write_text(json.dumps(dict(status='PENDING_ACTUAL_VISUAL',forms=results),ensure_ascii=False,indent=2)+'\n')
