"""Source-qualified local range reservation probe; shared inputs stay frozen."""
from pathlib import Path
import concurrent.futures
import hashlib
import json
import subprocess
import sys

sys.path.insert(0, str(Path('work/scripts').resolve()))
import build_readers
import fitz
from texenv import environment
from verify_pdf import parse_log

ROOT = Path.cwd()
OUT = ROOT / 'work/layout_probes'
PACKAGE = 'LM_C4-134-152'
OLD = r'\ifnum\LMform<2\Needspace{11\baselineskip}\subsection*{Scans 134--152}\fi'
NEW = r'\ifnum\LMform<2\Needspace{\dimexpr123mm+11\baselineskip\relax}\subsection*{Scans 134--152}\fi'
SPARES = (140, 400, 490, 530)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rel(path):
    return path.relative_to(ROOT).as_posix()


def run(job):
    language, variant, target, fixtures = job
    proc = subprocess.run(['lualatex', '--no-shell-escape', '-interaction=nonstopmode',
                           '-halt-on-error', target.name], cwd=OUT, env=environment(),
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    target.with_suffix('.console.txt').write_text(proc.stdout)
    log = parse_log(target.with_suffix('.log'))
    if proc.returncode:
        raise RuntimeError('Range134 probe failed: ' + target.name)
    rows = []
    with fitz.open(target.with_suffix('.pdf')) as pdf:
        texts = [p.get_text() for p in pdf]
        for fixture in fixtures:
            first = next(i for i, text in enumerate(texts) if 'Fixture ' + fixture['id'] + '.' in text)
            last = next(i for i in range(first, len(pdf)) if 'Following text.' in texts[i])
            headings = [i + 1 for i in range(first, last + 1) if 'Scans 134–152' in texts[i]]
            strokes = []
            for i in range(first, last + 1):
                for path in pdf[i].get_drawings():
                    rect = fitz.Rect(path['rect'])
                    if 345 < rect.height < 355 and rect.width < 20:
                        strokes.append({'page': i + 1, 'bbox': list(rect)})
            assert len(strokes) == 1, (fixture, strokes)
            assert len(headings) == (0 if fixture['form'] == 2 else 1), (fixture, headings)
            pages = sorted(set(headings + [strokes[0]['page']]))
            images = []
            for number in pages:
                image = OUT / (target.stem + '_' + fixture['id'] + '_p' + str(number) + '.png')
                pdf[number - 1].get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False).save(image)
                images.append({'path': rel(image), 'sha256': sha(image), 'page': number,
                               'basis': 'Native1.5x complete constrained-foot proof page'})
            rows.append({**fixture, 'variant': variant, 'heading_pages': headings,
                         'first_source_stroke': strokes[0], 'images': images,
                         'heading_with_first_complete_source_item': fixture['form'] == 2 or headings == [strokes[0]['page']],
                         'status': 'PENDING_ACTUAL_VISUAL_REVIEW'})
    report = {'language': language, 'variant': variant, 'pdf': rel(target.with_suffix('.pdf')),
              'pdf_sha256': sha(target.with_suffix('.pdf')), 'tex_sha256': sha(target),
              'compile_exit_code': proc.returncode, 'error_count': log['error_count'],
              'overfull_count': log['overfull_count'], 'missing_character_count': log['missing_character_count'],
              'log': rel(target.with_suffix('.log')), 'log_sha256': sha(target.with_suffix('.log')),
              'fixtures': rows}
    print(language, variant, 'attached', sum(r['heading_with_first_complete_source_item'] for r in rows),
          '/', len(rows), 'errors', report['error_count'], 'overfull', report['overfull_count'],
          'missing', report['missing_character_count'], flush=True)
    return report


def main():
    jobs, sources = [], []
    for language in ('fr', 'en'):
        path = ROOT / 'sources' / ('fr/texts' if language == 'fr' else 'en/packages') / (PACKAGE + ('_en' if language == 'en' else '') + '.tex')
        raw = path.read_bytes().decode('utf-8')
        start = raw.index(r'\scanpage{134}')
        end = raw.index(r'\par a)', start)
        first_item = raw[start:end]
        sources.append({'language': language, 'source_path': rel(path), 'source_sha256': sha(path),
                        'source_line': raw.count('\n', 0, start) + 1,
                        'source_offset_start': start, 'source_offset_end': end,
                        'source_byte_start': len(raw[:start].encode()), 'source_byte_end': len(raw[:end].encode()),
                        'source_prefix_exact': first_item, 'source_first_item_height': '123mm',
                        'manuscript_source_changed': False})
        for variant in ('before', 'after'):
            prefix = OLD if variant == 'before' else NEW
            parts = [build_readers.preamble(language, 1), r'\begin{document}\LMcote{140-4}']
            fixtures = []
            for form in (0, 1, 2):
                for spare in SPARES:
                    ident = f'{language}-{form}-{spare}'
                    fixtures.append({'id': ident, 'language': language, 'form': form,
                                     'spare_points': spare, 'package': PACKAGE, 'cote': '140-4', 'scan': 134})
                    parts += [rf'\clearpage\LMform={form}\noindent Fixture {ident}.\par',
                              rf'\vspace*{{\dimexpr\textheight-{spare}pt-\baselineskip\relax}}',
                              prefix, first_item, r'\par\noindent Following text.\par']
            parts.append(r'\end{document}')
            target = OUT / f'range134_heading_{variant}_{language}.tex'
            target.write_text('\n'.join(parts))
            jobs.append((language, variant, target, fixtures))
    candidate = {'id': 'GEN-RANGE-LM_C4-134-152', 'kind': 'generated formatting',
                 'package': PACKAGE, 'cote': '140-4', 'scan': 134,
                 'old_generated_prefix': OLD, 'new_generated_prefix': NEW,
                 'reservation': r'\dimexpr123mm+11\baselineskip\relax',
                 'source_qualification': sources,
                 'reason': 'Reserve the exact123mm height of this package\'s first source marginal stroke in addition to the existing11-baseline range-heading allowance. The package heading, scan marker and complete first source item must start together. Only this package receives the larger reservation, before its generated title; the reading form omits title and reservation together.',
                 'manuscript_text_changed': False, 'shared_dependencies_modified': False,
                 'integration_targets': ['work/scripts/build_readers.py', 'work/scripts/verify_sources.py',
                                         'work/scripts/record_generated_heading_repairs.py']}
    (OUT / 'range134_heading_candidate.json').write_text(json.dumps(candidate, ensure_ascii=False, indent=2) + '\n')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(run, jobs))
    report = {'status': 'PENDING_ACTUAL_VISUAL_REVIEW', 'candidate': 'work/layout_probes/range134_heading_candidate.json',
              'proofs': results, 'source_files_unchanged': all(sha(ROOT / r['source_path']) == r['source_sha256'] for r in sources),
              'shared_dependencies_modified': False, 'observations_generated_by_script': False}
    (OUT / 'range134_heading_validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    main()
