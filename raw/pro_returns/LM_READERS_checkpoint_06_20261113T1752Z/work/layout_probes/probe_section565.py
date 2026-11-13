"""Bind the source item heading to its opening definition, locally."""
from pathlib import Path
import hashlib, json, subprocess, sys
sys.path.insert(0, str(Path('work/scripts').resolve()))
import build_readers, editorial, mechanical_repairs, layout_repairs, fitz
from texenv import environment

D = Path('work/layout_probes')
jobs = []; candidates = []
for lang in ('fr', 'en'):
    package = 'LM_C3-549-567'
    raw = build_readers.raw_package(package, lang)
    text, _ = mechanical_repairs.repair(raw, package, lang)
    text, _ = layout_repairs.repair(text, package, lang)
    start = text.index('6°) \\uline{', text.index(r'\scanpage{565}'))
    end = text.index(r'\]', start) + 2
    original = text[start:end]
    heading = original.split('\n\n', 1)[0]
    old = heading + '\n\n'
    new = r'\Needspace{14\baselineskip}' + '\n' + heading + r'\par\nobreak' + '\n'
    assert original.count(old) == raw.count(old) == 1
    rawindex = raw.index(old)
    candidates.append(dict(language=lang, package=package, cote='140-3', scan=565,
                           source_line=raw[:rawindex].count('\n') + 1, old=old, new=new,
                           reason='Keep the unchanged item6 heading with its opening We put/On pose definition68. Reserve fourteen baselines before the heading and forbid a break immediately after it; the remainder of the section stays in normal flow.'))
    for variant, source in [('before', original), ('after', original.replace(old, new))]:
        body, entries, _ = editorial.annotate(r'\scanpage{565}' + source, package, lang)
        body = body.replace(r'\scanpage{565}', '', 1)
        parts = [build_readers.preamble(lang, 1), r'\begin{document}\LMcote{140-3}']
        fixtures = []
        for form in (0, 1, 2):
            for spare in (60, 130, 190):
                ident = f'{lang}-{form}-{spare}'
                fixtures.append(dict(id=ident, language=lang, form=form, spare=spare))
                parts += [rf'\clearpage\LMform={form}\noindent Fixture {ident}.\par',
                          rf'\vspace*{{\dimexpr\textheight-{spare}pt-\baselineskip\relax}}',
                          body, r'\par\noindent End of opening definition.\par']
        parts += [r'\end{document}']
        target = D / f'section565_{variant}_{lang}.tex'
        target.write_text('\n'.join(parts))
        proc = subprocess.Popen(['lualatex', '--no-shell-escape', '-interaction=nonstopmode', '-halt-on-error', target.name],
                                cwd=D, env=environment(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        jobs.append((lang, variant, target, fixtures, proc))
(D / 'section565_candidate.json').write_text(json.dumps(candidates, ensure_ascii=False, indent=2) + '\n')
proof = []
for lang, variant, target, fixtures, proc in jobs:
    stdout, _ = proc.communicate()
    target.with_suffix('.console.txt').write_text(stdout)
    log = target.with_suffix('.log').read_text(errors='replace')
    counts = dict(exit=proc.returncode, overfull=log.count('Overfull'), missing=log.count('Missing character'))
    print(lang, variant, counts, flush=True)
    assert counts == dict(exit=0, overfull=0, missing=0)
    doc = fitz.open(target.with_suffix('.pdf'))
    texts = [page.get_text() for page in doc]
    for fixture in fixtures:
        first = next(i for i, text in enumerate(texts) if f"Fixture {fixture['id']}." in text)
        last = next(i for i in range(first, len(doc)) if 'End of opening definition.' in texts[i])
        heading = "L’ensemble" if lang == 'fr' else 'The set'
        hp = [i for i in range(first, last + 1) if heading in texts[i]]
        dp = [i for i in range(first, last + 1) if '(68)' in texts[i]]
        assert len(hp) == len(dp) == 1
        page = doc[hp[0]]
        spans = [s for b in page.get_text('dict')['blocks'] if b['type'] == 0 for line in b['lines'] for s in line['spans']]
        hs = [s for s in spans if heading in s['text']]
        y = min(s['bbox'][1] for s in hs)
        clip = fitz.Rect(65, max(0, y-12), 535, min(page.rect.height, y+245))
        image = D / f"section565_{variant}_{fixture['id']}.png"
        page.get_pixmap(matrix=fitz.Matrix(2, 2), clip=clip).save(image)
        proof.append(dict(**fixture, variant=variant, compile=counts,
                          heading_page=hp[0]+1, definition_page=dp[0]+1,
                          attached=hp==dp, image=image.as_posix(),
                          image_sha256=hashlib.sha256(image.read_bytes()).hexdigest(), status='PENDING_VISUAL'))
(D / 'section565_validation.json').write_text(json.dumps(dict(status='PENDING_VISUAL', probes=proof), ensure_ascii=False, indent=2) + '\n')
