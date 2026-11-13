from pathlib import Path
import sys, json, subprocess, hashlib
sys.path.insert(0, str(Path('work/scripts').resolve()))
import build_readers, mechanical_repairs, layout_repairs, editorial, fitz
from texenv import environment
from PIL import Image, ImageDraw

D = Path('work/layout_probes')
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
sites = [
    dict(site='653', package='LM_C3-644-662', cote='140-3', scan=653,
         identifier='140-3-653-H2', baselines=14, remaining=[60, 160, 240]),
    dict(site='032', package='LM_C4-020-038', cote='140-4', scan=32,
         identifier='140-4-32-HTheorem', baselines=24, remaining=[60, 260, 360]),
]
jobs = []
for cfg in sites:
    records = []
    for lang in ('fr', 'en'):
        raw = build_readers.raw_package(cfg['package'], lang)
        heading = r'$2^\circ)$' if cfg['site'] == '653' else (r'\uline{Théorème}' if lang == 'fr' else r'\uline{Theorem}')
        a = raw.index(heading, raw.index(r'\scanpage{' + str(cfg['scan']) + '}'))
        b = raw.index('\n', a)
        old = raw[a:b]
        new = r'\Needspace{' + str(cfg['baselines']) + r'\baselineskip}' + '\n' + old
        reason = ('Reserve fourteen current baselines before the unchanged item2 heading so its opening word and complete definition4 remain with it; preserve all source words, marks, formula geometry and normal paragraph flow.' if cfg['site'] == '653' else 'Reserve twenty-four current baselines before the unchanged theorem heading to retain its intervening tall marginal source sketch and first theorem assertion on the same page; preserve the note in its existing normal rendering flow and all source content.')
        records.append(dict(id=cfg['identifier'], language=lang, package=cfg['package'],
                            cote=cfg['cote'], scan=cfg['scan'], source_line=raw.count('\n', 0, a)+1,
                            old=old, new=new, expected_match_count=1,
                            kind='section-heading pagination', reason=reason))
        text, _ = mechanical_repairs.repair(raw, cfg['package'], lang)
        text, _ = layout_repairs.repair(text, cfg['package'], lang, include_pagination=False)
        a = text.index(heading, text.index(r'\scanpage{' + str(cfg['scan']) + '}'))
        if cfg['site'] == '653':
            b = text.index(r'\]', a)+2
        else:
            b = text.index(r'\margin{31}', a)
        original = text[a:b]
        assert original.count(old) == 1
        for version, source in [('before', original), ('after', original.replace(old, new))]:
            body, _, _ = editorial.annotate(r'\scanpage{' + str(cfg['scan']) + '}' + source, cfg['package'], lang)
            body = body.replace(r'\scanpage{' + str(cfg['scan']) + '}', '', 1)
            parts = [build_readers.preamble(lang, 1), r'\begin{document}\LMcote{' + cfg['cote'] + '}']
            placements = []
            for remaining in cfg['remaining']:
                for form in (0, 1, 2):
                    parts += [f'\\clearpage\\LMform={form}\n' + r'\noindent Preceding material.\par\vspace*{\dimexpr\textheight-' + str(remaining) + r'pt\relax}\par\penalty0', body]
                    placements.append(dict(form=form, remaining_page_height_pt=remaining))
            parts.append(r'\end{document}')
            path = D / f'heading{cfg["site"]}_{lang}_{version}.tex'
            path.write_text('\n'.join(parts))
            jobs.append((cfg, lang, version, path, placements, subprocess.Popen(
                ['lualatex', '--no-shell-escape', '-interaction=nonstopmode', '-halt-on-error', path.name],
                cwd=D, env=environment(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)))
    (D / f'heading{cfg["site"]}_candidate.json').write_text(json.dumps(records, ensure_ascii=False, indent=2)+'\n')

results = {cfg['site']: [] for cfg in sites}
for cfg, lang, version, path, placements, job in jobs:
    stdout, _ = job.communicate()
    path.with_suffix('.console.txt').write_text(stdout)
    log = path.with_suffix('.log').read_text(errors='replace')
    counts = dict(exit=job.returncode, overfull=log.count('Overfull'), missing=log.count('Missing character'))
    print(cfg['site'], lang, version, counts, flush=True)
    if job.returncode:
        print(stdout[-2500:]); raise SystemExit(job.returncode)
    doc = fitz.open(path.with_suffix('.pdf')); rows = []
    for i, page in enumerate(doc):
        txt = page.get_text()
        hasheading = ('2°)' in txt or '2◦)' in txt or '2∘)' in txt) if cfg['site'] == '653' else (('Théorème' if lang == 'fr' else 'Theorem') in txt)
        if not hasheading:
            continue
        # The manuscript item numeral is font-dependent in PDF text; the
        # authoritative full raster is retained with the extracted page.
        words = [w for w in page.get_text('words') if 65 < w[1] < 770 and w[4] not in ('Preceding', 'material.')]
        y0 = min(w[1] for w in words); y1 = max(w[3] for w in words)
        out = D / f'heading{cfg["site"]}_{lang}_{version}_p{i+1:02}.png'
        page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False).save(out)
        detail = D / f'heading{cfg["site"]}_{lang}_{version}_p{i+1:02}_opening3x.png'
        page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=fitz.Rect(55, max(45, y0-12), 595.276, min(790, y1+12)), alpha=False).save(detail)
        rows.append(dict(**placements[len(rows)], page=i+1, image=str(out), image_sha256=sha(out),
                         detail=str(detail), detail_sha256=sha(detail),
                         page_text=txt, status='PENDING_ACTUAL_VISUAL'))
    if len(rows) != 9:
        print('Unexpected heading pages:', len(rows), [p.get_text()[:160] for p in doc]); raise SystemExit(2)
    if version == 'after':
        for remaining in cfg['remaining']:
            selected = [r for r in rows if r['remaining_page_height_pt'] == remaining]
            ims = [Image.open(r['detail']).convert('RGB') for r in selected]
            canvas = Image.new('RGB', (max(im.width for im in ims), sum(im.height+38 for im in ims)), (230,230,230))
            dr = ImageDraw.Draw(canvas); y = 0
            for row, im in zip(selected, ims):
                dr.text((10,y+8), f'{cfg["site"]} {lang} form{row["form"]}, remaining{remaining}pt — actual native3x', fill='black')
                canvas.paste(im, (0,y+38)); y += im.height+38
            canvas.save(D / f'heading{cfg["site"]}_{lang}_after_remaining{remaining}_3x.png')
    results[cfg['site']].append(dict(language=lang, version=version, compile=counts,
        pdf=str(path.with_suffix('.pdf')), pdf_sha256=sha(path.with_suffix('.pdf')),
        probe_pdf_delivery_status='HISTORICAL_PROBE_NOT_DELIVERED_AS_PUBLICATION',
        pages=rows, status='PENDING_ACTUAL_VISUAL'))
for cfg in sites:
    (D / f'heading{cfg["site"]}_validation.json').write_text(json.dumps(dict(
        status='PENDING_ACTUAL_VISUAL', forms_per_language=3, stressed_placements=cfg['remaining'],
        source_changes='Exact Needspace prefix only; no boxing, word/math/mark removal, font change or diagram-geometry change.',
        probes=results[cfg['site']]), ensure_ascii=False, indent=2)+'\n')
