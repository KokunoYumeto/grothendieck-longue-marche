"""Probe a generated retained-uncertainty heading without changing the frozen build."""
from pathlib import Path
import hashlib, json, subprocess, sys
sys.path.insert(0, str(Path('work/scripts').resolve()))
import build_readers, fitz
from texenv import environment

D = Path('work/layout_probes')
old = (r'\par\smallskip\begingroup\footnotesize\noindent\textcolor{gray}{\rule{.2\linewidth}{.35pt}}\par'
       '\n' + r'\noindent\textit{\LMdoubtheading.}\par')
new = (r'\par\smallskip\begingroup\footnotesize\Needspace{4\baselineskip}'
       r'\csname @beginparpenalty\endcsname=10000\relax'
       r'\noindent\textcolor{gray}{\rule{.2\linewidth}{.35pt}}\par\nobreak'
       '\n' + r'\noindent\textit{\LMdoubtheading.}\par\nobreak')
jobs, rows = [], []
for lang in ('fr', 'en'):
    annotated, entries, meta, provenance = build_readers.package_data('LM_P04', lang, 'build')
    selected = [e for e in entries if int(e['scan']) == 36]
    body = build_readers.apparatus(selected, lang)
    assert body.count(old) == 1
    for variant in ('before', 'after'):
        actual = body if variant == 'before' else body.replace(old, new)
        parts = [build_readers.preamble(lang, 2), r'\begin{document}\LMcote{140-2}\scanpage{36}']
        for spare in (28, 35, 42, 50):
            parts.append(r'\clearpage\noindent Preceding material.\par'
                         + f'\\vspace*{{\\dimexpr\\textheight-{spare}pt-\\baselineskip\\relax}}\n'
                         + actual + r'\par\noindent Following text.\par')
        parts.append(r'\end{document}')
        target = D / f'retained_heading_{variant}_{lang}.tex'
        target.write_text('\n'.join(parts))
        jobs.append((lang, variant, target, subprocess.Popen(
            ['lualatex', '--no-shell-escape', '-interaction=nonstopmode', '-halt-on-error', target.name],
            cwd=D, env=environment(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)))
(D / 'retained_heading_candidate.json').write_text(json.dumps(dict(
    old_generated_prefix=old, new_generated_prefix=new,
    reason='Keep the generated retained-uncertainty rule and heading with the first unchanged entry. Reserve four small-type baselines and prohibit breaks after rule/heading; leave later entries and long content breakable.',
    manuscript_text_changed=False, affects_forms=[2]), ensure_ascii=False, indent=2) + '\n')
for lang, variant, target, job in jobs:
    output, _ = job.communicate(); target.with_suffix('.console.txt').write_text(output)
    log = target.with_suffix('.log').read_text(errors='replace')
    counts = dict(exit=job.returncode, overfull=log.count('Overfull'), missing=log.count('Missing character'))
    print(lang, variant, counts, flush=True)
    assert counts == dict(exit=0, overfull=0, missing=0)
    doc = fitz.open(target.with_suffix('.pdf'))
    heading = 'Doutes conservés' if lang == 'fr' else 'Uncertainty retained'
    for i, page in enumerate(doc):
        text = page.get_text()
        if heading not in text: continue
        rect = next(r for r in page.search_for(heading))
        image = D / f'retained_heading_{variant}_{lang}_p{i+1:02}.png'
        clip = fitz.Rect(65, max(65, rect.y0-25), 530, min(800, rect.y1+85))
        page.get_pixmap(matrix=fitz.Matrix(2.5,2.5),clip=clip).save(image)
        rows.append(dict(language=lang,variant=variant,page=i+1,
            first_entry_same_page='140-2-s036-D002' in text, compile=counts,
            image=image.as_posix(),image_sha256=hashlib.sha256(image.read_bytes()).hexdigest(),status='PENDING_VISUAL'))
(D / 'retained_heading_validation.json').write_text(json.dumps(dict(status='PENDING_VISUAL',probes=rows),ensure_ascii=False,indent=2)+'\n')
