#!/usr/bin/env python3
"""Probe an exact unchanged tag+map-name+diagram binding at C3:590 (60)."""
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
    proc = subprocess.run(['lualatex', '--no-shell-escape', '-interaction=nonstopmode', '-halt-on-error', tex.name],
                          cwd=OUT, env=environment(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    tex.with_suffix('.console.txt').write_text(proc.stdout)
    log = parse_log(tex.with_suffix('.log'))
    if proc.returncode:
        raise RuntimeError('Tag60 probe failed: ' + tex.name)
    pdf = tex.with_suffix('.pdf')
    with fitz.open(pdf) as doc:
        hits = [(p.number + 1, box) for p in doc for box in p.search_for('(60)')]
        assert len(hits) == 1
        physical, box = hits[0]
        page = doc[physical - 1]
        native = tex.with_name(tex.stem + '_native.png')
        page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=fitz.Rect(40, max(0, box.y0 - 25), page.rect.width, min(page.rect.height, box.y0 + 280)), alpha=False).save(native)
        plain = unicodedata.normalize('NFKC', page.get_text())
        row = {'language': language, 'form': form, 'pdf': rel(pdf), 'pdf_sha256': sha(pdf),
               'pages': len(doc), 'tag_page': physical, 'diagram_terminal_beta_on_tag_page': 'β' in plain,
               'image': rel(native), 'image_sha256': sha(native), 'log': rel(tex.with_suffix('.log')),
               'log_sha256': sha(tex.with_suffix('.log')), 'compile_exit_code': proc.returncode,
               'error_count': log['error_count'], 'overfull_count': log['overfull_count'],
               'missing_character_count': log['missing_character_count'], 'status': 'PENDING_ACTUAL_VISUAL_REVIEW'}
    print(language, form, 'tag page', physical, 'terminal beta', row['diagram_terminal_beta_on_tag_page'],
          'errors', row['error_count'], 'overfull', row['overfull_count'], 'missing', row['missing_character_count'], flush=True)
    return row


def main():
    candidates, jobs = [], []
    for language in ('fr', 'en'):
        package = 'LM_C3-587-605'
        source_path = ROOT / 'sources' / ('fr/texts' if language == 'fr' else 'en/packages') / (package + ('_en' if language == 'en' else '') + '.tex')
        source = source_path.read_text()
        start = source.index('$(60)\\quad A:$', source.index(r'\scanpage{590}'))
        end = source.index(r'\end{tikzcd}}', start) + len(r'\end{tikzcd}}')
        old = source[start:end]
        new = '\\begin{samepage}\n' + old + '\n\\end{samepage}'
        margin_start = source.index(r'\margin{', end)
        margin_end = source.index('}', margin_start) + 1
        following_margin = source[margin_start:margin_end]
        candidates.append({'id': '140-3-590-K60A', 'language': language, 'package': package, 'cote': '140-3', 'scan': 590,
                           'tag': '60', 'map_name': 'A:', 'source_path': rel(source_path), 'source_sha256': sha(source_path),
                           'source_line': source[:start].count('\n') + 1, 'source_offset_start': start, 'source_offset_end': end,
                           'source_byte_start': len(source[:start].encode()), 'source_byte_end': len(source[:end].encode()),
                           'old': old, 'new': new, 'expected_match_count': 1, 'original_content_unchanged': True,
                           'following_margin_unchanged_outside_binding': following_margin,
                           'kind': 'tagged introduction pagination',
                           'reason': 'Keep the unchanged equation tag (60), map name A:, and its immediately following full diagram together using samepage break penalties. Preserve every mathematical token and source wrapper; the following margin remains outside the binding with its original flow.'})
        body, _, _ = editorial.annotate('\\scanpage{590}\n' + new + '\n' + following_margin + '\n', package, language)
        for form in (0, 1, 2):
            tex = OUT / f'scan590_tag60_bound_{language}_{form}.tex'
            tex.write_text(build_readers.preamble(language, form) + '\n' + r'\begin{document}\LMcote{140-3}' + '\n' +
                           r'\noindent Preceding body text.\par\vspace{\dimexpr\textheight-6\baselineskip\relax}' + '\n' + body + '\n' + r'\end{document}')
            jobs.append((language, form, tex))
    (OUT / 'scan590_tag60_candidate.json').write_text(json.dumps(candidates, ensure_ascii=False, indent=2) + '\n')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        rows = list(executor.map(run, jobs))
    report = {'status': 'PENDING_ACTUAL_VISUAL_REVIEW', 'forms': rows,
              'before_evidence': 'work/data/scan590_tag60_before.json',
              'candidate_file': 'work/layout_probes/scan590_tag60_candidate.json',
              'source_files_unchanged': all(sha(ROOT / r['source_path']) == r['source_sha256'] for r in candidates),
              'shared_repair_module_modified': False, 'observations_generated_by_script': False}
    (OUT / 'scan590_tag60_validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    main()
