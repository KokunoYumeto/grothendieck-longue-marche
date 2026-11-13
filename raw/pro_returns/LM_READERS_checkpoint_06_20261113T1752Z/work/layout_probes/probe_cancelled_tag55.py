"""Keep the author-cancelled tag argument; omit only generated parentheses."""
from pathlib import Path
import hashlib, json, re, subprocess, sys
sys.path.insert(0, str(Path('work/scripts').resolve()))
import build_readers, editorial, fitz
from texenv import environment

D = Path('work/layout_probes')
definition = r'\newcommand\LMcancelledtag[1]{\ifnum\LMform=0\tag{#1}\else\tag*{#1}\fi}'
before = r'\tag{\deleted{55}}'
after = r'\LMcancelledtag{\deleted{55}}'
jobs = []
records = []
for lang in ('fr', 'en'):
    package = 'LM_C3-359-377'
    raw = build_readers.raw_package(package, lang)
    i = raw.index(before)
    scan = int(list(re.finditer(r'\\scanpage\{(\d+)\}', raw[:i]))[-1][1])
    start = raw.rfind(r'\[', 0, i)
    end = raw.index(r'\]', i) + 2
    old = raw[start:end]
    new = old.replace(before, after)
    old_ann, old_entries, _ = editorial.annotate(r'\scanpage{' + str(scan) + '}' + old, package, lang)
    new_ann, new_entries, _ = editorial.annotate(r'\scanpage{' + str(scan) + '}' + new, package, lang)
    stable = lambda es: [(e['id'], e['kind'], e['manuscript'], e['corrected']) for e in es]
    assert stable(old_entries) == stable(new_entries)
    assert old_ann.count(r'\var{') == new_ann.count(r'\var{') == 2
    records.append(dict(language=lang, package=package, scan=scan, source_line=raw[:i].count('\n')+1,
                        old=before, new=after, macro_definition=definition,
                        reason='The entire tag55 is explicitly cancelled in the source. Preserve its unchanged deleted argument and single annotated variant occurrence; use the unparenthesized AMS tag only in corrected forms to remove synthetic empty parentheses. Retain the diplomatic parenthesized cancelled55.',
                        original_readings_unchanged=True, variant_count=2,
                        evidence='work/build/LM_EN_corrected_apparatus.pdf physical888'))
    for variant, body in [('before', old_ann), ('after', new_ann)]:
        parts = [build_readers.preamble(lang, 1), definition, r'\begin{document}\LMcote{140-3}']
        for form in (0, 1, 2):
            parts += [rf'\clearpage\LMform={form}', r'\noindent Preceding source text.', body,
                      r'\noindent Following source text.']
        parts += [r'\end{document}']
        target = D / f'cancelled_tag55_{variant}_{lang}.tex'
        target.write_text('\n'.join(parts))
        job = subprocess.Popen(['lualatex', '--no-shell-escape', '-interaction=nonstopmode', '-halt-on-error', target.name],
                               cwd=D, env=environment(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        jobs.append((lang, variant, target, job))
(D / 'cancelled_tag55_candidate.json').write_text(json.dumps(records, ensure_ascii=False, indent=2)+'\n')
rows = []
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
        image = D / f'cancelled_tag55_{variant}_{lang}_{form}.png'
        page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=fitz.Rect(65, 70, 535, 220)).save(image)
        rows.append(dict(language=lang, variant=variant, form=form, compile=counts,
                         extracted_text=page.get_text(), image=image.as_posix(),
                         image_sha256=hashlib.sha256(image.read_bytes()).hexdigest(), status='PENDING_VISUAL'))
(D / 'cancelled_tag55_validation.json').write_text(json.dumps(dict(status='PENDING_VISUAL', forms=rows), ensure_ascii=False, indent=2)+'\n')
