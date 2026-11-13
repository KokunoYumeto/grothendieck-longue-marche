"""Stress the exact circled-item heading and its first definition in all modes."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

sys.path.insert(0, str(Path('work/scripts').resolve()))
import build_readers
import editorial
import mechanical_repairs
import layout_repairs
import fitz
from texenv import environment

D = Path('work/layout_probes')
package = 'LM_C3-416-434'
jobs = []
candidates = []
for lang in ('fr', 'en'):
    raw = build_readers.raw_package(package, lang)
    text, _ = mechanical_repairs.repair(raw, package, lang)
    text, _ = layout_repairs.repair(text, package, lang)
    start = text.index(r'\figure{\begin{tikzpicture}[baseline=(n.base)]', text.index(r'\scanpage{419}'))
    figure_end = text.index(r'\end{tikzpicture}}', start) + len(r'\end{tikzpicture}}')
    end = text.index('\n', text.index(r'\hspace*{4em}', figure_end))
    original = text[start:end]
    old = text[start:figure_end] + '\n'
    new = r'\Needspace{14\baselineskip}' + '\n' + old.rstrip('\n') + r'\par\nobreak' + '\n'
    assert raw.count(old) == text.count(old) == 1
    raw_start = raw.index(old)
    candidates.append(dict(language=lang, package=package, cote='140-3', scan=419,
                           source_line=raw[:raw_start].count('\n') + 1,
                           source_sha256=hashlib.sha256(raw.encode()).hexdigest(),
                           old=old, new=new,
                           reason='Keep the unchanged circled3-degree source figure heading and double bracket with its identity-component opening and complete sequence39. Reserve fourteen baselines locally and forbid the break immediately after the figure; later prose stays in normal flow.'))
    for variant, source in [('before', original), ('after', original.replace(old, new))]:
        body, entries, marks = editorial.annotate(r'\scanpage{419}' + source, package, lang)
        body = body.replace(r'\scanpage{419}', '', 1)
        parts = [build_readers.preamble(lang, 1), r'\begin{document}\LMcote{140-3}']
        fixtures = []
        for form in (0, 1, 2):
            for spare in (65, 145, 215):
                ident = f'{lang}-{form}-{spare}'
                fixtures.append(dict(id=ident, language=lang, form=form, spare=spare))
                parts += [rf'\clearpage\LMform={form}\noindent Fixture {ident}.\par',
                          rf'\vspace*{{\dimexpr\textheight-{spare}pt-\baselineskip\relax}}',
                          body, r'\par\noindent End of opening definition.\par']
        parts.append(r'\end{document}')
        target = D / f'scan419_circled3_{variant}_{lang}.tex'
        target.write_text('\n'.join(parts), encoding='utf-8')
        proc = subprocess.Popen(['lualatex', '--no-shell-escape', '-interaction=nonstopmode', '-halt-on-error', target.name],
                                cwd=D, env=environment(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        jobs.append((lang, variant, target, fixtures, proc))
(D/'scan419_circled3_candidate.json').write_text(json.dumps(candidates, ensure_ascii=False, indent=2)+'\n')
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
        hp = []
        for i in range(first, last+1):
            # The figure's large3 plus superscript o forms one line in text extraction.
            if any(line.strip().replace(' ', '') in ('3o', '3ᵒ') for line in texts[i].splitlines()):
                hp.append(i)
        dp = [i for i in range(first, last+1) if '(39)' in texts[i]]
        if len(hp) != 1:
            print('HEADING DETECTION', fixture, [texts[i] for i in range(first,last+1)], flush=True)
        assert len(hp) == len(dp) == 1, (fixture, hp, dp)
        page = doc[hp[0]]
        spans = [s for block in page.get_text('dict')['blocks'] if block['type']==0 for line in block['lines'] for s in line['spans']]
        hs = [s for s in spans if s['text'].strip()=='3']
        y = min(s['bbox'][1] for s in hs)
        image = D/f"scan419_circled3_{variant}_{fixture['id']}.png"
        page.get_pixmap(matrix=fitz.Matrix(3,3), clip=fitz.Rect(65,max(0,y-18),535,min(page.rect.height,y+240)), alpha=False).save(image)
        proof.append(dict(**fixture, variant=variant, compile=counts,
                          heading_page=hp[0]+1, definition_page=dp[0]+1, attached=hp==dp,
                          image=image.as_posix(), image_sha256=hashlib.sha256(image.read_bytes()).hexdigest(),
                          status='PENDING_VISUAL'))
(D/'scan419_circled3_validation.json').write_text(json.dumps(dict(status='PENDING_VISUAL', probes=proof), ensure_ascii=False, indent=2)+'\n')
