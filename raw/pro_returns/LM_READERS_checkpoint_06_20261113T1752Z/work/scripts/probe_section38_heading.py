#!/usr/bin/env python3
"""Probe a prefix-only reservation before the existing C3:6 section 38 start.

Raw source and shared publication dependencies are never modified. The entire
heading and the first paragraph, including display (1), remain byte-identical
apart from the standard LF normalization used by the publication build.
"""
from pathlib import Path
import concurrent.futures
import hashlib
import json
import subprocess
import unicodedata

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
    proc = subprocess.run(['lualatex', '--no-shell-escape', '-interaction=nonstopmode',
                           '-halt-on-error', tex.name], cwd=OUT, env=environment(),
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    tex.with_suffix('.console.txt').write_text(proc.stdout)
    log = parse_log(tex.with_suffix('.log'))
    if proc.returncode:
        raise RuntimeError('Section38 probe failed: ' + tex.name)
    pdf = tex.with_suffix('.pdf')
    with fitz.open(pdf) as doc:
        hits = [(p.number + 1, b) for p in doc for b in p.search_for('38')]
        if len(hits) != 1:
            raise ValueError('Expected one section38 heading in ' + pdf.name)
        physical, box = hits[0]
        page = doc[physical - 1]
        plain = unicodedata.normalize('NFKC', page.get_text())
        native = tex.with_name(tex.stem + '_native.png')
        full = tex.with_name(tex.stem + '_full.png')
        page.get_pixmap(matrix=fitz.Matrix(3, 3),
                        clip=fitz.Rect(40, max(0, box.y0 - 25), page.rect.width,
                                       min(page.rect.height, box.y0 + 330)), alpha=False).save(native)
        page.get_pixmap(matrix=fitz.Matrix(900 / page.rect.width, 900 / page.rect.width),
                        alpha=False).save(full)
        terminal = 'de plus près' if language == 'fr' else 'more closely'
        row = {'language': language, 'form': form, 'pdf': rel(pdf), 'pdf_sha256': sha(pdf),
               'pages': len(doc), 'heading_page': physical, 'heading_bbox': list(box),
               'display_1_on_heading_page': '(1)' in plain,
               'opening_paragraph_terminal_phrase_on_heading_page': terminal in plain,
               'images': [{'path': rel(p), 'sha256': sha(p)} for p in (native, full)],
               'log': rel(tex.with_suffix('.log')), 'log_sha256': sha(tex.with_suffix('.log')),
               'compile_exit_code': proc.returncode, 'error_count': log['error_count'],
               'overfull_count': log['overfull_count'], 'missing_character_count': log['missing_character_count'],
               'status': 'PENDING_ACTUAL_VISUAL_REVIEW'}
    print(language, form, 'heading', physical, 'display', row['display_1_on_heading_page'],
          'paragraph', row['opening_paragraph_terminal_phrase_on_heading_page'],
          'errors', row['error_count'], 'overfull', row['overfull_count'],
          'missing', row['missing_character_count'], flush=True)
    return row


def main():
    candidates, jobs = [], []
    for language in ('fr', 'en'):
        package = 'LM_P059'
        path = ROOT / 'sources' / ('fr/texts' if language == 'fr' else 'en/packages') / (
            package + ('_en' if language == 'en' else '') + '.tex')
        source = path.read_bytes().decode('utf-8')
        start = source.index(r'\uline{38}\quad', source.index(r'\scanpage{6}'))
        following = "On a dans $" if language == 'fr' else 'We have in $'
        end = source.index(following, start)
        source_old = source[start:end]
        old = source_old.replace('\r\n', '\n')
        prefix = '\\Needspace{12\\baselineskip}\n'
        new = prefix + old
        assert new.removeprefix(prefix) == old
        candidates.append({'id': '140-3-6-H38', 'language': language, 'package': package,
                           'cote': '140-3', 'scan': 6, 'source_path': rel(path),
                           'source_sha256': sha(path), 'source_line': source[:start].count('\n') + 1,
                           'source_offset_start': start, 'source_offset_end': end,
                           'source_byte_start': len(source[:start].encode()),
                           'source_byte_end': len(source[:end].encode()), 'source_old': source_old,
                           'old': old, 'new': new, 'expected_match_count': 1,
                           'kind': 'section-heading pagination', 'original_content_unchanged': True,
                           'reason': 'Reserve twelve current baselines before this exact section38 heading so it starts with its opening paragraph and display(1). Preserve the whole heading, complete opening paragraph, all original mathematical tokens and source marks; do not box or restyle the paragraph.'})
        body, _, _ = editorial.annotate('\\scanpage{6}\n' + new, package, language)
        for form in (0, 1, 2):
            tex = OUT / f'section38_heading_{language}_{form}.tex'
            tex.write_text(build_readers.preamble(language, form) + '\n' +
                           r'\begin{document}\LMcote{140-3}' + '\n' +
                           r'\noindent Preceding body text.\par\vspace{\dimexpr\textheight-6\baselineskip\relax}' + '\n' +
                           body + '\n' + r'\end{document}')
            jobs.append((language, form, tex))
    candidate_path = OUT / 'section38_heading_candidate.json'
    candidate_path.write_text(json.dumps(candidates, ensure_ascii=False, indent=2) + '\n')
    before = json.loads((ROOT / 'work/visual_repair_proofs/revision512_section38/index.json').read_text())
    before['actual_classification'] = before['status']
    before['status'] = 'OPEN'
    before['candidate_file'] = rel(candidate_path)
    before['affected_languages'] = ['fr', 'en']
    before['final_rebuilt_closure_required'] = True
    (ROOT / 'work/data/section38_heading_before.json').write_text(json.dumps(before, ensure_ascii=False, indent=2) + '\n')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        rows = list(executor.map(run, jobs))
    report = {'status': 'PENDING_ACTUAL_VISUAL_REVIEW', 'forms': rows,
              'before_evidence': 'work/data/section38_heading_before.json',
              'candidate_file': rel(candidate_path),
              'source_files_unchanged': all(sha(ROOT / row['source_path']) == row['source_sha256'] for row in candidates),
              'shared_repair_module_modified': False, 'observations_generated_by_script': False}
    (OUT / 'section38_heading_validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    main()
