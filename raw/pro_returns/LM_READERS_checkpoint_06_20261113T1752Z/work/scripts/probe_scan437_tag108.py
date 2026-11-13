#!/usr/bin/env python3
"""Probe an unchanged tagged introduction and its three maps at C3:437 (108)."""
from pathlib import Path
import concurrent.futures
import hashlib
import json
import subprocess
import fitz
import build_readers
import editorial
from texenv import environment
from verify_pdf import parse_log

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'work/layout_probes'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rel(path):
    return path.relative_to(ROOT).as_posix()


def run(job):
    language, form, tex = job
    proc = subprocess.run(['lualatex', '--no-shell-escape', '-interaction=nonstopmode', '-halt-on-error', tex.name],
                          cwd=OUT, env=environment(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    tex.with_suffix('.console.txt').write_text(proc.stdout)
    log = parse_log(tex.with_suffix('.log'))
    if proc.returncode:
        raise RuntimeError('Tag108 probe failed: ' + tex.name)
    pdf = tex.with_suffix('.pdf')
    with fitz.open(pdf) as doc:
        hits = [(p.number + 1, box) for p in doc for box in p.search_for('(108)')]
        assert len(hits) == 1
        physical, box = hits[0]
        page = doc[physical - 1]
        native = tex.with_name(tex.stem + '_native.png')
        page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=fitz.Rect(40, max(0, box.y0 - 25), page.rect.width, min(page.rect.height, box.y0 + 330)), alpha=False).save(native)
        row = {'language': language, 'form': form, 'pdf': rel(pdf), 'pdf_sha256': sha(pdf),
               'pages': len(doc), 'tag_page': physical, 'image': rel(native), 'image_sha256': sha(native),
               'log': rel(tex.with_suffix('.log')), 'log_sha256': sha(tex.with_suffix('.log')),
               'compile_exit_code': proc.returncode, 'error_count': log['error_count'],
               'overfull_count': log['overfull_count'], 'missing_character_count': log['missing_character_count'],
               'status': 'PENDING_ACTUAL_VISUAL_REVIEW'}
    print(language, form, 'tag page', physical, 'errors', row['error_count'], 'overfull', row['overfull_count'], 'missing', row['missing_character_count'], flush=True)
    return row


def main():
    candidates, jobs = [], []
    for language in ('fr', 'en'):
        package = 'LM_C3-435-453'
        source_path = ROOT / 'sources' / ('fr/texts' if language == 'fr' else 'en/packages') / (package + ('_en' if language == 'en' else '') + '.tex')
        source = source_path.read_text()
        start = source.index(r'\noindent(108)', source.index(r'\scanpage{437}'))
        end = source.index(r'\mspage{436}', start)
        while source[end - 1].isspace():
            end -= 1
        old = source[start:end]
        assert old.count(r'\diagram{') == 2
        assert old.count(r'\arrow[') == 3
        new = '\\begin{samepage}\n' + old + '\n\\end{samepage}'
        candidates.append({'id': '140-3-437-K108INTRO', 'language': language, 'package': package, 'cote': '140-3', 'scan': 437,
                           'tag': '108', 'source_path': rel(source_path), 'source_sha256': sha(source_path),
                           'source_line': source[:start].count('\n') + 1, 'source_offset_start': start, 'source_offset_end': end,
                           'source_byte_start': len(source[:start].encode()), 'source_byte_end': len(source[:end].encode()),
                           'old': old, 'new': new, 'expected_match_count': 1, 'original_content_unchanged': True,
                           'kind': 'tagged introduction pagination',
                           'reason': 'Keep the unchanged equation tag (108), its group-name introduction, and the two immediately following diagrams (three labeled maps) together using samepage break penalties. Preserve every word, mathematical token, source wrapper, and both separating commas; manuscript page marker and subsequent scan remain outside.'})
        body, _, _ = editorial.annotate('\\scanpage{437}\n' + new + '\n\\mspage{436}\n', package, language)
        for form in (0, 1, 2):
            tex = OUT / f'scan437_tag108_bound_{language}_{form}.tex'
            tex.write_text(build_readers.preamble(language, form) + '\n' + r'\begin{document}\LMcote{140-3}' + '\n' +
                           r'\noindent Preceding body text.\par\vspace{\dimexpr\textheight-6\baselineskip\relax}' + '\n' + body + '\n' + r'\end{document}')
            jobs.append((language, form, tex))
    (OUT / 'scan437_tag108_candidate.json').write_text(json.dumps(candidates, ensure_ascii=False, indent=2) + '\n')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        rows = list(executor.map(run, jobs))
    report = {'status': 'PENDING_ACTUAL_VISUAL_REVIEW', 'forms': rows,
              'before_evidence': 'work/data/scan437_tag108_before.json',
              'candidate_file': 'work/layout_probes/scan437_tag108_candidate.json',
              'source_files_unchanged': all(sha(ROOT / r['source_path']) == r['source_sha256'] for r in candidates),
              'shared_repair_module_modified': False, 'observations_generated_by_script': False}
    (OUT / 'scan437_tag108_validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    main()
