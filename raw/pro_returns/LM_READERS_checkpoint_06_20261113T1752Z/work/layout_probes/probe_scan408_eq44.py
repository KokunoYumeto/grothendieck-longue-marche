"""Paired source-local gap probe; no frozen source/module mutation."""
from pathlib import Path
import hashlib, json, subprocess, sys
sys.path.insert(0, str(Path('work/scripts').resolve()))
import build_readers, editorial, mechanical_repairs, fitz
from texenv import environment

D = Path('work/layout_probes')
package = 'LM_C3-397-415'
jobs = []
records = []
for lang in ('fr', 'en'):
    text = build_readers.raw_package(package, lang)
    text, _ = mechanical_repairs.repair(text, package, lang)
    start = text.index(r'\scanpage{408}')
    start = text.index(r'\noindent$(44)$', start)
    start = text.index(r'\begin{tikzcd}', start)
    end = text.index(r'\end{tikzcd}', start) + len(r'\end{tikzcd}')
    old = text[start:end]
    before = r'\&\{1,\tau_\infty\}'
    after = r'\&[30pt]\{1,\tau_\infty\}'
    assert old.count(before) == 1
    assert old.count(r'\&D_4') == 1
    new = old.replace(before, after).replace(r'\&D_4', r'\&[10pt]D_4')
    records.append(dict(language=lang, package=package, scan=408, tag='44', old=old, new=new,
                        reason='Add10pt to the first gap and30pt to the second. The unchanged two-line projection label then clears the first lower barb, and the homomorphism/canonical labels fit between the second arrow endpoints and clear its barbs and target brace. Preserve font size, labels, endpoints, matrix rows and outer height.'))
    for variant, snippet in [('before', old), ('after', new)]:
        body, *_ = editorial.annotate(r'\scanpage{408}\diagram{' + snippet + '}', package, lang)
        parts = [build_readers.preamble(lang, 1), r'\begin{document}\LMcote{140-3}']
        for form in (0, 1, 2):
            parts += [rf'\clearpage\LMform={form}', body]
        parts += [r'\end{document}']
        target = D / f'scan408_eq44_{variant}_{lang}.tex'
        target.write_text('\n'.join(parts))
        job = subprocess.Popen(['lualatex', '--no-shell-escape', '-interaction=nonstopmode', '-halt-on-error', target.name],
                               cwd=D, env=environment(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        jobs.append((lang, variant, target, job))
(D / 'scan408_eq44_candidate.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
proof = []
for lang, variant, target, job in jobs:
    output, _ = job.communicate()
    target.with_suffix('.console.txt').write_text(output)
    log = target.with_suffix('.log').read_text(errors='replace')
    counts = dict(exit=job.returncode, overfull=log.count('Overfull'), missing=log.count('Missing character'))
    print(lang, variant, counts, flush=True)
    assert counts == dict(exit=0, overfull=0, missing=0)
    doc = fitz.open(target.with_suffix('.pdf'))
    assert len(doc) == 3
    for form, page in enumerate(doc):
        image = D / f'scan408_eq44_{variant}_{lang}_{form}.png'
        page.get_pixmap(matrix=fitz.Matrix(5, 5), clip=fitz.Rect(140, 80, 460, 155)).save(image)
        proof.append(dict(language=lang, variant=variant, form=form, compile=counts,
                          image=image.as_posix(), image_sha256=hashlib.sha256(image.read_bytes()).hexdigest(), status='PENDING_VISUAL'))
(D / 'scan408_eq44_validation.json').write_text(json.dumps(dict(status='PENDING_VISUAL', forms=proof), ensure_ascii=False, indent=2) + '\n')
