#!/usr/bin/env python3
"""Probe the source-local first arrow of C3:55 equation (3), without source edits."""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

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


def main():
    records = []
    jobs = []
    for language, source_path in [('fr', ROOT / 'sources/fr/texts/LM_P064.tex'),
                                  ('en', ROOT / 'sources/en/packages/LM_P064_en.tex')]:
        text = source_path.read_text()
        needle = r'\widehat{\varphi}:\widehat{\Pi}_{0,3}'
        assert text.count(needle) == 1
        pos = text.index(needle)
        start = text.rfind(r'\begin{tikzcd}', 0, pos)
        end = text.index(r'\end{tikzcd}', pos) + len(r'\end{tikzcd}')
        old = text[start:end]
        word = 'épi' if language == 'fr' else 'epimorphism'
        arrow_old = '\\arrow[r,"\\text{' + word + '}"]'
        arrow_new = '\\arrow[r,"{\\text{' + word + '}}"{yshift=2pt}]'
        assert old.count(arrow_old) == 1
        new = old.replace(arrow_old, arrow_new)
        column_old = r'\& \widehat{\mathfrak S}_{0,3}^{+}'
        column_new = r'\&[4em] \widehat{\mathfrak S}_{0,3}^{+}'
        assert new.count(column_old) == 1
        new = new.replace(column_old, column_new)
        records.append({'id': '140-3-55-E3', 'language': language, 'package': 'LM_P064',
                        'cote': '140-3', 'scan': 55, 'tag': '3',
                        'source_path': rel(source_path), 'source_sha256': sha(source_path),
                        'source_line': text[:start].count('\n') + 1,
                        'source_offset_start': start, 'source_offset_end': end,
                        'source_byte_start': len(text[:start].encode()),
                        'source_byte_end': len(text[:end].encode()),
                        'old': old, 'new': new, 'expected_match_count': 1,
                        'kind': 'Local diagram label clearance',
                        'reason': 'Add 4em only to the first intercolumn gap and raise only its epimorphism label by 2pt. This separates the English label from the target hat, plus accent, and terminal arrow barb. Preserve every object, arrow, word, mathematical symbol, and editorial wrapper; equation (1) is untouched.',
                        'final_full_book_confirmation': 'PENDING_REBUILD_AND_ACTUAL_PAGE_REVIEW'})
        parts = [build_readers.preamble(language, 0), r'\begin{document}\LMcote{140-3}']
        for form in (0, 1, 2):
            for phase in ('old', 'new'):
                source = '\\scanpage{55}\n\\[\n(3)\\qquad\\diagram{' + (old if phase == 'old' else new) + '}\n\\]\n'
                body, _, _ = editorial.annotate(source, 'LM_P064', language)
                parts += [r'\clearpage', f'\\LMform={form}', body]
        parts.append(r'\end{document}')
        tex = OUT / f'scan055_epimorphism_{language}.tex'
        tex.write_text('\n'.join(parts))
        process = subprocess.Popen(['lualatex', '--no-shell-escape', '-interaction=nonstopmode',
                                    '-halt-on-error', tex.name], cwd=OUT, env=environment(),
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        jobs.append((language, tex, process))
    (OUT / 'scan055_epimorphism_candidate.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
    forms = []
    for language, tex, process in jobs:
        console, _ = process.communicate()
        tex.with_suffix('.console.txt').write_text(console)
        log = parse_log(tex.with_suffix('.log'))
        if process.returncode:
            raise RuntimeError('Source-specific epimorphism probe failed for ' + language)
        with fitz.open(tex.with_suffix('.pdf')) as doc:
            assert len(doc) == 6
            for index, page in enumerate(doc):
                form, phase = index // 2, 'before' if index % 2 == 0 else 'after'
                picture = OUT / f'scan055_epimorphism_{language}_{form}_{phase}.png'
                page.get_pixmap(matrix=fitz.Matrix(4, 4), clip=fitz.Rect(50, 65, 555, 225), alpha=False).save(picture)
                forms.append({'language': language, 'form': form, 'phase': phase,
                              'pdf': rel(tex.with_suffix('.pdf')), 'pdf_sha256': sha(tex.with_suffix('.pdf')),
                              'physical_page': index + 1, 'image': rel(picture), 'image_sha256': sha(picture),
                              'log': rel(tex.with_suffix('.log')), 'log_sha256': sha(tex.with_suffix('.log')),
                              'compile_exit_code': process.returncode, 'error_count': log['error_count'],
                              'overfull_count': log['overfull_count'], 'missing_character_count': log['missing_character_count'],
                              'status': 'PENDING_ACTUAL_VISUAL_REVIEW'})
        print(language, 'six before/after form pages', log['error_count'], log['overfull_count'], log['missing_character_count'], flush=True)
    for row in records:
        assert sha(ROOT / row['source_path']) == row['source_sha256']
    validation = {'status': 'PENDING_ACTUAL_VISUAL_REVIEW', 'forms': forms,
                  'candidate_file': 'work/layout_probes/scan055_epimorphism_candidate.json',
                  'source_files_unchanged': True, 'shared_repair_module_modified': False,
                  'before_full_book_evidence': 'work/visual_repair_proofs/release512_findings/enapp570_epimorphism_1_10x.png',
                  'observations_generated_by_script': False}
    (OUT / 'scan055_epimorphism_validation.json').write_text(json.dumps(validation, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    main()
