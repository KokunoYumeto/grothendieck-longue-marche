"""Paired position-only probe for the two retained blue uncertainty labels."""
from pathlib import Path
import hashlib, json, re, subprocess, sys
sys.path.insert(0, str(Path('work/scripts').resolve()))
import build_readers, editorial, mechanical_repairs, layout_repairs, fitz
from texenv import environment

D = Path('work/layout_probes')
records, jobs, proof = [], [], []
package, scan = 'LM_C3-625-643', 637
before = r'"{\unsure{\searrow}}"{pos=.93}'
after = r'"{\unsure{\searrow}}"{pos=.93,xshift=10pt,yshift=-6pt}'
for lang in ('fr', 'en'):
    text = build_readers.raw_package(package, lang)
    text, _ = mechanical_repairs.repair(text, package, lang)
    text, _ = layout_repairs.repair(text, package, lang)
    a, b = next((a, b) for n, a, b in layout_repairs._scan_ranges(text) if n == scan)
    old = next(m[0] for m in re.finditer(r'\\begin\{tikzcd\}.*?\\end\{tikzcd\}', text[a:b], re.S) if '(37)' in m[0])
    assert old.count(before) == 1
    new = old.replace(before, after)
    records.append(dict(language=lang, package=package, scan=scan, tag='37', old=old, new=new,
        reason='Shift only the existing uncertain southeast-arrow glyph10pt right and6pt down, separating it from the unchanged uncertain product label. Preserve both uncertainty macros, all object and arrow text, endpoints, routes, sizes and the previously repaired degree positions.'))
    body, entries, meta = editorial.annotate(r'\scanpage{637}\diagram{' + new + '}', package, lang)
    parts = [build_readers.preamble(lang, 1), r'\begin{document}\LMcote{140-3}']
    for form in (0, 1, 2):
        parts.append(f'\\clearpage\\LMform={form}\n' + body)
    parts.append(r'\end{document}')
    target = D / f'scan637_blue_note_{lang}.tex'
    target.write_text('\n'.join(parts))
    jobs.append((lang, target, subprocess.Popen(['lualatex', '--no-shell-escape', '-interaction=nonstopmode', '-halt-on-error', target.name], cwd=D, env=environment(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)))
(D / 'scan637_blue_note_candidate.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
for lang, target, job in jobs:
    output, _ = job.communicate()
    target.with_suffix('.console.txt').write_text(output)
    log = target.with_suffix('.log').read_text(errors='replace')
    counts = dict(exit=job.returncode, overfull=log.count('Overfull'), missing=log.count('Missing character'))
    print(lang, counts, flush=True)
    assert counts == dict(exit=0, overfull=0, missing=0)
    doc = fitz.open(target.with_suffix('.pdf'))
    assert len(doc) == 3
    for form, page in enumerate(doc):
        content = page.get_text('blocks')
        bounds = fitz.Rect(65, 85, 525, 310)
        image = D / f'scan637_blue_note_{lang}_{form}.png'
        page.get_pixmap(matrix=fitz.Matrix(4, 4), clip=bounds).save(image)
        proof.append(dict(language=lang, form=form, compile=counts, image=image.as_posix(), image_sha256=hashlib.sha256(image.read_bytes()).hexdigest(), status='PENDING_VISUAL'))
(D / 'scan637_blue_note_validation.json').write_text(json.dumps(dict(status='PENDING_VISUAL', forms=proof), ensure_ascii=False, indent=2) + '\n')
