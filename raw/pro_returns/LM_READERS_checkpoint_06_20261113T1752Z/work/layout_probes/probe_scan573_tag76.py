"""Source-local figure/tag pagination candidate; frozen inputs remain untouched."""
from pathlib import Path
import concurrent.futures
import csv
import hashlib
import json
import subprocess
import sys

sys.path.insert(0, str(Path('work/scripts').resolve()))
import fitz
import build_readers
import editorial
from texenv import environment
from verify_pdf import parse_log

ROOT = Path.cwd()
OUT = ROOT / 'work/layout_probes'
EVIDENCE = ROOT / 'work/visual_repair_proofs/revision578_scan573_tag76'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rel(path):
    return path.relative_to(ROOT).as_posix()


def current_inventory():
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    readers = []
    for reader in ('LM_FR_diplomatique', 'LM_FR_corrige_apparat', 'LM_FR_texte_de_lecture',
                   'LM_EN_corrected_apparatus', 'LM_EN_reading',
                   'LM_FR_master_annotated', 'LM_EN_master_annotated'):
        path = ROOT / 'work/build' / (reader + '.pdf')
        scanmap = path.with_suffix('.lm-scans.tsv')
        with scanmap.open() as f:
            hit = next(r for r in csv.DictReader(f, delimiter='\t')
                       if r['cote'] == '140-2' and r['scan'] == '573')
        pages = [int(x) for x in hit['physical_pages'].split(',') if x]
        pdfhash = sha(path)
        images, tags = [], []
        with fitz.open(path) as pdf:
            for n in pages:
                page = pdf[n-1]
                for box in page.search_for('(76)'):
                    tags.append({'page': n, 'bbox': list(box)})
                target = EVIDENCE / (reader + '_p' + str(n).zfill(4) + '_900.png')
                page.get_pixmap(matrix=fitz.Matrix(900/page.rect.width, 900/page.rect.width), alpha=False).save(target)
                images.append({'path': rel(target), 'sha256': sha(target), 'page': n,
                               'basis': 'Full current physical page at900px'})
        readers.append({'reader': reader, 'pdf_sha256': pdfhash,
                        'tex_sha256': sha(path.with_suffix('.tex')),
                        'scan_map_sha256': sha(scanmap), 'source_pages': pages,
                        'tag_candidates': tags, 'images': images,
                        'status': 'PENDING_ACTUAL_VISUAL_REVIEW'})
    report = {'cote': '140-2', 'scan': 573, 'package': 'LM_P058', 'tag': '76',
              'status': 'PENDING_ACTUAL_VISUAL_REVIEW', 'readers': readers,
              'observations_generated_by_script': False}
    (OUT / 'scan573_tag76_current_scope.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    return report


def run(job):
    lang, form, tex = job
    proc = subprocess.run(['lualatex', '--no-shell-escape', '-interaction=nonstopmode',
                           '-halt-on-error', tex.name], cwd=OUT, env=environment(),
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    tex.with_suffix('.console.txt').write_text(proc.stdout)
    log = parse_log(tex.with_suffix('.log'))
    if proc.returncode:
        raise RuntimeError('Tag76 probe failed: ' + tex.name)
    path = tex.with_suffix('.pdf')
    images = []
    with fitz.open(path) as pdf:
        hits = [(p.number+1, box) for p in pdf for box in p.search_for('(76)')]
        for number, box in hits:
            page = pdf[number-1]
            picture_paths = [d for d in page.get_drawings() if any(item[0] == 'c' for item in d['items'])]
            target = tex.with_name(tex.stem + '_tagpage' + str(number) + '.png')
            page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False).save(target)
            images.append({'path': rel(target), 'sha256': sha(target), 'page': number,
                           'tag_bbox': list(box), 'curved_picture_paths_on_tag_page': len(picture_paths),
                           'basis': 'Native2x full-page constrained-foot proof'})
        row = {'language': lang, 'form': form, 'pdf': rel(path), 'pdf_sha256': sha(path),
               'pages': len(pdf), 'images': images, 'status': 'PENDING_ACTUAL_VISUAL_REVIEW',
               'compile_exit_code': proc.returncode, 'error_count': log['error_count'],
               'overfull_count': log['overfull_count'], 'missing_character_count': log['missing_character_count'],
               'log': rel(tex.with_suffix('.log')), 'log_sha256': sha(tex.with_suffix('.log'))}
    print(lang, form, 'tagpages', [(x['page'], x['curved_picture_paths_on_tag_page']) for x in images],
          'errors', row['error_count'], 'overfull', row['overfull_count'], 'missing', row['missing_character_count'], flush=True)
    return row


def main():
    current_inventory()
    candidates, jobs = [], []
    for language in ('fr', 'en'):
        path = ROOT / 'sources' / ('fr/texts' if language == 'fr' else 'en/packages') / ('LM_P058' + ('_en' if language == 'en' else '') + '.tex')
        source = path.read_bytes().decode('utf-8')
        start = source.index('(76) \\figure{', source.index(r'\scanpage{573}'))
        figure = source.index(r'\figure{', start)
        end = editorial.brace_end(source, figure + len(r'\figure'))
        rawold = source[start:end]
        old = rawold.replace('\r\n', '\n')
        new = '\\begin{samepage}\n' + old + '\n\\end{samepage}'
        assert new.removeprefix('\\begin{samepage}\n').removesuffix('\n\\end{samepage}') == old
        candidates.append({'id': '140-2-573-K76figure', 'language': language, 'package': 'LM_P058',
                           'cote': '140-2', 'scan': 573, 'tag': '76', 'source_path': rel(path),
                           'source_sha256': sha(path), 'source_line': source[:start].count('\n')+1,
                           'source_offset_start': start, 'source_offset_end': end,
                           'source_byte_start': len(source[:start].encode()), 'source_byte_end': len(source[:end].encode()),
                           'source_old': rawold, 'old': old, 'new': new, 'expected_match_count': 1,
                           'kind': 'equation-tag pagination', 'original_content_unchanged': True,
                           'reason': 'Keep the unchanged standalone equation number(76) and its immediately following complete sphere sketch in one local samepage group. Only page-break penalties change; all coordinates, strokes, typography, words, and source marks are retained. The following explanatory prose remains outside the group.'})
        for form in (0, 1, 2):
            tex = OUT / f'scan573_tag76_bound_{language}_{form}.tex'
            parts = [build_readers.preamble(language, form), r'\begin{document}\LMcote{140-2}']
            for label, body in [('BEFORE', old), ('AFTER', new)]:
                parts += [r'\clearpage\noindent '+label+r' constrained-foot probe.\par',
                          r'\vspace*{\dimexpr\textheight-58pt\relax}\par\penalty0', body,
                          r'\par Following explanation.']
            parts.append(r'\end{document}')
            tex.write_text('\n'.join(parts))
            jobs.append((language, form, tex))
    (OUT / 'scan573_tag76_candidate.json').write_text(json.dumps(candidates, ensure_ascii=False, indent=2)+'\n')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(run, jobs))
    report = {'status': 'PENDING_ACTUAL_VISUAL_REVIEW', 'candidate_file': 'work/layout_probes/scan573_tag76_candidate.json',
              'forms': results, 'source_files_unchanged': all(sha(ROOT / r['source_path']) == r['source_sha256'] for r in candidates),
              'shared_dependencies_modified': False, 'observations_generated_by_script': False}
    (OUT / 'scan573_tag76_validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')


if __name__ == '__main__':
    main()
