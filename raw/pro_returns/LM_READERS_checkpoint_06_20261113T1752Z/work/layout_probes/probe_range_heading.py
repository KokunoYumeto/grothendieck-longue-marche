"""Stress the generated package heading without changing frozen dependencies."""
from pathlib import Path
import hashlib, json, subprocess, sys
sys.path.insert(0, str(Path('work/scripts').resolve()))
import build_readers, fitz
from texenv import environment

D = Path('work/layout_probes')
BASELINES = 11
specs = [('LM_C4-115-133', 115, '115--133', '(267)'),
         ('LM_C4-267-280', 267, '267--280', '(107)')]
jobs = []
for lang in ('fr', 'en'):
    for variant in ('before', 'after'):
        parts = [build_readers.preamble(lang, 1), r'\begin{document}\LMcote{140-4}']
        fixtures = []
        for form in (0, 1, 2):
            for package, scan, label, tag in specs:
                body, *_ = build_readers.package_data(package, lang, 'build')
                body = body[:body.index(r'\]') + 2]
                for spare in (90, 140, 170):
                    ident = f'{lang}-{form}-{scan}-{spare}'
                    fixtures.append(dict(id=ident, language=lang, form=form, scan=scan,
                                         package=package, spare=spare, heading='Scans ' + label.replace('--', '–'), tag=tag))
                    reserve = rf'\Needspace{{{BASELINES}\baselineskip}}' if variant == 'after' else ''
                    heading = r'\ifnum\LMform<2' + reserve + r'\subsection*{Scans ' + label + r'}\fi'
                    parts += [rf'\clearpage\LMform={form}\noindent Fixture {ident}.\par',
                              rf'\vspace*{{\dimexpr\textheight-{spare}pt-\baselineskip\relax}}',
                              heading, body, r'\par\noindent Following text.\par']
        parts += [r'\end{document}']
        target = D / f'range_heading_{variant}_{lang}.tex'
        target.write_text('\n'.join(parts))
        job = subprocess.Popen(['lualatex', '--no-shell-escape', '-interaction=nonstopmode', '-halt-on-error', target.name],
                               cwd=D, env=environment(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        jobs.append((lang, variant, target, fixtures, job))

candidate = dict(old_template=r'\ifnum\LMform<2\subsection*{Scans #1}\fi',
                 new_template=rf'\ifnum\LMform<2\Needspace{{{BASELINES}\baselineskip}}\subsection*{{Scans #1}}\fi',
                 kind='generated formatting', manuscript_text_changed=False,
                 reason='Reserve space before the generated range heading for its scan/page markers and opening source content. Reading form omits the heading and reservation together.',
                 actual_witnesses='work/data/range_heading_orphans_revision512.json')
(D / 'range_heading_candidate.json').write_text(json.dumps(candidate, ensure_ascii=False, indent=2) + '\n')
rows = []
for lang, variant, target, fixtures, job in jobs:
    output, _ = job.communicate()
    target.with_suffix('.console.txt').write_text(output)
    log = target.with_suffix('.log').read_text(errors='replace')
    counts = dict(exit=job.returncode, overfull=log.count('Overfull'), missing=log.count('Missing character'))
    print(lang, variant, counts, flush=True)
    assert counts == dict(exit=0, overfull=0, missing=0)
    doc = fitz.open(target.with_suffix('.pdf'))
    texts = [p.get_text() for p in doc]
    for fixture in fixtures:
        first = next(i for i, text in enumerate(texts) if f"Fixture {fixture['id']}." in text)
        last = next(i for i in range(first, len(doc)) if 'Following text.' in texts[i])
        heading_pages = [i for i in range(first, last + 1) if fixture['heading'] in texts[i]]
        tag_pages = [i for i in range(first, last + 1) if fixture['tag'] in texts[i]]
        assert len(tag_pages) == 1, fixture
        page_no = heading_pages[0] if heading_pages else tag_pages[0]
        page = doc[page_no]
        image = D / f"range_heading_{variant}_{fixture['id']}.png"
        page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5)).save(image)
        rows.append(dict(**fixture, variant=variant, heading_pages=[i+1 for i in heading_pages],
                         opening_display_page=tag_pages[0]+1,
                         heading_with_opening_display=(fixture['form']==2 or heading_pages==tag_pages),
                         compile=counts, image=image.as_posix(),
                         image_sha256=hashlib.sha256(image.read_bytes()).hexdigest(), status='PENDING_VISUAL'))
(D / 'range_heading_validation.json').write_text(json.dumps(dict(status='PENDING_VISUAL', baselines=BASELINES, probes=rows), ensure_ascii=False, indent=2) + '\n')
print('after attachments', sum(r['heading_with_opening_display'] for r in rows if r['variant']=='after'), 'of', sum(r['variant']=='after' for r in rows), flush=True)
