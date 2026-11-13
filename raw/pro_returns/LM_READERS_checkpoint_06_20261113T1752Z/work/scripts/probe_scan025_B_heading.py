#!/usr/bin/env python3
"""Prepare a paired source-local B) opening-group pagination repair and probes.

The immutable source and shared repair module are not modified. The existing
label, cancelled opening, surviving paragraph, words and marks are retained.
"""
from pathlib import Path
import concurrent.futures
import hashlib
import json
import re
import subprocess
import unicodedata

import fitz
import build_readers
import editorial
from texenv import environment
from verify_pdf import parse_log

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / 'work/layout_probes'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_job(job):
    language, form, tex = job
    result = subprocess.run(['lualatex', '--no-shell-escape', '-interaction=nonstopmode',
                             '-halt-on-error', tex.name], cwd=D, env=environment(),
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    tex.with_suffix('.console.txt').write_text(result.stdout)
    log = parse_log(tex.with_suffix('.log'))
    if result.returncode:
        raise RuntimeError('Heading probe failed: ' + tex.name)
    pdf = tex.with_suffix('.pdf')
    with fitz.open(pdf) as doc:
        hits = [(page.number + 1, box) for page in doc for box in page.search_for('B)')]
        if len(hits) != 1:
            raise ValueError('Expected one B) label in ' + pdf.name)
        page_number, box = hits[0]
        page = doc[page_number - 1]
        text = unicodedata.normalize('NFKC', page.get_text())
        complete = ('mixte' if language == 'fr' else 'mixed') in text
        native = D / f'scan025_B_heading_needspace_{language}_{form}_native.png'
        full = D / f'scan025_B_heading_needspace_{language}_{form}_full.png'
        page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=fitz.Rect(35, max(0, box.y0 - 25), 565, min(page.rect.height, box.y0 + 300)), alpha=False).save(native)
        page.get_pixmap(matrix=fitz.Matrix(900 / page.rect.width, 900 / page.rect.width), alpha=False).save(full)
        row = {'language': language, 'form': form, 'pdf': pdf.relative_to(ROOT).as_posix(), 'pdf_sha256': sha(pdf),
               'pages': len(doc), 'heading_page': page_number, 'heading_bbox': list(box),
               'surviving_paragraph_terminal_word_on_heading_page': complete,
               'images': [{'path': p.relative_to(ROOT).as_posix(), 'sha256': sha(p)} for p in (native, full)],
               'compile_exit_code': result.returncode, 'error_count': log['error_count'],
               'overfull_count': log['overfull_count'], 'missing_character_count': log['missing_character_count'],
               'log': tex.with_suffix('.log').relative_to(ROOT).as_posix(), 'log_sha256': sha(tex.with_suffix('.log')),
               'status': 'PENDING_ACTUAL_VISUAL_REVIEW'}
    print(language, form, 'heading page', page_number, 'paragraph terminal word', complete,
          'errors', log['error_count'], 'overfull', log['overfull_count'], 'missing', log['missing_character_count'], flush=True)
    return row


def main():
    candidates, jobs = [], []
    for language in ('fr', 'en'):
        package = 'LM_C1-020-037'
        path = ROOT / 'sources' / ('fr/texts' if language == 'fr' else 'en/packages') / (package + ('_en' if language == 'en' else '') + '.tex')
        raw = path.read_bytes()
        source = raw.decode('utf-8')
        scan_start = source.index(r'\scanpage{25}')
        start = source.index('B)', scan_start)
        end = source.index(r'\margin{24}', start)
        old_raw = source[start:end]
        old = old_raw.replace('\r\n', '\n')
        prefix = '\\Needspace{14\\baselineskip}\n'
        suffix = ''
        new = prefix + old + suffix
        assert new.removeprefix(prefix).removesuffix(suffix) == old
        candidates.append({'id': '140-1-25-HB', 'language': language, 'package': package, 'cote': '140-1', 'scan': 25,
                           'source_path': path.relative_to(ROOT).as_posix(), 'source_sha256': sha(path),
                           'source_line': source[:start].count('\n') + 1,
                           'source_offset_start': start, 'source_offset_end': end,
                           'source_byte_start': len(source[:start].encode()), 'source_byte_end': len(source[:end].encode()),
                           'source_old': old_raw, 'old': old, 'new': new, 'expected_match_count': 1,
                           'kind': 'section-heading pagination',
                           'reason': 'Reserve fourteen current baselines before this existing B) opening, so the label stays with the cancelled opening and first surviving paragraph in all three edition forms. Preserve normal outer editorial mode, all paragraph style, type size and linewidth. No source word, mathematical token, uncertainty or deletion wrapper changes.',
                           'original_content_unchanged': True})
        body, _, _ = editorial.annotate(r'\scanpage{25}' + '\n' + new + r'\margin{24}' + '\n', package, language)
        for form in (0, 1, 2):
            tex = D / f'scan025_B_heading_needspace_{language}_{form}.tex'
            text = (build_readers.preamble(language, form) + '\n' +
                    r'\begin{document}\LMcote{140-1}' + '\n' +
                    r'\vspace*{\dimexpr\textheight-4\baselineskip\relax}' + '\n' + body + '\n' + r'\end{document}')
            tex.write_text(text)
            jobs.append((language, form, tex))
    (D / 'scan025_B_heading_candidate.json').write_text(json.dumps(candidates, ensure_ascii=False, indent=2) + '\n')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        rows = list(executor.map(run_job, jobs))
    report = {'status': 'PENDING_ACTUAL_VISUAL_REVIEW', 'forms': rows,
              'before_evidence': 'work/visual_repair_proofs/revision512_B_heading/index.json',
              'candidate_file': 'work/layout_probes/scan025_B_heading_candidate.json',
              'source_files_unchanged': all(sha(ROOT / r['source_path']) == r['source_sha256'] for r in candidates),
              'shared_repair_module_modified': False, 'observations_generated_by_script': False}
    (D / 'scan025_B_heading_validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    main()
